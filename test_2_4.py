def func_print(func, *args):
    func_name = func.__name__.capitalize().replace("_", " ")
    print(func_name, *args)


def open_browser(browser_name):
    func_print(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    func_print(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    func_print(find_registration_button_on_login_page, page_url, button_text)


open_browser("Chrome")
go_to_companyname_homepage("https://www.fclm.ru/")
find_registration_button_on_login_page("https://lk.fclm.ru/register", "Зарегистрироваться")