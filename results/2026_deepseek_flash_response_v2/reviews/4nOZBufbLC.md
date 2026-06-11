## Summary

Count Bridges introduces a stochastic bridge process on ℤ^d using Poisson birth-death dynamics, yielding closed-form conditionals (Bessel, Binomial, Hypergeometric) that satisfy the composition and projection properties required for diffusion-style training and sampling. The paper extends this framework to deconvolution from aggregates via an EM procedure with projection-guided sampling, enabling unit-level count profile generation from aggregated observations. Experiments include synthetic benchmarks demonstrating favorable scaling to high dimensions, nucleotide-resolution single-cell RNA-seq modeling with bulk deconvolution (comparing against CIBERSORTx and MuSiC), and spatial transcriptomic deconvolution (comparing against STDeconvolve).

## Strengths

- **Closed-form bridge kernels on integers with proven composition property (Proposition 3.1, Figure 1).** The Count Bridge gives exact, tractable conditionals — the slack posterior has Bessel form, and the recursive steps are Binomial + Hypergeometric draws. The composition property (Eqs. 1–2) is empirically validated in Figure 1, where one-step and two-step ECDFs are indistinguishable. This is a genuine theoretical advance over Blackout Diffusion, which uses a pure-death process and cannot transport between arbitrary integer-valued distributions.

- **Dramatically better scaling to high dimensions than CFM and DFM (Figure 3).** Count Bridges maintain near-zero W1 distance across dimensions 4 to 512 on a low-rank Gaussian mixture transport task, while both CFM and DFM degrade sharply. This is the most concrete evidence that the birth–death bridge respects the ordinal structure of counts in a way that categorical discrete models cannot.

- **Principled deconvolution from aggregates via EM with projection-guided sampling (Algorithms 3–4).** The paper provides a complete procedure for training from aggregated measurements when unit-level counts are latent. Proposition 4.1 justifies the projection operator as a first-order exponential tilt (not an ad-hoc heuristic). This is, to my knowledge, the first framework to generate *unit-level count profiles* from aggregates, going beyond the cell-type proportion outputs of CIBERSORTx, MuSiC, and STDeconvolve.

- **Theoretical connection to entropy-regularized optimal transport (Section 3.1, lines 121–135).** The paper shows that Count Bridges solve the static Schrödinger bridge problem, with jump intensity κ playing the same role as entropy regularization in Gaussian bridges. As κ → 0, the KL cost recovers discrete OT with cost |x₁−x₀|, directly analogous to the Gaussian case where σ → 0 recovers quadratic OT. This situates the method within a well-understood theoretical framework.

- **Distributional scoring loss tailored to ordinal counts (Section 3.2).** Using the energy score with a characteristic semimetric ρ(x,x′) = ‖x−x′‖₂ is a principled choice: it is strictly proper, incorporates the lattice geometry, and enables joint modeling across dimensions — properties the paper correctly argues are necessary for discrete generators.

## Weaknesses

### Fatal
None.

### Major

- **Information asymmetry in the spatial transcriptomic deconvolution comparison (Section 6.3, Table 4).** Count Bridge receives spot-level aggregates *and* single-cell nuclear images as side information (z), while the baseline STDeconvolve receives only spot-level counts with no image data. This confounds the comparison — the improvement on JSD/RMSE/Spearman could reflect the additional image data rather than the Count Bridge mechanism itself. The paper acknowledges no control for this. A fairer comparison would either give an alternative method the same image features or restrict Count Bridge to not use images in an ablation.  
  (The bulk RNA-seq comparison against CIBERSORTx/MuSiC is less problematic because those methods also leverage single-cell reference data to build their signatures, though the Enformer embeddings do give CB additional information not available to the baselines.)

- **Missing Blackout Diffusion baseline in synthetic experiments (Section 6.1).** The paper acknowledges Blackout Diffusion (Santos et al., 2023) as the only other count-specific generative approach (Section 5) but does not include it as a baseline. The claim of "state-of-the-art performance on integer distribution matching" is supported only by comparisons against CFM (a continuous method adapted by rounding) and DFM (designed for categorical data, not ordinal counts). Adding Blackout Diffusion would substantiate this claim, especially since the paper identifies it as the most relevant comparator.

