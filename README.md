# TCWT: Temporal Curvature Wave Theory

**A Scalar-tensor K-essence model proposing time as a coherent oscillation behaving as dark matter.**

## Theory Overview
Temporal Curvature Wave Theory (TCWT) suggests that the phenomena typically attributed to Dark Matter are instead the result of **temporal tension** and **curvature waves**. 

### Key Hypotheses:
1. **Coherent Oscillation:** Time is modeled not as a linear construct, but as a high-frequency coherent oscillation. 
2. **Temporal Tension:** Regions of high causal activity or "event density" generate a field-like quantity called *temporal tension* that slows the local rate of proper time.
3. **Dark Matter Emergence:** This slowing of time creates a deep gravitational potential in galactic outskirts, producing the flat rotation curves and lensing signatures typically assigned to dark matter, without requiring new particles.

## Numerical Implementation
This repository contains the tools to solve the cosmic linear anisotropy equations within the TCWT framework, built upon the **hi_class/CLASS** public code.

### Project Structure
- **/project_contents**:
  - `configs/`: Selection of `.ini` files (e.g., `tcwt_stabilized_squeeze.ini`) for different model parameters.
  - `plots/`: Visualizations of the temporal power spectrum and mass-tension ratios.
  - `scripts/`: Over 70 diagnostic Python tools for analyzing the temporal wave dynamics.

## Quick Start
To run a diagnostic script and view the wave stability:
```bash
python3 project_contents/scripts/plot_tcwt.py
