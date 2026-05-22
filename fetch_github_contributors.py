import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Default list of (owner, repo) pairs
DEFAULT_REPOS = [
    ('ishandutta2007', 'Top-AI-repos')
]
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

def get_contributors(owner, repo, token=None):
    """
    Fetches contributor usernames for a given repository.
    """
    token = token or ADMIN_TOKEN

    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    headers = {"Accept": "application/vnd.github+json"}
    
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    contributors = []
    page = 1
    
    while True:
        try:
            response = requests.get(url, headers=headers, params={'per_page': 100, 'page': page})
            if response.status_code != 200:
                print(f"Error fetching {owner}/{repo}: {response.status_code} - {response.text}")
                break
                
            data = response.json()
            if not data:
                break
                
            contributors.extend([item['login'] for item in data])
            page += 1
        except Exception as e:
            print(f"Request failed for {owner}/{repo}: {e}")
            break
        
    return contributors

def save_to_file(usernames, filename="contributors.txt", append=False):
    """Saves a list of usernames to a file, one per line."""
    if not usernames:
        return False
    
    mode = "a" if append else "w"
    with open(filename, mode) as f:
        for username in usernames:
            f.write(username + "\n")
    return True

if __name__ == "__main__":
    # Clear file first in CLI mode
    open("contributors.txt", "w").close()
    
    total_found = 0
    for owner, repo in DEFAULT_REPOS:
        print(f"Fetching contributors for {owner}/{repo}...")
        usernames = get_contributors(owner, repo)
        if usernames:
            save_to_file(usernames, append=True)
            print(f"  Added {len(usernames)} usernames.")
            total_found += len(usernames)
        else:
            print(f"  No contributors found for {owner}/{repo}.")
            
    print(f"\nTotal usernames saved to contributors.txt: {total_found}")
