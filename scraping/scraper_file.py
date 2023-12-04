from parsel import Selector
import requests


class AnimeScraper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0 ',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }
    MAIN_URL = "https://animego.org/"
    LINK_XPATH = '//a[@class="text-nowrap"]/@href'
    TITLE_XPATH = '//a[@class="text-nowrap"]/@title'

    # PLUS_URL = 'https://www.prnewswire.com'
    # IMG_XPATH = '//div[@class="img-ratio-element"]/img/@src'

    # MAIN_URL = "https://animespirit.tv/xfsearch/%D0%B0%D0%BD%D0%B8%D0%BC%D0%B5%20%D0%BF%D1%80%D0%BE%20%D0%B4%D0%B5%D0%BC%D0%BE%D0%BD%D0%BE%D0%B2/"
    # LINK_XPATH = '//div[@class="custom-poster"]/a/@href'
    # IMG_XPATH = '//div[@class="custom-poster"]/a/img/@src'
    # SERIES_XPATH = '//div[@class="custom-label1"]/text()'

    def parse_data(self):
        i = 0
        list_anime = []
        html = requests.get(url=self.MAIN_URL, headers=self.headers).text
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_XPATH).extract()
        titles = tree.xpath(self.TITLE_XPATH).extract()
        for title in titles:
            anime = {title: links[i]}
            list_anime.append(anime)
            i += 1
        return list_anime


if __name__ == "__main__":
    scraper = AnimeScraper()
    scraper.parse_data()