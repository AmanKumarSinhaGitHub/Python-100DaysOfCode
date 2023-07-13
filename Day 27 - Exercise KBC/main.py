# Basic KBC Game Program

def welcome():
    print("Welcome to KBC Game")

def endGame():
    print("The GAME IS OVER")

def askQues(quesNo):

    match quesNo:
        case 1: 
            ques1()
        case 2:
            ques2()
        case 3:
            ques3()
        case 4:
            ques4()
        case 5:
            ques5()
        case 6:
            ques6()
        case 7:
            ques7()
        case 8:
            ques8()
        case 9:
            ques9()
        case 10:
            ques10()
        case 11:
            print("You WIN")
            endGame()
        case -1:
            endGame()

quesNo = 1

def ques1():
    print("Which is the largest state in India?")
    print("1. Rajasthan  2. Madhya Pradesh  3. Uttar Pradesh  4. Maharashtra")
    global quesNo
    quesNo += 1
    correctAns = 1
    userAns = int(input("Your Answer : "))
    if(userAns != correctAns):
        print("You WIN Nothing")
        endGame()
    else:
        print("You WIN 10 Thousands\n")
        askQues(quesNo=2)
    

def ques2():
    print("What is the capital of India?")
    print("1. New Delhi  2. Mumbai  3. Chennai  4. Kolkata")
    correctAns = 1
    userAns = int(input("Your Answer : "))
    if(userAns != correctAns):
        print("You WIN 10 Thousands")
        endGame()
    else:
        print("You WIN 20 Thousands\n")
        askQues(quesNo=3)
    


def ques3():
    print("What is the national language of India?")
    print("1. Hindi  2. English  3. Tamil  4. Punjabi")
    correctAns = 1
    userAns = int(input("Your Answer : "))
    if(userAns != correctAns):
        print("You WIN 20 Thousands ")
        endGame()
    else:
        print("You WIN 50 Thousands \n")
        askQues(quesNo=4)
    

def ques4():
    print("What is the national flower of India?")
    print("1. Lotus  2. Rose  3. Sunflower  4. Jasmine")
    correctAns = 1
    userAns = int(input("Your Answer : "))
    if(userAns != correctAns):
        print("You WIN 50 Thousands\n")
        endGame()
    else:
        print("You WIN 1 Lakhs")
        askQues(quesNo=5)
    

def ques5():
    print("What is the national bird of India?")
    print("1. Peacock  2. Eagle  3. Parrot  4. Crow")
    correctAns = 1
    userAns = int(input("Your Answer : "))
    if(userAns != correctAns):
        print("You WIN 1 Lakhs")
        endGame()
    else:
        print("You WIN 5 Lakhs\n") 
        askQues(quesNo=6)
    
def ques6():
    print("What is the national fruit of India?")
    print("1. Mango  2. Apple  3. Banana  4. Grapes")
    correctAns = 1
    userAns = int(input("Your Answer : "))
    if(userAns != correctAns):
        print("You WIN 5 Lakhs")
        endGame()
    else:
        print("You WIN 10 Lakhs\n")
        askQues(quesNo=7)
    

def ques7():
    print("What is the national game of India?")
    print("1. Cricket  2. Hockey  3. Football  4. Badminton")
    correctAns = 2
    userAns = int(input("Your Answer : "))
    if(userAns != correctAns):
        print("You WIN 10 Lakhs")
        endGame()
    else:
        print("You WIN 20 Lakhs\n")
        askQues(quesNo=8)
    

def ques8():
    print("What is the national anthem of India?")
    print("1. Jana Gana Mana  2. Vande Mataram  3. Saraswati Vandana  4. Abhas Bharatam")
    correctAns = 1
    userAns = int(input("Your Answer : "))
    if(userAns != correctAns):
        print("You WIN 20 Lakhs")
        endGame()
    else:
        print("You WIN 50 Lakhs\n")
        askQues(quesNo=9)
    

def ques9():
    print("What is the national flag of India?")
    print("1. Tricolour  2. Ashoka Chakra  3. Saffron, White, Green  4. None of these")
    correctAns = 3
    userAns = int(input("Your Answer : "))
    if(userAns != correctAns):
        print("You WIN 50 Lakhs")
        endGame()
    else:
        print("You WIN 75 Lakhs\n")
        askQues(quesNo=10)
    

def ques10():
    print("Which is the largest desert in India?")
    print("1. Thar Desert  2. Rann of Kutch  3. Ladakh Desert  4. Great Indian Desert")
    correctAns = 1
    userAns = int(input("Your Answer : "))
    if(userAns != correctAns):
        print("You WIN 75 Lakhs")
        endGame()
    else:
        print("You WIN 5 Crore")

welcome()

askQues(quesNo=1)
