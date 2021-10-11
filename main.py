"""
main.py
    Main method for the pomodoro.
    This is a simple pomodoro clock that increase the effectiveness and efficiency of the workflow.
    The concept is simple:
        - Work in 25 minutes, then break in 5 minutes. This is called a rep
        - For every 4th rep: break in 30 minutes instead.
    The clock will tell you what to do and for how long you will do it.
"""

from gui import PomodoroGUI


def main():
    gui = PomodoroGUI()
    gui.create_gui()


main()
