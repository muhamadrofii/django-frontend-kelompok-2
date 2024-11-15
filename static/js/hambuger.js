// Klik Hamburger di luar elemen
const hamburger = document.querySelector('#navbarNav');
const navbarNa = document.querySelector('#navbarNav');

document.addEventListener('click', function(e) {
    if (!hamburger.contains(e.target) && !navbarNa.contains(e.target)) {
        navbarNa.classList.remove('show'); //
    }
});