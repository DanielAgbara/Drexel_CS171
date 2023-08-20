#Purpose: Converting to Binary using Recursion
#Author: Daniel Agbara
#Date: 11/22/2021


#function block
def decimalToBinary(number):
    #division without remainder
    division = number // 2
    #division that give only the remainder
    remainder = number % 2
    #converting remainder to a string
    remainder = str(remainder)
    #base case
    if division == 0:
        return remainder
    else:
        return (decimalToBinary(division) + remainder)

#main block
if __name__ == "__main__":
    #reading data
    decimal = input("Enter a positive integer or 0 to end: ")
    #validation loop and block
    while True:
        #try and except block
        try:
            decimal = int(decimal)
            #validation to make sure that the nuimber entered is a negative value
            if decimal < 0:
                print("Error: you entered a negative value. Try again")
                decimal = input("Enter a positive integer or 0 to end: ")
            #if the number entered is 0 the loop stops
            elif decimal == 0:
                break 
            #if the correct integer numbers are entered
            elif decimal > 0:
                #calling the function
                binary = decimalToBinary(decimal)
                print("The equivalent of {:d} in Binary is {:s}".format(decimal, binary))
                decimal = input("Enter a positive integer or 0 to end: ")
        except:
            print("Error: An integer value was expected. Try again")
            decimal = input("Enter a positive integer or 0 to end: ")
        
