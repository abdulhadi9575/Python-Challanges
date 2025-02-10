theboard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
board_key=[]

for key in theboard:
    board_key.append(key)

def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printboard(theboard)
        print("It's your turn," + turn + ".Move to which place ?")

        move = input()

        if theboard[move] == ' ':
            theboard[move] = turn
            count += 1
        else:
            print("That place is already filled. \nMove to which place")
            continue

        if count >= 5:
            if theboard['7'] == theboard['8'] == theboard['9'] !=' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " + turn + "won. ****")
                break
            elif theboard['4'] == theboard['5'] == theboard['6'] !=' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " + turn + "won. ****")
                break
            elif theboard['1'] == theboard['2'] == theboard['3'] !=' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " + turn + "won. ****")
                break
            elif theboard['1'] == theboard['4'] == theboard['7'] != ' ': 
                printboard(theboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theboard['2'] == theboard['5'] == theboard['8'] != ' ': 
                printboard(theboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theboard['3'] == theboard['6'] == theboard['9'] != ' ': 
                printboard(theboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theboard['7'] == theboard['5'] == theboard['3'] != ' ': # diagonal
                printboard(theboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theboard['1'] == theboard['5'] == theboard['9'] != ' ': # diagonal
                printboard(theboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_key:
            theboard[key] = " "

        game()

if __name__ == "__main__":
    game()