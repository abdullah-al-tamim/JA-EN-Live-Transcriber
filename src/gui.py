import tkinter as tk

def start_transcription():
    # Call the function to capture and transcribe audio
    pass

window = tk.Tk()
window.title("Japanese Audio Transcriber")

label_transcription = tk.Label(window, text="Transcription:")
label_translation = tk.Label(window, text="Translation:")

text_transcription = tk.Text(window, height=10, width=50)
text_translation = tk.Text(window, height=10, width=50)

btn_start = tk.Button(window, text="Start", command=start_transcription)

label_transcription.pack()
text_transcription.pack()
label_translation.pack()
text_translation.pack()
btn_start.pack()

window.mainloop()
