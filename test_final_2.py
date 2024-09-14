
# testování hlavního nadpisu stránky
def test_busem_title(page):
    page.goto("https://www.busem.cz/")
    title = page.locator("title")
    assert title.inner_text() == "Busem.cz | ČSAD Autobusy České Budějovice"

# testování cookies
def test_busem_cookies(page):
    page.goto("https://www.busem.cz/")

    button = page.locator(".iimGdprAcceptAll")
    button.click()
    
    page.wait_for_selector("#iimGdprRoot", state="hidden")

    div = page.locator("#iimGdprRoot")
    assert div.is_visible() == False

# testování vyhledávacího pole
def test_busem_submit(page):
    page.goto("https://www.busem.cz/")
    search = page.locator('input[name="search"][placeholder="Zadejte hledaný výraz"]').nth(0)
    search.fill("rezervace jízdenek")
   
    assert page.title() == "Busem.cz | ČSAD Autobusy České Budějovice"

    button = page.locator('button[type="submit"]')
    button.click()
