// banner owl carousel
$(document).ready(function () {
  $(".target-groups").owlCarousel({
    loop: true,
    autoplay: true,
    // autoplayTimeout: 3000, 
    responsive: {
      0: {
        items: 1
      },
      600: {
        items: 2
      },
      1000: {
        items: 3
      }
    }
  })
  $(".client-cente").owlCarousel({
    loop: true,
    autoplay: false,
    // autoplayTimeout: 3000, 
    responsive: {
      0: {
        items: 1
      },
      600: {
        items: 2
      },
      1000: {
        items: 3
      }
    }
  })
})