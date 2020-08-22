from datetime import datetime, date
from colorama import Fore
import os


def get_time():
    now = datetime.now()
    current_time = now.strftime("%H hours %M minutes")
    return current_time


def get_hours():
    now = datetime.now()
    return now.strftime("%H")


def get_date():
    return str(date.today())


def welcome_msg():
    return "At Your Service MR AKASH. How May I Help You"


def opening():
    os.system("aida.bat")
