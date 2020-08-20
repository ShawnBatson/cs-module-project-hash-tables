def word_count(s):

    # ignoredChars = ['', '', "?", "!", "\"", ":", ";", ",", ".", "-", "+", "=",
    #                 "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]

    # ignoredCount = 0
    # words = s.split()
    # box = {}

    # # check for restricted characters from ignoredChars
    # for i in s:
    #     for x in ignoredChars:
    #         if i == x:
    #             ignoredCount += 1
    #             s = s.replace(i, '')

    # # if the ignored count inside the string is 0, return an empty dictionary
    # if ignoredCount == 0:
    #     return {}

    # # make the table, first split the string at the space

    # for word in words:
    #     if word not in box:
    #         box[word] = 1
    #     else:
    #         box[word] += 1

    # return box

    tr = str.maketrans('', '', '":;,.-+=/\\|[]{}()*^&')
    s = s.translate(tr).lower()
    words = s.split()
    counts = {}
    for w in words:
        if w not in counts:
            counts[w] = 1
        else:
            counts[w] += 1
    return counts


if __name__ == "__main__":
    print(word_count("Hello    hello"))
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
