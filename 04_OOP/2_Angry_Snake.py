class Board:
    def __init__(self):
        self.cells = ["*","*","*","*","*","*","*","*",pig.name,"*","*",bird.name,"*","*","*","*","*","*","*"]
        """ print(self.cells.index(pig.name)) """

    def display(self):
        print(self.cells[1],self.cells[2],self.cells[3],self.cells[4],self.cells[5],self.cells[6])
        print(self.cells[7],self.cells[8],self.cells[9],self.cells[10],self.cells[11],self.cells[12])
        print(self.cells[13],self.cells[14],self.cells[15],self.cells[16],self.cells[17],self.cells[18])

    def move(self):

        move = input("a for højre, d for vesntre, w for up og s for ned")

        while(self.cells.index(bird.name) == 11):
            if(move == "a"):
                board.left()
                board.display() 
                board.move()
            if(move == "d"):
                board.right()
                board.display() 
                board.move()
            if(move == "w"):
                board.up() 
                board.display() 
                board.move()
            if(move == "s"):
                board.down() 
                board.display() 
                board.move()
            else:
                print("+++YOU WON!+++")

    def right(self):
        p1 = self.cells.index(pig.name)
        p2 = p1 + 1
        self.cells[p1],self.cells[p2] = self.cells[p2],self.cells[p1]
        return self.cells

    def left(self):
        p1 = self.cells.index(pig.name)
        p2 = p1 - 1
        self.cells[p1],self.cells[p2] = self.cells[p2],self.cells[p1]
        return self.cells

    def up(self):
        p1 = self.cells.index(pig.name)
        p2 = p1 - 6
        self.cells[p1],self.cells[p2] = self.cells[p2],self.cells[p1]
        return self.cells

    def down(self):
        p1 = self.cells.index(pig.name)
        p2 = p1 + 6
        self.cells[p1],self.cells[p2] = self.cells[p2],self.cells[p1]
        return self.cells

class Pig:
    def __init__(self,name):
        self.name = name

class Bird:
    def __init__(self,name):
        self.name = name


bird = Bird("B")
pig = Pig("G")
board = Board()
board.display()
board.move()
print()