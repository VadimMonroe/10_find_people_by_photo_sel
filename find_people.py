from selenium import webdriver


def go_to_site(site: str, size: (int, int), pos: (int, int)):
    browser = webdriver.Chrome('./chromedriver_99/chromedriver')
    browser.get(site)
    browser.set_window_size(size[0], size[1])
    browser.set_window_position(pos[0], pos[1])
    return browser


browser1 = go_to_site('https://yandex.ru/images/?utm_source=main_stripe_big', (500, 300), (950, 10))
browser2 = go_to_site('https://search4faces.com/vk01/index.html', (500, 300), (950, 400))
