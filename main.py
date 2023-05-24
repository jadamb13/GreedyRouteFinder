from Hash import ChainingHashTable
from Package import *


def get_package_data():

    # Eval/optimize for efficiency with hash search
    """
    # Fetch data from Hash Table
    for i in range(len(my_hash.table)+1):
        print("Package key: {} Package info: {}".format(i+1, my_hash.search(i+1))) # 1 to 11 is sent to my_hash.search()
    """
    for kv in my_hash.table:
        for k, v in kv:
            print("Key: " + k + " | Package object: " + str(v))
    print()

if __name__ == '__main__':

    print()
    # CLI or GUI logic
    # Hash table instance
    my_hash = ChainingHashTable()

    # Load packages to Hash Table
    Package.load_package_data('package_data.csv', my_hash)

    print("Packages from Hashtable:")
    get_package_data()

    Package.load_distance_data('distances.csv')

