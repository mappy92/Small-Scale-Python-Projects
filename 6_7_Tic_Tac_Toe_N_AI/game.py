from player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # Using a single list for 3*3 board
        self.current_winner = None # Keeps track of the winner
    
    def print_board(self):
        # getting rows on the board
        for row in [self.board[(i*3):(i+1)*3] for i in range(3)]:
            print('| '+ ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+ ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for(i, spot) in enumerate(self.board):
        #     # ['X', 'X', 'O'] --> [(0, 'X'), (1, 'X'), (2, 'O')]
        #     if(spot == ' '):
        #         moves.append(i)
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        # return len(self.available_moves); 
        return self.available_moves.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter

            return True
        return False
   
    def winner(self, square, letter):
        # winner if 3 in a row anywhere 
        # first check the rows
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # now check columns 
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # now diagonal 
        # but only if the square is even (0, 2, 4, 6, 8)
        # these are the only possible moves in diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True 
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        # if all these checks fail then we don't have a winner
        return False
        


def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game(letter)! or None for a tie
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # statring letter
    # iterate while the game has empty squares 
    # we don't worry about the winner just end the loop for now 
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)    

        # if a player makes a move 
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print(' ') #empty line
            # before switch if the current player won then we will end the game 
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                    return letter
            # after we made move, we need to switch the letter
            letter = 'O' if letter == 'X' else 'X'
            # tiny break 
            time.sleep(0.8)
            # if letter == 'X':
            #     letter ='O'
            # else: 
            #     letter = 'X'

    # if we won then ? that should should be right after a player makes a move
    if print_game & len(game.ava):
            print('It\'s a tie')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)