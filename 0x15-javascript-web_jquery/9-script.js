// wait for the document to be ready
$(document).ready(function() {
  // making a get request
  $.ajax({
    method: 'GET',
    url: ' https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function(data) {
      $('#hello').text(data.hello);
    }
  });
});
