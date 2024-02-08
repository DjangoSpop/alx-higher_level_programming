$(document).ready(function() {
    $('#btn_translate').click(function() {
        const languageCode = $('#language_code').val();
        const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}.json`;

        $.getJSON(apiUrl, function(data) {
            const translation = data.hello;
            $('#hello').text(translation);
        });
    });
});