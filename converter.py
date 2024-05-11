from gtts import gTTS           
import PIL   
import os                       
import pytesseract              
from tkinter import filedialog  
from tkinter import *
from PIL import Image, ImageTk
import pyperclip
import speech_recognition as sr
import pygame
from googletrans import Translator 
window = Tk()
window.geometry('1280x832')
window.resizable(0, 0)
window.title("Speechify Converter")
image=Image.open("_bg_.jpg")
photo=ImageTk.PhotoImage(image)
lab=Label(image=photo,bg='#8fb5c2')
lab.pack()

message = Label(window, text="Speechify Converter", bg="#000000", fg="#FFFF00", width=50, height=3,
                font=('Helvetica', 35, 'italic bold'))
message.place(relx=0.5, rely=0.1, anchor="center")


from tkinter import Text, Scrollbar

result_label = Text(window, bg="grey", fg="black", width=80, height=12, font=('Helvetica', 20, 'bold'))
result_label.place(relx=0.5, rely=0.5, anchor="center")


enter_text_label = Label(window, text="Enter text:", width=15, fg="white", bg="#000000", height=2,
                        font=('Helvetica', 20, 'bold'))
enter_text_label.place(relx=0.01, rely=0.75)

from tkinter import Text


txt2 = Text(window, width=65, height=10, bg="white", fg="black", font=('Helvetica', 20, 'bold'))
txt2.place(relx=0.2, rely=0.75, relheight=0.07)



def PicTexts():
    window.filename = filedialog.askopenfilename()
    img = PIL.Image.open(window.filename)
    result = pytesseract.image_to_string(img)
    res = "**Text copied**\n" + result
    pyperclip.copy(res)
    result_label.delete(1.0, END)  
    result_label.insert(END, res) 
    if not result.strip():
        result_label.configure(text="Sorry!! Nothing recognized\n")


pygame.mixer.init()

