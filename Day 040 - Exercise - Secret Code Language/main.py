import random
import string

secretCode = input("Enter the Secret Code : ")

codingOrDecoding = input("\nWhat do you want?\nPress: 1 for Coding  \tPress: 2 for Decoding\n")

def reverse(secretCode):

    sizeOfCode = len(secretCode)
    
    reversedCode = ""
    for i in range(sizeOfCode - 1, -1, -1):
        reversedCode += secretCode[i]

    return reversedCode


def coding(secretCode):

    if(len(secretCode)<=3):
        return reverse(secretCode)
    else:
        # Slicing char and append first char at last
        secretCode =  secretCode[1:] + secretCode[0]

        # Adding 3 random char in front and end
        for i in range(6):
            randomChar = random.choice(string.ascii_letters)

            if i<3 : 
                secretCode = randomChar + secretCode
            else:
                secretCode =  secretCode + randomChar 
        
        return secretCode
        

def decoding(secretCode):

    if len(secretCode)<=3:
        return reverse(secretCode)
    else:
        secretCode = secretCode[3:-3] 
        secretCode = secretCode[-1] + secretCode[:-1]
        return secretCode



if codingOrDecoding=="1":
    print(coding(secretCode))
else:
    print(decoding(secretCode))