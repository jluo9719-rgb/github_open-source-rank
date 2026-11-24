import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone


def fetch_trending(days: int, limit: int = 30) -> list[dict]:
    since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    query = urllib.parse.quote(f"created:>{since}")
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page={limit}"

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "Rising-Repos-Tracker",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as resp:
        items = json.loads(resp.read().decode("utf-8")).get("items", [])

    return [
        {
            "full_name": r["full_name"],
            "html_url": r["html_url"],
            "description": r["description"] or "暂无简介",
            "stars": r["stargazers_count"],
            "forks": r["forks_count"],
            "language": r["language"] or "Other",
            "created_at": r["created_at"][:10],
            "avatar": r["owner"]["avatar_url"],
            "topics": r.get("topics", [])[:4],
        }
        for r in items
    ]


def main():
    data = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "weekly": fetch_trending(days=7),
        "monthly": fetch_trending(days=30),
    }
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"抓取完成：周榜 {len(data['weekly'])} 条，月榜 {len(data['monthly'])} 条")


if __name__ == "__main__":
    main()


