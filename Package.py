import csv

from ChainHashTable import ChainHashTable


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

    def __str__(self):  # overwrite print(Package), otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s" % (
            self.package_id, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight)

    def load_package_data(filename):
        with open(filename) as package_file:
            package_data = csv.reader(package_file, delimiter=',')

            for package in package_data:
                p_id = package[0]
                p_address = package[1]
                p_city = package[2]
                p_state = package[3]
                p_zipcode = package[4]
                p_deadline = package[5]
                p_weight = package[6]

                # Package object
                p = Package(p_id, p_address, p_city, p_state, p_zipcode, p_deadline, p_weight)
                #print(p)
                # Hash table instance
                my_hash = ChainHashTable()

                # insert it into the hash table
                my_hash.insert(p_id, p)


        print("Packages from Hashtable:")
        # Fetch data from Hash Table
        for i in range(len(my_hash.table) + 1):
            print("Key: {} and PackageObj: {}".format(i + 1, my_hash.search(i + 1)))  # 1 to 11 is sent to
            # myHash.search()
