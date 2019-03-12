def most_frequent(table):
    '''
    Check what is the most frequent number in an array. If there are 
    multiple such numbers, return the largest one. 
    python3 -m doctest most_frequent.py
    
    >>> most_frequent([3, 3, 3, 2, 2, 2, 4, 4])
    3
    >>> most_frequent([3, 3, 2, 2, 2, 4, 4])
    2
    >>> most_frequent([1, 2, 3, 4, 5])
    5
    '''

    return max(set(table), key=table.count())

