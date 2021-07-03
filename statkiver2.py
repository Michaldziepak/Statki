import numpy as np
import random
#stworzenie tablic
board = []
boardcomp = []
shots = []
shotscomp=[]
matrix_of_fate= np.zeros([13,13])
matrix_of_my_ships = np.zeros([11,11])
coords = []
my_coords = []
trafienia = [np.zeros([11,11])]
trafienia_comp = [np.zeros([11,11])]


def add_to_fate(matrix_of_fate,coords):
    for a in coords:
        (x,y) = a
        if x != 0 and y != 0:
                    for wsp1 in range(x-1,x+2):
                        for wsp2 in range(y-1,y+2):
                            matrix_of_fate[wsp1][wsp2]=1
        elif x ==0:
                for wsp1 in range(x,x+2):
                    for wsp2 in range(y-1,y+2):
                        matrix_of_fate[wsp1][wsp2]=1
        elif y ==0:
                for wsp1 in range(x-1,x+2):
                    for wsp2 in range(y,y+2):
                        matrix_of_fate[wsp1][wsp2]=1
        elif x ==0 and y == 0:
                for wsp1 in range(x,x+2):
                    for wsp2 in range(y,y+2):
                        matrix_of_fate[wsp1][wsp2]=1


def one_mast():
     #row = x column=y

                     x = random.randint(0,9)
                     y = random.randint(0,9)
                     if matrix_of_fate[x][y] == 1:
                                one_mast()
                     else:                    
                              coords.append((x,y))
                              add_to_fate(matrix_of_fate,coords)




def two_mast():
     x = random.randint(0,9)
     y = random.randint(0,9)
     
     while matrix_of_fate[x][y]==1:
        x = random.randint(0,9)
        y = random.randint(0,9)       
     
     coords.append((x,y))
             
     loopend = 1   
     while loopend == 1:

        (xydirectionrandom,xydirectionplusminus) = (random.randint(0,1),random.choice([-1,1]))
        if xydirectionrandom == 0:
            additional_var = x + xydirectionplusminus
            
            if additional_var == 10:
                additional_var=8
            if additional_var == -1:
                additional_var= 1
            if additional_var <10 and additional_var >=0 and matrix_of_fate[additional_var][y] != 1:
                x = additional_var
                
                coords.append((x,y))
                loopend = 0

        elif xydirectionrandom ==1:
            additional_var2 = y + xydirectionplusminus
          
            if additional_var2 == 10:
                additional_var2 = 8
            if additional_var2 == -1:
                additional_var2 = 1
            if additional_var2 <10 and additional_var2 >=0 and matrix_of_fate[x][additional_var2] != 1:
                    y = additional_var2
                   
                    coords.append((x,y))
                    loopend = 0
               
     add_to_fate(matrix_of_fate,coords)
     
def three_mast():
    x = random.randint(0,9)
    y = random.randint(0,9)
     
    while matrix_of_fate[x][y] == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)

    coords.append((x,y))
    loopend = 1   
    while loopend == 1:
         b = random.randint(0,5)

         if b == 0 and matrix_of_fate[x+1][y] == 0 and matrix_of_fate[x+2][y] == 0 and x+2 < 10:
            coords.append((x+1,y))
            coords.append((x+2,y))
            loopend = 0

         elif b == 1 and matrix_of_fate[x-1][y] == 0 and matrix_of_fate[x-2][y] == 0 and x-2 >= 0:    
            coords.append((x-1,y))
            coords.append((x-2,y))
            loopend = 0

         elif b == 2 and matrix_of_fate[x-1][y] == 0 and matrix_of_fate[x+1][y] == 0 and x-1 >= 0 and x+1 <10:    
            coords.append((x-1,y))
            coords.append((x+1,y))
            loopend = 0

         elif b == 3 and matrix_of_fate[x][y+1] == 0 and matrix_of_fate[x][y-1] == 0 and y-1 >= 0 and y+1 <10:    
            coords.append((x,y-1))
            coords.append((x,y+1))
            loopend = 0
         elif b == 4 and matrix_of_fate[x][y+1] == 0 and matrix_of_fate[x][y+2] == 0 and y+2 < 10:    
            coords.append((x,y+1))
            coords.append((x,y+2))
            loopend = 0
         elif b == 5 and matrix_of_fate[x][y-1] == 0 and matrix_of_fate[x][y-2] == 0 and y-2 >=0:    
            coords.append((x,y-1))
            coords.append((x,y-2))
            loopend = 0        

    add_to_fate(matrix_of_fate,coords)

