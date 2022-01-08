$(document).ready(function () {
  // Infinite scroll
  var infinite = new Waypoint.Infinite({
    element: $('.infinite-container')[0],
    handler: function (direction) {},
    offset: 'bottom-in-view',

    onBeforePageLoad: function () {
      $('.spinner-border').show();
    },
    onAfterPageLoad: function () {
      $('.spinner-border').hide();
    },
  });

  // update slug
  // https://www.w3schools.com/jsref/jsref_replace.asp
  $('#id_title').on('keyup', function () {
    let title = document.getElementById('id_title').value;
    document.getElementById('id_slug').value = String(title.replaceAll(' ', '-').toLowerCase());
  });
});
