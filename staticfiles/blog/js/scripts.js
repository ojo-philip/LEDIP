let navBtn = document.querySelector(".nav-btn");
let closeBtn = document.querySelector(".nav-close-btn");
let navBar = document.querySelector(".close-links")
let footerDate = document.querySelector(".footer-date")


navBtn.addEventListener("click", function(){
  navBar.classList.toggle("show-nav")
})

closeBtn.addEventListener("click", function(){
  navBar.classList.remove("show-nav")
})

let date = new Date();
let year = date.getFullYear();
footerDate.innerHTML = year;

$(document).ready(function(){
      $(".post-contents").bind("cut copy", function(e){
        e.preventDefault();
      })
    })