from tkinter import *
from buttons import buttons
import settings
import utils


root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

section1 = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_percent(25)
)
section1.place(x=0, y=0)

game_title = Label(
    section1,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)

game_title.place(
    x=utils.width_percent(25), y=0
)

section2 = Frame(
    root,
    bg='black',
    width=utils.width_percent(25),
    height=utils.height_percent(75)
)
section2.place(x=0, y=utils.height_percent(25))

section3 = Frame(
    root,
    bg='black',
    width=utils.width_percent(75),
    height=utils.height_percent(75)
)
section3.place(
    x=utils.width_percent(25),
    y=utils.height_percent(25),
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = buttons(x, y)
        c.create_btn_object(section3)
        c.btn_object.grid(
            column=x, row=y
        )
# Call the label from the Cell class
buttons.create_button_count_label(section2)
buttons.buttons_count_label_object.place(
    x=0, y=0
)

buttons.randomize_buttons()


# Run the window
root.mainloop()
