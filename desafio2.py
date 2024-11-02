
import json
import pandas as pd
with open('api_response.json', 'r', encoding='utf-8') as file:
    dados = json.load(file)


ofertas = []

for key, product in dados.items():
    if key.startswith("Product:"):   # somente chaves que começam com product
        title = product.get("productName") 
        offer_link = product.get("link")  
        price_info = dados.get(f"${key}.priceRange.sellingPrice")  
        if price_info:
            price = price_info.get("lowPrice")  


            ofertas.append({
                "offer_link": offer_link,
                "image_link": product.get("image"),  
                "price": price,
                "title": title
            })

ofertas_df = pd.DataFrame(ofertas)

ofertas_df.to_csv('ofertas.csv', index=False, encoding='utf-8')

print("Dados salvos em ofertas.csv")