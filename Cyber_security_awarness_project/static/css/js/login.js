document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const errorMsg = document.getElementById("errorMsg");

    form.addEventListener("submit", function (event) {

        event.preventDefault(); // stop form from submitting

        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();

        // // Simple validation check
        // if (email === "" || password === "") {
        //     showError("Login failed. Please enter valid details.");
        //     return;
        // }

        // Example dummy validation (you can replace with backend check)
        if (email !== "admin@gmail.com" || password !== "123456") {
            showError("Login failed. Please enter valid details.");
        }
         else {
            errorMsg.style.color = "green";
            errorMsg.textContent = "Login successful!";
            // If needed, submit form after success
            // form.submit();
        }
    });

    function showError(message) {
        errorMsg.style.color = "red";
        errorMsg.textContent = message;
    }
     setTimeout(function () {
            window.location.href = "/awareness";  // next page
        }, 2000); // 2 seconds

});

       
    