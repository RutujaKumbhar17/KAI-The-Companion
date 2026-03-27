// chat.js - Dedicated Chat Logic
const socket = io();

// DOM Elements
const chatMessages = document.getElementById('chat-messages');
const chatInput = document.getElementById('chat-input');
const btnSend = document.getElementById('send-btn');

function appendMessage(text, sender) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', sender === 'user' ? 'user-msg' : 'bot-msg');
    msgDiv.innerText = text;
    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight; 
}

function sendChatMessage() {
    const text = chatInput.value.trim();
    if (!text) return;
    appendMessage(text, 'user');
    chatInput.value = '';
    socket.emit('chat_message', { message: text });
}

if (btnSend) {
    btnSend.addEventListener('click', sendChatMessage);
}

if (chatInput) {
    chatInput.addEventListener('keypress', (e) => { 
        if (e.key === 'Enter') sendChatMessage(); 
    });
}

socket.on('chat_response', (data) => {
    appendMessage(data.response, 'bot');
});

socket.on('ai_response', (data) => {
    // Note: In dedicated chat, we don't handle audio/avatar unless required.
    // However, if we want to play audio, we can add it here.
    if (data.audio_url) {
        const audio = new Audio(data.audio_url);
        audio.play();
    }
});
