$(function(){
  $('.square-left').click(function() {
    $(this).parent('.square').css('background-color', '#b0c4de');
  });

  $('.square-right').click(function() {
    $(this).parent('.square').css('background-color', '#000000');
  });

});
