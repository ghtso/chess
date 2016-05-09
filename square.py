class Square:
    def __init__(self, offset, col, row, field, color):
        self.offset = offset
        self.col = col
        self.row = row
        self.name = field    # 'a1', 'a2' ... 'h8'
        self.color = color
        self.piece = None
        self.canvas_center = None   # tuple: (canvasx, canvasy)



    def add(self, piece):
        if self.piece:
            return False
        else:
            self.piece = piece
            return True

    def give(self):
        if self.piece:
            _piece = self.piece
            self.piece = None
            return _piece
        return False

    def is_empty(self):
        if self.piece:
            return False
        else:
            return True

    def show(self):
        print(self.offset, self.col, self.row, self.name, self.col, self.piece)


# ----------------------------------------- main ------------------------------------------

def test():
    class PieceTest:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name


    piece = PieceTest('piece-1')
    piece2 = PieceTest('piece-2')
    s = Square(10, 1, 1, 'b2', 'White')

    s.show()
    #
    add = s.add(piece)
    print('add return:', add)
    s.show()
    #
    give = s.give()
    print('give return:', give)
    s.show()
    #
    print ('2 x add: ===========')
    add = s.add(piece2)
    print('add return:', add)
    add = s.add(piece)
    print('add return:', add)
    s.show()
    #
    print('2 x give: ===========')
    give = s.give()
    print('give return:', give)
    give = s.give()
    print('give return:', give)
    s.show()

def main():
    test()
    pass

if __name__ == "__main__":
    main()