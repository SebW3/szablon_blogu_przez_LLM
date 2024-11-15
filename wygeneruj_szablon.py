from openai import OpenAI
from openAI_api_key import openAI_api_key


with open("artykul.html", "r", encoding="utf-8") as file:
    artykul = file.read()

def stworz_szablon(artykul):
    client = OpenAI(api_key=openAI_api_key())
    print("Tworzenie szablonu...")
    prompt_system = "Twoim zadaniem jest stworzenie szablonu HTML dla podanego artykułu. Dodaj tytuł na górze. " \
                    "Stwórz CSS i prosty JS. Obrazy i ich podpisy muszą mieć taki sam align. " \
                    "Sekcja body ma być pusta (tam będzie artykuł). Stwórz navbar. " \
                    "Wszystkie elementy mają się znajdować w 1 pliku. Zwróć sam kod"
    messages = [{"role": "system", "content": prompt_system}, {"role": "user", "content": artykul}]

    response = client.chat.completions.create(messages=messages, model="gpt-4o-mini", temperature=0)

    artykul = response.choices[0].message.content

    return artykul.replace("```html", "").replace("```", "").strip()



szablon = stworz_szablon(artykul)

with open("szablon.html", "w", encoding="utf-8") as file:
    file.write(szablon)