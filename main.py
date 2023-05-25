from Hash import ChainingHashTable
from Package import *


def get_package_data():
    # Eval/optimize for efficiency with hash search

    # Fetch data from Hash Table
    for i in range(0, 40):
        print("Key: {} Package info: {}".format(i+1, my_hash.search(i+1))) # 1 to 11 is sent to my_hash.search()


if __name__ == '__main__':
    print()
    # CLI or GUI logic

    # Hash table instance
    my_hash = ChainingHashTable()

    # Load packages to Hash Table
    load_package_data(my_hash)

    # print("Packages from Hashtable:")
    get_package_data()

    # Load address and distance data into lists
    load_distance_data()