### Minor

- **The projection step's theoretical grounding is acknowledged as weak (Section 7).** The Limitations section openly states the projection step "lacks serious theoretical support." This is honest but means the deconvolution pipeline's core approximation is uncharacterized. An ablation comparing the first-order scaling projection (Proposition 4.1) against the learned projection (Section 6.2) and against an oracle using ground-truth latent counts would help quantify the loss from this approximation.

- **Cell-type proportion evaluation is a proxy for the paper's core claim.** The main comparisons against CIBERSORTx, MuSiC, and STDeconvolve use cell-type proportion accuracy (JSD, RMSE, Spearman). While this is the standard evaluation in the deconvolution literature, the paper's novelty is generating *unit-level count profiles* from aggregates. The paper does evaluate count profiles against mean baselines (Tables 2, 5 using MMD, W₂, Energy), but the primary baselines are compared only on proportions. This mismatch between the claimed output (count profiles) and the headline evaluation (proportions) weakens the empirical story, though it is partially mitigated by the distributional evaluations in Tables 2 and 5.

### Trivial

- Figure 3 caption text is duplicated verbatim (the image placeholder description followed by the real caption).

## Nice-to-Haves

- Report formal statistical testing (confidence intervals for differences, permutation tests) for the improvements over baselines.
- Provide an ablation of the projection operator (first-order scaling vs. learned projection vs. oracle with ground-truth latent counts).
- Include inference time comparisons; the Bessel sampler and multi-step diffusion may carry a computational cost relative to the proportion-estimation baselines.

## Removed Points

These points were raised by the harsh critic but removed after cross-checking against the paper:

- **"CIBERSORTx and MuSiC receive no single-cell training data"** — Factually incorrect. Both methods use reference data (signature matrices or single-cell references derived from scRNA-seq data). Removed.
- **"The Enformer comparison (Table 1) is unfair because CB uses Enformer features"** — The comparison shows CB *built on top of* Enformer features outperforming a fine-tuned Enformer, which is informative about the value added by the Count Bridge framework. Not unfair. Removed.
- **"Nucleotide-level modeling is underspecified"** — The paper clearly states each training example corresponds to a nucleotide position in a single cell, with local genomic context from Enformer. The dimensionality is per-position, not genome-wide. Removed.
- **"No code availability"** — The paper states "codebase is available here"; hard rule removes this criticism. Removed.
- **"No evaluation of single-cell count profiles"** — Tables 2 and 5 *do* evaluate count profiles against mean baselines using MMD, W₂, Energy. The issue is only that the proportion-estimation baselines do not produce count profiles, so the comparison on proportions is necessary. Folded into the Minor weakness above. Removed as standalone point.
- **Generic presentation/formatting nitpicks.** Removed.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the spatial deconvolution comparison is confounded by image information is a valid methodological point but not a novel insight; the critic's framing of this as "testing whether having cell images helps, which is already obvious" is accurate and worth flagging.

## Suggestions

