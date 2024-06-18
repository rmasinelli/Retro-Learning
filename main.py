# main.py

import tkinter as tk
from ui import EduGame

if __name__ == "__main__":
    root = tk.Tk()
    game = EduGame(root)
    root.geometry("400x400")  # Set the window size
    root.mainloop()
