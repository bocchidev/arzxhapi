import requests
from bs4 import BeautifulSoup as bs


def Otakudesu(query):
    """
    Otakudesu scraper
    """
    try:

        def rep(text, d):
            for i, j in d.items():
                text = text.replace(i, j)
            return text.strip()

        results = {}
        params = {"s": query, "post_type": "anime"}
        base = "https://otakudesu.video/"
        data = requests.get(base, params=params)
        html = bs(data.text, "html.parser")
        chivsrc = html.find("ul", {"class": "chivsrc"}).find("li")
        if not chivsrc:
            pass
        else:
            url = chivsrc.find("a").get("href")
            anime = requests.get(url)
            anime_html = bs(anime.text, "html.parser")
            anime_info = anime_html.find("div", {"class": "infozingle"})
            judul = anime_info.find("b", text="Judul").find_parent("span").text
            japanese = anime_info.find("b", text="Japanese").find_parent("span").text
            skor = anime_info.find("b", text="Skor").find_parent("span").text
            produser = anime_info.find("b", text="Produser").find_parent("span").text
            tipe = anime_info.find("b", text="Tipe").find_parent("span").text
            status = anime_info.find("b", text="Status").find_parent("span").text
            eps = anime_info.find("b", text="Total Episode").find_parent("span").text
            durasi = anime_info.find("b", text="Durasi").find_parent("span").text
            rilis = anime_info.find("b", text="Tanggal Rilis").find_parent("span").text
            studio = anime_info.find("b", text="Studio").find_parent("span").text
            genre = anime_info.find("b", text="Genre").find_parent("span").text
            info = {
                "title": rep(judul, {"Judul": "", ":": ""}),
                "japanese": rep(japanese, {"Japanese": "", ":": ""}),
                "score": rep(skor, {"Skor": "", ":": ""}),
                "producer": rep(produser, {"Produser": "", ":": ""}),
                "types": rep(tipe, {"Tipe": "", ":": ""}),
                "status": rep(status, {"Status": "", ":": ""}),
                "total_episodes": rep(eps, {"Total Episode": "", ":": ""}),
                "duration": rep(durasi, {"Durasi": "", ":": ""}),
                "release": rep(rilis, {"Tanggal Rilis": "", ":": ""}),
                "studio": rep(studio, {"Studio": "", ":": ""}),
                "genres": rep(genre, {"Genre": "", ":": ""}),
            }
            anime_episodes = anime_html.find_all("div", {"class": "episodelist"})
            batch = {}
            episode = []
            anime_batch = anime_episodes[0].find_all("li")
            anime_episode = anime_episodes[1].find_all("li")
            for anime_b in anime_batch:
                res_360p = []
                res_480p = []
                res_720p = []
                batch_url = anime_b.find("a").get("href")
                batch_data = requests.get(batch_url)
                batch_html = bs(batch_data.text, "html.parser")
                batchlink = batch_html.find("div", {"class": "batchlink"})
                batch_360 = (
                    batchlink.find("strong", text="360p MP4")
                    if batchlink.find("strong", text="360p MP4")
                    else batchlink.find("strong", text="MP4 360p")
                )
                batch_480 = (
                    batchlink.find("strong", text="480p MP4")
                    if batchlink.find("strong", text="480p MP4")
                    else batchlink.find("strong", text="MP4 480p")
                )
                batch_720 = (
                    batchlink.find("strong", text="720p MP4")
                    if batchlink.find("strong", text="720p MP4")
                    else batchlink.find("strong", text="MP4 720p")
                )
                if not batch_360:
                    pass
                else:
                    batch_360p = batch_360.find_parent("li").find_all("a")
                    for res_360 in batch_360p:
                        res_360p.append(
                            {
                                "name": res_360.text.strip(),
                                "url": res_360.get("href"),
                                "size": batch_360.find_parent("li").find("i").text,
                            }
                        )
                if not batch_480:
                    pass
                else:
                    batch_480p = batch_480.find_parent("li").find_all("a")
                    for res_480 in batch_480p:
                        res_480p.append(
                            {
                                "name": res_480.text.strip(),
                                "url": res_480.get("href"),
                                "size": batch_480.find_parent("li").find("i").text,
                            }
                        )
                if not batch_720:
                    pass
                else:
                    batch_720p = batch_720.find_parent("li").find_all("a")
                    for res_720 in batch_720p:
                        res_720p.append(
                            {
                                "name": res_720.text.strip(),
                                "url": res_720.get("href"),
                                "size": batch_720.find_parent("li").find("i").text,
                            }
                        )
                batch_downloads = {
                    "sd_360p": res_360p,
                    "sd_480p": res_480p,
                    "hd_720p": res_720p,
                }
                batch.update(
                    {
                        "url": anime_b.find("a").get("href"),
                        "upload": anime_b.find("span", {"class": "zeebr"}).text,
                        "download": batch_downloads,
                    }
                )
            for anime_e in anime_episode:
                eps_360p = []
                eps_480p = []
                eps_720p = []
                episode_url = anime_e.find("a").get("href")
                episode_data = requests.get(episode_url)
                episode_html = bs(episode_data.text, "html.parser")
                download = episode_html.find("div", {"class": "download"})
                if not download:
                    pass
                else:
                    episode_360 = (
                        download.find("strong", text="360p")
                        if download.find("strong", text="360p")
                        else download.find("strong", text="Mp4 360p")
                        if download.find("strong", text="Mp4 360p")
                        else download.find("strong", text="MP4 360p")
                    )
                    episode_480 = (
                        download.find("strong", text="480p")
                        if download.find("strong", text="480p")
                        else download.find("strong", text="Mp4 480p")
                        if download.find("strong", text="Mp4 480p")
                        else download.find("strong", text="MP4 480p")
                    )
                    episode_720 = (
                        download.find("strong", text="720p")
                        if download.find("strong", text="720p")
                        else download.find("strong", text="Mp4 720p")
                        if download.find("strong", text="Mp4 720p")
                        else download.find("strong", text="MP4 720p")
                    )
                    episode_downloads = {
                        "sd_360p": eps_360p,
                        "sd_480p": eps_480p,
                        "hd_720p": eps_720p,
                    }
                    if not episode_360:
                        pass
                    else:
                        episode_360p = episode_360.find_parent("li").find_all("a")
                        for eps_360 in episode_360p:
                            eps_360p.append(
                                {
                                    "name": eps_360.text.strip(),
                                    "url": eps_360.get("href"),
                                    "size": episode_360.find_parent("li")
                                    .find("i")
                                    .text,
                                }
                            )
                    if not episode_480:
                        pass
                    else:
                        episode_480p = episode_480.find_parent("li").find_all("a")
                        for eps_480 in episode_480p:
                            eps_480p.append(
                                {
                                    "name": eps_480.text.strip(),
                                    "url": eps_480.get("href"),
                                    "size": episode_480.find_parent("li")
                                    .find("i")
                                    .text,
                                }
                            )
                    if not episode_720:
                        pass
                    else:
                        episode_720p = episode_720.find_parent("li").find_all("a")
                        for eps_720 in episode_720p:
                            eps_720p.append(
                                {
                                    "name": eps_720.text.strip(),
                                    "url": eps_720.get("href"),
                                    "size": episode_720.find_parent("li")
                                    .find("i")
                                    .text,
                                }
                            )
                    episode.append(
                        {
                            "title": download.find("h4").text,
                            "url": episode_url,
                            "upload": anime_e.find("span", {"class": "zeebr"}).text,
                            "download": episode_downloads,
                        }
                    )
            results.update(
                {
                    "title": chivsrc.find("a").text,
                    "url": url,
                    "thumbnail": chivsrc.find("img").get("src"),
                    "info": info,
                    "batch": batch,
                    "episode": episode,
                }
            )
            return results
    except Exception as e:
        raise e
