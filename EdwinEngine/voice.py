import speech_recognition as sr

def speech_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said_by_user = r.recognize_google(audio, language="bg-BG")

        except Exception as e:
            print("Не можах да разбера! [google vr problem]")
            said_by_user = ""

    return said_by_user.lower()

