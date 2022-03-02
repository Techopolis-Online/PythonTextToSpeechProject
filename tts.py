
import pyttsx3
# function to speek the typed text from the users
def speekUserInput():
        userInput = input("Please enter text to be spoken.")
        if len(userInput) ==  0:
            print("User input must not be empty.")
        else:
            tts = pyttsx3.init()
            tts.say(userInput)
            tts.runAndWait()

# function to speek the text from text file
def speekFromFile():
    fileName = input("Please type the file you would like spoken.")
    try:
        with open(fileName + ".txt", "r") as fileName:
             fileContent = fileName.read()
             print(fileContent)
        tts = pyttsx3.init()
        tts.say(fileContent)
        tts.runAndWait()
    except FileNotFoundError:
        print("The file  can't be found. You may want to try that again.")
