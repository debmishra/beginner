
#Player1 = input('First Player:')
#Player2 = input('Second Player:')

#PlayerX = Player1
#PlayerO = Player2

PlayBoard = ['-', '-', '-', '-', '-', '-', ' -', '-', '-']
AvailablePositions = [1,2,3,4,5,6,7,8,9]
PlayCount = 0
GameOver = 0
pe = 1

def ClearBoard() :
    global PlayBoard
    global PPE
    global AvailablePositions
    PlayBoard = ['-', '-', '-', '-', '-', '-', ' -', '-', '-']
    AvailablePositions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ClearBoard()

def PrintBoard() :
    print(PlayBoard[0:3])
    print(PlayBoard[3:6])
    print(PlayBoard[6:9])

def AcceptPositionX() :
    global pe
    global AvailablePositions
    while True:
        try:
            pe = input('enter position for X : ')
            if int(pe) >=1 and int(pe) <=9 :
                AvailablePositions.remove(int(pe))
                PlayBoard[int(pe) - 1] = 'X'
                break
            else:
                raise
        except:
            print("Please enter a number between 1-9. Open slots only")
            continue

def AcceptPositionO() :
    global pe
    global AvailablePositions
    while True:
        try:
            pe = input('enter position for O : ')
            if int(pe) >=1 and int(pe) <=9 :
                AvailablePositions.remove(int(pe))
                PlayBoard[int(pe) - 1] = 'O'
                break
            else:
                raise
        except:
            print("Please enter a number between 1-9. Open slots only")
            continue

def checkwinner() :
    global GameOver
    if ((PlayBoard[0] == 'X' and PlayBoard[1] == 'X' and PlayBoard[2] == 'X') or
        (PlayBoard[3] == 'X' and PlayBoard[4] == 'X' and PlayBoard[5] == 'X') or
        (PlayBoard[6] == 'X' and PlayBoard[7] == 'X' and PlayBoard[8] == 'X') or
        (PlayBoard[0] == 'X' and PlayBoard[3] == 'X' and PlayBoard[6] == 'X') or
        (PlayBoard[1] == 'X' and PlayBoard[4] == 'X' and PlayBoard[7] == 'X') or
        (PlayBoard[2] == 'X' and PlayBoard[5] == 'X' and PlayBoard[8] == 'X') or
        (PlayBoard[0] == 'X' and PlayBoard[4] == 'X' and PlayBoard[8] == 'X') or
        (PlayBoard[2] == 'X' and PlayBoard[4] == 'X' and PlayBoard[6] == 'X') or
        (PlayBoard[0] == 'O' and PlayBoard[1] == 'O' and PlayBoard[2] == 'O') or
        (PlayBoard[3] == 'O' and PlayBoard[4] == 'O' and PlayBoard[5] == 'O') or
        (PlayBoard[6] == 'O' and PlayBoard[7] == 'O' and PlayBoard[8] == 'O') or
        (PlayBoard[0] == 'O' and PlayBoard[3] == 'O' and PlayBoard[6] == 'O') or
        (PlayBoard[1] == 'O' and PlayBoard[4] == 'O' and PlayBoard[7] == 'O') or
        (PlayBoard[2] == 'O' and PlayBoard[5] == 'O' and PlayBoard[8] == 'O') or
        (PlayBoard[0] == 'O' and PlayBoard[4] == 'O' and PlayBoard[8] == 'O') or
        (PlayBoard[2] == 'O' and PlayBoard[4] == 'O' and PlayBoard[6] == 'O')) :
        GameOver = 1

PrintBoard()

while True :
    for entries in range(0,9) :
        PlayCount = PlayCount + 1
        if (PlayCount % 2) != 0 :
            AcceptPositionX()
        else :
            AcceptPositionO()

        PrintBoard()
        checkwinner()
        if GameOver == 1 :
            print('WOO HOO - GAME OVER')
            print()
            break
        if PlayCount == 9 :
            print('huh.. Its a Draw')
            print()
    OneMoreGame = input('One more y/n: ')
    if OneMoreGame == 'Y' or OneMoreGame == 'y':
        ClearBoard()
        PlayCount = 0
        GameOver = 0
        PrintBoard()
    else :
        print('See you next time!')
        break
