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

	let col = $.parseHTML("<div></div>");
	$(col).addClass("col-lg-3 m-2");
		let card = $.parseHTML("<div></div>");
		$(card).addClass("card text-center");

			let cardHeader = $.parseHTML("<div></div>");
			$(cardHeader).addClass("card-header").html("ID: " + pump["id"]);
			$(card).append(cardHeader);

			let cardBody = $.parseHTML("<div></div>");
			$(cardBody).addClass("card-body");
				let img = $.parseHTML("<img>");
				$(img).addClass("card-img-top").attr("src", "/static/pic/standart.jpg");

				let row = $.parseHTML("<div></div>");
				$(row).addClass("row");
					let btnActivate = $.parseHTML("<button></button>");
					$(btnActivate).addClass("btn btn-outline-primary col-lg m-2")
					.html("Activate")
					.click(function(){
						activatePump(pump["id"]);
					});

					let btnSet = $.parseHTML("<button></button>");
					$(btnSet).addClass("btn btn-outline-primary col-lg m-2")
					.html("Set")
					.click(function(){
						activatePump(pump["id"]);
					});

					let btnEdit = $.parseHTML("<button></button>");
					$(btnEdit).addClass("btn btn-outline-primary col-lg m-2")
					.html("Edit")
					.click(function(){
						activatePump(pump["id"]);
					});

					let btnDelete = $.parseHTML("<button></button>");
					$(btnDelete).addClass("btn btn-danger col-lg m-2")
					.html("Delete")
					.click(function(){
						activatePump(pump["id"]);
					});

					$(row).append(btnActivate)
					.append(btnSet)
					.append(btnEdit)
					.append(btnDelete);


				$(cardBody).append(img).append(row);

			$(card).append(cardBody);



			$(col).append(card);
		$(container).append(col);
}

function activatePump(id){
	console.log(id);
}