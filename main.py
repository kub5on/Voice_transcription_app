import speech_recognition as sr
import os


def voice_transcription():
    r = sr.Recognizer()
    mic = sr.Microphone()
    all = []

    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Start talking: ")
        try:
            while True:
                audio = r.listen(source)

                try:
                    res = r.recognize_google(audio, language="pl-PL")
                    all.append(res)
                    print("You said: " + res)
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))

        except KeyboardInterrupt:
            print("Recording stopped.")

    return "\n".join(all)


if __name__ == "__main__":
    result = voice_transcription()

with open('wynik.txt', mode='w', encoding='UTF-8') as f:
    f.write(result)






