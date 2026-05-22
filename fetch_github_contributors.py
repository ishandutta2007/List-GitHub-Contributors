import requests
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
OWNER = 'ishandutta2007'
REPO = 'Top-AI-repos'

def get_contributors(owner, repo, token=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    headers = {"Accept": "application/vnd.github+json"}
    
    # Using a Personal Access Token (PAT) is recommended to avoid rate limits
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    contributors = []
    page = 1
    
    while True:
        # The API is paginated; we fetch 100 results per page
        response = requests.get(url, headers=headers, params={'per_page': 100, 'page': page})
        
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break
            
        data = response.json()
        if not data:
            break
            
        contributors.extend(data)
        page += 1
        
    return contributors

if __name__ == "__main__":
    contributors_data = get_contributors(OWNER, REPO, ADMIN_TOKEN)
    
    if contributors_data:
        with open("contributors.txt", "w") as f:
            for contributor in contributors_data:
                f.write(contributor['login'] + "\n")
        print(f"Usernames successfully written to contributors.txt")
    else:
        print("No contributors found or an error occurred.")
