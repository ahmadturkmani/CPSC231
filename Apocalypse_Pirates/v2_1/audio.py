import winsound
import os

def play_music(file):
	script_dir = os.path.dirname(__file__) #Absolute directory the script is in
	rel_path = 'resources/audio/' #The path that will never change, this is where the audio is located
	abs_file_path = os.path.join(script_dir, rel_path, file) #This is combining the three strings together
	winsound.PlaySound(abs_file_path, winsound.SND_FILENAME) #Playing the wave file(SND_FILENAME), and abs_file_path is the location of audio
	
