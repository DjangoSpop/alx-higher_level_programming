// Import jQuery library
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
document.head.appendChild(script);

// Wait for jQuery to load
script.onload = function() {
    // Add event listener for adding new element
    $('div#add_item').on('click', function() {
        // Create new li element
        var newLi = $('<li>Item</li>');
        // Append new li element to ul.my_list
        $('ul.my_list').append(newLi);
    });

    // Add event listener for removing last element
    $('div#remove_item').on('click', function() {
        // Remove last li element from ul.my_list
        $('ul.my_list li:last-child').remove();
    });

    // Add event listener for clearing the list
    $('div#clear_list').on('click', function() {
        // Remove all li elements from ul.my_list
        $('ul.my_list').empty();
    });
};