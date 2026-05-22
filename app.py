from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fetch_github_contributors import get_contributors, save_to_file
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
    owner: str = Query(None),
    repo: str = Query(None)
):
    # If parameters are empty strings or None, they will fallback in the get_contributors function
    usernames = get_contributors(owner=owner or None, repo=repo or None)
    
    # Save to file as requested
    save_to_file(usernames)
    
    return {"usernames": usernames, "count": len(usernames)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
