# TCWT-TimeWave-Dark-Matter
Scalar–tensor K‑essence model where time is a coherent oscillation behaving as dark matter
# TCWT: Time‑Wave Dark Matter in a K‑essence Scalar–Tensor Framework

## Overview

This repository is for a cosmological model where **time is represented by a coherently oscillating scalar field**, and that same field behaves as a **dark‑matter–like component** at cosmological scales.

The model is technically a **minimally coupled K‑essence / P(X,Θ) scalar–tensor theory** inside standard General Relativity, with:

- a non‑canonical kinetic term,
- an axion‑like potential,
- a coherent oscillation regime that mimics cold dark matter (CDM),
- and a modified small‑scale structure behaviour compared to fuzzy dark matter (FDM).

The goal of this project is to:

1. **Implement the model in CLASS or hi\_class**,  
2. **Generate cosmological predictions** (CMB, matter power spectrum, growth of structure),  
3. **Compare its behaviour to CDM and FDM**, especially on small scales.

I’m looking for collaborators with experience in **CLASS/hi\_class, numerical cosmology, or scalar–tensor theory** who are interested in exploring this framework.

---

## The model

We work in a standard GR background with a single scalar field Θ:

\[
S = \int d^4x \sqrt{-g} \left[ \frac{M_{\rm Pl}^2}{2} R + f(X) - V(\Theta) + \mathcal{L}_m \right],
\]
where
\[
X = -\frac{1}{2} g^{\mu\nu} \partial_\mu \Theta \partial_\nu \Theta.
\]

### Kinetic term

Non‑canonical K‑essence form:
\[
f(X) = X + \frac{\beta}{M^4} X^2,
\]
with
\[
f_X = \frac{\partial f}{\partial X} = 1 + \frac{2\beta}{M^4} X,
\qquad
f_{XX} = \frac{\partial^2 f}{\partial X^2} = \frac{2\beta}{M^4}.
\]

On an FRW background:
\[
X = \frac{1}{2} \dot{\Theta}_0^2.
\]

### Potential

Axion‑like potential:
\[
V(\Theta) = m^2 f_a^2 \left( 1 - \cos\frac{\Theta}{f_a} \right).
\]

In the small‑angle regime this reduces to a quadratic potential:
\[
V(\Theta) \approx \frac{1}{2} m^2 \Theta^2,
\]
so the field undergoes coherent oscillations when \(m \gg H\), behaving like CDM on average.

---

## Perturbations and effective fluid description

For scalar perturbations, the standard K‑essence quantities are:

\[
Q_s = f_X + 2X f_{XX} = 1 + \frac{6\beta}{M^4} X,
\]
\[
c_s^2 = \frac{f_X}{f_X + 2X f_{XX}}
= \frac{1 + \dfrac{2\beta}{M^4} X}{1 + \dfrac{6\beta}{M^4} X}.
\]

Using \(X = \tfrac{1}{2} \dot{\Theta}_0^2\):
\[
c_s^2 = \frac{1 + \dfrac{\beta}{M^4} \dot{\Theta}_0^2}
             {1 + 3 \dfrac{\beta}{M^4} \dot{\Theta}_0^2}.
\]

For \(\beta > 0\), we have \(c_s^2 < 1\), so the effective sound speed is **reduced** compared to canonical scalar fields.

In the coherent oscillation regime (\(m \gg H\)), the dispersion relation for small perturbations can be written schematically as:
\[
\omega^2 \simeq c_s^2 \frac{k^2}{a^2} + m^2
\]
at leading order, and more generally (see below) with an additional \(k^4\) “quantum pressure” term.

---

## Effective Jeans scale

By analogy with fuzzy/ultralight dark matter, we can define an effective Jeans scale. For canonical FDM, the Jeans scale is:
\[
k_J^{\rm canon} \sim \left( 16\pi G \rho\, a^4 m^2 \right)^{1/4}.
\]

In this non‑canonical model, the effective Jeans scale becomes:
\[
k_J^{\rm eff} \sim \left( \frac{16\pi G \rho\, a^4 m^2}{c_s^2} \right)^{1/4},
\]
so that:
\[
\frac{k_J^{\rm eff}}{k_J^{\rm canon}} = c_s^{-1/2}.
\]

