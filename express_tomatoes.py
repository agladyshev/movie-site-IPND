import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Express tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="my_style.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Express Tomatoes Movie Trailers</a>
          </div>
          <ul class="nav navbar-nav">
            <li class="active"><a href="express_tomatoes.html">Trailers</a></li>
            <li class="active"><a href="express_tomatoes_description.html">Full description</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}

     <div class="container">
      <div class="navbar navbar-default navbar-fixed-bottom" role="navigation">
        <div class="container">
          <div class="navbar-footer">
            <a class="navbar-brand" href="https://github.com/agladyshev">Udacity IPND project, Alexey Gladyshev, 2016</a>
          </div>
        </div>
      </div>
    </div>
    

  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h3>{movie_title}</h3>
</div>
'''

# A larger movie entry html template
movie_tile_content_desc = '''
<div class="col-md-12 col-lg-6 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="330" height="513">
    <h3>{movie_title}</h3>
    <div class="description">
      <p><b>Trivia:</b> {storyline}</p>
      <p><b>Release year:</b> {year}</p>
    </div>
</div>
'''


def create_movie_tiles_content(movies, page_type):
  """
  Procedure takes as input all movie instances and a type of page we want to create.
  Output is a html code of page content.    
  """
  # The HTML content for this section of the page
  content = ''
  for movie in movies:
    # Extract the youtube ID from the url
    youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
    youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
    trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
    # Append the tile for the movie with its content filled in
    if page_type == "trailer":
      content += movie_tile_content.format(
          movie_title=movie.title,
          poster_image_url=movie.poster_image_url,
          trailer_youtube_id=trailer_youtube_id
      )
    # 2-tiled grid for description page
    if page_type == "description":
      content += movie_tile_content_desc.format(
           movie_title=movie.title,
           poster_image_url=movie.poster_image_url,
           trailer_youtube_id=trailer_youtube_id,
          storyline=movie.storyline,
          year=movie.year
       )
  return content

def open_movies_page(movies):
  # Create or overwrite the output file
  for page in ['express_tomatoes_description.html', 'express_tomatoes.html']:
    output_file = open(page, 'w')

    # Storing the parameter of what page type we're creating
    if "description" in page:
      page_type = "description"
    else:
      page_type = "trailer"

    # Replace the placeholder for the movie tiles with the actual dynamically generated content     
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies, page_type))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible

