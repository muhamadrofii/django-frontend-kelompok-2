$(document).ready(function(){
    // Fungsi untuk membuka modal yang berbeda berdasarkan klik
    $(".openModalBtn").click(function(){
        var modalId = $(this).data("target");
        $("#" + modalId).fadeIn();
    });

    // Fungsi untuk menutup modal
    $(".close-btn").click(function(){
        $(this).parents(".modal").fadeOut();
    });
});



const wrapper = document.querySelector('.slider-wrapper');
let currentIndex = 0;

document.getElementById('next').addEventListener('click', () => {
  currentIndex++;
  wrapper.style.transform = `translateX(-${currentIndex * 320}px)`;
});

document.getElementById('prev').addEventListener('click', () => {
  if (currentIndex > 0) {
    currentIndex--;
    wrapper.style.transform = `translateX(-${currentIndex * 320}px)`;
  }
});