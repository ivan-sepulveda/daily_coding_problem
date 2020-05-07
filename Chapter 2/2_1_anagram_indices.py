from collections import defaultdict

w = 'ab'
s = 'abxaba'


def del_if_zero(dict, char):
    if dict[char] == 0:
        del dict[char]

def anagram_indices(word, s):
    result = []

    freq = defaultdict(int)
    print("starting loop: for char in word")
    for char in word:
        print(char)
        freq[char] += 1
        print("freq below")
        print(freq)

    print("\n\nstarting loop: char in s[:len(word)]")
    for char in s[:len(word)]:
        print(char)
        freq[char] -= 1
        print('freq post subtract')
        print(freq)
        del_if_zero(freq, char)
        print('freq post delete')
        print(freq)

    if not freq:
        result.append(0)

    print("\n\nresult so far")
    print(result)

    for i in range(len(word), len(s)):
        print("i = %s" % str(i))
        print("freq so far")
        print(freq)
        print(("\n\n"))
        start_char, end_char = s[i - len(word)], s[i]
        print("start_char: %s" % start_char)
        print("end_char: %s" % end_char)
        freq[start_char] += 1
        del_if_zero(freq, start_char)

        freq[end_char] -= 1
        del_if_zero(freq, end_char )

        if not freq:
            print(freq)
            beginning_index = i - len(word) + 1
            result.append(beginning_index)

            print("result so far")
            print(result)

    return result


print(anagram_indices(w, s))