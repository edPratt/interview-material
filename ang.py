def anagram(s1, s2):
    d1 = {}
    d2 = {}
    for c in s1:
        c = c.lower()
        if c in d1:
            d1[c] += 1
        else:
            d1[c] = 1
    for c in s2:
        c = c.lower()
        if c in d2:
            d2[c] += 1
        else:
            d2[c] = 1
    return d1 == d2

if __name__ == '__main__':
    s1 = 'iceman'
    s2 = 'cinema'
    print(s1, s2, anagram(s1, s2))
    s1 = 'The Morse Code'
    s2 = 'Here comes dot'
    print(s1, s2, anagram(s1, s2))
