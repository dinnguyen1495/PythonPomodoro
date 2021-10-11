"""
timer.py
    Pomodoro's timer
"""

# Pomodoro timer's rules
SESSION_TIME = 1500  # 25 minutes
SMALL_PAUSE = 300    # 5 minutes
BIG_PAUSE = 1800    # 30 minutes


class Timer:
    """
    Class for the timer
    """
    def __init__(self):
        self.start = False
        self.counter = 1
        self.timer = SESSION_TIME

    def show_timer(self) -> str:
        """
        Show time of the timer
        :return: time in countdown format
        """
        minutes = self.timer // 60
        seconds = self.timer % 60
        return '{:02d}:{:02d}'.format(minutes, seconds)

    def increase_counter(self):
        """
        Increase the timer by 1 second
        """
        self.counter += 1

    def set_timer(self) -> None:
        """
        Set time of next phase based on pomodoro's rules
        """
        if self.counter % 2 == 1:
            self.timer = SESSION_TIME
        elif self.counter % 8 == 0:
            self.timer = BIG_PAUSE
        else:
            self.timer = SMALL_PAUSE

    def countdown_timer(self) -> None:
        """
        Countdown function of the timer
        """
        if not self.start:
            return
        if self.timer > 0:
            self.timer -= 1
        else:
            self.increase_counter()
            self.set_timer()
            self.start = False

    def set_start(self) -> None:
        """
        Start the timer
        """
        self.start = True

    def set_stop(self) -> None:
        """
        Stop the timer
        """
        self.start = False

    def is_started(self) -> bool:
        """
        Check state of the timer
        :return: boolean value, shows if timer is on or not
        """
        return self.start

    def reset_timer(self) -> None:
        """
        Reset the timer
        """
        self.counter = 1
        self.timer = SESSION_TIME

    def show_reps(self) -> int:
        """
        Return time in the counter
        :return: time in second
        """
        return self.counter

    def show_timer_stage(self) -> str:
        """
        Show the action for each phase of the timer
        :return: text that indicates what to do in current phase
        """
        if self.counter % 2 == 1:
            return "Let\'s work!"
        else:
            return "Take a break!"

    def increase_timer(self, seconds: int) -> None:
        """
        Increase time in the timer by a certain amount
        :param seconds: increased amount of time in second
        """
        self.timer += seconds
