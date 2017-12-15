$(function() {
	
	$(".afish-swaper").css({
		"height":$(window).height()*0.85
	});

	$.scrollify({
		section:".afish-swaper", // селектор для секций (разделов) на странице
	    scrollSpeed: 1100,
	    offset : -40, // расстояние в пикселях для комппенсации положения каждого раздела.
	    scrollbars: true //Будет ли видна полоса прокрутки
	});
});