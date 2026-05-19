- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 6, 5, 5
Now I have sufficient understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper introduces a framework for conditioning protein diffusion models on dynamical properties (specifically the lowest non-trivial normal mode from Normal Mode Analysis) via an analytical loss function (NMA-loss) defined on pairwise angle and amplitude terms. The method is theoretically grounded in the SDE-based classifier guidance framework, uses a rotation/translation-invariant loss, and supports joint conditioning on both dynamics and structure. The approach is demonstrated on two models: a custom GVP-based denoiser (trained from scratch) and the published unconditional Genie model (modified only at sampling time, with no retraining). On Genie, the method generates novel backbones with targeted hinge-like motions that remain designable by the scTM metric.

## Strengths

1. **Novel analytical conditioning avoids training a separate network for dynamics**: The NMA-loss (Eq. 15) is a simple, closed-form function of pairwise angles and normalized displacement amplitudes. This replaces what would otherwise require a neural network to predict eigenvectors for matrices of varying sizes — a challenging and unsolved problem. The approach is model-agnostic and can be plugged into any diffusion model that produces backbone coordinates.

2. **Plug-and-play transfer to a published unconditional model without retraining**: The method is applied to Genie (Lin & AlQuraishi, 2023) using only modifications to the sampling scheme. Conditional samples for three hinge targets (lysozyme, adenylate kinase, hemoglobin) achieve simultaneously low NMA-loss and low RMSD to the structural motif (Figure 5), with visual alignment of displacement vectors shown in Figure 1. This demonstrates genuine transferability.

3. **Formal SDE justification links the method to established theory**: Section 3.1 connects the conditional sampling to score-based SDEs (Eqs. 5–6) and derives the gradient of the loss via Tweedie's formula and the Bayes point machine approximation (Eqs. 12–14), placing the work squarely within the classifier-guidance family.

4. **Invariant loss design respects physical symmetries**: The NMA-loss uses only relative pairwise angles and normalized amplitudes (Eq. 15), ensuring rotation and translation invariance. The structure loss uses a differentiable Kabsch alignment, preserving SE(3) equivariance. The amplitude normalization also makes the loss independent of protein length.

5. **Quantitative evidence of novelty and designability**: 90% of generated samples have TM-score < 0.5 to the training set, showing the model generates genuinely novel folds rather than memorizing training data. The hinge-conditioned samples achieve designability (scTM > 0.5) proportions of 0.48–0.78 across targets, demonstrating that conditioned backbones remain foldable.

## Weaknesses

### Fatal

None.

### Major

- **Asymmetric filtering in hinge experiments undermines fair comparison**: In Section 5.2, conditional samples are filtered by chain distance (3.75–3.85 Å) and RMSD to motif (< 1 Å), keeping only 23%–60% of samples depending on the target, while the 27 unconditional comparison samples are drawn without equivalent quality filters. This creates a selection bias: the conditional set is pre-screened for geometric quality while the unconditional set is not, making the subsequent comparison of NMA-loss and scTM distributions uninterpretable as a fair test. The authors should either apply the same filters to both sets or report unfiltered statistics.

### Minor

- **Best-of-3 selection in GVP experiments inflates apparent effect (but symmetrically)**: Section 4.4 states that for each of the 300 strain/random targets, "we took 3 conditional and unconditional samples, and for each group we selected the one with the lowest NMA-loss." While this selection is applied symmetrically to both conditional and unconditional groups (so the relative comparison is not biased), the reported distributions in Figure 2 reflect the best-of-3 rather than the full distribution, making the absolute improvement difficult to assess. Reporting mean/median over all samples without selection would be more informative.

- **Lack of confidence intervals and statistical significance**: The hinge experiment reports scTM proportions (0.48, 0.78, 0.41) from 27 filtered samples per target — a small-N binomial estimate — without confidence intervals, standard errors, or statistical tests. Similarly, the NMA-loss distributions lack uncertainty quantification. This makes it difficult to assess whether observed differences across targets are meaningful or due to noise.

