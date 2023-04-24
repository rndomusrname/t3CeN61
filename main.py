from os import popen
from time import sleep
from subprocess import run
from pynput.mouse import Button, Controller as mse_controller
from pynput.keyboard import KeyCode, Controller as kbd_controller


class MediaHandler:
    def __init__(self):
        self.links = []
        self.mse = mse_controller()
        self.kbd = kbd_controller()

    def get_link(self):
        self.mse.click(Button.right, 1)
        sleep(0.7)
        self.kbd.press(KeyCode(char="e"))
        self.kbd.release(KeyCode(char="e"))

        clipboard = popen("xclip -o").read().strip()
        if clipboard.find("&list=") != -1 or clipboard.find("&pp=") != -1:
            clipboard = clipboard[:43]
        if clipboard not in self.links and clipboard.startswith("http"):
            self.links.append(clipboard)

    def play(self):
        run(
            f"mpv {' '.join(link for link in self.links)} > /dev/null 2>&1 &",
            shell=True,
        )
        self.links.clear()
