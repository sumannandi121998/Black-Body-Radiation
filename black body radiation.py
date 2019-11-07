""" comparing blackbody spectrum of COBE data with theoretical data 
name: Suman Nandi
Date: 06.11.2019"""


import matplotlib.pyplot as plt
import numpy as np 

h=6.625e-34 #Planck's Constant in SI
c=3.0e+8 #Speed of Light in SI
k=1.38e-23 #Boltzmann Constant in SI
T=2.725 #Temperature in K

#Plotting the Theoretical data
def I(a):
    b=(2*h*c*a**3)/(np.exp(h*c*a/(k*T))-1.0)
    return b
a=np.arange(200,2500,0.5)
plt.plot(a,I(a),'r-')

plt.xlabel('Frequency(1/m)')
plt.ylabel('Black body Radiation Flux(SI)')
plt.title('Plot of Black body Radiation vs Frequency')
plt.show()

#Plotting COBE  data
freq= np.loadtxt("nasa_txt.txt",delimiter="   ",usecols=[0])
cmb= np.loadtxt("nasa_txt.txt",delimiter="   ",usecols=[1])
frequency=100*freq[:] #Converting cm^(-1) to m^(-1)
cmb_flux=1.0e-20*cmb[:] #Converting MJy/sr to SI

plt.plot(frequency,cmb_flux)
plt.xlabel('Frequency(1/m)')
plt.ylabel('CMB Radiation Flux(SI)')
plt.title('Plot of CMB-Flux vs Frequency')
plt.show()

#superimpose the curve on the blackbody spectrum
plt.plot(a,I(a),'r-',label='Theoretical')
plt.plot(frequency,cmb_flux,'*',label='From the CMB data')
plt.xlabel('Frequency(1/m)')
plt.ylabel('Black body Radiation Flux(SI)')
plt.title('Comparison between two curves')
plt.legend()
plt.show()

#finding wave no for which flux is maximum
xmax=a[np.argmax(I(a))]
print ("wave no for which flux is maximum in SI:  ", xmax)