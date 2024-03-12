import tkinter as tk

class InputElement():
  def __init__(self, parent, labelUnit, value) -> None:
    parts = labelUnit.split("#", 1)
    label = ""
    unit = ""
    if len(parts) == 1:
      label = parts[0]
    if len(parts) == 2:
      label, unit = parts
    self.parent = parent
    self.label = label
    self.unit = unit
    self.value = value
    self.frame = tk.Frame(self.parent)
    self.frame.pack(side=tk.TOP, fill=tk.X)
    
  
  def show(self, labelWidth, unitWidth):
    self.label = tk.Label(self.frame, text=self.label, font=("Arial",16), anchor="w", width=labelWidth)
    self.label.pack(padx=10, pady=5, side=tk.LEFT, anchor="nw", expand=True)

    self.value = tk.IntVar(value = self.value)
    self.input = tk.Entry(self.frame, textvariable=self.value)
    self.input.pack(padx=10, pady=5, side=tk.LEFT, anchor="n", expand=True)

    self.unit = tk.Label(self.frame, text=self.unit, font=("Arial",16), anchor="w", width=unitWidth)
    self.unit.pack(padx=10, pady=5, side=tk.LEFT, anchor="n",expand=True)
    