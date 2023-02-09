# script to detect input audio and echo back
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

def SpeakText(command):
    """
    Convert text to speech and play aloud
    """
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    return True
	
	
# Await input
status = False
while(status == False):
	try:
		with sr.Microphone() as source2:
			
			# allow time to adjust to ambient noise
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for input
			audio2 = r.listen(source2)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("Did you say ",MyText)
			status = SpeakText(MyText)
            
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occurred")
