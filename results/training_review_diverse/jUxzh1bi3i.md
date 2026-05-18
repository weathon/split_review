Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces GlobalTomo, the first 3D global synthetic seismic dataset designed for ML-driven seismic wavefield modeling and full-waveform inversion (FWI). The dataset comprises three tiers of increasing complexity — Acoustic (1 km radius, 20 Hz), Elastic (same scale with source variations), and Real Earth (full 6,371 km radius, 30 s period) — generated using the AxiSEM3D numerical solver. Velocity structures are parameterized using real spherical harmonics up to degree 8. The paper demonstrates ML baselines (MLP, HFN, DeepONet, physics-informed DeepONet) on the Acoustic and Elastic tiers, showing ~60,000× speedup for forward modeling and inversion strategies achieving meaningful structure recovery (R=0.826 for direct inversion mapping).

## Strengths

- **First comprehensive 3D global synthetic dataset for ML-driven seismic tomography.** The paper introduces a dataset that fills a genuine gap: prior datasets like OpenFWI are limited to subsurface exploration scales, while GlobalTomo spans from 1-km radius at 20 Hz to the full Earth radius at a 30-second period. The three-tier design (Acoustic, Elastic, Real Earth) with increasing physical realism is a well-thought-out contribution. The Real Earth tier alone required ~100,000 CPU hours of simulation, representing a scale unmatched by existing ML benchmark seismic datasets.

- **Efficient physics-inspired parameterization of Earth structure.** Velocity perturbations are modeled using real spherical harmonics up to degree 8, capturing dominant long-wavelength heterogeneity while keeping the parameter count tractable for inversion. The paper justifies this choice with references to spectral analyses of mantle tomographic models (citing Meschede et al., Ritsema et al.), showing that significant power resides at lower degrees. This design choice directly supports the dataset's utility for inversion tasks.

- **Demonstrated ~60,000× speedup for forward modeling with ML baselines.** Numerical forward simulation takes 120 s on 24 CPU cores, whereas trained ML models (MLP, DeepONet) run in 1–3 ms on a single GPU. This quantified acceleration is a concrete enabler for the computationally expensive iterative inversion procedures discussed in the paper.

- **ML-based inversion strategies achieve meaningful structure recovery.** The paper demonstrates three inversion approaches using the ML forward models. For direct seismogram-to-structure mapping, an MLP achieved an average correlation R=0.826 on unseen test structures. The multi-start experiments show monotonic improvement with increasing starting points, illustrating that ML's low inference cost enables more thorough search in the inversion landscape compared to computationally constrained traditional FWI.

- **Physics-informed learning improves temporal generalization.** DeepONet trained on 4 timesteps struggled to predict intermediate timesteps, but incorporating PDE constraints during training significantly improved performance on unseen finer-resolution time steps — a key requirement for practical FWI where continuous temporal coverage matters.

## Weaknesses

### Fatal
None.

### Major

- **No ML experiments on the Real Earth tier.** The paper's title, abstract, and introduction emphasize global-scale seismic tomography. However, every ML experiment — forward modeling, gradient-based inversion, multi-start sampling, direct inversion mapping — is performed only on the Acoustic and Elastic tiers (1 km radius). The Real Earth tier (full Earth radius, 30 s period) is described and the data has been generated (Table 1 documents 10,000 samples, 5427 structure parameters, ~100,000 CPU hours), but no baseline results are shown on this tier. Since the Real Earth tier is what distinguishes this dataset from existing local-scale datasets, the absence of any ML demonstration on it weakens the paper's central narrative that ML approaches are "particularly suitable for global FWI." The reader cannot assess whether the ML methods scale — even in a proof-of-concept form — to the realistic problem the dataset was designed to address. This is the most significant gap in the paper.

### Minor

