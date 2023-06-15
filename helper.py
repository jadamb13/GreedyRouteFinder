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
    # Reference: Hadzhiev, B. (2023)
    new_time = (datetime.combine(date.today(), time_object) + timedelta(
        seconds=minutes_to_add * 60)).time()

    # Convert new_time time object into string to store in Package attribute -> delivery_time
    time_delivered = new_time.strftime("%I:%M:%S")
    return time_delivered


def set_attributes_on_delivery(truck, package, address, time):
    package.set_status("Delivered")
    package.set_delivery_time(time)
    truck.set_last_delivered_package_time(time)
    truck.set_location(address)


def load_package_data(filename, my_hash):
    with open(filename) as package_file:
        package_data = csv.reader(package_file, delimiter=',')

        for row in package_data:
            p_id = int(row[0])
            p_address = row[1]
            p_city = row[2]
            p_state = row[3]
            p_zipcode = row[4]
            p_deadline = row[5]
            p_weight = row[6]

            # Package object
            p = Package(p_id, p_address, p_city, p_state, p_zipcode, p_deadline, p_weight)

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
        distances[0].append(0.0)

        # For all other rows, extract address from second column
        for row in distance_table:
            # Turn address into single line, split into tokens, extract token for street address
            addresses.append(row[1].split('\n')[0].strip().replace('\n', ' '))

            for i in range(0, len(addresses) - 1):
                distances[len(addresses) - 1].append(float(row[2 + i]))
            distances[len(addresses) - 1].append(0.0)

    # Save addresses and distances into dictionary
    # key: address | values: list of distances to other addresses
    distances_dict = {}
    keys = [a for a in addresses]
    # Set distances_dict keys to addresses from CSV file
    for key in keys:
        distances_dict[key] = [x for x in distances[keys.index(key)]]

    # Save addresses in dictionary to reference by index
    address_dict = {}
    for i in range(0, len(distances_dict)):
        address_dict[i] = keys[i]

    # Fully populate distances_dict to get symmetrical data
    address_index = 1
    values = []

    # 26 values should be in each distances list for each key/address in distances_dict
    for i in range(27):
        for row in distances_dict:
            if address_index == 27:
                break
            # Append column of values associated with row's address to temporary list
            # to be added on to current row's distances
            values.append(distances_dict[address_dict[address_index]][i])
            address_index += 1
        # Move to next row (excluding first two rows)
        address_index = 2 + i

        # Append associated distances to each list in distances_dict values to make all lists equal length
        distances_dict[address_dict[i]] += values

        # Clear temporary values list for next row
        values.clear()

    return distances_dict


def get_single_package_status_at_time(my_hash, trucks, time, package_id):
    package = my_hash.search(int(package_id))

    # Create datetime time object from time string
    time_object = datetime.strptime(time + ":00", '%H:%M:%S').time()

    # Create datetime time object for 10:20:00
    ten_twenty = datetime.strptime("10:20:00", '%I:%M:%S').time()

    # Create package_nine_address string to hold address of updated Package #9
    package_nine_address = "410 S State St, Salt Lake City, UT, 84111"

    start_time = None

    if time_object >= ten_twenty and package.get_package_id() == 9:
        package.set_address(package_nine_address)
    if package in trucks[0].get_packages():
        start_time = '08:00:00'
    if package in trucks[1].get_packages():
        start_time = '09:15:00'
    if package in trucks[2].get_packages():
        start_time = '10:18:00'

    # Create datetime time object from start_time string
    start_time_object = datetime.strptime(start_time, '%I:%M:%S').time()

    # Create datetime time object from package delivery time string
    delivery_time_object = datetime.strptime(package.get_delivery_time(), '%I:%M:%S').time()

    # If after start time, check time given against package delivery times to set package status to delivered
    if time_object >= start_time_object:
        # If delivery time after given time, set status to "En Route"
        if time_object <= delivery_time_object:
            package.set_status("En Route")
            package.set_delivery_time("N/A")

        # Else: (delivery time before or equal to given time, set status to "Delivered"
        else:
            package.set_status("Delivered")

    # Else: (not after start time)
    else:
        # Set all packages to "At hub"
        package.set_status("At hub")
        package.set_delivery_time("N/A")

    print(package)


