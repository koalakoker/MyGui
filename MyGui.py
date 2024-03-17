import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from lib.VGroup import VGroup
from lib.MainPack import MainPack
from lib.button import Button
from lib.load import loadParams, load
from lib.calc import calc
from lib.save import save

mainBg = "#00234B"
class MyGui():
  def __init__(self) -> None:
    self.root = tk.Tk()
    self.root.title("Second order equation solver")
    self.root.geometry("450x600")
    self.root.configure(bg=mainBg)

    # Create a style
    style = ttk.Style()
    style.configure("TButton", foreground="black")  # Set text color for TButton

    self.mainPack = MainPack(self.root, mainBg)
    self.vg = loadParams("defParams.txt", mainBg, lambda bg : VGroup(self.mainPack.frame, bg))
    
    self.bottomRow = tk.Frame(self.root, bg = mainBg)
    self.bottomRow.pack(side=tk.BOTTOM, fill=tk.X)

    self.calcBTN = Button(self.bottomRow, text="Calc", bg = mainBg, command=self.calculate)
    self.saveBTN = Button(self.bottomRow, text="Save", bg = mainBg, command=self.save)
    self.loadBTN = Button(self.bottomRow, text="Load", bg = mainBg, command=self.load)
    self.quitBTN = Button(self.bottomRow, text="Quit", bg = mainBg, command=self.closeWin)

    image = Image.open("fig.jpg")
    image = image.resize((250, 150), Image.BICUBIC)
    tk_image = ImageTk.PhotoImage(image)
    label = tk.Label(self.root, image = tk_image)
    label.pack(pady=20)

    self.root.bind('<Escape>', self.closeWin)
    
    self.root.mainloop()

  def calculate(self):
    calc("formulae.py", self.vg)
    self.vg["results"].show()

  def save(self):
    save(self.vg)

  def load(self):
    load(self.vg)

  def closeWin(self,key = None):
    if (messagebox.askyesno(title="Quit?", message="Do you really want to quit?")):
      self.root.destroy()
    else:
      self.root.focus_force()

MyGui()