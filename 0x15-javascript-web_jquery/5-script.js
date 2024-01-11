// Wait for the document to be ready
$(document).ready(function () {
  // attach a click event listener
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });
});
