from playwright.sync_api import Browser, Locator, Page


class scrapModel:
    def __init__(self, browser: Browser) -> None:
        self.page: Page = browser.new_page()
        self.url: str = ""
        self.urlsearch: str = ""
        self.cookieName: str = ""
        self.productSelector: str = ""
        self.nameSelector: str = ""
        self.priceSelector: str = ""

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

    def search(self, query: str) -> None:
        self.page.goto(
            f"{self.url}{self.urlsearch}{query}", wait_until="domcontentloaded"
        )
        self.scrollToBottom()

    def scrollToBottom(self) -> None:
        ultima_altura = self.page.evaluate("document.body.scrollHeight")
        repeat: bool = True
        print(ultima_altura)
        while repeat:
            self.page.mouse.wheel(0, 5000)
            self.page.wait_for_timeout(3500)
            self.page.wait_for_load_state("domcontentloaded")

            nova_altura = self.page.evaluate("document.body.scrollHeight")
            print(nova_altura)
            if nova_altura == ultima_altura:
                break
            ultima_altura = nova_altura

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

    def doAll(self, q: str) -> dict[str, str]:
        self.page.goto(self.url)
        self.setup()
        self.search(query=q)
        resultados = self.getProducts()
        print(f"Limpeza feita. {len(resultados)} itens extraídos para '{q}'.")
        return resultados
