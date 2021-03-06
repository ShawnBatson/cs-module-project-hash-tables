class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.nodes = 0  # number of boxes
        self.top = 0.7  # slightly below 1 so load capacity stays within range
        self.bottom = 0.2  # slightly above 0 so load capacity stays within range

    def get_num_slots(self, limit=0):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):  # load factor should always be below 1
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.nodes / self.capacity  # to get less than 1, divide amount of nodess by capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for b in key:
            hash = (hash * 33) + ord(b)
            hash &= 0xffffffff
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        if self.get_load_factor() >= self.top:  #
            # change the size by a multiple of 2
            self.resize(self.capacity * 2)

        index = self.hash_index(key)  # get the hash index key

        if self.storage[index] == None:  # if the index is none,
            self.storage[index] = HashTableEntry(
                key, value)  # make that none the entry
            self.nodes += 1  # add one to the node count

        # elif self.storage[index] != None:
        #     self.storage[index] = HashTableEntry(key, value)
        #     self.nodes += 1
        #     return
        else:
            current = self.storage[index]  # set the current to the index
            while current != None:  # while current is not none
                if current.key == key:  # and if the current key = key
                    current.value = value  # then the current vaue = value
                    break
                elif current.next != None:  # if the current.next is none
                    current = current.next  # set the current to the non-None next
                else:
                    break  # otherwise stop
            # set the current.next to the new entry
            current.next = HashTableEntry(key, value)
            self.nodes += 1  # add to the node count

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        if self.get_load_factor() <= self.bottom:  # THIS IS THE STRETCH
            # THIS IS THE STRETCH / if goes below 0.2, resize to minimum 8
            self.resize(MIN_CAPACITY)
        else:
            # else, just resize it like normal, cut in half.
            self.resize(self.capacity // 2)

        # grab the index:
        index = self.hash_index(key)
        current = self.storage[index]  # set up the linked list directional
        previous = self.storage[index]  # set up the linked list direcional

        if current.next == None:  # if next is none
            self.storage[index] = None  # Then the index is none
            self.nodes -= 1  # remove one from count
            return
        elif current.key == key:  # if the current key = target key
            self.storage[index] = current.next  # index then equals next
            self.nodes -= 1  # remove one from node count
        else:
            current = current.next  # just remove the pointer from current

        while current != None:  # while current is none
            if current.key == key:  # if current key is key
                previous.next = current.next  # the previous' next, now is the current.next
                self.nodes -= 1  # remove from count
                return
            elif current.next != None:  # if current next is not None
                current = current.next  # current now equals current.next
                previous = previous.next  # previous now equals previous.next
            else:
                break  # break

        print('Warning, key not found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # grab the index:
        index = self.hash_index(key)

        current = self.storage[index]

        while current != None:  # while the box is not empty
            if current.key == key:  # if the current key matches the input key
                return current.value  # return the current key's value
            current = current.next
            return None  # else return none

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # bring in the original list
        old = self.storage
        new = [None] * new_capacity  # make a new blank list
        self.storage = new  # replace storage with the new set
        self.capacity = len(new)  # set a new original capacity

        # loop through the old list, and place in original positions:
        for box in old:  # for all in box
            if box != None:  # if box is not empty
                current = box  # set that box to current
                while current:  # while there is a current
                    # use the put function to insert the key value pair
                    self.put(current.key, current.value)
                    current = current.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
