#CS171 - Week 3 Homework 2
#Purpose: Converting Phone Numbers
#Auhtor: Daniel Agbara
#Date: 10/13/2021


alphabets = ['A','B','C','D','E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#I will creat a list with number from 2 - 9, the numbers are repeated multiple times because one number refers to different alphabets
Numbers = [2, 2, 2, 3, 3, 3, 4, 4 ,4, 5, 5, 5, 6, 6, 6, 7, 7, 7,7, 8, 8, 8, 9, 9, 9, 9]

print("Phone Number Translator")
number = input("Enter a phone number in the format XXX-XXX-XXXX: ")
#Divide the string into parts
first_part = number[0:3]
second_part = number[4:7]
third_part = number[8:]

#converting the second and third part to numbers 
# by using the index function to find their position 
# in the alphabets list and then finding the number 
# that has that same position in the number list
num1 = alphabets.index(second_part[0])
str1 = str(Numbers[num1])
num2 = alphabets.index(second_part[1])
str2 = str(Numbers[num2])
num3 = alphabets.index(second_part[2])
str3 = str(Numbers[num3])
new_second_part = str1 + str2 + str3
num4 = alphabets.index(third_part[0])
str4 = str(Numbers[num4])
num5 = alphabets.index(third_part[1])
str5 = str(Numbers[num5])
num6 = alphabets.index(third_part[2])
str6 = str(Numbers[num6])
num7 = alphabets.index(third_part[3])
str7 = str(Numbers[num7])
new_third_part = str4 + str5 + str6 + str7

#concatinating all the parts into one new number
new_number = first_part + '-' + new_second_part + '-' + new_third_part
print("Dial: {:s}".format(new_number))
