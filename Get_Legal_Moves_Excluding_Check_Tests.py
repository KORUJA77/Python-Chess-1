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


class TestBishopGetLegalMovesExcludingCheck(unittest.TestCase):
    def test_4_4_empty_board(self):
        bishop = Bishop(Position(4, 4))
        white_pieces = {Position(4, 4): bishop}
        black_pieces = {}
        moves = bishop.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(5, 5))
        expected_moves.append(Position(6, 6))
        expected_moves.append(Position(7, 7))
        expected_moves.append(Position(5, 3))
        expected_moves.append(Position(6, 2))
        expected_moves.append(Position(7, 1))
        expected_moves.append(Position(3, 5))
        expected_moves.append(Position(2, 6))
        expected_moves.append(Position(1, 7))
        expected_moves.append(Position(3, 3))
        expected_moves.append(Position(2, 2))
        expected_moves.append(Position(1, 1))
        expected_moves.append(Position(0, 0))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_4_4_block_bottom_left(self):
        bishop = Bishop(Position(4, 4))
        white_pieces = {Position(4, 4): bishop,
                        Position(0, 0): Pawn(Position(0, 0))}
        black_pieces = {}
        moves = bishop.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(5, 5))
        expected_moves.append(Position(6, 6))
        expected_moves.append(Position(7, 7))
        expected_moves.append(Position(5, 3))
        expected_moves.append(Position(6, 2))
        expected_moves.append(Position(7, 1))
        expected_moves.append(Position(3, 5))
        expected_moves.append(Position(2, 6))
        expected_moves.append(Position(1, 7))
        expected_moves.append(Position(3, 3))
        expected_moves.append(Position(2, 2))
        expected_moves.append(Position(1, 1))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_4_4_take_bottom_left(self):
        bishop = Bishop(Position(4, 4))
        white_pieces = {Position(4, 4): bishop}
        black_pieces = {Position(0, 0): Pawn(Position(0, 0), False)}
        moves = bishop.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(5, 5))
        expected_moves.append(Position(6, 6))
        expected_moves.append(Position(7, 7))
        expected_moves.append(Position(5, 3))
        expected_moves.append(Position(6, 2))
        expected_moves.append(Position(7, 1))
        expected_moves.append(Position(3, 5))
        expected_moves.append(Position(2, 6))
        expected_moves.append(Position(1, 7))
        expected_moves.append(Position(3, 3))
        expected_moves.append(Position(2, 2))
        expected_moves.append(Position(1, 1))
        expected_moves.append(Position(0, 0))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_4_4_block_all(self):
        bishop = Bishop(Position(4, 4))
        white_pieces = {Position(4, 4): bishop,
                        Position(3, 3): Pawn(Position(3, 3)),
                        Position(5, 5): Pawn(Position(5, 5)),
                        Position(3, 5): Pawn(Position(3, 5)),
                        Position(5, 3): Pawn(Position(5, 3))}
        black_pieces = {}
        moves = bishop.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_4_4_take_all(self):
        bishop = Bishop(Position(4, 4))
        white_pieces = {Position(4, 4): bishop}
        black_pieces = {Position(3, 3): Pawn(Position(3, 3), False),
                        Position(5, 5): Pawn(Position(5, 5), False),
                        Position(3, 5): Pawn(Position(3, 5), False),
                        Position(5, 3): Pawn(Position(5, 3), False)}
        moves = bishop.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(3, 3))
        expected_moves.append(Position(5, 5))
        expected_moves.append(Position(3, 5))
        expected_moves.append(Position(5, 3))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    '''
    BLACK TESTS
    '''

    def test_4_4_empty_board_black(self):
        bishop = Bishop(Position(4, 4), False)
        white_pieces = {}
        black_pieces = {Position(4, 4): bishop}
        moves = bishop.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(5, 5))
        expected_moves.append(Position(6, 6))
        expected_moves.append(Position(7, 7))
        expected_moves.append(Position(5, 3))
        expected_moves.append(Position(6, 2))
        expected_moves.append(Position(7, 1))
        expected_moves.append(Position(3, 5))
        expected_moves.append(Position(2, 6))
        expected_moves.append(Position(1, 7))
        expected_moves.append(Position(3, 3))
        expected_moves.append(Position(2, 2))
        expected_moves.append(Position(1, 1))
        expected_moves.append(Position(0, 0))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_4_4_block_bottom_left_black(self):
        bishop = Bishop(Position(4, 4), False)
        black_pieces = {Position(4, 4): bishop,
                        Position(0, 0): Pawn(Position(0, 0), False)}
        white_pieces = {}
        moves = bishop.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(5, 5))
        expected_moves.append(Position(6, 6))
        expected_moves.append(Position(7, 7))
        expected_moves.append(Position(5, 3))
        expected_moves.append(Position(6, 2))
        expected_moves.append(Position(7, 1))
        expected_moves.append(Position(3, 5))
        expected_moves.append(Position(2, 6))
        expected_moves.append(Position(1, 7))
        expected_moves.append(Position(3, 3))
        expected_moves.append(Position(2, 2))
        expected_moves.append(Position(1, 1))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_4_4_take_bottom_left_black(self):
        bishop = Bishop(Position(4, 4), False)
        black_pieces = {Position(4, 4): bishop}
        white_pieces = {Position(0, 0): Pawn(Position(0, 0))}
        moves = bishop.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(5, 5))
        expected_moves.append(Position(6, 6))
        expected_moves.append(Position(7, 7))
        expected_moves.append(Position(5, 3))
        expected_moves.append(Position(6, 2))
        expected_moves.append(Position(7, 1))
        expected_moves.append(Position(3, 5))
        expected_moves.append(Position(2, 6))
        expected_moves.append(Position(1, 7))
        expected_moves.append(Position(3, 3))
        expected_moves.append(Position(2, 2))
        expected_moves.append(Position(1, 1))
        expected_moves.append(Position(0, 0))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_4_4_block_all_black(self):
        bishop = Bishop(Position(4, 4))
        white_pieces = {Position(4, 4): bishop,
                        Position(3, 3): Pawn(Position(3, 3)),
                        Position(5, 5): Pawn(Position(5, 5)),
                        Position(3, 5): Pawn(Position(3, 5)),
                        Position(5, 3): Pawn(Position(5, 3))}
        black_pieces = {}
        moves = bishop.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_4_4_take_all_black(self):
        bishop = Bishop(Position(4, 4))
        white_pieces = {Position(4, 4): bishop}
        black_pieces = {Position(3, 3): Pawn(Position(3, 3), False),
                        Position(5, 5): Pawn(Position(5, 5), False),
                        Position(3, 5): Pawn(Position(3, 5), False),
                        Position(5, 3): Pawn(Position(5, 3), False)}
        moves = bishop.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(3, 3))
        expected_moves.append(Position(5, 5))
        expected_moves.append(Position(3, 5))
        expected_moves.append(Position(5, 3))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))


