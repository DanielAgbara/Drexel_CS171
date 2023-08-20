#Purpose:
#Author:Daniel Agbara
#Date: 06/12/2021

def createReport(filename):
    f = open(filename, 'r')
    w = open('US-stats.txt', 'w')
    totalmedals = 0
    totalGmedals = 0
    totalSmedals = 0
    totalBmedals = 0
    #reading the line in the f
    lines = f.readlines()
    #loop block
    for i in lines:
        line_content = i.split()
        if type(line_content[1]) == str:
            sport = line_content[0] + ' ' + line_content[1]
            sportmedal= 0
            totalGmedals += int(line_content[-3])
            totalSmedals += int(line_content[-2])
            totalBmedals += int(line_content[-1]) 
            for j in line_content[2:]:
                n = int(j)
                totalmedals += n
                sportmedal += n
            
            if sportmedal > 0:
                w.write("{:s}: {:d} medals\n".format(sport, sportmedal))
        else:
            sport = line_content[0]
            sportmedal = 0
            totalGmedals += int(line_content[-3])
            totalBmedals += int(line_content[-2])
            totalGmedals += int(line_content[-1]) 
            for j in line_content[1:]:
                n = int(j)
                totalmedals += n
                sportmedal += n
            
            if sportmedal > 0:
                w.write("{:s}: {:d} medals\n".format(sport, sportmedal))
    
    w.write('Total medals: {:d}\n'.format(totalmedals))
    w.write('Total Gold medals: {:d}\n'.format(totalGmedals))
    w.write('Total Silver medals: {:d}\n'.format(totalSmedals))
    w.write('Total Bronze medals: {:d}\n'.format(totalBmedals))
    
                




def getFileName():
    filename = input("Enter name of the data file: ")
    while True:
        try:
            f = open(filename)
            break
        except:
            print("Error: that file does not exist. Try again.")
            filename = input("Enter name of the data file: ")
    return filename


# main script
if __name__ == "__main__":

    # Get data file 
    filename = getFileName()
    # Call report function
    createReport(filename)
    # End program
    print('Done. Results saved in output file.')