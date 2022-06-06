"use strict";

jQuery.fn.pumpDispaly = function(){
	$(this).addClass("pumpDisplay__pumpContainer");
	let targetContainer = this
	$.get("http://192.168.1.120:5000/pumps").done(function(data){
		for(let pump in data){
			add_box(data[pump], targetContainer);
		}

	})
}

function add_box (pump, container){
	console.log(pump)
	let pumpContainer = $.parseHTML("<div class='pumpDisplay__pumpContainder'></div>");
	$(pumpContainer).html("ID: " + pump["id"]);

	$(container).append(pumpContainer);
}