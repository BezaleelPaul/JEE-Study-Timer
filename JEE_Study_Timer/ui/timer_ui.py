import tkinter as tk
from tkinter import ttk, messagebox
from logic.timer_logic import Timer
import datetime

class TimerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("JEE Study Timer")
        self.root.configure(bg="#2C2F33")
        self.timer = Timer(25 * 60, self.timer_finished)

        self.label = tk.Label(root, text="Select Subject", font=("Arial", 18, "bold"), bg="#2C2F33", fg="#FFFFFF")
        self.label.pack(pady=20)

        self.subject_var = tk.StringVar()
        self.subject_dropdown = ttk.Combobox(root, textvariable=self.subject_var, font=("Arial", 14))
        self.subject_dropdown['values'] = ["Physics", "Chemistry", "Math"]
        self.subject_dropdown.pack(pady=10)
        self.subject_dropdown.configure(state="readonly")

        self.timer_label = tk.Label(root, text="25:00", font=("Arial", 48, "bold"), bg="#2C2F33", fg="#43B581")
        self.timer_label.pack(pady=30)

        button_style = {'bg': '#7289DA', 'fg': '#FFFFFF', 'font': ('Arial', 14, 'bold')}

        self.start_button = tk.Button(root, text="Start Study", command=self.start_timer, **button_style)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Study", command=self.stop_timer, **button_style)
        self.stop_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset Study", command=self.reset_timer, **button_style)
        self.reset_button.pack(pady=5)

        self.log_button = tk.Button(root, text="Log Session", command=self.log_session, **button_style)
        self.log_button.pack(pady=5)

        self.footer_label = tk.Label(root, text="Stay Focused and Keep Learning!", bg="#2C2F33", fg="#FFFFFF", font=("Arial", 12))
        self.footer_label.pack(side=tk.BOTTOM, pady=20)

        self.update_timer()

    def start_timer(self):
        self.timer.start()

    def stop_timer(self):
        self.timer.stop()

    def reset_timer(self):
        self.timer.reset()
        self.timer_label.config(text="25:00")

    def update_timer(self):
        minutes, seconds = divmod(self.timer.time_left, 60)
        self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        self.root.after(1000, self.update_timer)

    def timer_finished(self):
        messagebox.showinfo("Session Complete", f"Time to take a break from {self.subject_var.get()}!")
        self.log_session()

    def log_session(self):
        subject = self.subject_var.get()
        if subject:
            with open('data/session_log.txt', 'a') as log_file:
                log_file.write(f"{datetime.datetime.now()}: Completed study session for {subject}\n")
            messagebox.showinfo("Session Logged", f"Session for {subject} has been logged.")
        else:
            messagebox.showwarning("No Subject Selected", "Please select a subject to log the session.")
