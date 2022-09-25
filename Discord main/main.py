import aiohttp, asyncio, bs4

Session  = aiohttp.ClientSession
Response = aiohttp.ClientResponse

class StaticScraper():

    """
        A static site webscraper
    """

    def __init__(self, session: Session) -> None:
        self.session: Session = session

    async def request(self, method: str, url: str, **kwargs) -> Response:
        return await self.session._request(method, url, **kwargs)


async def main(*args, **kwargs) -> None:
    URL = "https://your.url/"
    PAR = "html.parser"

    async with Session() as session:
        scraper = StaticScraper(session)

        resp = await scraper.request("GET", URL)
        html = await resp.text()
        soup = bs4.BeautifulSoup(html, PAR)

    print(soup.prettify())


asyncio.run(main())