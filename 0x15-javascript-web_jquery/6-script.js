// Wait for the document to ready
$(document).ready(function() {
    // attach event listener
    $('#update_header').click(function() {
        $('header').text('New Header!!!');
    });
});
