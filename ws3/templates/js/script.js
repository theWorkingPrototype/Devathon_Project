(function ($) {

    "use strict";

    var fullHeight = function () {

        $('.js-fullheight').css('height', $(window).height());
        $(window).resize(function () {
            $('.js-fullheight').css('height', $(window).height());
        });

    };
    fullHeight();

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

})(jQuery);

let cards = document.getElementsByClassName("card");
let i = 0;


let t = setInterval(() => {
    if (i < cards.length)
        cards[i].style.opacity = 1;
    i++;
    if (i >= cards.length) { clearInterval(t); }
}, 100);
