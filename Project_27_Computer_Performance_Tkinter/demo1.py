from tkinter import *
import psutil
import speedtest
import math
from PIL import Image, ImageTk


def usage():
    cpu_count = psutil.cpu_count()
    cpu_count_label.config(text=cpu_count,image=tk_image,compound='center',fg='#00ffff')

    cpu_usage = psutil.cpu_percent(1)
    cpu_usage_label.config(text=cpu_usage,image=tk_image,compound='center',fg='#00ffff')
    cpu_usage_label.after(100,usage)

    ram_count = math.floor(psutil.virtual_memory()[0]/1000000000)
    ram_count_text = str(ram_count) + " GB"
    ram_count_label.config(text=ram_count_text,image=tk_image,compound='center',fg='#00ffff')

    ram_usage = psutil.virtual_memory()[2]
    ram_usage_text = str(ram_usage)+ " %"
    ram_usage_label.config(text=ram_usage_text,image=tk_image,compound='center',fg='#00ffff')

    available_ram = math.floor(psutil.virtual_memory()[3]/1000000000)
    available_ram_text = str(available_ram) + ' GB'
    available_ram_label.config(text=available_ram_text,image=tk_image,compound='center',fg='#00ffff')

def internet_speed():
    st = speedtest.Speedtest()
    download_speed = str(math.floor(st.download()/1000000000)) + "Mb/s"
    upload_speed = str(math.floor(st.upload()//1000000000))+ "Mb/s"
    ping = str(st.results.ping)+ "MSS"
    download_label.config(text=download_speed)
    upload_label.config(text=upload_speed)
    ping_label.config(text=ping)
    



root = Tk()
root.config(bg='black')
image = Image.open('speedometer.jpg')
tk_image = ImageTk.PhotoImage(image)

root.geometry("1300x1080")
root.title("Computer Health Report")


## Code for CPU Count
cpu_count_label = Label(root,font=('Orbitron',40,'bold'),text='0',bd=-4)
cpu_count_label.grid(row=0,column=0)
l1 = Label(root,text='CPUs',)
l1.grid(row=1,column=0)

## CPU usage
cpu_usage_label = Label(root,font=('Orbitron',20,'bold'),text='0',bd=-2)
cpu_usage_label.grid(row=0,column=1)
l2 = Label(root,text='CPU Usage in Percentage')
l2.grid(row=1,column=1)

## Total RAM
ram_count_label = Label(root, font=('Orbitron',20,'bold'),text='0',bd=-2)
ram_count_label.grid(row=0,column=2)
l3 = Label(root,text='Total RAM')
l3.grid(row=1,column=2)

## Total RAM % Usage
ram_usage_label = Label(root, font=('Orbitron',20,'bold'),text='0')
ram_usage_label.grid(row=0,column=3)
l4 = Label(root,text='%RAM Used')
l4.grid(row=1,column=3)

## Available RAM
available_ram_label = Label(root,font=('Orbitron',20,'bold'),text=0)
available_ram_label.grid(row=0, column=4)
l5 = Label(root,text='Available RAM')
l5.grid(row=1,column=4)

## Check Internet Speed
speed_button = Button(root,text="Test Internet Speed",command=internet_speed)
speed_button.grid(row=3,column=0)


download_label = Label(root,font=('Orbitron',20,'bold'),text="0 Mb/s")
download_label.grid(row=3,column=1)
l6 = Label(root,text='Download Speed')
l6.grid(row=4,column=1)

upload_label = Label(root,font=('Orbitron',20,'bold'),text="0 Mb/s")
upload_label.grid(row=3,column=2)
l7 = Label(root,text='Upload Speed')
l7.grid(row=4,column=2)

ping_label = Label(root,font=('Orbitron',20,'bold'),text="0 Mb/s")
ping_label.grid(row=3,column=3)
l8 = Label(root,text='Ping')
l8.grid(row=4,column=3)



usage()
root.mainloop()







