import numpy as np

n=0

score_card={'Player':0,'Computer':0}

def score(winner='None'):

    if winner=='Player':
        score_card['Player']+=1
    elif winner=='None':
        pass   
    else:
        score_card['Computer']+=1

    print("Scores")
   
    print(player," : ",score_card['Player'])
    print("Computer : ",score_card['Computer'])
        


print(" Welcome To StonE PapeR ScissorS game ","\n"," Win with your LUCK")

player=input("Enter player name")


while n!=4:
    print()
    print(" 1.Stone","\n","2.Paper","\n","3.Scissors","\n","4.Quit")

    n=int(input("Enter your lucky spell"))


    val=''


    if n==1:
        val='Stone'
    elif n==2:
        val='Paper'
    elif n==3:
        val='Scissors'
    else:
        print("Enter valid Spell")
    

    computer=np.random.choice(['Stone','Papper','Scissors'])


    print()

    if val:

        print(" Your Spell: ",val," V/S ",computer," : Computer Spell ")

        if val=='Paper' and computer=='Stone':
            print("Congratulations ",player," you win!!!")
            score('Player')

        elif val=='Stone' and computer=='Scissors':
            print("Congratulations ",player," you win!!!")
            score('Player')

        elif val=='Scissors' and computer=='Paper':
            print("Congratulations ",player," you win!!!")
            score('Player')

        elif val==computer:
            print("OMG!!! It's a Tie!!!")
            print("Scores Clashed!!!")
            score()

        else:
            print("Computer Wins- Better Luck Next Time!!!")
            score('Computer')

else:
    print("Game Over!!!")
    score()
    exit()

