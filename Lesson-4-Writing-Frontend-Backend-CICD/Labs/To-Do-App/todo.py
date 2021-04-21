# tkinter allows you to create GUI apps with Python
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
# Push down the GUI screen a little bit
frame.pack(pady=10)

# What the box for the to-do app looks like
list1 = Listbox(frame,
                width=40,
                height=10,
                # Background border
                bg="SystemButtonFace",
                # Borderline
                bd=0,
                # Font color
                fg="#464646")

# Pack into under the screen
list1.pack(side=LEFT, fill=BOTH)

# Make a list of stuff to do
my_stuff = ["Dog", "pick up son from daycare", "deep work"]

# Save it to the list
for item in my_stuff:
    list1.insert(END, item)


# Scrollabar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=BOTH)

# Add scrollbar to list config
list1.config(yscrollcommand=scrollbar.set)

# Configure scrollbar
scrollbar.config(command=list1.yview)

# Create an entrybox
entry = Entry(app)
entry.pack(pady=20)

# Create a button frame
button_frame = Frame(app)
button_frame.pack(pady=20)

# Functions to delete, add, and cross of items on the list

def delete_item():
    list1.delete(ANCHOR)

def add_item():
    list1.insert(END, entry.get())
    entry.delete(0, END)


# Add buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1)

app.mainloop()