- **No comparison with traditional numerical FWI on the same test cases.** The inversion experiments show that ML-based gradients improve correlation with ground truth, but there is no reference inversion (e.g., a few iterations of conventional FWI using the numerical solver's adjoint on the same acoustic test cases) to calibrate what "good" inversion looks like on this dataset. The paper argues that ML overcomes limitations of traditional FWI, but it never demonstrates what traditional FWI would produce under the same conditions. Without this anchor, the improvement numbers are difficult to interpret. (This weakness is not fatal for a dataset paper — the primary contribution is the data, not a novel inversion method — but it limits the force of the claims about ML-based FWI.)

- **No Fourier Neural Operator (FNO) baseline.** FNO is a standard neural operator for PDE problems and is cited prominently in the paper's related work section. Its absence from the baseline comparison is an odd omission that weakens the benchmarking claim. The HFN architecture incorporates some frequency-domain ideas but is not a substitute for the well-established FNO baseline that the community would expect.

- **Dataset access and release are not specified.** The paper introduces the dataset as a resource for the community but provides no repository, DOI, license, or statement of planned release. For a dataset paper, this is a structural omission that must be addressed before publication. (Per the hard rules, this is not about questioning whether the dataset exists — it is about the paper failing to provide access information for its own contribution, which is a legitimate concern for a dataset paper.)

- **Inversion experiments are confined to the Acoustic tier with a single forward model (MLP).** The Elastic tier, which includes source variations and P/S wave conversions and is arguably more relevant for real data, receives no inversion results. The generality of the inversion claims would be strengthened by at least one demonstration on the Elastic tier.

### Trivial

- The spherical-harmonic degree-8 limitation is acknowledged by the authors (Section 2.2) and discussed in the future work section. The harsh critic's point about this — that higher degrees matter for shallow structures — is valid in principle but the paper already addresses it with a cited justification and explicit mention of future expansion. No additional action required beyond what the authors already state.

## Nice-to-Haves

- Adding a traditional FWI comparison on the Acoustic tier (even a few adjoint iterations) would ground the inversion results and directly connect to the paper's motivating argument.
- Including FNO as a baseline would make the benchmarking more comprehensive and align with related work.
- A brief discussion of compute budget for Real Earth ML experiments (and why they were deferred) would help manage reader expectations.

## Removed Points

- **Criticism about FNO not being included was kept** as a Minor weakness (it is a legitimate omission from the baseline set).
- **Harsh critic's suggestion to "run at least one baseline on Real Earth tier"** — This is a valid suggestion but kept implicitly as it underlies the Major weakness above.
- **Harsh critic's point about spherical-harmonic degree 8** — The paper already addresses this with cited justification (lines 64–65) and mentions future expansion (line 247). Moved to Trivial.
- **Harsh critic's point about run Real Earth baseline as a suggestion** — This is essentially the same as the Major weakness; the suggestion form is redundant.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations primarily iterate on gaps the paper could address rather than offering fundamentally new perspectives on the work.

## Suggestions

1. **Demonstrate at least one ML baseline on the Real Earth tier.** Even a simple experiment — e.g., training a small MLP or DeepONet on a subset of the 10,000 samples to predict wavefields or seismograms — would substantially increase confidence that the dataset's most novel tier is usable in practice and that ML methods do not collapse at global scale.

2. **Add a traditional FWI comparison.** On the Acoustic tier, run a few iterations of gradient descent using the numerical solver's adjoint and report the resulting correlation. This grounds the inversion results and directly supports the paper's claim that ML helps overcome traditional FWI's computational limitations.

3. **Specify dataset release details.** Provide a repository (e.g., Zenodo, Figshare), DOI, license (e.g., CC-BY 4.0), and the expected total dataset size before final publication. This is essential for a dataset paper to be accepted.

4. **Add FNO as a baseline.** Given its prominence in the neural operator literature and its citation in the paper's own related work, including FNO would strengthen the benchmarking contribution.

5. **Consider extending inversion experiments to the Elastic tier** to demonstrate the approach generalizes beyond the simplest setting.

## Score and Decision

The paper presents a genuinely useful dataset that fills an important gap at the intersection of geophysics and ML. The dataset construction is sound, the multi-tier design is thoughtful, and the baselines on the smaller tiers provide a credible starting point for the community. However, the absence of any ML experiments on the Real Earth tier — the tier that makes this dataset novel — is a significant gap that weakens the paper's central claims about enabling global-scale ML-driven FWI. The paper is on the right track but needs at least minimal demonstration on the global tier and clarification of dataset release plans to fully deliver on its promise.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>