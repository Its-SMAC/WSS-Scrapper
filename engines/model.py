from playwright.sync_api import Browser, Locator, Page


class scrapModel:
    def __init__(self, browser: Browser) -> None:
        self.page: Page = browser.new_page()
        self.url = ""
        self.cookieName = ""
        self.productSelector = ""
        self.nameSelector = ""
        self.priceSelector = ""

    def setup(self) -> None:
        self.page.goto(self.url, wait_until="networkidle")
        self.cookieClick()

    def cookieClick(self) -> None:
        try:
            botao: Locator = self.page.get_by_role(
                "button", name=self.cookieName, exact=False
            )
            botao.wait_for(state="visible", timeout=5000)
            botao.click()
            print("Botão de cookies clicado!")
        except Exception as e:
            print(f"Não foi possível clicar nos cookies: {e}")

    def scrollToBottom(self) -> None:
        ultima_altura = self.page.evaluate("document.body.scrollHeight")
        repeat: bool = True

        while repeat:
            self.page.mouse.wheel(0, 4000)
            self.page.wait_for_timeout(3500)

            nova_altura = self.page.evaluate("document.body.scrollHeight")
            if nova_altura == ultima_altura:
                break
            ultima_altura = nova_altura

    def search(self, query: str) -> None:
        self.page.goto(f"{self.url}/pesquisa?q={query}", wait_until="networkidle")
        self.scrollToBottom()

    def getProducts(self) -> dict[str, str]:
        produtos: list[Locator] = self.page.locator(self.productSelector).all()
        prices: dict[str, str] = {}

        for item in produtos:
            try:
                nome = item.locator(".auc-product-tile__name").inner_text().strip()

                try:
                    preco_texto = (
                        item.locator(".price .sales .value").inner_text().strip()
                    )
                except Exception as e:
                    preco_texto = "N/D"
                    print(f"Erro ao ler preco: {e}")

                prices[nome] = preco_texto
            except Exception as e:
                print(f"Erro ao ler produto: {e}")
        return prices
