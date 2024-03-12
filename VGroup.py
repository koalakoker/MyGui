import tkinter as tk
from InputElement import InputElement

class VGroup():
  def __init__(self, parent):
    self.frame = tk.Frame(parent)
    self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    self.fields = {}

  def add(self, name, labelUnit, initValue):
    self.fields[name] = InputElement(self.frame, labelUnit, initValue)