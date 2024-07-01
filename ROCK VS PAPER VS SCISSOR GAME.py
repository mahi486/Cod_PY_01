
# ROCK-PAPER-SCISSOR GAME:
# HOW TO PLAY:
#     ROCK VS PAPER - PAPER WINS
#     ROCK VS SCISSOR - ROCK WINS
#     SCISSOR VS PAPER  - SCISSOR WINS
    
    # ONLY THREE CASES POSSIBLE
    
# PYTHON CODE FOR ROCK -PAPER-SCISSOR GAME:




import random
r = ["Rock","Paper","Scissor"]

# condition = True
while True:
    usercount = 0
    comcount = 0
    userchoice = int(input('''
GAME START
1. YES
2. NO
        
          '''))
          
    if userchoice == 1:
        for i in range(1,11):
           userinput = int(input('''
1. Rock
2. Paper
3. Scissor                                   
             
           '''))
     
           if userinput == 1:
               userchoice = "Rock"
           elif userinput == 2:
               userchoice = "Paper"
           elif userinput == 3:
               userchoice = "Scissor"
           comchoice = random.choice(r) 
           if comchoice == userchoice:
               print("computer choose =",comchoice)
               print("user choose = ",userchoice)
               print("GAME IS DRAW")
               usercount = usercount+1
               comcount = comcount+1
           elif  (userchoice == "Rock" and comchoice == "scissor") or (userchoice =="Paper"
                 and comchoice=="Rock")  or (userchoice == "scissor" and comchoice == "Paper"):
               print("computer choose = ",comchoice)
               print("user choose = ",userchoice)
               print("user win" )
               usercount = usercount+1
           else:
               print("computer choose = ",comchoice)
               print("user choose = ",userchoice)
               print( "computer win")
               comcount = comcount+1
        if usercount == comcount:
         print("FINALLY GAME DRAW")
         print("total user score = " ,usercount)
         print("total computer score =", comcount)
        elif usercount>comcount:
         print("FINALLY USER WIN")
         print("total user score = " ,usercount)
         print("total computer score =", comcount) 
        else:
         print("FINALLY COMPUTER WIN")
         print("total user score = " ,usercount)
         print("total computer score =", comcount)
         
         
    else:
        break
    
    