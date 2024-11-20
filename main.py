from game import GoldRush


def play_game():
    print("Welcome to Gold Rush!")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    game = GoldRush(rows, cols)
    game.load_board()
    game.print_matrix()

    while not game.winner:
        player = "player1"
        direction = input(f"{player}, enter your move (up, down, left, right): ").strip().lower()
        game.move_player(player, direction)
        game.print_matrix()
        if game._check_return_winner(player):#change functions and parameters name according to what i changed in the other classes
            print(f"{player} wins!")
            break

        player = "player2"
        direction = input(f"{player}, enter your move (up, down, left, right): ").strip().lower()
        game.move_player(player, direction)
        game.print_matrix()
        if game._check_return_winner(player):
            print(f"{player} wins!")
            break

if __name__ == "__main__":
    play_game()