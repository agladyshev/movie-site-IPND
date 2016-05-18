import express_tomatoes
import media


twelve_monkeys = media.Movie(
	"12 Monkeys", "Prisoner from 2035 investigates the outbreak of virus in "
	"1990 that wiped out most of the human race", "http://img.goldposter.com/2"
	"015/05/Twelve-Monkeys_poster_goldposter_com_7.jpg", "https://www.youtube."
	"com/watch?v=CBNMEwNx9x4", 1995)

good_will_hunting = media.Movie(
	"Good Will Hunting", "Will Hunting, a janitor at M.I.T., has a gift for "
	"mathematics, but needs help from a psychologist to find direction in his "
	"life", "https://billysteele60.files.wordpress.com/2014/08/good-will-hunti"
	"ng-poster.jpg", "https://www.youtube.com/watch?v=z02M3NRtkAA", 1997)

dead_poets_society = media.Movie(
	"Dead Poets Society", "Unorthodox English teacher at the conservative "
	"boarding school", "http://moviefiles.alphacoders.com/206/poster-206.jpg",
	"https://www.youtube.com/watch?v=wrBk780aOis", 1989)

gattaca = media.Movie(
	"Gattaca", "Vincent Freeman struggles to overcome genetic discrimination "
	"to realize his dream of traveling into space", "https://gatacproduction.f"
	"iles.wordpress.com/2011/07/gattaca-2.jpg", "https://www.youtube.com/watch"
	"?v=hWjlUj7Czlk", 1997)

chef = media.Movie(
	"Chef", "Talented LA chef refuse to compromise his creative integrity",
	"http://www.fatmovieguy.com/wp-content/uploads/2014/04/Chef-Movie-Poster"
	".jpg", "https://www.youtube.com/watch?v=wgFws3AoIUY", 2014)

dark_city = media.Movie(
	"Dark City", "A man struggles with memories of his past, including a wife "
	"he cannot remember, in a nightmarish world with no sun", "https://cinemat"
	"emple.files.wordpress.com/2016/04/dark-city-poster.jpg", "https://www.you"
	"tube.com/watch?v=gt9HkO-cGGo", 1998)

nightcrawler = media.Movie(
	"Nightcrawler", "Louis Bloom, a driven man desperate for work, muscles "
	"into the world of L.A. crime journalism", "http://cdn.collider.com/wp-con"
	"tent/uploads/nightcrawler-poster-final.jpg", "https://www.youtube.com/wat"
	"ch?v=X8kYDQan8bw", 2014)

all_the_presidents_men = media.Movie(
	"All the President's Men", "A reconstruction of the discovery of the White"
	" House link with the Watergate affair by two young reporters from the "
	"Washington Post", "http://www.impawards.com/1976/posters/all_the_presiden"
	"ts_men_xlg.jpg", "https://www.youtube.com/watch?v=vLt6djxhNe8", 1976)

the_hunt_for_red_october = media.Movie(
	"The Hunt for Red October", "In November 1984, the Soviet Union's best "
	"submarine captain in their newest sub violates orders and heads for the "
	"USA. Is he trying to defect or to start a war?", "http://projections.blog"
	"s.gainesville.com/files/2013/08/Red-October-poster.jpg", "https://www.you"
	"tube.com/watch?v=3C2tE7vjdHk", 1990)

movies = [
	twelve_monkeys, good_will_hunting, dead_poets_society, gattaca, chef,
	dark_city, nightcrawler, all_the_presidents_men, the_hunt_for_red_october]
# Creating a list of all Movie instances

express_tomatoes.open_movies_page(movies)
# Launching a procedure to create our movie site and providing it with list of
# our movies
