# -*- coding: utf-8 -*-

"""
Copyright (c) 2018 hackbox developers (http://hackbox.io)
See the file 'LICENSE' for copying permission
"""

from utils import config


HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def banner():
    bar = "+------------------------------------+"
    print(bar)
    logo = "Hackbox v{}".format(config.VERSION)
    bar_size = len(bar)
    logo_size = len(logo)
    print("|{}{}{}|".format(
        " " * ((bar_size - logo_size) / 2 - 1),
        logo,
        " " * ((bar_size - logo_size) / 2 - 1))
    )
    print(bar)


def status(s):
    print("[{}*{}] {}".format(BLUE, END, s))


def success(s):
    print("[{}+{}] {}".format(GREEN, END, s))


def error(s):
    print("[{}-{}] {}".format(FAIL, END, s))


def warning(s):
    print("[{}!{}] {}".format(WARNING, END, s))


def line():
    print("+----------------------------+")


def running(s):
    print("[{}+{}] {} {}running{} ... [ {}OK{} ]".format(GREEN, END, s, BOLD, END, GREEN, END))


def ok(s):
    print("[{}+{}] {} ... [ {}{}OK{}{} ]".format(GREEN, END, s, BOLD, GREEN, END, END))
