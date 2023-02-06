from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

# creating driver with chrome, maximize window, clear cooky
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()

# opening cetagory page in chrome using driver.get()
url="https://datarade.ai/data-categories/"
driver.get(url)
sleep(3)

# declaration of lists
all_links=[]

# getting all elements in a list-> all_elements
all_elements=driver.find_elements(By.XPATH,'//a[@class="categories__list-item"]')
print("total elements------------------>",len(all_elements))

# getting links from each element & adding in list
count=1
for one_elements in all_elements:
    href=one_elements.get_attribute("href")
    all_links.append(href)
    print(count,"-",href)
    count+=1


# total of cetagory links after collection
print(len(all_links),"---------------links")

# creating dataframe of list (all_links)
data={
    "link":all_links
}
df1=pd.DataFrame(data)
sleep(0.5)

# making csv
df1.to_csv('cetagory_links.csv',index=False)

# quit driver and close/stop all process
driver.quit()









