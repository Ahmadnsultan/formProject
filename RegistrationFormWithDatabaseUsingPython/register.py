from tkinter import*
from tkinter import ttk, messagebox
from PIL import ImageTk   # pip3 install pillow
import pyttsx3 # pip install pyttsx3

class Register:
    def __init__(self, root,):
        self.root = root
        self.root.title("Registration Page")  # For Title of the page
        self.root.geometry("1350x700+0+0")    # Resolution of the page , top, bottom
        self.root.config(bg="white")

        # text-to-speech
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        # ===BackGround Image===
        self.bg = ImageTk.PhotoImage(file="images/back.png")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # ===Side Image===
        self.left = ImageTk.PhotoImage(file="images/side.jpg")
        left = Label(self.root, image=self.left).place(x=250, y=250, width=230, height=230)

        # ===Register Frame===
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=35, width=600, height=550)

        # ====Footer Frame=====
        footer = Frame(self.root, bg="gray")
        footer.place(x=0, y=650, relwidth=1, relheight=30)

        footer_name = Label(footer, text="Created & Developed By Ahmad Nabi Sultan",
                            font=("comic sans ms", 25, "bold"), bg="gray", fg="#ECF0F1").place(x=700, y=12)


        title = Label(frame1, text="Register Here", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=270, y=30)

        # --------First Row
        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=220, y=100, width=250)

        # --------Second Raw
        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=140)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=220, y=140, width=250)

        # --------3rd Raw
        user_name = Label(frame1, text="User Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=180)
        self.txt_username = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_username.place(x=220, y=180, width=250)

        # -------Contact
        contact = Label(frame1, text="Contact No ", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=220)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=220, y=220, width=250)

        # -------Email
        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=260)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=220, y=260, width=250)

        # -------Age
        age = Label(frame1, text="Age", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=300)
        self.txt_age = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_age.place(x=220, y=300, width=250)

        # -------Gender
        gender = Label(frame1, text="Gender", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=340)
        self.cmb_gender = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_gender['values']=("Select", "Male", "Female", "Other")
        self.cmb_gender.place(x=220, y=340, width=250)
        self.cmb_gender.current(0)

        # ---------Password
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=380)
        self.txt_password = Entry(frame1, show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=220, y=380, width=250)

        # --------Confirm Password
        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=420)
        self.txt_cpassword = Entry(frame1, show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=220, y=420, width=250)


        # --------Terms
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I Agree the Terms & Conditions ", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font=("times new roman", 12)).place(x=50, y=460)

        # Register Button with Image
        self.btn_img = ImageTk.PhotoImage(file="images/register.jpg")
        btn_register = Button(frame1, image=self.btn_img, bd=0, cursor="hand2", command=self.register_data).place(x=50, y=490)

        # -------Sign in Button-----
        btn_login = Button(self.root, text="Sign In", command=self.login_window, font=("times new roman", 20), bd=0, cursor="hand2").place(x=320, y=480)
        self.engine.say('Welcome to the registration form')
        self.engine.runAndWait()

    def login_window(self):
        self.root.destroy()
        import login


    def clear_data(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0, END)
        self.txt_username.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_age.delete(0, END)
        self.cmb_gender.current(0)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0,END)


    def register_data(self):

        if self.txt_fname.get() == "" or self.txt_fname.get() == "1234":
            self.engine.say('Please enter your valid first name')
            self.engine.runAndWait()
            messagebox.showerror("Error !","Please enter last name", parent=self.root)
        elif self.txt_lname.get() == "" or self.txt_lname.get() == "1234":
            self.engine.say('Please enter your valid last name')
            self.engine.runAndWait()
            messagebox.showerror("Error !","Please enter your second name", parent=self.root)
        elif self.txt_username.get() == "" or self.txt_username == "1234":
            self.engine.say('Please enter your valid username')
            self.engine.runAndWait()
            messagebox.showerror("Error !","Please enter valid username", parent=self.root)
        elif self.txt_contact.get() == "" or self.txt_contact.get() == "qwer":
            self.engine.say('Please enter your valid contact number')
            self.engine.runAndWait()
            messagebox.showerror("Error !", "Please enter your valid contact", parent=self.root)
        elif self.txt_email.get() == "" or self.txt_email.get() == "qwer":
            self.engine.say('Please enter your valid email')
            self.engine.runAndWait()
            messagebox.showerror("Error !", "Please enter your valid email", parent=self.root)
        elif self.txt_age.get() == "" or self.txt_age.get() == "qwer":
            self.engine.say('Please enter your valid age')
            self.engine.runAndWait()
            messagebox.showerror("Error !", "Please enter your valid age", parent=self.root)
        elif self.cmb_gender.get() == "select":
            self.engine.say('Please select your Gender')
            self.engine.runAndWait()
            messagebox.showerror("Error !", "Please enter select your Gender", parent=self.root)
        elif self.txt_password.get() == "":
            self.engine.say('Please enter your password')
            self.engine.runAndWait()
            messagebox.showerror("Error !","Please enter password", parent=self.root)
        elif self.txt_cpassword.get() == "":
            self.engine.say('Please confirm your password')
            self.engine.runAndWait()
            messagebox.showerror("Error !","Please confirm your password", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            self.engine.say('your password did not match')
            self.engine.runAndWait()
            messagebox.showerror("Error !", "Password Didn't Match !", parent=self.root)
        elif self.var_chk.get() == 0:
            self.engine.say('Please agree to our terms and conditions')
            self.engine.runAndWait()
            messagebox.showerror("Error !", "Please Agree to our Terms & Conditions", parent=self.root)
        else:
            self.engine.say("thanks for filling the registration form")
            self.engine.runAndWait()
            self.clear_data()


root = Tk()
obj = Register(root)
root.mainloop()