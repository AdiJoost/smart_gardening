"use strict";

jQuery(document).ready(function($){

	$("p")
		.click(function() {
			$("p").css("color", "black");
			$(this).css("color", "green");
		})
		.mouseenter(function(){
			$(this).css("color", "blue");
		})
		.mouseleave(function(){
			$(this).css("color", "black");
		})

	$("p").each(function(i, element){
		if (i % 2 == 0){
			$(this).css("color", "purple");
		}
	})

	$("p").click(function(){
		$(this).removeClass("display-1")
		.addClass("display-3");
	})

	$("#testList").click(function(){
		let item = $.parseHTML("<li>Kokosnuss</li>");
		$(this).append(item);
	})

	$("#getOrders").click(function(){
		$.get("http://192.168.1.120:5000/orders").done(function(data){
			console.log(data);
		})
	})
	});