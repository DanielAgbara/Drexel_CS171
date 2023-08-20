#Purpose: Determing the BAC for A Person
#Author: Daniel Agbara
#Date: 8/11/2021

def computeBloodAlcoholConcentration(drinks, weight, duration):
    reduction = (duration // 40) * 0.1         
    BACM = ((drinks / weight) * 3.8) - reduction
    BACF = ((drinks / weight) * 4.5) - reduction
    
    return BACM, BACF

def impairment(bac):
    if (bac == 0):
        message = 'Safe to Drive'
    elif (0 < bac < 0.04):
        message = 'Some Impairment'
    elif (0.04 <= bac < 0.08):
        message = 'Driving Skills Significantly Affected'
    elif (0.08 <= bac < 0.1):
        message = 'Criminal Penalties in Most US States'
    elif bac >= 0.1:
        message = 'Legally Intoxicated - Criminal Penalties in All US States'
        
    return message


def showImpairmentChart(weight, duration, sex):
    if (sex =='f') or (sex =='F'):
        sex_name = 'female'
    else:
        sex_name = 'male'
        
        

    print('{:d} pounds, {:s}, {:d} minute(s) since last drink'.format(weight, sex_name, duration))
    print('{drink:9}{BAC:8}Status'.format(drink= '#drinks', BAC='BAC'))
    for i in range(0, 12):
        drinks = i
        BAC_M_F = computeBloodAlcoholConcentration(drinks, weight, duration)
        if (sex == 'm') or (sex == 'M'):
            bac = BAC_M_F[0]
        elif (sex == 'f') or (sex == 'F'):
            bac = BAC_M_F[1]
        
        Status = impairment(bac)
        print('{drink:<9}{BAC:<8}{message}'.format(drink = drinks, BAC = bac, message = Status))


def promptForInteger(lower, upper):
    while True:
        try:
            integer = int(input())
            if (lower <= integer < upper):
                break
            else:
                print("Error: Value out of bounds")
        except:
            print("Error: An ineger value was expected. Try again")
    
    return integer




def promptForMorF():
    while True:
            MorF = input()
            if (MorF == 'f') or (MorF == 'F') or (MorF == 'm') or ( MorF == 'M'):
                break
            else:
                continue
    
    return MorF


if __name__ == '__main__':
    print('Enter your weight (in lbs): ')
    weight = promptForInteger(0, 500)
    print('How many minutes has it been since your last drink? ')
    duration = promptForInteger(0, 300)
    print('Enter your sex as M or F: ')
    sex = promptForMorF()
    showImpairmentChart(weight, duration, sex)