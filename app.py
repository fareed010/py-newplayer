class PrintColor:
    red_color = "\033[91m {}\033[00m"
    green_color = "\033[92m {}\033[00m"

    def __init__(self, text):
        self.text = text

    def print_red(self):
        print(self.red_color.format(self.text))

    def print_green(self):
        print(self.green_color.format(self.text))

prnt = PrintColor("Text to be printed")

prnt.print_green()
prnt.print_red()