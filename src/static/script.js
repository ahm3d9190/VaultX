const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Function to set the theme
const setTheme = (theme) => {
    if (theme === 'dark') {
        body.classList.remove('light-mode');
        body.classList.add('dark-mode');
    } else {
        body.classList.remove('dark-mode');
        body.classList.add('light-mode');
    }
};

// Check for saved theme in localStorage
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    setTheme(savedTheme);
} else {
    // Check for user's system preference
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    setTheme(prefersDark ? 'dark' : 'light');
}

// Event listener for the theme toggle button
themeToggle.addEventListener('click', () => {
    const currentTheme = body.classList.contains('dark-mode') ? 'dark' : 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
});

// Crypto functionality
const messageInput = document.getElementById('message-input');
const passwordInput = document.getElementById('password-input');
const encryptBtn = document.getElementById('encrypt-btn');
const decryptBtn = document.getElementById('decrypt-btn');

const callApi = async (endpoint, message, password) => {
    const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message, password }),
    });
    const data = await response.json();
    messageInput.value = data.result;
};

encryptBtn.addEventListener('click', () => {
    const message = messageInput.value;
    const password = passwordInput.value;
    callApi('/encrypt', message, password);
});

decryptBtn.addEventListener('click', () => {
    const message = messageInput.value;
    const password = passwordInput.value;
    callApi('/decrypt', message, password);
});
