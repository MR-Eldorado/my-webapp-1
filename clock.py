import tkinter as tk
import time


def display_time():
    window = tk.Tk()
    window.title('Clock')

    def p_time():
        disp_time = time.strftime("%H:%M:%S %p")
        digi_clock.config(text=disp_time)
        digi_clock.after(200, p_time)

    digi_clock = tk.Label(window, font=('arial', 150), bg='yellow', fg='black')
    digi_clock.pack()

    p_time()
    window.mainloop()


display_time()
