// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function () {
    // Attempt to retrieve the JSON-username and JSON-message-username elements
    const jsonUsernameElement = document.getElementById('json-username');
    const jsonMessageUsernameElement = document.getElementById('json-message-username');

    // Check if the elements exist and contain text content
    if (jsonUsernameElement && jsonUsernameElement.textContent) {
        try {
            // Parse the JSON content
            const id = JSON.parse(jsonUsernameElement.textContent);

            // Continue with your code using 'id'
            console.log('ID:', id);
        } catch (error) {
            console.error('Error parsing JSON for ID:', error);
        }
    } else {
        console.error('JSON-username element not found or does not contain text content.');
    }

    // Repeat the process for JSON-message-username
    if (jsonMessageUsernameElement && jsonMessageUsernameElement.textContent) {
        try {
            const messageUsername = JSON.parse(jsonMessageUsernameElement.textContent);
            // Continue with your code using 'messageUsername'
            console.log('Message Username:', messageUsername);
        } catch (error) {
            console.error('Error parsing JSON for Message Username:', error);
        }
    } else {
        console.error('JSON-message-username element not found or does not contain text content.');
    }

    // Your WebSocket code here
    const socket = new WebSocket('ws://' + window.location.host + '/ws/' + jsonUsernameElement.textContent + '/');

    socket.onopen = function (e) {
        console.log('CONNECTION ESTABLISHED');
    }

    socket.onclose = function (e) {
        console.log('CONNECTION_LOST');
    }

    socket.onerror = function (e) {
        console.log(e);
    }

    socket.onmessage = function (e) {
        console.log(e);
    }
});