Using the explicit form of \(c_s^2\):
\[
\frac{k_J^{\rm eff}}{k_J^{\rm canon}}
= \left(
\frac{1 + 3\dfrac{\beta}{M^4}\dot{\Theta}_0^2}
     {1 + \dfrac{\beta}{M^4}\dot{\Theta}_0^2}
\right)^{1/4}.
\]

For \(\beta > 0\), this implies:
- \(c_s^2 < 1\),
- \(k_J^{\rm eff} > k_J^{\rm canon}\),

i.e. **less small‑scale suppression** than canonical fuzzy DM for the same mass \(m\). The model is therefore **more CDM‑like** in its clustering behaviour.

---

## Madelung representation and “quantum pressure”

In the oscillatory regime, we can write the field in a Madelung‑like form:
\[
\Theta(\mathbf{x}, t) = A(\mathbf{x}, t) \cos\big( m t + S(\mathbf{x}, t) \big),
\]
and perform a time‑averaging over many oscillations.

The phase \(S\) obeys a modified Hamilton–Jacobi equation:
\[
\dot{S} + \frac{f_X}{2m} (\nabla S)^2 + V_{\rm eff} + Q_{\rm TCWT} = 0,
\]
with a modified “quantum pressure” term:
\[
Q_{\rm TCWT}
= -\frac{1}{2m^{2}f_X}
\left[
\frac{\nabla^{2}\big(A\sqrt{f_X}\big)}{A\sqrt{f_X}}
\right].
\]

This leads to a dispersion relation of the form:
\[
\omega^{2} \simeq
c_s^{2}\frac{k^{2}}{a^{2}}
+ \frac{1}{f_X^{2}}\frac{k^{4}}{4m^{2}a^{4}}.
\]

Interpretation:
- The \(c_s^{2} k^{2}\) term is the **fluid‑like (K‑essence) pressure**.
- The \(k^{4}/(4m^{2}a^{4} f_X^{2})\) term is the **wave‑like (quantum pressure)**.

For \(\beta > 0\), we have \(f_X > 1\), so the quantum pressure term is **suppressed by \(1/f_X^{2}\)**. Together with \(c_s^2 < 1\), this means:

- **Fluid pressure is weaker** than in canonical FDM.
- **Quantum pressure is weaker** than in canonical FDM.

The net result is that the scalar field behaves **more like CDM** than standard fuzzy DM, while still retaining a wave‑like structure at small scales.

---

## Why this is interesting to simulate

This model:

- Lives fully inside **GR** (minimally coupled, \(c_T = 1\), GW170817‑safe).
- Uses a **single scalar field** to:
  - define a “time‑wave” (oscillating background),
  - and act as a **dark‑matter–like component** (coherent oscillations).
- Is technically a **K‑essence / P(X,Θ)** model, compatible with **hi\_class**.
- Predicts:
  - CDM‑like behaviour on large scales,
  - softened but non‑negligible small‑scale effects (vs CDM and FDM),
  - potentially interesting signatures in the matter power spectrum and halo structure.

This makes it a good candidate for:

- **Implementation in CLASS or hi\_class**,
- **Comparison with ΛCDM and FDM**,
- **Confrontation with Lyman‑α forest, small‑scale structure, and halo core data**.

---

## Collaboration goals

I am looking for collaborators who can help with one or more of:

1. **Implementing the model in CLASS or hi\_class**
   - Add the background evolution for the scalar field.
   - Add the perturbation equations using the K‑essence structure.
   - Verify stability and consistency in the code.

2. **Running cosmological simulations**
   - Compute CMB spectra, matter power spectra, growth functions.
   - Compare with ΛCDM and fuzzy DM benchmarks.
   - Explore parameter space in \(\beta, M, m, f_a\).

3. **Phenomenological analysis**
   - Study small‑scale structure (Jeans scale, halo cores, substructure).
   - Check compatibility with Lyman‑α constraints.
   - Identify potential observational signatures that distinguish TCWT from CDM and FDM.

If you are familiar with CLASS/hi\_class, scalar–tensor cosmology, or numerical simulations and would like to explore this framework, please open an issue or start a discussion.

---

## Contact

If you’re interested in collaborating, have questions about the model, or see immediate ways to improve or generalise it, please open an issue or discussion in this repository.

I’m especially keen to work with:

- cosmology PhD students,
- postdocs,
- or experienced users of CLASS/hi\_class

who are curious about alternative dark matter models and emergent time frameworks.
