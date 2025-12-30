import tkinter as tk
from tkinter import scrolledtext
import json
from datetime import datetime

root = tk.Tk()
root.title("Keylogger Project")
root.geometry("420x520")
root.configure(bg="#0f172a")  
key_list = []
logging_active = False


def log_key(event):
    if logging_active:
        data = {
            "key": event.keysym,
            "time": datetime.now().strftime("%H:%M:%S")
        }
        key_list.append(data)

        log_box.insert(tk.END, f"{data['time']}  →  {data['key']}\n")
        log_box.see(tk.END)

        with open("logs.json", "w") as f:
            json.dump(key_list, f, indent=4)

def start_logger():
    global logging_active
    logging_active = True
    status_label.config(text="● Logger Running", fg="#22c55e")

def stop_logger():
    global logging_active
    logging_active = False
    status_label.config(text="● Logger Stopped", fg="#ef4444")

def clear_logs():
    key_list.clear()
    log_box.delete(1.0, tk.END)
    with open("logs.json", "w") as f:
        json.dump([], f, indent=4)

tk.Label(
    root,
    text="KEYLOGGER PROJECT",
    bg="#020617",
    fg="#38bdf8",
    font=("Segoe UI", 15, "bold"),
    pady=15
).pack(fill="x")

status_label = tk.Label(
    root,
    text="● Logger Stopped",
    bg="#0f172a",
    fg="#ef4444",
    font=("Segoe UI", 10, "bold")
)
status_label.pack(pady=8)

btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="START",
    width=12,
    bg="#22c55e",
    fg="black",
    font=("Segoe UI", 10, "bold"),
    command=start_logger
).grid(row=0, column=0, padx=5)

tk.Button(
    btn_frame,
    text="STOP",
    width=12,
    bg="#ef4444",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=stop_logger
).grid(row=0, column=1, padx=5)

tk.Button(
    btn_frame,
    text="CLEAR",
    width=12,
    bg="#eab308",
    fg="black",
    font=("Segoe UI", 10, "bold"),
    command=clear_logs
).grid(row=0, column=2, padx=5)

log_box = scrolledtext.ScrolledText(
    root,
    width=48,
    height=18,
    bg="#020617",
    fg="#e5e7eb",
    font=("Consolas", 10)
)
log_box.pack(padx=12, pady=15)

root.bind("<KeyPress>", log_key)

root.mainloop()
