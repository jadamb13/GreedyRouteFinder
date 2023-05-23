from ChainHashTable import ChainHashTable
from Package import *


def get_package_data():
    # Fetch data from Hash Table
    for i in range(len(my_hash.table) + 1):
        print("Key: {} and PackageObj: {}".format(i + 1, my_hash.search(i + 1)))  # 1 to 11 is sent to myHash.search()


if __name__ == '__main__':
    print()
    # CLI or GUI logic
    # Hash table instance
    my_hash = ChainHashTable()

    # Load packages to Hash Table
    Package.load_package_data('package_data.csv', my_hash)

    print("Packages from Hashtable:")
    get_package_data();
