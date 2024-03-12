import tkinter as tk
from tkinter import messagebox
from InputElement import InputElement
from VGroup import VGroup

class MyGui():
  def __init__(self) -> None:
    self.root = tk.Tk()
    self.root.geometry("400x600")

    self.vg = VGroup(self.root)

    self.vg.add("PWMfreq", "PWM frequency#Hz", 10000)
    self.vg.add("deadT", "Dead time#ns", 100)
    self.vg.add("RepRate", "Rep Rate", 1)
    
    self.bottomRow = tk.Frame(self.root)
    self.bottomRow.pack(side=tk.TOP, fill=tk.X)

    self.calculate = tk.Button(self.bottomRow, text="Calculate", justify="left", command=self.calculate)
    self.calculate.pack(padx=10, pady=5, side=tk.LEFT, anchor="s", expand=True)

    self.quit = tk.Button(self.bottomRow, text="Quit", justify="left", command=self.closeWin)
    self.quit.pack(padx=10, pady=5, side=tk.LEFT, anchor="s", expand=True)

    self.root.bind('<Escape>', self.closeWin)
    self.root.mainloop()

  def calculate(self):
    print("Calc")

  def closeWin(self,key = None):
    if (messagebox.askyesno(title="Quit?", message="Do you really want to quit?")):
      self.root.destroy()
    else:
      self.root.focus_force()

MyGui()