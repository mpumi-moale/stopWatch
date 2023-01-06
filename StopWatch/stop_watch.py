import datetime
import tkinter as Tkinter

# converts initial count to 00:00:00
counter = -7200
# condition to check if program is running
active = False

def counter_label(label):
    def count():
        if active:
            global counter

            # to manage the initial dalay.
            if counter == -7200:
                display = 'Starting...'
            else:
                zero_count = datetime.datetime.fromtimestamp(counter)
                zero_count_string = zero_count.strftime("%H:%M:%S")
                display = zero_count_string

            label['text'] = display # Or label.config(text=display)

            # label.after(agr1, agr2) delays by
            # first argument given in milliseconds
            # and then calls the function given as second agrument
            # Generally like here we need to call the 
            # function in which it is present repeatly
            # Delays by 1000ms=1 seconds and call count again
            label.after(1000, count)
            counter += 1
        # Triggering the start of the counter 
    count()

# start function of the stopwatch
def Start(label):
    global active
    active = True

    counter_label(label)

    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'

# Stop function of the stopwatch
def Stop():
    global active

    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    
    active = False

# Reset function of the stopwatch
def Reset(label):
    global counter
    counter = -7200

    # If reset is pressed while the stopwatch is running.
    if active == False:
        reset['state'] = 'disabled'
        label['text'] = 'Welcome!'
    else:
        label['text'] = 'Starting...'

root = Tkinter.Tk()
root.title("Stopwatch")

# Fixing the window size
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdan 30 bold")
label.pack()

f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda:Reset(label))

f.pack(anchor= 'center', pady=5)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")
root.mainloop()
