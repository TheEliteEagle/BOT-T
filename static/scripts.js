console.log('scripts.js is loaded');
$(document).ready(function() {
    $('#inputField').on('submit', function(event) {
        event.preventDefault();
        var formData = $(this).serialize(); 
        $('#inputBox').val('');
        $('#response').text('....');
        $.ajax({
            type: 'POST',
            url:'/', 
            data: formData,
            success: function(data) {
                $('#response').text(data.response);
            },
            error: function() {
                $('#response').text("ERROR LOADING AI RESPONSE");    
            }
        });
    });
});