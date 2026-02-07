from playwright.sync_api import Browser, Locator, Page, sync_playwright

url: str = "https://www.auchan.pt/pt/homepage"


def clickCookies(page: Page, text: str):
    try:
        botao: Locator = page.get_by_role("button", name=text, exact=False)
        botao.wait_for(state="visible", timeout=5000)
        botao.click()
        print("Botão de cookies clicado!")
    except Exception as e:
        print(f"Não foi possível clicar nos cookies: {e}")


def searchProduct(page: Page, query: str):
    page.goto(f"https://www.auchan.pt/pt/pesquisa?q={query}", wait_until="networkidle")


def scroll_to_bottom(page: Page):
    ultima_altura = page.evaluate("document.body.scrollHeight")
    repeat: bool = True

    while repeat:
        page.mouse.wheel(0, 3000)
        page.wait_for_timeout(2000)

        nova_altura = page.evaluate("document.body.scrollHeight")
        if nova_altura == ultima_altura:
            break
        ultima_altura = nova_altura


def parseProducts(page: Page):
    produtos: list[Locator] = page.locator(".auc-product").all()

    print(f"\n--- Encontrei {len(produtos)} produtos ---")

    for item in produtos:
        try:
            nome = item.locator(".auc-product-tile__name").inner_text().strip()
            preco_texto = item.locator(".price .sales .value").inner_text().strip()
            print(f"Produto: {nome} | Preço: {preco_texto}")
        except Exception as e:
            print("Erro: ", e)


def getSite(pesquisa: str):
    with sync_playwright() as p:
        browser: Browser = p.firefox.launch(headless=False)
        page: Page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        clickCookies(page, "aceitar todos os cookies")
        searchProduct(page, pesquisa)
        scroll_to_bottom(page)
        page.wait_for_selector(".auc-product", timeout=10000)
        parseProducts(page)
        print(f"Título real: {page.title()}")
        page.screenshot(path="auchan_resultados.png", full_page=True)
        browser.close()


if __name__ == "__main__":
    pesquisa: str = input("Qual o produto a pesquisar? ")
    getSite(pesquisa)
