from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3


engine = pyttsx3.init()    # Creating instance of engine class
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

# functionality code
def search():
    data = json.load(open('data.json'))
    word = enterEntry.get()
    word = word.lower()
    if word in data:
        meaning = data[word]
        textArea.delete(1.0, END)
        for item in meaning:
            textArea.insert(END, u'\u2022' + item + '\n\n')

    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = get_close_matches(word, data.keys())[0]
        res = messagebox.askyesno('Confirm', f'Did you mean {close_match} instead?')

        if res == True:
            enterEntry.delete(0, END)
            enterEntry.insert(END, close_match)
            meaning = data[close_match]
            textArea.delete(1.0, END)
            for item in meaning:
                textArea.insert(END, u'\u2022' + item + '\n\n')

        else:
            messagebox.showerror('Error','The word does not exist, Please double check it.')
            enterEntry.delete(0, END)
            textArea.delete(1.0, END)

    else:
        messagebox.showinfo('Information', 'The word does not exist.')
        enterEntry.delete(0, END)
        textArea.delete(1.0, END)




def clear():
    enterEntry.delete(0, END)
    textArea.delete(1.0, END)


def wordaudio():
    engine.say(enterEntry.get())
    engine.runAndWait()


def meaningaudio():
    engine.say(textArea.get(1.0, END))
    engine.runAndWait()



# gui code
root = Tk()  # Create gui window
root.geometry('1000x626+100+30')  # Resize the window
root.title('Talking Dictionary created by Ahinsa')
root.resizable(FALSE, FALSE)  # Resize with fixed width and height

bgImage = PhotoImage(file='F:/Ahinsa/Python project/TalkingDicationary/TalkingDictionary/bg.png')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

enterLabel = Label(root, text='DICTIONARY', font=('arial', 20), fg='#004AAD', bg='white', anchor=CENTER)
enterLabel.place(x=450, y=50)

enterEntry = Entry(root, font=('arial', 20), justify=CENTER, bd=2, relief=GROOVE)
enterEntry.place(x=375, y=100)

searchImage = PhotoImage(file='search.png')
searchButton = Button(root, image=searchImage, bd=0, bg='white', cursor='hand2', activebackground='white',
                      command=search)
searchButton.place(x=470, y=150)

voiceImage = PhotoImage(file='voice.png')
voiceButton = Button(root, image=voiceImage, bd=0, bg='white', cursor='hand2', activebackground='white', command=wordaudio)
voiceButton.place(x=540, y=150)

meaningLabel = Label(root, text='MEANING', font=('arial', 20), fg='#004AAD', bg='white', anchor=CENTER)
meaningLabel.place(x=460, y=220)

textArea = Text(root, width=60, height=12, font=('arial', 10), bd=2, relief=GROOVE)
textArea.place(x=325, y=270)

audioImage = PhotoImage(file='voice.png')
audioButton = Button(root, image=audioImage, bd=0, bg='white', cursor='hand2', activebackground='white', command=meaningaudio)
audioButton.place(x=470, y=485)

clearImage = PhotoImage(file='trash.png')
clearButton = Button(root, image=clearImage, bd=0, bg='white', cursor='hand2', activebackground='white', command=clear)
clearButton.place(x=540, y=485)



def enter_function(event):
    searchButton.invoke()



root.bind('<Return>', enter_function)

root.mainloop()  # Hold gui window in the screen
