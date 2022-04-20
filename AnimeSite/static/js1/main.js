/* Dark theme */
$(document).ready(function(){
	/**/
	$('button.mode-switch').click(function(){
		$('body').toggleClass('dark');
	});
	/**/
	$(".btn-close-right").click(function () {
		$(".right-side").removeClass("show");
		$(".expand-btn").addClass("show");
	});
	/**/
	$(".expand-btn").click(function () {
		$(".right-side").addClass("show");
		$(this).removeClass("show");
	});
	/**/
	$('.card').on('click', function (e) {
		if (!e.target.hasAttribute("unclosable")) {
			$(this).toggleClass("card_open");
			$("body").toggleClass("not-scrollbar");
		}
	});
	/**/
	const $header = $('.side-l')
	let prevScroll
	let lastShowPos
	$('.baka-main').on('scroll', function () {
		const scrolled = $('.baka-main').scrollTop()

		if (scrolled > 100 && scrolled > prevScroll) {
			$header.addClass('side-l_hide')
			lastShowPos = scrolled
		} else if (scrolled <= Math.max(lastShowPos - 250, 0)) {
			$header.removeClass('side-l_hide')
		}
		prevScroll = scrolled
	});
	/* Lazy load for background css */
	$.lazyLoadXT.scrollContainer = '.baka-main';
	(function ($) {
		var options = $.lazyLoadXT,
			bgAttr = options.bgAttr || 'data-bg';

		options.selector += ',[' + bgAttr + ']';

		$(document).on('lazyshow', function (e) {
			var $this = $(e.target),
				url = $this.attr(bgAttr);
			if (!!url) {
				$this
					.css('background-image', "url('" + url + "')")
					.removeAttr(bgAttr)
					.triggerHandler('load');
			}
		});
	})(window.jQuery || window.Zepto || window.$);
});

/* Open card anime
var scrollPosition = null;
$('.js-o-card').on('click', function (e) {
	if (!e.target.hasAttribute("unclosable")) {
		var $window = $(window);
		const scrollAnimationDuration = 1000;
		if (!$(this).hasClass('active-card')) {

			$(this).addClass('active-card');

			$('html,body').animate({
				scrollTop: $(".active-card .thumbnail").offset().top - $(window).height() / 3
			}, scrollAnimationDuration);

			scrollPosition = $window.scrollTop();
		} else {
			$(this).removeClass('active-card');

			$('html,body').animate({
			scrollTop: scrollPosition
			}, scrollAnimationDuration);
		}
	}
});*/