1. **Address the information asymmetry in the spatial transcriptomic experiment** by either: (a) incorporating cell images into the STDeconvolve baseline (if feasible), or (b) running an ablation where Count Bridge does not use cell images, isolating the contribution of the bridge mechanism itself.
2. **Add Blackout Diffusion as a baseline** in the synthetic experiments to directly compare against the only other count-native method.
3. **Evaluate single-cell count profiles against ground truth** using distributional metrics (MMD, W₂, Energy) for the deconvolution experiments, since ground-truth single-cell data is available for both PBMC and MERFISH. Report this alongside (or instead of) the proportion-based metrics for the primary baselines.
4. **Ablate the projection operator** (first-order scaling vs. learned projection vs. oracle) to characterize the performance loss from the unprincipled approximation.
5. **Provide more details on the nucleotide-level modeling**: clarify how Enformer is used (frozen vs. fine-tuned), the exact dimensionality of predictions, and how the "nucleotide-level" framing is operationalized.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| 5sPgOyyjG5.md | 3.00 | R1 (weak) | Feynman-Kac estimator using diffusion bridges; much weaker theory and evaluation |
| 4u0ruVk749.md | 3.00 | R1 (weak) | Causal effect estimation with diffusion; straightforward application |
| FjifPJV2Ol.md | 3.40 | R1 (weak) | Schrödinger bridge via stochastic action; limited empirical validation |
| RDLvnUJ5JZ.md | 3.00 | R1 (weak) | Time-series diffusion; straightforward application |
| FKksTayvGo.md | 7.00 | R1 (mid) | Denoising Diffusion Bridge Models; similar bridge framework, cleaner image eval |
| Q1QTxFm0Is.md | 6.80 | R1 (mid) | Underdamped Diffusion Bridges; strong on sampling, modest theoretical novelty |
| 6awxwQEI82.md | 7.00 | R1 (mid) | Discrete/Continuous diffusion analysis; pure theory, no applications |
| pq1WUegkza.md | 7.00 | R1 (mid) | Convergence of discrete diffusion; pure theory |
| EO8xpnW7aX.md | 8.00 | R1 (strong) | Learning to Permute; comprehensive, clean evaluation |
| CxXGvKRDnL.md | 8.00 | R1 (strong) | Progressive compression; clean, well-scoped |
| RuP17cJtZo.md | 8.00 | R1 (strong) | Generator Matching; comprehensive framework |
| fV0t65OBUu.md | 8.00 | R1 (strong) | Optimal Covariance Matching; clean theory + eval |
| DWJr05rymY.md | 5.25 | R2 | Hypergeometric ML estimation; less novel |
| WZfatbNdLV.md | 5.50 | R2 | RNA splicing generative model; straightforward |
| oeDcgVC7Xh.md | 5.25 | R2 | Counterfactual generative model; limited novelty |
| sYrdb3mhM4.md | 5.33 | R2 | STFlow for spatial transcriptomics; straightforward flow matching application |
| IcbC9F9xJ7.md | 6.50 | R2 | scDiff diffusion model for scRNA-seq; rejected for lack of ML novelty |
| **3MnMGLctKb.md** | **6.75** | **R2** | **CFGen for single-cell counts; close match — similar domain, cleaner evaluation** |
| Tqdsruwyac.md | 6.67 | R2 | Spatial causal disentanglement; different methodology |
| lBB3eSn6fY.md | 6.50 | R2 | Gaussian mixture counterfactuals; different domain |
| **XsgHl54yO7.md** | **6.50** | **R2** | **Discrete guidance; similar discrete-state-space contribution level** |

**Round 1 bracket:** The paper sits between weak (~3.0) and strong (~8.0) anchors, clearly in the middle band (3.5–7.5), comparable to DDBM (7.0) and Underdamped Bridges (6.8) in scope but with weaker evaluation.

**Round 2 narrowing:** Compared to CFGen (6.75), Count Bridges has stronger theoretical novelty but messier evaluation (confounded spatial comparison, missing Blackout Diffusion baseline, proxy evaluation). Compared to Unlocking Guidance for Discrete Space (6.50), Count Bridges has more novel theory but less controlled experiments. Compared to scDiff (6.50, rejected), Count Bridges has clearly more ML novelty. Based on these comparisons, the paper is closest to the 6.0–6.5 range.

**Final calibration:** The paper has genuine theoretical contributions (closed-form birth-death bridge, OT connection, distributional scoring) that exceed many papers in this band. However, the evaluation weaknesses — particularly the confounded spatial transcriptomic comparison — prevent it from reaching the 7+ band occupied by papers with both strong theory and clean evaluations (DDBM, discrete diffusion theory papers). The paper is stronger than straightforward application papers (~5.0–5.5) due to the novelty of the core framework.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>