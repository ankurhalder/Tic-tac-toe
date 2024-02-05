import tkinter as tk
from tkinter import messagebox
import webbrowser
import random


class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.configure(background="#f2f2f2")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = []
        self.create_board()

        self.heading_label = tk.Label(
            self.root,
            text="Tic Tac Toe By Ankur Halder",
            font=("Helvetica", 20),
            bg="#f2f2f2",
        )
        self.heading_label.grid(row=0, columnspan=3, pady=(10, 20))

        self.website_label = tk.Label(
            self.root,
            text=" ankurhalder.netlify.app ",
            font=("Helvetica", 12),
            bg="#f2f2f2",
        )
        self.website_label.grid(row=4, column=0, pady=(20, 10), sticky="e")

        self.website_link = tk.Label(
            self.root,
            text="Visit My Website",
            font=("Helvetica", 12, "underline"),
            bg="#f2f2f2",
            fg="blue",
            cursor="hand2",
        )
        self.website_link.grid(row=4, column=1, pady=(20, 10), sticky="w")
        self.website_link.bind(
            "<Button-1>", lambda e: webbrowser.open("https://ankurhalder.netlify.app")
        )

    def create_board(self):
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(
                    self.root,
                    text="",
                    font=("Helvetica", 24),
                    width=6,
                    height=2,
                    command=lambda row=i, col=j: self.button_click(row, col),
                    bg="#ffffff",
                    fg="#000000",
                )
                button.grid(row=i + 1, column=j, padx=5, pady=5)
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
                if self.current_player == "O":
                    self.computer_play()

    def computer_play(self):
        best_move = self.find_best_move()
        row, col = best_move
        self.board[row][col] = "O"
        self.buttons[row][col].config(text="O")

        winner = self.check_winner()
        if winner:
            messagebox.showinfo("Winner", f"Player {winner} wins!")
            self.reset_game()
        elif self.is_board_full():
            messagebox.showinfo("Tie", "It's a tie!")
            self.reset_game()
        else:
            self.current_player = "X"

    def find_best_move(self):
        best_score = float("-inf")
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def minimax(self, board, depth, is_maximizing):
        result = self.check_winner()
        if result:
            if result == "O":
                return 1
            elif result == "X":
                return -1
            else:
                return 0

        if self.is_board_full():
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "O"
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "X"
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = " "
                        best_score = min(score, best_score)
            return best_score

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
