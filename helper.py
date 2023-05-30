from datetime import datetime, timedelta, date


def calculate_arrival_time(current_time, miles):
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
