# TCWT: Temporal Curvature Wave Theory  
### A Scalar–Tensor TimeWave Dark Matter Framework with Vainshtein Screening

Temporal Curvature Wave Theory (TCWT) is a scalar–tensor cosmological model in which a single scalar field \(\phi\) generates a coherent “TimeWave.”  
This oscillatory field behaves as ultra-light dark matter while modifying the growth of structure through additional friction terms.  

TCWT is constructed within **DHOST Class I**, the only surviving branch of scalar–tensor gravity compatible with the GW170817 constraint on the speed of gravitational waves.

### 🔄 Comparison: Standard Cosmology vs. TCWT

In TCWT, the TimeWave is the primary reality. It is an eternal, beginningless oscillation. Spacetime, Big Bangs, and Black Holes are secondary structures—ripples, bubbles, and knots—emerging from a wave that has always been

| Feature | Standard Big Bang ($\Lambda$CDM) | TCWT (TimeWave Theory) |
| :--- | :--- | :--- |
| **Origin of Time** | Time begins at $t=0$ (The Singularity). | **Eternal Oscillation:** The TimeWave has no beginning. |
| **The "Big Bang"** | A point of infinite density and heat. | A **High-Tension Expansion Event** in the wave. |
| **Dark Matter** | Cold, inert particles (WIMPs). | **Coherent Ripples:** High-frequency oscillations. |
| **Black Holes** | Dead-ends/Holes in spacetime. | **Knots:** Tightly wound, finite wave-structures. |
| **The Universe** | The "Everything" that began 13.8bn years ago. | A **"Chestnut"**: One of many bubbles on the wave. |
| **Future Fate** | Heat Death or Big Rip. | **Relaxation:** The knot unwinds back into the field. |
| **Information** | Potential loss in Black Holes. | **Phase-Memory:** Always preserved in the wave. |



This repository provides:
- The theoretical foundations of TCWT  
- A Vainshtein screening mechanism ensuring local viability  
- Example `.ini` files for running TCWT in **hi_class/CLASS**  
- A roadmap for numerical implementation and testing  

---

## 📘 Documentation

All documentation is located in the `docs/` directory:

- **TCWT Theory Overview**  
  [`docs/tcwt_theory.md`](docs/tcwt_theory.md)

- **Vainshtein Screening & Local Viability**  
  [`docs/tcwt_screening.md`](docs/tcwt_screening.md)

- **hi_class Integration Guide**  
  [`docs/tcwt_hi_class_integration.md`](docs/tcwt_hi_class_integration.md)

These documents explain the action, perturbation structure, screening mechanism, and how to integrate TCWT into hi_class.

---

## 🧪 Example hi_class Configuration Files

Example `.ini` files are provided in the `examples/` directory:

- **Standard TCWT cosmology run**  
  [`examples/tcwt_example.ini`](examples/tcwt_example.ini)

- **Cluster-scale Vainshtein-breaking test**  
  [`examples/tcwt_cluster_test.ini`](examples/tcwt_cluster_test.ini)

These files define:
- TCWT scalar-field parameters  
- DHOST Class I degeneracy condition (ensuring \(c_{\rm GW} = c\))  
- Vainshtein screening parameters  
- Output settings for CMB and matter power spectra  

To run:




