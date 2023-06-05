# Author: James Bennett, Student ID: 009454560

from datetime import datetime

from helper import *
from Hash import ChainingHashTable
from Truck import *


def get_package_data():
    # Fetch data from Hash Table
    for i in range(0, 40):
        print("Key: {} Package info: {}".format(i + 1, my_hash.search(i + 1)))


def find_route(truck, distance_data):
    # Logic for delivering first package
    while True:

        # Set start times and first address to visit for trucks
        if truck.get_truck_id() == 1:
            start_time = "08:00:00"
            first_address = "4580 S 2300 E"
            # Set package statuses after leaving hub
            for p in truck1.get_packages():
                p.set_status("En route")

        if truck.get_truck_id() == 2:
            start_time = "09:15:00"
            first_address = "5383 S 900 East #104"
            # Set package statuses after leaving hub
            for p in truck2.get_packages():
                p.set_status("En route")

        if truck.get_truck_id() == 3:
            start_time = "10:18:00"
            first_address = "2530 S 500 E"
            # Set package statuses after leaving hub
            for p in truck3.get_packages():
                p.set_status("En route")

        # Add mileage to truck for distance to travel to nearest_address
        # truck.set_mileage(truck.get_mileage() + min(address_distances))
        mileage_to_first_address = distance_data[first_address][0]
        truck.set_mileage(mileage_to_first_address)
        time_delivered = calculate_trip_time(start_time, mileage_to_first_address)

        break

    # Find package associated with the first address and set attributes
    for p in truck.get_packages():
        # If first_address matches package address:
        if p.get_address() == first_address:
            # Update delivery_time, status of package, and truck's last delivery time/location
            deliver_package(truck, p, first_address, time_delivered)

    # Logic for delivering packages with deadlines first
    address_distances = []
    address_indexes = {}
    keys = distance_data.keys()
    count = 0
    for j in keys:
        address_indexes[j] = count
        count += 1

    # Create addresses_with_deadlines list and populate it with addresses for all packages on the truck
    # that haven’t been delivered and have a delivery_deadline other than End of Day (EOD)
    addresses_with_deadlines = [x.get_address() for x in truck.get_packages()
                                if x.get_deadline() != "EOD"
                                and x.get_status() != "Delivered"]

    # Clear the address_distances list
    address_distances.clear()

    # Set the starting time to time of the truck’s last delivered package
    time = truck.get_last_delivered_package_time()

    # Create datetime time object from start time string
    current_time = datetime.strptime(time, '%I:%M:%S').time()

    # Create datetime time object for 10:20:00
    ten_twenty = datetime.strptime("10:20:00", '%I:%M:%S').time()


    # Populate address_distances with distances between starting address
    # and all addresses in addresses_with_deadlines list
    # address_distances = calculate_distances_between_addresses(starting_address, addresses_with_deadlines,
    #                                  distance_data, address_indexes)

    # If address_distances isn't empty
    while len(addresses_with_deadlines) > 0:

        # Set the starting address to the truck’s current location
        starting_address = truck.get_location()
        # Create addresses_with_deadlines list and populate it with addresses for all packages on the truck
        # that haven’t been delivered and have a delivery_deadline other than End of Day (EOD)
        addresses_with_deadlines = [x.get_address() for x in truck.get_packages()
                                    if x.get_deadline() != "EOD"
                                    and x.get_status() != "Delivered"]
        if len(addresses_with_deadlines) == 0:
            continue

        nearest_address_data = find_nearest_address(starting_address, addresses_with_deadlines,
                                                    distance_data, address_indexes)
        print("\tNearest_address_data: " + str(nearest_address_data[0]) + " " + str(nearest_address_data[1]))
        print()
        nearest_address = nearest_address_data[0]
        nearest_address_mileage = nearest_address_data[1]

        # Add mileage to travel to the nearest address
        truck.set_mileage(truck.get_mileage() + nearest_address_mileage)

        # Calculate the trip time from the truck’s location to the nearest_address and
        # store it into a time_delivered variable
        time_delivered = calculate_trip_time(truck.get_last_delivered_package_time(), nearest_address_mileage)

        # For all packages with an address == nearest_address
        for k in truck.get_packages():

            if k.get_address() == nearest_address:
                # Check if the Package ID is 9 and the time is >= 10:20am
                # If so, set Package #9 address and deliver it
                if k.get_package_id() == 9 and current_time >= ten_twenty:
                    deliver_package(truck, k, nearest_address, time_delivered)

                else:
                    # If the package is Package #9 but it’s not >= 10:20am
                    if k.get_package_id() == 9:
                        continue
                    # If not package #9, deliver the package(s)
                    deliver_package(truck, k, nearest_address, time_delivered)

    # Logic for all remaining packages where package.get_status() isn't "Delivered"
    # (until no more packages to deliver)

    # Populate addresses_to_check list with the remaining addresses of packages on the truck
    # that haven’t been delivered
    addresses_to_check = [x.get_address() for x in truck.get_packages() if x.get_status() != "Delivered"]

    while len(addresses_to_check) > 0:

        # Set the starting address to the truck’s current location
        starting_address = truck.get_location()

        # Populate addresses_to_check list with the remaining addresses of packages on the truck
        # that haven’t been delivered
        addresses_to_check = [x.get_address() for x in truck.get_packages() if x.get_status() != "Delivered"]

        # Clear the address_distances list
        address_distances.clear()

        # Populate the address_distances list with distances between the starting address
        # and each address in addresses_to_check
        # address_distances = calculate_distances_between_addresses(starting_address, addresses_to_check,
        #        distance_data, address_indexes)

        # If the address_distances list isn't empty
        # if len(address_distances) > 0:
        # Set nearest_address to the address that corresponds with the minimum value in address_distances
        # nearest_address = addresses_to_check[address_distances.index(min(address_distances))]

        if len(addresses_to_check) == 0:
            if truck.get_truck_id() == 2 or truck.get_truck_id() == 3:
                truck.set_end_route_time(truck.get_last_delivered_package_time())
                continue
            # Set the starting address to the truck’s current location
            starting_address = truck.get_location()

            # Determine the mileage back to the hub and add it to the truck’s current mileage
            truck.set_mileage(truck.get_mileage() + distance_data[starting_address][0])
            print(str(truck.get_truck_id()) + " distance to the hub: " + str(distance_data[starting_address][0]))
            #
            # Calculate the trip time from the truck’s location to the hub
            # and set the truck’s end of route time equal to the time calculated
            truck.set_end_route_time(calculate_trip_time(truck.get_last_delivered_package_time(),
                                                         distance_data[starting_address][0]))

            continue
        nearest_address_data = find_nearest_address(starting_address, addresses_to_check,
                                                    distance_data, address_indexes)
        print("\tNearest_address_data: " + str(nearest_address_data[0]) + " " + str(nearest_address_data[1]))
        print()
        nearest_address = nearest_address_data[0]
        nearest_address_mileage = nearest_address_data[1]

        # Add mileage to travel to the nearest address
        truck.set_mileage(truck.get_mileage() + nearest_address_mileage)

        # Calculate the trip time from the truck’s location to the nearest_address
        # and store it into a time_delivered variable
        time_delivered = calculate_trip_time(truck.get_last_delivered_package_time(), nearest_address_mileage)

        # For all packages with an address == nearest_address
        for pkg in truck.get_packages():
            if pkg.get_address() == nearest_address:
                # Update delivery_time, status of package, and truck's last delivery time/location
                deliver_package(truck, pkg, nearest_address, time_delivered)


