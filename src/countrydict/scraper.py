
import requests

from bs4 import BeautifulSoup

def build_country_dict(soup):
    country_dict = {}
    all_countries = soup.find_all("div", class_="country")

    for country in all_countries:

        name = country.find("h3", class_="country-name").text.strip()
        capital = country.find("span", class_="country-capital").text.strip()
        population = country.find("span", class_="country-population").text.strip()
        area = country.find("span", class_="country-area").text.strip()

        #print(f"name: {name}, capital: {capital}, population: {population}, area: {area}")

        country_dict[name] = {
            "Population": int(population),
            "Area": float(area),
            "Capital": capital
        }
    #print(f"{name}: {country_dict[name]}")

    return country_dict


if __name__ == "__main__":
    url = "https://www.scrapethissite.com/pages/simple/"
    resp = requests.get(url, timeout=20)
    soup = BeautifulSoup(resp.text, "html.parser")
    
    
    data = build_country_dict(soup)
    
    
    if len(data) != 250:
        print(f'''You should have found 250 countries, you found {len(data)}''')
    
    if int(data["Angola"]["Population"]) != 13068161:
        print(f'''Angola's population should be 13068161 you said it was {data["Angola"]["Population"]}''')
        
    if float(data["Israel"]["Area"]) != 20770.0:
        print(f'''Israel should have an area of 20770.0 you said it was {data["Israel"]["Area"]}''')
        
    if data["Venezuela"]["Capital"] != "Caracas":
        print(f'''Venezuela's capital should be Caracas, it was {data["Venezuela"]["Capital"]}''')

    
