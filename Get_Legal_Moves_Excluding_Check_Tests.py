import unittest
from Python_Chess import *


class TestPawnGetLegalMovesExcludingCheck(unittest.TestCase):
    def test_empty_board_white(self):
        pawn = Pawn(Position(4, 4))
        white_pieces = {}
        black_pieces = {}
        moves = pawn.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(4, 5))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_empty_board_black(self):
        pawn = Pawn(Position(4, 4), False)
        white_pieces = {}
        black_pieces = {}
        moves = pawn.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(4, 3))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_take_left_white(self):
        pawn = Pawn(Position(4, 4))
        white_pieces = {}
        black_pieces = {Position(5, 5): Queen(Position(5, 5), False)}
        moves = pawn.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(4, 5))
        expected_moves.append(Position(5, 5))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_take_right_white(self):
        pawn = Pawn(Position(4, 4))
        white_pieces = {}
        black_pieces = {Position(3, 5): Queen(Position(3, 5), False)}
        moves = pawn.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(4, 5))
        expected_moves.append(Position(3, 5))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_en_passant_left_white(self):
        pawn = Pawn(Position(4, 4))
        white_pieces = {}
        black_pieces = {Position(5, 4): Pawn(Position(5, 4), False, True)}
        moves = pawn.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(4, 5))
        expected_moves.append(Position(5, 5))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_en_passant_right_white(self):
        pawn = Pawn(Position(4, 4))
        white_pieces = {}
        black_pieces = {Position(3, 4): Pawn(Position(3, 4), False, True)}
        moves = pawn.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(4, 5))
        expected_moves.append(Position(3, 5))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_take_both_white(self):
        pawn = Pawn(Position(4, 4))
        white_pieces = {}
        black_pieces = {Position(3, 5): Pawn(Position(3, 5), False),
                        Position(5, 5): Pawn(Position(5, 5), False)}
        moves = pawn.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(4, 5))
        expected_moves.append(Position(3, 5))
        expected_moves.append(Position(5, 5))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_move_two_white(self):
        pawn = Pawn(Position(3, 1))
        white_pieces = {}
        black_pieces = {Position(3, 5): Pawn(Position(3, 5), False),
                        Position(5, 5): Rook(Position(5, 5), False)}
        moves = pawn.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(3, 2))
        expected_moves.append(Position(3, 3))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    '''
    -------------------temp-------------------
    '''

    def test_take_left_black(self):
        pawn = Pawn(Position(4, 4), False)
        white_pieces = {Position(5, 3): Queen(Position(5, 3))}
        black_pieces = {}
        moves = pawn.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(4, 3))
        expected_moves.append(Position(5, 3))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_take_right_black(self):
        pawn = Pawn(Position(4, 4), False)
        white_pieces = {Position(3, 3): Queen(Position(3, 3))}
        black_pieces = {}
        moves = pawn.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(4, 3))
        expected_moves.append(Position(3, 3))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_en_passant_left_black(self):
        pawn = Pawn(Position(4, 3), False)
        white_pieces = {Position(5, 3): Pawn(Position(5, 3), True, True)}
        black_pieces = {}
        moves = pawn.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(4, 2))
        expected_moves.append(Position(5, 2))
        print(len(moves))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_en_passant_right_black(self):
        pawn = Pawn(Position(4, 3), False)
        white_pieces = {Position(3, 3): Pawn(Position(3, 3), True, True)}
        black_pieces = {}
        moves = pawn.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(4, 2))
        expected_moves.append(Position(3, 2))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_take_both_black(self):
        pawn = Pawn(Position(4, 4), False)
        white_pieces = {Position(3, 3): Pawn(Position(3, 3)),
                        Position(5, 3): Pawn(Position(5, 3))}
        black_pieces = {}
        moves = pawn.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(4, 3))
        expected_moves.append(Position(3, 3))
        expected_moves.append(Position(5, 3))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_move_two_black(self):
        pawn = Pawn(Position(3, 6), False)
        white_pieces = {Position(3, 2): Pawn(Position(3, 2)),
                        Position(5, 5): Rook(Position(5, 5))}
        black_pieces = {}
        moves = pawn.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(3, 4))
        expected_moves.append(Position(3, 5))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

class TestKnightGetLegalMovesExcludingCheck(unittest.TestCase):

    def test_0_0_empty_board(self):
        knight = Knight(Position(0, 0))
        white_pieces = {Position(0, 0): knight}
        black_pieces = {}
        moves = knight.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(1, 2))
        expected_moves.append(Position(2, 1))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_0_0_pieces_to_take(self):
        knight = Knight(Position(0, 0))
        white_pieces = {Position(0, 0): knight}
        black_pieces = {Position(1, 2): King(Position(1, 2), False),
                        Position(2, 1): Queen(Position(2, 1), False)}
        moves = knight.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(1, 2))
        expected_moves.append(Position(2, 1))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_0_0_pieces_in_the_way(self):
        knight = Knight(Position(0, 0))
        white_pieces = {Position(0, 0): knight,
                        Position(1, 2): King(Position(1,2)),
                        Position(2, 1): Queen(Position(2, 1))}
        black_pieces = {}
        moves = knight.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))