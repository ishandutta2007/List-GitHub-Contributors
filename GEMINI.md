# Project Overview
A simple Python utility to fetch and list contributors for a GitHub repository using the GitHub REST API.

## Tech Stack
- **Language:** Python 3.11.4
- **Libraries:** `requests`, `python-dotenv`

## Architecture
- `fetch_github_contributors.py`: Main script containing the logic to interact with GitHub's API, handle pagination, and save contributor usernames to a file.
- `.env`: (Required) Stores the `ADMIN_TOKEN` for authenticated requests to avoid rate limits.
- `contributors.txt`: (Generated) Contains the list of GitHub usernames, one per line.

## Setup and Running

### Prerequisites
- Python 3.11.4 (specified in `.python-version`)
- A GitHub Personal Access Token (PAT) with appropriate permissions.

### Installation
1. Install dependencies:
   ```bash
   pip install requests python-dotenv
   ```
2. Configure environment variables:
   - Copy `.env.example` to `.env`.
   - Update `ADMIN_TOKEN` with your GitHub PAT.

### Running
Run the script using:
```bash
python fetch_github_contributors.py
```
The script will fetch the contributors and save their usernames to `contributors.txt`.

## Development Conventions
- **API Interaction:** Uses GitHub REST API v3.
- **Environment Management:** Uses `python-dotenv` for local configuration.
- **Pagination:** Handles paginated results from GitHub (100 items per page).
- **Authentication:** Supports Bearer token authentication via `ADMIN_TOKEN`.
