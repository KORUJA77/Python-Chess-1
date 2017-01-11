import unittest
import sys
#Used for position on chess board. X can be 0-7 legally (a-h on board)
#Y can be 0-7 legally (1-8 on board)
class Position:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def to_string(self):
		return "({0}, {1})".format(self.x, self.y)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__


class Piece:

	#All pieces have a position, and whether or not they are white or not.
	#Pieces are defaulted to White, and position (0,0) == a1
	def __init__(self, pos=Position(), isWhite=True):
		self.pos = pos
		self.isWhite = isWhite

	def to_string(self):
		return "Position: {0}, White: {1}".format(self.pos.to_string(), self.isWhite)

#Class pawn is a piece, inherits from it so that it can use its pos and isWhite.
class Pawn(Piece):

	def __init__(self, pos=Position(), isWhite=True):
		super().__init__(pos, isWhite)

	#Gets all the possible moves of a pawn based on its current position
	def getAllMoves(self):
		moves = []
		y_factor = 1
		if not self.isWhite:
			y_factor = -1
		#Checking for whether pawn is on left side of board
		if(self.pos.x > 0):
			takeLeft = Position(self.pos.x - 1, self.pos.y + y_factor)
			moves.append(takeLeft)
		#Straight forwards
		forwards = Position(self.pos.x, self.pos.y + y_factor)
		moves.append(forwards)
		#Move forwards 2
		if((self.pos.y == 1 and self.isWhite) or (self.pos.y == 6 and (not self.isWhite))):
			forwards_two = Position(self.pos.x, self.pos.y + (y_factor * 2))
			moves.append(forwards_two)
		#Checking whether pawn is on right side of board
		if(self.pos.x < 7):
			takeRight = Position(self.pos.x + 1, self.pos.y + y_factor)
			moves.append(takeRight)
		return moves

#Class to represent a knight piece
class Knight(Piece):

	def __init__(self, pos=Position(), isWhite=True):
		super().__init__(pos, isWhite)


	'''
	Diagram of Knight's possible moves:
	7 - - - - - - - -
	6 - - - X - X - -
	5 - - X - - - X -
	4 - - - - N - - -
	3 - - X - - - X -
	2 - - - X - X - -
	1 - - - - - - - -
	0 - - - - - - - -
  	  0 1 2 3 4 5 6 7
  	'''
	def getAllMoves(self):
		moves = []
		'''
		How this works: Gets Knight moves for each column of diagram above, skips
		0 as there is nothing at 0. Uses the fact that the knight always moves 3 squares to its advantage.
		'''
		for i in range(-2, 3):
			if i == 0:
				continue
			moves.append(Position(self.pos.x + i, self.pos.y + 3 - abs(i)))
			moves.append(Position(self.pos.x + i, self.pos.y - 3 + abs(i)))
		#Gets rid of any moves that are out of bounds.
		filtered_moves = [pos for pos in moves if isPositionInBounds(pos)]
		return filtered_moves

#Class to represent a bishop piece
class Bishop(Piece):

	def __init__(self, pos=Position(), isWhite=True):
		super().__init__(pos, isWhite)


	'''
	Diagram of Bishop's possible moves:
	7 - X - - - - - X
	6 - - X - - - X -
	5 - - - X - X - -
	4 - - - - B - - -
	3 - - - X - X - -
	2 - - X - - - X -
	1 - X - - - - - X
	0 X - - - - - - -
  	  0 1 2 3 4 5 6 7
  	'''
	def getAllMoves(self):
		moves = []
		'''
		How this works: Loops through the four paterns -- Up right, up left, down right, and down left.
		'''

		curr_position = Position(self.pos.x + 1, self.pos.y + 1)
		while (isPositionInBounds(curr_position)):
			moves.append(curr_position)
			curr_position = Position(curr_position.x + 1, curr_position.y + 1)

		curr_position = Position(self.pos.x + 1, self.pos.y - 1)
		while (isPositionInBounds(curr_position)):
			moves.append(curr_position)
			curr_position = Position(curr_position.x + 1, curr_position.y - 1)

		curr_position = Position(self.pos.x - 1, self.pos.y + 1)
		while (isPositionInBounds(curr_position)):
			moves.append(curr_position)
			curr_position = Position(curr_position.x - 1, curr_position.y + 1)

		curr_position = Position(self.pos.x - 1, self.pos.y - 1)
		while (isPositionInBounds(curr_position)):
			moves.append(curr_position)
			curr_position = Position(curr_position.x - 1, curr_position.y - 1)
		return moves

