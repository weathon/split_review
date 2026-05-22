Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper proposes Pi-CCA, a replay-free continual learning method for vision-language models that preserves cross-modal alignment by directly constraining the canonical correlation structure (spectrum and subspaces) of the image-text embedding space. The method uses a compact, sketched certificate to summarize alignment geometry and regularizes the model during streaming updates using only mini-batch statistics, without storing past data. The paper additionally introduces a prompt-invariance mechanism that averages over prompt perturbations. Experiments on MTIL, X-TAIL, VLCL, and ConStruct-VL show state-of-the-art results among replay-free methods, consistently outperforming 11+ baselines.

## Strengths

- **Geometry-first alignment preservation via compact certificate**: The paper directly constrains canonical correlations and subspaces — the actual alignment invariants underlying CLIP's zero-shot capabilities — rather than acting on proxy signals (logits, similarities, parameters). This is a principled departure from prior VL-CL work and is validated by SOTA results across all four benchmarks. Table 1 shows Pi-CCA achieves MTIL Avg 76.8, Last 75.5, Transfer 73.2, outperforming 11 replay-free methods. Table 2 shows it leads on VLCL (I2T R@1 48.6) and ConStruct-VL (FA 75.2, AF 2.7), even surpassing a synthetic-replay method (GIFT) without storing or generating data.

- **Replay-free, constant-memory consolidation with demonstrated efficiency**: The certificate uses random orthonormal sketches (Section 3.2) to achieve O(h) storage per modality with h << d_v, d_t. The Pareto analysis (Figure 2) empirically confirms that the configuration (k=64, h=256) lies near the efficient frontier, balancing peak memory, step time, and accuracy. This is a practical advantage over methods requiring replay buffers or generators.

- **Explicit prompt-robustness mechanism with measurable impact**: The L_pi loss (Eq. 11) averages over prompt perturbations to reduce phrasing sensitivity. Figure 4 shows that with L_pi, performance degrades more slowly under increasing perturbation strength — at s=1.0, R@1 is 46.9 (ID) vs. 44.5 without invariance, and AF drops from 3.6 to 2.5 (ID). This addresses a real deployment concern for VLMs.

- **Comprehensive ablation isolating each component's contribution**: Table 3 quantifies the drop from removing each term: spectral term (λ₁=0) drops MTIL Avg by 2.5 p.p., subspace term drops 2.2 p.p., prompt invariance drops 1.5 p.p., confirming all three loss terms are necessary. The ablation also compares Hungarian pairing vs. sorted surrogate, Gaussian vs. SRHT sketches, and EMA variants — providing a clear picture of what matters.

- **Robustness to task order**: Figure 5 shows narrow interquartile ranges over 20 random MTIL task orders (Avg range ~1 p.p., AF range ~0.4), demonstrating that performance does not depend on a favorable sequence.

## Weaknesses

### Fatal
None.

### Major

- **Figure 3 reports suspiciously perfect correlations (r=1.00, ρ=1.00) that are inconsistent with "realistic scatter."** The paper reports Pearson r=1.00 / Spearman ρ=1.00 for angle drift vs. performance drops across 20+ hyperparameter settings, and r=0.99 / ρ=1.00 for spectral drift. Correlation coefficients of exactly 1.00 (rounded to two decimals) over multiple varied configurations — spanning certificate size, EMAs, invariance strength, whitening, pairing, LoRA capacity/LR, sketch type — are highly unusual and suggest either rounding from an extremely small number of distinct data points or a methodological confound. The caption's claim of "realistic scatter" directly contradicts the reported statistics. This figure is the primary evidence for the paper's causal claim that "geometry preservation predicts retention." The authors must clarify: (i) on exactly how many distinct configuration points the scatter plots are based, (ii) whether the correlations are rounded, and (iii) provide actual scatter plots with variance across seeds. The core contribution (Tables 1-3) stands independently, but the conceptual claim is weakened until this is resolved.

- **Missing error bars on MTIL and X-TAIL classification results (Table 1).** The paper reports standard deviations for VLCL and ConStruct-VL (Table 2) but provides only point estimates for the main classification benchmarks. Given that the reported gains over prior methods are modest (1–3 p.p.), it is unclear whether improvements are statistically significant. The authors should report variability (e.g., over 3-5 seeds) for all benchmarks.

### Minor

- **Certificate EMA creates an unresolved tension between "preserving" and "allowing drift."** The certificate reference (Eq. 13) is updated via EMA toward the current model's CCA quantities, meaning the target being regularized against moves over time. The paper invokes "controlled plasticity" (line 146-147) but never formally specifies what invariant is actually preserved. The ablation (Table 3) shows α=0 drops only 1.2 p.p., suggesting the losses L_spec and L_sub do the heavy lifting — but the motivation section centers on preserving the *pre-trained* alignment geometry. Clarifying whether the reference fixed point is the pre-trained structure (and why α is needed) or whether the method merely slows drift would sharpen the conceptual contribution.

- **Source of baseline numbers is not stated.** The paper does not specify whether results for baselines (ZSCL, Mod-X, C-CLIP, etc.) are taken from original papers or re-implemented with tuned hyperparameters. Given the competitive nature of the claimed SOTA, this should be clarified.

