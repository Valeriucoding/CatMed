document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        const alert = document.getElementById('customAlert');
        console.log(alert);
        if (alert) {
            alert.style.transition = 'opacity 0.5s ease-out';
            alert.style.opacity = '0';
            setTimeout(function () {
                alert.remove();
            }, 500);
        }
    }, 3000);
});