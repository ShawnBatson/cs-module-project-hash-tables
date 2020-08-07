# HASH TABLES (Dictionary, map, object)
class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


hash_table = [None] * 8  # 8 slots


def my_hash(s):

    string_utf = s.encode()

    total = 0
    for char in string_utf:
        total += char
        total &= 0xffffffff
    return total  # THIS GETS THE HASH


def hash_index(key):
    hash_num = my_hash(key)  # creates the hash
    # where in the hash it should go   #### THIS GETS THE INDEX
    return hash_num % len(hash_table)


def put(key, val):
    i = hash_index(key)
    # find the start of the linked list using the index
    # insert into this linked list a new HashTableEntry
    # Search throught he linked List
    # if the key already exists in linked list:
    #     replace the value --
    # else:
    #     Add new hashTableEntry to the head of linked list --

    # can delete this collission code
    if hash_table[i] != None:
        print(f'Collision! Overwriting {repr(hash_table[i])}')
    hash_table[i] = val


def get(key):
    # hash the key and get the index
    i = hash_index(key)
    # Get the linked list AT the computed INDEX
    # Search throught he linked list for the key
    # If it exists, return the value
    # else, return None

    # Return the value from the array at the index
    return hash_table[i]


def delete(key):
    # has the key and get the index
    i = hash_index(key)
    # Search through the linked list for the matching key
    # DELETE THAT NODE
    # Return the value of deleted node (or None)

# LOAD FACTOR
# load factor =  number of items in hash table / number of total slots

# IF LOAD FACTOR TOO HIGH, RESIZE (Capacity * 2) add to count (0.7)
# IF LOAD FACTOR BECOMES TOO LOW, RESIZE (CAPACITY / 2) sub from count (0.2)


def resize():
    # make a new array, double the current size
    # Go through each linked list in the array,
    #     GO through each item and re-hash it (index might change)
    #     insert the items into their new locations


def shrink():
    # same as resize, but reduce by half instead
    pass


put("Hello", "Hello Value")
put("World", "World Value")

print(hash_table)

put("foo", "Foo Value")

print(hash_table)


value = get("Hello")
print(value)

print(hash_index("Hello"))
print(hash_index("foo"))


# linear probing - foo wants to go to spot 4, if 4 is taken we just check spot 5, and so on, until you find none, and place foo.


# hash function and array, plus:
# ADD A LINKED LIST to the array itself!

# Hello and foo both sit at 4, lets turn 4 into a linked list, where foo is the head, and hello is the next node in the linked list, both occupying space 4 in the array.
# to retrieve Hello (second position in a linked list), we search through the linked list.
# we want to make sure we store the key and value in each node
#
