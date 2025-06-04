import tkinter as tk
from views.main_view import MainView
from utils.database import init_db

init_db()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()