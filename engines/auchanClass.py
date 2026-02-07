from model import Browser, scrapModel


class Auchan(scrapModel):
    def __init__(self, browser: Browser) -> None:
        super().__init__(browser)
        self.url = "https://www.auchan.pt"
        self.cookieName = "aceitar todos os cookies"
        self.productSelector = ".auc-product"
        self.nameSelector = ".auc-product-tile__name"
        self.priceSelector = ".price .sales .value"

    def search(self, query: str) -> None:
        self.page.goto(f"{self.url}/pt/pesquisa?q={query}", wait_until="networkidle")
        self.scrollToBottom()
