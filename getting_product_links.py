from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

# creating driver with chrome, maximize window, clear cooky
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()

# reading CSV and getting cetagory links in list-> cetagory_links
df=pd.read_csv("cetagory_links.csv")
cetagory_links=df["link"].tolist()
print(len(cetagory_links),"---------------cetagory links")


count=1
product_links=[]
for url in cetagory_links:
    print('link no-------------->',str(count)+"/"+str(len(cetagory_links)))
    print(url)
    driver.get(url)
    sleep(3)
    count+=1
    try:
        if driver.find_element(By.XPATH,'//div[@class="text-right"]/input'):
            driver.find_element(By.XPATH, '//div[@class="text-right"]/input').click()
            sleep(3)

            page = 1
            while True:
                top10=driver.find_elements(By.XPATH,'//a[@class="data-product-card__title"]')
                for top1 in top10:
                    tophref=top1.get_attribute("href")
                    product_links.append(tophref)
                    print("+++",tophref)
                try:
                    print("page no---------------",str(page))
                    page+=1
                    next=driver.find_element(By.XPATH,'//a[@rel="next"]')
                    next_page=next.get_attribute("href")
                    driver.get(next_page)
                    sleep(3)
                except:
                    break
        else:
            unclicked=driver.find_elements(By.XPATH,'//a[@=class="data-product-card__title"]')
            for one in unclicked:
                href=one.get_attribute("href")
                product_links.append(href)
                print("+++",href)

        print(len(product_links),"---------------------------product links")
    except Exception as e:
        print(e)


# creating dataframe of list (all_links)
data={
    "link":product_links
}
df1=pd.DataFrame(data)
sleep(0.5)

# making csv
df1.to_csv('product_links.csv',index=False)

# quit driver and close/stop all process
driver.quit()










