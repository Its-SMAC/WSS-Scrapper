from playwright.sync_api import sync_playwright

from .model import Browser, scrapModel


class Auchan(scrapModel):
    def __init__(self, browser: Browser) -> None:
        super().__init__(browser)
        self.url = "https://www.auchan.pt"
        self.urlsearch = "/pt/pesquisa?q="
        self.cookieName = "aceitar todos os cookies"
        self.productSelector = ".auc-product"
        self.nameSelector = ".auc-product-tile__name"
        self.priceSelector = ".price .sales .value"


if __name__ == "__main__":
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(headless=False)
        auchan: Auchan = Auchan(browser)
        q: str = input("Qual o produto? ")
        data: dict[str, str] = auchan.doAll(q)
        for nome, preco in data.items():
            print(nome, " | ", preco)
