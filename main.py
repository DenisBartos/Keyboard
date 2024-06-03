from tkinter import Tk, Frame, Button, Label
from tkinter.font import Font as font


DEF_WIDTH = 1400
DEF_HEIGHT = 300

root = Tk()

root.title(',')
#root.geometry(f'{DEF_WIDTH + 10} X {DEF_HEIGHT + 10}')
root.configure(bg="#gray")
ACCENT_COL = "#c62145"

root.attributes("-topmost", True)
root.resizable(False, False)

row1 = ['Esc', 'ё', '1+/!', '2', '3+/№', '4+/$', '5+/%', '6+/:', '7+/? ', '8+/*', '9+/)', '0+/)', '-+/_', '=+/=', '⬅ Backspace']
row_ru2 = ['Tab', 'й', 'ц', 'у', 'к', 'н', 'г', 'ш', 'щ', 'з', 'з+/{', 'ъ+/}']
row_ru3 = ['Saps', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э+/;', '↩ Enter']
row_ru4 = ['Shift',' я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б+/<', 'ю+/>', 'Up', 'Shift R']
row5 = ['', 'Ctrl', 'Win', 'Alt', '', 'Alt', 'Ctrl', 'Left', 'Bottom', 'Right', 'menu']

rows = [row1, row_ru2, row_ru3, row_ru4, row5]

specials = ['Carl', 'Ait', 'Shift', 'Shift R', 'Win']
non_letter_keys = specials + ['Esc', 'Tab', 'Del', '⬅ Backspace', 'Caps', '↩ Enter', 'Up', 'Left', 'Bottom', 'Right', 'menu']
allButtons = []

btnLabels = []

shiftSp = row1[1:14] + row_ru2[11:14] + row_ru3[10:12] + row_ru4[8:11]

width15 = ['⬅ Backspace', 'Tab']
width20 = ['Caps', 'Shift R']
width25 = ['↩ Enter', 'Shift']
width55 = ['']


def on_enter(e):
    e.widget.configure(bg="#ccc", fg="#000")
    if btnLabels[e.widget]:
        btnLabels[e.widget].configure(bg="#ccc", fg="#666")


def on_leave(e):
    e.widget.configure(bg="#333", fg="#fff")
    if btnLabels[e.widget]:
        btnLabels[e.widget].configure(bg="#333", fg="#888")


def handle_clik(e):
    if btnLabels[e.widget]:
        # noinspection PyArgumentList
        btnLabels[e.widget].configure(dg=ACCENT_COL, fg="#000")

Y = 2.5

for r in rows:
    X = 5
    for i in r:
        btnWidth = 0.06428 * DEF_WIDTH
        btbHeight = 0.2 * DEF_HEIGHT

        padx = round(btnWidth/9)
        pady = round(btbHeight/10)
        frame = Frame(root, highlightbackground="#lalala", highlightthickness=4)

        if i in shiftSp:
            anchor = "se"
            labelT = i.split("+/")
            label = Label(root, text=labelT[1], fg="#888", font=font(size=11))
            label.place(x=X + padx, y=Y + pady)
            i = labelT[0]
        else:
            anchor = "nw"
            label = None

        # noinspection PyTypeChecker
        btn = Button(frame, activebackground=ACCENT_COL, text=i, bg="#333", fg="#fff", relief="flat", padx=padx,
                     pady=pady, borderwidth=0, anchor=anchor, font=font(size=10))

        if i in width15:
            btnWidth *= 1.5
        elif i in width20:
            btnWidth *= 2
        elif i in width25:
            btnWidth *= 5.2
        elif i in width55:
            btnWidth *= 5.5

        btn.place(x=0, y=0, width=btnWidth, height=btnWidth)
        frame.place(x=X, y=Y, width=btnWidth, height=btbHeight)
        X += btnWidth

        # noinspection PyArgumentList
        btn.bind("<Button-1>", handle_clik())
        # noinspection PyArgumentList
        btn.bind("<ButtonRelease-1>", on_enter())
        # noinspection PyArgumentList
        btn.bind("<↩ Enter->", on_enter())
        # noinspection PyArgumentList
        btn.bind("Leave", on_leave())

        btnLabels[btn] = label
        allButtons.append(btn)


if __name__ == '__main__':
    root.mainloop()