def get_delivery_status_at_time(packages, time, trucks):
    # Create datetime time object from time string
    time_object = datetime.strptime(time + ":00", '%H:%M:%S').time()

    # Create datetime time object for 10:20:00
    ten_twenty = datetime.strptime("10:20:00", '%I:%M:%S').time()

    # Create package_nine_address string to hold address of updated Package #9
    package_nine_address = "410 S State St, Salt Lake City, UT, 84111"

    start_time = None

    for i in packages:
        if time_object >= ten_twenty and i.get_package_id() == 9:
            i.set_address(package_nine_address)
        if i in trucks[0].get_packages():
            start_time = '08:00:00'
        if i in trucks[1].get_packages():
            start_time = '09:15:00'
        if i in trucks[2].get_packages():
            start_time = '10:18:00'

        # Create datetime time object from start_time string
        start_time_object = datetime.strptime(start_time, '%I:%M:%S').time()

        # Create datetime time object from package delivery time string
        delivery_time_object = datetime.strptime(i.get_delivery_time(), '%I:%M:%S').time()

        # If after start time, check time given against package delivery times to set package status to delivered
        if time_object >= start_time_object:
            # If delivery time after given time, set status to "En Route"
            if time_object <= delivery_time_object:
                i.set_status("En Route")
                i.set_delivery_time("N/A")

            # Else: (delivery time before or equal to given time, set status to "Delivered"
            else:
                i.set_status("Delivered")

        # Else: (not after start time)
        else:
            # Set all packages to "At hub"
            i.set_status("At hub")
            i.set_delivery_time("N/A")

    for p in packages:
        print(p)


def find_nearest_address(starting_address, address_list, distance_data, indexes):
    # Initialize nearest address to empty string
    nearest_address = ''

    # Set shortest_distance to a high number that the first distances value will be lower than
    shortest_distance = 10000

    # For each address in the list
    for address in address_list:

        # Get the distance from the starting address to the address
        distance = distance_data[starting_address][indexes[address]]

        # If the distance is less than shortest_distance, set the address as the new nearest_address
        # and set the distance as the new shortest_distance
        if distance < shortest_distance and distance != 0.0:
            shortest_distance = distance
            nearest_address = address
    return [nearest_address, shortest_distance]


def get_packages_with_deadlines_data(trucks):
    all_packages = []
    for truck in trucks:
        all_packages += truck.get_packages()
    packages_with_deadlines = [x for x in all_packages if x.get_deadline() != "EOD"]
    print()
    print("Packages with deadlines: ".center(110))
    print("-" * 130)
    print("%-5s %-68s %-10s %-13s %-15s %s" %
          ("ID", "Address".center(30), "Weight".center(6),
           "Deadline".center(12), "Status".center(13), "Delivery Time".center(15)))
    print("-" * 130)
    for pkg in packages_with_deadlines:
        print(pkg)
    print()


def send_truck_to_first_address(truck):
    # Set start times and first address to visit for trucks
    if truck.get_truck_id() == 1:
        start_time = "08:00:00"
        first_address = "4580 S 2300 E"
        # Set package statuses after leaving hub
        for p in truck.get_packages():
            p.set_status("En route")

    if truck.get_truck_id() == 2:
        start_time = "09:15:00"
        first_address = "5383 S 900 East #104"
        # Set package statuses after leaving hub
        for p in truck.get_packages():
            p.set_status("En route")

    if truck.get_truck_id() == 3:
        start_time = "10:18:00"
        first_address = "2530 S 500 E"
        # Set package statuses after leaving hub
        for p in truck.get_packages():
            p.set_status("En route")

    return [first_address, start_time]


def deliver_packages(truck, address_data):
    # address_data is a list of length 2 holding a string address and a
    # float mileage to the nearest address from the starting address
    address = address_data[0]
    address_mileage = address_data[1]

    # Set the starting time to time of the truck’s last delivered package
    truck_time = truck.get_last_delivered_package_time()

    # Create datetime time object from start time string
    current_time = datetime.strptime(truck_time, '%I:%M:%S').time()

    # Create datetime time object for 10:20:00
    ten_twenty = datetime.strptime("10:20:00", '%I:%M:%S').time()

    # Add mileage to travel to the nearest address
    truck.set_mileage(truck.get_mileage() + address_mileage)

    # Calculate the trip time from the truck’s location to the nearest_address
    # and store it into a time_delivered variable
    time_delivered = calculate_trip_time(truck_time, address_mileage)

    # Find package associated with the address and deliver
    for p in truck.get_packages():
        # If first_address matches package address:
        if p.get_address() == address:
            # Check if the Package ID is 9 and the time is >= 10:20am
            # If so, set Package #9 address and deliver it
            if p.get_package_id() == 9 and current_time >= ten_twenty:
                set_attributes_on_delivery(truck, p, address, time_delivered)

            else:
                # If the package is Package #9 but it’s not >= 10:20am
                if p.get_package_id() == 9:
                    continue
                # If not package #9, deliver the package(s)
                set_attributes_on_delivery(truck, p, address, time_delivered)
