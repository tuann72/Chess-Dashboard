import requests
import pprint
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

from settings import *

import customtkinter as ctk
from initial import *
from menu import MultiMenu, SideMenu


class App(ctk.CTk):
    def __init__(self):
        # Setup
        super().__init__()
        ctk.set_appearance_mode("Dark")
        self.geometry("1200x800")
        self.title("Chess Dashboard")
        self.minsize(800, 500)

        # layout
        self.rowconfigure(0, weight=1, uniform="a")
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=5)

        # Widgets
        self.front_entry = UsernameEntry(self, self.initialize)

        # Run
        self.mainloop()

    def initialize(self, username):
        self.username = username
        self.wins = 0
        self.draws = 0
        self.loss = 0

        self.find_player_monthly_games(self.username)
        self.front_entry.grid_forget()
        self.multimenu = MultiMenu(
            self, self.username, self.find_player_monthly_mode_stat
        )
        self.sidemenu = SideMenu(self, [self.wins, self.draws, self.loss])

    def find_player_monthly_games(self, username):
        self.username = username
        self.printer = pprint.PrettyPrinter()

        today_date = datetime.now().date()

        today_date_str = today_date.strftime("%Y-%m-%d")

        this_month = today_date_str.split("-")

        month = this_month[1]

        response = requests.get(
            f"{BASE_URL}{self.username}/games/2023/{month}", headers=HEADER
        ).json()

        for i in range(len(response["games"])):
            player1 = response["games"][i]["white"]["username"]
            white_result = response["games"][i]["white"]["result"]

            if not (
                (
                    player1 == username
                    and (
                        white_result == "resigned"
                        or white_result == "timeout"
                        or white_result == "abandoned"
                    )
                )
                or (player1 != username and white_result == "win")
                or (
                    white_result == "insufficient"
                    or white_result == "stalemate"
                    or white_result == "agreed"
                )
            ):
                self.wins += 1

            if (
                white_result == "statemate"
                or white_result == "agreed"
                or white_result == "insufficient"
            ):
                self.draws += 1

        self.loss = abs((self.wins + self.draws) - len(response["games"]))

    def find_player_monthly_mode_stat(self, username, mode):
        mode_wins = 0
        mode_draws = 0
        mode_loss = 0
        mode_counter = 0

        self.username = username

        today_date = datetime.now().date()

        today_date_str = today_date.strftime("%Y-%m-%d")

        this_month = today_date_str.split("-")

        month = this_month[1]

        response = requests.get(
            f"{BASE_URL}{self.username}/games/2023/{month}", headers=HEADER
        ).json()

        for i in range(len(response["games"])):
            time_control = response["games"][i]["time_class"]
            if time_control == mode:
                mode_counter += 1
                player1 = response["games"][i]["white"]["username"]
                white_result = response["games"][i]["white"]["result"]
                if not (
                    (
                        player1 == self.username
                        and (
                            white_result == "resigned"
                            or white_result == "timeout"
                            or white_result == "abandoned"
                        )
                    )
                    or (player1 != self.username and white_result == "win")
                    or (
                        white_result == "insufficient"
                        or white_result == "stalemate"
                        or white_result == "agreed"
                    )
                ):
                    mode_wins += 1

                if (
                    white_result == "statemate"
                    or white_result == "agreed"
                    or white_result == "insufficient"
                ):
                    mode_draws += 1

        mode_loss = abs((mode_wins + mode_draws) - mode_counter)
        data = [mode_wins, mode_draws, mode_loss]
        return data


App()
