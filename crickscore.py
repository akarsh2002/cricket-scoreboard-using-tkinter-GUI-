from tkinter import *
from tkinter import messagebox
import tkinter.font
import json
import requests




master = Tk()
master.configure(bg='light grey')
master.geometry("720x480")
Font = tkinter.font.Font(family="Times New Roman")
master.title('Online Cricket Score Board')




def clicked():
    messagebox.showwarning(title="Warning", message="Enter Match ID to proceed!")

def display():
    if len(e1.get()) == 0:
        clicked()
    else:
        match_id = e1.get()
        url = f"https://cricket-api.vercel.app/cri.php?url=https://www.cricbuzz.com/live-cricket-scores/{match_id}/"
        req = requests.get(url)
        match_data = req.json()
        match_name = match_data['livescore']['title']
        title.configure(text="Name of the match:   " + match_data['livescore']['title'])
        update.configure(text="Update:   " + match_data['livescore']['update'])
        current_score.configure(text="Current Score:   " + match_data['livescore']['current'])
        current_batsman.configure(text="Current Batsman:   " + match_data['livescore']['batsman'] + " - " + match_data['livescore']['batsmanrun']+match_data['livescore']['ballsfaced'])
        fours.configure(text="Fours:   " + match_data['livescore']['fours'])
        sixes.configure(text="Sixes:   " + match_data['livescore']['sixes'])
        partnership.configure(text="Partnership:   " + match_data['livescore']['partnership'])
        current_bowler.configure(text="Current Bowler:   " + match_data['livescore']['bowler'] + "  " + match_data['livescore']['bowlerwickets'] + " - " + match_data['livescore']['bowlerruns'] + "(" + match_data['livescore']['bowlerover'] + ")")
        last_wicket.configure(text="Last Wicket:   " + match_data['livescore']['lastwicket'])
        run_rate.configure(text="Run rate:   " + match_data['livescore']['runrate'])
        recent_balls.configure(text="Recent Balls:   " + match_data['livescore']['recentballs'])
       

Label(master, text="Enter match ID: " , bg = "light grey").grid(row=0, sticky=W)
title = Label(master,text="Name of the match:", bg = "light grey")
update = Label(master,text="Update:", bg = "light grey")
current_score = Label(master,text="Current Score:", bg = "light grey")
current_batsman = Label(master,text="Current Batsman:", bg = "light grey")
boundaries = Label(master,text="Boundaries:", bg = "light grey")
fours = Label(master,text="Fours:", bg = "light grey")
sixes = Label(master,text="Sixes:", bg = "light grey")
partnership = Label(master,text="Partnership:", bg = "light grey")
current_bowler = Label(master,text="Current Bowler:", bg = "light grey")
last_wicket = Label(master,text="Last Wicket:", bg = "light grey")
run_rate = Label(master,text="Run Rate:", bg = "light grey")
recent_balls = Label(master,text="Recent Balls:", bg = "light grey")

title.grid(row=5, sticky=W)
update.grid(row=10, sticky=W)
current_score.grid(row=15, sticky=W)
current_batsman.grid(row=20, sticky=W)
boundaries.grid(row=25, sticky=W)
fours.grid(row=30, sticky=W)
sixes.grid(row=35, sticky=W)
partnership.grid(row=40, sticky=W)
current_bowler.grid(row=45, sticky=W)
last_wicket.grid(row=50, sticky=W)
last_wicket.grid(row=55, sticky=W)
run_rate.grid(row=60, sticky=W)
recent_balls.grid(row=70, sticky=W)

p1=PhotoImage(file="icon2.png")
master.iconphoto(False,p1)


e1 = Entry(master)
e1.grid(row=0, column=1)
b = Button(master, text="Show", command = display)
b.grid(row=0, column=2,padx=20,pady=10)
mainloop()
