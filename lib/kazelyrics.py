import requests
from bs4 import BeautifulSoup as bs


def Kazelyrics(query):
    """
    Kazelyrics scraper
    """
    try:
        results = []
        params = {"q": query}
        base = "https://kazelyrics.com/search"
        data = requests.get(base, params=params)
        html = bs(data.text, "html.parser")
        hentry = html.find_all("div", {"class": "hentry"})
        if not hentry:
            pass
        else:
            for entry in hentry:
                post = entry.find("div", {"class": "post-thumb"})
                url = post.find("a").get("href")
                image = post.find("img")
                song = requests.get(url)
                song_data = bs(song.text, "html.parser")
                song_content = song_data.find("div", {"class": "entry-content"})
                song_lyrics = (
                    song_content.find("b", text="ROMAJI:")
                    .find_parent("div", {"class": "post-body"})
                    .text
                )
                lyrics = song_lyrics.split("ROMAJI:")[1]
                res = {
                    "title": image.get("alt"),
                    "url": url,
                    "thumbnail": image.get("src"),
                    "lyrics": "ROMAJI:\n\n" + lyrics.strip(),
                }
                results.append(res)
        return results
    except Exception as e:
        raise e
