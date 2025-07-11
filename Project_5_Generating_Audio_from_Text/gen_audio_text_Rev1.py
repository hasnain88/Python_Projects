from gtts import gTTS
import os

def text_to_audio():
    print("=== Text to Audio Converter ===")
    text = input("Enter the text you want to convert to audio:\n")

    if not text.strip():
        print("❌ No text entered. Exiting.")
        return

    language = 'en'  # You can change this to 'hi', 'gu', 'fr', etc.
    filename = "converted_audio.mp3"

    try:
        # Create and save audio
        audio = gTTS(text=text, lang=language, slow=False)
        audio.save(filename)

        print(f"✅ Audio saved successfully as: {filename}")
        print("🔊 Playing audio...")

        os.startfile(filename)  # Only works on Windows

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    text_to_audio()