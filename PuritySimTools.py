import numpy as np
import scipy.constants as constant
import math 

class PuritySimTools:

    #this function takes as input a list with the resistances and sums them in series
    @staticmethod
    def R_in_series(input_list):
        return sum(input_list)

    #this function takes as input a list with the resistances and sums them in parallel
    @staticmethod
    def R_in_parallel(input_list):
        return sum(input_list)/np.prod(np.array(input_list))

    #this function takes as input a list with the capacities and sums them in series
    @staticmethod
    def C_in_series(input_list):
        #return sum(input_list)/np.prod(np.array(input_list))
        new_list = []
        for i in range(len(input_list)):
            new_list.append(pow(input_list[i],-1))
        sum_new_list = sum(new_list)
        return pow(sum_new_list,-1)

    #this function takes as input a list with the capacities and sums them in parallel
    @staticmethod
    def C_in_parallel(input_list):
        return sum(input_list)

    #this function takes as input an area, a length, a resistivity and returns the resistance in Ohm
    @staticmethod
    def R_from_rho(area, length, resistivity):
        return resistivity*(length/area)

    #this function takes as input an area, a length, a conductivity and returns the resistance in Ohm
    @staticmethod
    def R_from_sigma(area, length, conductivity):
        return (length/area)/conductivity

    #this function takes as input a dielectric constant, the distance between two plates, the areas of the two plates, and returns a capacitance value in Farad
    @staticmethod
    def C_from_plates(dielectric, distance, area1, area2):
        return  constant.epsilon_0*dielectric*(area1*area2)/(distance*(area1+area2))

    #this function evaluates the area given a radius
    @staticmethod
    def area_radius(radius):
        return (radius**2)*math.pi

    #this function evaluates the conductivity from the electron mobility
    @staticmethod
    def e_conductivity(density, mobility):
        return constant.e*density*mobility

