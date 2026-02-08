from playwright.sync_api import Browser, Locator, sync_playwright

from engines.model import scrapModel


class PingoDoce(scrapModel):
    def __init__(self, browser: Browser) -> None:
        super().__init__(browser)
        self.url = "https://www.pingodoce.pt"
        self.urlsearch = (
            "/on/demandware.store/Sites-pingo-doce-Site/default/Search-Show?q="
        )
        self.cookieName = "Aceitar todos os Cookies"
        self.productSelector = ".product"
        self.nameSelector = ".product-name-link"
        self.priceSelector = ".product-price"
        self.havebtn = True
        self.btnname = "button:has-text('Ver mais')"

    def getProducts(self) -> dict[str, str]:
        produtos: list[Locator] = self.page.locator(self.productSelector).all()
        prices: dict[str, str] = {}

        for item in produtos:
            try:
                nome: str = item.locator(self.nameSelector).inner_text().strip()
                marca: str = item.locator(".product-brand-name").inner_text().strip()

                try:
                    preco_raw: str = str(
                        item.locator(self.priceSelector).inner_text()
                    ).strip()
                    preco_texto: str = preco_raw.split("€")[0] + "\b€"
                except Exception as e:
                    preco_texto = "N/D"
                    print(f"Erro ao ler preco: {e}")

                prices[nome + " " + marca] = preco_texto
            except Exception as e:
                print(f"Erro ao ler produto: {e}")
        return prices


if __name__ == "__main__":
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(headless=False)
        continente: PingoDoce = PingoDoce(browser)
        q: str = input("Qual o produto? ")
        data: dict[str, str] = continente.doAll(q)
        for nome, preco in data.items():
            print(nome, " | ", preco)
