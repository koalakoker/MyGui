import tkinter as tk
from tkinter import messagebox
import InputElement

class MyGui():
  def __init__(self) -> None:
    self.root = tk.Tk()
    self.root.geometry("400x600")

    self.verticalLayout = tk.Frame(self.root)
    self.verticalLayout.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    self.fields = {}
    self.fields["PWMfreq"] = InputElement.InputElement(self.verticalLayout, "PWM frequency#Hz", 10000)
    self.fields["deadT"] = InputElement.InputElement(self.verticalLayout, "Dead time#ns", 100)
    self.fields["RepRate"] = InputElement.InputElement(self.verticalLayout, "Rep Rate", 1)
    
    self.fields["bottomRow"] = tk.Frame(self.verticalLayout)
    self.fields["bottomRow"].pack(side=tk.TOP, fill=tk.X)

    self.fields["calculate"] = tk.Button(self.fields["bottomRow"], text="Calculate", justify="left", command=self.calculate)
    self.fields["calculate"].pack(padx=10, pady=5, side=tk.LEFT, anchor="s", expand=True)

    self.fields["quit"] = tk.Button(self.fields["bottomRow"], text="Quit", justify="left", command=self.closeWin)
    self.fields["quit"].pack(padx=10, pady=5, side=tk.LEFT, anchor="s", expand=True)

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