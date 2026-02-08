from playwright.sync_api import sync_playwright

from .model import Browser, scrapModel


class Continente(scrapModel):
    def __init__(self, browser: Browser) -> None:
        super().__init__(browser)
        self.url = "https://www.continente.pt"
        self.urlsearch = "/pesquisa/?q="
        self.cookieName = "permitir todos"
        self.productSelector = ".product"
        self.nameSelector = ".pwc-tile--description"
        self.priceSelector = ".pwc-tile--price-primary"
        self.havebtn = True
        self.btnname = ".js-show-more-products"


if __name__ == "__main__":
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(headless=False)
        continente: Continente = Continente(browser)
        q: str = input("Qual o produto? ")
        data: dict[str, str] = continente.doAll(q)
        for nome, preco in data.items():
            print(nome, " | ", preco)

        # for nome, preco in data.items():
        #     nomeComPeso: str
        #     nometratado: list[str] = nome.split("\n")
        #     if len(nometratado) > 2:
        #         nomeComPeso = nometratado[0] + nometratado[-1]
        #     else:
        #         nomeComPeso = nometratado[0]
        #     print(nomeComPeso, " | ", preco)
