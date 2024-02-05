import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(
                    self.root,
                    text="",
                    width=8,
                    height=4,
                    command=lambda row=i, col=j: self.button_click(row, col),
                )
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Winner", f"Player {winner} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tie", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for row in self.board:
            if len(set(row)) == 1 and row[0] != " ":
                return row[0]

        for col in range(3):
            if (
                len(set([self.board[row][col] for row in range(3)])) == 1
                and self.board[0][col] != " "
            ):
                return self.board[0][col]

        if (
            len(set([self.board[i][i] for i in range(3)])) == 1
            and self.board[0][0] != " "
        ):
            return self.board[0][0]

        if (
            len(set([self.board[i][2 - i] for i in range(3)])) == 1
            and self.board[0][2] != " "
        ):
            return self.board[0][2]

        return None

    def is_board_full(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.current_player = "X"

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()
