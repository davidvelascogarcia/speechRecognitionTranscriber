'''
 * ************************************************************
 *      Program: Speech Recognition Transcriber Module
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
'''

# Libraries
import datetime
from fpdf import FPDF
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.utils import make_chunks
import speech_recognition as sr
import shutil
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

print("")
print("Loading Speech Recognition Transcriber module ...")
print("")

# Check file exist
loopFileExist = 0

while int(loopFileExist) == 0:
    
    try:
        print("")
        print("**************************************************************************")
        print("Enter file path:")
        print("**************************************************************************")
        print("")

        # Enter file path
        print("")
        print("[INFO] Please, enter the file path:")
        print("")

        originalFilePath = input()

        print("")
        print("**************************************************************************")
        print("Reading original file:")
        print("**************************************************************************")
        print("")

        # Read file path
        print("")
        print("[INFO] Reading file " + originalFilePath + " at " + str(datetime.datetime.now()) + " ...")
        print("")

        originalFile = AudioSegment.from_file(originalFilePath)
        originalFile = originalFile.set_channels(1)
        loopFileExist = 1

    except:
        # File not exists
        print("")
        print("[ERROR] Sorry, this file not exist re-enter correct name and extension again.")
        print("")

print("")
print("**************************************************************************")
print("Converting file to .wav:")
print("**************************************************************************")
print("")

# Convert file to .wav
print("")
print("[INFO] Converting " + originalFilePath + " to convertedFile.wav at " + str(datetime.datetime.now()) + " ...")
print("")

originalFile.export("convertedFile.wav", format="wav")
convertedFilePath = "convertedFile.wav"

print("")
print("[INFO] File converted.")
print("")

print("")
print("Initializing Speech Recognition engine ...")

print("")
print("**************************************************************************")
print("Reading converted file .wav:")
print("**************************************************************************")
print("")

# Read file path
print("")
print("[INFO] Reading file " + convertedFilePath + " at " + str(datetime.datetime.now()) + " ...")
print("")

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
transcribedFileName = transcribedFileName + ".txt"

print("")
print("[INFO] Transcribed text will be save on " + str(transcribedFileName) + " file.")
print("")

transcribedOutputFile = open(str(transcribedFileName), "w+")

print("")
print("**************************************************************************")
print("Split configuration:")
print("**************************************************************************")
print("")
print("Configuring split mode ...")
print("")

loopControl = 0

while int(loopControl) == 0:

	print("")
	print("Do you want to make split by time or by silence method?.")
	print("")
	print("1. By silence")
	print("2. By time")
	print("")
	print("Enter your split selection:")

	splitSelection = input()

	if int(splitSelection) == 1:

		print("")
		print("[INFO] Split by silence has been selected.")
		print("")

		loopControl = 1

	elif int(splitSelection) == 2:

		print("")
		print("[INFO] Split by time has been selected.")
		print("")

		loopControl = 1

	else:
		print("")
		print("[ERROR] Sorry, option not available, enter your split selection again.")
		print("")

if int(splitSelection) == 1:

	print("")
	print("**************************************************************************")
	print("Processing split on silence:")
	print("**************************************************************************")
	print("")
	print("[INFO] Configuring split on silence ...")
	print("")

	fragments = split_on_silence(convertedFile, min_silence_len = 500, silence_thresh = -45)

if int(splitSelection) == 2:

	print("")
	print("**************************************************************************")
	print("Processing split on time:")
	print("**************************************************************************")
	print("")
	print("[INFO] Configuring split on time ...")
	print("")

	fragmentTime = 1000*55
	fragments = make_chunks(convertedFile, fragmentTime)

try:
    print("[INFO] Creating audio fragments dir ...")
    os.mkdir('fragments')

except(FileExistsError):
	pass

# Move fragments to dir fragments
os.chdir('fragments')

i = 0


print("")
print("**************************************************************************")
print("Processing request:")
print("**************************************************************************")
print("")

