// wait for document to be ready
$(document).ready(function() {
   // making a GET request with $.ajax()
   $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function(character) {
        $('#character').text(character.name);
    }
   }); 
});
