import tkinter as tk

class InputElement():
  def __init__(self, parent, labelUnit, value, bg) -> None:
    parts = labelUnit.split("#", 1)
    label = ""
    unit = ""
    if len(parts) == 1:
      label = parts[0]
    if len(parts) == 2:
      label, unit = parts
    self.parent = parent
    self.labelText = label
    self.unitText = unit
    self.value = value
    self.bg = bg
    self.frame = tk.Frame(self.parent) # BG is not showed
    self.frame.pack(side=tk.TOP, fill=tk.X)


  def show(self, labelWidth, unitWidth):
    self.label = tk.Label(self.frame, text=self.labelText, font=("Arial",16), anchor="w", width=labelWidth, bg=self.bg)
    self.label.pack(padx=0, pady=0, side=tk.LEFT, anchor="nw", expand=False, fill=tk.Y)

    self.value = tk.IntVar(value = self.value)
    self.input = tk.Entry(self.frame, textvariable=self.value, highlightbackground = self.bg)
    self.input.pack(padx=0, pady=0, side=tk.LEFT, anchor="n", expand=True, fill=tk.X)

    self.unit = tk.Label(self.frame, text=self.unitText, font=("Arial",16), anchor="w", width=unitWidth, bg=self.bg)
    self.unit.pack(padx=0, pady=0, side=tk.LEFT, anchor="n",expand=False, fill=tk.Y)
    