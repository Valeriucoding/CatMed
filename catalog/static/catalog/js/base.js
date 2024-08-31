function handleBaseAfterLoad() {
    removeAlert()
    changeToSelectedState()
    posthog.capture('$pageview')
//     if url changes there should be a page leave event

}

window.addEventListener('beforeunload', function (e) {
    posthog.capture('$pageleave')
});

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
    const medicineLink = document.getElementById('medicine-sidebar-item');
    const diseaseLink = document.getElementById('disease-sidebar-item');
    const medicationTypeLink = document.getElementById('medication-type-sidebar-item');
    const organLink = document.getElementById('organ-sidebar-item');
    medicineLink.classList.toggle('active-nav', currentPath === "/");
    diseaseLink.classList.toggle('active-nav', currentPath === "/diseases/");
    medicationTypeLink.classList.toggle('active-nav', currentPath === "/medication-types/");
    organLink.classList.toggle('active-nav', currentPath === "/organs/");

}


function clearMedicineListFilter(badge) {
    const parentDiv = badge.parentElement;
    const badgeSearchParam = parentDiv.id.split('-')[1];
    const searchParamName = parentDiv.getAttribute('data-search-param');

    const url = new URL(window.location);
    const params = url.searchParams.get(searchParamName);
    if (params) {
        console.log(params);
        const values = params.split(',');
        const newValues = values.filter(value => value !== badgeSearchParam);
        if (newValues.length > 0) {
            url.searchParams.set(searchParamName, newValues.join(','));
        } else {
            url.searchParams.delete(searchParamName);
        }
        window.history.pushState({}, '', url);

        htmx.ajax('GET', url.toString(), {
            target: '#main-container',
            swap: 'innerHTML',
            pushUrl: true
        });
    }

    if (parentDiv) {
        parentDiv.remove();
    }
}


document.addEventListener('htmx:pushedIntoHistory', handleBaseAfterLoad);
document.addEventListener('DOMContentLoaded', handleBaseAfterLoad);
