from playwright.sync_api import sync_playwright

from .model import Browser, scrapModel


class Continente(scrapModel):
    def __init__(self, browser: Browser) -> None:
        super().__init__(browser)
        self.url = "https://www.continente.pt"
        self.urlsearch = "/pesquisa/?q="
        self.cookieName = "permitir todos"
        self.productSelector = ".product"
        self.nameSelector = ".ct-pdp-details"  # ".pwc-tile--description"
        self.priceSelector = ".pwc-tile--price-secondary"


if __name__ == "__main__":
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(headless=False)
        continente: Continente = Continente(browser)
        q: str = input("Qual o produto? ")
        data: dict[str, str] = continente.doAll(q)
        print(data)
