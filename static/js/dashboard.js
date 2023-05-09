$(document).ready(function(){
	$("button.composebtn").click(function(){
		//$("div#Mailinbox").animate("3000");
		$("div#Mailinbox").fadeOut("3000");
		//$("div#Mailoutbox").animate("3000");
		$("div#Mailoutbox").fadeOut("3000");
		//$("div#Mailtrash").animate("3000");
		$("div#Mailtrash").fadeOut("3000");
		$("div#composeMail").fadeIn("3500");
	});
	
	$("button#close").click(function(){
		$("div#composeMail").animate("500");
		$("div#composeMail").fadeOut("3500");
		$("div#composeMail").animate("500");
	});
	
	$("button#inboxbtn").click(function(){
		$("div#composeMail").fadeOut("500");
		$("div#Mailoutbox").fadeOut("500");
		$("div#Mailtrash").fadeOut("500");
		$("div#Mailinbox").animate("3500");
		$("div#Mailinbox").fadeIn("3500");
		
	});
	
	$("button#sentbtn").click(function(){
		$("div#composeMail").fadeOut("500");
		$("div#Mailinbox").fadeOut("500");
		$("div#Mailtrash").fadeOut("500");
		$("div#Mailoutbox").animate("3500");
		$("div#Mailoutbox").fadeIn("3000");
		$('button#inboxbtn').addClass('btn-default');
		$('button#sentbtn').removeClass('btn-default');
		$('button#sentbtn').addClass('btn-default');
	});
	
	$("button#trashbtn").click(function(){
		$("div#composeMail").fadeOut("500");
		$("div#Mailinbox").fadeOut("500");
		$("div#Mailoutbox").fadeOut("500");
		$("div#Mailtrash").animate("3000");
		$("div#Mailtrash").fadeIn("3000");
	});
    $(document).on('click', '.panel-heading span.clickable', function (e) {
    var $this = $(this);
    if (!$this.hasClass('panel-collapsed')) {
        $this.parents('.panel').find('.panel-body').slideUp();
        $this.addClass('panel-collapsed');
        $this.find('i').removeClass('glyphicon-minus').addClass('glyphicon-plus');
    } else {
        $this.parents('.panel').find('.panel-body').slideDown();
        $this.removeClass('panel-collapsed');
        $this.find('i').removeClass('glyphicon-plus').addClass('glyphicon-minus');
    }
});
$(document).on('click', '.panel div.clickable', function (e) {
    var $this = $(this);
    if (!$this.hasClass('panel-collapsed')) {
        $this.parents('.panel').find('.panel-body').slideUp();
        $this.addClass('panel-collapsed');
        $this.find('i').removeClass('glyphicon-minus').addClass('glyphicon-plus');
    } else {
        $this.parents('.panel').find('.panel-body').slideDown();
        $this.removeClass('panel-collapsed');
        $this.find('i').removeClass('glyphicon-plus').addClass('glyphicon-minus');
    }
});
$(document).ready(function () {
    $('.panel-heading span.clickable').click();
    $('.panel div.clickable').click();
});

    
});