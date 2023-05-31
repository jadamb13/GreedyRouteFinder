from datetime import datetime, timedelta, date
import csv

from Package import Package


def calculate_trip_time(current_time, miles):
    # Ratio of total miles traveled in an hour to miles traveled to nearest address
    mileage_ratio = 18 / miles
    minutes_to_add = 60 / mileage_ratio

    # Create datetime time object from start time string
    time_object = datetime.strptime(current_time, '%I:%M:%S').time()

    # Use time_object and timedelta to create new_time object to represent delivery time
    # datetime.combine() and timedelta() adapted from:
    # https://bobbyhadz.com/blog/python-add-minutes-to-datetime
    new_time = (datetime.combine(date.today(), time_object) + timedelta(
        seconds=minutes_to_add * 60)).time()

    # Convert new_time time object into string to store in Package attribute -> delivery_time
    time_delivered = new_time.strftime("%I:%M:%S")
    return time_delivered


def deliver_package(truck, package, address, time):
    package.set_status("Delivered")
    package.set_delivery_time(time)
    truck.set_last_delivered_package_time(time)
    truck.set_location(address)


def calculate_distances_between_addresses(starting_address, address_list, distances_dict):
    address_distances = []

    # For each address to check, append distance from starting_address to address
    for address in address_list:
        if not list(distances_dict).index(address) > len(distances_dict[starting_address]):
            address_distances.append(distances_dict[starting_address][list(distances_dict).index(address)])
        else:
            address_distances.append(distances_dict[address][list(distances_dict).index(starting_address)])
    return address_distances


def load_package_data(filename, my_hash):
    with open(filename) as package_file:
        package_data = csv.reader(package_file, delimiter=',')

        for package in package_data:
            p_id = int(package[0])
            p_address = package[1]
            p_city = package[2]
            p_state = package[3]
            p_zipcode = package[4]
            p_deadline = package[5]
            p_weight = package[6]

            # Package object
            p = Package(p_id, p_address, p_city, p_state, p_zipcode, p_deadline, p_weight)
            # print(p)

            # insert it into the hash table
            my_hash.insert(p_id, p)


def load_distance_data(filename):
    addresses = []
    distances = []

    for i in range(0, 27):
        distances.append([])

    with open(filename) as distance_file:
        distance_table = csv.reader(distance_file, delimiter=',')

        # No address is listed in the second column for the first row
        # Separates first row to pull address from first column
        row0 = next(distance_table)
        # Turn address into single line, split into tokens, extract token for street address
        addresses.append(row0[0].split('\n')[1].replace('\n', ' ').replace(',', ''))

        # For all other rows, extract address from second column
        for row in distance_table:
            # Turn address into single line, split into tokens, extract token for street address
            addresses.append(row[1].split('\n')[0].strip().replace('\n', ' '))

            for i in range(0, len(addresses) - 1):
                distances[len(addresses) - 1].append(float(row[2 + i]))

    # Save addresses and distances into dictionary
    # key: address | values: list of distances to other addresses
    distances_dict = {}
    keys = [a for a in addresses]
    for key in keys:
        distances_dict[key] = [x for x in distances[keys.index(key)]]

    return distances_dict
