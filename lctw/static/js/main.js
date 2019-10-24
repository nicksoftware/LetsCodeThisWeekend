setTimeout(function(){
    $('message').fadeOut('slow');
}, 30);

$(document).ready(function(){
    $(".owl-carousel").owlCarousel();
  });


  
  $('#main-slider').owlCarousel({
    items: 1,
    nav: false,
    dots: true,
    autoplay: true,
    autoplayHoverPause: true,
    dotsSpeed: 400
});

$('#courses').owlCarousel({
    loop:true,
    items:1,
    margin:1,
    nav:false,
    autoplay:true,
    responsive: {
        480: {
            items: 1
        },
        765: {
            items: 2
        },
        991: {
            items: 3
        },
        1200: {
            items: 3
        }
    }

})

  $('.owl-carousel').owlCarousel({
    loop:true,
    items:1,
    margin:2,
    nav:false,
    autoplay:true,
    responsive: {
        480: {
            items: 1
        },
        765: {
            items: 2
        },
        991: {
            items: 2
        },
        1200: {
            items: 2
        }
    }

})




