document.getElementById('fetch-btn').addEventListener('click', async () => {
    const reposInput = document.getElementById('repos-input').value.trim();
    const statusDiv = document.getElementById('status');
    const resultsArea = document.getElementById('results-area');
    const btn = document.getElementById('fetch-btn');

    // Parse input
    const repos = reposInput.split('\n').map(r => r.trim()).filter(r => r !== '');

    // Reset UI
    statusDiv.textContent = 'Processing repositories...';
    statusDiv.style.color = 'inherit';
    resultsArea.innerHTML = '';
    btn.disabled = true;

    try {
        let url = '/api/contributors';
        if (repos.length > 0) {
            const params = new URLSearchParams();
            repos.forEach(r => params.append('repos', r));
            url += `?${params.toString()}`;
        }

        const response = await fetch(url);
        
        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        const data = await response.json();
        
        if (data.results && data.results.length > 0) {
            if (data.using_defaults) {
                const notice = document.createElement('div');
                notice.className = 'default-notice';
                notice.textContent = 'No input provided. Showing results for the default repository (ishandutta2007/Top-AI-repos).';
                resultsArea.appendChild(notice);
            }

            data.results.forEach(res => {
                const section = document.createElement('div');
                section.className = 'repo-section';

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
            });
            statusDiv.textContent = 'All batches completed successfully!';
            statusDiv.style.color = '#2ea44f';
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
