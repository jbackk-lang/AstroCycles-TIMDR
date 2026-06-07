# AstroCycles-TIMDR

A geometric model of astrological cycles based on the TIMDR framework.

This project explores:
- harmonic structures,
- resonance layers,
- cycle transitions,
- geometric phase shifts,
- and multi-level periodicity.

The goal is to create a unified geometric interpretation of astrological
cycles using TIMDR principles.

---

## 📁 Project Structure

### **1. Data**
`data/planetary_cycles.json`  
Contains astronomical cycle data used for harmonic and resonance analysis.

### **2. Algorithms**
`algorithms/harmonic_generator.py`  
Generates harmonic layers and resonance nodes.

`algorithms/resonance_detector.py`  
Detects resonance events based on phase thresholds.

### **3. Diagrams**
`diagrams/harmonic_structure.md`  
Conceptual description of harmonic layers.

`diagrams/harmonic_ascii.md`  
Lightweight ASCII visualization of harmonic structure.

---

## 🔍 Purpose

This repository serves as a foundation for:
- modeling harmonic cycles,
- exploring resonance behavior,
- developing geometric interpretations of astrological systems,
- and preparing research materials for further publication.

More materials coming soon.
import unittest
from algorithms.resonance_detector import detect_resonance, next_phase

class TestResonanceDetector(unittest.TestCase):

    def test_resonance_detection(self):
        self.assertFalse(detect_resonance(0.5))
        self.assertTrue(detect_resonance(0.9))

    def test_phase_wrapping(self):
        self.assertEqual(next_phase(0.95, 0.1), 0.05)
        self.assertEqual(next_phase(0.2, 0.3), 0.5)

if __name__ == "__main__":
    unittest.main()

