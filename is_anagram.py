def is_anagram(a, b):
    '''
    Checks if the two words are anagrams, that is, if letters in one word can
    be rearranged to give the other.
    python3 -m doctest is_anagram.py

    >>> is_anagram('listen', 'silent')
    True
    >>> is_anagram('aabcd', 'dabac')
    True
    >>> is_anagram('cat', 'dog')
    False
    >>> is_anagram('abc', 'defgh')
    False
    >>> is_anagram('aabcd', 'dabcc')
    False
    >>> is_anagram('abcd', 'dabcc')
    False
    '''

    return sorted(a) == sorted(b)