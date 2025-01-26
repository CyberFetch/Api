# import requests
# import json
# from bs4 import BeautifulSoup

# # Headers to mimic browser behavior
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }

# def get_jumia_products(search_query):
#     search_url = f"https://www.jumia.ma/catalog/?q={search_query.replace(' ', '+')}"
#     response = requests.get(search_url, headers=headers)
    
#     if response.status_code != 200:
#         print("Failed to retrieve data")
#         return []
    
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # Extract product information
#     products = []
#     for item in soup.select('article.prd._fb'):
#         title = item.select_one('h3.name')
#         price = item.select_one('div.prc')
#         image = item.select_one('img')
        
#         image_url = image['data-src'] if image else None
        
#         if title and price and image_url:
#             product = {
#                 'title': title.get_text(strip=True),
#                 'price': price.get_text(strip=True),
#                 'image_url': image_url
#             }
#             products.append(product)
    
#     return products

# def save_to_json(data, filename="jumia_products.json"):
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)
#     print(f"Data saved to {filename}")

# # Example usage
# search_query = "chaussures-femme"
# products = get_jumia_products(search_query)

# # Save to JSON file
# save_to_json(products)




# import requests
# from bs4 import BeautifulSoup
# import json

# # Headers pour imiter un navigateur
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Connection': 'keep-alive',
#     'Upgrade-Insecure-Requests': '1'
# }


# def get_jumia_products(search_query):
#     # Construire l'URL de recherche
#     search_url = f"https://www.jumia.ma/catalog/?q={search_query.replace(' ', '+')}"
#     response = requests.get(search_url, headers=headers)
    
#     if response.status_code != 200:
#         print(f"Failed to retrieve data. Status code: {response.status_code}")
#         return []
    
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     products = []
    
#     # Extraire les informations des produits
#     for item in soup.select('article.prd'):
#         title = item.select_one('h3.name')
#         price = item.select_one('div.prc')
#         image = item.select_one('img')
#         category = item.get('data-category')  # Catégorie si disponible
#         description = title.get_text(strip=True) if title else None  # Utiliser le titre comme description simplifiée
        
#         image_url = image['data-src'] if image and 'data-src' in image.attrs else None
        
#         if title and price and image_url:
#             product = {
#                 'title': title.get_text(strip=True),
#                 'price': price.get_text(strip=True),
#                 'image_url': image_url,
#                 'category': category,
#                 'description': description
#             }
#             products.append(product)
    
#     return products

# def save_to_json(data, filename="jumia_products.json"):
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)
#     print(f"Data saved to {filename}")

# # Exemple d'utilisation
# search_query = "machine à laver"  # Rechercher les machines à laver
# products = get_jumia_products(search_query)

# # Enregistrer dans un fichier JSON
# save_to_json(products)

























# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import json

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC



# def get_jumia_products_with_selenium(search_query):
#     # Options pour exécuter sans interface graphique
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")

#     # Initialisation du driver
#     service = Service('chemin/vers/chromedriver')  # Remplacez par le chemin de ChromeDriver
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     # Charger l'URL
#     search_url = f"https://www.jumia.ma/catalog/?q={search_query.replace(' ', '+')}"
#     driver.get(search_url)

#     WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "article.prd"))
# )
#     # Scraper les données
#     products = []
#     items = driver.find_elements(By.CSS_SELECTOR, 'article.prd')  # Vérifiez le sélecteur CSS actuel
#     for item in items:
#         try:
#             title = item.find_element(By.CSS_SELECTOR, 'h3.name').text
#             price = item.find_element(By.CSS_SELECTOR, 'div.prc').text
#             image_url = item.find_element(By.CSS_SELECTOR, 'img').get_attribute('data-src')
            
#             product = {
#                 'title': title,
#                 'price': price,
#                 'image_url': image_url
#             }
#             products.append(product)
#         except Exception as e:
#             print(f"Erreur sur un élément : {e}")

#     driver.quit()
#     return products

# # Exemple d'utilisation
# search_query = "machine à laver"
# products = get_jumia_products_with_selenium(search_query)