def four_mast():
    x = random.randint(0,9)
    y = random.randint(0,9)
     
    while matrix_of_fate[x][y] == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)

    coords.append((x,y))
    print(x,y)

    loopend = 1   
    while loopend == 1:

        b = random.randint(0,7)

        if b == 0: 
            
            if x+3 < 10 :
              coords.append((x+1,y))
              coords.append((x+2,y))
              coords.append((x+3,y))
              loopend = 0
            
        elif b == 1:
          
          if x+2 < 10 and x-1>= 0:
            coords.append((x+1,y))
            coords.append((x+2,y))
            coords.append((x-1,y))
            loopend = 0
            
        elif b == 2: 
            
            if x+1 < 10 and x-2>= 0:
                coords.append((x+1,y))
                coords.append((x-2,y))
                coords.append((x-1,y))
                loopend = 0
               
        elif b == 3:
            
            if x-3>= 0:
                coords.append((x-3,y))
                coords.append((x-2,y))
                coords.append((x-1,y))
                loopend = 0
                
        elif b == 4: 
            
            if y+3 < 10:
                coords.append((x,y+1))
                coords.append((x,y+2))
                coords.append((x,y+3))
                loopend = 0
                
        elif b == 5:
            
            if y+2 < 10 and y-1>= 0:
                coords.append((x,y+1))
                coords.append((x,y+2))
                coords.append((x,y-1))
                loopend = 0
                
        elif b == 6: 
            
            if y+1 < 10 and y-2>= 0:
                
                coords.append((x,y+1))
                coords.append((x,y-2))
                coords.append((x,y-1))
                loopend = 0
                
        elif b == 7 :
            
            if y-3 >= 0:
                coords.append((x,y-1))
                coords.append((x,y-2))
                coords.append((x,y-3))
                loopend = 0
                
        add_to_fate(matrix_of_fate,coords)


def ships_on_board(coords):
    #row = x, #column = y
     print("+-" + "--" * 9 + "+")      
     for row in range(10):
          rows = []

          for column in range(10):
                if (row,column) in coords:
                     ch = "O"
                else:
                     ch = " "
                rows.append(ch)
          print("|" + " ".join(rows) + "|")                      
     print("+-" + "--" * 9 + "+")



def make_onemasts():
    one_mast()
    one_mast()
    one_mast()
    one_mast()
def make_twomasts():
    two_mast()
    two_mast()
    two_mast()
def createcompships():
    four_mast()
    three_mast()
    three_mast()
    make_twomasts()
    make_onemasts()
    return coords
    


