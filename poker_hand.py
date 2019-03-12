def poker_hand(table):
    '''
    Write a poker_hand function that will score a poker hand. The function 
    will take an array 5 numbers and return a string based on what is inside. 
    python3 -m doctest poker_hand.py
    
    >>> poker_hand([1, 1, 1, 1, 1])
    'five'
    >>> poker_hand([2, 2, 2, 2, 3])
    'four'
    >>> poker_hand([1, 1, 1, 2, 3])
    'three'
    >>> poker_hand([2, 2, 3, 3, 4])
    'twopairs'
    >>> poker_hand([1, 2, 2, 3, 4])
    'pair'
    >>> poker_hand([1, 1, 2, 2, 2])
    'fullhouse'
    >>> poker_hand([1, 2, 3, 4, 6])
    'nothing'
    '''

    temp = [table.count(x) for x in set(table)]

    if 5 in temp:
        return 'five'
    elif 4 in temp:
        return 'four'
    elif 3 in temp and not 2 in temp:
        return 'three'
    elif 3 in temp and 2 in temp:
        return 'fullhouse'
    elif 2 in temp:
        k = temp.count(2)
        if k == 1:
            return 'pair'
        elif k == 2:
            return 'twopairs'
    return 'nothing'
