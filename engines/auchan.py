from playwright.sync_api import sync_playwright

from core import base_engine.BaseEngine

class AuchanEngine(BaseEngine):
    def __init__(self) -> None:
        super().__init__()
        self.selectors = {
            "product_card": ".aucproduct-name",
            "product_price": "span.price",
        }

    def test_connection(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("https://www.auchan.pt")
            print(f"Conectado a: {page.title()}")
            browser.close


if __name__ == "__main__":
    test = AuchanEngine()
    test.test_connection()
