// wait for the document to be ready
$(document).ready(function () {
  // attach a click event handler
  $('#red_header').click(function () {
    // update text colour on header to red
    $('header').css('color', '#FF0000');
  });
});
