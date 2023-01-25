import pyautogui
import json
from pynput import keyboard
from pynput import mouse
from time import sleep
import pyperclip
from category_classifier import CategoryClassifier


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

    def on_click_paste(self, x_coord, y_coord, pressed):
        if pressed:
            self.x_paste, self.y_paste = x_coord, y_coord
            print(f'Click registered at {self.x_paste=}, {self.y_paste=}')
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

    def start_paste_script(self):
        if (self.x_paste and self.y_paste):
            self.register_position_and_run(self.x_paste, self.y_paste)

    def register_position_and_run(self, x, y):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        print("<<<<<<<<<<<<<<<<<<<<<<< PASTE SCRIPT >>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("NOTE: Press ESC to stop the script at any point of time.")
        print("Starting PASTE script...")

        pyautogui.leftClick(x, y, 2)
        for line in self.line_items:
            if not listener.running:
                print("Stopping script...")
                break
            self.write_entry(line)
            self.completion_count += 1

        listener.stop()
        self.write_completion_log()

    def write_entry(self, line):
        classifier = CategoryClassifier()
        line = line.split(" ")
        expense = " ".join(line[2:-1])
        category = classifier.classify(expense)
        for e in self.entry_format:
            match e:
                case "INPUT_YEAR":
                    pyautogui.write("2023")
                    pyautogui.press('Tab')
                case "INPUT_MONTH":
                    pyautogui.write(line[1])
                    pyautogui.press('Tab')
                case "INPUT_DATE":
                    date = line[0] + " " + line[1].lower()
                    pyautogui.write(date)
                    pyautogui.press('Tab')
                case "INPUT_LINE_ITEM":
                    pyautogui.write(" ".join(line[2:-1]))
                    pyautogui.press('Tab')
                case "INPUT_CATEGORY":
                    with open('keywords_food.json', 'r') as f:
                        keywords = json.load(f)
                    res = any(k in expense for k in keywords)
                    if res:
                        pyautogui.write("Food")
                    else:
                        pyautogui.write(category)
                    pyautogui.press('Tab')
                case "INPUT_LINE_ITEM_TYPE":
                    if "(" in line[-1]:
                        pyautogui.write("Credit")
                    else:
                        pyautogui.write("Debit")
                    pyautogui.press('Tab')
                case "INPUT_PAYMENT_TYPE":
                    if category == "Bill":
                        pyautogui.write("Recurring")
                    else:
                        pyautogui.write("Single")
                    pyautogui.press('Tab')
                case "INPUT_AMOUNT":
                    if "(" in line[-1]:
                        pyautogui.write(line[-1].replace("()", ""))
                    else:
                        pyautogui.write(line[-1])
                    pyautogui.press('Tab')
                case "INPUT_METHOD":
                    pyautogui.write("CITI")
                    pyautogui.press('Tab')
                case "INPUT_TIMEFRAME":
                    pyautogui.write("One-Time")
                    pyautogui.press('Tab')
                case _:
                    break
        pyautogui.press('Enter')
        pyautogui.press('Enter')
        pyautogui.press('home')

    def write_completion_log(self):
        print("<<<<<<<<<<<<<<<<<<<<<<< COMPLETE >>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(
            f"Script executed successfully. {self.completion_count} items processed")
