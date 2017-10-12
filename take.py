# coding: utf-8
import feedparser
import urllib.request
import bs4
import re

def download_img(url):
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())

    return response

def scraping_img(url):
    soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    img = soup.find_all("img")
    img_src = ""
    for tag in img:
        try:
            string_ = tag.get('alt')
            if "comic" in string_:
                img_src = tag['src']
                break
        except:
            pass

    return img_src

def detect_name(url):
    pattern = r"https?.*/(.*?)/$" 
    match = re.findall(pattern, url)
    match_ret = ""
    if match:
        match_ret = match[0]
    else:
        print("nothing")

    return match_ret

def save_img(url, filename):
    res = download_img(url)
    f = open("/home/komekome09/Dropbox/pic/素材/popute/" + filename + ".jpg", 'wb')
    f.write(res.read())
    f.close()

def main():
    rss_url = "http://mangalifewin.takeshobo.co.jp/rss20.php"
    rss = feedparser.parse(rss_url)
    for entry in rss.entries:
        print(entry.title)
        if ("あいまいみー" in entry.title) or ("ポプテピピック" in entry.title):
            src = scraping_img(entry.link)
            filename = detect_name(entry.link)
            save_img(src, filename)
            print("🎉")

        print(entry.link)

if __name__ == "__main__":
    main()