for fragment in fragments:

    print("")
    print("[INFO] Building audio fragment at " + str(datetime.datetime.now()) + " ...")
    print("")

    fragmentSilent = AudioSegment.silent(duration = 10)

    print("")
    print("[INFO] Build done.")
    print("")

    audioFragment = fragmentSilent + fragment + fragmentSilent

    print("")
    print("[INFO] Saving audioFragment{0}.wav".format(i))
    print("[INFO] Audio saved.")
    print("")

    audioFragment.export("./audioFragment{0}.wav".format(i), bitrate ='192k', format ="wav")
    audioFragmentFileName = 'audioFragment'+str(i)+'.wav'

    print("")
    print("[INFO] Recognizing audio fragment " + str(i) + " at " + str(datetime.datetime.now()) + " ...")
    print("")

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

        print("")
        print("[INFO] Audio recognized at " + str(datetime.datetime.now()) + ".")
        print("")

        # Write into file
        transcribedOutputFile.write(recognizedText+".\n")

        print("**************************************************************************")
        print("**************************************************************************")
        print("Recognized text: ")
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
        print("[ERROR] I couldn´t understand anything.")
        print("")


    except sr.RequestError as e:

        print("**************************************************************************")
        print("**************************************************************************")
        print("ERROR Request:")
        print("**************************************************************************")
        print("**************************************************************************")
        print("")
        print("[ERROR] Error, Request Google Speech API.")
        print("")


    # Waiting time to next request to avoid audio cut recognition
    print("**************************************************************************")
    print("**************************************************************************")
    print("Waiting for request:")
    print("**************************************************************************")
    print("**************************************************************************")
    print("")
    print("[INFO] Waiting 3 seconds to next request ...")
    print("")

    time.sleep(3)
    i += 1


os.chdir('..')
transcribedOutputFile.close()

print("")
print("[INFO] File transcription finished at " + str(datetime.datetime.now()) + ".")
print("")

print("")
print("**************************************************************************")
print("Transcription finished")
print("**************************************************************************")
print("")
print("[INFO] Finishing program ...")
print("")

# Export to PDF
print("")
print("**************************************************************************")
print("Exporting to PDF:")
print("**************************************************************************")
print("")
print("[INFO] Exporting to PDF ...")
print("")

try:
    # PDF object
    pdfObject = FPDF('P', 'mm', 'A4')

    # Add page
    pdfObject.add_page()

    # Set font and size
    pdfObject.set_font('Times', size = 12)

    # Set margins
    pdfObject.set_margins(20, 20, 20)

    # Add title
    pdfObjectTitle = transcribedFileName
    pdfObjectTitle = pdfObjectTitle.replace(".txt", "")
    pdfObjectTitle = str(pdfObjectTitle).upper()
    pdfObjectTitle = pdfObjectTitle.replace("_"," ")
    pdfObjectTitle = pdfObjectTitle.replace("-"," ")
    pdfObject.set_font('Times', 'B', size = 18)
    pdfObject.cell(0, 0, str(pdfObjectTitle), align='C')

    # Add new page
    pdfObject.add_page()

    # Re-set font and size
    pdfObject.set_font('Times', size = 12)

    # Open source to get data
    textSource = open(str(transcribedFileName),"r")

    for fileLine in textSource:
        pdfObject.multi_cell(157, 10, str(fileLine), 0, 'J' , 0)

    # Close .text
    textSource.close()

    # Prepare output PDF name and export
    pdfOutputName = str(transcribedFileName)
    pdfOutputName = pdfOutputName.replace(".txt", ".pdf")
    pdfObject.output(str(pdfOutputName))

    print("")
    print("[INFO] File exported to PDF.")
    print("")

except:
    print("")
    print("[ERROR] Sorry, I couldn´t export to PDF this file. Some characters had errors, but transcribed text is saved correctly in .txt format.")
    print("")

# Clean temporal data
print("")
print("**************************************************************************")
print("Cleaning temporal data:")
print("**************************************************************************")
print("")
print("[INFO] Cleaning temporal data ...")

try:
    os.remove("convertedFile.wav")

    print("")
    print("[INFO] convertedFile.wav temporal file deleted.")
    print("")

    shutil.rmtree('fragments')

    print("")
    print("[INFO] fragments temporal directoty deleted.")
    print("")

except:
    print("[ERROR] I couldn´t delete convertedFile.wav and fragments directoty. Please, manual delete.")

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
print("")
print("")
print("speechRecognitionTranscriber program finished correctly.")
print("")

# Enter to exit
exitProgram = input("Press any key to close.")
