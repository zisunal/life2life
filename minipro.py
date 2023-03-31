from tkinter import *

top = Tk()
top.title("Life2Life")

top.geometry("800x400")

# creating label
Fname = Label(top, text="First Name").place(x=30, y=50)
Lname = Label(top, text="Last Name").place(x=250, y=50)
dob = Label(top, text="DOB").place(x=30, y=90)
Address = Label(top, text="Address").place(x=30, y=130)
city = Label(top, text="City").place(x=30, y=170)
District = Label(top, text="District").place(x=250, y=170)
State = Label(top, text="State").place(x=490, y=170)
BloodGroup = Label(top, text="Blood Group").place(x=30, y=210)
Quantity = Label(top, text="Quantity").place(x=250, y=210)
email = Label(top, text="Email").place(x=30, y=250)
phoneno = Label(top, text="Phone Number").place(x=250, y=250)

sbmitbtn = Button(top, text="Submit", font=5, activebackground="#9898F5", activeforeground="blue").place(x=350, y=300)

e1 = Entry(top, width=20).place(x=105, y=50)

e2 = Entry(top, width=20).place(x=340, y=50)

e3 = Entry(top, width=20).place(x=105, y=90)
e4 = Entry(top, width=20).place(x=105, y=170)
e5 = Entry(top, width=20).place(x=105, y=210)
e6 = Entry(top, width=20).place(x=340, y=170)
e7 = Entry(top, width=20).place(x=545, y=170)
e8 = Entry(top, width=20).place(x=340, y=210)
e9 = Entry(top, width=20).place(x=105, y=250)
e10 = Entry(top, width=20).place(x=340, y=250)

menu = Menu(top)
top.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=top.quit)
menu.add_cascade(label='Home')

# Dropdown menu options
options = [
    "Male",
    "Female",
    "Other"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Gender")

# Create Dropdown menu
drop = OptionMenu(top, clicked, *options)
drop.place(x=250, y=85)
p1 = PhotoImage(file='bd.png')
top.iconphoto(False, p1)
top.mainloop()
