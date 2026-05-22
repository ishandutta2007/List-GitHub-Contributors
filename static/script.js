document.getElementById('fetch-btn').addEventListener('click', async () => {
    const reposInput = document.getElementById('repos-input').value.trim();
    const appendMode = document.getElementById('append-mode').checked;
    const statusDiv = document.getElementById('status');
    const resultsArea = document.getElementById('results-area');
    const btn = document.getElementById('fetch-btn');

    // Parse input
    const repos = reposInput.split('\n').map(r => r.trim()).filter(r => r !== '');

    // Reset UI
    statusDiv.textContent = 'Processing repositories...';
    statusDiv.style.color = 'inherit';
    statusDiv.style.background = 'transparent';
    resultsArea.innerHTML = '';
    btn.disabled = true;

    try {
        let url = `/api/contributors?append=${appendMode}`;
        if (repos.length > 0) {
            const params = new URLSearchParams();
            repos.forEach(r => params.append('repos', r));
            url += `&${params.toString()}`;
        }

        const response = await fetch(url);
        
        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        const data = await response.json();
        
        if (data.results && data.results.length > 0) {
            statusDiv.textContent = 'Results loaded successfully';
            statusDiv.style.color = 'var(--success)';
            statusDiv.style.background = '#e6ffec';
            
            if (data.using_defaults) {
                const notice = document.createElement('div');
                notice.className = 'default-notice';
                notice.innerHTML = '<strong>Note:</strong> No input provided. Using default repository (ishandutta2007/Top-AI-repos).';
                resultsArea.appendChild(notice);
            }

            data.results.forEach((res, index) => {
                const section = document.createElement('div');
                section.className = 'repo-section';
                section.style.opacity = '0';
                section.style.transform = 'translateY(10px)';
                section.style.transition = `all 0.3s ease ${index * 0.1}s`;

                const header = document.createElement('div');
                header.className = 'repo-header';
                header.innerHTML = `
                    <span class="repo-name">${res.repo}</span>
                    <span class="repo-count">${res.count} contributors</span>
                `;
                section.appendChild(header);

                const list = document.createElement('ul');
                if (res.usernames.length > 0) {
                    res.usernames.forEach(user => {
                        const li = document.createElement('li');
                        li.textContent = user;
                        list.appendChild(li);
                    });
                } else {
                    const li = document.createElement('li');
                    li.textContent = 'No contributors found.';
                    li.style.fontStyle = 'italic';
                    list.appendChild(li);
                }
                section.appendChild(list);
                resultsArea.appendChild(section);
                
                // Trigger animation
                setTimeout(() => {
                    section.style.opacity = '1';
                    section.style.transform = 'translateY(0)';
                }, 50);
            });
            statusDiv.textContent = 'Batch results displayed below.';
            statusDiv.style.color = 'var(--success)';
        } else {
            statusDiv.textContent = 'No data returned.';
            statusDiv.style.color = '#cf222e';
        }
    } catch (error) {
        statusDiv.textContent = `Error: ${error.message}`;
        statusDiv.style.color = '#cf222e';
    } finally {
        btn.disabled = false;
    }
});
