import tkinter
import os
import random

FIELD_SIZE = 4

main_window = tkinter.Tk()
main_window.title('игра 15')

files_list = sorted(os.listdir('nums'))
print(files_list)

images_list = []
for file_name in files_list:
    full_path = os.path.join('nums', file_name)
    image = tkinter.PhotoImage(file=full_path)
    images_list.append(image)

labels_list = []
for row in range(FIELD_SIZE):
    buf = []
    for column in range(FIELD_SIZE):
        index = row * FIELD_SIZE + column
        label = tkinter.Label(main_window, image=images_list[index])
        label.index = index
        label.row = row
        label.column = column
        label.grid(row=row, column=column)
        buf.append(label)

    labels_list.append(buf)

current = labels_list[-1][-1]


def exchange_items(arg):
    arg.row, current.row = current.row, arg.row
    arg.column, current.column = current.column, arg.column
    labels_list[arg.row][arg.column], arg = arg, labels_list[arg.row][arg.column]


def render_item(arg):
    arg.grid(row=arg.row, column=arg.column)


def key_press(arg):
    near = None

    if arg == 'Up' and current.row > 0:
        near = labels_list[current.row - 1][current.column]
    elif arg == 'Down' and current.row < FIELD_SIZE - 1:
        near = labels_list[current.row + 1][current.column]
    elif arg == 'Left' and current.column > 0:
        near = labels_list[current.row][current.column - 1]
    elif arg == 'Right' and current.column < FIELD_SIZE - 1:
        near = labels_list[current.row][current.column + 1]

    if near:
        exchange_items(near)
        render_item(near)
        render_item(current)


def shuffle_game():
    actions = ['Up', 'Down', 'Left', 'Right']
    for _ in range(100):
        current_action = random.sample(actions, 1)[0]
        key_press(current_action)


main_window.after(2000, shuffle_game)
main_window.bind('<KeyPress>', lambda x: key_press(x.keysym))

main_window.mainloop()
