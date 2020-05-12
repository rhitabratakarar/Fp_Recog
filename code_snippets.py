# importing tkinter module 
from tkinter.ttk import Progressbar
import time 
from tkinter import *
  
# creating tkinter window 
root = Tk() 
  
# Progress bar widget 
progress = Progressbar(root, orient = HORIZONTAL, length = 100, mode = 'determinate') 
  
# Function responsible for the updation 
# of the progress bar value 
def bar(): 
    progress['value'] = 20
    root.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 40
    root.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 50
    root.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 60
    root.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 80
    root.update_idletasks() 
    time.sleep(1) 
    progress['value'] = 100
  

progress.pack(pady = 10) 
  
# This button will initialize 
# the progress bar 
Button(root, text = 'Start', command = bar).pack(pady = 10) 
  
# infinite loop 
mainloop()
