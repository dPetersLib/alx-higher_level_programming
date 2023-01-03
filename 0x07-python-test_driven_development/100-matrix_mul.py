#!/usr/bin/python3
"""Matix Multiplication

It takes two matrices and returns their multiple
"""
def matrix_mul(m_a, m_b):
    """A function to multiply two matrices
    
    This function takes in two lists of lists (i.e. matrices),
    multiplies them and returns their multiple.

    Args:
        m_a (list) : this is the first matrix. It is a list of lists.
        m_b (list) : this is the second matrix, it is also a list of lists.
    
    Returns:
        a new matrix
    """
    
    # m_a amd m_b must be lists
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    
    # m_a amd m_b must be list of lists of int or floats
    is_list_list_a = True
    for item in m_a:
        if type(item) != list:
            is_list_list_a = False
    if not is_list_list_a:
        raise TypeError("m_a must be a list of lists")
    is_list_list_b = True
    for item in m_b:
        if type(item) != list:
            is_list_list_b = False
    if not is_list_list_b:
        raise TypeError("m_b must be a list of lists")
    
    # m_a and m_b cannot be empty
    if len(m_a) == 1 and len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 1 and len(m_b[0] == 0):
        raise ValueError("m_b can't be empty")

    # each element in the lists of m_a and m_b must be int or float
    lenght_a = []
    for l in m_a:
        for i in l:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
        if l in lenght_a:
            continue
        else:
            lenght_a.append(len(l))
    # must be a rectangle
    if len(lenght_a) > 1:
        print("len MA: ", lenght_a)
        raise TypeError("each row of m_a must be of the same size")
    
    lenght_b = []
    for l in m_b:
        for i in l:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
        if l not in lenght_b:
            lenght_b.append(len(l))
    # must be a rectangle
    if len(lenght_b) > 1:
        raise TypeError("each row of m_a must be of the same size")
    
    # m_a row must equal m_b column and vise versa
    if lenght_a != len(m_b) or len(m_a) != lenght_b:
        raise ValueError("m_a and m_b can't be multiplied")
    
    # IF ALL VALIDATION PASS, WE THEN DO THE MULTIPLICATION :)

    c = []

    for x in range(len(m_a)):
        for y in range(len(m_b[0])):
            for z in range(len(m_b)):
                c.append(list(m_a[x][y] * m_b[z][y]))
    return c

