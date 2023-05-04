$('#toggle_header').on('click', function(){
    $('header').toggleClass('red');
    if ($('header').hasClass('red green')){
        $('header').removeClass('red');
    }
});