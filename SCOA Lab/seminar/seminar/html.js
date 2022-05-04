$(document).ready(function() {
  jQuery.fn.carousel.Constructor.TRANSITION_DURATION = 2000  // 2 seconds
});
JQuery(document).ready(function($){
  $(".homepage-slides").owlCarousel({
      items: 1,
      nav: true,
      dots: true,
      autoplay: true,
      loop: true,
  autoplay:true,
      autoplayTimeout:2000 
      _navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
      get navText() {
        return this._navText;
      },
      set navText(value) {
        this._navText = value;
      },
      mouseDrag: true,
      touchDrag: false,
  });