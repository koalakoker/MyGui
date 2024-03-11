import tkinter as tk
from tkinter import messagebox

class MyGui():
  def __init__(self) -> None:
    self.root = tk.Tk()
    self.root.geometry("400x600")

    self.verticalLayout = tk.Frame(self.root)
    self.verticalLayout.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    self.row1 = tk.Frame(self.verticalLayout)
    self.row1.pack(side=tk.TOP, fill=tk.X)

    self.label = tk.Label(self.row1, text="PWM frequency", font=("Arial",16), justify ="left")
    self.label.pack(padx=10, pady=5, side=tk.LEFT, anchor="n", expand=True)

    self.inputValue = tk.IntVar(value=10000)
    self.input = tk.Entry(self.row1, textvariable=self.inputValue)
    self.input.pack(padx=10, pady=5, side=tk.LEFT, anchor="n", expand=True)

    self.unit = tk.Label(self.row1, text="Hz", font=("Arial",16), justify ="left")
    self.unit.pack(padx=10, pady=5, side=tk.LEFT, anchor="n",expand=True)

    self.row2 = tk.Frame(self.verticalLayout)
    self.row2.pack(side=tk.TOP, fill=tk.X)

    self.quit = tk.Button(self.row2, text="Quit", justify="left", command=self.closeWin)
    self.quit.pack(padx=10, pady=5, side=tk.LEFT, anchor="s", expand=True)

    self.root.bind('<Escape>', self.closeWin)
    self.root.mainloop()

  def closeWin(self,key = None):
    if (messagebox.askyesno(title="Quit?", message="Do you really want to quit?")):
      self.root.destroy()
    else:
      self.root.focus_force()

MyGui()