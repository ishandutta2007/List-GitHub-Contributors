# Project Overview
A utility to fetch and list contributors for multiple GitHub repositories using the GitHub REST API. Features both a CLI interface and a web-based UI with batch processing capabilities.

## Tech Stack
- **Backend:** Python 3.11.4, FastAPI, `requests`, `python-dotenv`
- **Frontend:** Vanilla HTML, CSS, and JavaScript
- **Server:** Uvicorn

## Architecture
- `fetch_github_contributors.py`: Core logic for interacting with the GitHub API. Supports single and batch repository processing.
- `app.py`: FastAPI application serving the web UI and providing a batch-aware REST API endpoint.
- `static/`: Contains frontend assets for the batch UI.
- `.env`: (Required) Stores the `ADMIN_TOKEN` for authenticated requests.
- `contributors.txt`: (Generated) Cumulative list of GitHub usernames from the latest batch. Updated via append during processing.

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
3. Enter repositories in `owner/repo` format (one per line).

### Running the CLI
Run the script to process the default list of repositories:
```bash
python fetch_github_contributors.py
```

## Development Conventions
- **Batch Processing:** Both CLI and UI support processing multiple repositories in a single run.
- **File Output:** Usernames are appended to `contributors.txt` during the batch run. The file is cleared at the start of each new batch.
- **UI Grouping:** Results in the web UI are visually grouped by repository for clarity.
- **Fallback Logic:** Uses `DEFAULT_REPOS` in `fetch_github_contributors.py` if no input is provided.
