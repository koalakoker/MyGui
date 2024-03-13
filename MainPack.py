import tkinter as tk

class MainPack():

  def __init__(self, parent, bg):
    self.parent = parent
    self.frame = tk.Frame(self.parent, bg = bg)
    self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx=0, pady=0)