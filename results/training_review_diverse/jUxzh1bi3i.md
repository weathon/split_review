Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper introduces GlobalTomo, the first 3D global synthetic seismic dataset designed for ML-based full-waveform modeling and inversion. It comprises three tiers of increasing complexity (Acoustic, Elastic, Real Earth) with 10,000–30,000 samples each, generated using AxiSEM3D with spherical-harmonic parameterization up to degree 8. The paper demonstrates ML baselines (MM, MLP, H-Fourier Net, DeepONet) for forward modeling on the Acoustic and Elastic tiers, achieving ~60,000× speedup over numerical simulation, and showcases inversion strategies (gradient-based optimization with multiple starting points, direct mapping) on the Acoustic tier.

## Strengths

- **First 3D global synthetic dataset for ML seismic tomography.** GlobalTomo fills a genuine and important gap — existing open-FWI datasets (OpenFWI, etc.) are limited to exploration-scale (subsurface) scenarios. The three-tier structure (Acoustic, Elastic, Real Earth) with 50,000 total samples spanning from 1-km/20 Hz to global/30-second scales is a valuable community resource (Section 2, Table 1).

- **~60,000× speedup of ML forward modeling over numerical simulation.** The paper quantifies that AxiSEM3D requires 120 seconds on 24 CPU cores, while the trained MLP produces predictions in 1–3 ms on a single GPU (Section 3.2.1, Fig. 4b). This acceleration is the central enabler for the inversion strategies explored and is convincingly demonstrated.

- **ML-based inversion strategies that exploit the speedup to address traditional FWI limitations.** The paper shows that using an ML forward model enables gradient-based optimization with 200 iterations and up to 1,000 random starting points, with consistent improvement in model correlation — a strategy computationally prohibitive in classical FWI (Section 3.2.2, Figs. 5 & 6).

- **Realistic geophysical parameterization.** The use of real spherical harmonics up to degree 8 with ±10 % perturbations to a 1D background model (PREM for Real Earth) is geophysically principled and supported by spectral analysis from tomographic literature showing dominant power at low degrees (Section 2.2).

- **Systematic baseline comparisons.** The paper evaluates MM, MLP, H-Fourier Net, and DeepONet on both Acoustic and Elastic tiers with R² and relative L2 metrics including standard deviations (Table 2), establishing clear benchmarks.

## Weaknesses

### Fatal
None.

### Major

- **The Real Earth tier (Tier 3) is not used in any ML experiment.** The paper describes this tier as enabling "planetary-scale wave propagation" and "detailed geophysical analyses" (Section 2.2, line 60), and the abstract claims ML approaches are "particularly suitable for global FWI." Yet every baseline experiment — forward modeling (Table 2, Figs. 3 & 4), gradient-based inversion (Fig. 5), and direct mapping (Fig. 6) — is performed only on Acoustic and/or Elastic tiers. The claim that ML methods are suitable for global-scale FWI rests on evidence from orders-of-magnitude smaller scales (1-km radius, 0–3 s). Demonstrating forward modeling on even a subset of the Real Earth data would substantially strengthen the paper's core narrative.

- **Inversion experiments are limited in scope and lack baselines.** Only the Acoustic tier is inverted, using a single forward model (MLP) with no comparison to traditional numerical FWI. The paper claims that ML "effectively tackle[s] the challenges of ill-posedness and local minima" (Section 3.2.2, line 230), but this is asserted without quantifying against any classical FWI baseline — even a single example with a few numerical solver iterations would anchor the claim. The inversion is also not demonstrated on the Elastic tier, which would test the method on more realistic wave physics.

### Minor

- **PIDO is introduced as a baseline but omitted from the main comparison table.** Section 3.1 lists PIDO as one of five baseline models, yet Table 2 (the main forward modeling results) includes only MM, MLP, H-Fourier Net, and DeepONet. PIDO appears only in Fig. 4c for a qualitative temporal-resolution experiment on a single uniform model. While PIDO's purpose (physics-constrained temporal generalization) differs from the main forward modeling task, listing it as a baseline creates an expectation that should be acknowledged or the role clarified.

