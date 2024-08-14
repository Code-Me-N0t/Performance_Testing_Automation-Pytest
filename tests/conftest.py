from src.modules import *

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.execute_cdp_cmd('Performance.enable', {})

    yield driver

    driver.execute_cdp_cmd('Performance.disable', {})
    driver.quit()
