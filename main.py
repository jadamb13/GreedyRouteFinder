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


    # Logic for delivering first package #
    while True:
        first_address_data = send_truck_to_first_address(truck)
        first_address = first_address_data[0]
        start_time = first_address_data[1]

        # Add mileage to truck for distance to travel to nearest_address
        mileage_to_first_address = distance_data[first_address][0]
        truck.set_mileage(mileage_to_first_address)
        time_delivered = calculate_trip_time(start_time, mileage_to_first_address)
        break

    # Find package associated with the first address and deliver
    for p in truck.get_packages():
        # If first_address matches package address:
        if p.get_address() == first_address:
            set_attributes_on_delivery(truck, p, first_address, time_delivered)

    # Logic for delivering packages with deadlines first #

    # Dictionary to map index values to addresses from distance table
    address_indexes = {}
    keys = distance_data.keys()
    count = 0
    for j in keys:
        address_indexes[j] = count
        count += 1

    # Create addresses_with_deadlines list and populate it with addresses of undelivered packages with deadlines
    addresses_with_deadlines = [x.get_address() for x in truck.get_packages()
                                if x.get_deadline() != "EOD"
                                and x.get_status() != "Delivered"]

    # If address_distances isn't empty
    while len(addresses_with_deadlines) > 0:

        # Set the starting address to the truck’s current location
        starting_address = truck.get_location()

        # List of packages that haven’t been delivered and have a delivery_deadline other than End of Day (EOD)
        addresses_with_deadlines = [x.get_address() for x in truck.get_packages()
                                    if x.get_deadline() != "EOD"
                                    and x.get_status() != "Delivered"]

        # If all packages with deadlines have been delivered, exit while loop
        if len(addresses_with_deadlines) == 0:
            continue

        # Find the nearest address and distance to that address | Returns: [address, distance]
        nearest_address_data = find_nearest_address(starting_address, addresses_with_deadlines,
                                                    distance_data, address_indexes)
        # Deliver packages to the nearest address
        deliver_packages(truck, nearest_address_data)

    # Logic for delivering remaining packages #

    # List with the remaining addresses of packages on the truck that haven’t been delivered
    addresses_to_check = [x.get_address() for x in truck.get_packages() if x.get_status() != "Delivered"]

    # Until no more packages are left
    while len(addresses_to_check) > 0:

        # Set the starting address to the truck’s current location
        starting_address = truck.get_location()

        # Repopulate the addresses_to_check list after packages have been delivered each loop
        addresses_to_check = [x.get_address() for x in truck.get_packages() if x.get_status() != "Delivered"]

        if len(addresses_to_check) == 0:
            if truck.get_truck_id() == 2 or truck.get_truck_id() == 3:
                truck.set_end_route_time(truck.get_last_delivered_package_time())
                continue

            # Set the starting address to the truck’s current location
            starting_address = truck.get_location()

            # Determine the mileage back to the hub and add it to the truck’s current mileage
            truck.set_mileage(truck.get_mileage() + distance_data[starting_address][0])

            # Calculate the trip time from the truck’s location to the hub
            # and set the truck’s end of route time equal to the time calculated
            truck.set_end_route_time(calculate_trip_time(truck.get_last_delivered_package_time(),
                                                         distance_data[starting_address][0]))
            continue
        nearest_address_data = find_nearest_address(starting_address, addresses_to_check,
                                                    distance_data, address_indexes)

        # Deliver all packages with an address == nearest_address
        deliver_packages(truck, nearest_address_data)


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

        print()
        header = "Package statuses at " + time
        print(header.center(120))
        print("-" * 130)
        print("%-5s %-68s %-10s %-13s %-15s %s" %
              ("ID", "Address".center(30), "Weight".center(6),
               "Deadline".center(12), "Status".center(13), "Delivery Time".center(15)))
        print("-" * 130)
        get_delivery_status_at_time(packages, time, trucks)

    if choice == str(2):
        print("Truck 1 mileage: " + str(round(truck1.get_mileage(), 2)))
        print("Truck 2 mileage: " + str(round(truck2.get_mileage(), 2)))
        print("Truck 3 mileage: " + str(round(truck3.get_mileage(), 2)))
        print("Total mileage: " + str(total_mileage_rounded))

    if choice == str(3):
        get_packages_with_deadlines_data([truck1, truck2, truck3])
