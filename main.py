from datetime import timedelta

from pynput import keyboard

from timer import Timer

global running, i, markers

START_STOP = [
    {keyboard.Key.f9}
]

ELAPSED = [
    {keyboard.Key.f8}
]

current = set()
t = Timer()
running = False
i = 0
markers = []


def start():
    global running, startlol
    print("start")
    startlol = t.start().strftime('%Y-%m-%d %H-%M-%S.txt')
    print(startlol + " wurde eben erstellt.")
    running = True


def stop():
    global running, markers, startlol
    print("stop")
    t.stop()
    running = False
    with open(f"D:/Eigene Dateien/Eigene Videos/OBS/{startlol}", "w") as f:
        for i in markers:
            f.write(i)
    t.reset()
    markers = []


def elepsed():
    global i, markers
    timestamp = t.elapsed()

    micro = timestamp.microseconds / 1000000 * 29
    micro = round(micro)

    marker = timestamp - timedelta(microseconds=timestamp.microseconds)
    marker = f"{marker};{micro}"
    print(marker)

    i += 1

    markers.append(f"{marker}    {i}\n")


def on_press(key):
    global running
    if any([key in START_STOP for START_STOP in START_STOP]):
        current.add(key)
        if not running:
            start()
        else:
            stop()

    if any([key in ELAPSED for ELAPSED in ELAPSED]):
        current.add(key)
        if running:
            elepsed()
        else:
            pass


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()