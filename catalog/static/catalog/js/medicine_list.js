// // on hx trigger medicine-deleted, add a toast message
// document.body.addEventListener("htmx:afterSwap", function (event) {
//     // Check if this event corresponds to a redirect
//     console.log("Medicine Deleted - After Swap");
//     console.log(event)
//     if (event.detail.xhr && event.detail.xhr.getResponseHeader("HX-Trigger") === "medicine-deleted") {
//         console.log("Medicine Deleted - After Redirect");
//         // Add your toast notification logic here
//         Alpine.store("toastManager").addToast(
//             "Medicine Deleted",
//             "The medicine has been successfully deleted.",
//             "default",
//             "info"
//         );
//     }
// });
