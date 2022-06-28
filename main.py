# Author: Colin
# Python text-based Tic-Tac-Toe game

import random

def playerLetterChoice():
  player_letter = input("Do you want to be X or O?: ")
  if player_letter == 'X':
    return ['X', 'O']
  else:
    return ['O', 'X']

def whoGoesFirst():
  result = random.randint(0, 1)
  if result == 0:
    return 'player'
  elif result == 1:
    return 'computer'


def drawBoard(board):
  print(board[7] + '|' + board[8] + '|' + board[9])
  print('-+-+-')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print('-+-+-')
  print(board[1] + '|' + board[2] + '|' + board[3])

def playerMove(board):
  pMove = 0
  while pMove not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(pMove)):
    pMove = input("What is your next move? (1-9)\n")
  return int(pMove)

def isSpaceFree(board, move):
  return board[move] == ' '

def makeMove(board, letter, move):
  board[move] = letter


def boardCopy(board):
  board2 = []
  for x in board:
    board2.append(x)
  return board2


def isWinner(board, letter):
  return((board[7] == letter and board[8] == letter and board[9] == letter) or 
  (board[4] == letter and board[5] == letter and board[6] == letter) or 
  (board[1] == letter and board[2] == letter and board[3] == letter) or
  (board[7] == letter and board[4] == letter and board[1] == letter) or
  (board[8] == letter and board[5] == letter and board[2] == letter) or 
  (board[9] == letter and board[6] == letter and board[3] == letter) or
  (board[7] == letter and board[5] == letter and board[3] == letter) or
  (board[9] == letter and board[5] == letter and board[1] == letter))


def tie(board):
  for x in range(1, 10):
    if board[x] == ' ':
      return False
  return True
    
      
def computerMove(board, computerLetter):
  if computerLetter == 'X':
    playerLetter = 'O'
  else:
    playerLetter = 'X'
  
  
  for x in range(1, 10):
    sampleBoard = boardCopy(board)
    if sampleBoard[x] == ' ':
      makeMove(sampleBoard, computerLetter, x)
      if isWinner(sampleBoard, computerLetter):
        return x

  for x in range(1, 10):
    sampleBoard = boardCopy(board)
    if sampleBoard[x] == ' ':
      makeMove(sampleBoard, playerLetter, x)
      if isWinner(sampleBoard, playerLetter):
        return x

  for x in range(1, 10):
    win = 0
    sampleBoard = boardCopy(board)
    if sampleBoard[x] == ' ':
      makeMove(sampleBoard, computerLetter, x)
      for y in range(1, 10):
        sampleBoard = boardCopy(sampleBoard)
        if sampleBoard[y] == ' ':
          makeMove(sampleBoard,computerLetter, y)
          if isWinner(sampleBoard, playerLetter):
            win += 1
    if win > 1:
      return x

  for x in range(1, 10):
    win = 0
    sampleBoard = boardCopy(board)
    if sampleBoard[x] == ' ':
      makeMove(sampleBoard, playerLetter, x)
      for y in range(1, 10):
        sampleBoard = boardCopy(sampleBoard)
        if sampleBoard[y] == ' ':
          makeMove(sampleBoard, playerLetter, y)
          if isWinner(sampleBoard, playerLetter):
            win += 1
    if win > 1:
      return x

  if board[5] == ' ':
    return 5
  moveList = []
  if board[1] == computerLetter and board[9] == ' ':
    moveList.append(9)
  if board[3] == computerLetter and board[7] == ' ':
    moveList.append(7)
  if board[7] == computerLetter and board[3] == ' ':
    moveList.append(3)
  if board[9] == computerLetter and board[1] == ' ':
    moveList.append(1)
  x = chooseRandomMoveFromList(board, moveList)
  if x != None:
    return x
  moveList2 = [1, 3, 7, 9]
  x = chooseRandomMoveFromList(board, moveList2)
  if x != None:
    return x
  moveList3 = [2, 4, 6, 8]
  x = chooseRandomMoveFromList(board, moveList3)
  return x 

  


def chooseRandomMoveFromList(board, moveList):
  possibleMoves = []
  for x in moveList:
    if board[x] == ' ':
      possibleMoves.append(x)
  if len(possibleMoves) == 0:
    return None
  x = random.choice(possibleMoves)
  return x  

def playAgain():
  playerChoice = input("Do you want to play again? (yes or no)\n")
  if playerChoice == 'yes':
    return True
  else:
    return False

    
while True:
  print('Welcome to Tic Tac Toe! ')
  board = [' '] * 10
  playerLetter, computerLetter = playerLetterChoice()
  turn = whoGoesFirst()
  if turn == 'computer':
    print('The computer will go first.')
  else:
    print('The player will go first.')
  print('''Here is a board with its numerical values for reference: 
---------------------------------
7|8|9
-+-+-
4|5|6
-+-+-
1|2|3
---------------------------------
''')


  game = True
  
  while game:
    if turn == 'computer':
      cMove = computerMove(board, computerLetter)
      makeMove(board, computerLetter, cMove)

      if isWinner(board, computerLetter):
        drawBoard(board)
        print('The computer has beaten you! You lose.')
        game = False
      elif tie(board):
        drawBoard(board)
        print("It's a tie!")
        game = False
      else:
        turn = 'player'

    elif turn == 'player':
      drawBoard(board)
      pMove = playerMove(board)
      makeMove(board, playerLetter, pMove)

      if isWinner(board, playerLetter):
        drawBoard(board)
        print('You win!')
        game = False
      elif tie(board):
        drawBoard(board)
        print("It's a tie!")
        game = False
      else:
        turn = 'computer'

  if not playAgain():
    break


