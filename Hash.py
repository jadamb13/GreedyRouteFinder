# Ref: zyBooks - Figure 7.8.2: Hash table using chaining.

class ChainingHashTable:
    # Constructor with optional initial capacity parameter
    # Assigns all buckets with an empty list
    def __init__(self, initial_capacity=40):
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
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table
    # Returns the item if found, or None if not found
    def search(self, key):
        # get the bucket list where this key would be
        #print(key)
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        #print(bucket_list)

        # search for the key in the bucket list
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
            return None

    # Removes an item with matching key from the hash table
    def remove(self, key):
        # get the bucket list where this item will be removed from
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])