class TestKnightGetLegalMovesExcludingCheck(unittest.TestCase):
    def test_0_0_empty_board(self):
        knight = Knight(Position(0, 0))
        white_pieces = {Position(0, 0), knight}
        black_pieces = {}
        moves = knight.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(1, 2))
        expected_moves.append(Position(2, 1))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_0_0_take_both(self):
        knight = Knight(Position(0, 0))
        white_pieces = {Position(0, 0), knight}
        black_pieces = {Position(1, 2), Pawn(Position(1, 2), False),
                        Position(2, 1), Pawn(Position(2, 1), False)}
        moves = knight.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(1, 2))
        expected_moves.append(Position(2, 1))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_0_0_block_both(self):
        knight = Knight(Position(0, 0))
        white_pieces = {Position(0, 0), knight,
                        Position(1, 2), Pawn(Position(1, 2)),
                        Position(2, 1), Pawn(Position(2, 1))}
        black_pieces = {}
        moves = knight.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_0_0_take_both_black(self):
        knight = Knight(Position(0, 0), False)
        black_pieces = {Position(0, 0), knight}
        white_pieces = {Position(1, 2), Pawn(Position(1, 2)),
                        Position(2, 1), Pawn(Position(2, 1))}
        moves = knight.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        expected_moves.append(Position(1, 2))
        expected_moves.append(Position(2, 1))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_0_0_block_both_black(self):
        knight = Knight(Position(0, 0), False)
        black_pieces = {Position(0, 0), knight,
                        Position(1, 2), Pawn(Position(1, 2), False),
                        Position(2, 1), Pawn(Position(2, 1), False)}
        white_pieces = {}
        moves = knight.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        expected_moves = []
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))