def my_ships():
    my_onemast = 0
    my_twomast = 0
    my_threemast = 0
    my_fourmast = 0

    while my_fourmast  != 1 :
         inp = (input("Gdzie chcesz postawić czteromasztowiec. Wprowadź numer kolumny i numer wiersza (x,y)\n")).replace("(","").replace(")","")
         try:    
             xstr , ystr = inp.split(",")
             x = int(xstr)-1
             y = int(ystr)-1
             if matrix_of_my_ships[x][y] != 1 :
                if x <= 9 and x >= 0 and y <= 9 and y >= 0:
                    my_coords.append((x,y))
                    ships_on_board(my_coords)
                    my_fourmast+=1
                    matrix_of_my_ships[x][y] = 1
                    placed = 0
                    while placed == 0:

                      inp = (input("Czy chcesz żeby Twój statek był skierowany na wschód (1), zachód (2), północ(3) czy południe(4) \n")).replace("(","").replace(")","")
                      try:
                          if int(inp) == 1 and y+2 < 10 and matrix_of_my_ships[x][y+1] == 0 and matrix_of_my_ships[x][y+2] == 0 and matrix_of_my_ships[x][y+3] == 0:
                            my_coords.append((x,y+1))
                            my_coords.append((x,y+2))
                            my_coords.append((x,y+3))
                            placed = True
                            ships_on_board(my_coords)
                          elif int(inp) == 2 and y-2 >= 0 and matrix_of_my_ships[x][y-1] == 0 and matrix_of_my_ships[x][y-2] == 0 and matrix_of_my_ships[x][y-3] == 0:
                            my_coords.append((x,y-1))
                            my_coords.append((x,y-2))
                            my_coords.append((x,y-3))
                            placed = True
                            ships_on_board(my_coords)  
                          elif int(inp) == 3 and x-2 >= 0 and matrix_of_my_ships[x-1][y] and matrix_of_my_ships[x-2][y] == 0 and matrix_of_my_ships[x-3][y] == 0:
                            my_coords.append((x-1,y))
                            my_coords.append((x-2,y))
                            my_coords.append((x-3,y))
                            placed = True
                            ships_on_board(my_coords)
                          elif int(inp) == 4 and x+3 < 10 and matrix_of_my_ships[x+1][y] == 0 and matrix_of_my_ships[x+2][y] == 0 and matrix_of_my_ships[x+3][y] == 0:
                            my_coords.append((x+1,y))
                            my_coords.append((x+2,y))
                            my_coords.append((x+3,y))
                            placed = True
                            ships_on_board(my_coords)
                          else:
                            print("Czy na pewno dobrze wpisałeś ?\n")

                      except ValueError as ve:
                        print("Czy wpisałeś prawidłowy tekst na wejściu ? \n")

                    add_to_fate(matrix_of_my_ships,my_coords)
                    print(matrix_of_my_ships)
         except ValueError as ve:
            print("Czy wpisałeś prawidłowy tekst na wejściu ?")

    while my_threemast != 2 :
         
         inp = (input("Gdzie chcesz postawić trójmasztowiec. Wprowadź numer kolumny i numer wiersza (x,y)\n")).replace("(","").replace(")","")
         try:
             xstr , ystr = inp.split(",")
             x = int(xstr)-1
             y = int(ystr)-1
             if matrix_of_my_ships[x][y] != 1 :
                if x <= 9 and x >= 0 and y <= 9 and y >= 0:
                    my_coords.append((x,y))
                    ships_on_board(my_coords)
                    my_threemast+=1
                    matrix_of_my_ships[x][y] = 1
                    placed = 0
                    while placed == 0:
                      inp = (input("Czy chcesz żeby Twój statek był skierowany na wschód (1), zachód (2), północ(3) czy południe(4) \n")).replace("(","").replace(")","")
                      try:
                          if int(inp) == 1 and y+2 < 10 and matrix_of_my_ships[x][y+1] == 0 and matrix_of_my_ships[x][y+2] == 0:
                            my_coords.append((x,y+1))
                            my_coords.append((x,y+2))
                            placed = True
                            ships_on_board(my_coords)
                          elif int(inp) == 2 and y-2 >= 0 and matrix_of_my_ships[x][y-1] == 0 and matrix_of_my_ships[x][y-2] == 0:
                            my_coords.append((x,y-1))
                            my_coords.append((x,y-2))
                            placed = True
                            ships_on_board(my_coords)  
                          elif int(inp) == 3 and x-2 >= 0 and matrix_of_my_ships[x-1][y] and matrix_of_my_ships[x-2][y] == 0:
                            my_coords.append((x-1,y))
                            my_coords.append((x-2,y))
                            placed = True
                            ships_on_board(my_coords)
                          elif int(inp) == 4 and x+2 < 10 and matrix_of_my_ships[x+1][y] == 0 and matrix_of_my_ships[x+2][y] == 0:
                            my_coords.append((x+1,y))
                            my_coords.append((x+2,y))
                            placed = True
                            ships_on_board(my_coords)
                          else:
                            print("Czy na pewno dobrze wpisałeś ?\n")  

                      except ValueError as ve:
                        print("Czy wpisałeś prawidłowy tekst na wejściu ?")

                    add_to_fate(matrix_of_my_ships,my_coords)
                    print(matrix_of_my_ships)
             else:
                print("Statki nie mogą być tak blisko siebie")
         except ValueError as ve:
            print("Czy wpisałeś prawidłowy tekst na wejściu ?")                

    while my_twomast != 3 :
         inp = (input("Gdzie chcesz postawić dwumasztowiec. Wprowadź numer kolumny i numer wiersza (x,y)\n")).replace("(","").replace(")","")
         try:    
             xstr , ystr = inp.split(",")
             x = int(xstr)-1
             y = int(ystr)-1
             if matrix_of_my_ships[x][y] != 1 :
                if x <= 9 and x >= 0 and y <= 9 and y >= 0:
                    my_coords.append((x,y))
                    ships_on_board(my_coords)
                    my_twomast+=1
                    matrix_of_my_ships[x][y] = 1
                    placed = 0
                    while placed == 0:
                      inp = (input("Czy chcesz żeby Twój statek był skierowany na wschód (1), zachód (2), północ(3) czy południe(4) )\n")).replace("(","").replace(")","")
                      try:
                          if int(inp) == 1 and y+1 < 10 and matrix_of_my_ships[x][y+1] == 0:
                            my_coords.append((x,y+1))
                            placed = True
                            ships_on_board(my_coords)
                          elif int(inp) == 2 and y-1 >= 0 and matrix_of_my_ships[x][y-1] == 0:
                            my_coords.append((x,y-1))
                            placed = True
                            ships_on_board(my_coords)  
                          elif int(inp) == 3 and x-1 >= 0 and matrix_of_my_ships[x-1][y] == 0:
                            my_coords.append((x-1,y))
                            placed = True
                            ships_on_board(my_coords)
                          elif int(inp) == 4 and x+1 < 10 and matrix_of_my_ships[x+1][y] == 0:
                            my_coords.append((x+1,y))
                            placed = True
                            ships_on_board(my_coords)
                          else:
                            print("Czy na pewno dobrze wpisałeś ?\n")  

                      except ValueError as ve:
                        print("Czy naprawdę wpisałeś poprawne wejście")
                    add_to_fate(matrix_of_my_ships,my_coords)
                    print(matrix_of_my_ships)
                        
                else:
                    print("Czy naprawdę wpisałeś poprawne współrzędne?")
             else:
                    print("Statki nie mogą być tak blisko siebie") 
         except ValueError as ve:
            print("Czy wpisałeś prawidłowy tekst na wejściu ?")   
                
    while my_onemast != 4 :  
         inp = (input("Gdzie chcesz postawić jednomasztowce. Wprowadź numer kolumny i numer wiersza (x,y)\n")).replace("(","").replace(")","")
         try:
             xstr , ystr = inp.split(",")
             x = int(xstr)-1
             y = int(ystr)-1
             if matrix_of_my_ships[x][y] != 1 :
                 if x <= 9 and x >= 0 and y <= 9 and y >= 0:
             
                    my_coords.append((x,y))
                    ships_on_board(my_coords)
                    print("jednomasztowiec gotowy")
                    my_onemast+=1
                    add_to_fate(matrix_of_my_ships,my_coords)
                    print(matrix_of_my_ships)

                 else:
                    print("Czy naprawdę wpisałeś poprawne współrzędne?")
             else:
                print("Statki nie mogą być tak blisko siebie")
         except ValueError as ve:
            print("Czy wpisałeś prawidłowy tekst na wejściu ?")

    
