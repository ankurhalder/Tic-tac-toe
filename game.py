def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if (
            len(set([board[row][col] for row in range(3)])) == 1
            and board[0][col] != " "
        ):
            return board[0][col]

    # Check diagonals
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != " ":
        return board[0][0]
    if len(set([board[i][2 - i] for i in range(3)])) == 1 and board[0][2] != " ":
        return board[0][2]

    return None


def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)

        row = int(
            input(
                "Enter row (0, 1, or 2) for player {}: ".format(players[current_player])
            )
        )
        col = int(
            input(
                "Enter column (0, 1, or 2) for player {}: ".format(
                    players[current_player]
                )
            )
        )

        if board[row][col] == " ":
            board[row][col] = players[current_player]

            winner = check_winner(board)
            if winner:
                print_board(board)
                print("Player {} wins!".format(winner))
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = (current_player + 1) % 2
        else:
            print("That position is already taken. Try again.")


if __name__ == "__main__":
    main()
