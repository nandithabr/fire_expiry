function addExtinguisher() {
    // Fetch form data
    var id = document.getElementById('id').value;
    var expiry = document.getElementById('expiry').value;
    var install = document.getElementById('install').value;
    var refill = document.getElementById('refill').value;
    var last = document.getElementById('last').value;

    // Example: Send data to server using fetch API
    fetch('your_server_endpoint', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id: id,
            expiry: expiry,
            install: install,
            refill: refill,
            last: last
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').style.display = 'block'; // Show success message
        console.log(data); // Log server response
        // Optionally, redirect to another page or perform additional actions
        // window.location.href = 'success.html';
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error adding extinguisher. Please try again.');
    });
}

function retrieveData() {
    const id = document.getElementById('fire-ext-id').value;

    fetch('/retrieve', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: id })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        if (data.message) {
            resultDiv.innerHTML = `<p>${data.message}</p>`;
        } else {
            resultDiv.innerHTML = `
                <table>
                    <tr><th>ID</th><td>${data.Id}</td></tr>
                    <tr><th>Expiry Date</th><td>${data.ExpiryDate}</td></tr>
                    <tr><th>Refilling Date</th><td>${data.RefillingDate}</td></tr>
                    <tr><th>Last Refilled Date</th><td>${data.LastRefilledDate}</td></tr>
                    <tr><th>Location</th><td>${data.Location}</td></tr>
                    <tr><th>Nearby Station</th><td>${data.NearbyStation}</td></tr>
                </table>
            `;
        }
    })
    .catch(error => console.error('Error:', error));
}

