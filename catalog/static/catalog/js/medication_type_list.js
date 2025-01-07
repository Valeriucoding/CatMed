function showMedicationTypeDeleteModal(button) {
    const medicationTypeName = button.getAttribute('data-medication-type-name');
    const medicationTypeID = button.getAttribute('data-medication-type-id');

    const modal = document.getElementById('medication_type_delete_modal');
    const messageElement = document.getElementById('delete_modal_message');
    const confirmDeleteButton = document.getElementById('confirm_medication_type_delete_button');
    confirmDeleteButton.textContent = "Delete"
    messageElement.textContent = `Are you sure you want to delete "${medicationTypeName}"? This action cannot be undone.`;

    confirmDeleteButton.setAttribute('hx-delete', `/medication-types/delete/${medicationTypeID}/`);
    confirmDeleteButton.setAttribute('hx-target', 'this');
    htmx.process(confirmDeleteButton);

    modal.showModal();
}

document.body.addEventListener('htmx:afterRequest', function (event) {
    if (event.detail.elt.id === 'confirm_medication_type_delete_button' && event.detail.xhr.status === 200) {
        const response = JSON.parse(event.detail.xhr.responseText);
        if (response.status === 'success') {
            const row = document.getElementById(`medication-type-${response.medication_type_id}-item`);
            Alpine.store("toastManager").addToast("Medication Type Deleted", "Medication Type has been deleted successfully", "default", "info");
            if (row) {
                row.remove();
            }
            document.getElementById("medication_type_delete_modal").close();
        }
    }
}, { once: true });
document.body.addEventListener('closeMedicationTypeCreateModal', function () {
    document.getElementById('medication_type_create').close();
}, { once: true });

document.body.addEventListener("updateMedicationTypesTable", function (event) {
    const tableBody = document.querySelector("#medicationTypesTableBody");
    Alpine.store('toastManager').addToast("Medication Type Created", "Medication Type has been created successfully", "success");
    tableBody.insertAdjacentHTML("beforeend", event.detail.html);
}, {once: true});
