import tkinter as tk

class InputElement():
  def __init__(self, parent, labelUnit, initValue) -> None:
    parts = labelUnit.split("#", 1)
    label = ""
    unit = ""
    if len(parts) == 1:
      label = parts[0]
    if len(parts) == 2:
      label, unit = parts
    
    self.frame = tk.Frame(parent)
    self.frame.pack(side=tk.TOP, fill=tk.X)

    self.label = tk.Label(self.frame, text=label, font=("Arial",16), anchor="w", width=12)
    self.label.pack(padx=10, pady=5, side=tk.LEFT, anchor="nw", expand=True)

    self.value = tk.IntVar(value = initValue)
    self.input = tk.Entry(self.frame, textvariable=self.value)
    self.input.pack(padx=10, pady=5, side=tk.LEFT, anchor="n", expand=True)

    self.unit = tk.Label(self.frame, text=unit, font=("Arial",16), anchor="w", width=5)
    self.unit.pack(padx=10, pady=5, side=tk.LEFT, anchor="n",expand=True)
