import csv


class Package:

    def __init__(self, package_id, address, city, state, zipcode,
                 deadline, weight):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = "At hub"
        self.delivery_time = "N/A"


    def __str__(self):  # overwrite print(Package), otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.package_id, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.status,
            self.delivery_time)



    def set_delivery_time(self, time):
        self.delivery_time = time

    def get_address(self):
        return self.address

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

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
