from os import path
from subprocess import run, DEVNULL
from main import MediaHandler
from pynput.keyboard import Key, KeyCode, Listener

PATH = path.dirname(path.abspath(__file__))

run(f"cd {PATH} && git pull")
run(f"cp {PATH}/media.handler.desktop ~/.config/autostart/", shell=True)

mh = MediaHandler()


def on_press(key):
    if key == KeyCode(char="\\"):
        mh.get_link()

    if key == Key.ctrl_r:
        mh.play()


with Listener(on_press=on_press) as listener:
    listener.join()
