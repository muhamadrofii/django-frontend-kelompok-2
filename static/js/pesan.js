$(document).ready(function () {
    $('#contactForm').on('submit', function (event) {
        event.preventDefault(); // Mencegah form dikirim langsung

        // Mengambil nilai dari setiap input menggunakan jQuery
        let nama = $('#nama').val();
        let email = $('#email').val();
        let feedback = $('#feedback').val();

        // Cek apakah semua kolom sudah terisi
        if (nama === '' || email === '' || feedback === '') {
            alert('Semua kolom harus diisi!');
        } else {
            alert('Pesan Anda telah terkirim!');
            // Di sini, logika pengiriman form bisa ditambahkan, seperti AJAX
        }
    });
});