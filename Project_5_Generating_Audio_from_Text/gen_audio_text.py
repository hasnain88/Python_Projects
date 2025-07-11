# from gtts import gTTS
# import os


# text = "LOL this is really funny"
# output = gTTS(text=text,lang='en',slow=False)
# output.save('output.mp3')

# os.startfile("output.mp3")

from gtts import gTTS
import os

# Text to convert
text = "LOL this is really funny"

# Create gTTS object
output = gTTS(text=text, lang='en', slow=False)

# Output file path
file_path = "output.mp3"

# Save audio to file
try:
    output.save(file_path)
    print("Audio file saved successfully at:", os.path.abspath(file_path))

    # Play the audio file (Windows only)
    os.startfile(file_path)
except Exception as e:
    print("Error:", e)
