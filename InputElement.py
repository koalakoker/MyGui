import tkinter as tk

class InputElement():
  def __init__(self, parent, labelText, unit, initValue) -> None:
    self.row1 = tk.Frame(parent)
    self.row1.pack(side=tk.TOP, fill=tk.X)

    self.label = tk.Label(self.row1, text=labelText, font=("Arial",16), justify ="left")
    self.label.pack(padx=10, pady=5, side=tk.LEFT, anchor="n", expand=True)

    self.inputValue = tk.IntVar(value = initValue)
    self.input = tk.Entry(self.row1, textvariable=self.inputValue)
    self.input.pack(padx=10, pady=5, side=tk.LEFT, anchor="n", expand=True)

    self.unit = tk.Label(self.row1, text=unit, font=("Arial",16), justify ="left")
    self.unit.pack(padx=10, pady=5, side=tk.LEFT, anchor="n",expand=True)
