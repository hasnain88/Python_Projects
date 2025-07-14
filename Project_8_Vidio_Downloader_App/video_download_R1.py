from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import shutil
import os


def get_path():
    path = filedialog.askdirectory()
    if path:
        path_label.config(text=path)

def download():
    video_url = url_entry.get().strip()
    file_path = path_label.cget("text").strip()

    if not video_url or not file_path or file_path == "Select path to download":
        status_label.config(text="❌ Please provide both URL and download path.", fg="red")
        return

    try:
        status_label.config(text="Downloading...", fg="blue")
        root.update_idletasks()

        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        downloaded_file = stream.download()

        video_clip = VideoFileClip(downloaded_file)
        video_clip.close()

        shutil.move(downloaded_file, os.path.join(file_path, os.path.basename(downloaded_file)))

        status_label.config(text="✅ Download Complete!", fg="green")
    except Exception as e:
        status_label.config(text=f"❌ Error: {str(e)}", fg="red")

# GUI Setup
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("400x300")
root.resizable(False, False)

canvas = Canvas(root, width=400, height=300)
canvas.pack()

# App Title
app_label = Label(root, text="YouTube Video Downloader", fg='blue', font=("Arial", 16))
canvas.create_window(200, 30, window=app_label)

# Video URL Input
url_label = Label(root, text="Enter YouTube Video URL:")
url_entry = Entry(root, width=40)
canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)

# Download Path
path_label = Label(root, text="Select path to download", font=("Arial", 9))
path_button = Button(root, text="Browse", command=get_path)
canvas.create_window(200, 150, window=path_label)
canvas.create_window(200, 170, window=path_button)

# Download Button
download_button = Button(root, text="Download Video", command=download)
canvas.create_window(200, 220, window=download_button)

# Status Label
status_label = Label(root, text="", font=("Arial", 10))
canvas.create_window(200, 260, window=status_label)

root.mainloop()
