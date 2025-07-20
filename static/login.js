const LOGIN_API_URL = "https://ai-website-with-assistant.onrender.com/backend/login.php";

function toggleLogin() {
    const container = document.getElementById('login-container');
    container.classList.toggle('hidden');
}

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch(LOGIN_API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action: 'login', username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("✅ Logged in as " + data.username);
            toggleLogin();
            document.getElementById('header-login').innerHTML = "👋 Hello, " + data.username + " <button onclick='logout()'>Logout</button>";
        } else {
            alert("❌ " + data.message);
        }
    });
}

function register() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch(LOGIN_API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action: 'register', username, password })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    });
}

function logout() {
    fetch(LOGIN_API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action: 'logout' })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        location.reload();
    });
}