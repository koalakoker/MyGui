import tkinter as tk
from tkinter import messagebox
from InputElement import InputElement
from VGroup import VGroup

mainBg = "#00234B"

class MyGui():
  def __init__(self) -> None:
    self.root = tk.Tk()
    self.root.geometry("400x600")

    self.vgIn = VGroup(self.root, mainBg)

    self.vgIn.add("PWMfreq", "PWM frequency#Hz", 10000)
    self.vgIn.add("deadT", "Dead time#ns", 100)
    self.vgIn.add("RepRate", "Rep Rate", 1)

    self.vgOut = VGroup(self.root, "darkgray")

    self.vgOut.add("Duty", "Duty cycle", 0)
    self.vgOut.add("MMI", "Maximum modulation Index", 0)

    self.vgIn.show()
    
    self.bottomRow = tk.Frame(self.root, bg = mainBg)
    self.bottomRow.pack(side=tk.TOP, fill=tk.X)

    self.calculate = tk.Button(self.bottomRow, text="Calculate", justify="left", command=self.calculate, bg = mainBg, highlightbackground = mainBg)
    self.calculate.pack(padx=10, pady=5, side=tk.LEFT, anchor="s", expand=True)

    self.quit = tk.Button(self.bottomRow, text="Quit", justify="left", command=self.closeWin, bg = mainBg, highlightbackground = mainBg)
    self.quit.pack(padx=10, pady=5, side=tk.LEFT, anchor="s", expand=True)

    self.root.bind('<Escape>', self.closeWin)
    
    self.root.mainloop()

  def calculate(self):
    self.vgOut.show()

  def closeWin(self,key = None):
    if (messagebox.askyesno(title="Quit?", message="Do you really want to quit?")):
      self.root.destroy()
    else:
      self.root.focus_force()

MyGui()