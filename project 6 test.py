#all correct words
answers = ['hand','pen','hair','eye','case','fan','time','toy', 'paper','towel','light','shape','skirt','watch', 'system','laptop','pillow','trouser','beard','mirror']
#all jumbled words
questions = ['adhn','npe','irha','yee','sace','anf','mite','oty', 'rapep','lewot','tighl','pesha','triks','tchaw', 'metyss','paptol','wiollp','suerotr','dreba','rmiror']




#begins with showing rules

def begin():
    print('_____Jumble Jumble_______')
    print('\npress 0 to exit and any key to start')
    print("\n\n- Jumbled words will be given. Guess the correct word\n- Every correct answer will fetch +10 points\n- Every wrong answer will lose one life(from 3 life)")
    choice = input("\nPress any key to continue: ")




#function to play
def game():
    score = 0
    life=3
    i=0
    while(life!=0 and i<len(questions)):
        x=input('Question- '+questions[i]+' -> ')
        if(x==answers[i]):
          score = score+10
          print("Right ans.")
          print('\nNew score ',score)
        else:
          print('\nWrong answer')
          print('you lost one life')
          life = life-1
        i=i+1
          
    else:
        print('\n\nGAME OVER')
        print('Final Score= ',score)
        next = input('\n\nDo u want to continue and play again? press y for yes,or any key for no')
        
        if(next=='y' or next=='Y'):
            play()
        else:
            exit()


def play():
    begin()
    game()
play()    

    
