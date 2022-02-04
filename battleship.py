'''
Battleship :
In battleship, there are basically two actions. 

At the start of the game you "place_ship", by which I mean you take one of the ship pieces and place it on the board

When you "fire" there are four things that can happen: 
1) "Miss" - meaning you missed all the ships.
2) "Hit" - meaning you hit a ship
3) "Sink" - this is a special case of hit, where you hit the last remaining part of a ship
4) "Win" - this is a special case of "sink", where you sink the final ship
'''
'''
Solution:

There are 2 major components in the game of battleship
the board and the ships. 
I am going to create two classes
1.Ship class
2.Board class

Ship Class:
every ship will have the following properties
1. size 
2. orientation - (vertical or horizontal)
3. coordinates - coordinates on the board that the ship occupies.
4. hit-locations - locations where this ship has been hit. 

the functions of the ship would be 
1. place the ship - assigns the location of the ship on the board
2. guess - tells if the guess made was a Miss/Hit/Sink

Board class:
the board has the following properties
1. A 8x8 array representing the board itself.
    -1 = if ship present
    0 = empty spot
    1 = guessed spot -empty
    2 = guessed spot -hit

2. List of all the ship objects

the functions of the board would be :
1. create ships - creates objects of ship class and adds them to the list of ships
2. place ships - asks the users to place the ships , the ships should not intersect
3. make guesses - calls the guess function of every ship if ship returns sink then it removes the ship from the list of ship.
                    if all the ships are over it declares victory!
4. print the current board.

'''
'''
edge cases:
1. ships intersect each other -to solve this I need to make the board a global variable.
2. the size of the ships should not be greater than the board. fixed sizes of the ships 
3. the placement of the ship should not go outside the board.
4. cordinates should be = size of the ship.
5. the user should not guess the same location twice
6.
'''
global board
board = [[0]*8 for i in range(8)]

class ship:
    def __init__(self,size):
        self.size = size
        # since the user cannot hit the same location twice we can just have hit locations to be a counter of the locations being hit
        self.hit_locations = 0
        print("ship created")
    def place_ship(self,orientation,start_row,start_col):
        
        self.orientation = orientation
        
        if orientation == "horizontal":
            if start_col+self.size< 8:
                for i in range(self.size):
                    if board[start_row][start_col+i] == -1:
                        return "ship cannot be placed due to intersection"
                    else:
                        board[start_row][start_col+i] = -1
                self.col_coordinates = [start_col+i for i in range(self.size)]
                self.row_coordinates = [start_row for i in range(self.size)]

                return "success"
            else:
                return "the ship is going out of the baord"
        elif orientation == "vertical":
            if start_row+self.size< 8:
                for i in range(self.size):
                    if board[start_row+i][start_col] == -1:
                        return "ship cannot be placed due to intersection"
                    else:
                        board[start_row+i][start_col] = -1
                self.row_coordinates = [start_row+i for i in range(self.size)]
                self.col_coordinates = [start_col for i in range(self.size)]
                return "success"
            else:
                return "the ship is going out of the baord"

        else:
            return "the orientation should be vertical or horizontal only"
        
        
    def make_guess(self, row, col):
        #if both the row and column are correct then its a hit, otherwise it will be a miss. If its a hit then we need to check if  it is a sink or not.
        if row in self.row_coordinates:
            if col in self.col_coordinates:
                self.hit_locations +=1
                if self.hit_locations == self.size:
                    return "Sink"
                return "Hit"
        return "Miss"

class boards:
    def __init__(self):
        
        self.number_of_ships = int(input("number of ships: "))
        
        # for now I am just creating 2 ships with size 3 and 4 one vertical and other horizontal respectively
        self.ships = []
        for i in range(self.number_of_ships):
            size = int(input("enter size of ship "+str(i)+": "))
            current_ship = ship(size)
            resp = ""
            while resp != "success":
                print(resp)
                orientation = input("enter orientation of ship "+str(i)+": ")
                row = int(input("enter starting row of ship "+str(i)+": "))
                col = int(input("enter starting col of ship "+str(i)+": "))
                if row <8 and col <8 and row>=0 and col >= 0:
                    resp = current_ship.place_ship(orientation,row,col)
                else:
                    resp = "enter a coordinate within the board"
            self.ships.append(current_ship)

    def display_board(self):
        print(str(len(self.ships))+" ships remaining")
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    print(" O ",end="")
                elif board[i][j] == -1:
                    print(" O ",end="")
                elif board[i][j] == 1:
                    print(" - ",end="")
                elif board[i][j] == 2:
                    print(" X ",end="")
            print()
    
    def make_guess(self):
        row = int(input("enter row"))
        col = int(input("enter col"))
        flag = 0 # the value is initially 0 and is made 1 if there is a hit. the value stays 0 if it was miss on all ships otherwise it is 1.
        # covers the case missing the first ship but hitting the next
        # hitting the first and missing the rest
        if row<8 and col <8 and row >= 0 and col>=0:
            #if the user has already guessed this spot then ask him to re-enter the guess
            if board[row][col] >0:
                print("the spot has been guessed please enter another spot")
            else:
                for s in self.ships:
                    resp = s.make_guess(row,col)
                    if resp == "Miss":
                        continue
                    elif resp == "Hit":
                        flag = 1
                        print(resp)
                        
                    elif resp == "Sink":
                        flag = 1 
                        print(resp)
                        self.ships.remove(s)
                if flag ==0:
                    print("Miss")
                    board[row][col] = 1
                else:
                    board[row][col] = 2
        else:
            print("please enter a value within the grid")
            
                        
                    





a = boards()
a.display_board()
for i in range(20):
    if len(a.ships) > 0:
        a.make_guess()
        a.display_board()
        print("\n\n\n\n")
    else:
        print("Victory !!")
        break