- **Implementation details of NMA computation at each reverse step are unspecified**: The method requires computing the lowest non-trivial eigenvector of the Hessian/elastic network of the denoised backbone at each reverse diffusion step. The paper does not describe which elastic network model is used, whether sparse or dense solvers are employed, whether automatic differentiation flows through the eigen-solver (and if so, how), or what the wall-clock cost is. While NMA on 256-residue proteins (768×768) is standard and tractable, these omissions are a reproducibility concern for a method whose central operation depends on this computation.

- **Guidance scales are large, vary per target, and are not ablated**: For Genie, guidance scales are in the order of 2000–3000 and differ per target. No analysis is provided of how the scale affects the trade-off between constraint satisfaction and designability, or whether a single scale would work across targets. For the GVP model experiments, guidance scales are not reported at all.

### Trivial

None beyond standard formatting artifacts.

## Nice-to-Haves

- **Independent validation of dynamics control** (e.g., short MD simulations, or at minimum a cross-mode consistency check: computing the NMA on the final generated structure and measuring angular alignment with the target displacement vectors) would strengthen the claim that dynamics conditioning produces physically meaningful motions, beyond showing lower NMA-loss.
- **A structure-only conditioning baseline** on the hinge targets (same model, same sampling procedure, but without the dynamics loss) would isolate the effect of dynamics conditioning from the effect of structure conditioning.
- **Ablation of guidance scale** across a range of values would help understand the sensitivity of the method and whether the large scales (~2000–3000) are necessary or an artifact of loss magnitude.
- **Analysis of discarded samples** (77% discarded for hemoglobin) — understanding why conditioning fails for these cases would illuminate limitations of the approach.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Circular evidence (Claim 3 from Harsh Critic)**: Removed because showing that conditional samples achieve lower NMA-loss is a standard and valid way to demonstrate that conditioning works — analogous to showing that classifier-guided samples have higher class logits. The paper does not rely solely on this metric; it also provides visual inspection (Figures 1, 3), novelty analysis (90% TM<0.5), designability (scTM), and structural quality metrics (SSE, Rg, chain distance).
- **"No comparison to existing conditional generation methods"**: Removed because the paper's contribution is dynamics conditioning specifically — existing methods (RFdiffusion, FrameDiff) do not offer dynamics conditioning, so a direct comparison would not test the claimed contribution. A structure-only baseline on the same model (as noted in Nice-to-Haves) would be useful but the absence is not a weakness for evaluating whether dynamics conditioning works.
- **"Novelty aggregation hides conditional-specific reduction"**: Removed because the paper explicitly states "Both unconditional and conditional samples of both target types were highly novel" — the 90% figure applies across the board, not as a masked aggregation.
- **"scTM inconsistency unexplained for hemoglobin vs lysozyme"**: Removed because the paper reports observed results honestly; a full explanation of target-specific differences is interesting future work but not a flaw in the reported experiment.
- **"NMA computation is likely prohibitive"**: Weakened to the minor point above about unspecified implementation details. NMA on 768×768 matrices is standard in computational biology (milliseconds with sparse solvers on GPU). The harsh critic's characterization as "prohibitive" is not supported.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Re-run the hinge experiment with symmetric filtering**: Apply the same chain-distance and RMSD filters to both conditional and unconditional samples, or report unfiltered results for both groups. This single change would eliminate the most serious evaluation concern.

2. **Add confidence intervals to scTM proportions**: For the hinge targets, report exact binomial confidence intervals or bootstrap estimates. This is straightforward and would substantially strengthen the designability claims.

3. **Clarify the NMA computation pipeline in the methods**: Specify the elastic network model used (e.g., ANM), the solver (e.g., sparse eigensolver), whether gradients flow through the eigen-decomposition or are approximated, and provide approximate per-step runtime for a 256-residue protein.

4. **Report mean/median NMA-loss over all 3 samples** (not just best-of-3) in the GVP experiments, to give a complete picture of the conditioning effect.

5. **Ablate guidance scale on at least one hinge target**, showing the trade-off between NMA-loss, RMSD, and scTM across a range of scales.
