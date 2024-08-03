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

    document.body.addEventListener('htmx:afterOnLoad', function (event) {
        if (event.detail.elt.id === 'ModalContent') {
            let response = event.detail.xhr.response;

            if (typeof response === 'string') {
                try {
                    response = JSON.parse(response);
                } catch (e) {
                    console.log('Received HTML response, updating modal content');
                    document.getElementById('ModalContent').innerHTML = response;
                    return;
                }
            }

            if (response && response.status === 'success') {
                console.log('Disease added:', response);
                // capitalized model name
                const capitalizedModel = response.model.charAt(0).toUpperCase() + response.model.slice(1);
                console.log('Capitalized model:', capitalizedModel);
                const dropdownMenu = document.getElementById(`${capitalizedModel}Menu`);
                if (dropdownMenu) {
                    const newItem = document.createElement('div');
                    newItem.className = 'p-2';
                    newItem.innerHTML = `
                    <label class="flex items-center space-x-2 cursor-pointer">
                        <label for="id_${response.model}_${response.id}">
                            <input type="checkbox" name="diseases" value="${response.id}" class="checkbox" id="id_${response.model}_${response.id}">
                            ${response.name}
                        </label>
                    </label>
                `;
                    dropdownMenu.appendChild(newItem);

                    const dropdownButton = document.getElementById('DiseasesButton');
                    if (dropdownButton) {
                        let currentText = dropdownButton.textContent;
                        dropdownButton.textContent = currentText ? `${currentText}, ${response.name}` : response.name;
                    }
                } else {
                    console.error('Dropdown menu element not found');
                }

                const modal = document.getElementById('add_modal');
                if (modal) {
                    modal.close();
                } else {
                    console.error('Modal element not found');
                }
            } else {
                console.error('Unexpected response format:', response);
            }
        }
    });
});

function loadDiseaseModal() {
    document.getElementById('add_modal').showModal();
}

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