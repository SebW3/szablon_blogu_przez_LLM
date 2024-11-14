import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from openAI_api_key import openAI_api_key

# pobranie tekstu ze strony
text = requests.get("https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt").content

# zamiana typu na string i odpowiednie kodowanie znaków
soup = BeautifulSoup(text, "html.parser")

print(soup)

def dodaj_elementy_html(text):
    client = OpenAI(api_key=openAI_api_key())
    prompt_system = "Użyj tagów HTML do stworzenia struktóry tekstu. " \
                    "Zwróć fragment <body> zawierający czysty HTML, bez CSS ani JS."
    messages = [{"role": "system", "content": prompt_system}, {"role": "user", "content": text}]

    response = client.chat.completions.create(messages=messages, model="gpt-4o-mini", temperature=0)

    return response.choices[0].message.content



print("="*100)

artykul = dodaj_elementy_html(str(soup))


with open("artykul.html", "w", encoding="utf-8") as file:
    file.write(artykul)