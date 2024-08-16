function handleAfterLoad() {
    createDropdowns();
}

handleModalContent();

function handleModalContent() {
    document.body.addEventListener('htmx:afterOnLoad', function (event) {
        if (event.detail.elt.id === 'ModalContent') {
            let response = event.detail.xhr.response;

            if (typeof response === 'string') {
                try {
                    response = JSON.parse(response);
                } catch (e) {
                    document.getElementById('ModalContent').innerHTML = response;
                    return;
                }
            }

            if (response && response.status === 'success') {
                const capitalizedModel = response.model.charAt(0).toUpperCase() + response.model.slice(1);
                const dropdownMenu = document.getElementById(`${capitalizedModel}Menu`);
                if (dropdownMenu) {
                    const newItem = document.createElement('div');
                    newItem.className = 'p-2';
                    newItem.innerHTML = `
                    <label class="flex items-center space-x-2 cursor-pointer">
                        <label for="id_${response.model}_${response.id}">
                            <input type="checkbox" name="${response.model}" value="${response.id}" class="checkbox" id="id_${response.model}_${response.id}">
                            ${response.name}
                        </label>
                    </label>
                `;
                    dropdownMenu.appendChild(newItem);

                    const dropdownButton = document.getElementById(`${capitalizedModel}Button`);
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
                    document.getElementById('ModalContent').innerHTML = '';
                } else {
                    console.error('Modal element not found');
                }
            } else {
                console.error('Unexpected response format:', response);
            }
        }
    });
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

function loadCreateModal() {
    document.getElementById('add_modal').showModal();
}

document.addEventListener('htmx:afterOnLoad', handleAfterLoad);
document.addEventListener('DOMContentLoaded', handleAfterLoad);