// wait for the document to be ready
$(document).ready(function () {
  // attach a click event handler
  $('#red_header').click(function () {
    // adds the class red to the <header>
    $('header').addClass('red');
  });
});
