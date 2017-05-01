from selenium import webdriver
from fixture.session import SessionHelper



class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            try:
                self.wd = webdriver.Chrome(executable_path="C:\Project\Chromedriver.exe")
            except:
                self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie(executable_path="C:\Project\IEDriverServer.exe")
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
