import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        ticker = "AllUSA"
        browser = await p.chromium.launch()
        browser._defaultViewport = {"width": 1200, "height": 1000} # Increase viewport height so that more stocks are visible
        page = await browser.new_page()
        url = f"https://www.tradingview.com/heatmap/stock/?color=change&dataset={ticker}&group=sector&size=market_cap_basic&theme=dark"
        await page.goto(url, wait_until="networkidle") # Wait for most background tasks to be done
        x_button = await page.query_selector(".tv-dialog__close")
        if x_button is not None:
            await x_button.click()
        heatmap_top_bar = await page.query_selector('div[class^="heatmapTopBar"]')
        heatmap = await page.query_selector("canvas")
        full_box = bar_box = await heatmap_top_bar.bounding_box()
        heatmap_box = await heatmap.bounding_box()
        full_box["height"] += heatmap_box["height"]
        await page.screenshot(path=f"heatmap.png", clip=full_box)
        await page.close()
        await browser.close()
        
        print(f"Screenshot saved successfully: {os.path.exists('heatmap.png')}")

asyncio.run(main())