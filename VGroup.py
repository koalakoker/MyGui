import tkinter as tk
from InputElement import InputElement

class VGroup():
  def __init__(self, parent, bg):
    self.fields = {}
    self.parent = parent
    self.bg = bg
    self.frame = tk.Frame(self.parent, bg = "red") #self.bg)
    self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx=5, pady=5)
    self.isShown = False

  def add(self, name, labelUnit, initValue):
    self.fields[name] = InputElement(self.frame, labelUnit, initValue, self.bg)

  def show(self):
    if (self.isShown == False):
      maxLenLabel = 0
      maxLenUnit = 0
      for key, value in self.fields.items():
        lenLabelText = len(value.labelText)
        if (lenLabelText > maxLenLabel):
          maxLenLabel = lenLabelText
        lenUnitText = len(value.unitText)
        if (lenUnitText > maxLenUnit):
          maxLenUnit = lenUnitText
      for key, value in self.fields.items():
        value.show(maxLenLabel,maxLenUnit)
      self.isShown = True