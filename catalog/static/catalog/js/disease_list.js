function showDiseaseDeleteModal(button) {

    const diseaseName = button.getAttribute('data-disease-name');
    const diseaseId = button.getAttribute('data-disease-id');

    const modal = document.getElementById('disease_delete_modal');
    const messageElement = document.getElementById('delete_modal_message');
    const confirmDeleteButton = document.getElementById('confirm_disease_delete_button');
    confirmDeleteButton.textContent = "Delete"
    messageElement.textContent = `Are you sure you want to delete "${diseaseName}"? This action cannot be undone.`;

    confirmDeleteButton.setAttribute('hx-delete', `/disease/delete/${diseaseId}/`);
    confirmDeleteButton.setAttribute('hx-target', 'this');
    htmx.process(confirmDeleteButton);

    modal.showModal();
}

document.body.addEventListener('htmx:afterRequest', function (event) {
    if (event.detail.elt.id === 'confirm_disease_delete_button' && event.detail.xhr.status === 200) {
        const response = JSON.parse(event.detail.xhr.responseText);
        if (response.status === 'success') {
            const row = document.getElementById(`disease-${response.disease_id}-item`);
            Alpine.store("toastManager").addToast("Disease Deleted", "Disease has been deleted successfully", "default", "info");
            if (row) {
                row.remove();
            }
            document.getElementById("disease_delete_modal").close();
        }
    }
});
document.body.addEventListener('closeDiseaseCreateModal', function () {
    document.getElementById('disease_create').close();
});

document.body.addEventListener("updateDiseaseTable", function (event) {
    const tableBody = document.querySelector("#diseaseTableBody");
    Alpine.store('toastManager').addToast("Disease Created", "Disease has been created successfully", "success");
    tableBody.insertAdjacentHTML("beforeend", event.detail.html);
});