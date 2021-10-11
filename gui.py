"""
gui.py
    Visualized Pomodoro Timer and its function
"""

from typing import Any
from timer import Timer
from tkinter import Tk, Canvas, Label, Button, PhotoImage


# Custom color palettes
NAVY = '#2C2891'
GREY = '#39A388'
GREEN = '#1C7947'
YELLOW = '#FFF9B2'
WHITE = '#F3F0D7'


class PomodoroGUI:
    """
    Class for GUI of Pomodoro
    """
    def __init__(self):
        self.pomodoro = Timer()

    def run_timer(self, window: Tk, timer_canvas: Canvas, timer_text: Any, start_button: Button,
                  timer_label: Label, reps_counter: Label) -> None:
        """
        Run the pomodoro timer
        :param window:
            tkinter.Tk
        :param timer_canvas:
            tkinter.Canvas
        :param timer_text:
            tkinter.Label
        :param start_button:
            tkinter.Button
        :param timer_label:
            tkinter.Label
        :param reps_counter:
            tkinter.Label
        """
        if not self.pomodoro.is_started():
            return
        if timer_label['text'] == "Pomodoro":
            timer_label.config(text="Let\'s work!")
        self.pomodoro.countdown_timer()
        timer_canvas.itemconfig(timer_text, text=self.pomodoro.show_timer())
        if self.pomodoro.is_started():
            window.after(1000,
                         self.run_timer,
                         window,
                         timer_canvas,
                         timer_text,
                         start_button,
                         timer_label,
                         reps_counter)
            return
        start_button.config(text='Start')
        if self.pomodoro.show_reps() > 1 and self.pomodoro.show_reps() % 2 == 1:
            reps_counter.config(text=f'Reps completed: {self.pomodoro.show_reps() // 2}')
        timer_label.config(text=self.pomodoro.show_timer_stage())

    def create_gui(self) -> None:
        """
        Create the GUI of Pomodoro
        """
        def reset_timer() -> None:
            """
            Reset pomodoro timer to the very beginning
            """
            self.pomodoro.set_stop()
            timer_label.config(text='Pomodoro')
            self.pomodoro.reset_timer()
            timer_canvas.itemconfig(timer_text, text=self.pomodoro.show_timer())
            reps_counter.config(text='Reps completed: 0')
            start_button.config(text='Start')

        def start_timer() -> None:
            """
            Start/Stop the pomodoro timer based on its state
            """
            if self.pomodoro.is_started():
                self.pomodoro.set_stop()
                start_button.config(text='Start')
            else:
                self.pomodoro.set_start()
                start_button.config(text='Pause')
                self.pomodoro.increase_timer(1)
                self.run_timer(window, timer_canvas, timer_text, start_button, timer_label, reps_counter)

        window = Tk()
        window.title('Pomodoro Timer')
        window.config(padx=50, pady=50, bg=YELLOW)

        timer_label = Label(window, text='Pomodoro', fg=NAVY, bg=YELLOW, font=('Calibri', 30, 'bold'))
        timer_label.grid(row=0, column=1, padx=5, pady=5, sticky='nesw')

        pomodoro_img = PhotoImage(file="img/tomato.png")

        timer_canvas = Canvas(window, width=230, height=205, bg=YELLOW, highlightthickness=0)
        timer_canvas.create_image(115, 102, image=pomodoro_img)
        timer_text = timer_canvas.create_text(115, 115, text=self.pomodoro.show_timer(), fill=WHITE,
                                              font=("Tahoma", 35, 'bold'))
        timer_canvas.grid(row=1, column=1, padx=5, pady=5)

        start_button = Button(window, text='Start', width=10, command=start_timer)
        start_button.grid(row=3, column=0, padx=5, pady=5)

        reps_counter = Label(window, text='Reps completed: 0', fg=GREEN, bg=YELLOW, font=("Arial", 16))
        reps_counter.grid(row=2, column=1, padx=5, pady=5)

        reset_button = Button(window, text='Reset', width=10, command=reset_timer)
        reset_button.grid(row=3, column=2, padx=5, pady=5)

        window.mainloop()
