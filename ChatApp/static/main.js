$(document).on('submit', '#message', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: "",
        data: {
            message: $('#msg').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        }
    });
})