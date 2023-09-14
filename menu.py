import customtkinter as ctk
from figures import BarFigure, PIFigure


class MultiMenu(ctk.CTkTabview):
    def __init__(self, parent, username, data_func):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky="nsew")

        self.add("Bullet")
        self.add("Blitz")
        self.add("Rapid")
        self.add("Classical")

        BulletFrame(self.tab("Bullet"), data_func(username, "bullet"))
        BlitzFrame(self.tab("Blitz"), data_func(username, "blitz"))
        RapidFrame(self.tab("Rapid"), data_func(username, "rapid"))
        ClassicalFrame(self.tab("Classical"), data_func(username, "classical"))


class SideMenu(ctk.CTkFrame):
    def __init__(self, parent, data):
        super().__init__(master=parent, fg_color="transparent")
        self.grid(row=0, column=1, sticky="nsew")
        PIFigure(self, data)


class BulletFrame(ctk.CTkFrame):
    def __init__(self, parent, data):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=True, fill="both")
        BarFigure(self, "Bullet", data)


class BlitzFrame(ctk.CTkFrame):
    def __init__(self, parent, data):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=True, fill="both")
        BarFigure(self, "Blitz", data)


class RapidFrame(ctk.CTkFrame):
    def __init__(self, parent, data):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=True, fill="both")
        BarFigure(self, "Rapid", data)


class ClassicalFrame(ctk.CTkFrame):
    def __init__(self, parent, data):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=True, fill="both")
        BarFigure(self, "Classical", data)
