from tkinter import *

root = Tk()
root.iconbitmap('')
root.geometry("1100x700")

frame1 = Frame(master=root, width = 1000, height=300)
frame1.grid(row = 0, column = 0, rowspan = 2, columnspan = 7)

logoImg = PhotoImage(file="logo.png")
logoresize=logoImg.subsample(6,6)
logo = Button(
    text="poop",
    bg="white",
    fg="black",
    master=frame1,
    anchor=CENTER,
    image=logoresize
)
logo.grid(row =0, column=0, padx=2)


journal = Button(
    text="Journal",
    bg="white",
    fg="black",
    width=15,
    height=10,
    master=frame1,
    anchor=CENTER
)
journal.grid(row =0, column=1, padx=2)

reflections = Button( 
    text="Reflections",
    bg="white",
    fg="black",
    width=15,
    height=10,
    master=frame1,
    anchor=CENTER

)
reflections.grid(row =0, column=2, padx=2)

moodtracker = Button(
    text="Mood Tracker",
    bg="white",
    fg="black",
    width=15,
    height=10,
    master=frame1,
    anchor=CENTER
)
moodtracker.grid(row =0, column=3, padx=2)

mealplanning  = Button( 
    text="Meal Planning",
    bg="white",
    fg="black",
    width=15,
    height=10,
    master=frame1,
    anchor=CENTER

)
mealplanning.grid(row =0, column=4, padx=2)

def login():
    global login_screen
    login_screen = Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    if username1 == "emma":
        if password1 in "emma1":
            login_screen.destroy()

        else:
            user_not_found()

    else:
        user_not_found()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=remove_user_mot_found).pack()

def remove_user_mot_found():
    user_not_found_screen.destroy()
    
loginsignup = Button( 
    text="Login",
    bg="white",
    fg="black",
    width=15,
    height=10,
    master=frame1,
    anchor=CENTER,
    command=login
)
loginsignup.grid(row =0, column=5, padx=2)

homepageImg = PhotoImage(file="homescrreen.png")
homepage = Label(master=frame1, image=homepageImg)
homepage.grid(row=1, column=0,columnspan=5)

root.mainloop()

