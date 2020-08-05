# HASH TABLES (Dictionary, map, object)

# array
words = ["apple", "book", "cat", "dog", "egypt", "france"]
# to access egypt, runtime is: O(n)


# what if we had a function that takes a word -->
# returns the ineex for where that word is located in said array
# book --> 1
# egypt --> 4
# fake-word --> None
# this function is O(1)

# HAS FUNCTIONS

# has function will take in ANY input, and return a number within a list range
# MOST IMPORTANT feature:
# This function must be deterministic.  -- same input will always return same output.


def my_hash(s, limit):

    # take every character in the string, and convert character to number
    # convert each character into UTF-8 numbers
    # encode() returns an array
    string_utf = s.encode()

    total = 0
    for char in string_utf:
        total += char
        # limit total to 32 bits
        # this is an operator that works on binary &
        total &= 0xffffffff
        # 8 f's for 32 bit. 16 f's for 64 bit
        #  this is the biggest number you can have in a 32 bit system 0xffffffff
    return total % limit


# hash table
# make sure it is OF SIZE OF A POWER OF 2
hash_table = [None] * 8

# add items to hash table using the my_hash function
# Hash the key to get an index
# Store the value at the generated Index
index = my_hash("Hello", len(hash_table))
hash_table[index] = "Value for Hello"

index = my_hash("World", len(hash_table))
hash_table[index] = "Value for World"


# Retrieve some items from hash_table
# Lets retrieve the value for Hello
index = my_hash("Hello",  len(hash_table))
print(hash_table[index])
print(hash_table)


print(f'card hashes to {my_hash("card", 8)}')
print(f'apple hashes to {my_hash("apple", 8)}')
