from Matrix import Matrix
import random

class GoldRush(Matrix):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.score_player1 = 0  #score of player1
        self.score_player2 = 0 #score of player2
        self.winner = ""#change from win to winner
        self.coins_count = 0 #change name coins->coins count here and where its needed in the code

    def load_board(self):
        if self.rows == 0 and self.cols == 0:
            self.matrix = []
            return

        self.matrix = []
        coin_symbol="$"#added names to the symbols
        empty_path_symbol="."
        wall_symbol="||"
        elements = [coin_symbol, empty_path_symbol, wall_symbol]###change coins to $ and wall to || and changed in the code where its needed
        coins_count = 0

        for row in range(self.rows):#change i into meaningful pr row refer to row index
            self.matrix.append([])
            for col in range(self.cols):#change j into col
                if row % 2 != 0:
                    rand_element_index = random.randint(0, 1)#change rand index to rand_element_index
                    rand_element = elements[rand_element_index]
                    self.matrix[row].append(rand_element)
                    if rand_element == "$":
                        coins_count += 1
                else:
                    wall_index = 2
                    wall = elements[wall_index]
                    self.matrix[row].append(wall)

            column_step = random.randint(1, 2)#change rand to column_step
            for random_col in range(1, self.cols, column_step):#change k to random col
                column_step += 1
                rand_element_index = random.randint(0, 1)#change rand_index to rand_element_index
                chosen_element = elements[rand_element_index]#change rand_element to chosen element
                self.matrix[row][random_col] = chosen_element
                if chosen_element == "$":
                    coins_count += 1

        self.matrix[0][0] = "player1"
        self.matrix[self.rows - 1][self.cols - 1] = "player2"
        self.coins_count = coins_count

        if coins_count < 10:
            return self.load_board()
        else:
            return self.matrix

    def _check_return_winner(self, player):#change def check win to check_return_winner
        player_num = player[-1]
        score = getattr(self, f"score_player{player_num}")#change s into score_player
        if score == 50:#changed from 100 to more more reasanble score 
            self.winner = player
            return self.winner

    def change_player_turn(self, curr_player):#change def check_other_player name to change player turn and player pr into curr_player
        otherPlayer = None
        if curr_player == "player1":
            otherPlayer = "player2"
            return otherPlayer
        elif curr_player == "player2":
            otherPlayer = "player1"
            return otherPlayer
        

    def process_player_move(self, curr_row, curr_col, player, delta_row, delta_col):#change name from_move to process_player_move
        other_player = self.change_player_turn(player)
        new_row, new_col = curr_row + delta_row, curr_col + delta_col

        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return

        if self.matrix[new_row][new_col] not in ["||", other_player]:
            if self.matrix[new_row][new_col] == "$":
                self._score(player)

            self.matrix[curr_row][curr_col] = "."
            self.matrix[new_row][new_col] = player

        return self._check_return_winner(player)

    def _move_down(self, curr_row, curr_col, player):
        return self.process_player_move(curr_row, curr_col, player, 1, 0)

    def _move_up(self, curr_row, curr_col, player):
        return self.process_player_move(curr_row, curr_col, player, -1, 0)

    def _move_right(self, curr_row, curr_col, player):
        return self.process_player_move(curr_row, curr_col, player, 0, 1)

    def _move_left(self, curr_row, curr_col, player):
        return self.process_player_move(curr_row, curr_col, player, 0, -1)

    def move_player(self, player, direction):
        curr_row, curr_col = None, None

        for i, row in enumerate(self.matrix):
            for j, value in enumerate(row):
                if value == player:
                    curr_row, curr_col = i, j
                    break
            if curr_row is not None:
                break

        if direction == "down":
            self._move_down(curr_row, curr_col, player)
        elif direction == "up":
            self._move_up(curr_row, curr_col, player)
        elif direction == "right":
            self._move_right(curr_row, curr_col, player)
        elif direction == "left":
            self._move_left(curr_row, curr_col, player)

    def _score(self, player):
        player_num = player[-1]
        score_attr = f"score_player{player_num}"#change s to score_player to match the change above
        setattr(self, score_attr, getattr(self, score_attr) + 10)
        print("player current score:",getattr(self, score_attr))#added a message to make it clear what is the number on the screen