- **Limitations are not discussed.** The paper concludes with only success. A frank discussion — e.g., sensitivity to the choice of anchor prompt set for the certificate, computational overhead of recomputing SVD at every step for large batches, potential failure modes for very long task sequences, or how the method scales beyond the 7-11 task settings evaluated — would strengthen the paper.

### Trivial
None.

## Nice-to-Haves
- Replace Figure 3 with a genuine empirical analysis showing scatter with variance across seeds and drift computed on a held-out validation set. If the correlations weaken, that is still informative; if they remain strong, the point is made honestly.
- Explicit discussion of how the EMA rate α trades off stability vs. plasticity.

## Removed Points

**These points are flagged to be removed, treat them with caution:**

1. **Harsh critic's accusation that Figure 3 "is not derived from real runs" or that correlations are "fabricated"** — This goes well beyond what is verifiable from the paper. The paper's method description (Section 3.4) clearly explains how drifts and performance drops are computed across hyperparameter configurations. While the perfect correlations are suspicious and warrant explanation (included as a Major weakness above), accusing fabrication is unwarranted. The paper presents the figure as real experimental data, and there is no evidence to the contrary.

2. **"Replay-free classification is slightly overstated"** — The criticism that EMA covariances aggregate past statistics and thus constitute "compressed memory" is standard practice in replay-free methods. The Pi-CCA certificate stores no raw data, generators, or past embeddings — fitting squarely within the replay-free definition used in the VL-CL literature. This is a minor semantic point that would not change the paper's framing.

3. **Missing appendix content** — Per instructions, sections stripped by the parser (appendix, references after the cut-off) exist in the original submission.

4. **Formatted text about "M forward passes of the SVD per step" being "not negligible"** — The reviewer speculates about computational cost without evidence. The paper provides wall-clock timing in the Pareto analysis (Figure 2), which is the appropriate way to evaluate efficiency.

5. **Missing related works** — Per instructions, this cannot be raised without external verification.

## Novel Insights

The most interesting observation from the cross-review analysis is a tension the paper itself does not fully address: the paper's conceptual framing ("forgetting is alignment-geometry drift, so prevent drift") and the method's actual mechanism ("slow the drift via EMA toward a moving target") are not perfectly aligned. The ablation showing α=0 (completely frozen certificate) is nearly competitive suggests the losses L_spec and L_sub are the real drivers, and the EMA certificate update is a secondary stabilization mechanism. Reframing the contribution as "alignment geometry regularization with an evolving reference" would be more precise than "geometry preservation." That said, the losses themselves — directly minimizing spectral distances and subspace Frobenius differences to a reference — are genuinely novel in the VL-CL context and convincingly shown to matter (2.5 p.p. and 2.2 p.p. drops in Table 3 when removed).

## Suggestions

1. **Address the Figure 3 credibility gap directly.** Report the exact number of configuration points plotted, provide per-seed scatter (not just point estimates), and clarify whether reported r/ρ values are rounded. If the correlations remain high with proper variance, this actually strengthens the paper.

2. **Add standard deviations to Table 1 (MTIL, X-TAIL).** Even 3 seeds with error bars would silence concerns about statistical significance of the 1–3 p.p. gains.

3. **Clarify the certificate's role.** If the EMA update is important, explain why freezing the certificate (α=0) loses only 1.2 p.p. If it's not critical, adjust the motivation to reflect that the losses, not the certificate reference stability, are the core mechanism.

4. **Add a limitations section** covering failure modes, scaling assumptions, and sensitivity to anchor prompts.

## Score and Decision

**Anchor comparisons:**

| Anchor | Avg Score | Comparison |
|--------|-----------|-----------|
| HyCoCLIP (3i13Gev2hV.md) | 8.00 | Exceptionally clean paper; Pi-CCA has a more challenging problem setting but less polished evidence due to Figure 3 concerns. |
| C-CLIP (sb7qHFYwBc.md) | 6.50 | Closest-related anchor; Pi-CCA has a more principled approach and broader eval, but C-CLIP has no Figure 3 credibility issue. Comparable quality. |
| PROOF (k9NYnsC4Mq.md) | 5.67 | Pi-CCA is clearly stronger — more novel contribution, more thorough experiments, better ablations. |
| Task Codebook (EKfcngSxwD.md) | 4.67 | Pi-CCA is substantially more novel and rigorous. |
| Efficient Online CL (G9Ea7mlqGO.md) | 3.80 | Much weaker in all dimensions. |
| LVLM-CL (JIlIYIHMuv.md) | 2.50 | Incomparable quality; Pi-CCA is vastly better. |
| Multimodal CIL benchmark (gNoqEdT2wO.md) | 2.33 | Much weaker. |

Relative to these anchors, Pi-CCA is a solid paper with a genuinely novel contribution that advances the state of the art in replay-free VL-CL. The main results (Tables 1-3) are consistent and well-supported. The Figure 3 issue is a genuine weakness that must be addressed, but it does not invalidate the core method contribution. The paper is above the acceptance threshold, comparable to or slightly better than C-CLIP (6.50) and clearly above PROOF (5.67). Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>