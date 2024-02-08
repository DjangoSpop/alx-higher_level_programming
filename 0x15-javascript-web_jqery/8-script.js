// Import jQuery library
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);

// Wait for jQuery to load
script.onload = function() {
    // Fetch movies data
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
        // Get the movie titles
        var movieTitles = data.results.map(function(movie) {
            return movie.title;
        });

        // Create a list element
        var list = $('<ul id="list_movies"></ul>');

        // Append each movie title as a list item
        movieTitles.forEach(function(title) {
            var listItem = $('<li></li>').text(title);
            list.append(listItem);
        });

        // Append the list to the body
        $('body').append(list);
    });
};