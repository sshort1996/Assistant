import speech_recognition as sr
import pyttsx3
import functools
import threading

class ParseCommands:
    # init method or constructor
    # def __init__(self, name):
    #     self.name = name

    def _speak_text(self, command):
        """
        Convert text to speech and play aloud
        """
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
        return True

    def _await_input(self):
        """
        Listen for speech using the mic, play back using `_speak_text` method
        """
        r = sr.Recognizer()
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

                    return MyText
                    # print("Did you say ",MyText)
                    # status = self._speak_text(MyText)
                    
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                
            except sr.UnknownValueError:
                print("unknown error occurred")

class Listener:

    def _run_in_threads(*functions):
        threads = []

        for function in functions:
            thread = threading.Thread(target = function)
            thread.daemon = True
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    def _listen_for_trigger(value, listen):
        p = ParseCommands()
        while not listen.is_set():
            input = p._await_input()        


    def _print_my_value_n_times(value, n, listen):
        for i in range(n):
            print(value)
        listen.set()

    def _listen_for_trigger(self):
        p = ParseCommands()
        while True:
            input = p._await_input()        
            if input == str.upper("Hello Arthur"):
                print("Heard trigger word")
                break


if __name__ == "__main__":
    
    # Class instance for listening for input on main thread
    L = Listener()
    L._listen_for_trigger()
    # # Event to stop listening when hears trigger word
    # listen = threading.Event()
    # infinite_loop = functools.partial(L._listen_for_trigger, "xyz", listen)
    # my_values = functools.partial(L._print_my_value_n_times, "123", 5, listen)
    # L.run_in_threads(infinite_loop, my_values)

    
