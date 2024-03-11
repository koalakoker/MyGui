import tkinter as tk
from tkinter import messagebox

class MyGui():
  def __init__(self) -> None:
    self.root = tk.Tk()
    self.root.geometry("800x600")

    self.label = tk.Label(self.root, text="Label", font=("Arial",16), justify ="left")
    self.label.pack(padx=10, pady=5, anchor="w")

    self.quit = tk.Button(self.root, text="Quit", justify="left", command=self.closeWin)
    self.quit.pack(padx=10, pady=5, anchor="sw")

    self.root.bind('<Escape>', self.closeWin)
    self.root.mainloop()

  def closeWin(self,key = None):
    if (messagebox.askyesno(title="Quit?", message="Do you really want to quit?")):
      self.root.destroy()
    else:
      self.root.focus_force()

MyGui()