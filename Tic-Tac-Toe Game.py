import tkinter as tk ;
from tkinter import font ;
from typing import NamedTuple;
from itertools import cycle;

class Player(NamedTuple):
  label : str
  color : str

class Move(NamedTuple):
  row : str
  col : str
  label: str = "" 

BOARD_SIZE = 3 ;
DEFAULT_PLAYERS = (
  Player(label='X',color="blue"),
  Player(label='O',color="green")
)

class TicTacToeGame : 
  def __init__(self , players=DEFAULT_PLAYERS , board_size = BOARD_SIZE):
    self.players = cycle(players)
    self.board_size = board_size
    self.current_player = next(self.players)
    self.winner_combo = []
    self.current_moves = []
    self.has_winner = False
    self.winning_combo = []
    self.setup_board()

  def setup_board(self):
    self.current_moves = [
      [Move(str(row), str(col)) for col in range(self.board_size)]
      for row in range(self.board_size)]
      
    self.winning_combos = self.get_winning_combos()  

  def get_winning_combos(self):
    rows = [
      [(move.row, move.col) for move in row]
      for row in self.current_moves
    ]
    columns = [list(col) for col in zip(rows)]
    first_diagonal = [row[i] for i , row in enumerate(rows)]
    second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
    return rows + columns + [first_diagonal+second_diagonal]


  def is_valid_move(self,move):
    row,col=int(move.row),int(move.col)
    move_was_not_played = self.current_moves[row][col].label==""
    no_winner = not self.has_winner
    return move_was_not_played and no_winner 

class TicTacToeBoard(tk.Tk):
  def __init__(self):
    super().__init__()
    self._cells = {}
    self.create_board_display()
    self.create_board_grid()

  def create_board_display(self):
    display_frame = tk.Frame(master=self)
    display_frame.pack(fill=tk.X)
    self.display = tk.Label(
      master= display_frame,
      text = "Ready",
      font = font.Font(size=28,weight="bold",underline=True)
    )
    self.display.pack()

  def create_board_grid(self):
    grid_frame = tk.Frame(master=self)
    grid_frame.pack()
    for row in range(3):
      self.rowconfigure(row,weight=1,minsize=50)
      self.columnconfigure(row,weight=1,minsize=75)
      for col in range(3):
        button = tk.Button(
          master=grid_frame,
          text="",
          font= font.Font(size=36,weight="bold"),
          fg="black",
          width=3,
          height=2,
          highlightbackground="lightblue",
        )
        self._cells[button] = (row,col)
        button.grid(
          row = row,
          column=col,
          padx = 5,
          pady = 5,
          sticky="nsew",
        )

def main():
  board = TicTacToeBoard()
  board.mainloop()

if __name__ == "__main__" :
  main()