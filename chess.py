from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        """
        Vrací možné tahy pěšce vpřed bez braní.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        direction = 1 if self.color == 'white' else -1
        new_pos = (row + direction, col)
        
        if self.is_position_on_board(new_pos):
            moves.append(new_pos)
            
        return moves
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy střelce po diagonálách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        
        # Všechny diagonální směry
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for row_dir, col_dir in directions:
            current_row, current_col = row, col
            while True:
                current_row += row_dir
                current_col += col_dir
                new_pos = (current_row, current_col)
                if not self.is_position_on_board(new_pos):
                    break
                moves.append(new_pos)
                
        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy věže po řádcích a sloupcích.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        
        # Horizontální a vertikální směry
        for i in range(1, 9):
            if i != row:
                moves.append((i, col))
            if i != col:
                moves.append((row, i))
                
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy dámy (kombinace věže a střelce).
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        # Kombinuje tahy věže a střelce
        rook_moves = Rook(self.color, self.position).possible_moves()
        bishop_moves = Bishop(self.color, self.position).possible_moves()
        return rook_moves + bishop_moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy krále o jedno pole všemi směry.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        
        # Všechny směry o jedno pole
        for row_diff in [-1, 0, 1]:
            for col_diff in [-1, 0, 1]:
                if row_diff == 0 and col_diff == 0:
                    continue
                new_pos = (row + row_diff, col + col_diff)
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                    
        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())