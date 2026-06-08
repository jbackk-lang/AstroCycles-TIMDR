c# AstroCycles‑TIMDR
[Punkt A – szybki start]

[Punkt B – dane wejściowe]

## ⚙️ Algorytmy i pipeline TIMDR

Model TIMDR (Time‑Integrated Multi‑Dimensional Resonance) analizuje cykle astronomiczne
w kilku etapach, łącząc podejście harmoniczne, fazowe i widmowe.

### 1. Generowanie warstw harmonicznych
Moduł: `algorithms/harmonic_generator.py`

- oblicza wielokrotności cykli (1×, 2×, 3×, 4× …)
- tworzy warstwy harmoniczne dla każdego obiektu
- wyznacza punkty przecięć i potencjalne węzły rezonansowe

Wynik: lista harmonicznych z parametrami fazowymi.

---
## 🧭 Diagram działania TIMDR (tekstowy)

Poniższy schemat pokazuje pełny przepływ pracy w modelu TIMDR — od danych wejściowych
do końcowej analizy rezonansów i harmonicznych.

1. **Dane wejściowe**
   - wczytanie cykli z pliku `planetary_cycles.json`
   - przygotowanie listy obiektów i ich parametrów

2. **Warstwy harmoniczne**
   - generowanie wielokrotności cykli (1×, 2×, 3×…)
   - tworzenie mapy harmonicznych dla każdego obiektu

3. **Porównanie faz**
   - obliczenie różnic fazowych między cyklami
   - identyfikacja punktów zbieżności

4. **Detekcja rezonansów**
   - sprawdzenie, czy różnica faz mieści się w progu rezonansu
   - klasyfikacja rezonansu (np. 1:1, 2:1, 3:2)

5. **Analiza wid
### 2. Detekcja rezonansów
Moduł: `algorithms/resonance_detector.py`

- porównuje fazy dwóch lub więcej cykli
- wykrywa momenty, w których różnica faz mieści się w zadanym progu
- klasyfikuje rezonanse (np. 1:1, 2:1, 3:2)

Wynik: lista zdarzeń rezonansowych z poziomem zgodności.

---

### 3. Analiza widmowa i cykliczna
Moduł: `algorithms/spectral_analysis.py`

- wykonuje analizę widmową (FFT / harmoniczną)
- identyfikuje dominujące częstotliwości
- łączy je z cyklami planetarnymi

Wynik: mapa częstotliwości i ich siły.

---

### 4. Pipeline TIMDR (pełny przepływ)

1. Wczytanie danych cyklicznych  
2. Generowanie harmonicznych  
3. Detekcja rezonansów  
4. Analiza widmowa  
5. Łączenie wyników w model TIMDR  
6. Opcjonalnie: wizualizacja (`visualization/`)

---

### 5. Wynik końcowy

Pipeline zwraca:

- wykryte rezonanse  
- listę harmonicznych  
- analizę widmową  
- strukturę fazową  
- opcjonalne wykresy i diagramy

Dzięki temu TIMDR pozwala badać zależności cykliczne i harmoniczne
w danych astronomicznych w sposób wielowymiarowy.



# AstroCycles‑TIMDR

AstroCycles‑TIMDR to narzędzie do analizy cykli harmonicznych, rezonansów i struktur fazowych w danych astronomicznych.  
Projekt opiera się na modelu TIMDR (Time‑Integrated Multi‑Dimensional Resonance), łącząc analizę widmową, harmoniczną i cykliczną.

---


## 🚀 Szybki start

### 1. Pobierz repozytorium
git clone https://github.com/jbackk-lang/AstroCycles-TIMDR.git
cd AstroCycles-TIMDR

### 2. Zainstaluj zależności
pip install -r requirements.txt

### 3. Uruchom podstawowy przykład
python examples/basic_usage.py

---

## 🧪 Minimalny przykład użycia

from timdr.algorithms.resonance_detector import detect_resonance

wynik = detect_resonance("Mars", "Jupiter")
print(wynik)

# Wynik:
# Lista wykrytych harmonicznych, poziomy rezonansu i parametry fazowe

## 📊 Wizualizacje

Projekt zawiera moduły odpowiedzialne za generowanie wykresów i diagramów
przedstawiających harmoniczne, rezonanse oraz strukturę fazową.

Wizualizacje znajdują się w katalogu:

visualization/

### Dostępne typy wizualizacji

1. **Wykresy harmonicznych**
   - przedstawiają wielokrotności cykli (1×, 2×, 3×…)
   - pokazują punkty przecięć i potencjalne węzły rezonansowe

