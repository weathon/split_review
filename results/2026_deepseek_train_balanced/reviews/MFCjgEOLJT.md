Now let me write the final consolidated review.

## Summary

This paper introduces a framework combining iLQR-VAE with sparse priors and balanced model reduction to learn interpretable latent dynamical systems underlying natural, unconstrained animal locomotion. Using zebrafish (30,800 swim bouts) and C. elegans (90 escape trials), the authors show that sparse, impulse-like control signals can reconstruct the full locomotor repertoire (R² > 0.94), that the learned latent space untangles movement categories, and that balanced truncation of a separately trained linear model yields a reduced interpretable system revealing distinct dynamical modes for forward swims vs. turns.

## Strengths

- **Sparse control signals suffice for the full zebrafish locomotor repertoire with strong quantitative support.** Models achieve R² > 0.94, and restricting inputs to a single time-step impulse still yields R² = 0.82 on held-out test bouts (Section 4.1.2). This is a non-trivial finding that goes beyond categorical segmentation approaches.

- **Latent representation untangles movement categories better than raw posture, even against classifiers using the full time series.** A simple classifier on a single latent snapshot (40 ms post-control) outperforms a linear classifier on the full postural time series (Figure 2C). This provides direct evidence that the learned latent space systematically disentangles movement types.

- **Inferred control signals in C. elegans align with a known external perturbation, providing ground-truth validation.** The inferred input peak aligns precisely with a 100 ms aversive heat shock, with a secondary burst coinciding with the Ω-turn transition (Figure 4D). This directly validates that inferred sparse control signals correspond to real behavioral drivers.

- **Systematic comparison against LFADS demonstrates the advantage of the sparse prior.** LFADS yields a control signal correlated with posture at r = 0.73 and worse latent-state classification accuracy (Figure 2C), concretely showing that the sparse prior is critical for learning a meaningful dynamical system rather than just fitting the data.

- **Methodological finding: direct training of small linear models cannot achieve sparse control, but post-hoc balanced truncation can.** As shown in Table S1, it was not possible to directly train small linear models that both reconstruct accurately and use sparse inputs; the overparameterize-then-reduce approach solves this problem.

## Weaknesses

### Major

- **The paper's biological conclusions about movement-mode architecture are drawn from a substantially weaker model than the one that best fits the data, and the impact of this gap is not discussed.** The mode decomposition analysis (oscillatory vs. non-oscillatory modes for forward swims vs. turns, linked to reticulospinal neurons) is performed on the reduced LDS, which achieves only R² = 0.818 overall and R² = 0.76/0.74 for forward swims and turns respectively (Figure 3D). The MGU RNN achieves R² > 0.94. The paper acknowledges this as a "limitation" (Discussion) but does not discuss how 24-26% unexplained variance in the very behaviors being decomposed might affect the biological conclusions. There is no evidence that the same mode structure would arise from linearizing the better-fitting MGU network. This gap between the best model and the interpreted model is structural: the biological claims rest on a model that explains substantially less variance in the target behaviors.

### Minor

- **The spatial navigation claim is asserted without quantitative evidence in the main text.** The paper states that "spatial displacement can be linearly predicted from the 120-dimensional initial latent state" and that this "allows for a simple sensorimotor coupling" (lines 138-141), but the only support is a reference to Figure S4. No R² value, prediction error, or baseline comparison (e.g., predicting displacement from raw posture) appears in the main paper. If true, this is a significant finding meriting main-text quantification.

- **No comparison against switching LDS models (MoSeq, ARHMMs) is provided, despite the Related Work critiquing their interpretability.** The paper argues that switching LDS models "complicate interpretation" (Section 2), but never demonstrates that the proposed single-system + sparse-control approach yields a more interpretable or more accurate account of the same behavioral data. While this doesn't undermine the paper's core methodological contribution, it leaves comparative claims about interpretability unsupported.

