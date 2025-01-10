function showMedicineProductDeleteModal(button) {
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

document.body.addEventListener('addMedicineProductTableComponent', function (event) {
    document.getElementById("medicine_product_create_modal").close();
    const tableBody = document.querySelector("#medicineProductTableBody");
    Alpine.store('toastManager').addToast("Medicine Product Created", "Medicine Product has been created successfully", "success");
    tableBody.insertAdjacentHTML("beforeend", event.detail.html);
});

document.body.addEventListener("updateMedicineProductTable", function (event) {
    document.getElementById("medicine_product_update_modal").close();
    const path = event.target["htmx-internal-data"].path;
    const id = path.match(/\/medicine-products\/update\/(\d+)\//)[1];
    const medicineProductItem = document.getElementById(`medicine-product-${id}`);
    medicineProductItem.outerHTML = event.detail.html;
    const newMedicineProductItem = document.getElementById(`medicine-product-${id}`);
    htmx.process(newMedicineProductItem);
    Alpine.store('toastManager').addToast("Medicine Product Updated", "Medicine Product has been updated successfully", "default" , "success");
});