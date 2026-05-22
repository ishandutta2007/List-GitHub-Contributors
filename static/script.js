document.getElementById('fetch-btn').addEventListener('click', async () => {
    const owner = document.getElementById('owner').value.trim();
    const repo = document.getElementById('repo').value.trim();
    const statusDiv = document.getElementById('status');
    const countSpan = document.getElementById('count');
    const listUl = document.getElementById('contributor-list');
    const btn = document.getElementById('fetch-btn');

    // Reset UI
    statusDiv.textContent = 'Fetching contributors...';
    statusDiv.style.color = 'inherit';
    listUl.innerHTML = '';
    countSpan.textContent = '0';
    btn.disabled = true;

    try {
        const url = `/api/contributors?owner=${encodeURIComponent(owner)}&repo=${encodeURIComponent(repo)}`;
        const response = await fetch(url);
        
        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        const data = await response.json();
        
        if (data.usernames && data.usernames.length > 0) {
            countSpan.textContent = data.count;
            data.usernames.forEach(user => {
                const li = document.createElement('li');
                li.textContent = user;
                listUl.appendChild(li);
            });
            statusDiv.textContent = 'Success!';
            statusDiv.style.color = '#2ea44f';
        } else {
            statusDiv.textContent = 'No contributors found.';
            statusDiv.style.color = '#cf222e';
        }
    } catch (error) {
        statusDiv.textContent = `Error: ${error.message}`;
        statusDiv.style.color = '#cf222e';
    } finally {
        btn.disabled = false;
    }
});
