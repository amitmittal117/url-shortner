# 🔗 URL Shortener Microservice (MCP + Python)

This is a lightweight URL shortener microservice built using Modern Computing Platform (MCP) and Python. It demonstrates a microservice pattern using file-based storage and can later be extended with PostgreSQL, Docker, or Kubernetes.

## 🧠 Features

* Shorten any long URL to a simple slug
* Resolve shortened slugs to the original URLs
* List all URL mappings
* Summarize all shortened links (via prompt)
* Fully compatible with MCP tools (e.g. Claude, Devin, FastMCP)

## ⚙️ Tech Stack

* 🐍 Python 3.11+
* 🧠 FastMCP
* 📦 Dependency management via `uv`
* 📁 File-based storage (`urls.json`)

## 🚀 How to Run

1. Clone and install dependencies:

```bash
git clone https://github.com/your-username/url-shortener-mcp.git
cd url-shortener-mcp
uv venv
.venv/Scripts/activate # or source .venv/bin/activate on Linux/macOS
uv sync
```

2. Start the MCP server:

```bash
uv run python server.py
```

## 💡 Demo Prompts

### 📌 Shorten a URL

```json
{
  "tool": "shorten_url",
  "input": {
    "url": "https://example.com"
  }
}
```

### 🔍 Resolve a Short Slug

```json
{
  "tool": "resolve_url",
  "input": {
    "slug": "abc123"
  }
}
```

### 📋 List All URLs

```json
{
  "tool": "list_urls",
  "input": {}
}
```

### 🧾 Summarize via Prompt

```json
{
  "prompt": "summarize_urls"
}
```

## 📂 Project Structure

```
.
├── server.py        # Main MCP server with URL shortening logic
├── urls.json        # File-based storage for slug-to-URL mappings
└── pyproject.toml   # Managed by uv for dependencies
```

## 📈 Future Improvements

* Switch to PostgreSQL via `SQLModel`
* Add FastAPI web redirect endpoint
* Containerize with Docker
* Deploy via Kubernetes or MicroK8s
* Add expiration support for links

## 👤 Author

**Amit Mittal**  
Graduate Student @ California State University, Fullerton  
[LinkedIn Profile](https://www.linkedin.com/in/amitrmittal/)