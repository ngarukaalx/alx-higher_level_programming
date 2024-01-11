// Wait for thr document to load
$(document).ready(function() {
  $('#add_item').click(function() {
    $('.my_list').append('<li>New item</li>');
  });
  $('#remove_item').click(function() {
    // remove the last li list
    $('.my_list li:last').remove();
  });
  $('#clear_list').click(function() {
    $('.my_list').empty();
  });
});
