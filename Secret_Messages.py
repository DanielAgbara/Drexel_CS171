#Purpose:
#Author: Daniel Agbara
#Date: 11/19/2021


def encode(originalMsg, code):
    text = open(code, 'r')
    save = open("secret.txt", 'w')
    key= text.readline()
    elements_in_key = []
    encodedMsg = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elements_in_alphabets = []

    for i in key:
        elements_in_key.append(i)
    
    for i in alphabets:
        elements_in_alphabets.append(i)
    
    for i in originalMsg:
        for j in i:
            if j in elements_in_alphabets:
                position = elements_in_key.index(j)
                encodedMsg += elements_in_alphabets[position]
            else:
                encodedMsg += j
    
    return encodedMsg

    

def decode(codedMsg, code):
    Msg = open(codedMsg, "r")
    text = open(code, 'r')
    cryptedMsg= Msg.readline()
    key = text.readline()
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elements_in_key = []
    elements_in_alphabets = []
    decodedMsg = ''
    for i in alphabets:
        elements_in_alphabets.append(i)
    
    for i in key:
        elements_in_key.append(i)
    
    for i in cryptedMsg:
        for j in i:
            if j in elements_in_alphabets:
                position = elements_in_alphabets.index(j)
                decodedMsg += elements_in_key[position]
            else:
                decodedMsg += j
    
    return decodedMsg


if __name__ == "__main__":
    print("Enter E to encode a message.")
    print("Enter D to decode a message.")
    choice = input("Enter your choice: ")
    while True:
        if (choice == 'd') or (choice == 'D') or (choice == 'e') or (choice == 'E'):
            break
        else:
            print("Error: You must enter E or D")
            choice = input("Enter your choice: ")

    if choice == 'E' or (choice == 'e'):
        code_name = input("Enter name of the file that has the code: ")
        save = open("secrets.txt", "w")
        while True:
            try:
                test = open(code_name)
                break
            except:
                print('Error: that file does not exist')
                code_name = input("Enter name of the file that has the code: ")
        
        message = input("Enter the message you want to encode: ")
    
        encodedMsg = encode(message, code_name)

        print()
        print("Encoded message:", encodedMsg)
        save.write(encodedMsg)
        print("Encoded message has been saved in secret.txt")
    elif (choice == 'D') or (choice == 'd'):
        code_name = input("Enter the name of the file that has the code: ")
        while True:
            try:
                test = open(code_name)
                break
            except:
                print('Error: that file does not exist')
                code_name = input("Enter name of the file that has the code: ")

        message = input("Enter name of the file that has the message to decode: ")
        while True:
            try:
                test = open(message)
                break
            except:
                print('Error: that file does not exist')
                message = input("Enter name of the file that has the code: ") 
              
        cryptedMsg = open(message, 'r')
        cryptedMsg = cryptedMsg.readline()
        decodedMsg = decode(message, code_name)
        
        print()
        print("Encoded message:", cryptedMsg)
        print("Decoded message:", decodedMsg)