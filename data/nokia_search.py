from selenium.webdriver.common.by import By

URL = 'https://www.nokiaphone.com.cn/'
searchinput = (By.CSS_SELECTOR, '.search__input>input')
searchtext = '诺基亚X7'
submit = (By.CSS_SELECTOR, '.search__icon')
noresult = (By.CSS_SELECTOR, '.icon-search-empty')
clickplpproduct = (By.XPATH, '//h4[contains(text(),"Nokia/诺基亚 X7")]')
shopbtn_assert = (By.CSS_SELECTOR, '.cp-btn.cp-btn--primary.cp-btn--lg.cp-btn--lg')
