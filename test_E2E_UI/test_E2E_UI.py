import asyncio
from playwright.async_api import async_playwright
from datetime import datetime


def log_m(message):
    current_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    print(f"{current_time}. {message}")

async def test_purchase(browser_name="chromium"):
    async with async_playwright() as p:
        if browser_name == "chromium":
            browser = await p.chromium.launch(headless=False)
        elif browser_name == "firefox":
            browser = await p.firefox.launch(headless=False)
        elif browser_name == "webkit":
            browser = await p.webkit.launch(headless=False)
        else:
            raise ValueError(f"Браузер не поддерживается: {browser_name}")

        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.saucedemo.com/")
        log_m("Переход на сайт выполнен успешно")

        await page.fill('input[name="user-name"]', 'standard_user')
        await page.fill('input[name="password"]', 'secret_sauce')
        log_m("Данные введены успешно")

        await page.click('input[type="submit"]')
        log_m("Авторизация прошла успешно")

        await page.wait_for_selector('.inventory_item')
        await page.wait_for_selector('button[data-test="add-to-cart-sauce-labs-backpack"]')

        await page.click('button[data-test="add-to-cart-sauce-labs-backpack"]')
        log_m("Товар добавлен в корзину")

        await page.click('a.shopping_cart_link')
        assert await page.is_visible('div.inventory_item_name:has-text("Sauce Labs Backpack")'), "Товар не найден в корзине"

        await page.click('button[data-test="checkout"]')
        await page.fill('input[data-test="firstName"]', 'Simon')
        await page.fill('input[data-test="lastName"]', 'Kashin')
        await page.fill('input[data-test="postalCode"]', '614000')
        await page.click('input[data-test="continue"]')
        await page.click('button[data-test="finish"]')
        assert await page.is_visible('h2:has-text("THANK YOU FOR YOUR ORDER")'), "Покупка не завершена успешно"
        log_m("Покупка успешно завершена")

        await browser.close()

# Запуск теста (для Safari)
asyncio.run(test_purchase())