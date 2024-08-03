document.addEventListener("DOMContentLoaded", function () {
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

    createDropdowns();
});


function createDropdowns() {
    const dropdownButtons = Array.from(document.querySelectorAll('[id$="Button"]'));

    dropdownButtons.forEach(dropdownButton => {
        const baseId = dropdownButton.id.replace('Button', '');
        const dropdownMenu = document.getElementById(`${baseId}Menu`);

        if (!dropdownMenu) {
            console.warn(`No menu found for button ${dropdownButton.id}`);
            return;
        }

        const dropdownButtonText = dropdownButton.textContent;

        dropdownButton.addEventListener('click', (event) => {
            closeOtherDropdowns(dropdownButton);

            dropdownMenu.classList.toggle('hidden');
            event.stopPropagation();
        });

        document.addEventListener('click', (event) => {
            if (!dropdownButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
                dropdownMenu.classList.add('hidden');
            }
        });

        const checkboxes = dropdownMenu.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', updateButtonText);
        });

        updateButtonText();

        function updateButtonText() {
            const selectedOptions = Array.from(checkboxes)
                .filter(checkbox => checkbox.checked)
                .map(checkbox => checkbox.parentElement.textContent.trim());

            if (selectedOptions.length > 0) {
                dropdownButton.textContent = selectedOptions.join(', ');
            } else {
                dropdownButton.textContent = dropdownButtonText;
            }
        }

        function closeOtherDropdowns(currentButton) {
            dropdownButtons.forEach(button => {
                if (button !== currentButton) {
                    const baseId = button.id.replace('Button', '');
                    const menu = document.getElementById(`${baseId}Menu`);
                    if (menu && !menu.classList.contains('hidden')) {
                        menu.classList.add('hidden');
                    }
                }
            });
        }
    });
}


function loadDiseaseModal() {
    document.getElementById('disease_modal').showModal();
}

// document.body.addEventListener('diseaseAdded', function () {
//     document.getElementById('disease_modal').close();
//     console.log('Disease added');
//     // refresh disease dropdown here
//     // make an AJAX call to get the updated list of diseases
// });