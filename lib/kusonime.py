import requests
from bs4 import BeautifulSoup as bs


def Kusonime(query) -> dict:
    """
    Kusonime scraper
    """
    try:
        results = []
        params = {"s": query, "type_post": "post"}
        _data = requests.get("https://kusonime.com/", params=params)
        _html = bs(_data.text, "html.parser")
        venz = _html.find_all("div", {"class": "venz"})
        if len(venz) <= 0:
            return False
        details = venz[0].find_all("div", {"class": "detpost"})
        if len(details) <= 0:
            return False
        for detail in details:
            base = detail.findChildren()
            title = base[0].find("a").get("title")
            url = base[0].find("a").get("href")
            data = requests.get(url)
            html = bs(data.text, "html.parser")
            lexot = html.find("div", {"class": "lexot"})
            info = lexot.find("div", {"class": "info"})
            res = {}
            if not info:
                pass
            else:
                jap = info.find("b", text="Japanese").find_parent("p").text
                gen = info.find("b", text="Genre ").find_parent("p").text
                sea = info.find("b", text="Seasons ").find_parent("p").text
                pro = info.find("b", text="Producers").find_parent("p").text
                typ = info.find("b", text="Type").find_parent("p").text
                sta = info.find("b", text="Status").find_parent("p").text
                eps = info.find("b", text="Total Episode").find_parent("p").text
                sco = info.find("b", text="Score").find_parent("p").text
                dur = info.find("b", text="Duration").find_parent("p").text
                rel = info.find("b", text="Released on").find_parent("p").text
                sd = []
                hd = []
                down = html.find("div", {"class": "smokeddl"})
                down_sd = down.find("strong", text="480P").find_parent("div")
                _sd_url = down_sd.find_all("a")
                if len(_sd_url) <= 0:
                    return False
                for sd_url in _sd_url:
                    sd.append(sd_url.get("href"))
                down_hd = down.find("strong", text="720P").find_parent("div")
                _hd_url = down_hd.find_all("a")
                for hd_url in _hd_url:
                    hd.append(hd_url.get("href"))

                def rep(text, d):
                    for i, j in d.items():
                        text = text.replace(i, j)
                    return text.strip()

                res = {
                    "title": html.find("title").text,
                    "url": html.find("meta", {"property": "og:url"}).get("content"),
                    "thumbnail": html.find("meta", {"property": "og:image"}).get(
                        "content"
                    ),
                    "description": lexot.find("strong").find_parent("p").text,
                    "info": {
                        "japanese": rep(jap, {"Japanese": "", ":": ""}),
                        "genres": rep(gen, {"Genre": "", ":": ""}),
                        "seasons": rep(sea, {"Seasons": "", ":": ""}),
                        "producers": rep(pro, {"Producers": "", ":": ""}),
                        "type": rep(typ, {"Type": "", ":": ""}),
                        "status": rep(sta, {"Status": "", ":": ""}),
                        "total_episodes": rep(eps, {"Total Episode": "", ":": ""}),
                        "scores": rep(sco, {"Score": "", ":": ""}),
                        "duration": rep(dur, {"Duration": "", ":": ""}),
                        "released_on": rep(rel, {"Released on": "", ":": ""}),
                    },
                    "download": {"sd": sd, "hd": hd},
                }
                results.append(res)
        return results
    except Exception as e:
        raise e
