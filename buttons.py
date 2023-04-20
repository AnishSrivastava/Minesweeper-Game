from tkinter import Button, Label
import random
import settings
import ctypes
import sys

class buttons:
    all = []
    buttons_count = settings.CELL_COUNT
    buttons_count_label_object = None
    def __init__(self,x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_clicked = False
        self.is_mine_candidate = False
        self.btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        buttons.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind('<Button-1>', self.left_click) # Left Click
        btn.bind('<Button-3>', self.right_click) # Right Click
        self.btn_object = btn

    @staticmethod
    def create_button_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left:{buttons.buttons_count}",
            font=("", 30)
        )
        buttons.buttons_count_label_object = lbl

    def left_click(self, event):
        if self.is_mine:
            self.clicked_on_mine()
        else:
            if self.surrounding_mines_num == 0:
                for cell_obj in self.surrounded_buttons:
                    cell_obj.show_button()
            self.show_button()
            # If Mines count is equal to the cells left count, player won
            if buttons.buttons_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the game!', 'Game Over', 0)

        # Cancel Left and Right click events if cell is already opened:
        self.btn_object.unbind('<Button-1>')
        self.btn_object.unbind('<Button-3>')

    def button_axis(self, x, y):
        # Return a cell object based on the value of x,y
        for cell in buttons.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_buttons(self):
        cells = [
            self.button_axis(self.x - 1, self.y - 1),
            self.button_axis(self.x - 1, self.y),
            self.button_axis(self.x - 1, self.y + 1),
            self.button_axis(self.x, self.y - 1),
            self.button_axis(self.x + 1, self.y - 1),
            self.button_axis(self.x + 1, self.y),
            self.button_axis(self.x + 1, self.y + 1),
            self.button_axis(self.x, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounding_mines_num(self):
        counter = 0
        for cell in self.surrounded_buttons:
            if cell.is_mine:
                counter += 1

        return counter

    def show_button(self):
        if not self.is_clicked:
            buttons.buttons_count -= 1
            self.btn_object.configure(text=self.surrounding_mines_num)
            # Replace the text of cell count label with the newer count
            if buttons.buttons_count_label_object:
                buttons.buttons_count_label_object.configure(
                    text=f"Cells Left:{buttons.buttons_count}"
                )
            # If this was a mine candidate, then for safety, we should
            # configure the background color to SystemButtonFace
            self.btn_object.configure(
                bg='lime'
            )

        # Mark the cell as opened (Use is as the last line of this method)
        self.is_clicked = True

    def clicked_on_mine(self):
        self.btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        sys.exit()


    def right_click(self, event):
        if not self.is_mine_candidate:
            self.btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_buttons():
        picked_buttons = random.sample(
            buttons.all, settings.MINES_COUNT
        )
        for picked_cell in picked_buttons:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"