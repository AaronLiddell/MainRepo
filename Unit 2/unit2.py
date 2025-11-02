#Unit 2
#Computer Modelling
#Aaron Liddell

import numpy as np
from matplotlib import pyplot as plt
from tabulate import tabulate

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

    print("Task 1a: \n Zero array",m_zeros,"\n Array to n numbers",array_to_n,"\n Random 2d array \n",random_2d)

    return m_zeros, array_to_n, random_2d

def task1c(m,n):
    m_zeros, array_to_n, random_2d = task1a(m,n)
    
    ave_array_to_n = np.average(array_to_n)
    max_random_2d = np.max(random_2d)

    print("\n Task 1c: \n Mean of second array:",ave_array_to_n,"\n Max value of third array",max_random_2d)

    return ave_array_to_n, max_random_2d

def task1d(a):
    a = np.array([2,4,6,8,10])
    a_squ = a.copy 
    a_squ = a*a
    print("\n Task 1d: \n Array is:",a,"\n Square of array is:",a_squ )  

    #mutable objects can be changed once its been created, while an immutable object cant be.
    #mutable, an operation to object a would effect object b
    #immutable, changing object a does not effect b

def task2a(n):
    M = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            M[i, j] = i + 2*j
    print("\n Task 2a: \n Square nxn array:\n",M)
    return M

def task2b(n):
    sumM = 0
    M = task2a(n)
    for j in range(n):
        sumM += M[:, j]
    print("\n Task 2b: \n Sum of task 2a:",sumM)

def task3(d, mu, sigma):
    logL = -1/2 * np.sum(((d-mu)/sigma)**2)
    print("\n Task 3: \n Gaussian log likelyhood:",logL)


def task4():
    data = np.genfromtxt("data.txt")
    omegamh2 = data[:, 0]
    omegabh2 = data[:, 1]
    H0 = data[:, 2]

    #calulate each mean
    mean_omegamh2 = np.average(omegamh2)
    mean_omegabh2 = np.average(omegabh2)
    mean_H0 = np.average(H0)

    #calculate each standard deviation
    std_omegamh2 = np.std(omegamh2)
    std_omegabh2 = np.std(omegabh2)
    std_H0 = np.std(H0)

    #show each histogram
    plt.hist(data[:,0], bins=20)
    plt.title("Omegamh2 histogram")
    plt.ylabel("Omegamh2")
    plt.savefig("Omegamh2Histo.jpg")
    plt.show()
    
    plt.hist(data[:,1], bins=20)
    plt.title("Omegabh2 histogram")
    plt.ylabel("Omegabh2")
    plt.savefig("Omegabh2Histo.jpg")
    plt.show()
    
    plt.hist(data[:,2], bins=20)
    plt.title("H0 histogram")
    plt.ylabel("H0")
    plt.savefig("H0Histo.jpg")
    plt.show()

    #show each scatter plot
    plt.scatter(data[:,0],data[:,1])
    plt.title("omegabh2 against omegamh2")
    plt.xlabel("Omegamh2")
    plt.ylabel("Omegabh2")
    plt.savefig("Omegabh2VsOmegamh2.jpg")
    plt.show()

    plt.scatter(data[:,1],data[:,2])
    plt.title("H0 against Omegabh2")
    plt.xlabel("Omegabh2")
    plt.ylabel("H0")
    plt.savefig("H0VsOmegabh2.jpg")
    plt.show()

    plt.scatter(data[:,0],data[:,2])
    plt.title("H0 against Omegamh2")
    plt.xlabel("Omegamh2")
    plt.ylabel("H0")
    plt.savefig("H0VsOmegamh2.jpg")
    plt.show()

    #calculate 5th and 95th percentiles for each column of data
    percent_omegamh2 = np.percentile(omegamh2, [5,95])
    percent_omegabh2 = np.percentile(omegabh2, [5,95])
    percent_H0 = np.percentile(H0, [5,95])

    #create table for all numerical data
    rows = [
        ["omegamh2", f"{mean_omegamh2:.6g}", f"{std_omegamh2:.6g}", f"{percent_omegamh2[0]:.6g}, {percent_omegamh2[1]:.6g}"],
        ["omegabh2", f"{mean_omegabh2:.6g}", f"{std_omegabh2:.6g}", f"{percent_omegabh2[0]:.6g}, {percent_omegabh2[1]:.6g}"],
        ["H0",        f"{mean_H0:.6g}",        f"{std_H0:.6g}",        f"{percent_H0[0]:.6g}, {percent_H0[1]:.6g}"]
    ]

    headers = ["Column", "Mean", "StdDev", "5th and 95th percentiles"]
    table_str = tabulate(rows, headers=headers, tablefmt="github")

    with open("table.txt", "w", encoding="utf-8") as f:
        f.write(table_str + "\n")


def main():

    task1c(2,4)

    task1d(5)

    task2b(4)
    
    #runs task 4.3
    d = np.array([1,2,3])
    mu = np.array([6,7,8])
    sigma = np.array([1,2,3])
    task3(d, mu, sigma)

    task4()




main()