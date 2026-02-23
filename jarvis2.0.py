# import speech_recognition as sr
# import pyttsx3
# import datetime
# import wikipedia
# import webbrowser
# import pywhatkit
# import time

# # ---------------------- #
# # Initialize Text-to-Speech
# # ---------------------- #
# engine = pyttsx3.init()
# engine.setProperty('rate', 170)

# def speak(text):
#     print(f"Jarvis: {text}")
#     engine.say(text)
#     engine.runAndWait()

# # ---------------------- #
# # Listen for Voice Commands
# # ---------------------- #
# def listen():
#     listener = sr.Recognizer()
#     try:
#         with sr.Microphone() as source:
#             print("\n Listening...")
#             listener.adjust_for_ambient_noise(source, duration=1)
#             audio = listener.listen(source)
#         command = listener.recognize_google(audio)
#         command = command.lower()
#         print(f"You said: {command}")
#         return command
#     except sr.UnknownValueError:
#         print(" Could not understand your voice.")
#     except sr.RequestError:
#         print(" Speech service is unavailable (check your internet).")
#     except Exception as e:
#         print(f" Error: {e}")
#     return ""

# # ---------------------- #
# # Process Commands
# # ---------------------- #
# def process_command(command):
#     if 'time' in command:
#         time_now = datetime.datetime.now().strftime('%I:%M %p')
#         speak(f"The time is {time_now}")

#     elif 'date' in command:
#         date_today = datetime.datetime.now().strftime('%B %d, %Y')
#         speak(f"Today's date is {date_today}")

#     elif 'who is' in command:
#         person = command.replace('who is', '').strip()
#         try:
#             info = wikipedia.summary(person, 1)
#             speak(info)
#         except wikipedia.exceptions.DisambiguationError as e:
#             speak(f"Be more specific. Did you mean {e.options[0]}?")
#         except wikipedia.exceptions.PageError:
#             speak("Sorry, I couldn't find any information on that.")
#         except Exception as e:
#             speak(f"An error occurred while fetching information: {e}")

#     elif 'open youtube' in command:
#         speak("Opening YouTube")
#         webbrowser.open("https://www.youtube.com")

#     elif 'play' in command:
#         song = command.replace('play', '').strip()
#         if song:
#             speak(f"Playing {song} on YouTube")
#             pywhatkit.playonyt(song)
#         else:
#             speak("Please tell me what you want me to play.")

#     elif any(word in command for word in ['stop', 'exit', 'bye']):
#         speak("Goodbye! Have a great day.")
#         exit()

#     elif 'how are you' in command:
#         speak("I'm doing great, thank you for asking!")

#     else:
#         speak("Sorry, I didn’t understand that. Please try again.")

# # ---------------------- #
# # Main Program
# # ---------------------- #
# speak("Hello! I am Jarvis. How can I help you today?")

# while True:
#     command = listen()

#     # Optional: Wake word
#     if 'jarvis' in command:
#         command = command.replace('jarvis', '').strip()
#         process_command(command)
#     elif command != "":
#         process_command(command) 

##################################################################### add flac 1.5 win  >>>>>>>>>>>>  