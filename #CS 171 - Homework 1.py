#CS 171 - Homework 1
#Purpose:  ADD A BRIEF EXPLANATION OF PURPOSE OF THE PROGRAM HERE
#Author:   ADD YOUR FIRST AND LAST NAME HERE
#Date:     ADD THE DATE WHEN YOU WORK ON THIS PROBLEM 

# Define any functions you need to
def calculate_shipping_charges(weight, shipping_rate):
    shipping_charges = weight * shipping_rate
    return shipping_charges

def roundFloat(shipping_charges):
    shipping_charges = shipping_charges * 100
    shipping_charges = int(shipping_charges)/100
    return shipping_charges
# Instructions to the user
print("Shipping Charges Calculator")
print()
weight = input("Enter the weight of your parcel in pounds: ")
weight = float(weight)
shipping_rate = input("Enter the shipping price per pound: ")
shipping_rate = float(shipping_rate)


# Get input from the user


# Calculate the shipping charges
shipping_charges = calculate_shipping_charges(weight, shipping_rate)

# Round the result to display the shipping charges to the nearest hundredth
shipping_charges = roundFloat(shipping_charges)

# Display the results
print("The weight of the parcel is", weight, "pounds")
print("The shipping price per pound is", shipping_rate,"dollars")
print("The shipping charges for your parcel is",shipping_charges,"dollars")