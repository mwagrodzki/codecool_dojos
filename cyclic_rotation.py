def cyclic_rotation(string, number):
    '''
    Calculate a cyclic rotation of a string; i.e. move 
    the last N elements from the end to the beginning.
    python3 -m doctest cyclic_rotation.py
    
    >>> cyclic_rotation('abcde', 2)
    'deabc'
    >>> cyclic_rotation('aaabb', 3)
    'abbaa'
    >>> cyclic_rotation('asdfg', 1)
    'gasdf'
    '''

    return string[(-1 * number):] + string[:(-1 * number)]
