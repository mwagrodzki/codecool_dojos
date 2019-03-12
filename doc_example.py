def word_lengths(sentence):
    '''
    Returns a list with lengths of all words in a sentence.

    >>> word_lengths('Hello world')
    [5, 5]
    >>> word_lengths('Once upon a midnight dreary')
    [4, 4, 1, 8, 6]
    >>> word_lengths('')
    []
    '''

    words = sentence.split()
    return [len(word) for word in words]


def count_negative(numbers):
    '''
    Count how many numbers in the given sequence are negative.

    >>> count_negative([])
    0
    >>> count_negative([1, 2, 3])
    0
    >>> count_negative([-1, -2, -3])
    3
    >>> count_negative([10, -10, -10, 10, 10, -20, -30, 0])
    4
    '''

    count = 0
    for i in numbers:
        if i < 0:
            count += 1
    
    return count