# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.proxy import Proxy, ProxyType
# import time
# import pandas as pd
# #from selenium.webdriver.chrome.service import Service as ChromeService
# #from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options

# chrome_option=webdriver.ChromeOptions()
# browser=webdriver.Chrome(options=chrome_option)
# #browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# liste_cars = {
#     "AUDI" : 1,
#     "BMW" : 1,
#     "CITROEN" : 1, 
#     "MERCEDES" : 1,
#     "PEUGEOT" : 1,
#     "RENAULT" : 1, 
#     "VOLKSWAGEN" : 1,
#     "ALFA" : 1,
#     "ALPINE" : 1,
#     "DACIA" : 1,
#     "DS" : 1,
#     "FIAT" : 1,
#     "FORD" : 1,
#     "HYUNDAI" : 1,
#     "JAGUAR" : 1,
#     "JEEP" : 1,
#     "KIA" : 1,
#     "LAND-ROVER" : 1,
#     "LEXUS" : 1,
#     "MASERATI" : 1,
#     "MINI" : 1,
#     "NISSAN" : 1,
#     "OPEL" : 1,
#     "PORSCHE" : 1,
#     "SEAT" : 1,
#     "SUZUKI" : 1,
#     "TOYOTA" : 1,
#     "VOLVO" : 1
#     }

# browser.get("https://www.autosphere.fr/recherche?chaine=dacia&market=VO&page=10&critaire_checked[]=year&critaire_checked[]=discount&critaire_checked[]=emission_co2")

# for i,k in liste_cars.items():
#   for m in range(1,k+1): 
#      url=f"https://www.autosphere.fr/recherche?market=VO&marque[]={str(i)}&page={str(m)}&&critaire_checked[]=marque&critaire_checked[]=year&critaire_checked[]=discount&critaire_checked[]=emission_co2"
#      browser.get(url)
#      browser.delete_all_cookies()
#      elements=browser.find_elements(By.CLASS_NAME,'bloc_infos_veh_parent');
#      for j in elements:
#          link=WebDriverWait(j,100).until(EC.presence_of_element_located((By.TAG_NAME,'a')))
#          link=link.get_property("href");
#          prix = WebDriverWait(j, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'bloc_prix'))).text
#          links=[];
#          prices=[];    
#          links.append(link);prices.append(prix);
#          df=pd.DataFrame(columns=["links","prices"]);
#          df["links"]=links;df["prices"]=prices;
#          df.to_csv("link_price.csv",index=False)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# import pandas as pd

# chrome_options = webdriver.ChromeOptions()
# browser = webdriver.Chrome(options=chrome_options)

# liste_cars = {
#     "AUDI" : 1,
#     "BMW" : 1,
#     "CITROEN" : 1, 
#     "MERCEDES" : 1,
#     "PEUGEOT" : 1,
#     "RENAULT" : 1, 
#     "VOLKSWAGEN" : 1,
#     "ALFA" : 1,
#     "ALPINE" : 1,
#     "DACIA" : 1,
#     "DS" : 1,
#     "FIAT" : 1,
#     "FORD" : 1,
#     "HYUNDAI" : 1,
#     "JAGUAR" : 1,
#     "JEEP" : 1,
#     "KIA" : 1,
#     "LAND-ROVER" : 1,
#     "LEXUS" : 1,
#     "MASERATI" : 1,
#     "MINI" : 1,
#     "NISSAN" : 1,
#     "OPEL" : 1,
#     "PORSCHE" : 1,
#     "SEAT" : 1,
#     "SUZUKI" : 1,
#     "TOYOTA" : 1,
#     "VOLVO" : 1
# }
# browser.get("https://www.autosphere.fr/recherche?chaine=dacia&market=VO&page=10&critaire_checked[]=year&critaire_checked[]=discount&critaire_checked[]=emission_co2")
# browser.delete_all_cookies()

# for i, k in liste_cars.items():
#     for m in range(1, k + 1): 
#         url = f"https://www.autosphere.fr/recherche?market=VO&marque[]={str(i)}&page={str(m)}&&critaire_checked[]=marque&critaire_checked[]=year&critaire_checked[]=discount&critaire_checked[]=emission_co2"
#         browser.get(url)
#         browser.delete_all_cookies()

#         elements = browser.find_elements(By.CLASS_NAME, 'bloc_infos_veh_parent')
#         for j in elements:
#             try:
#                 prix = WebDriverWait(j, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'bloc_prix'))).text
#                 link = WebDriverWait(j, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'a'))).get_property("href")
#                 links = [];
#                 prices = [];
#                 links.append(link)
#                 prices.append(prix)

#             except Exception as e:
#                 print(f"Erreur lors de la récupération des données : {e}")
#             df = pd.DataFrame(columns=["links", "prices"])
#             df["links"] = links
#             df["prices"] = prices
#             df.to_csv("link_price.csv", index=False)

# browser.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import pandas as pd
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_option=webdriver.ChromeOptions()
browser=webdriver.Chrome(options=chrome_option)
#browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

links=[];
prices=[];
liste_cars = {
    "AUDI" : 1,
    "BMW" : 1,
    "CITROEN" : 1, 
    "MERCEDES" : 1,
    "PEUGEOT" : 1,
    "RENAULT" : 1, 
    "VOLKSWAGEN" : 1,
    "ALFA" : 1,
    "ALPINE" : 1,
    "DACIA" : 1,
    "DS" : 1,
    "FIAT" : 1,
    "FORD" : 1,
    "HYUNDAI" : 1,
    "JAGUAR" : 1,
    "JEEP" : 1,
    "KIA" : 1,
    "LAND-ROVER" : 1,
    "LEXUS" : 1,
    "MASERATI" : 1,
    "MINI" : 1,
    "NISSAN" : 1,
    "OPEL" : 1,
    "PORSCHE" : 1,
    "SEAT" : 1,
    "SUZUKI" : 1,
    "TOYOTA" : 1,
    "VOLVO" : 1
    }

browser.get("https://www.autosphere.fr/recherche?chaine=dacia&market=VO&page=10&critaire_checked[]=year&critaire_checked[]=discount&critaire_checked[]=emission_co2")

for i,k in liste_cars.items():
  for m in range(1,k+1): 
     try: 
         url=f"https://www.autosphere.fr/recherche?market=VO&marque[]={str(i)}&page={str(m)}&&critaire_checked[]=marque&critaire_checked[]=year&critaire_checked[]=discount&critaire_checked[]=emission_co2"
         browser.get(url)
         browser.delete_all_cookies()
         elements=browser.find_elements(By.CLASS_NAME,'bloc_infos_veh_parent')
         for j in elements:
             prix=WebDriverWait(j,100).until(EC.presence_of_element_located((By.CLASS_NAME,'bloc_prix'))).text
             link=WebDriverWait(j,100).until(EC.presence_of_element_located((By.TAG_NAME,'a')))
             link=link.get_property("href")
             links.append(link);prices.append(prix);
             df=pd.DataFrame(columns=["links","prices"]);
             df["links"]=links;df["prices"]=prices;
             df.to_csv("link_price.csv",index=False)
     except Exception as e:
                   print("error")