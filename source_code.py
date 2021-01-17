"""

Main class file for the chequers game engine

"""

import random


class Piece:
    """

    Class for defining a piece used in the game

    """
    def __init__(self, piece_color, piece_type, player_owner):
        """

        Initialize the Piece with an owner, a color and a type (pawn or queen)

        :param piece_color:
        :param piece_type:
        :param player_owner:
        """

        self.player_owner = player_owner

        if piece_color in ('B', 'W'):
            self.piece_color = piece_color
        if piece_color == 'B':
            self.disp_col = '\033[1;30m'

        elif piece_color == 'W':
            self.disp_col = '\033[1;36m'

        else:
            raise NameError('Piece color has to be B or W')

        # Pawn or queen
        if piece_type in ('P', 'Q'):
            self.piece_type = piece_type
        else:
            raise NameError('Piece type has to be P or Q')


class Board:
    """

    Class for the chequers board itself

    """

    def __init__(self, game_version):
        """

        Can start a game with a different board size depending on the game variant

        :param game_version:
        """
        self.game_version = game_version

        if game_version == 'International':
            self.grid = [['.'] * 10 for _ in range(10)]
            self.size_b = 10

        elif game_version in ('British', 'American', 'Russian'):
            self.grid = [['.'] * 8 for _ in range(8)]
            self.size_b = 8
        else:
            raise NameError('Incorrect version specified: must be American, British, Russian or International')

    def display_grid(self):
        """

        Display the pieces in the grid with their associated color

        :return:
        """
        col_numerals = [str(i) for i in range(0, self.size_b)]

        print('  ' + ' '.join(col_numerals))

        ticker = 0
        for line in self.grid:
            print(ticker, end='')

            ticker += 1

            for obj in line:
                if isinstance(obj, str) and obj == '.':
                    print('|'+obj, end='')

                elif isinstance(obj, Piece):
                    print('|' + obj.disp_col + obj.piece_type + '\033[0m', end='')

                else:
                    raise NameError('Unidentified piece spotted')

            print('|')

        print('\n')

    def valid_coord(self, coordinate):
        """

        Check if we are still within the board

        :param coordinate:
        :return:
        """
        return self.size_b > coordinate >= 0 and isinstance(coordinate, int)

    def valid_board_coord(self, coord1, coord2):
        """

        Check if the board coordinate is valid

        :param coord1:
        :param coord2:
        :return:
        """

        return self.valid_coord(coord1) and self.valid_coord(coord2)

    def add_piece(self, piece, coord1, coord2):
        """

        For a given set of coordinates, we add a piece

        :param piece:
        :param coord1:
        :param coord2:
        :return:
        """
        if self.valid_board_coord(coord1, coord2):

            if isinstance(piece, Piece):

                if isinstance(self.grid[coord1][coord2], Piece):
                    raise NameError('We already have a piece at the current place')

                else:
                    self.grid[coord1][coord2] = piece

            else:
                raise NameError('Add piece did not get a piece as argument ')

        else:
            raise NameError('Invalid coordinates given when adding a piece')

    def initialize_game_board(self, player_first, player_second):
        """

        Fill up the chequers board

        :param player_first:
        :param player_second:
        :return:
        """

        for i in range(self.size_b):
            for j in range(self.size_b):
                if i + 1 < self.size_b / 2:
                    if (i + j) % 2 == 1:
                        self.add_piece(Piece('W', 'P', player_second), i, j)
                if i > self.size_b / 2:
                    if (i + j) % 2 == 1:
                        self.add_piece(Piece('B', 'P', player_first), i, j)

    def initialize_game(self, player1, player2):
        """

        Set the pieces on the board and randomly select who gets to go first

        :param player1:
        :param player2:
        :return:
        """

        player_first = player1 if random.random() < 0.5 else player2
        player_second = player1 if player_first == player2 else player2

        self.initialize_game_board(player_first, player_second)

        return player_first


class Player:
    """

    Class for players who interact with the game

    """
    def __init__(self, name, is_computer=False):
        """

        Players have a name and can be computers

        :param name:
        :param is_computer:
        """
        self.name = name
        self.is_computer = is_computer

    def print_player_info(self):
        """Simple printout of the name"""
        print('The player name is ' + self.name)


class Game:
    """

    Main class for setting up a game and running it

    """
    def __init__(self, player1, player2, game_version='British'):
        self.board = Board(game_version)
        self.player1 = player1
        self.player2 = player2
        self.player_first = self.board.initialize_game(player1, player2)
        print('Creating a game for ' + self.player1.name + ' vs ' + self.player2.name)
        print('Player ' + self.player_first.name + ' starts first !')

    def valid_move(self, player, start_position, end_position):
        """

        Determine if we have a valid move; if not we display a message indicating the reason
        Positions enter as a vector

        :param player
        :param start_position:
        :param end_position:
        :return:
        """

        if self.board.valid_board_coord(start_position[0], start_position[1]) is False:
            print('Starting position is not on the board')
            return False

        if self.board.valid_board_coord(end_position[0], end_position[1]) is False:
            print('End position is not on the board')
            return False

        if self.board.grid[start_position[0]][start_position[1]] == '.':
            print('Starting position has to correspond to a piece')
            return False

        if self.board.grid[start_position[0]][start_position[1]].player_owner != player:
            print('You have to select one of your pieces to move')
            return False

        if self.board.grid[end_position[0]][end_position[1]] != '.':
            print('You have end your move on an empty spot')
            return False

        return True


def main():

    board1 = Board('British')
    board1.display_grid()

    player1 = Player('A')
    player2 = Player('B')

    game = Game(player1, player2)
    game.board.display_grid()

    game.valid_move(player1, [5, 0], [4, 1])

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
