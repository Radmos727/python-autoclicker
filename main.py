import tkinter as tk
from tkinter import ttk, simpledialog, messagebox 
import pyautogui
import threading
import keyboard
import sys


class autoclickerYippieeee:
    def __init__(self, master):
        self.master = master
        self.master.title("autocwicker :3")

        self.create_menu()

        self.master.resizable(False, False)

        
        icon_path = "./ico/michaelcera.ico"
        self.master.iconbitmap(icon_path)

        self.click_interval_label = ttk.Label(master, text="Clicks per Second:")
        self.click_interval_label.grid(row=1, column=0, padx=10, pady=10)

        self.click_interval_entry = ttk.Entry(master)
        self.click_interval_entry.grid(row=1, column=1, padx=10, pady=10)
        self.click_interval_entry.insert(0, "20")

        self.status_label = ttk.Label(master, text="Status: Stopped")
        self.status_label.grid(row=4, column=0, columnspan=2, pady=10)

        self.start_stop_button = ttk.Button(master, text=f"To start, press F8", command=self.toggle_autoclicker)
        self.start_stop_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.running = False
        self.current_keybind = "F8"

        keyboard.on_press_key(self.current_keybind, self.toggle_autoclicker)

    def create_menu(self):
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        self.options_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Options", menu=self.options_menu)

        self.options_menu.add_command(label="Change Keybind", command=self.change_binds)
        self.options_menu.add_command(label="Exit", command=self.exit_app)

    def change_binds(self):
        new_keybind = simpledialog.askstring("Hotkey Setting", "Enter a new hotkey:")
        if new_keybind:
            keyboard.unhook_all()
            self.current_keybind = new_keybind
            keyboard.on_press_key(self.current_keybind, self.toggle_autoclicker)
            messagebox.showinfo("Success", f"Keybind changed to {new_keybind}")
            self.start_stop_button["text"] = f"To start, press {self.current_keybind}"

    def exit_app(self):
        sys.exit()

    def toggle_autoclicker(self, event=None):
        if not self.running:
            try:
                clicks_per_second = float(self.click_interval_entry.get())
                interval = 1 / clicks_per_second
            except ValueError:
                tk.messagebox.showerror("Error", "Invalid input. Enter a valid number.")
                return

            self.running = True
            self.start_stop_button["text"] = f"To stop, press {self.current_keybind}"
            self.status_label["text"] = "Status: Running"
            self.autoclicker_thread = threading.Thread(target=self.autoclicker, args=(interval,))
            self.autoclicker_thread.start()
        else:
            self.running = False
            self.start_stop_button["text"] = f"To start, press {self.current_keybind}"
            self.status_label["text"] = "Status: Stopped"
            self.autoclicker_thread.join()

    def autoclicker(self, interval):
        pyautogui.PAUSE = interval 
        while self.running:
            pyautogui.click()

if __name__ == "__main__":
    root = tk.Tk()
    app = autoclickerYippieeee(root)
    root.mainloop()