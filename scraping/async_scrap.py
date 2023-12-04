import httpx
from parsel import Selector
import asyncio


class AsyncScraper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }
    MAIN_URL = "https://lordfilms.day/filmes/{page}"
    LINK_XPATH = '//a[@class="th-in with-mask"]/@href'
    TITLE_XPATH = '//div[@class="th-title"]/text()'
    # PLUS_URL = 'https://remanga.org'
    # IMG_XPATH = '//div[@class="img-ratio-element"]/img/@src'

    # TEMPLATE_CONTAINS_XPATH = '//a[contains(@id, "app-show-episode-title")]'

    async def async_generator(self, limit):
        for p in range(1, limit + 1):
            yield p

    async def parse_pages(self):
        async with httpx.AsyncClient(headers=self.headers) as client:
            async for p in self.async_generator(limit=5):
                if p == 1:
                    await self.get_url(
                        client=client,
                        url=self.MAIN_URL.format(
                            page=''
                        )
                    )
                else:
                    await self.get_url(
                        client=client,
                        url=self.MAIN_URL.format(
                            page=f'page/{p}/'
                        )
                    )


    async def get_url(self, client, url):
        response = await client.get(url=url)
        print("response: ", response)
        await self.scrape_responses(response)

    async def scrape_responses(self, response):
        i = 0
        list_anime = []
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).extract()
        titles = tree.xpath(self.TITLE_XPATH).extract()
        for title in titles:
            anime = {title: links[i]}
            list_anime.append(anime)
            # print(anime)
            i += 1
        print(list_anime)
        return list_anime


if __name__ == "__main__":
    scraper = AsyncScraper()
    asyncio.run(scraper.parse_pages())