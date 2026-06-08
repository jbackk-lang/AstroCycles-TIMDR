# AstroCycles‑TIMDR

AstroCycles‑TIMDR to narzędzie do analizy cykli harmonicznych, rezonansów i struktur widmowych w danych astronomicznych.  
Projekt opiera się na modelu TIMDR (Time‑Integrated Multi‑Dimensional Resonance), łącząc analizę harmoniczną, fazową i cykliczną.

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

result = detect_resonance("Mars", "Jupiter")
print(result)

# Wynik:
# Lista wykrytych harmonicznych, poziomy rezonansu i parametry fazowe