- **Direct inversion mapping reported without uncertainty quantification.** The direct MLP mapping from seismograms to velocity structures is reported as achieving "an average R of 0.826" (Section 3.2.2, line 234) without standard deviation or per-degree breakdown. While the qualitative visualizations (Fig. 6) are informative, the quantitative claim lacks the rigor applied to the forward modeling results in Table 2.

- **The paper's central claim about ML suitability for global FWI is somewhat over-claimed given the evidence.** The abstract states that "ML approaches are particularly suitable for global FWI" as a conclusion, but the supporting experiments are on the 1-km-scale Acoustic tier. Qualifying this as "show promise" or "demonstrate potential" would better match the presented evidence.

### Trivial
None.

## Nice-to-Haves

- A forward modeling experiment on the Real Earth tier (e.g., training one model on a subset of samples) would transform the paper from describing a potentially useful dataset to demonstrating it actually works at global scale.
- Including PIDO results with the same metrics as Table 2 (even as an appendix entry) would complete the baseline suite.
- A small comparison with traditional FWI (e.g., a few iterations of the numerical solver on one Acoustic example) would ground the claimed advantage.
- Quantitative per-degree breakdowns with error bars for the direct inversion mapping would improve reproducibility.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The dataset itself is not linked to a repository in the main text"** — Removed per hard rules: criticisms questioning the existence or availability of cited resources are not permitted. The appendix (stripped by the parsing pipeline) likely contains the link.
- **"No comparison to real tomographic models"** — The paper explicitly justifies the degree‑8 truncation with spectral analysis from the tomographic literature; this request is scope-creep beyond what a dataset paper should be expected to demonstrate.
- **"The discussion reads as speculation rather than evidence-based conclusions"** — Overstated; the Discussion section (Section 3.3) is appropriately speculative about future applications of a dataset paper.
- **"The inversion should be tested on Elastic and Real Earth tiers"** — This is a valid suggestion but is already captured in the Major weakness above; the Real Earth aspect is the crucial gap, while Elastic inversion is a nice-to-have.

## Novel Insights

The reviews do not surface an insight beyond the paper's own contributions. The key observation — that an ML forward model at ~60,000× speedup can support inversion strategies (200 iterations, 1,000 starting points) that are computationally prohibitive in classical FWI — is already clearly presented in the paper.

## Suggestions

1. **Add at least one forward-modeling experiment on the Real Earth tier.** Even training a single model (e.g., MLP or DeepONet) on 5,000 samples and evaluating on the held-out 5,000 would directly support the paper's claims about planetary-scale applicability and close the most important evidential gap.

2. **Include a baseline comparison in the inversion study.** A few L-BFGS iterations using the numerical solver on one or two Acoustic examples, reporting wall-clock time and final model correlation, would ground the claimed advantage of ML-based inversion.

3. **Clarify PIDO's role.** Either add PIDO metrics to the main forward modeling table or explicitly state that PIDO is explored only for temporal super-resolution and is not intended as a general forward-modeling baseline.

4. **Provide error bars for the direct inversion mapping.** Standard deviations or per-degree correlation coefficients would make this result more credible.

5. **Tone down the central claim.** Replace "ML approaches are particularly suitable for global FWI" with "ML approaches show significant promise for global FWI" or similar qualification that better matches the experimental scope.

## Score and Decision

This is a dataset paper with a genuine contribution. The dataset is well-designed, the simulation pipeline is sound, and the forward-modeling speedup is convincingly demonstrated. However, the experimental validation has a meaningful gap: the most distinctive data tier (Real Earth) is not used in any ML experiment, and the inversion study lacks baselines against traditional methods. These issues are real but fixable and do not invalidate the core contribution (the dataset itself). The paper is borderline but on balance warrants acceptance subject to revisions that address the Real Earth gap.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>