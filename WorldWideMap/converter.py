class Converter():
    def decimal_to_degrees(self, number, show_degrees=False):
        self.degrees = int(number)
        self.minutes = int((number - self.degrees) * 60)
        self.seconds = (number - self.degrees - self.minutes / 60) * 3600

        if show_degrees:
            return "{}° {}′ {}″".format(self.degrees, self.minutes, round(self.seconds, 2))
        else:
            self.seconds = round(self.seconds, 2)
            return self.degrees, self.minutes, self.seconds

    def degrees_to_decimal(self, degrees, minutes, seconds):
        self.decimal = degrees + minutes / 60 + seconds / 3600

        return self.decimal

    def metres_to_kilometres(self, metres):

        self.metres = metres
        self.kilometres = self.metres / 1000

        return self.kilometres

    def kilometres_to_metres(self, kilometres):

        self.kilometres = kilometres
        self.metres = self.kilometres * 1000

        return self.metres