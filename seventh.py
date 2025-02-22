from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        pass

    @property
    @abstractmethod
    def symbol(self):
        pass

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def set_position(self, new_postion):
        self.__position = new_postion

    def is_position_on_board(self, position):

        row, col = position
        return 0 < row <= 8 and 0 < col <= 8

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        
        if self.color == "white":
            moves.append((row + 1, col))
            if row == 2:
                moves.append((row + 2, col))
        else:
            moves.append((row - 1, col))
            if row == 7:
                moves.append((row - 2, col))
        
        return [move for move in moves if self.is_position_on_board(move)]

    @property
    def symbol(self):
        return 'pesec_c' if self.color == "black" else 'pesec_b'

    def __str__(self):
        return f'Pesec({self.symbol}) na pozici {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for i in range(1, 8):
            moves.extend([
                (row + i, col + i),
                (row + i, col - i),
                (row - i, col + i),
                (row - i, col - i)
            ])
        return [move for move in moves if self.is_position_on_board(move)]

    @property
    def symbol(self):
        return 'strelec_c' if self.color == "black" else 'strelec_b'

    def __str__(self):
        return f'Strelec({self.symbol}) na pozici {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for i in range(1, 9):
            if i != row:
                moves.append((i, col))
            if i != col:
                moves.append((row, i))
        return [move for move in moves if self.is_position_on_board(move)]

    @property
    def symbol(self):
        return 'vez_c' if self.color == "black" else 'vez_b'

    def __str__(self):
        return f'Vez({self.symbol}) na pozici {self.position}'


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for i in range(1, 8):
            moves.extend([
                (row + i, col + i),
                (row + i, col - i),
                (row - i, col + i),
                (row - i, col - i)
            ])
        for i in range(1, 9):
            if i != row:
                moves.append((i, col))
            if i != col:
                moves.append((row, i))
        return [move for move in moves if self.is_position_on_board(move)]

    @property
    def symbol(self):
        return 'dama_c' if self.color == "black" else 'dama_b'

    def __str__(self):
        return f'Dama({self.symbol}) na pozici {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 1, col), (row - 1, col),
            (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1),
            (row - 1, col + 1), (row - 1, col - 1)
        ]
        return [move for move in moves if self.is_position_on_board(move)]

    @property
    def symbol(self):
        return 'kral_c' if self.color == "black" else 'kral_b'

    def __str__(self):
        return f'Kral({self.symbol}) na pozici {self.position}'


class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        return [move for move in moves if self.is_position_on_board(move)]

    @property
    def symbol(self):
        return 'kun_c' if self.color == "black" else 'kun_b'

    def __str__(self):
        return f'Kun({self.symbol}) na pozici {self.position}'


if __name__ == "__main__":
    try:
        pieces = [
            Pawn("white", (2, 1)),
            Knight("black", (1, 2)),
            Bishop("white", (3, 3)),
            Rook("black", (4, 4)),
            Queen("white", (5, 5)),
            King("black", (6, 6))
        ]
        
        print("Test figur:")
        for piece in pieces:
            print(piece)
            print(f"Možné tahy: {piece.possible_moves()}")
            print(f"Je na šachovnici? {piece.is_position_on_board(piece.position)}\n")
            
    except Exception as e:
        print(f"Chyba: {e}")