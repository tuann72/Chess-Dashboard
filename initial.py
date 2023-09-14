import customtkinter as ctk


class UsernameEntry(ctk.CTkFrame):
    def __init__(self, parent, get_username_func):
        super().__init__(master=parent)

        # data
        self.username = ctk.StringVar()
        self.get_username_func = get_username_func

        # layout
        self.grid(column=0, row=0, columnspan=2, rowspan=2, sticky="nsew")

        self.entry = ctk.CTkEntry(
            self, textvariable=self.username, placeholder_text="Username", width=170
        ).place(relx=0.5, rely=0.5, anchor="center")
        self.btn = ctk.CTkButton(self, text="Search", command=self.submit).place(
            relx=0.5, rely=0.55, anchor="center"
        )

    def submit(self):
        self.get_username_func(self.username.get())
