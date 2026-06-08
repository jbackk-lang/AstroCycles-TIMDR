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
