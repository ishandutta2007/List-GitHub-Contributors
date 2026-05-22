# Project Overview
A utility to fetch and list contributors for a GitHub repository using the GitHub REST API. Features both a CLI interface and a web-based UI.

## Tech Stack
- **Backend:** Python 3.11.4, FastAPI, `requests`, `python-dotenv`
- **Frontend:** Vanilla HTML, CSS, and JavaScript
- **Server:** Uvicorn

## Architecture
- `fetch_github_contributors.py`: Core logic for interacting with the GitHub API. Supports CLI execution and modular imports.
- `app.py`: FastAPI application serving the web UI and providing a REST API endpoint.
- `static/`: Contains frontend assets (`index.html`, `style.css`, `script.js`).
- `.env`: (Required) Stores the `ADMIN_TOKEN` for authenticated requests.
- `contributors.txt`: (Generated) Contains the list of GitHub usernames, one per line. Updated automatically on every successful fetch (UI or CLI).

## Setup and Running

### Prerequisites
- Python 3.11.4
- A GitHub Personal Access Token (PAT).

### Installation
1. Install dependencies:
   ```bash
   pip install requests python-dotenv fastapi uvicorn
   ```
2. Configure environment variables:
   - Copy `.env.example` to `.env`.
   - Update `ADMIN_TOKEN` with your GitHub PAT.

### Running the Web UI
1. Start the server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://localhost:8000`.

### Running the CLI
Run the script directly to save defaults to `contributors.txt`:
```bash
python fetch_github_contributors.py
```

## Development Conventions
- **API Interaction:** Uses GitHub REST API v3 with pagination support.
- **Fallback Logic:** If owner or repo are not provided in the UI, the script falls back to hardcoded defaults in `fetch_github_contributors.py`.
- **Styling:** GitHub-inspired aesthetic using Vanilla CSS.
