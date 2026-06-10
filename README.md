# AstroCycles‑TIMDR  
### Harmoniczne cykle, rezonanse i struktury fazowe oparte na modelu TIMDR

AstroCycles‑TIMDR to narzędzie do analizy **cykli astronomicznych**, **harmonicznych**, **rezonansów** i **struktur fazowych**, oparte na modelu **TIMDR — Time‑Integrated Multi‑Dimensional Resonance**.  
Łączy analizę **widmową**, **fazową**, **cykliczną** i **harmoniczną**, tworząc spójny model wielopoziomowych zależności czasowych.

---

## 1. Jak działa TIMDR (skrót)

Model TIMDR analizuje cykle w kilku etapach:

1. **Generowanie warstw harmonicznych**  
   Moduł `harmonic_generator.py` oblicza wielokrotności cykli (1×, 2×, 3×…) i tworzy mapy harmonicznych dla każdego obiektu.  
   Źródło: [sec4]

2. **Detekcja rezonansów**  
   Moduł `resonance_detector.py` porównuje fazy cykli i wykrywa momenty, w których różnica faz mieści się w progu rezonansu (np. 1:1, 2:1, 3:2).  
   Źródło: [sec7][sec8]

3. **Analiza widmowa**  
   Moduł `spectral_analysis.py` wykonuje FFT / analizę harmoniczną i identyfikuje dominujące częstotliwości.  
   Źródło: [sec9]

4. **Pipeline TIMDR**  
   Pełny przepływ:  
   wczytanie danych → harmoniczne → rezonanse → widmo → integracja wyników → opcjonalna wizualizacja.  
   Źródło: [sec10]

5. **Wynik końcowy**  
   - lista rezonansów  
   - lista harmonicznych  
   - analiza widmowa  
   - struktura fazowa  
   - opcjonalne wykresy  
   Źródło: [sec11]

---

## 2. Szybki start

1. Pobierz repozytorium  
   ```bash
   git clone https://github.com/jbackk-lang/AstroCycles-TIMDR.git
   cd AstroCycles-TIMDR
   ```  
   Źródło: [sec14]

2. Zainstaluj zależności  
   ```bash
   pip install -r requirements.txt
   ```  
   Źródło: [sec15]
