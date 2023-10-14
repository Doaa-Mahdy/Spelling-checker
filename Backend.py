from textblob import Word
def wordchecker():
    print("Word Checker")
    word= Word(input("Enter word: "))
    result= word.spellcheck()
    correctresult = f'Correct spelling of "{word}" is : "{result[0][0]}"' 
    def convertuple1(tup):
        stre=""
        for item in tup:
            for element in item:
                if item.index(element)==0:
                    stre= stre +" "+ element
        return(stre)
    output= correctresult+ "\n" +f'Other suggestions: '+ convertuple1(result)
    return(output)
def sentchecker():
    print("Sentence and paragraph Checker")
    sentence= input("Enter Sentence: ")
    words= sentence.split()
    correctresult=                          ""
    othersuggestions=""
    for word in words:
        wordd= Word(word)
        result= wordd.spellcheck()
        correctresult= correctresult + " "+ f'{result[0][0]}'
        def convertuple2(tup):
            stre=""
            for item in tup:
                for element in item:
                    if item.index(element)==0:
                        stre= stre +" "+element
            return(stre)
        othersuggestions = othersuggestions + f'other suggestions for: "{wordd}" are: '+ convertuple2(result)+ "\n"

    output= f'The best spelling suggestion of "{sentence}" is: {correctresult}'+"\n" + othersuggestions
    return(output)
while True:
    inputtype=input("Do you want to check a word, paragraph or sentence: ")
    if inputtype=="word" or inputtype=="Word":
        print(wordchecker())
        continue 
    elif inputtype=="sentence" or inputtype=="Sentence" or inputtype=="paragraph" or inputtype=="Paragraph":
        print(sentchecker())
        continue
    else:
        print("Please choose Word, Sentence or paragraph.")
        continue
