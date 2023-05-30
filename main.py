from datetime import datetime, timedelta, date
from random import randrange
from time import strftime

from Hash import ChainingHashTable
from Package import *
from Truck import *


def get_package_data():
    # Fetch data from Hash Table
    for i in range(0, 40):
        print("Key: {} Package info: {}".format(i + 1, my_hash.search(i + 1)))


def find_route(truck, distance_data):
    address_distances = []

    # Logic for delivering first package
    while True:

        # Set start times and first address to visit for trucks
        if truck.get_truck_id() == 1:
            start_time = "08:00:00"
            first_address = "4580 S 2300 E"
        if truck.get_truck_id() == 2:
            start_time = "09:15:00"
            first_address = "5383 S 900 East #104"
        if truck.get_truck_id() == 3:
            start_time = "10:18:00"
            first_address = "2530 S 500 E"

        # Populate list with addresses for all packages on truck
        addresses_to_check = [x.get_address() for x in truck.get_packages()]
        for i in addresses_to_check:
            address_distances.append(distance_data[i][0])

        # Randomly select first address to start [TESTING]
        # nearest_address = addresses_to_check[address_distances.index(min(address_distances))]
        #random_start_index = randrange(1, len(addresses_to_check) - 1)
        # print("Random start index: " + str(random_start_index))
        #first_address = addresses_to_check[random_start_index]


        # Add mileage to truck for distance to travel to nearest_address
        # truck.set_mileage(truck.get_mileage() + min(address_distances))
        mileage_to_first_address = address_distances[addresses_to_check.index(first_address)]
        truck.set_mileage(truck.get_mileage() + mileage_to_first_address)

        # Ratio of total miles traveled in an hour to miles traveled to nearest address
        # mileage_ratio = 18 / min(address_distances)
        mileage_ratio = 18 / mileage_to_first_address
        minutes_to_add = 60 / mileage_ratio

        # Create datetime time object from start time string
        time_object = datetime.strptime(start_time, '%I:%M:%S').time()

        # Use time_object and timedelta to create new_time object to represent delivery time
        # datetime.combine() and timedelta() adapted from:
        # https://bobbyhadz.com/blog/python-add-minutes-to-datetime
        new_time = (datetime.combine(date.today(), time_object) + timedelta(seconds=minutes_to_add * 60)).time()

        # Convert new_time time object into string to store in Package attribute -> delivery_time
        time_delivered = new_time.strftime("%I:%M:%S")

        break

    # Find package associated with the first address and set attributes
    for i in truck.get_packages():
        # If first_address matches package address:
        # set package status and delivery time
        # set truck's location to first_address and set truck's last_delivery_time
        if i.get_address() == first_address:
            # Update delivery_time, status of package, and truck's last delivery time
            i.set_status("Delivered")
            i.set_delivery_time(time_delivered)
            truck.set_last_delivered_package_time(time_delivered)
            truck.set_location(first_address)
    addresses_to_check.remove(first_address)
    package_nine_address = "410 S State St"
    # Logic for delivering packages with deadlines first
    addresses_with_deadlines = [x.get_address() for x in truck.get_packages()
                                if x.get_deadline() != "EOD"
                                and x.get_status() != "Delivered"
                                and x.get_package_id() != 9]


    while len(addresses_with_deadlines) > 0:
        address_distances.clear()
        starting_address = truck.get_location()

        # Create datetime time object from start time string
        time = truck.get_last_delivered_package_time()
        current_time_object = datetime.strptime(time, '%I:%M:%S').time()

        # Create datetime time object for 10:20:00
        ten_twenty = "10:20:00"
        ten_twenty_time_object = datetime.strptime(ten_twenty, '%I:%M:%S').time()

        # Compare time to 10:20:00 and append package # 9 address if >= 10:20:00
        if(current_time_object >= ten_twenty_time_object):
            addresses_with_deadlines.append(package_nine_address)

        addresses_with_deadlines = [x.get_address() for x in truck.get_packages()
                                    if x.get_deadline() != "EOD"
                                    and x.get_status() != "Delivered"]

        # For each address to check, append distance from starting_address to address
        for address in addresses_with_deadlines:
            if not list(distance_data).index(address) > len(distance_data[starting_address]):
                address_distances.append(distance_data[starting_address][list(distance_data).index(address)])
            else:
                address_distances.append(distance_data[address][list(distance_data).index(starting_address)])
        if len(address_distances) > 0:

            nearest_address = addresses_with_deadlines[address_distances.index(min(address_distances))]

            # Add mileage to travel to the nearest address
            truck.set_mileage(truck.get_mileage() + min(address_distances))

            # Ratio of total miles traveled in an hour to miles traveled to nearest address
            mileage_ratio = 18 / min(address_distances)
            minutes_to_add = 60 / mileage_ratio

            # Create datetime time object from start time string
            time_object = datetime.strptime(truck.get_last_delivered_package_time(), '%I:%M:%S').time()
            # Use time_object and timedelta to create new_time object to represent delivery time
            new_time = (datetime.combine(date.today(), time_object) + timedelta(seconds=minutes_to_add * 60)).time()

            # Convert new_time time object into string to store in Package attribute -> delivery_time
            time_delivered = new_time.strftime("%I:%M:%S")

            # Deliver package associated with nearest address
            for i in truck.get_packages():
                if i.get_package_id() == 9:
                    i.set_address(package_nine_address)
                if i.get_address() == nearest_address:

                    # Update truck's location and last delivery time
                    truck.set_location(nearest_address)
                    truck.set_last_delivered_package_time(time_delivered)

                    # Update status/delivery_time of package(s) delivered
                    i.set_status("Delivered")
                    i.set_delivery_time(time_delivered)

    # Logic for all remaining packages where package.get_status() isn't "Delivered" (until no more packages to deliver)
    while len(addresses_to_check) > 0:
        starting_address = truck.get_location()
        addresses_to_check = [x.get_address() for x in truck.get_packages() if x.get_status() != "Delivered"]
        address_distances.clear()

        # For each address to check, append distance from starting_address to address
        for address in addresses_to_check:
            if not list(distance_data).index(address) > len(distance_data[starting_address]):
                address_distances.append(distance_data[starting_address][list(distance_data).index(address)])
            else:
                address_distances.append(distance_data[address][list(distance_data).index(starting_address)])

        if len(address_distances) > 0:

            nearest_address = addresses_to_check[address_distances.index(min(address_distances))]

            # Add mileage to travel to the nearest address
            truck.set_mileage(truck.get_mileage() + min(address_distances))

            # Ratio of total miles traveled in an hour to miles traveled to nearest address
            mileage_ratio = 18 / min(address_distances)
            minutes_to_add = 60 / mileage_ratio

            # Create datetime time object from start time string
            time_object = datetime.strptime(truck.get_last_delivered_package_time(), '%I:%M:%S').time()

            # Use time_object and timedelta to create new_time object to represent delivery time
            new_time = (datetime.combine(date.today(), time_object) + timedelta(seconds=minutes_to_add * 60)).time()

            # Convert new_time time object into string to store in Package attribute -> delivery_time
            time_delivered = new_time.strftime("%I:%M:%S")

            # Find package associated with nearest address
            for i in truck.get_packages():
                if i.get_address() == nearest_address:

                    # Update truck's location and last delivery time
                    truck.set_location(nearest_address)
                    truck.set_last_delivered_package_time(time_delivered)

                    # Update status/delivery_time of package(s) delivered
                    i.set_status("Delivered")
                    i.set_delivery_time(time_delivered)

        else:
            starting_address = truck.get_location()

            # Calculate distance/time to get back to hub
            truck.set_mileage(truck.get_mileage() + distance_data[starting_address][0])

            # Ratio of total miles traveled in an hour to miles traveled to nearest address
            mileage_ratio = 18 / distance_data[starting_address][0]
            minutes_to_add = 60 / mileage_ratio

            # Create datetime time object from start time string
            time_object = datetime.strptime(truck.get_last_delivered_package_time(), '%I:%M:%S').time()

            # Use time_object and timedelta to create new_time object to represent delivery time
            new_time = (datetime.combine(date.today(), time_object) + timedelta(seconds=minutes_to_add * 60)).time()

            # Convert new_time time object into string to store in Package attribute -> delivery_time
            truck.set_end_route_time(new_time.strftime("%H:%M:%S"))

    end_route_mileage = round((truck.get_mileage()), 2)
    print("End route mileage: " + str(end_route_mileage))
    print("Truck " + str(truck.get_truck_id()) + " end of route time: " + truck.get_end_route_time())
    print()


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
    print()

    # Hash table instance
    my_hash = ChainingHashTable()

    # Load packages to Hash Table
    Package.load_package_data('package_data.csv', my_hash)

    # Create truck objects and load them
    truck1 = Truck(1)
    truck2 = Truck(2)
    truck3 = Truck(3)
    load_trucks(truck1, truck2, truck3)

    # Load address and distance data from csv file into lists
    distance_data = Package.load_distance_data('distances.csv')

    # Set package status after leaving hub
    for package in truck1.get_packages():
        package.set_status("En route")

    # find_nearest_address('4001 South 700 East', truck2, distance_data)
    # find_nearest_address('2530 S 500 E', truck2, distance_data)

    # Set package status after leaving hub
    for package in truck2.get_packages():
        package.set_status("En route")

    # find_nearest_address('4001 South 700 East', truck3, distance_data)
    # find_nearest_address('5383 S 900 East #104', truck3, distance_data)

    # Set package status after leaving hub
    for package in truck3.get_packages():
        package.set_status("In route")

    # Find routes for trucks
    find_route(truck1, distance_data)
    find_route(truck2, distance_data)
    find_route(truck3, distance_data)

    total_mileage = truck1.get_mileage() + truck2.get_mileage() + truck3.get_mileage()
    total_mileage_rounded = round(total_mileage, 2)

    print("Total mileage: " + str(total_mileage_rounded))

    # print("Packages from Hashtable:")
    print()
    get_package_data()

    # CLI or GUI logic

    # TODO: 1. Reduce duplicated code -> move to functions
    # TODO: 2. Separate out find_nearest_address/nearest_neighbor from find_route()
    # TODO: 3. Decide on GUI or CLI and implement
