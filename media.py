#Submitted by Cheryl J. Banks

import webbrowser

class Movie():
	"""This class provides a way to store movie related information."""

	#The list below is called a "Class Variable".
	VALID_RATINGS = ["G","PG","PG-13","R"]
	
	"""	The function def __init__(): creates space in memory for a new instance or object,
	including title, story line, poster image, and movie trailer. """
	
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	
	#The function def show_trailer(): below opens the YouTube trailer that is specified
	#in the def __init_(): above.	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)