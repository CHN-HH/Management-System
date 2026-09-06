import tkinter as tk
from time import strftime
from datetime imp

root = tk.Tk()
root.title("Clock")
root.attributes("-topmost", True)
root.geometry("550x256")
root.resizable(False, False)
root.configure(bg="#0f0f0f")

time_label = tk.Label(
    root,
    font=("Segoe UI", 32, "bold"),
    bg="#0f0f0f",
    fg="#00ffcc"
)
time_label.pack(pady=10)

count_title = tk.Label(
    root,
    text="距离目标时间",
    font=("Segoe UI",16),
    bg="#0f0f0f",
    fg="#ffdd44"
)
count_title.pack()

count_label = tk.Label(
    root,
    font=("Segoe UI", 36, "bold"),
    bg="#0f0f0f",
    fg="#ff6666"
)
count_label.pack(pady=8)

TARGET_TIME = datetime(2026, 9, 28, 00, 00, 00)

def update_clock():

    now_text = strftime("%Y‑%m‑%d  %A\n%H:%M:%S")
    time_label.config(text=now_text)

    now = datetime.now()
    delta = TARGET_TIME - now

    if delta.total_seconds() <= 0:
        count_label.config(text="⏰ 时间已到！", fg="#ff2222")
    else:
        days = delta.days
        hours = delta.seconds // 3600
        mins = (delta.seconds % 3600) // 60
        secs = delta.seconds % 60
        count_text = f"{days}天 {hours:02d}:{mins:02d}:{secs:02d}"
        count_label.config(text=count_text)

    root.after(1000, update_clock)

update_clock()
root.mainloop()
