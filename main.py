import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from openAI_api_key import openAI_api_key

# pobranie tekstu ze strony
text = requests.get("https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt").content

# zamiana typu na string i odpowiednie kodowanie znaków
soup = BeautifulSoup(text, "html.parser")

print("Treść artykułu")
print(soup)

def dodaj_elementy_html(text):
    client = OpenAI(api_key=openAI_api_key())
    print("Tworzenie struktury...")
    prompt_system = "Użyj tagów HTML do stworzenia struktury tekstu. " \
                    "Zwróć fragment <body> zawierający czysty HTML, bez CSS ani JS."
    messages = [{"role": "system", "content": prompt_system}, {"role": "user", "content": text}]

    response = client.chat.completions.create(messages=messages, model="gpt-4o-mini", temperature=0)

    artykul = response.choices[0].message.content

    print("Dodawanie tagów <img>...")
    prompt_system = "Otrzymasz artykuł z tagami HTML nadającemu mu strukturę. " \
                    "Twoim zadaniem jest dodanie tagów <img> w odpowiednich miejscach, w których będzie pasowała grafika. " \
                    'Do każdego tagu dodaj atrybut src="image_placeholder.jpg" oraz ' \
                    'alt=(opis obrazka na podstawie fragmentu tekstu w którym się znajduje. Tekst zostanie użyty do wygenerowania grafiki. Każdy z tagów musi zawierać coś z AI). ' \
                    'Umieść podpisy pod grafikami używając odpowiedniego tagu HTML. Każdy obraz wraz z figcaption musi być w tagu <figure></figure>. ' \
                    'Zwróć cały kod wraz z dodanymi tagami'
    messages = [{"role": "system", "content": prompt_system}, {"role": "user", "content": artykul}]

    response = client.chat.completions.create(messages=messages, model="gpt-4o-mini", temperature=0)

    return response.choices[0].message.content



print("="*100)

artykul = dodaj_elementy_html(str(soup))
print(artykul)

# usunięcie niepotrzebnych elementów
artykul = artykul.replace("```html", "").replace("```", "")#.replace("<body>", "").replace("</body>", "").strip()

# zapisanie do pliku
with open("artykul.html", "w", encoding="utf-8") as file:
    file.write(artykul)
