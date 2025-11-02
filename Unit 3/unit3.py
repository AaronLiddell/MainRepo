#Computer Modelling
#Aaron Liddell
#Unit 1

import matplotlib.pyplot as plt
import numpy as np
from scipy import constants

def main():
    
    integrand = demoCosmology() #to test the functions in the Cosmology class

    #c = Cosmology(H0, Omega_m, Omega_lambda)
    #graphVaryZ()
    #graphVaryOmegaM()
    #graphSetOmegaM()
    #printCosmo()
    

class Cosmology:
    def __init__(self,H0,Omega_m,Omega_lambda):         #__init__ is used to initalise variables when a new instance of the class is created
        self.H0=H0                                      #self is used so that when a new instance is created, the attributes of the class keep their original value
        self.Omega_m = Omega_m
        self.Omega_lambda = Omega_lambda
        self.Omega_k = round(1 - (self.Omega_lambda + self.Omega_m),6)

    def computeIntegrand(self, z):
        integrand = 1/np.sqrt(self.Omega_m*(1+z)**3 + self.Omega_k*(1+z)**2 + self.Omega_lambda)
        return integrand
    
    def univFlat(self):
        if self.Omega_k == 0:
            print("Universe is flat")
        else:
            print("Universe is NOT flat")
        return self.Omega_k

    def modLambda(self, new_Omega_m):
        self.Omega_m = new_Omega_m
        self.Omega_lambda = 1 - self.Omega_m
        return self.Omega_lambda
    
    def modM(self, new_Omega_lambda):
        self.Omega_lambda = new_Omega_lambda
        self.Omega_m = 1 - self.Omega_lambda
        return self.Omega_m
    
    def calcOmegamh2(self):
        h = self.H0/100
        Omegamh2 = self.Omega_m*h**2
        return Omegamh2
    
    def __str__(self):
        return (f"Cosmology with H0 = {self.H0}, Omega_m = {self.Omega_m}, Omega_lambda = {self.Omega_lambda}, Omega_k = {self.Omega_k}")
    
    def rectangle(self, n, z):
        delta_x = z/n
        integral = 0
        
        for i in range(n):
            xi = i*delta_x
            integral += self.computeIntegrand(xi)

        integral = delta_x * integral
        distance = integral *((constants.speed_of_light/1000) / self.H0)
        print("distance", distance) #in units Mpc

    def trap(self, n, z):
        delta_x = z/(n-1)
        integral = 0

        for i in range(n-1):
            xi = i*delta_x
            integral += self.computeIntegrand(xi)
            
        
        


def demoCosmology():
    cosmo = Cosmology(72, 0.3, 0.7)
    z = 1
    
    """print(cosmo)

    omegaK = cosmo.univFlat()
    print("Omega k is: ",omegaK)"""

    #integrand = cosmo.computeIntegrand(z)
    #print("The result of the integrand is: ",integrand)

    cosmo.rectangle(10000, z)
    cosmo.trap(10000,z)


def graphVaryZ():
    cosmo = Cosmology(70, 0.3, 0.7)
    xVal = np.linspace(0,1,100)
    yVal = cosmo.computeIntegrand(xVal)
    plt.plot(xVal,yVal)
    plt.grid()
    plt.xlabel("z values")
    plt.ylabel("integrand")
    plt.title("integrand against z")
    plt.show()

def graphVaryOmegaM():
    xVal = np.linspace(0, 1, 100)
    Omega_m_values = [0.2, 0.3, 0.4]
    for Omega_m in Omega_m_values:
        cosmo = Cosmology(70, Omega_m, 1-Omega_m)
        yVal = cosmo.computeIntegrand(xVal)
        plt.plot(xVal, yVal, label=f"Omega m = {Omega_m}")
    plt.xlabel("z values")
    plt.ylabel("integrand")
    plt.title("Integrand for different omega m")
    plt.legend()
    plt.show()
    #changing Omega m by a small amount has a large affect on the integrand. 
    #smaller omega m results in a larger integrand for high z, but integand will converge for all omega m at low z

def graphSetOmegaM():
    cosmo = Cosmology(70, 0.3, 0.7)
    xVal = np.linspace(0, 1, 100)
    Omega_m_values = [0.2, 0.3, 0.4]

    for Omega_m in Omega_m_values:
        cosmo.modLambda(Omega_m)        #updates Omega_m in Cosmology class for cosmo instance 
        yVal = cosmo.computeIntegrand(xVal)
        plt.plot(xVal,yVal, label=f"Omega m = {Omega_m}. Omega lambda = {cosmo.Omega_lambda}")
    
    plt.xlabel("z values")
    plt.ylabel("integrand")
    plt.title("Integrand for different omega m, with one Cosmology object")
    plt.legend()
    plt.show()
    
    #appears to be no difference in the plot where multiple objects of Cosmology were made, and where only one object was made.
    #input values are the same between the two plots, so this makes sense

def printCosmo():
    c1 = Cosmology(70, 0.2, 0.8)    #assuming 0 curvature
    c2 = Cosmology(80, 0.5, 0.3)
    c3 = Cosmology(90, 0.4,0.5)
    print(c1)
    print(c2)
    print(c3)

    #Each instance of Cosmology is printed with its associated parameters that are defined in the initalising method.
    #Omega_k is calculated using Omega_lambda and Omega_m.

if __name__ == "__main__":
    
    main()




   