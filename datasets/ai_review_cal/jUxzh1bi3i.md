- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6
Now I have a thorough understanding of the paper and all review inputs. Let me construct the consolidated review.

## Summary

GlobalTomo introduces the first large-scale 3D global synthetic seismic dataset designed for ML-based wavefield modeling and full-waveform inversion (FWI). The dataset spans three tiers of increasing complexity (Acoustic, Elastic, Real Earth) using spherical-harmonic parameterization up to degree 8, with realistic source variations. Baseline experiments on the smaller tiers demonstrate that ML forward models achieve dramatic speedups (≈60,000×) over numerical solvers and can be used within iterative inversion workflows with multiple starting points.

## Strengths

1. **First large-scale global synthetic seismic dataset tailored for ML**: The paper fills a real gap — existing FWI benchmarks (e.g., OpenFWI) are limited to subsurface exploration scales. GlobalTomo spans from 1-km radius (20 Hz) to full Earth radius (30 s period) and includes 10,000–30,000 samples per tier with both wavefield and seismogram outputs (Table 1). This is a concrete, well-motivated resource for the community.

2. **Physically grounded dataset design**: The use of spherical harmonics up to degree 8 is justified by spectral analysis of real tomographic models (citing Meschede & Romanowicz 2015, Ritsema et al. 2020), and the perturbation range (±10%) mirrors observed heterogeneity. The three-tier structure (Acoustic → Elastic → Real Earth) provides a natural progression of complexity. This design is described in sufficient detail to be reproducible.

3. **Demonstrated ML speed advantage for forward modeling**: Section 3.2.1 reports 1–3 ms inference on a single GPU vs. 120 s with 24 CPU cores for the numerical solver. The paper acknowledges the comparison is not perfectly apples-to-apples ("the acceleration rate may vary with the degree of parallelism") but the qualitative speedup is substantial and relevant to the FWI bottleneck the paper targets.

4. **Iterative inversion with multiple starting points**: Section 3.2.2 shows that using the ML forward model enables 200 gradient-based iterations with up to 1,000 random starting points, and that increasing the number of starting points monotonically improves inversion correlation (Figure 5). This directly addresses the ill-posedness and local-minima challenges that constrain traditional FWI.

5. **Comprehensive baseline comparisons**: Table 2 reports RL2 and R metrics (with standard deviations) and inference times for four baselines (MM, MLP, H-Fourier, DeepONet) on both Acoustic and Elastic tiers, enabling direct comparison of vector-based and point-based approaches.

## Weaknesses

### Fatal
None.

### Major

1. **The Real Earth tier — the tier that gives the dataset its "global" significance — is completely absent from all experiments.** The paper's introduction and title frame the contribution around *global* seismic wavefield modeling and FWI, and the Real Earth tier (PREM background, 5,427 structural parameters, 6,000 s seismograms) is the tier that corresponds to this claim. Yet every baseline in Table 2, every inversion experiment in Section 3.2.2, and every complexity analysis is confined to the Acoustic and Elastic tiers (both <1 km scale, 3 s time windows). No figure, table, or quantitative result involves the Real Earth tier. For a dataset paper, failing to demonstrate that the most important tier is usable by the target community is a significant evidential gap. The computational cost is high (~100,000 CPU hours), but even a single limited experiment on this tier would substantially strengthen the paper.

2. **ML-based inversion is evaluated without comparison to a traditional numerical FWI baseline.** Section 3.2.2 shows that gradient-based optimization using an ML forward model can improve the correlation between inverted and true structures, and that multiple starting points help. But the paper never asks: how well would a conventional adjoint-based FWI solver perform on these same synthetic structures with a comparable number of iterations? Without this anchor, we cannot assess whether the ML approach is genuinely overcoming the limitations of traditional FWI (as claimed in the abstract) or simply succeeding on a problem that is well-posed by design (due to the low-degree spherical-harmonic parameterization).

3. **The abstract claims that ML methods "overcome" the limitations of global FWI, but the experiments do not support claims about *global* FWI specifically.** The abstract states: "we illustrate that ML approaches are particularly suitable for global FWI, overcoming its limitations with rapid forward modeling and flexible inversion strategies." However, the forward modeling and inversion experiments are conducted on the small-scale Acoustic and Elastic tiers. The speed advantage and multi-start strategy are demonstrated, but these demonstrations are on simplified, non-global settings. The gap between "local-scale acoustic inversion with an MLP" and "global full-waveform inversion" is substantial and unaddressed by the evidence.

