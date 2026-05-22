from fastapi import FastAPI, Query, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fetch_github_contributors import get_contributors, save_to_file, DEFAULT_REPOS
from typing import List, Optional
import os

app = FastAPI()

# Mount static files
if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

@app.get("/api/contributors")
async def fetch_contributors(
    repos: Optional[List[str]] = Query(None)
):
    # Determine repo list
    repo_list = []
    if repos:
        for r in repos:
            if '/' in r:
                owner, repo = r.split('/', 1)
                repo_list.append((owner.strip(), repo.strip()))
    
    # Fallback to defaults if no valid repos provided
    using_defaults = False
    if not repo_list:
        repo_list = DEFAULT_REPOS
        using_defaults = True

    # Clear file first for a fresh batch
    open("contributors.txt", "w").close()

    results = []
    for owner, repo in repo_list:
        usernames = get_contributors(owner, repo)
        if usernames:
            save_to_file(usernames, append=True)
            results.append({
                "repo": f"{owner}/{repo}",
                "usernames": usernames,
                "count": len(usernames)
            })
        else:
            results.append({
                "repo": f"{owner}/{repo}",
                "usernames": [],
                "count": 0
            })

    return {"results": results, "using_defaults": using_defaults}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
