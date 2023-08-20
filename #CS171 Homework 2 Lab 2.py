#CS171 Homework 2 Lab 2
#Purpose 1: Determine number of slices a pizza of any sizes can be divided into
#Purpose 2: Determine the number of pizza a customer should order
#Author: Daniel Agbara
#Date: 10/02/2021

import math
#defining my function for slices per pizza
def slicesPerPizza(diameter_pizza):
    area_of_slice = 14.125
    radius_pizza = diameter_pizza / 2
    area_pizza = math.pi * math.pow(radius_pizza, 2)
    no_of_slices = math.floor(area_pizza / area_of_slice)
    return no_of_slices

#Defining my function for number of pizza to be ordered

def PizzaOrdered(no_of_people, slices_per_pizza):
    average_slices = no_of_people * 3
    no_of_pizza = math.ceil(average_slices / slices_per_pizza)
    return no_of_pizza

if __name__=="__main__":
    print("Welcome to Mario and Luigi's Pizzeria")
    print()
    #Reading the data from the user
    diameter_pizza = int(input("Enter the diameter of the pizzas you want to order (in inches): "))
    no_of_people = int(input("Enter the number of people in your party: "))
    #Determining numbers of slices per pizza through the function made
    slices_per_pizza = slicesPerPizza(diameter_pizza)
    #Determing the number of pizza that needs to be ordered
    pizza_number = PizzaOrdered(no_of_people, slices_per_pizza)
    print("For a party of", no_of_people,"people you need to order", pizza_number, "pizza(s).")
    print("A", diameter_pizza,"inch pizza will yield", slices_per_pizza, "slices.")