### Minor

1. **No cross-tier generalization experiments.** The paper notes that the dataset's "scope varies from a local scale of 1-km radius … to a global scale" and suggests the tiers support training at one scale and applying at another, but no experiment tests whether models trained on the Acoustic tier transfer to the Elastic or Real Earth tiers. This limits the paper's ability to support claims about multi-scale applicability.

2. **The higher-temporal-resolution experiment (Section 3.2.1, Figure 4c) is conducted on a single uniform velocity structure with acoustic waves using DeepONet.** While the result that physics constraints improve temporal generalization is interesting, a single uniform-structure test is too narrow to support general conclusions about temporal generalization across the diverse velocity structures in the dataset.

3. **The 60,000× speedup ratio, while qualitatively meaningful, compares 24 CPU cores to a single GPU without controlling for hardware generational differences.** The paper does acknowledge this ("the acceleration rate may vary with the degree of parallelism"), but the specific factor is used prominently and could mislead readers who do not notice the caveat.

4. **Inversion results lack error bars or variance estimates.** The gradient-based optimization reports correlation values without standard deviation across test structures, and the direct inversion mapping reports a single average R=0.826 with no measure of variability. Table 2 includes standard deviations for forward modeling, and this practice should be carried through to inversion results.

5. **Direct inversion mapping (R=0.826) is reported without a simple non-ML baseline** (e.g., linear regression or a traditional tomographic back-projection on the same data). While the MM baseline provides a naive reference for forward modeling, no comparable reference is provided for inversion, making it difficult to contextualize the reported correlation.

### Trivial
None.

## Nice-to-Haves

- An experiment applying at least one baseline (e.g., an MLP or FNO) to a subset of the Real Earth tier, even if only for forward modeling (not inversion), would significantly strengthen the paper's core claim.
- A comparison with a few iterations of traditional numerical FWI on the same acoustic test structures (using the AxiSEM3D solver's adjoint capabilities) would provide an important reference point for the inversion results.
- Reporting inversion results with confidence intervals or standard deviations across test structures would improve reproducibility.

## Removed Points

These points were raised by reviewers but are removed as they are inaccurate, speculative, or violate the filtering rules:

1. **"Section 2.2 does not discuss whether degree 8 resolution is sufficient"** — Removed because the paper explicitly addresses this: "spectrum analysis indicates that the significant power predominantly resides at lower degrees … our choice to limit structural parameterization to degree 8 … effectively captures the predominant long-wavelength heterogeneity." The paper justifies this choice with citations.

2. **"Missing data licensing, download location, file format" / "Missing appendix sections"** — Removed per policy. The paper references appendix sections (e.g., \cref{sec:config}, \cref{sec:models}, \cref{sec:constraints}) that are stripped by PDF parsing; these exist in the original submission.

3. **"Not yet released / cannot be independently verified" type reproducibility concerns** — Removed per policy. All cited models, benchmarks, and tools are assumed to exist.

4. **Generic area-of-concern speculations** (e.g., "could metric be measuring a proxy," "are confounders controlled") — Removed for lacking a specific textual anchor in the paper. These are category-driven noise from the review task structure, not grounded criticisms.

5. **Strength Finder's generic strengths** (e.g., "addressed an important problem," "targeted an interesting question") — Removed as superficial. The specific, evidence-backed strengths are retained above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Run at least one forward modeling baseline on the Real Earth tier.** This is the single most impactful addition. Even a limited experiment (e.g., training an MLP on 1,000 Real Earth samples and reporting wavefield prediction error) would connect the paper's experiments to its "global" framing.

2. **Add a traditional FWI baseline for the inversion experiments.** Run a few iterations of adjoint-based inversion using the numerical solver on the same Acoustic-tier test structures and report the resulting correlation. This directly addresses whether ML is providing a genuine advantage or merely succeeding on a simplified problem.

3. **Revise the abstract's strongest claims.** Replace "overcoming its limitations" with a more measured statement such as "demonstrating potential to address key computational bottlenecks" or "illustrating the feasibility of ML-driven approaches for accelerating key components." The dataset contribution is strong enough to stand on its own without overclaiming.

4. **Test cross-tier transfer** in a simple form: train on the Acoustic tier, evaluate on the Elastic tier (or vice versa), and report the performance gap relative to within-tier performance. This would provide initial evidence about how the tiers relate.
