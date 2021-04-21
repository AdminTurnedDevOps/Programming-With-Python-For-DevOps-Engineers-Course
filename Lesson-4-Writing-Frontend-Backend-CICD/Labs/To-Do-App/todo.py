from tkinter import *
from tkinter.font import Font

app = Tk()

app.title('CloudSkills To-Do')
app.geometry("500x500")

# Font

font = Font(
    family="Brush Script MT",
    size=30,
    weight="bold"
)

frame = Frame(app)
frame.pack(pady=10)

list1 = Listbox(
    frame,
    width=40,
    height=10,
    bg="SystemButtonFace",
    bd=0,
    fg="#464646"
)

list1.pack(side=LEFT, fill=BOTH)

my_stuff = ["Pick up dog", "Pick up son from daycare", "deep work"]
for item in my_stuff:
    list1.insert(END, item)


scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=BOTH)

list1.config(yscrollcommand=scrollbar.set)

scrollbar.config(command=list1.yview)

entry = Entry(app)
entry.pack(pady=20)

button_frame = Frame(app)
button_frame.pack(pady=20)

def delete_item():
    list1.delete(ANCHOR)

def add_item():
    list1.insert(END, entry.get())
    entry.delete(0, END)

delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1)


app.mainloop()