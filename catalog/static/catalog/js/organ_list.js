function showOrganDeleteModal(button) {
    const organName = button.getAttribute('data-organ-name');
    const organID = button.getAttribute('data-organ-id');

    const modal = document.getElementById('organ_delete_modal');
    const messageElement = document.getElementById('delete_modal_message');
    const confirmDeleteButton = document.getElementById('confirm_organ_delete_button');
    confirmDeleteButton.textContent = "Delete"
    messageElement.textContent = `Are you sure you want to delete "${organName}"? This action cannot be undone.`;

    confirmDeleteButton.setAttribute('hx-delete', `/organs/delete/${organID}/`);
    confirmDeleteButton.setAttribute('hx-target', 'this');
    htmx.process(confirmDeleteButton);

    modal.showModal();
}

document.body.addEventListener('htmx:afterRequest', function (event) {
    if (event.detail.elt.id === 'confirm_organ_delete_button' && event.detail.xhr.status === 200) {
        const response = JSON.parse(event.detail.xhr.responseText);
        if (response.status === 'success') {
            const row = document.getElementById(`organ-${response.organ_id}-item`);
            Alpine.store("toastManager").addToast("Organ Deleted", "Organ has been deleted successfully", "default", "info");
            if (row) {
                row.remove();
            }
            document.getElementById("organ_delete_modal").close();
        }
    }
});
document.body.addEventListener('closeOrganCreateModal', function () {
    document.getElementById('organ_create').close();
});


document.body.addEventListener("updateOrganTable", function (event) {
    const tableBody = document.querySelector("#organTableBody");
    Alpine.store('toastManager').addToast("Organ Created", "Organ has been created successfully", "success");
    tableBody.insertAdjacentHTML("beforeend", event.detail.html);
});

