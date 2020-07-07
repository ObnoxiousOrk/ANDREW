import pyttsx3
import speech_recognition as sr
import subprocess
import os

import splitCommand as s

class CONTROLLER():
	def __init__(self):
		self.vName = "ANDREW"
		self.vVersion = 1

	#-- Intitilises the tts engine and the speach regniser engine --#
		self.tts = pyttsx3.init()
		self.r = sr.Recognizer()

	def listen(self):
		while(1):     
			with sr.Microphone() as listener: #--Uses the mic as an input

				self.r.adjust_for_ambient_noise(listener, duration=0.2) #--Adjusts the sensitivity of the mic
				listener = self.r.listen(listener) #--Listens for audio input
				vCommand = self.r.recognize_google(listener) #--Sends the audio to google for decoding and stores the result as text

				# vCommand = "count in 2 from 1 to 10"

				return vCommand

	def splitCommand(self, vCommand):
		return s.split(vCommand)


	def main(self):
		vCommand = self.listen()
		global aCommand
		aCommand = self.splitCommand(vCommand)

global ANDREW
ANDREW = CONTROLLER()

"""
proper format for commands is always ["command keyword", "additional parameter 1", "any additional info needed for parameter 1" etc etc]
"""