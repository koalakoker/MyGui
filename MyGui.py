import tkinter as tk
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
    self.root.geometry("400x600")
    self.root.configure(bg=mainBg)

    self.mainPack = MainPack(self.root, mainBg)
    self.vg = loadParams("defParams.txt", mainBg, lambda bg : VGroup(self.mainPack.frame, bg))
    
    self.bottomRow = tk.Frame(self.root, bg = mainBg)
    self.bottomRow.pack(side=tk.BOTTOM, fill=tk.X)


    self.calculate = Button(self.bottomRow, text="Calculate", bg = mainBg, command=self.calculate)
    self.save = Button(self.bottomRow, text="Save", command=self.save, bg = mainBg)
    self.load = Button(self.bottomRow, text="Load", command=self.load, bg = mainBg)
    self.quit = Button(self.bottomRow, text="Quit", command=self.closeWin, bg = mainBg)

    image = Image.open("fig.jpg")
    image = image.resize((300, 200), Image.BICUBIC)
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