class TestRookGetLegalMovesExcludingCheck(unittest.TestCase):
    def test_4_4_empty_board(self):
        rook = Rook(Position(4, 4))
        white_pieces = {Position(4, 4): rook}
        black_pieces = {}
        expected_moves = rook.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        moves = []
        moves.append(Position(4, 5))
        moves.append(Position(4, 6))
        moves.append(Position(4, 7))
        moves.append(Position(4, 3))
        moves.append(Position(4, 2))
        moves.append(Position(4, 1))
        moves.append(Position(4, 0))
        moves.append(Position(5, 4))
        moves.append(Position(6, 4))
        moves.append(Position(7, 4))
        moves.append(Position(3, 4))
        moves.append(Position(2, 4))
        moves.append(Position(1, 4))
        moves.append(Position(0, 4))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_4_4_block_all(self):
        rook = Rook(Position(4, 4))
        white_pieces = {Position(4, 4): rook,
                        Position(4, 5): Bishop(Position(4, 5)),
                        Position(5, 4): Bishop(Position(5, 4)),
                        Position(3, 4): Bishop(Position(3, 4)),
                        Position(4, 3): Bishop(Position(4, 3))}
        black_pieces = {}
        expected_moves = rook.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        moves = []
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_4_4_take_all(self):
        rook = Rook(Position(4, 4))
        white_pieces = {Position(4, 4): rook}
        black_pieces = {Position(4, 5): Bishop(Position(4, 5), False),
                        Position(5, 4): Bishop(Position(5, 4), False),
                        Position(3, 4): Bishop(Position(3, 4), False),
                        Position(4, 3): Bishop(Position(4, 3), False)}
        expected_moves = rook.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        moves = [Position(4, 5), Position(5, 4), Position(3, 4), Position(4, 3)]
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    '''
    BLACK TESTS
    '''

    def test_4_4_empty_board_black(self):
        rook = Rook(Position(4, 4), False)
        black_pieces = {Position(4, 4): rook}
        white_pieces = {}
        expected_moves = rook.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        moves = []
        moves.append(Position(4, 5))
        moves.append(Position(4, 6))
        moves.append(Position(4, 7))
        moves.append(Position(4, 3))
        moves.append(Position(4, 2))
        moves.append(Position(4, 1))
        moves.append(Position(4, 0))
        moves.append(Position(5, 4))
        moves.append(Position(6, 4))
        moves.append(Position(7, 4))
        moves.append(Position(3, 4))
        moves.append(Position(2, 4))
        moves.append(Position(1, 4))
        moves.append(Position(0, 4))
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_4_4_block_all_black(self):
        rook = Rook(Position(4, 4), False)
        black_pieces = {Position(4, 4): rook,
                        Position(4, 5): Bishop(Position(4, 5), False),
                        Position(5, 4): Bishop(Position(5, 4), False),
                        Position(3, 4): Bishop(Position(3, 4), False),
                        Position(4, 3): Bishop(Position(4, 3), False)}
        white_pieces = {}
        expected_moves = rook.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        moves = []
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))

    def test_4_4_take_all_black(self):
        rook = Rook(Position(4, 4), False)
        black_pieces = {Position(4, 4): rook}
        white_pieces = {Position(4, 5): Bishop(Position(4, 5)),
                        Position(5, 4): Bishop(Position(5, 4)),
                        Position(3, 4): Bishop(Position(3, 4)),
                        Position(4, 3): Bishop(Position(4, 3))}
        expected_moves = rook.getLegalMovesExcludingCheck(white_pieces, black_pieces)
        moves = [Position(4, 5), Position(5, 4), Position(3, 4), Position(4, 3)]
        for move in moves:
            self.assertTrue(move in expected_moves)
        self.assertEqual(len(expected_moves), len(moves))
