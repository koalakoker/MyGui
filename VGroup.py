import tkinter as tk
from InputElement import InputElement

class VGroup():
  def __init__(self, parent):
    self.frame = tk.Frame(parent)
    self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    self.fields = {}

  def add(self, name, labelUnit, initValue):
    self.fields[name] = InputElement(self.frame, labelUnit, initValue)

  def show(self):
    maxLenLabel = 0
    maxLenUnit = 0
    for key, value in self.fields.items():
      if (len(value.label) > maxLenLabel):
        maxLenLabel = len(value.label)
      if (len(value.unit) > maxLenUnit):
        maxLenUnit = len(value.unit)
    for key, value in self.fields.items():
      value.show(maxLenLabel,maxLenUnit)