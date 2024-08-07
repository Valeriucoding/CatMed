function handleBaseAfterLoad() {
    removeAlert()
    changeToSelectedState()
}


function removeAlert() {
    setTimeout(function () {
        const alert = document.getElementById('customAlert');
        if (alert) {
            alert.style.transition = 'opacity 0.5s ease-out';
            alert.style.opacity = '0';
            setTimeout(function () {
                alert.remove();
            }, 500);
        }
    }, 3000);
}

function changeToSelectedState() {
    const currentPath = window.location.pathname;
    const diseaseLink = document.getElementById('disease-sidebar-item');
    console.log(currentPath)
    if (currentPath === "/diseases/") {
        diseaseLink.classList.add('active-nav');
    } else {
        diseaseLink.classList.remove('active-nav');
    }
}

document.addEventListener('htmx:pushedIntoHistory', handleBaseAfterLoad);
document.addEventListener('DOMContentLoaded', handleBaseAfterLoad);