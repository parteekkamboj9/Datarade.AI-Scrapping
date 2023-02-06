from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

# creating driver with chrome, maximize window, clear cooky
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()

# reading CSV and getting mcategory links in list-> category_links
count = 1
product_links = []
while True:
    url = f"https://datarade.ai/search/products?keywords=&page={count}&search_context=products&search_type=navbar&utf8=%E2%9C%93"
    driver.get(url)
    sleep(3)
    print("url->"+str(count)+"-", url)
    if count < 365:
        products = driver.find_elements(By.XPATH, '//a[@class="data-product-card__title"]')
        for product in products:
            href = product.get_attribute("href")
            product_links.append(href)
        datasets = driver.find_elements(By.XPATH, '//div[@class="dataset-card__title"]/a')
        for dataset in datasets:
            href = dataset.get_attribute("href")
            product_links.append(href)
        print(len(product_links),"------------------------------length of list")
        count += 1
        url = f"https://datarade.ai/search/products?keywords=&page={count}&search_context=products&search_type=navbar&utf8=%E2%9C%93"
    else:
        break

# creating dataframe of list (all_links)
data = {
    "link": product_links
}
df1 = pd.DataFrame(data)
sleep(0.5)

# making csv
df1.to_csv('product_links.csv', index=False)

# quit driver and close/stop all process
driver.quit()
