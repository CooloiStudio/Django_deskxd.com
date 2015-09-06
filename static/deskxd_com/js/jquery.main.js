$(function(){
	var wallHeight = $("body").height()
	var H = $(window).height()
	if(H>wallHeight)
	{
		$("#footer-line").height(H - wallHeight)
	}
});