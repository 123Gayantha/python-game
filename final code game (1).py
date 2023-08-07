6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666import random
#Creating variables..........................................................................................

RandomHiddenPegs = []
score = 100
numbers = [1,2,3,4,5,6]
RandomHiddenPegs = (random.sample(numbers,  k=4)) #Keyword
#print(RandomHiddenPegs)

counter = 0 #(Attempts)
PegLocationList = ""
ZeroList = [0,0,0,0] 
GuessPeg1 = 0
GuessPeg2 = 0
GuessPeg3 = 0
GuessPeg4 = 0



#Genarating random list........................................................................................
StudentName=input("Enter your name :")
print("                            Hi",StudentName,"Welcome to Gamelnt")
print()
print("Number to guess -",RandomHiddenPegs,"           Colour Mapping:")
print("                                                1-White 2-Blue 3-Red")
print("                                                4-Yellow 5-Green 6-Purple")
print()
print("Attempt No                                    ")
print()
      

#Process.....................................................................................................

while (counter <= 7):
    PlayerGuessList = []
    GuessPeg1 = int(input("Guess1: "))
    GuessPeg2 = int(input("Guess2: "))
    GuessPeg3 = int(input("Guess3: "))
    GuessPeg4 = int(input("Guess4: "))
    
    PlayerGuessList.append(GuessPeg1)
    PlayerGuessList.append(GuessPeg2)
    PlayerGuessList.append(GuessPeg3)
    PlayerGuessList.append(GuessPeg4)
    print(PlayerGuessList)

    if PlayerGuessList == ZeroList:
        print("You ended the game")
        break
        
        
    if PlayerGuessList == RandomHiddenPegs:
        print("Congratulations !!!! You have won the game...")
        print("Your score is:",score) 
        break


    
#cheking for conditions...................................................................................................

    
    if PlayerGuessList[0]== RandomHiddenPegs[0]:
        PegLocation1 = "1"
        print(PegLocation1)

    elif PlayerGuessList[0] in RandomHiddenPegs :
        PegLocation1 = "0"
        print(PegLocation1)


    else:
        PegLocation1 = "."
        print(PegLocation1)



    if PlayerGuessList[1]== RandomHiddenPegs[1]:
        PegLocation2 = "1"
        print(PegLocation2)

    elif PlayerGuessList[1] in RandomHiddenPegs :
        PegLocation2 = "0"
        print(PegLocation2)

    else:
        PegLocation2 = "."
        print(PegLocation2)



    if PlayerGuessList[2]== RandomHiddenPegs[2]:
        PegLocation3 = "1"
        print(PegLocation3)

    elif PlayerGuessList[2] in RandomHiddenPegs :
        PegLocation3 = "0"
        print(PegLocation3)

    else:
        PegLocation3 = "."
        print(PegLocation3)



    if PlayerGuessList[3] == RandomHiddenPegs[3]:
        PegLocation4 = "1"
        print(PegLocation4)

    elif PlayerGuessList[3] in RandomHiddenPegs :
        PegLocation4 = "0"
        print(PegLocation4)

    else:
        PegLocation4 = "."
        print(PegLocation4)

    counter = counter + 1
    score = score/counter
    print("Number of attempts: ",counter)    



   
            
        

            
            
            
            


        
        

