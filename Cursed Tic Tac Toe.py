import tkinter as tk
from tkinter import messagebox

def main():
    game = Application()
    game.mainloop()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Tic Tac Toe")
        self.geometry('300x300')
        self.config(bg="#3b3b3b")
        self.resizable(False, False)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=0)

        showPlayerText = tk.Label(self, text=f"Cursed Tic Tac Toe", font=('Times New Roman', 11, 'bold'))

        showPlayerText.grid(row=0, columnspan=3, sticky="nsew", pady=(5, 10), padx=1)

        defaultButtonValue = "_"

        selected = "X"

        def button1select():
            nonlocal selected
            if button1["text"] == "_":
                if selected == "X":
                    button1.config(text=f"{selected}")
                    selected = "O"
                elif selected == "O":
                    button1.config(text=f"{selected}")
                    selected = "X"
            else:
                messagebox.showerror("Slot Taken", "This spot has already been taken")

        def button2select():
            nonlocal selected
            if button2["text"] == "_":
                if selected == "X":
                    button2.config(text=f"{selected}")
                    selected = "O"
                elif selected == "O":
                    button2.config(text=f"{selected}")
                    selected = "X"
            else:
                messagebox.showerror("Slot Taken", "This spot has already been taken")

        def button3select():
            nonlocal selected
            if button3["text"] == "_":
                if selected == "X":
                    button3.config(text=f"{selected}")
                    selected = "O"
                elif selected == "O":
                    button3.config(text=f"{selected}")
                    selected = "X"
            else:
                messagebox.showerror("Slot Taken", "This spot has already been taken")

        def button4select():
            nonlocal selected
            if button4["text"] == "_":
                if selected == "X":
                    button4.config(text=f"{selected}")
                    selected = "O"
                elif selected == "O":
                    button4.config(text=f"{selected}")
                    selected = "X"
            else:
                messagebox.showerror("Slot Taken", "This spot has already been taken")

        def button5select():
            nonlocal selected
            if button5["text"] == "_":
                if selected == "X":
                    button5.config(text=f"{selected}")
                    selected = "O"
                elif selected == "O":
                    button5.config(text=f"{selected}")
                    selected = "X"
            else:
                messagebox.showerror("Slot Taken", "This spot has already been taken")

        def button6select():
            nonlocal selected
            if button6["text"] == "_":
                if selected == "X":
                    button6.config(text=f"{selected}")
                    selected = "O"
                elif selected == "O":
                    button6.config(text=f"{selected}")
                    selected = "X"
            else:
                messagebox.showerror("Slot Taken", "This spot has already been taken")

        def button7select():
            nonlocal selected
            if button7["text"] == "_":
                if selected == "X":
                    button7.config(text=f"{selected}")
                    selected = "O"
                elif selected == "O":
                    button7.config(text=f"{selected}")
                    selected = "X"
            else:
                messagebox.showerror("Slot Taken", "This spot has already been taken")

        def button8select():
            nonlocal selected
            if button8["text"] == "_":
                if selected == "X":
                    button8.config(text=f"{selected}")
                    selected = "O"
                elif selected == "O":
                    button8.config(text=f"{selected}")
                    selected = "X"
            else:
                messagebox.showerror("Slot Taken", "This spot has already been taken")

        def button9select():
            nonlocal selected
            if button9["text"] == "_":
                if selected == "X":
                    button9.config(text=f"{selected}")
                    selected = "O"
                elif selected == "O":
                    button9.config(text=f"{selected}")
                    selected = "X"
            else:
                messagebox.showerror("Slot Taken", "This spot has already been taken")

        def restartGame():
            button1.config(text="_")
            button2.config(text="_")
            button3.config(text="_")
            button4.config(text="_")
            button5.config(text="_")
            button6.config(text="_")
            button7.config(text="_")
            button8.config(text="_")
            button9.config(text="_")

        button1 = tk.Button(self, text=f"{defaultButtonValue}", command = button1select)
        button2 = tk.Button(self, text=f"{defaultButtonValue}", command = button2select)
        button3 = tk.Button(self, text=f"{defaultButtonValue}", command = button3select)
        button4 = tk.Button(self, text=f"{defaultButtonValue}", command = button4select)
        button5 = tk.Button(self, text=f"{defaultButtonValue}", command = button5select)
        button6 = tk.Button(self, text=f"{defaultButtonValue}", command = button6select)
        button7 = tk.Button(self, text=f"{defaultButtonValue}", command = button7select)
        button8 = tk.Button(self, text=f"{defaultButtonValue}", command = button8select)
        button9 = tk.Button(self, text=f"{defaultButtonValue}", command = button9select)

        restartButton = tk.Button(self, text=f"Restart Game", command = restartGame)

        button1.grid(row=1, column=0, sticky="nsew", padx=1, pady=1)
        button2.grid(row=1, column=1, sticky="nsew", padx=1, pady=1)
        button3.grid(row=1, column=2, sticky="nsew", padx=1, pady=1)
        button4.grid(row=2, column=0, sticky="nsew", padx=1, pady=1)
        button5.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)
        button6.grid(row=2, column=2, sticky="nsew", padx=1, pady=1)
        button7.grid(row=3, column=0, sticky="nsew", padx=1, pady=1)
        button8.grid(row=3, column=1, sticky="nsew", padx=1, pady=1)
        button9.grid(row=3, column=2, sticky="nsew", padx=1, pady=1)

        restartButton.grid(row=4, columnspan=3, sticky="nsew", padx=1, pady=1)

if __name__ == "__main__":
    main()

