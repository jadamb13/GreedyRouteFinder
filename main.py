from datetime import datetime, timedelta, date
from time import strftime

from Hash import ChainingHashTable
from Package import *
from Truck import *


def get_package_data():
    # Fetch data from Hash Table
    for i in range(0, 40):
        print("Key: {} Package info: {}".format(i + 1, my_hash.search(i + 1)))


def find_nearest_address(current_address, truck, distance_data):
    addresses_to_check = []
    address_distances = []
    # If starting address is the hub, find the closest address from all packages on truck
    if current_address == '4001 South 700 East':
        start_time = "08:00:00"
        addresses_to_check = [x.get_address() for x in truck.get_packages()]
        for i in addresses_to_check:
            address_distances.append(distance_data[i][0])
        # print(address_distances)
        nearest_address = addresses_to_check[address_distances.index(min(address_distances))]
        # print(nearest_address)

        # Add mileage to truck for distance to travel to nearest_address
        truck.set_mileage(truck.get_mileage() + min(address_distances))
        # print(truck.get_mileage())

        # Ratio of total miles traveled in an hour to miles traveled to nearest address
        mileage_ratio = 18 / min(address_distances)
        minutes_to_add = 60 / mileage_ratio

        # Create datetime time object from start time string
        time_object = datetime.strptime(start_time, '%I:%M:%S').time()

        # Use time_object and timedelta to create new_time object to represent delivery time
        # datetime.combine() and timedelta() adapted from: https://bobbyhadz.com/blog/python-add-minutes-to-datetime
        new_time = (datetime.combine(date.today(), time_object) + timedelta(seconds=minutes_to_add * 60)).time()

        # Convert new_time time object into string to store in Package attribute -> delivery_time
        time_delivered = new_time.strftime("%H:%M:%S")

        # Find package associated with nearest address
        for i in truck.get_packages():
            if i.get_address() == nearest_address:
                # Update delivery_time, status of package, and truck's last delivery time
                i.set_status("Delivered")
                i.set_delivery_time(time_delivered)
                truck.set_last_delivered_package_time(time_delivered)
                truck.set_location(nearest_address)
    else:
        # Starting from location other than hub
        addresses_to_check.clear()
        address_distances.clear()
        starting_address = truck.get_location()
        # For all remaining packages where package.get_status() isn't "Delivered" (until no more packages to deliver)
        addresses_to_check = [x.get_address() for x in truck.get_packages() if x.get_status() != "Delivered"]
        # print(list(distance_data))
        # print()
        #print(list(distance_data))
        # print(distance_data[starting_address])
        for address in addresses_to_check:
            # print(distance_data[address])
            if not list(distance_data).index(address) > len(distance_data[starting_address]):
                address_distances.append(distance_data[truck.get_location()][list(distance_data).index(address)])
            else:
                address_distances.append(distance_data[address][list(distance_data).index(starting_address)])
        print(address_distances)
        nearest_address = addresses_to_check[address_distances.index(min(address_distances))]

        # Add mileage to travel to neartest address
        truck.set_mileage(truck.get_mileage() + min(address_distances))

        # Ratio of total miles traveled in an hour to miles traveled to nearest address
        mileage_ratio = 18 / min(address_distances)
        minutes_to_add = 60 / mileage_ratio

        # Create datetime time object from start time string
        time_object = datetime.strptime(truck.get_last_delivered_package_time(), '%I:%M:%S').time()

        # Use time_object and timedelta to create new_time object to represent delivery time
        # datetime.combine() and timedelta() adapted from: https://bobbyhadz.com/blog/python-add-minutes-to-datetime
        new_time = (datetime.combine(date.today(), time_object) + timedelta(seconds=minutes_to_add * 60)).time()

        # Convert new_time time object into string to store in Package attribute -> delivery_time
        time_delivered = new_time.strftime("%H:%M:%S")

        # Find package associated with nearest address
        for i in truck.get_packages():
            if i.get_address() == nearest_address:
                # Update delivery_time, status of package, and truck's last delivery time
                i.set_status("Delivered")
                i.set_delivery_time(time_delivered)
                truck.set_last_delivered_package_time(time_delivered)
                truck.set_location(nearest_address)
        for package in truck.get_packages():
            print(package)

def load_trucks(t1, t2, t3):
    t1.packages.append(my_hash.search(13))
    t1.packages.append(my_hash.search(14))
    t1.packages.append(my_hash.search(15))
    t1.packages.append(my_hash.search(19))
    t1.packages.append(my_hash.search(11))
    t1.packages.append(my_hash.search(12))
    t1.packages.append(my_hash.search(16))
    t1.packages.append(my_hash.search(20))
    t1.packages.append(my_hash.search(21))
    t1.packages.append(my_hash.search(22))
    t1.packages.append(my_hash.search(23))
    t1.packages.append(my_hash.search(24))
    t1.packages.append(my_hash.search(26))
    t1.packages.append(my_hash.search(34))
    t1.packages.append(my_hash.search(39))

    t2.packages.append(my_hash.search(3))
    t2.packages.append(my_hash.search(18))
    t2.packages.append(my_hash.search(36))
    t2.packages.append(my_hash.search(38))
    t2.packages.append(my_hash.search(1))
    t2.packages.append(my_hash.search(2))
    t2.packages.append(my_hash.search(4))
    t2.packages.append(my_hash.search(5))
    t2.packages.append(my_hash.search(7))
    t2.packages.append(my_hash.search(10))
    t2.packages.append(my_hash.search(17))
    t2.packages.append(my_hash.search(29))
    t2.packages.append(my_hash.search(33))
    t2.packages.append(my_hash.search(37))
    t2.packages.append(my_hash.search(40))

    t3.packages.append(my_hash.search(6))
    t3.packages.append(my_hash.search(25))
    t3.packages.append(my_hash.search(28))
    t3.packages.append(my_hash.search(32))
    t3.packages.append(my_hash.search(9))
    t3.packages.append(my_hash.search(8))
    t3.packages.append(my_hash.search(27))
    t3.packages.append(my_hash.search(30))
    t3.packages.append(my_hash.search(31))
    t3.packages.append(my_hash.search(35))


if __name__ == '__main__':
    print()

    # Hash table instance
    my_hash = ChainingHashTable()

    # Load packages to Hash Table
    Package.load_package_data('package_data.csv', my_hash)

    # Create truck objects and load them
    truck1 = Truck()
    truck2 = Truck()
    truck3 = Truck()

    load_trucks(truck1, truck2, truck3)

    # Load address and distance data into lists
    distance_data = Package.load_distance_data('distances.csv')

    # Show truck package lists [Testing]
    for package in truck1.get_packages():
        package.set_status("In route")
        # print(package)
    # print()
    for package in truck2.get_packages():
        package.set_status("In route")
        # print(package)
    # print()
    # for package in truck3.get_packages():
    # print(package)
    # print()

    # Find best routes for trucks
    find_nearest_address('4001 South 700 East', truck1, distance_data)
    find_nearest_address('4300 S 1300 E', truck1, distance_data)
    find_nearest_address('4580 S 2300 E', truck1, distance_data)

    # print("Packages from Hashtable:")
    # get_package_data()

    # TODO: 1. Implement nearest neighbor/greedy algorithm to decide best delivery routes for trucks
    # TODO: 3. Keep track of mileage (When address visited, add mileage to total mileage for that truck/
    #  add totals once last package delivered
    # TODO: 4. Keep track of delivery times (When address visited, set delivery time of package)
    # TODO: 5. Decide on GUI or CLI and implement

# CLI or GUI logic
