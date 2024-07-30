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

// function createDropdowns() {
//     const dropdownButtons = document.querySelectorAll('.dropdownButton');
//     const dropdownMenus = document.querySelectorAll('.dropdownMenu');
//
//     dropdownButtons.forEach((dropdownButton, index) => {
//         const dropdownMenu = dropdownMenus[index];
//         const dropdownButtonText = dropdownButton.textContent;
//         console.log(dropdownButtonText);
//         dropdownButton.addEventListener('click', () => {
//             dropdownMenu.classList.toggle('hidden');
//             console.log('click', dropdownButtonText);
//         });
//
//         document.addEventListener('click', (event) => {
//             if (!dropdownButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
//                 dropdownMenu.classList.add('hidden');
//                 console.log('click', dropdownButtonText);
//             }
//         });
//
//         const checkboxes = dropdownMenu.querySelectorAll('input[type="checkbox"]');
//         checkboxes.forEach(checkbox => {
//             checkbox.addEventListener('change', updateButtonText);
//         });
//         updateButtonText();
//
//         function updateButtonText() {
//             const selectedOptions = Array.from(checkboxes)
//                 .filter(checkbox => checkbox.checked)
//                 .map(checkbox => checkbox.parentElement.textContent.trim());
//             if (selectedOptions.length > 0) {
//                 dropdownButton.textContent = selectedOptions.join(', ');
//             } else {
//                 dropdownButton.textContent = dropdownButtonText;
//             }
//         }
//     });
// }


function createDropdowns() {
    // Find all elements with IDs ending in 'Button'
    const dropdownButtons = Array.from(document.querySelectorAll('[id$="Button"]'));

    dropdownButtons.forEach(dropdownButton => {
        const baseId = dropdownButton.id.replace('Button', '');
        const dropdownMenu = document.getElementById(`${baseId}Menu`);

        if (!dropdownMenu) {
            console.warn(`No menu found for button ${dropdownButton.id}`);
            return;
        }

        const dropdownButtonText = dropdownButton.textContent;
        console.log(dropdownButtonText);

        dropdownButton.addEventListener('click', () => {
            dropdownMenu.classList.toggle('hidden');
            console.log('click', dropdownButtonText);
        });

        document.addEventListener('click', (event) => {
            if (!dropdownButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
                dropdownMenu.classList.add('hidden');
                console.log('click', dropdownButtonText);
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
    });
}