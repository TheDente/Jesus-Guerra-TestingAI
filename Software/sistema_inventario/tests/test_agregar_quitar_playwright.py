# tests/test_agregar_quitar_playwright.py
import pytest
from playwright.sync_api import sync_playwright

def test_agregar_quitar():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True para ocultar navegador
        context = browser.new_context(
            viewport={"width": 1094, "height": 1392}
        )
        page = context.new_page()
        page.goto("http://localhost:8000/inventario.html")

        # Reemplaza estos selectores con otros más estables si es posible
        for _ in range(2):
            page.click("css=button:nth-child(3)")

        page.click("css=button:nth-child(4)")

        for _ in range(2):
            page.click("css=button:nth-child(3)")

        page.dblclick("css=button:nth-child(3)")
        page.click("css=button:nth-child(3)")
        page.click("css=button:nth-child(4)")
        page.click("css=button:nth-child(4)")
        page.dblclick("css=button:nth-child(4)")
        page.click("css=button:nth-child(3)")
        page.click("css=button:nth-child(4)")
        page.click("css=button:nth-child(4)")
        page.dblclick("css=button:nth-child(4)")
        page.click("css=button:nth-child(4)")

        browser.close()
