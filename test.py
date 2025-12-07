# محمد احمد صالح محمد طه
# سكشن 4

from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Sign Up")
win.geometry("350x420")
win.config(bg="#eef2f5")

Label(win, text="Create Account", font=("Calibri", 20, "bold"), bg="#eef2f5").pack(pady=20)

f = Frame(win, bg="#eef2f5")
f.pack()

def add_field(text, show=None):
    Label(f, text=text, font=("Calibri", 12), bg="#eef2f5").pack(anchor="w")
    e = Entry(f, font=("Calibri", 12), width=28, show=show)
    e.pack(pady=5)
    return e

name = add_field("Full Name:")
mail = add_field("Email:")
pw = add_field("Password:", show="•")
cpw = add_field("Confirm Password:", show="•")

def register():
    if not name.get() or not mail.get() or not pw.get() or not cpw.get():
        return messagebox.showerror("Error", "All fields are required.")
    if pw.get() != cpw.get():
        return messagebox.showerror("Error", "Passwords do not match.")
    messagebox.showinfo("Success", f"Account created for {name.get()}")

Button(win, text="Register", width=15, font=("Calibri", 13, "bold"),
    bg="#4a84d8", fg="white", command=register).pack(pady=25)

win.mainloop()

