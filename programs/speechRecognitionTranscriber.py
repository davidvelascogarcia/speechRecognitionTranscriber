'''
 * ************************************************************
 *      Program: Speech Recognition Transcriber Module
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
 */
'''

# Libraries
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr


print("**************************************************************************")
print("**************************************************************************")
print("             Program: Speech Recognition Transcriber Module               ")
print("                     Author: David Velasco Garcia                         ")
print("                             @davidvelascogarcia                          ")
print("**************************************************************************")
print("**************************************************************************")

print("")
print("Starting system ...")

print("")
print("Loading Speech Recognition Transcriber module ...")

# Enter file path
print("Please, enter the file path:")
originalFilePath = input()

# Read file path
print("Reading file "+originalFilePath+" ...")
originalFile = AudioSegment.from_file(originalFilePath)

# Convert file to .wav
print("Converting "+originalFilePath+" to convertedFile.wav ...")
originalFile.export("convertedFile.wav", format="wav")
convertedFilePath = "convertedFile.wav"
print("File converted.")

print("")
print("Initializing Speech Recognition engine ...")

# Read file path
print("Reading file "+convertedFilePath+" ...")
convertedFile = AudioSegment.from_wav(convertedFilePath)

# Configure silence thresh
print("Transcribed text will be save on transcribedText.txt file")
transcribedFile = open("transcribedText.txt", "w+")

print("Configuring split on silence ...")
fragments = split_on_silence(convertedFile, min_silence_len = 500, silence_thresh = -45)

try:
    print("Creating audio fragments dir ...")
    os.mkdir('fragments')

except(FileExistsError):
	pass

# Move fragments to dir fragments
os.chdir('fragments')

i = 0

for fragment in fragments:

    fragmentSilent = AudioSegment.silent(duration = 10)
    print("Building audio fragment ...")
    audioFragment = fragmentSilent + fragment + fragmentSilent

    print("Saving audioFragment{0}.wav".format(i))
    audioFragment.export("./audioFragment{0}.wav".format(i), bitrate ='192k', format ="wav")
    audioFragmentFileName = 'audioFragment'+str(i)+'.wav'

    print("Recognizing audio fragment "+str(i)+" ...")
    audioFragmentFile = audioFragmentFileName

    # Init speechRecognition engine
    speechRecognitionEngine = sr.Recognizer()

    # Recognize fragment
    with sr.AudioFile(audioFragmentFile) as audioSource:

        speechRecognitionEngine.adjust_for_ambient_noise(audioSource)
        audioListened = speechRecognitionEngine.listen(audioSource)

    try:

        # Recognizing audio
        recognizedText = speechRecognitionEngine.recognize_google(audioListened, language="es-ES")

        # Write into file
        transcribedFile.write(recognizedText+".\n")
        print("Recognized: "+recognizedText)


    except sr.UnknownValueError:
        print("")
        print("Error, Request Google Speech API.")
        print("")

    except sr.RequestError as e:
        print("")
        print("Unknown Error")
        print("")

    i += 1

os.chdir('..')
print("File transcription finished.")
