#CS171 - Week 3 Homework 1
#Purpose: Percipitation for 12 Months
#Author: Daniel Agbara
#Date: 10/13/2021

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
precipitation = []

January = float(input('Enter total precipitation for January: '))
February = float(input('Enter total precipitation for February: '))
March = float(input('Enter total precipitation for March: '))
April = float(input('Enter total precipitation for April: '))
May = float(input('Enter total precipitation for May: '))
June = float(input('Enter total precipitation for June: '))
July = float(input('Enter total precipitation for July: '))
August = float(input('Enter total precipitation for August: '))
September = float(input('Enter total precipitation for September: '))
October = float(input('Enter total precipitation for October: '))
November = float(input('Enter total precipitation for November: '))
December = float(input('Enter total precipitation for December: '))

precipitation.append(January)
precipitation.append(February)
precipitation.append(March)
precipitation.append(April)
precipitation.append(May)
precipitation.append(June)
precipitation.append(July)
precipitation.append(August)
precipitation.append(September)
precipitation.append(October)
precipitation.append(November)
precipitation.append(December)

print()
total_precipitation = sum(precipitation)
average_precipitation = sum(precipitation) / len(precipitation)
max_precipitation = max(precipitation)
min_precipitation = min(precipitation)
max_month = months[precipitation.index(max_precipitation)]
min_month = months[precipitation.index(min_precipitation)]
print("Total precipitation: {:.2f} inches.".format(total_precipitation))
print("Average Precipitation: {:.2f} inches.".format(average_precipitation))
print("{:s} has the highest precipitation: {:.2f} inches.".format(max_month, max_precipitation))
print("{:s} has the lowest precipitation: {:.2f} inches.".format(min_month, min_precipitation))