def load_trucks(t1, t2, t3):
    t1.packages.append(my_hash.search(14))
    t1.packages.append(my_hash.search(16))
    t1.packages.append(my_hash.search(13))
    t1.packages.append(my_hash.search(19))
    t1.packages.append(my_hash.search(15))
    t1.packages.append(my_hash.search(20))
    t1.packages.append(my_hash.search(21))
    t1.packages.append(my_hash.search(26))
    t1.packages.append(my_hash.search(34))
    t1.packages.append(my_hash.search(28))
    t1.packages.append(my_hash.search(1))
    t1.packages.append(my_hash.search(11))
    t1.packages.append(my_hash.search(4))
    t1.packages.append(my_hash.search(40))
    t1.packages.append(my_hash.search(39))

    t2.packages.append(my_hash.search(3))
    t2.packages.append(my_hash.search(18))
    t2.packages.append(my_hash.search(36))
    t2.packages.append(my_hash.search(38))
    t2.packages.append(my_hash.search(37))
    t2.packages.append(my_hash.search(31))
    t2.packages.append(my_hash.search(32))
    t2.packages.append(my_hash.search(6))
    t2.packages.append(my_hash.search(5))
    t2.packages.append(my_hash.search(9))
    t2.packages.append(my_hash.search(8))
    t2.packages.append(my_hash.search(30))
    t2.packages.append(my_hash.search(12))
    t2.packages.append(my_hash.search(17))
    t2.packages.append(my_hash.search(25))
    t2.packages.append(my_hash.search(29))

    t3.packages.append(my_hash.search(27))
    t3.packages.append(my_hash.search(35))
    t3.packages.append(my_hash.search(10))
    t3.packages.append(my_hash.search(24))
    t3.packages.append(my_hash.search(2))
    t3.packages.append(my_hash.search(33))
    t3.packages.append(my_hash.search(7))
    t3.packages.append(my_hash.search(23))
    t3.packages.append(my_hash.search(22))


