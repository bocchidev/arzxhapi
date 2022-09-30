import requests, json
from bs4 import BeautifulSoup as bs


def Textpro(url, text) -> dict:
    """
    Textpro scraper
    """
    try:
        headers = {"User-Agent": "GoogleBot"}
        data = requests.get(url, headers=headers)
        html = bs(data.text, "html.parser")

        def getCookie(h):
            a = h["set-cookie"]
            b = a.split(";")[0]
            return b.split("=")

        cookies = {getCookie(data.headers)[0]: getCookie(data.headers)[1]}
        token = html.find("input", {"id": "token"}).get("value")
        payload = {
            "text[]": text,
            "submit": "Go",
            "token": token,
            "build_server": "https://textpro.me",
            "build_server_id": 1,
        }
        res = requests.post(url, data=payload, headers=headers, cookies=cookies)
        reshtml = bs(res.text, "html.parser")
        restoken = reshtml.find("div", {"id": "form_value"}).get_text()
        r = json.loads(restoken)
        params = {
            "id": r["id"],
            "text[]": r["text"],
            "token": r["token"],
            "build_server": r["build_server"],
            "build_server_id": r["build_server_id"],
        }
        base = requests.get(
            "https://textpro.me/effect/create-image",
            cookies=cookies,
            headers=headers,
            params=params,
        )
        res = json.loads(base.text)
        results = {"title": html.find("title").get_text(), "url": "https://textpro.me" + res["fullsize_image"]}
        return results
    except Exception as e:
        raise e
