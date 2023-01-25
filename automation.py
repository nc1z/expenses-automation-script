import pyautogui
import json
from pynput import keyboard
from pynput import mouse
from time import sleep
import pyperclip


class Automation:
    def __init__(self):
        self.entry_format = ['INPUT_YEAR', 'INPUT_MONTH', 'INPUT_DATE', 'INPUT_LINE_ITEM', 'INPUT_CATEGORY',
                             'INPUT_LINE_ITEM_TYPE', 'INPUT_PAYMENT_TYPE', 'INPUT_AMOUNT', 'INPUT_METHOD', 'INPUT_TIMEFRAME']
        self.x_copy, self.y_copy = None, None
        self.x_paste, self.y_paste = None, None
        self.listener = None
        self.line_items = []
        self.completion_count = 0
        self.line_spacing = 20  # calibrate this to fit your own use case

    def on_press(self, key):
        if key == keyboard.Key.esc:
            return False

    def on_click_copy(self, x_coord, y_coord, pressed):
        if pressed:
            self.x_copy, self.y_copy = x_coord, y_coord
            print(f'Click registered at {self.x_copy=}, {self.y_copy=}')
            self.listener.stop()

    def start_copy_script(self):
        text = "placeholder"

        print("Click to register starting coordinates for copy")
        with mouse.Listener(on_click=lambda x, y, b, p: self.on_click_copy(x, y, p)) as self.listener:
            self.listener.join()

        print("Click to register starting coordinates for paste")
        with mouse.Listener(on_click=lambda x, y, b, p: self.on_click_paste(x, y, p)) as self.listener:
            self.listener.join()

        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

        print("<<<<<<<<<<<<<<<<<<<<<<< COPY SCRIPT >>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("NOTE: Press ESC to stop the script at any point of time.")
        print("Starting COPY script...")
        sleep(1)

        while text:
            if not self.listener.running:
                print("Stopping script...")
                break
            pyautogui.tripleClick(self.x_copy, self.y_copy)
            pyautogui.hotkey('ctrl', 'c')
            newText = pyperclip.paste().replace("\r\n", "")

            if newText == text:
                break

            text = newText

            if len(text.split(" ")) > 5:
                self.line_items.append(text)
                print("ADDED: " + text)

            self.y_copy += self.line_spacing

        self.listener.stop()
