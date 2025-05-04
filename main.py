# server.py
from mcp.server.fastmcp import FastMCP
import os
import json
import string
import random

# Create the MCP server
mcp = FastMCP("URL Shortener")

# Define the path to the local file for storing URL mappings
URL_FILE = os.path.join(os.path.dirname(__file__), 'urls.json')

def ensure_file():
    """Create the storage file if it does not exist."""
    if not os.path.exists(URL_FILE):
        with open(URL_FILE, 'w') as f:
            json.dump({}, f)

def load_urls():
    """Load the slug-to-URL mapping from the local file."""
    ensure_file()
    with open(URL_FILE, 'r') as f:
        return json.load(f)

def save_urls(data):
    """Save the updated URL mapping to the local file."""
    with open(URL_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def generate_slug(length=6):
    """Generate a random slug using alphanumeric characters."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@mcp.tool()
def shorten_url(url: str) -> str:
    """
    Generate a short slug and store the original URL.

    Args:
        url (str): The full URL to shorten.

    Return:
        str: A confirmation message with the shortened URL.
    """
    data = load_urls()
    slug = generate_slug()
    while slug in data:
        slug = generate_slug()
    data[slug] = url
    save_urls(data)
    return f"Shortened URL: http://localhost:8000/{slug}"

@mcp.tool()
def resolve_url(slug: str) -> str:
    """
    Retrieve the original URL from a slug.

    Args:
        slug (str): The short slug to resolve.

    Return:
        str: The original URL if found, else an error message.
    """
    data = load_urls()
    return data.get(slug, "Slug not found.")

@mcp.tool()
def list_urls() -> str:
    """
    Return all slug-to-URL mappings.

    Return:
        str: A string listing all mappings or an empty message.
    """
    data = load_urls()
    return json.dumps(data, indent=2) if data else "No URLs found."

@mcp.prompt()
def summarize_urls() -> str:
    """
    Prompt summary of all shortened URLs.

    Return:
        str: A summary string or message if no URLs exist.
    """
    data = load_urls()
    if not data:
        return "No URLs have been shortened yet."
    entries = "\n".join(f"{slug} → {url}" for slug, url in data.items())
    return f"Here are all shortened URLs:\n{entries}"
