"use strict";
console.log("Working!")
// Testimonial carousel
document.querySelectorAll(document).ready(function() {
  document.querySelectorAll(".testimonial-carousel").slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed:2000,
    arrows: true,
    prevArrow: document.querySelectorAll(".testimonial-carousel-controls .prev"),
    nextArrow: document.querySelectorAll(".testimonial-carousel-controls .next"),
  });
});

