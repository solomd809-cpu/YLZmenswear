import urllib.request, os

assets = r"C:\Users\14213\Doubao\chats\2026-10-05\new-chat\ylz-menswear\assets"
files = {
    "hero.jpg": "https://aka.doubaocdn.com/s/JQU2Ln1hcj",
    "factory.jpg": "https://aka.doubaocdn.com/s/J6VXfcWygY",
    "showroom.jpg": "https://aka.doubaocdn.com/s/7bUYE91VpW",
    "quality.jpg": "https://aka.doubaocdn.com/s/NovkoTvGiD",
    "cat-suits.jpg": "https://aka.doubaocdn.com/s/Dl2vFVajX0",
    "cat-shirts.jpg": "https://aka.doubaocdn.com/s/R2a5YA82jw",
    "cat-polos.jpg": "https://aka.doubaocdn.com/s/QO6W5pkUZX",
    "cat-tees.jpg": "https://aka.doubaocdn.com/s/IophFmF2VK",
    "cat-chinos.jpg": "https://aka.doubaocdn.com/s/QtKcWykhdq",
    "cat-jackets.jpg": "https://aka.doubaocdn.com/s/zV14CA1VM7",
    "cat-knitwear.jpg": "https://aka.doubaocdn.com/s/WNnmYa7qCX",
    "cat-activewear.jpg": "https://aka.doubaocdn.com/s/8NGJE5DYEL",
    "visit.jpg": "https://aka.doubaocdn.com/s/ArgNWt2MLU",
    "sourcing.jpg": "https://aka.doubaocdn.com/s/B1VIk3mra0",
}
for name, url in files.items():
    path = os.path.join(assets, name)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r, open(path, "wb") as f:
            f.write(r.read())
        size = os.path.getsize(path)
        print(name, size)
    except Exception as e:
        print(name, "ERROR", e)
