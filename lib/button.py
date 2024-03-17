import tkinter as tk

class Button():

    def __init__(self, parent, text, bg, command) -> None:
        self.button = tk.Button(parent, text=text, justify="left", command=command, bg = bg, fg="white", highlightbackground = bg)
        self.button.pack(padx=10, pady=5, side=tk.LEFT, anchor="s", expand=True)