import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
DEFAULT_OWNER = 'ishandutta2007'
DEFAULT_REPO = 'Top-AI-repos'
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

def get_contributors(owner=None, repo=None, token=None):
    """
    Fetches contributor usernames for a given repository.
    Falls back to default owner/repo if not provided.
    """
    owner = owner or DEFAULT_OWNER
    repo = repo or DEFAULT_REPO
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
                print(f"Error: {response.status_code} - {response.text}")
                break
                
            data = response.json()
            if not data:
                break
                
            contributors.extend([item['login'] for item in data])
            page += 1
        except Exception as e:
            print(f"Request failed: {e}")
            break
        
    return contributors

def save_to_file(usernames, filename="contributors.txt"):
    """Saves a list of usernames to a file, one per line."""
    if usernames:
        with open(filename, "w") as f:
            for username in usernames:
                f.write(username + "\n")
        return True
    return False

if __name__ == "__main__":
    usernames = get_contributors()
    
    if save_to_file(usernames):
        print(f"Successfully saved {len(usernames)} usernames to contributors.txt")
    else:
        print("No contributors found or an error occurred.")