if __name__ == '__main__':
    # Hash table instance
    my_hash = ChainingHashTable()

    # Load packages to Hash Table
    load_package_data('package_data.csv', my_hash)

    # Create truck objects and load them
    truck1 = Truck(1)
    truck2 = Truck(2)
    truck3 = Truck(3)
    load_trucks(truck1, truck2, truck3)

    # Load address and distance data from csv file into lists
    distance_data = load_distance_data('distances.csv')

    # Find routes for trucks
    find_route(truck1, distance_data)
    find_route(truck2, distance_data)
    find_route(truck3, distance_data)

    # Calculate total mileage for all three trucks after routes are complete
    total_mileage = truck1.get_mileage() + truck2.get_mileage() + truck3.get_mileage()
    total_mileage_rounded = round(total_mileage, 2)

    # print()
    # print("Total mileage: " + str(total_mileage_rounded))

    # CLI logic
    print()
    print("WGUPS Routing System")
    print("0: Exit")
    print("1: Enter a time to view status of all packages")
    print("2: View total mileage of all trucks after routes have been completed")
    print("3: View delivery report for packages with delivery deadlines")
    print()



    choice = input("Please enter a number for your selection: ")

    if choice == str(1):
        time = input("Please enter a time in the format mm:hh using 24 hour time (i.e. 15:00 for 3:00pm): ")

        packages = []
        trucks = [truck1, truck2, truck3]
        for i in range(0, 40):
            packages.append(my_hash.search(i + 1))
        print("Package statuses at " + time + ":")

        get_delivery_status_at_time(packages, time, trucks)

    if choice == str(2):
        print("Truck 1 mileage: " + str(round(truck1.get_mileage(), 2)))
        print("Truck 2 mileage: " + str(round(truck2.get_mileage(), 2)))
        print("Truck 3 mileage: " + str(round(truck3.get_mileage(), 2)))
        print("Total mileage: " + str(total_mileage_rounded))
        print(truck1.get_end_route_time())
        print(truck2.get_end_route_time())
        print(truck3.get_end_route_time())

    if choice == str(3):
        get_packages_with_deadlines_data([truck1, truck2, truck3])
