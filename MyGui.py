import tkinter as tk
from tkinter import messagebox
from InputElement import InputElement
from VGroup import VGroup
from MainPack import MainPack
from load import load
from calc import calc

mainBg = "#00234B"
class MyGui():
  def __init__(self) -> None:
    self.root = tk.Tk()
    self.root.title("GUI")
    self.root.geometry("400x600")
    self.root.configure(bg=mainBg)

    self.mainPack = MainPack(self.root, mainBg)
    self.vg = load("defParams.txt", mainBg, lambda bg : VGroup(self.mainPack.frame, bg))
    
    self.bottomRow = tk.Frame(self.root, bg = mainBg)
    self.bottomRow.pack(side=tk.BOTTOM, fill=tk.X)

    self.calculate = tk.Button(self.bottomRow, text="Calculate", justify="left", command=self.calculate, bg = mainBg, highlightbackground = mainBg)
    self.calculate.pack(padx=10, pady=5, side=tk.LEFT, anchor="s", expand=True)

    self.quit = tk.Button(self.bottomRow, text="Quit", justify="left", command=self.closeWin, bg = mainBg, highlightbackground = mainBg)
    self.quit.pack(padx=10, pady=5, side=tk.LEFT, anchor="s", expand=True)

    self.root.bind('<Escape>', self.closeWin)
    
    self.root.mainloop()

  def calculate(self):
    calc("formulae.txt", self.vg)
    self.vg["results"].show()

  def closeWin(self,key = None):
    if (messagebox.askyesno(title="Quit?", message="Do you really want to quit?")):
      self.root.destroy()
    else:
      self.root.focus_force()

MyGui()