# # Sauvegarder les données dans un fichier JSON
# with open("jumia_products.json", "w", encoding="utf-8") as file:
#     json.dump(products, file, ensure_ascii=False, indent=4)
#     print("Données sauvegardées dans jumia_products.json")




# import requests
# import json
# from bs4 import BeautifulSoup

# # Headers to mimic browser behavior
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }

# def get_jumia_products(search_query):
#     search_url = f"https://www.jumia.ma/catalog/?q={search_query.replace(' ', '+')}"
#     response = requests.get(search_url, headers=headers)
    
#     if response.status_code != 200:
#         print("Failed to retrieve data")
#         return []
    
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # Extract product information
#     products = []
#     for item in soup.select('article.prd._fb'):
#         title = item.select_one('h3.name')
#         price = item.select_one('div.prc')
#         image = item.select_one('img')
        
#         image_url = image['data-src'] if image else None
        
#         if title and price and image_url:
#             product = {
#                 'title': title.get_text(strip=True),
#                 'price': price.get_text(strip=True),
#                 'image_url': image_url
#             }
#             products.append(product)
    
#     return products

# def save_to_json(data, filename="jumia_products.json"):
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)
#     print(f"Data saved to {filename}")

# # Example usage
# search_query = "chemises hommes"
# products = get_jumia_products(search_query)

# # Save to JSON file
# save_to_json(products)


import requests
import json
from bs4 import BeautifulSoup

# Headers to mimic browser behavior
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def get_jumia_products(search_query):
    search_url = f"https://www.jumia.ma/catalog/?q={search_query.replace(' ', '+')}"
    response = requests.get(search_url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve data")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract product information
    products = []
    for item in soup.select('article.prd._fb'):
        title = item.select_one('h3.name')
        price = item.select_one('div.prc')
        image = item.select_one('img')
        description = item.select_one('div.desc')  # Assuming there is a 'desc' class for descriptions
        category = item.select_one('a.core')  # Assuming categories are linked with an 'a' tag
        product_type = item.get('data-type')  # Assuming there's a 'data-type' attribute
        
        image_url = image['data-src'] if image else None
        
        if title and price and image_url:
            product = {
                'title': title.get_text(strip=True),
                'price': price.get_text(strip=True),
                'image_url': image_url,
                'description': description.get_text(strip=True) if description else "N/A",
                'category': category.get_text(strip=True) if category else "N/A",
                'type': product_type if product_type else "N/A"
            }
            products.append(product)
    
    return products

def save_to_json(data, filename="jumia_products.json"):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")

# Example usage
search_query = "Appareils photo numériques :"
products = get_jumia_products(search_query)

# Save to JSON file
save_to_json(products)








# import requests
# import json
# from bs4 import BeautifulSoup

# # Headers pour imiter un navigateur
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Connection': 'keep-alive'
# }


# def get_aliexpress_products(search_query):
#     # Construire l'URL de recherche
#     search_url = f"https://www.aliexpress.com/wholesale?SearchText={search_query.replace(' ', '+')}"
#     response = requests.get(search_url, headers=headers)
    
#     if response.status_code != 200:
#         print(f"Failed to retrieve data. Status code: {response.status_code}")
#         return []
    
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # Extraire les informations des produits
#     products = []
#     for item in soup.select('div._3t7zg'):
#         title = item.select_one('h1._18_85').get_text(strip=True) if item.select_one('h1._18_85') else "N/A"
#         price = item.select_one('span._30jeq3').get_text(strip=True) if item.select_one('span._30jeq3') else "N/A"
#         image = item.select_one('img')
#         category = "AliExpress"  # Catégorie générique
#         description = title  # Utiliser le titre comme description simplifiée
        
#         image_url = image['src'] if image and 'src' in image.attrs else "N/A"
        
#         product = {
#             'title': title,
#             'price': price,
#             'image_url': image_url,
#             'category': category,
#             'description': description
#         }
#         products.append(product)
    
#     return products

# def save_to_json(data, filename="aliexpress_products.json"):
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)
#     print(f"Data saved to {filename}")

# # Exemple d'utilisation
# search_query = "women handbags"
# products = get_aliexpress_products(search_query)

# # Enregistrer dans un fichier JSON
# save_to_json(products)