#Class to represent a rook piece
class Rook(Piece):

	def __init__(self, pos=Position(), isWhite=True):
		super().__init__(pos, isWhite)


	'''
	Diagram of Rook's possible moves:
	7 - - - - X - - -
	6 - - - - X - - -
	5 - - - - X - - -
	4 X X X X R X X X
	3 - - - - X - - -
	2 - - - - X - - -
	1 - - - - X - - -
	0 - - - - X - - -
	  0 1 2 3 4 5 6 7
  	'''
	def getAllMoves(self):
		moves = []
		'''
		How this works: Loops through the four paterns -- Up right, up left, down right, and down left.
		'''

		curr_position = Position(self.pos.x + 1, self.pos.y)
		while (isPositionInBounds(curr_position)):
			moves.append(curr_position)
			curr_position = Position(curr_position.x + 1, curr_position.y)

		curr_position = Position(self.pos.x - 1, self.pos.y)
		while (isPositionInBounds(curr_position)):
			moves.append(curr_position)
			curr_position = Position(curr_position.x - 1, curr_position.y)

		curr_position = Position(self.pos.x, self.pos.y + 1)
		while (isPositionInBounds(curr_position)):
			moves.append(curr_position)
			curr_position = Position(curr_position.x, curr_position.y + 1)

		curr_position = Position(self.pos.x, self.pos.y - 1)
		while (isPositionInBounds(curr_position)):
			moves.append(curr_position)
			curr_position = Position(curr_position.x, curr_position.y - 1)
		return moves

#Class to represent a Queen piece
class Queen(Piece):

	def __init__(self, pos=Position(), isWhite=True):
		super().__init__(pos, isWhite)


	'''
	Diagram of Queen's possible moves:
	7 - X - - X - - X
	6 - - X - X - X -
	5 - - - X X X - -
	4 X X X X Q X X X
	3 - - - X X X - -
	2 - - X - X - X -
	1 - X - - X - - X
	0 X - - - X - - -
	  0 1 2 3 4 5 6 7
  	'''
	def getAllMoves(self):
		moves = []
		'''
		How this works: A queen can go any distance diagonal + vertical, so it is essentially a 
		rook and a bishop.
		'''
		dummy_bishop = Bishop(Position(self.pos.x, self.pos.y))
		dummy_rook = Rook(Position(self.pos.x, self.pos.y))
		return dummy_bishop.getAllMoves() + dummy_rook.getAllMoves()

#Class to represent a King piece
class King(Piece):

	'''
	hasMoved -- for castling -- It can only castle if it hasn't moved,
	and there is a rook on either corner that has not moved. Any time a move
	is made, hasMoved will be changed to true.
	'''
	def __init__(self, pos=Position(), isWhite=True, hasMoved=False):
		#You can set hasMoved for testing purposes, but typically a King should
		#be created with hasMoved being false.
		super().__init__(pos, isWhite)
		self.hasMoved = hasMoved

	'''
	Diagram of King's possible moves:
	7 - - - - - - - -
	6 - - - - - - - -
	5 - - - X X X - -
	4 - - - X K X - -
	3 - - - X X X - -
	2 - - - - - - - -
	1 - - - - - - - -
	0 - - - - - - - -
	  0 1 2 3 4 5 6 7

	Note: Caslte not depicted, but will be implemented.
  	'''
	def getAllMoves(self):
		moves = []
		for x in range(self.pos.x - 1, self.pos.x + 2):
			for y in range(self.pos.y - 1, self.pos.y + 2):
				curr_position = Position(x, y)
				if curr_position != self.pos and isPositionInBounds(curr_position):
					moves.append(curr_position)
		if not self.hasMoved:
			if self.isWhite:
				if self.pos.x == 4 and self.pos.y == 0:
					castle_kingside = Position(6, 0)
					moves.append(castle_kingside)
					castle_quenenside = Position(2, 0)
					moves.append(castle_quenenside)
			else:
				if self.pos.x == 4 and self.pos.y == 7:
					castle_kingside = Position(6, 7)
					moves.append(castle_kingside)
					castle_quenenside = Position(2, 7)
					moves.append(castle_quenenside)
		return moves






def isPositionInBounds(position):
	return position.x >= 0 and position.x <= 7 and position.y >= 0 and position.y <= 7

if __name__ == '__main__':
	king = King(Position(4, 4), True, True)
	for move in king.getAllMoves():
		print(move.to_string())



#class Board:

	#Board will contain a dictionary of Position -> Piece for both black and white. This will be useful in finding out whether or not a piece can move to a position.

