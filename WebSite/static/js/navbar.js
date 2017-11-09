$('#toggle').on('click', function() {
	$('#menu').slideToggle();
});

$(document).ready(function () {
	var h = $('nav.nav').height();
	$('body').css('margin-top', (h) + "px");
});
