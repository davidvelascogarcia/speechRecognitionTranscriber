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
from pydub.utils import make_chunks
import speech_recognition as sr
import time


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

# Check file exist
loopFileExist = 0

while int(loopFileExist)==0:

	try:
		# Enter file path
		print("")
		print("Please, enter the file path:")
		originalFilePath = input()

		print("")
		print("")
		print("**************************************************************************")
		print("Reading original file:")
		print("**************************************************************************")
		print("")

		# Read file path
		print("Reading file "+originalFilePath+" ...")
		originalFile = AudioSegment.from_file(originalFilePath)
		originalFile = originalFile.set_channels(1)
		loopFileExist = 1

	except:
		# File not exists
		print("")
		print("Sorry, this file not exist re-enter correct name and extension again.")
		print("")

print("")
print("")
print("**************************************************************************")
print("Converting file to .wav:")
print("**************************************************************************")
print("")

# Convert file to .wav
print("Converting "+originalFilePath+" to convertedFile.wav ...")
originalFile.export("convertedFile.wav", format="wav")
convertedFilePath = "convertedFile.wav"
print("File converted.")

print("")
print("Initializing Speech Recognition engine ...")

print("")
print("**************************************************************************")
print("Reading converted file .wav:")
print("**************************************************************************")
print("")

# Read file path
print("Reading file "+convertedFilePath+" ...")
convertedFile = AudioSegment.from_wav(convertedFilePath)

# Configure transcribedText
# Configure output transcribedText file name
transcribedFileName = str(originalFilePath)
transcribedFileName = transcribedFileName.replace(".mp4","")
transcribedFileName = transcribedFileName.replace(".mkv","")
transcribedFileName = transcribedFileName.replace(".avi","")
transcribedFileName = transcribedFileName.replace(".ogg","")
transcribedFileName = transcribedFileName.replace(".mp3","")
transcribedFileName = transcribedFileName.replace(".wav","")
transcribedFileName = transcribedFileName.replace(".aif","")
transcribedFileName = transcribedFileName.replace(".wma","")
transcribedFileName = transcribedFileName.replace(".amr","")
transcribedFileName = transcribedFileName.replace(".midi","")
transcribedFileName = transcribedFileName.replace(".mpeg","")
transcribedFileName = transcribedFileName.replace(".flv","")
transcribedFileName = transcribedFileName.replace(".mpeg4","")
transcribedFileName = transcribedFileName.replace(".mpg","")
transcribedFileName = transcribedFileName+".txt"

print("Transcribed text will be save on "+str(transcribedFileName)+" file.")
transcribedOutputFile = open(str(transcribedFileName), "w+")

print("")
print("")
print("**************************************************************************")
print("Split configuration:")
print("**************************************************************************")
print("")
print("Configuring split mode ...")

loopControl = 0

while int(loopControl)==0:

	print("")
	print("Do you want to make split by time or by silence method?.")
	print("")
	print("1. By silence")
	print("2. By time")
	print("")
	print("Enter your split selection:")
	splitSelection = input()

	if int(splitSelection)==1:

		print("")
		print("Split by silence has been selected.")
		print("")
		loopControl = 1

	elif int(splitSelection)==2:

		print("")
		print("Split by time has been selected.")
		print("")
		loopControl = 1

	else:
		print("")
		print("Sorry, option not available, enter your split selection again.")
		print("")



if int(splitSelection)==1:

	print("")
	print("")
	print("**************************************************************************")
	print("Processing split on silence:")
	print("**************************************************************************")
	print("")
	print("Configuring split on silence ...")
	print("")
	fragments = split_on_silence(convertedFile, min_silence_len = 500, silence_thresh = -45)

if int(splitSelection)==2:

	print("")
	print("")
	print("**************************************************************************")
	print("Processing split on time:")
	print("**************************************************************************")
	print("")
	print("Configuring split on time ...")
	print("")
	fragmentTime = 1000*55
	fragments = make_chunks(convertedFile, fragmentTime)

try:
    print("Creating audio fragments dir ...")
    os.mkdir('fragments')

except(FileExistsError):
	pass

# Move fragments to dir fragments
os.chdir('fragments')

i = 0

print("")
print("")
print("**************************************************************************")
print("Processing:")
print("**************************************************************************")
print("")

for fragment in fragments:

    fragmentSilent = AudioSegment.silent(duration = 10)
    print("")
    print("Building audio fragment ...")
    print("Build done.")
    print("")
    audioFragment = fragmentSilent + fragment + fragmentSilent

    print("")
    print("Saving audioFragment{0}.wav".format(i))
    print("Audio saved.")
    print("")
    audioFragment.export("./audioFragment{0}.wav".format(i), bitrate ='192k', format ="wav")
    audioFragmentFileName = 'audioFragment'+str(i)+'.wav'

    print("")
    print("Recognizing audio fragment "+str(i)+" ...")


    audioFragmentFile = audioFragmentFileName

    # Init speechRecognition engine
    speechRecognitionEngine = sr.Recognizer()

    # Recognize fragment
    with sr.AudioFile(audioFragmentFile) as audioSource:

        speechRecognitionEngine.adjust_for_ambient_noise(audioSource)
        audioListened = speechRecognitionEngine.record(audioSource, duration=55)

    try:
        # Recognizing audio
        recognizedText = speechRecognitionEngine.recognize_google(audioListened, language="es-ES")
        print("Audio recognized.")
        # Write into file
        transcribedOutputFile.write(recognizedText+".\n")
        print("**************************************************************************")
        print("**************************************************************************")
        print("Recognized: ")
        print("**************************************************************************")
        print("**************************************************************************")
        print("")
        print(recognizedText)
        print("")

    except sr.UnknownValueError:
        print("**************************************************************************")
        print("**************************************************************************")
        print("ERROR Understanding:")
        print("**************************************************************************")
        print("**************************************************************************")
        print("")
        print("I couldn´t understand anything.")
        print("")


    except sr.RequestError as e:
        print("**************************************************************************")
        print("**************************************************************************")
        print("ERROR Request:")
        print("**************************************************************************")
        print("**************************************************************************")
        print("")
        print("Error, Request Google Speech API.")
        print("")


    # Waiting time to next request to avoid audio cut recognition
    print("**************************************************************************")
    print("**************************************************************************")
    print("Waiting for request:")
    print("**************************************************************************")
    print("**************************************************************************")
    print("")
    print("Waiting 3 seconds to next request ...")
    print("")
    time.sleep(3)
    i += 1


os.chdir('..')
print("File transcription finished.")

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
