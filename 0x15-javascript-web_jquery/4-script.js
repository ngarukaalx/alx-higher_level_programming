// wait for the document to be ready
$(document).ready(function () {
  // attach a click event handler
  $('#toggle_header').click(function () {
    // check if it has class red class and update to green or viceveser
    if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      $('header').addClass('red');
    } else {
      $('header').removeClass('red');
      $('header').addClass('green');
    }
  });
});
