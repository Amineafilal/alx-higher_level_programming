#!/usr/bin/env python3
"""
Module for lazy_matrix_mul.
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Function to perform matrix multiplication using NumPy.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        numpy.ndarray: The result of the matrix multiplication.

    Raises:
        ValueError: If matrices cannot be multiplied.

    Example:
    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    array([[ 7, 10],
           [15, 22]])
    >>> lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]])
    array([[13, 16]])
    """
    try:
        result = np.dot(np.array(m_a), np.array(m_b))
        return result
    except ValueError as e:
        raise ValueError("Matrix shapes invalid for multiplication") from e

if __name__ == "__main__":
    import doctest
    doctest.testmod()