def play_audio(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def pause_audio():
    pygame.mixer.music.pause()

def unpause_audio():
    pygame.mixer.music.unpause()

def stop_audio():
    pygame.mixer.music.stop()

def picSpeechs():
    window.filename = filedialog.askopenfilename()
    img= PIL.Image.open(window.filename)      
    result= pytesseract.image_to_string(img)  
    if(result==""):
        res = "Sorry!! Nothing recognized"
        result_label.delete(1.0, END)  # Clear previous content
        result_label.insert(END, res)  # Insert new content
    else:
        res= gTTS(result)                
        window.filename =  filedialog.asksaveasfilename()
        if window.filename:
            res.save(window.filename+ '.mp3')
            play_audio(window.filename + '.mp3')  # Play the audio
            message.configure(text="Saved")
            create_audio_controls()

def TextSpeechs(): 
    textInp = txt2.get("1.0", "end-1c")  
    if textInp.strip(): 
        res = gTTS(textInp)
        window.filename = filedialog.asksaveasfilename()
        if window.filename:  
            res.save(window.filename + '.mp3')
            play_audio(window.filename + '.mp3')  # Play the audio
            message.configure(text="Saved")
            create_audio_controls()
        else:
            message.configure(text="Save canceled")
    else:
        message.configure(text="No text to save")

def create_audio_controls():
    play_button = Button(window, text="Play", command=lambda: play_audio(window.filename + '.mp3'), fg="red", bg="white", width=10, height=2, activebackground="grey", font=('Helvetica', 12, 'bold'))
    play_button.place(x=500, y=180)
    
    pause_button = Button(window, text="Pause", command=pause_audio, fg="red", bg="white", width=10, height=2, activebackground="grey", font=('Helvetica', 12, 'bold'))
    pause_button.place(x=600, y=180)
    
    unpause_button = Button(window, text="Unpause", command=unpause_audio, fg="red", bg="white", width=10, height=2, activebackground="grey", font=('Helvetica', 12, 'bold'))
    unpause_button.place(x=700, y=180)
    
    stop_button = Button(window, text="Stop", command=stop_audio, fg="red", bg="white", width=10, height=2, activebackground="grey", font=('Helvetica', 12, 'bold'))
    stop_button.place(x=800, y=180)

def SpeechToText():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        txt2.delete("1.0", "end")  
        txt2.insert("1.0", text)   
        print("Speech-to-text:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

translator = Translator()
def translate_to_gujarati():
    text_to_translate = txt2.get("1.0", "end-1c")
    translated_text = translator.translate(text=text_to_translate, dest='gu').text
    print(translated_text)
    pyperclip.copy(translated_text)
    result_label.delete(1.0, END)  
    result_label.insert(END, translated_text)  

def speak_gujarati():
    text = result_label.get("1.0", "end-1c")
    if text:
        speech = gTTS(text=text, lang='gu')
        speech.save("gujarati_speech.mp3")
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("gujarati_speech.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        create_audio_controls()

def translate_to_hindi():
    text_to_translate = txt2.get("1.0", "end-1c")
    translated_text = translator.translate(text=text_to_translate, dest='hi').text
    print(translated_text)
    pyperclip.copy(translated_text)
    result_label.delete(1.0, END)  
    result_label.insert(END, translated_text)  

def speak_hindi():
    text = result_label.get("1.0", "end-1c")
    if text:
        speech = gTTS(text=text, lang='hi')
        speech.save("hindi_speech.mp3")
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("hindi_speech.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        create_audio_controls()

def reset_all():
    txt2.delete("1.0", "end")
    result_label.delete("1.0", "end")
    for widget in window.winfo_children():
        if isinstance(widget, Button) and widget.cget("text") in ["Play", "Pause", "Unpause", "Stop"]:
            widget.destroy()


pictext = Button(window, text="Image to Text", command=PicTexts  ,fg="red"  ,bg="white"  ,width=15  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
pictext.place(x=20, y=700)
picspeech = Button(window, text="Image to Speech", command=picSpeechs  ,fg="red"  ,bg="white"  ,width=15  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
picspeech.place(x=20, y=760)
textspeech = Button(window, text="Text to Speech", command=TextSpeechs  ,fg="red"  ,bg="white"  ,width=15  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
textspeech.place(x=300, y=700)
speechtotext = Button(window, text="Speech to Text", command=SpeechToText, fg="red", bg="white", width=15, height=2, activebackground="grey", font=('Helvetica', 15, 'bold'))
speechtotext.place(x=300, y=760)
translate_button = Button(window, text="Text to Gujarati", command=translate_to_gujarati, fg="red", bg="white", width=15, height=2, activebackground="grey", font=('Helvetica', 15, 'bold'))
translate_button.place(x=580, y=700)
speechtotext = Button(window, text="Speak Gujarati", command=speak_gujarati, fg="red", bg="white", width=15, height=2, activebackground="grey", font=('Helvetica', 15, 'bold'))
speechtotext.place(x=580, y=760)
translate_hindi_button = Button(window, text="Text to Hindi", command=translate_to_hindi, fg="red", bg="white", width=15, height=2, activebackground="grey", font=('Helvetica', 15, 'bold'))
translate_hindi_button.place(x=860, y=700)
speechtotext = Button(window, text="Speak Hindi", command=speak_hindi, fg="red", bg="white", width=15, height=2, activebackground="grey", font=('Helvetica', 15, 'bold'))
speechtotext.place(x=860, y=760)


reset_button = Button(window, text="Reset", command=reset_all, fg="red", bg="white", width=15, height=2, activebackground="grey", font=('Helvetica', 15, 'bold'))
reset_button.place(x=1070, y=730)

quitWindow = Button(window, text="Quit", command=window.destroy  ,fg="white"  ,bg="red"  ,width=17  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
quitWindow.place(x=1060, y=60)

window.mainloop()