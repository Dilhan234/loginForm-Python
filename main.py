import tkinter as tk
from tkinter import messagebox

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")

        # Variables to store the entered username and password
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Create labels, entry widgets, and buttons
        self.label_username = tk.Label(root, text="Username:")
        self.entry_username = tk.Entry(root, textvariable=self.username_var)

        self.label_password = tk.Label(root, text="Password:")
        self.entry_password = tk.Entry(root, textvariable=self.password_var, show="*")

        self.button_login = tk.Button(root, text="Login", command=self.login)

        # Grid layout
        self.label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        self.label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.button_login.grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        # Retrieve entered username and password
        entered_username = self.username_var.get()
        entered_password = self.password_var.get()

        # Replace this dictionary with a secure database in a real-world scenario
        user_credentials = {"user1": "password1", "user2": "password2"}

        # Check if the entered username exists and the password matches
        if entered_username in user_credentials and user_credentials[entered_username] == entered_password:
            messagebox.showinfo("Login Successful", "Welcome, {}".format(entered_username))
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main application window
root = tk.Tk()

# Instantiate the LoginForm class
login_form = LoginForm(root)

# Run the Tkinter event loop
root.mainloop()