2. **Mapa rezonansów**
   - wizualizacja momentów, w których cykle wchodzą w rezonans
   - oznaczenie poziomu zgodności (np. 1:1, 2:1, 3:2)

3. **Widmo częstotliwości**
   - analiza widmowa (FFT / harmoniczna)
   - identyfikacja dominujących częstotliwości i ich siły

4. **Diagram fazowy**
   - przedstawia różnice fazowe między cyklami
   - pozwala łatwo zauważyć synchronizacje i przesunięcia

---

### Jak uruchomić wizualizacje

Przykład:

from timdr.visualization.plotter import plot_harmonics

plot_harmonics("Mars")

# Wynik:
# Wygenerowany wykres harmonicznych dla wybranego obiektu

---

### Zapis wykresów

Większość funkcji wizualizacyjnych umożliwia:

- wyświetlenie wykresu na ekranie
- zapis do pliku PNG lub SVG
- integrację z pipeline TIMDR

---

Wizualizacje są opcjonalne, ale znacząco ułatwiają interpretację wyników
i analizę zależności między cyklami.

## 🧪 Testy i walidacja

Projekt zawiera zestaw testów jednostkowych, które pozwalają sprawdzić poprawność
działania kluczowych modułów TIMDR. Testy znajdują się w katalogu:

tests/

### Co jest testowane?

1. **Generowanie harmonicznych**
   - poprawność obliczeń wielokrotności cykli
   - zgodność wyników z oczekiwanymi wartościami

2. **Detekcja rezonansów**
   - wykrywanie momentów zbieżności faz
   - klasyfikacja rezonansów (1:1, 2:1, 3:2 itd.)

3. **Analiza widmowa**
   - identyfikacja dominujących częstotliwości
   - poprawność transformacji widmowej

4. **Pipeline TIMDR**
   - integracja wyników z poszczególnych modułów
   - spójność danych wejściowych i wyjściowych

---

### Jak uruchomić testy

W katalogu głównym projektu:

pytest

lub, jeśli pytest nie jest zainstalowany:

python -m pytest

---

### Walidacja działania

Aby upewnić się, że TIMDR działa poprawnie:

1. Uruchom testy jednostkowe  
2. Porównaj wyniki przykładowych analiz z folderu `examples/`  
3. Sprawdź wykresy generowane przez moduł `visualization/`  
4. Zweryfikuj poprawność danych wejściowych w `planetary_cycles.json`

## 🗺️ Roadmap / Plany rozwoju

Poniżej znajduje się lista funkcji i rozszerzeń planowanych w kolejnych wersjach
AstroCycles‑TIMDR. Roadmap jest aktualizowana wraz z rozwojem projektu.

### ✔️ Etap 1 — Podstawowy model TIMDR (zrealizowane)
- generowanie harmonicznych
- detekcja rezonansów
- analiza widmowa
- podstawowe wizualizacje
- testy jednostkowe

### 🔄 Etap 2 — Rozszerzenia analityczne (w trakcie)
- obsługa wielu obiektów jednocześnie (multi‑cycle resonance)
- analiza rezonansów wyższych rzędów (np. 5:3, 7:4)
- ulepszone wykresy fazowe
- eksport wyników do formatu JSON/CSV

### 🧠 Etap 3 — Modelowanie zaawansowane (planowane)
- integracja z danymi efemeryd (np. JPL Horizons)
- dynamiczne cykle zależne od czasu
- adaptacyjne progi rezonansu
- analiza nieliniowa i chaosu cyklicznego

### 🌐 Etap 4 — Interfejs i narzędzia (planowane)
- interaktywny dashboard (np. Streamlit)
- generowanie raportów PDF/HTML
- API do integracji z innymi projektami

### 🧩 Etap 5 — Moduły eksperymentalne (opcjonalne)
- analiza toroidalno‑fazowa
- modele wielowymiarowe (TIMDR‑X)
- integracja z Twoim modelem toruso‑Möbiusa

  

---

Jeśli chcesz dodać własne propozycje do roadmapy,
możesz dopisać je w tej sekcji lub otworzyć issue w repozytorium.


Testy pozwalają szybko wykryć błędy i zapewniają stabilność projektu.

## 📄 Licencja

Projekt AstroCycles‑TIMDR jest udostępniany na licencji MIT.

Poniżej znajduje się pełna treść licencji:

---

MIT License

Copyright (c) 2024 Jacek Kielich

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.

