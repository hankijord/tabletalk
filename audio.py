from pprint import pprint
import time, os 
import speech_recognition as sr

# Requires that your env/bin/activate script contains the following line
# and that the env/credentials.json file exists
# eg. export GOOGLE_APPLICATION_CREDENTIALS=$VIRTUAL_ENV/credentials.json

# A class to parse audio from either a microphone or file and provide keywords from it
class AudioParser:
    # Initialise with optional audio file for testing
    def __init__(self):
        self.recogniser = sr.Recognizer()
        self.microphone = sr.Microphone()

    # Start listening through microphone
    def start_listening(self):
        with self.microphone as source:
            self.recogniser.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    
        # Starts listening in another thread, use self.stop_listening() to stop
        self.stop_listening = self.recogniser.listen_in_background(self.microphone, self.callback)

    # Analyse audio file for test
    def analyse_audio_file(self, audioFileName):
        # Join the file name to the directory path
        audioPath = path.join(path.dirname(path.realpath(__file__)), audioFileName)

        # Use the audio file as the source
        with sr.AudioFile(audioPath) as source:
            audio = self.recogniser.record(source)

        # Analyse the audio
        self.callback(self.recogniser, audio)

    def natural_language(self, phrase):
        keywords = []
        return keywords

    # A callback to analyse the speech to text
    def callback(self, recognizer, audio):
        try:
            results = self.recogniser.recognize_google_cloud(audio)
            print("Google Cloud Speech thinks you said: " + results)
            print("Google Natural Language thinks these are the keywords: " + ", ".join(self.natural_language(results)))
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))

def main():
    audio = AudioParser()  
    audio.start_listening()
    while True: time.sleep(0.1)

main()
