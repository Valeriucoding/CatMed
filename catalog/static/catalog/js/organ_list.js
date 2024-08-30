function showOrganDeleteModal(button) {
    const organName = button.getAttribute('data-organ-name');
    const organID = button.getAttribute('data-organ-id');

    const modal = document.getElementById('organ_delete_modal');
    const messageElement = document.getElementById('delete_modal_message');
    const confirmDeleteButton = document.getElementById('confirm_delete_button');
    confirmDeleteButton.textContent = "Delete"
    messageElement.textContent = `Are you sure you want to delete "${organName}"? This action cannot be undone.`;

    confirmDeleteButton.setAttribute('hx-delete', `/medication-types/delete/${organID}/`);
    // TODO: update url
    confirmDeleteButton.setAttribute('hx-target', 'this');
    htmx.process(confirmDeleteButton);

    modal.showModal();
}

document.body.addEventListener('htmx:afterRequest', function (event) {
    if (event.detail.elt.id === 'confirm_delete_button' && event.detail.xhr.status === 200) {
        const response = JSON.parse(event.detail.xhr.responseText);
        if (response.status === 'success') {
            const row = document.getElementById(`organ-${response.organ_id}-item`);
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