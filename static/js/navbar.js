"use strict";

jQuery.fn.navibar = function(){
	let navToggleID = "aaa";
	let baseURL = window.location.origin;


	$(this).addClass("py-4 navbar navbar-expand-lg navbar-dark bg-dark");
		let container = $.parseHTML("<div></div>");
		$(container).addClass("container display-3");

			let navBrand = $.parseHTML("<a></a>");
			$(navBrand).addClass("navbar-brand")
			.attr("href", "#");

				let brand = $.parseHTML("<span></span>");
				$(brand).addClass("display-1")
				.text("SGS V8");
				$(navBrand).append(brand);

			$(container).append(navBrand);

			let buttonToggler = $.parseHTML("<button></button>");
			$(buttonToggler).addClass("navbar-toggler")
			.attr("type", "button")
			.attr("data-toggle", "collapse")
			.attr("data-target", "#" + navToggleID);
				let iconSpan = $.parseHTML("<span></span>");
				$(iconSpan).addClass("navbar-toggler-icon display-1");
				$(buttonToggler).append(iconSpan);
			$(container).append(buttonToggler)

			let navCollapse = $.parseHTML("<div></div>");
			$(navCollapse).addClass("navbar-collapse collapse")
			.attr("id", navToggleID)
				let ul = $.parseHTML("<ul></ul>");
				$(ul).addClass("navbar-nav");

					$(ul).append(get_li("Home", "/", baseURL));
					$(ul).append(get_li("pumps", "/pumps", baseURL));
					$(ul).append(get_li("controll", "/controll", baseURL));

				$(navCollapse).append(ul);

			$(container).append(navCollapse);

	$(this).append(container);

	return this;
}


function get_li(name, link, baseURL){
	let li = $.parseHTML("<li></li>");
	$(li).addClass("nav-item");

	let anker = $.parseHTML("<a></a>");
	$(anker).addClass("nav-link")
	.attr("href", baseURL + link)
	.text(name);

	$(li).append(anker);

	return li;
}