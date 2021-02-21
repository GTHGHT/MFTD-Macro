from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter as tk

main_window = ThemedTk(theme='arc')

main_window.title("MFTD Automation")
main_window.geometry("280x200-8-200")

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=3)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=1)
main_window.rowconfigure(4, weight=3)
main_window.rowconfigure(5, weight=3)

# Title Frame
title_frame = ttk.Frame(main_window)
title_frame.grid(row=0, column=0, columnspan=2, sticky="NSEW")

title_lbl = ttk.Label(title_frame, text="MFTD Macro")
title_lbl.grid(row=0, column=0, sticky="W", padx=5)

help_btn = ttk.Button(title_frame, text="Help")
help_btn.grid(row=0, column=2, sticky="E")

about_btn = ttk.Button(title_frame, text="About")
about_btn.grid(row=0, column=3, sticky="E", padx=5)

title_frame.columnconfigure(0, weight=1)
title_frame.columnconfigure(1, weight=10)
title_frame.columnconfigure(2, weight=1)
title_frame.columnconfigure(3, weight=1)
title_frame.rowconfigure(0, weight=1)

ttk.Label(main_window, text="Emulator").grid(row=1, column=0, columnspan=2, sticky="S")
emul_cmb = ttk.Combobox(main_window, state="readonly", values=("Bluestacks", "LDPlayer"))
emul_cmb.grid(row=2, column=0, columnspan=2, sticky="N", pady=5)

ttk.Label(main_window, text="Action").grid(row=3, column=0, columnspan=2, sticky="S")
action_cmb = ttk.Combobox(main_window, state="readonly", values=("MP Grind", "Acc Reroll"))
action_cmb.grid(row=4, column=0, columnspan=2, sticky="N", pady=5)


def setup_btn_act():
    setup_pu = tk.Toplevel(main_window)

    ttk.Label(setup_pu, text="Hello World").grid(row=0, column=0)
    close_btn = ttk.Button(setup_pu, text="Close", command=setup_pu.destroy)
    close_btn.grid(row=1, column=0)


def start_btn_act():
    pass


setup_btn = ttk.Button(main_window, text="Setup", command=setup_btn_act)
setup_btn.grid(row=5, column=0)

start_btn = ttk.Button(main_window, text="Start", command=start_btn_act)
start_btn.grid(row=5, column=1)

# Disable Maximize/Minimize
main_window.resizable(0, 0)

# Start Window
main_window.mainloop()
