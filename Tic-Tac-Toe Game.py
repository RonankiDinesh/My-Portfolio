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
    row,col=move.row,move.col
    move_was_not_played = self.current_moves[row][col].label==""
    no_winner = not self.has_winner
    return move_was_not_played and no_winner 

  def process_move(self,move):
    row,col=move.row,move.col
    self.current_moves[row][col] = move
    for combo in self.winning_combos:
      results = set(
        self.current_moves[int(n)][int(m)].label
        for n,m in combo
      )
      is_win = (len(results) == 1) and ("" not in results)

      if is_win :
        self.has_winner = True
        self.winner_combo = combo
        break

  def _has_winner(self) :
    return self.has_winner

  def is_tied(self):
     no_winner = not self.has_winner
     played_moves = (
      move.label for row in self.current_moves for move in row
     )
     return no_winner and all(played_moves)

  def toggle_player(self):
    self.current_player = next(self.players)

class TicTacToeBoard(tk.Tk):
  def __init__(self , game):
    super().__init__()
    self._cells = {}
    self._game = game
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
    for row in range(self._game.board_size):
      self.rowconfigure(row,weight=1,minsize=50)
      self.columnconfigure(row,weight=1,minsize=75)
      for col in range(self._game.board_size):
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
        button.bind("<ButtonPress-1>", self.play)
        button.grid(
          row = row,
          column=col,
          padx = 5,
          pady = 5,
          sticky="nsew",
        )
  def play(self,event):
    clicked_btn = event.widget
    row,col = self._cells[clicked_btn]
    move = Move(row,col,self._game.current_player.label)
    if self._game.is_valid_move(move):
      self._update_button(clicked_btn)
      self._game.process_move(move)
      if self._game.is_tied():
        self._update_display(msg="Tied Game" , color ="red")
      elif self._game.has_winner():
        self.highlight_cells()
        msg = f'Player"{self._game.current_player.label}" won'
        color =self._game.current_player.color
        self._update_display(msg,color)
      else :
        self._game.toggle_player()
        msg = f'Player "{self._game.current_player.label}"turn'
        self._update_display(msg)
  def _update_button(self,clicked_btn):
    clicked_btn.config(text = self._game.current_player.label)
    clicked_btn.config(fg = self._game.current_player.color)
  def _update_display(self, msg , color = "black"):
    self.display["text"] = msg
    self.display["fg"] = color
  def highlight_cells(self):
    for button,coordinates in self._cells.items():
      if coordinates in self._game.winner_combo :
        button.config(highlightbackground = "red")

def main():
  game= TicTacToeGame()
  board = TicTacToeBoard(game)
  board.mainloop()
if __name__ == "__main__" :
  main()