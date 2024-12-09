function showMedicineProductDeleteModal(button) {
    console.log("showMedicineProductDeleteModal")
    const medicineProductName = button.getAttribute('data-medicine-product-name');
    const medicineProductPK = button.getAttribute('data-medicine-product-pk');

    const modal = document.getElementById('medicine_product_delete_modal');
    const messageElement = document.getElementById('delete_modal_message');
    const confirmDeleteButton = document.getElementById('confirm_medicine_product_delete_button');
    confirmDeleteButton.textContent = "Delete"
    messageElement.textContent = `Are you sure you want to delete "${medicineProductName}"? This action cannot be undone.`;

    confirmDeleteButton.setAttribute('hx-delete', `/medicine-products/delete/${medicineProductPK}/`);
    confirmDeleteButton.setAttribute('hx-target', 'this');
    htmx.process(confirmDeleteButton);

    modal.showModal();
}

document.body.addEventListener('htmx:afterRequest', function (event) {
    if (event.detail.elt.id === 'confirm_medicine_product_delete_button' && event.detail.xhr.status === 200) {
        const response = JSON.parse(event.detail.xhr.responseText);
        if (response.status === 'success') {
            const row = document.getElementById(`medicine-product-${response.medicine_product_pk}`);
            Alpine.store("toastManager").addToast("Medicine Product Deleted", "Medicine Product has been successfully deleted", "default", "info");
            if (row) {
                row.remove();
            }
            document.getElementById("medicine_product_delete_modal").close();
        }
    }
});