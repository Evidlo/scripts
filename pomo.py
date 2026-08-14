#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
root.attributes('-alpha', 0.0) #For icon
#root.lower()
root.iconify()
# window = tk.Toplevel(root)
# window.geometry("100x100") #Whatever size
# window.overrideredirect(1) #Remove border
#window.attributes('-topmost', 1)
#Whatever buttons, etc
def update(score, limit=60):
    score +=1
    if score < limit:
        ScoreL.configure(text=score)
        timer = root.after(1000, update, score)
    else:
        root.after_cancel(timer)
        ScoreL.configure(text='Game over')

limit = 10
score = 0
ScoreL = tk.Label(root, text=score)
ScoreL.pack()
timer = root.after(1000, update, score, limit)

root.mainloop()