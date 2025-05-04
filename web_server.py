# web_server.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import json
import os

app = FastAPI()

URL_FILE = os.path.join(os.path.dirname(__file__), 'urls.json')

@app.get("/{slug}")
def redirect_slug(slug: str):
    """
    Redirect the short slug to the original URL.

    Args:
        slug (str): The shortened slug.

    Returns:
        RedirectResponse: 307 redirect to the original URL, or 404 error.
    """
    try:
        with open(URL_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="No shortened URLs found")

    url = data.get(slug)
    if url:
        return RedirectResponse(url=url, status_code=307)
    raise HTTPException(status_code=404, detail="Slug not found")
