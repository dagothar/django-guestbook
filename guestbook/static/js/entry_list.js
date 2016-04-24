'use strict';

$(document).ready(function() {

  $('.search').toggle(search_on);

  $('.toggle-search').click(function(e) {
    e.preventDefault();

    if (search_on) {
      var search_div = $('.search');
      search_div.hide();

      $("input[name='filter']").val('');
      search_div.find("form").submit();

      search_on = false;
    } else {
      $('.search').show();
      search_on = true;
    }

  });

});
