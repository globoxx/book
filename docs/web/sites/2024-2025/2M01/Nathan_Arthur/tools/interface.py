import curses
import platform

class Interface():

    def __init__(self):
        self.screen = curses.initscr()
        curses.curs_set(0)
        curses.start_color()
        self.screen.clear()
        self.screen.refresh()
        self.screen.keypad(True)

    def showmenu(self, title, options, default_cursor_pos = 0):
        current_pos = default_cursor_pos
        max_pos = len(options) - 1

        while True:
            self.screen.clear()
            self.screen.addstr(title + "\n\n")

            for idx, choice in enumerate(options):
                if idx == current_pos:
                    self.screen.addstr(f"-> {choice}\n")
                else:
                    self.screen.addstr(f"   {choice}\n")

            self.screen.refresh()

            key = self.screen.getch()

            if key == curses.KEY_UP:
                if current_pos > 0:
                    current_pos -= 1
            elif key == curses.KEY_DOWN:
                if current_pos < max_pos:
                    current_pos += 1
            elif key == ord('\n'):
                break
        return current_pos
    
    def showaskbox(self, prompt):
        self.screen.clear()
        self.screen.addstr(prompt + "\n\n")
        self.screen.refresh()
        curses.echo()
        input_str = self.screen.getstr().decode('utf-8')
        curses.noecho()
        return input_str

    def printmsg(self, msg):
        self.screen.clear()
        self.screen.addstr(msg + "\n\nPress any key to continue.")
        self.screen.refresh()
        return self.screen.getch()

    def printerrmsg(self, errmsg):
        self.screen.clear()
        self.screen.addstr("ERROR: " + str(errmsg) + "\n\nPress any key to continue.")
        self.screen.refresh()
        self.screen.getch()