- **The C. elegans experiment uses only a single stimulus condition (heat shock) across 90 trials.** This provides an elegant sanity check but does not test whether the model generalizes across different stimulus types, intensities, or spontaneous behaviors. Additionally, the paper notes that inputs are "less sparse" in this setting, which somewhat undermines the sparsity framing central to the zebrafish results. The experiment functions as a qualitative demonstration rather than quantitative evidence of general utility.

- **The sparsity metric (L1/L∞ ratio) is used without discussion of its limitations.** A signal with one large spike and many small nonzero values can approach a ratio of 1, making the metric potentially ambiguous. The paper's conclusions about sparsity are buttressed by the ablation (impulse-only R² = 0.82) and visual inspection of Figure 2B, but the metric itself is not validated or bounded.

- **The composition of the zebrafish dataset (number of bouts per category, handling of variable-length bouts, segmentation procedure) is not described.** This limits the reader's ability to assess whether the latent space separation (Figure 2D) might be driven by imbalanced category representation or by the segmentation procedure itself.

### Trivial

- The phrase "five principal components explained 95% of the variance at movement onset" (line 131) does not explicitly state whether this refers to PCA in the latent space or in the raw posture space, though the surrounding context suggests the latent space.

## Nice-to-Haves

- Adding confidence intervals or error bars to the classification accuracy comparison (Figure 2C) and to the reported R² values would strengthen the quantitative claims.
- A comparison of the reduced model's mode decomposition against mode structure obtained by linearizing the MGU (à la Sussillo & Barak, 2013) would directly address the most significant weakness and could be a "killer experiment" for future work.

## Removed Points

These points were flagged during review but removed under the filtering rules; they are included here in case they are useful but should be treated with caution:

- **"Overstates the case" in Introduction** — Removed as a style/presentation nitpick. The paper's framing is appropriate for a top-venue submission.
- **Missing hyperparameter selection details (latent dimension, control dimension, sparsity prior parameters)** — Removed per Hard Rules: repro nitpicks about undisclosed hyperparameters should be removed.
- **"Comparing latent state at 40ms against classifier on full time series is unfair"** — Removed per Hard Rules: the asymmetry favors the baseline (full time series), not the author's method, so this criticism is invalid.
- **"Linearization should have been the primary approach"** — Removed as speculative opinion; the paper acknowledges this as a limitation and future direction.
- **Missing train/validation/test split details** — Removed per Hard Rules as a reproducibility nitpick about undisclosed implementation details.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation about the gap between the MGU (R² > 0.94) and the reduced LDS (R² = 0.74-0.82) used for mode decomposition is the most significant insight to emerge from the review process — it correctly identifies that the paper's most interesting biological claim rests on a model that explains substantially less variance in the specific behaviors being interpreted. The strength finder's complementary observation — that the C. elegans experiment provides the cleanest single validation of the framework — is also sharp, as it identifies the one experiment in the paper where ground truth is known and the inferred control signals can be directly verified.

## Suggestions

1. **Most impactful single improvement**: Either (a) linearize the trained MGU RNN and apply balanced truncation to that linearization, or (b) substantially soften the biological claims about mode composition, explicitly discussing how the 24-26% unexplained variance in forward/turn reconstruction may affect the interpretation.

2. **Provide quantitative metrics for the spatial navigation claim in the main text** — at minimum the R² of the linear prediction from latent state to spatial displacement and a comparison against a raw-posture baseline.

3. **Add a comparison against a switching LDS baseline (e.g., MoSeq or ARHMM)** on the same zebrafish dataset, even if only in the supplement, to substantiate the Related Work discussion about interpretability.

4. **Clarify the sparsity metric's behavior** with a simple synthetic example showing that the L1/L∞ ratio discriminates impulse-like signals from alternative sparse-but-structured patterns.

5. **Describe the zebrafish dataset composition** (bout counts per category, bout length distribution, segmentation criteria) to allow readers to assess the latent space analyses.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>