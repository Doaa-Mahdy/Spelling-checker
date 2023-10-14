from tkinter import *
from textblob import Word
## inserting all the code inside function start_gui to call it in refresh button 
def start_gui():
    global window
    window= Tk()
    ## define function wordchecker() to get a word entry from the user and call checkk function using a button 
    def wordchecker():
        word_entry= Entry(window,font=("Cursive",20,"bold"),bg="#A8c0c9",fg="#135369")
        word_entry.pack()
        ## checkk function  converts the entry to string then Word type to use spellcheck method
        def checkk():
            word = str(word_entry.get())
            word= Word(word)
            result= word.spellcheck()
            ## correct function returns the correct value after checking if it's correct or not
            def correct():
                if result[0][0]== word:
                    output= "Your text is correct"
                    output_label= Label(window, text=output, font=("Cursive",20,"bold"),bg="#A8c0c9",fg="#1C3239")
                    output_label.pack()
                else: 
                    correctresult = f'Correct spelling of "{word}" is : "{result[0][0]}"'
                    ## convertuple1 function gets the suggestions from result tuple and saves it as string
                    def convertuple1(tup):
                        stre=""
                        for item in tup:
                            for element in item:
                                if item.index(element)==0:
                                    stre= stre +" "+ element
                        return(stre)
                    output= correctresult+ "\n" +f'Other suggestions: '+ convertuple1(result)
                    output_label= Label(window, text=output, font=("Cursive",9,"bold"),bg="#A8c0c9",fg="#1C3239")
                    output_label.pack()
                    ## refresh button has command to call refresh function which is defined later on
                    refresh2= Button(window, text="refresh! ",font=("Cursive",20,"bold"),bg="#A8c0c9",fg="#135369", command= refresh)
                    refresh2.config(width=10, height=1)
                    refresh2.pack()
                    return(output)
            ## inside the checkk function correct function has been called
            correct()
        checkbuttoon= Button(window, text="Check! ",font=("Cursive",20,"bold"),bg="#A8c0c9",fg="#135369", command= checkk)
        checkbuttoon.config(width=8, height=1)
        checkbuttoon.pack()
    def sentchecker():
            ## define function sentchecker() to get a sentence entry from the user and call checkk function using a button 
        sent_entry= Entry(window,font=("Cursive",10,"bold"),width= 150,bg="#A8c0c9",fg="#135369")
        sent_entry.pack()
      ## checkk function  converts the entry to string then splits them into words and convert them to Word type to use spellcheck method
        def checkk():
            sentence = str(sent_entry.get())
            words= sentence.split()
            correctresult=""
            othersuggestions=""
            for word in words:
                wordd= Word(word)
                result= wordd.spellcheck()
                correctresult= correctresult + " "+ f'{result[0][0]}'
             ## correct function returns the correct value after checking if it's correct or not
                def correct():
                    nonlocal othersuggestions
                    if result[0][0] != wordd:
                        ## convertuple2 function gets the suggestions from result tuple and saves it as string
                        def convertuple2(tup):
                            stre=""
                            for item in tup:
                                for element in item:
                                    if item.index(element)==0:
                                        stre= stre +" "+element
                            return(stre)
                        othersuggestions = othersuggestions + f'other suggestions for: "{wordd}" are: '+ convertuple2(result)+ "\n"
                    else:
                        othersuggestions = othersuggestions + f' "{wordd}"is correct '+ "\n"
                ## inside the checkk function correct function has been called
                correct()
            output= f'The best spelling suggestion of "{sentence}" is: {correctresult}'+"\n" + othersuggestions
            output_label= Label(window, text=output, font=("Cursive",9,"bold"),bg="#A8c0c9",fg="#1C3239")
            output_label.pack()
            ## refresh2 button has command to call refresh function which is defined later on
            refresh2= Button(window, text="refresh! ",font=("Cursive",20,"bold"),bg="#A8c0c9",fg="#135369", command= refresh)
            refresh2.config(width=10, height=1)
            refresh2.pack()
            return(output)
        checkbuttoon= Button(window, text="Check! ",font=("Cursive",20,"bold"),bg="#A8c0c9",fg="#135369", command= checkk)
        checkbuttoon.config(width=8, height=1)
        checkbuttoon.pack()
    ## functioncaller() takes the value from inputtype entry and evalute it to call the right function for spelling check
    def functioncaller():
        inputtype = str(input_type.get())
        if inputtype=="word" or inputtype=="Word":
            thetype=Label(window, text="Word Checker", font=("Cursive",50,"bold"),bg="#A8c0c9",fg="#1C3239")
            thetype.pack()
            wordchecker()
        elif inputtype=="sentence" or inputtype=="Sentence" or inputtype=="paragraph" or inputtype=="Paragraph":
            thetype=Label(window, text="Sentence Checker", font=("Cursive",50,"bold"),bg="#A8c0c9",fg="#1C3239")
            thetype.pack()
            sentchecker() 
        else:
            thetype=Label(window, text="Please choose Word, Sentence or paragraph.", font=("Cursive",10,"bold"),bg="#A8c0c9",fg="red")
            thetype.pack()
             ## refresh2 button has command to call refresh function which is defined later on
            refresh2= Button(window, text="refresh! ",font=("Cursive",20,"bold"),bg="#A8c0c9",fg="#135369", command= refresh)
            refresh2.config(width=10, height=1)
            refresh2.pack()
    ## defining title, size and some styling for the window
    window.title("Spelling checker")
    window.geometry("800x600")
    window.config(background="#A8c0c9")
    text_heading =Label(window,text="Spelling checker", font=("Cursive",50,"bold"),bg="#A8c0c9",fg="#1C3239")
    text_heading.pack()
    input_typedes= Label(window, text="Do you want to check a word, paragraph or sentence: ", font=("Cursive",20,"bold"),bg="#A8c0c9",fg="#1C3239")
    input_typedes.pack()
    input_type = Entry(window,font=("Cursive",20,"bold"),bg="#A8c0c9",fg="#135369")
    input_type.pack()
    gobuttoon= Button(window, text="Go!",font=("Cursive",20,"bold"),bg="#A8c0c9",fg="#135369", command= functioncaller)
    gobuttoon.config(width=8, height=1)
    gobuttoon.pack()
    window.mainloop()
## refresh function destroys the window and call the start_gui() function that contain all the code. 
def refresh():
    window.destroy()
    start_gui()
start_gui()
