from ui.timer_ui import TimerUI
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("JEE Study Timer")
    root.geometry("800x600")
    TimerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
