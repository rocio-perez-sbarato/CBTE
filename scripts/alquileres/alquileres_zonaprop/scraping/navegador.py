from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

def crear_driver():
    options = Options()
    options.headless = True  # Cambiá a False si querés ver el navegador

    # Crear un perfil temporal con user-agent distinto
    profile = FirefoxProfile()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/115.0"
    profile.set_preference("general.useragent.override", user_agent)
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference("useAutomationExtension", False)
    profile.set_preference("media.peerconnection.enabled", False)  # A veces ayuda

    return webdriver.Firefox(firefox_profile=profile, options=options)
