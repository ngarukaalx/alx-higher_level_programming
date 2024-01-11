// wait for document to be ready
$(document).ready(function() {
   // making a GET request with $.ajax()
   const $list = $('#list_movies')
   $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function(data) {
        $.each(data.results, function(i, result) {
            $list.append('<li>'+ result.title + '</li>');
        });
    }
   }); 
});
