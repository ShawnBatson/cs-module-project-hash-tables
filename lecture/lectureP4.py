# BOTH OF THESE ARE ON MY LEETCODE.  THERE IS NO ACTIVE TESTS HERE.

# Count how many times each character in J appears in S
# Naive
class Solution:
    def numJewelsInStone(self, J: str, S: str) -> int:
        count = 0
        # for each Char in J
        for char_j in J:
            for char_s in S:
                if char_j == char_scount += 1
        #    compare with each char in s
        #       if char J = char S then count ++
        return count

# hash solution


class Solution2:
    def numJewelsInStone2(self, J: str, S: str) -> int:
        count = 0

        jewels_dict = {}

        for char_j in J:
            jewels_dict[char_j] = 0

        for char_s in S:
            if char_s in jewels_dict:
                jewels_dict[char_s] += 1

        for v in jewels_dict.values():
            count += v


# understand happy number
# input is some number, positive
# input will turn into a boolean/true false
# if n transforms to one, return true
# if n transforms into something we've already seen, return false

class Solution:

    def __init__(self):
        self.seen_values = set()  # for leet code

    def isHappy(self, n: int) -> bool:
        if n == 1:  # base case
            return True

        # if n was seen before, return false
        # return false at some point here

        if n in self.seen_values:
            return False

        # store this new sum into a cache
        # we now have seen this number before
        # add the original number to check against for false case
        self.seen_values.add(n)

        # transform n to the new value
        # break into digits
        # turn n into a string
        # square each digit
        # sum the squares of each digit up

        new_num = sum([int(digit)**2 for digit in str(n)])

        return self.isHappy(new_num)
