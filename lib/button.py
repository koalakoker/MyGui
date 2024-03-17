import tkinter as tk
from tkinter import ttk
class Button():

    def __init__(self, parent, text, bg, command) -> None:
        self.button = ttk.Button(parent, text=text, command=command)
        self.button.pack(padx=10, pady=5, side=tk.LEFT, anchor="s", expand=True)