import time
print("Enter the key to play game. ",end="")
key=int(input("Input 4 number key: "))
count=0
score=0
while key!=1111:
    print("Wrong key, please try again. ",end="")
    count+=1
    key=int(input("Input 4 number key: "))
    if count==5:
        print("The number of entered keys is reached the max, GAME END!")
        quit()
if key==1111:
    print("Welcome to the game")
    print("Do you want to start the game? Enter Yes or No: ",end="")
    pl=input()
    if pl!="Yes":
        print("Quiting the game")
        time.sleep(3)
        quit()
    else:
        #Question 1
        print("Lets start the game")
        a1=input("Question 1:  What is the most played game in the world? ")
        if a1.lower()=="minecraft":
            score+=1
            print("Correct answer :), Score:", score)
        else:
            print("Wrong answer :(, Score:", score)
        print()

        #Question 2
        a2=input("Question 2:  What is the largest continent in the world? ")
        if a2.lower()=="asia":
            score+=1
            print("Correct answer :), Score:", score)
        else:
            print("Wrong answer :(, Score:", score)
        print()

        #Question 3
        a3=input("Question 3:  Who wrote the play 'Romeo and Juliet'? ")
        if a3.lower()=="william shakespeare":
            score+=1
            print("Correct answer :), Score:", score)
        else:
            print("Wrong answer :(, Score:", score)
        print()

        #Question 4
        a4=input("Question 4:  What is the name of the world's largest ocean? ")
        if a4.lower()=="pacific":
            score+=1
            print("Correct answer :), Score:", score)
        else:
            print("Wrong answer :(, Score:", score)
        print()

        #Question 5
        a5=input("Question 5:  What is the capital city of Brazil? ")
        if a5.lower()=="brasilia":
            score+=1
            print("Correct answer :), Score:", score)
        else:
            print("Wrong answer :(, Score:", score)
        print()        

        #Question 6
        a6=input("What is the national animal of India? ")
        if a6.lower()=="tiger":
            score+=1
            print("Correct answer :), Score:", score)
        else:
            print("Wrong answer :(, Score:", score)
        print()

        #Question 7
        a7=input("Who is the author of 'The Odyssey'? ")
        if a7.lower()=="homer":
            score+=1
            print("Correct answer :), Score:", score)
        else:
            print("Wrong answer :(, Score:", score)
        print()

        #Question 8
        a8=input("What is the name of the world's largest waterfall? ")
        if a8.lower()=="angel falls":
            score+=1
            print("Correct answer :), Score:", score)
        else:
            print("Wrong answer :(, Score:", score)
        print()

        #Question 9
        a9=input("What is the currency of Japan? ")
        if a9.lower()=="yen":
            score+=1
            print("Correct answer :), Score:", score)
        else:
            print("Wrong answer :(, Score:", score)
        print()

        #Question 10
        a10=input("Who is the current President of Russia? ")
        if a10.lower()=="vladimir putin":
            score+=1
            print("Correct answer :), Score:", score)
        else:
            print("Wrong answer :(, Score:", score)
        print()

        print("End of the quiz")
        print("Score out of 10:",score,"/ 10")
        print("Quiting game!")
        time.sleep(3)
        quit()
        
            
    
