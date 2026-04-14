
document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("resetForm");
    const message = document.getElementById("message");

    form.addEventListener("submit", function (event) {

        event.preventDefault(); // stop normal form submission

        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        if (email === "" || password === "") {
            message.style.color = "red";
            message.textContent = "Please fill all fields.";
            return;
        }

        // Success Message
        message.style.color = "green";
        message.textContent = "Password updated successfully.";

        // Redirect after 3 seconds
        setTimeout(function () {
            window.location.href = "/login";  // change this to your next page
        }, 3000);
    });

});
