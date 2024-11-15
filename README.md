## Setup
#### Wymagane biblioteki
- openai==1.17.0
- beautifulsoup4==4.12.2
- requests==2.31.0

#### Klucz do API
Stworzyć plik `openAI_api_key.py` w którym będzie funkcja o tej samej nazwie zwracająca klucz do API openAI
<br>
<code>def openAI_api_key(): return "klucz_do_API"</code>

## Używanie
Prezentacja wygenerowanych kodów znajduje się w pliku `podglad.html`
### Główne zadanie
Aby wygenerować kod artykułu, należy uruchomić plik `main.py`, który stworzy plik `artykul.html`

#### Działanie
1. Kod pobiera treść artykułu z podanego linku
2. Artykuł jest dekodowany za pomocą BeautifulSoup, aby były poprawnie zapisane polskie znaki
3. Przygotowany tekst jest przekazywany do OpenAI wraz z zapytaniem, które nadaje mu struktury HTML
4. Artykuł wraz z tagami jest ponownie przetwarzany przez LLM w celu dodania tagów <img> i ich opisów
5. Formatowanie*
6. Gotowy kod zapisywany jest do pliku `artykul.html`

### Zadanie dodatkowe
Plik `wygeneruj_szablon.py` generuje szablon HTML zawierający CSS i JS

#### Działanie
1. Odczytywanie pliku `artykul.html`
2. Wysłanie artykułu wraz z instrukcją do OpenAI
3. Formatowanie*
4. Zapisanie szablonu do `szablon.html`


*OpenAI zwraca wiadomość jako kod zapisany w potrójnym pojedyńczym cudzysłowiu, więc trzeba go usunąć

### Uwagi
Przy każdej generacji pliku `artykul.html` mogą się nieznacznie zmienić alternatywne opisy obrazów oraz ich podpisy. Te zmiany mają taki sam przekaz lub bardzo zbliżony do wcześniejszego opisu.
Np. z "Etyka w sztucznej inteligencji" na "Etyczne wyzwania związane z AI"
<br>
Mogą się pojawić drobne zmiany w kolejności lub wartościach CSS. Komentarze też mogą ulec zmianie
<br>
Poza tymi drobnymi zmianami to program generuje za każdym razem taki sam kod
