// Import jQuery library
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

// Function to fetch and print translation
function fetchTranslation() {
    // Get the language code entered by the user
    var languageCode = $('input#language_code').val();

    // Fetch the translation from the API
    $.get('https://www.fourtonfish.com/hellosalut/hello/' + languageCode, function(data) {
        // Display the translation in the hello div
        $('div#hello').text(data.hello);
    });
}

// Event listener for button click
$('input#btn_translate').click(fetchTranslation);

// Event listener for enter key press
$('input#language_code').keypress(function(event) {
    if (event.which == 13) {
        fetchTranslation();
    }
});