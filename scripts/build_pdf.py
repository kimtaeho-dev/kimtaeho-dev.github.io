"""index.html을 A4 PDF(resume.pdf)로 만든다.

사용: python scripts/build_pdf.py
필요: pip install playwright && python -m playwright install chromium
"""
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "index.html"
OUT = ROOT / "resume.pdf"


def main() -> None:
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.goto(SRC.as_uri())
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(500)
        page.pdf(
            path=str(OUT),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            scale=0.82,
        )
        browser.close()
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
