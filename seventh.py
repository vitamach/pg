class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        direction = 1 if self.color == "white" else -1
        moves = [(row + direction, col)]
        if (self.color == "white" and row == 2) or (self.color == "black" and row == 7):
            moves.append((row + 2 * direction, col))
        return [(r, c) for r, c in moves if 0 < r <= 8 and 0 < c <= 8]

    @property
    def symbol(self):
        return '♟' if self.color == "black" else '♙'

    def __str__(self):
        return f'Pawn({self.symbol}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for dx, dy in [(1,1), (1,-1), (-1,1), (-1,-1)]:
            for i in range(1, 8):
                r, c = row + dx * i, col + dy * i
                if 0 < r <= 8 and 0 < c <= 8:
                    moves.append((r, c))
        return moves

    @property
    def symbol(self):
        return '♝' if self.color == "black" else '♗'

    def __str__(self):
        return f'Bishop({self.symbol}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            for i in range(1, 8):
                r, c = row + dx * i, col + dy * i
                if 0 < r <= 8 and 0 < c <= 8:
                    moves.append((r, c))
        return moves

    @property
    def symbol(self):
        return '♜' if self.color == "black" else '♖'

    def __str__(self):
        return f'Rook({self.symbol}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        for dx, dy in directions:
            for i in range(1, 8):
                r, c = row + dx * i, col + dy * i
                if 0 < r <= 8 and 0 < c <= 8:
                    moves.append((r, c))
        return moves

    @property
    def symbol(self):
        return '♛' if self.color == "black" else '♕'

    def __str__(self):
        return f'Queen({self.symbol}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        moves = [(row + dx, col + dy) for dx, dy in directions]
        return [(r, c) for r, c in moves if 0 < r <= 8 and 0 < c <= 8]

    @property
    def symbol(self):
        return '♚' if self.color == "black" else '♔'

    def __str__(self):
        return f'King({self.symbol}) at position {self.position}'