from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone as source:
  print("Clearing background noise...")
  sr.adjust_for_ambient_noise(source, duration=1)
  print("Waiting for message....")
  recordedAudio = recognizer.listen(source)
  print("Done recording")
try:
  print("Printing message")
  text = recognizer.recognize_google(recordedAudio, language="en-US")
  print("Your message: {}".format(text))
except Exception as ex:
  print(ex)
Sentence = [str(text)]
analyser = SentimentIntensityAnalyzer()
for i in Sentence:
  v = analyser.polarity_score(i)
  print(v)