coords = createcompships()
ships_on_board(coords)


my_coords = [(1, 2), (1, 3), (1, 4), (1, 1), (6, 7), (7, 7), (8, 7), (2, 9), (3, 9), (4, 9), (7, 3), (6, 3), (8, 1), (9, 1), (4, 0), (4, 1), (9, 5), (4, 3), (3, 7), (0, 7)]
#tu jest zastąpienie gracza gotowymi statkami funkcja jest napisana ale jej wpisywanie jest czasochłonne :D

ships_on_board(my_coords)


class GameBoard(object):

    def __init__(self,battleships):
        self.board_width = 10
        self.board_height = 10
        self.shots = []
        self.battleships = battleships

    def take_shot(self, shot_location):
      hit_battleship = None
      is_hit = False
      for b in self.battleships:
        idx = b.body_index(shot_location)
        if idx is not None:
                is_hit = True
                b.hits[idx] = True
                hit_battleship = b
                break

      self.shots.append(Shot(shot_location, is_hit))
      return hit_battleship
    def is_game_over(self):
        return all([b.is_destroyed() for b in self.battleships])

        

class Shot(object):

    def __init__ (self,location,is_hit):

        self.location = location
        self.is_hit = is_hit


class Battleship(object):

    @staticmethod
    def build(coords):
        body = coords
        return Battleship(body)

    def __init__(self,body):
        self.body = body
        self.hits = [False] * len(body)

    def body_index(self, location):
        try:
            return self.body.index(location)
        except ValueError:
            return None
    def is_destroyed(self):
        return all(self.hits)
