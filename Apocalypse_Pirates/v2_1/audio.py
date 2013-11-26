import pyglet

def play_music(file):
	music = pyglet.resource.media(file)
	music.play()
	pyglet.app.run()
