import math
d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

# print(d.get("foo"))
# print(d["foo"])

records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Sarah", "Sales"),
    ("Pranjal", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing"),
    ("Charles", "Marketing"),
    ("Brian", "Marketing"),
    ("Jordan", "Marketing"),
]

# Hash Tables
# array, arbitrary-has-three-items-in-it.  Some slots are filled with nodes. Has super fast access which is O(1), and can access with strings. (Fast Searching)


def build_index(recs):
    index = {}

    for record in recs:
        name, dept = record
        # Check if department is already in index
        if dept in index:
            # if it is, add name to the list
            index[dept].append(name)
        else:
            # else create new key with list with the name in it
            index[dept] = [name]
    return index


department_index = build_index(records)

# # print all the departments
# print(department_index.keys())

# # print everyone in engineering
# print(department_index["Engineering"])

# # print everyone in sales
# print(department_index["Sales"])

# # print everyone in Marketing
# print(department_index["Marketing"])


##### LOOKUP TABLE ######


# inverse square root is 1 / square root of number

def get_inverse_square(num):
    return 1 / math.sqrt(num)

# We need to constantly get the inverse sqrt of numbers between 1 and 1000
# Build a lookup table.


def build_lookup_table():
    lookup_table = {}
    for i in range(1, 1001):
        lookup_table[i] = get_inverse_square(i)
    return lookup_table


sqrt_lookup_table = build_lookup_table()

# print(sqrt_lookup_table[3])
# print(sqrt_lookup_table[982])
# print(sqrt_lookup_table[234])


# Given a string, can we figure out how many times each letter appears in it

def letter_count(s):
    # Dict where keys are letters and values will be an incrementing counter
    d = {}
    for char in s:
        if char.isspace():
            continue
        if char not in d:
            # create the key
            d[char] = 1
        else:
            d[char] += 1
    return d


def double_letter(s):
    d = set()
    for char in s:
        if char.isspace():
            continue
        if char not in d:
            # create the key
            d.add(char)
        else:
            # d[char] += 1
            return char

    # for key, value in d.items():
    #     if value == 2:
    #         return key

    # store letters as keys and a counter as value
    # find all lettesr, (or find the one letter) where value is more than one.


# print(double_letter("abcdeef"))


# print(letter_count("aaaabbc"))
# print(letter_count("Hello!"))
# print(letter_count("the quick brown fox jumps over the lazy dogs"))


#### CIPHER ####

# SUBSTITUTION CIPHERS #
# How to transform data from one thing to another.

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

decode_table = {}

for key, value in encode_table.items():
    decode_table[value] = key


def encode(plain_text):
    cipher = ""

    for char in plain_text:
        if char.isspace():
            cipher += " "
        else:
            cipher += encode_table[char.upper()]
    return cipher


def decode(cipher_text):
    plain_text = ""
    for char in cipher_text:
        if char.isspace():
            plain_text += ' '
        else:
            plain_text += decode_table[char.upper()]
    return plain_text


cipher = encode("Dictionaries are awesome")
print(cipher)

print(decode(cipher))