def render(game_board,player,show_ships= False):

  if player == 0:
    print("plansza komputera")
  elif player==1:
    print("plansza gracza") 
  board = []
  for _ in range(10):
        board.append([" " for _ in range(10)])
  print("+-" + "--" * 9 + "+")
  sunk = [b for b in game_board.battleships if b.is_destroyed()]
  
  for ele in range(len(sunk)):
    for coord in sunk[ele].body:
      (y,x) = coord
      for wsp1 in range(x-1,x+2):
        for wsp2 in range(y-1,y+2):
          try:
            if wsp1 != -1 and wsp2 != -1:
              game_board.take_shot((wsp2,wsp1))
          except Exception:
            pass 
  for sh in game_board.shots:
    x,y = sh.location
    if sh.is_hit:
      ch = "X"
      
    else:
      ch = "*"
    board[y][x] = ch
  for y in range(10):
        row = []
        for x in range(10):
            row.append(board[x][y] or " ")
        print("|" + " ".join(row) + "|")
  print("+-" + "--" * 9 + "+") 

      



  



if __name__ == "__main__":
    battleships = [
    Battleship.build(my_coords[0:4]),
    Battleship.build(my_coords[4:7]),
    Battleship.build(my_coords[7:10]),
    Battleship.build(my_coords[10:12]),
    Battleship.build(my_coords[12:14]),
    Battleship.build(my_coords[14:16]),
    Battleship.build(my_coords[16]),
    Battleship.build(my_coords[17]),
    Battleship.build(my_coords[18]),
    Battleship.build(my_coords[19])    
    ]
    battleships_comp = [
    Battleship.build(coords[0:4]),
    Battleship.build(coords[4:7]),
    Battleship.build(coords[7:10]),
    Battleship.build(coords[10:12]),
    Battleship.build(coords[12:14]),
    Battleship.build(coords[14:16]),
    Battleship.build(coords[16]),
    Battleship.build(coords[17]),
    Battleship.build(coords[18]),
    Battleship.build(coords[19])    
    ]
    my_game_board = GameBoard(battleships)
    comp_board = GameBoard(battleships_comp)


my_game_board.take_shot((1,2))
my_game_board.take_shot((1,3))
my_game_board.take_shot((1,4))
my_game_board.take_shot((4,0))
my_game_board.take_shot((4,1))
    

render(my_game_board,1)