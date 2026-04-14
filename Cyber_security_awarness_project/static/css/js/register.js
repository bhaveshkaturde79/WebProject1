document.getElementById("registerForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const fullname = document.getElementById("fullname").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const errorMsg = document.getElementById("errorMsg");

    errorMsg.textContent = "";

    if (!fullname ||  !email ||  !password || !confirmPassword) {
        errorMsg.textContent = "Please fill all fields";
        return;
    }

    if (password !== confirmPassword) {
        errorMsg.textContent = "Passwords do not match";
        return;
    }

    try {
        const response = await fetch("/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                fullname: fullname,
                email: email,
                password: password,
                confirmPassword:confirmPassword
            })
        });

        const result = await response.json();

        if (response.ok) {
            alert("Registration successful");
           window.location.href = '/awareness';
        } else {
            errorMsg.textContent = result.message;
        }

    } catch (error) {
        errorMsg.textContent = "Server error. Try again.";
        console.error(error);
    }
});
