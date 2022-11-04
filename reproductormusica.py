import tkinter as tk
import fnmatch
import  os
from pygame import mixer

window = tk.Tk()
window.title("Music Player")
window.geometry("600x800")
window.config(bg='black')

rootpath="C:\\Users\chumo\Music\My music"
pattern="*.mp3"

mixer.init()
pausar=tk.PhotoImage(file='pausar.png')
stop=tk.PhotoImage(file='quitar.png')
next_img=tk.PhotoImage(file='next_img.png')
play=tk.PhotoImage(file='reproducir.png')
prev_img=tk.PhotoImage(file='prev_img.png')
def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath +"//"+listBox.get("anchor"))
    mixer.music.play()
def stopb():
    mixer.music.stop()
    listBox.select_clear('active')
def pauses():
    if pauseButton["text"]=="Pause":
        mixer.music.pause()
        pauseButton["text"]="Play"
    else:
        mixer.music.unpause()
        pauseButton["text"]="Pause"

def play_next():
    next_song=listBox.curselection()
    next_song=next_song[0]+1
    next_song_name=listBox.get(next_song)
    label.config(text = next_song_name)
    mixer.music.load(rootpath + "//" + next_song_name)
    mixer.music.play()
    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    next_song=listBox.curselection()
    next_song=next_song[0]-1
    next_song_name=listBox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath + "//" + next_song_name)
    mixer.music.play()
    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


listBox= tk.Listbox(window,fg='cyan',bg='black',width=100,font=('poppins',14))
listBox.pack(padx=15,pady=15)
label =tk.Label(window,text='',bg='black',fg='yellow',font=('poppins',15))
label.pack(pady=15)

top=tk.Frame(window,bg="black")
top.pack(padx=10,pady=5,anchor='center')

prevButton=tk.Button(window,text="Prev",image=prev_img,bg='black',borderwidth=0,command=play_prev)
prevButton.pack(pady=15,in_=top,side='left')

nextButton=tk.Button(window,text="next",image=next_img,bg='black',borderwidth=0,command=play_next)
nextButton.pack(pady=15,in_=top,side="left")

stopButton=tk.Button(window,text="Stop",image=stop,bg='black',borderwidth=0,command=stopb)
stopButton.pack(pady=15, in_=top,side='left')

pauseButton=tk.Button(window,text="Pause",image=pausar,bg='black',borderwidth=0,command=pauses)
pauseButton.pack(pady=15,in_=top,side='left')

playButton=tk.Button(window,text="Play",image=play,bg='black',borderwidth=0, command=select)
playButton.pack(pady=15,in_=top,side="left")

for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end',filename)
window.mainloop()