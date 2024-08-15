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
    if (currentPath === "/diseases/") {
        diseaseLink.classList.add('active-nav');
    } else {
        diseaseLink.classList.remove('active-nav');
    }
}


function clearMedicineListFilter(badge) {
    const parentDiv = badge.parentElement;
    const badgeSearchParam = parentDiv.id.split('-')[1];
    const searchParamName = parentDiv.getAttribute('data-search-param');

    const url = new URL(window.location);
    const params = url.searchParams.get(searchParamName);
    if (params) {
        const values = params.split(',');
        const newValues = values.filter(value => value !== badgeSearchParam);
        if (newValues.length > 0) {
            url.searchParams.set(searchParamName, newValues.join(','));
        } else {
            url.searchParams.delete(searchParamName);
        }
        window.history.pushState({}, '', url);
    }

    if (parentDiv) {
        parentDiv.remove();
    }
}


document.addEventListener('htmx:pushedIntoHistory', handleBaseAfterLoad);
document.addEventListener('DOMContentLoaded', handleBaseAfterLoad);
