function handleBaseAfterLoad() {
    removeAlert()
    changeToSelectedState()
    posthog.capture('$pageview')
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

function toastManager() {
    return {
        toasts: [],

        addToast(title, message, type = 'default', icon = null, duration = 5000) {
            const id = Date.now();

            const icons = {
                success: `<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>`,
                warning: `<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>`,
                error: `<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>`,
                info: `<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>`
            };

            this.toasts.push({
                id,
                title,
                message,
                type,
                icon: icon || icons[type]
            });

            setTimeout(() => {
                this.removeToast(id);
            }, duration);
        },

        removeToast(id) {
            this.toasts = this.toasts.filter(toast => toast.id !== id);
        }
    };
}