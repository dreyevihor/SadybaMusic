$(function() {
	
	$(".panel").css({
		"height":$(window).height()
	});

	$.scrollify({
		section:".panel", // селектор для секций (разделов) на странице
	    scrollSpeed: 1100,
	    offset : 0, // расстояние в пикселях для комппенсации положения каждого раздела.
	    scrollbars: false //Будет ли видна полоса прокрутки

	});


});