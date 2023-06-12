# Reference: Lysecky, R., & Vahid, F. (2018)
# Figure 7.8.2: Hash table using chaining

class ChainingHashTable:
    # Constructor with optional initial capacity parameter
    # Assigns all buckets with an empty list
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table
    def insert(self, key, item):
        # get the bucket list where this item will go
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list
        kv_pair = [key, item]
        bucket_list.append(kv_pair)
        return True

    # Searches for an item with matching key in the hash table
    # Returns the value if key is found, or None if not found
    def search(self, key):
        # get the bucket list where this key would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list and return its value
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
        return None

