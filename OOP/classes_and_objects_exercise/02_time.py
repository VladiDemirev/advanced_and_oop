class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        # if self.hours < 10:
        #   self.hours = f"0{self.hours}"
        # if self.minutes < 10:
        #   self.minutes = f"0{self.minutes}"
        # if self.seconds < 10:
        #   self.seconds = f"0{self.seconds}"
        # return f"{self.hours}:{self.minutes}:{self.seconds}"
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def update_valid_time(self) -> None:
        if self.seconds > Time.max_seconds:
            self.seconds = 00
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 00
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 00

    def next_second(self) -> str:
        self.seconds += 1
        self.update_valid_time()
        # if self.seconds > Time.max_seconds:
        # self.seconds = 00
        # self.minutes += 1
        # if self.minutes > Time.max_minutes:
        #   self.minutes = 00
        #   self.hours += 1
        #   if self.hours > Time.max_hours:
        #     self.hours = 00

        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())
