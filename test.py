import tkinter as tk

class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My App")

        # Set the background color of the frame
        bg_color = "#ADD8E6"
        self.root.configure(bg=bg_color)

        # Create a frame with the same background color
        self.frame = tk.Frame(self.root, bg=bg_color)
        self.frame.pack(padx=10, pady=10)

        # Create an Entry with the same background color
        self.entry = tk.Entry(
            self.frame,
            bg="black",
            highlightthickness=0,
            bd=0,
            relief=tk.FLAT,
            highlightbackground=bg_color
        )
        self.entry.pack(padx=5, pady=5)

        # Create a button for testing
        self.button = tk.Button(
            self.frame,
            text="Click Me",
            bg=bg_color,
            command=self.on_button_click,
            highlightthickness=0,
            bd=0,
            relief=tk.FLAT,
            highlightbackground=bg_color
        )
        self.button.pack(padx=5, pady=5)

    def on_button_click(self):
        print("Button clicked!")

    def run(self):
        self.root.mainloop()

# Create an instance of your app
my_app = MyApp()

# Run the app
my_app.run()
