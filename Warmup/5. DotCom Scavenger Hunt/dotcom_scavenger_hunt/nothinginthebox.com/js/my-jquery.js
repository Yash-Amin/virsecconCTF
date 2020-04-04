/*
	This file is part of a site template for sale at ThemeForest.net.
	See: http://themeforest.net/user/GeertDD/portfolio
	Copyright ©2009 Geert De Deckere <geert@idoe.be>
*/

$(document).ready(function() {

	// CONFIGURATION ----------------------------------------------------------

	// Setting to globally change the speed of the effects
	// Options: 'slow', 'normal', 'fast', or a custom time in milliseconds
	var fxspeed = 'fast';


	// BODY'S TOP PADDING -----------------------------------------------------

	// Adjust the whitespace at the top of the page depending on the height of the viewport.
	// The original top padding is 181px. Each navigation bar is 40px high.
	if ($(window).height() < 800) {
		$('body').css('padding-top', '121px'); // -40px
	}
	if ($(window).height() < 700) {
		$('body').css('padding-top', '81px'); // -80px
	}
	if ($(window).height() < 600) {
		$('body').css('padding-top', '41px'); // -120px
	}


	// NAVIGATION -------------------------------------------------------------

	// Wrap an extra div around the content parts. This makes the slide effects smoother
	// because the new outer div does not contain padding or margin.
	$('div.content').wrap('<div></div>');

	// Hide all the inactive content blocks.
	$('#main > li > h2:not(.active)').siblings().hide();

	// A jQuery object containing the navigation bars
	var $nav = $('#main > li > h2');

	// Here is what happens when the navigation is clicked
	$nav.click(function() {
		// Determine the position (1-5) of the clicked navigation bar,
		// this is needed to calculate the margin to align it next to the title (see below).
		var navcount = $(this)[0].id.replace(/\D+/, '');

		// Highlight or de-highlight the clicked navigation bar by toggling the CSS class “active”
		if ($(this).hasClass('active')) {
			$nav.removeClass('active');
			$('#main').animate({marginTop:0}, fxspeed);
		} else {
			$nav.removeClass('active');
			$(this).addClass('active');
			// Align the active nav next to the title
			$('#main').animate({marginTop:'-' + (navcount - 1) * 40 + 'px'}, fxspeed);
		}

		// Happy sliding!
		$nav.siblings(':visible').slideUp(fxspeed);
		$(this).siblings(':hidden').slideDown(fxspeed);
	});

	// Regular links can also be used to jump to another section (by linking to “#nav1”)
	// This code makes them trigger the navigation bar sliding effects
	$('a[href^=#nav]').click(function() {
		// Clean up the id, we only want the “#xxx” anchor part, and then simulate a navigation bar click
		$('h2' + $(this)[0].href.replace(/^[^#]+/, '')).trigger('click');
	});


	// LIGHT/DARK SWITCHER ----------------------------------------------------

	// Show the light and dark switcher
	$('#switch').show();

	// And here is what happens when it gets clicked
	$('#switch').click(function() {
		// Turn the light on or off, view the CSS file for body.light styles
		$('body').toggleClass('light');

		// A boolean, referenced below
		var light_on = $('body').hasClass('light');

		// Animate the switch button, and change its text
		$(this)
			.animate({marginTop:'-40px'}, fxspeed, function() { $(this).text('Light ' + (light_on ? 'off' : 'on')); })
			.animate({opacity:1}, 300) // http://www.learningjquery.com/2007/01/effect-delay-trick
			.animate({marginTop:0}, fxspeed);
	});


	// AJAX CONTACT FORM ------------------------------------------------------

	// The contact form got submitted...
	$('#contactform').submit(function() {

		// Disable the submit button
		$('#contactform input[type=submit]')
			.attr('value', 'Sending message…')
			.attr('disabled', 'disabled');

		// AJAX POST request
		$.post(
			$(this).attr('action'),
			{
				name:$('#name').val(),
				email:$('#email').val(),
				message:$('#message').val()
			},
			function(errors) {
				// No errors
				if (errors == null) {
					$('#contactform')
						.hide()
						.html('<h3>Thank you</h3><p>Your message has been sent.</p>')
						.show();
				}

				// Errors
				else {
					// Re-enable the submit button
					$('#contactform input[type=submit]')
						.removeAttr('disabled')
						.attr('value', 'Send message');

					// Technical server problem, the email could not be sent
					if (errors.server != null) {
						alert(errors.server);
						return false;
					}

					// Empty the errorbox and reset the error alerts
					$('#contactform .errorbox').html('<ul></ul>').show();
					$('#contactform p').removeClass('alert');

					// Loop over the errors, mark the corresponding input fields,
					// and add the error messages to the errorbox.
					for (field in errors) {
						if (errors[field] != null) {
							$('#' + field).parent('p').addClass('alert');
							$('#contactform .errorbox ul').append('<li>' + errors[field] + '</li>');
						}
					}
				}
			},
			'json'
		);

		// Prevent non-AJAX form submission
		return false;
	});

});