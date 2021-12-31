// Navigation

(function ($) {
  $('.search-btn').on('click', function (e) {
    if ($('.search-input-container').hasClass('hide')) {
      e.preventDefault();
      $('.search-input-container').removeClass('hide');

      return false;
    }
  });

  $('.hide-search-input-container').on('click', function (e) {
    e.preventDefault();
    $('.search-input-container').addClass('hide');

    return false;
  });
})(jQuery);

// add navbar-lg to hide.  show
