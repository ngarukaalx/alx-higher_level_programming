// wait for the text to be ready
$(document).ready(function() {
  $('#btn_translate').click(function() {
    // get the value of language code
    const lang = $('#language_code').val();
    const link = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;
    $.ajax({
      url: link,
      method: 'GET',
      success: function(data) {
        $('#hello').text(data.hello);
      }
    });

  });
});
