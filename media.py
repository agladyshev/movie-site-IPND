import webbrowser


class Movie():
	"""This class is used to store essential information about movie"""
	def __init__(
			self, movie_title, movie_storyline, poster_image, trailer_youtube,
			year):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.year = year
