import tkinter as tk
from random import shuffle
class MyButton(tk.Button):
    def __init__(self, master, x, y, number, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font= 'Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
    def __repr__(self):
        return f'MyButton{self.x} {self.y} {self.number}, {self.is_mine}'


class MineSweeper:
    window=tk.Tk()
    ROW=5
    COLUMNS=3
    MINES=4
    def __init__(self):
        self.buttons = []
        count=1
        for i in range(MineSweeper.ROW):
            temp = []
            for j in range(MineSweeper.COLUMNS):
                btn = MyButton(MineSweeper.window, x=i, y=j, number=count)
                btn.config(command=lambda button = btn:self.click(button))
                temp.append(btn)
                count += 1
            self.buttons.append(temp)

    def click(self, clicked_button: MyButton):
        if clicked_button.is_mine:
            clicked_button.config(text="*", background='red', disabledforeground='black')
        else:
            clicked_button.config(text=clicked_button.number, disabledforeground='black')
        clicked_button.config(state='disabled')
    def create_widgets(self):
        for i in range(MineSweeper.ROW):
            for j in range(MineSweeper.COLUMNS):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.print_buttons()
        MineSweeper.window.mainloop()

    def print_buttons(self):
        for ROW_btn in self.buttons:
            print(ROW_btn)

    def insert_mines(self):
        index_mines=self.get_mines_places()
        print(index_mines)
        for ROW_btn in self.buttons:
            for btn in ROW_btn:
                if btn.number in index_mines:
                    btn.is_mine = True
    @staticmethod
    def get_mines_places():
        indexes = list(range(1, MineSweeper.COLUMNS * MineSweeper.ROW+1))
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]


game = MineSweeper()
game.start()


