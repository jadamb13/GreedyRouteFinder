from datetime import datetime, timedelta, date

from helper import calculate_arrival_time, deliver_package, calculate_distances_between_addresses
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
            # Set package statuses after leaving hub
            for p in truck1.get_packages():
                p.set_status("En route")
            start_time = "08:00:00"
            first_address = "4580 S 2300 E"
        if truck.get_truck_id() == 2:
            for p in truck2.get_packages():
                p.set_status("En route")
            start_time = "09:15:00"
            first_address = "5383 S 900 East #104"
        if truck.get_truck_id() == 3:
            for p in truck3.get_packages():
                p.set_status("En route")
            start_time = "10:18:00"
            first_address = "2530 S 500 E"

        # Populate list with addresses for all packages on truck
        addresses_to_check = [x.get_address() for x in truck.get_packages()]
        for i in addresses_to_check:
            address_distances.append(distance_data[i][0])

        # Randomly select first address to start [TESTING]
        # nearest_address = addresses_to_check[address_distances.index(min(address_distances))]
        # random_start_index = randrange(1, len(addresses_to_check) - 1)
        # print("Random start index: " + str(random_start_index))
        # first_address = addresses_to_check[random_start_index]

        # Add mileage to truck for distance to travel to nearest_address
        # truck.set_mileage(truck.get_mileage() + min(address_distances))
        mileage_to_first_address = address_distances[addresses_to_check.index(first_address)]
        truck.set_mileage(truck.get_mileage() + mileage_to_first_address)
        time_delivered = calculate_arrival_time(start_time, mileage_to_first_address)

        break

    # Find package associated with the first address and set attributes
    for i in truck.get_packages():
        # If first_address matches package address:
        if i.get_address() == first_address:
            # Update delivery_time, status of package, and truck's last delivery time/location
            deliver_package(truck, i, first_address, time_delivered)
    addresses_to_check.remove(first_address)

    # Logic for delivering packages with deadlines first
    package_nine_address = "410 S State St"
    addresses_with_deadlines = [x.get_address() for x in truck.get_packages()
                                if x.get_deadline() != "EOD"
                                and x.get_status() != "Delivered"]

    while len(addresses_with_deadlines) > 0:
        address_distances.clear()
        starting_address = truck.get_location()

        # Create datetime time object from start time string
        time = truck.get_last_delivered_package_time()
        current_time = datetime.strptime(time, '%I:%M:%S').time()

        # Create datetime time object for 10:20:00
        ten_twenty = datetime.strptime("10:20:00", '%I:%M:%S').time()

        addresses_with_deadlines = [x.get_address() for x in truck.get_packages()
                                    if x.get_deadline() != "EOD"
                                    and x.get_status() != "Delivered"]

        address_distances = calculate_distances_between_addresses(starting_address, addresses_with_deadlines,
                                                                  distance_data)

        if len(address_distances) > 0:

            nearest_address = addresses_with_deadlines[address_distances.index(min(address_distances))]

            # Add mileage to travel to the nearest address
            truck.set_mileage(truck.get_mileage() + min(address_distances))

            time_delivered = calculate_arrival_time(truck.get_last_delivered_package_time(), min(address_distances))

            # Deliver package associated with nearest address
            for i in truck.get_packages():

                if i.get_address() == nearest_address:
                    if i.get_package_id() == 9 and current_time >= ten_twenty:
                        i.set_address(package_nine_address)
                        deliver_package(truck, i, nearest_address, time_delivered)
                    # Update delivery_time, status of package, and truck's last delivery time/location
                    else:
                        if i.get_package_id() == 9:
                            continue
                        deliver_package(truck, i, nearest_address, time_delivered)

    # Logic for all remaining packages where package.get_status() isn't "Delivered" (until no more packages to deliver)
    while len(addresses_to_check) > 0:
        starting_address = truck.get_location()
        addresses_to_check = [x.get_address() for x in truck.get_packages() if x.get_status() != "Delivered"]
        address_distances.clear()
        address_distances = calculate_distances_between_addresses(starting_address, addresses_to_check,
                                                                  distance_data)

        if len(address_distances) > 0:

            nearest_address = addresses_to_check[address_distances.index(min(address_distances))]

            # Add mileage to travel to the nearest address
            truck.set_mileage(truck.get_mileage() + min(address_distances))

            time_delivered = calculate_arrival_time(truck.get_last_delivered_package_time(), min(address_distances))

            # Find package associated with nearest address
            for i in truck.get_packages():
                if i.get_address() == nearest_address:
                    # Update delivery_time, status of package, and truck's last delivery time/location
                    deliver_package(truck, i, nearest_address, time_delivered)

        else:
            starting_address = truck.get_location()

            # Calculate distance/time to get back to hub
            truck.set_mileage(truck.get_mileage() + distance_data[starting_address][0])

            # Convert new_time time object into string to store in Package attribute -> delivery_time
            truck.set_end_route_time(calculate_arrival_time(truck.get_last_delivered_package_time(),
                                                            distance_data[starting_address][0]))

    """ [Testing]
    end_route_mileage = round((truck.get_mileage()), 2)
    print("End route mileage: " + str(end_route_mileage))
    print("Truck " + str(truck.get_truck_id()) + " end of route time: " + truck.get_end_route_time())
    print()
    """

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

    # Find routes for trucks
    find_route(truck1, distance_data)
    find_route(truck2, distance_data)
    find_route(truck3, distance_data)

    # print("Packages from Hashtable:")
    print()
    get_package_data()

    total_mileage = truck1.get_mileage() + truck2.get_mileage() + truck3.get_mileage()
    total_mileage_rounded = round(total_mileage, 2)

    print()
    print("Total mileage: " + str(total_mileage_rounded))

    # CLI or GUI logic

    # TODO: 1. Reduce duplicated code -> move to functions
    # TODO: 2. Separate out find_nearest_address/nearest_neighbor from find_route()
    # TODO: 3. Decide on GUI or CLI and implement
