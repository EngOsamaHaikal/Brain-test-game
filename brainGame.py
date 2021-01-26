import random as rand
print("Brain Test Game \n ")

def playGame() :
    
 numberOfPlays=0
 score=0
 answerIS=True    
 while answerIS:
    numberOfPlays=numberOfPlays+1
    a=rand.randrange(0,21,1)
    b=rand.randrange(0,21,1)
 
    Sum=a+b 
    Answers=[0,0,0,0]

    LocOfCorrect=rand.randrange(0,4,1)
        

    for i in range(4):
     if i==LocOfCorrect :
        Answers[i]=Sum
     else :
        InCorrectAnswer=rand.randrange(0,41,1)
        Answers[i]=InCorrectAnswer     
        while  InCorrectAnswer==Sum   :
           InCorrectAnswer=rand.randrange(0,41,1)
           Answers[i]=InCorrectAnswer
    print("Questoin is :\n")           
    print(str(a)+ " +" + str(b)+"\n")

    print(Answers)    
    print("\n")

    UserInput=input("what is the Sum of these two numbers ? \n")
   
    if int(UserInput)==Sum :
        score=score+1

        print("Correct ! "+"\n")
        print("your Score is : " + str(score)+"/"+str(numberOfPlays)+"\n")
    else :
        print("Wrong ! ")
        print("your Score is : " + str(score)+"/"+str(numberOfPlays)+"\n")



    print("Do you want to Play Again ?  \n")  
    choiceIs=input("yes or no : \n")

    if choiceIs=="yes" :
            
        continue
    if choiceIs=="no"  :
        print("thank you")   
        break
           
 
playGame()