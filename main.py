import random
import numpy as np
bomb_counter = 0
win_counter = 0
unique_set = set()
d = {}

height = 8
width = 8
id = 1
#10 mines

class Person:  
      
    # init method or constructor   
    def __init__(self,id):
        self.id = id
        self.bomb = False
        self.clicked = False
        self.adj_bomb = 0

        
      
    # Sample Method   
      

#creates board
board = []
for x in range(height):
  board.append([])
  for y in range(width):
    p = Person(id) 
    board[x].append(p)
    id+=1


#places bombs randombly. Random function
while bomb_counter <10:
  x = random.randint(0, 7)
  y = random.randint(0, 7)
  if((x,y) not in unique_set):
    board[x][y].bomb = True
    unique_set.add((x,y))
    bomb_counter+=1



#basically it will be an onlick function 

def dfs(board,x,y):
  global win_counter
  adj_counter = 0
  board[x][y].clicked = True
  win_counter+=1
  arr = [[-1,0],[1,0],[0,-1],[0,1],[1,1],[-1,-1],[-1,1],[1,-1]] #checks adj 8 sqaures
  for z in arr:
     er,sr = x + z[0],y +z[1]
     if checker(board,er,sr) ==True and board[er][sr].bomb == True:
            adj_counter+=1
  board[x][y].adj_bomb = adj_counter
  
  if board[x][y].adj_bomb == 0: #makes sure there are no adj bombs
    for z in arr:
      er,sr = x +z[0],y +z[1]
      if checker(board,er,sr) ==True and board[er][sr].clicked ==False:         
          dfs(board,er,sr)


#makes sure recursion stays within bounds of board
def checker(board,x1,y1):
  p = len(board)-1
  q = len(board[0])-1
            
  if x1>p or y1>q:
      return False
  if x1<0 or y1<0:
      return False
  else:
      return True


#takes user input


def printboard(height,width):
  board2 = []
  for x in range(height):
    board2.append([])
    for y in range(width):
        if board[x][y].bomb == True:
          board2[x].append('B')
        elif board[x][y].adj_bomb>0:
          board2[x].append(board[x][y].adj_bomb)
        elif board[x][y].clicked==True:
          board2[x].append('-')
        else:
          board2[x].append(0)
  print(np.matrix(board2))
  
  
  
#print(board2)


val = input("Enter your guess i.e '00': ")
x_axis = int(val[0])
y_axis= int(val[1])
dfs(board,x_axis,y_axis)

printboard(8,8)
while board[x_axis][y_axis].bomb != True:
  if win_counter == 54:
    print('you win')
    break
  val = input("Enter your guess: ")
  x_axis = int(val[0])
  y_axis= int(val[1])
  dfs(board,x_axis,y_axis)
  printboard(8,8)
  
