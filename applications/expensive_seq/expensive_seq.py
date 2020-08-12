# Your code here
box = {}


def expensive_seq(x, y, z):
    # just made a dictionary with the directions and restrictions from readme as the key/value
    # not much else to say about it.
    if x <= 0:
        return y+z

    if x > 0:
        if (x, y, z) not in box:
            box[(x, y, z)] = expensive_seq(x-1, y+1, z) + \
                expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
        return box[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
