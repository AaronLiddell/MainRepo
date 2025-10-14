#Unit 2
#Computer Modelling
#Aaron Liddell

import numpy as np

def task1a(m,n):
    """
    Create a 1D array of all zeros of size m.
    Create a 1D array of all whole numbers from 1 to n inclusive.
    Create a 2d array of random numbers in the range [0,1)
    
    Parameters
    ----------
    m: any whole number
    n: any whole number

    Returns
    -------
    out: each array is returned
    """

    m_zeros = np.zeros(m)
    array_to_n = np.arange(1, n+1, 1)
    random_2d = np.random.rand(m,n)

    return array_to_n, random_2d

def task1c(m,n):
    array_to_n, random_2d = task1a(m,n)
    
    ave_array_to_n = np.average(array_to_n)
    max_random_2d = np.max(random_2d)

def task1d(a):
    a = a*a
    print(a)
    
            

def main():
    a = np.array([1,2,3])
    task1d(a)


main() 