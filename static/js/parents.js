const container = document.getElementById('thumbnail-container');
const arrowRight = document.getElementById('arrow-right');
const arrowLeft = document.getElementById('arrow-left');
let scrollAmount = 0;

arrowRight.addEventListener('click', () => {
  scrollAmount += 220; // Adjust this value for scrolling
  container.style.transform = `translateX(-${scrollAmount}px)`;
});

arrowLeft.addEventListener('click', () => {
  scrollAmount = Math.max(0, scrollAmount - 220); // Prevent scrolling left past the start
  container.style.transform = `translateX(-${scrollAmount}px)`;
});

const wrapper = document.querySelector('.card');
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

