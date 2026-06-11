## Summary

This paper introduces PI-CCA, a replay-free continual learning framework for vision-language models that directly preserves the geometry of cross-modal alignment (canonical correlations and subspaces) rather than proxy signals like logits or similarities. The method uses a compact sketched CCA certificate with constant memory, streaming EMA estimation, and prompt-invariance regularization. Experiments across MTIL, X-TAIL, VLCL, and ConStruct-VL show SOTA results among replay-free methods, with thorough ablations supporting the geometry-preservation hypothesis.

## Strengths

- **Principled geometry-first formulation with causal evidence.** The paper recasts forgetting in VL-CL as alignment-geometry drift rather than proxy-signal drift (Section 1). Table 3 provides direct causal evidence: removing the spectral term ($\lambda_1=0$) or subspace term ($\lambda_2=0$) causes the largest single-factor performance drops (2.5 and 2.2 p.p. on MTIL Avg), confirming that the geometry constraints themselves—not incidental regularization—drive retention.

- **Constant-memory certificate via random sketching.** The method replaces full $d_v \times d_v$ and $d_t \times d_t$ projectors with a sketched certificate of size $O(h \times k)$ (Section 3.2, Eq. 4). The Pareto analysis in Figure 2 maps certificate capacity against memory and speed, identifying $(k,h)=(64,256)$ as an efficient knee. This is a concrete replay- and generator-free consolidation mechanism that prior work (ZSCL, Mod-X, C-CLIP) does not provide.

- **SOTA replay-free results across four distinct VL-CL protocols.** Tables 1 and 2 show PI-CCA achieving the best metrics among replay-free methods on MTIL (Avg 76.8), X-TAIL (Avg 68.1), VLCL I2T R@1 (48.6), and ConStruct-VL FA (75.2) / AF (2.7). Notably, on VLCL it surpasses GIFT (a diffusion-based synthetic-replay method) without any generative model or stored data.

- **Systematic component-wise ablation.** Table 3 ablates seven design choices with per-component drops, allowing readers to attribute gains to specific mechanisms. Disabling covariance EMA ($\beta=0$) hurts MTIL Avg by 2.7 p.p., comparable to removing the spectral term—useful diagnostic information.

- **Task-order sensitivity analysis.** Figure 5 reports distributions over 20 random MTIL sequences with 3 seeds each; narrow interquartile ranges demonstrate that performance is not contingent on a favorable task ordering—a robustness check that most VL-CL papers do not provide.

## Weaknesses

### Fatal

None.

### Major

- **Figure 3 reports suspiciously perfect correlations.** Four scatter plots in Figure 3 claim Pearson $r=1.00$ and Spearman $\rho=1.00$ (two plots report $r=0.99$, $\rho=1.00$) while the caption describes "realistic scatter" and a 95% confidence interval. Pearson $r=1.00$ means every point lies exactly on the regression line, which is impossible for real experimental data from a sweep across "certificate size, EMAs, invariance strength, whitening, pairing, LoRA capacity/LR, sketch type" with "realistic scatter." Even rounding to two decimal places (e.g., $r=0.9996 \to 1.00$) would require the data to be nearly perfectly linear across diverse settings—highly unusual. The only benign explanation ($n=2$ points) would make the 95% CI meaningless. Since this figure is the primary evidence for contribution (iii)'s claim linking geometry drift to performance (the "why it works" analysis), the authors must: (a) disclose the number of data points, (b) report raw correlation values at higher precision, (c) explain how "realistic scatter" is compatible with these coefficients, or (d) provide corrected plots. Without resolution, this analysis cannot be trusted as presented.

### Minor

- **"Invariant" framing is overstated.** The certificate updates via EMA every step (Eq. 13): $\rho^* \leftarrow (1-\alpha)\rho^* + \alpha\hat{\rho}$, etc. This means the "invariant" being preserved is actually a slowly drifting target—a regularization that slows drift rather than a fixed anchor. The paper acknowledges "controlled plasticity" (line 133) but the abstract/intro language ("preserving alignment as an invariant," "first-class invariant") implies a fixed reference. The empirical result (Table 3: removing certificate EMA causes only a 1.2 drop on MTIL) is consistent with this being helpful but not decisive regularization. Clarifying the terminology would improve the paper.

- **Streaming covariance EMA under a changing encoder has no coherence analysis.** Eq. (12) maintains EMA of covariances $\Sigma_{vv}^{(t)}$, $\Sigma_{tt}^{(t)}$, $\Sigma_{vt}^{(t)}$ across mini-batches. As LoRA adapters update, the embedding function changes, so these EMAs mix statistics from different feature spaces. The whitened cross-covariance formed from them does not have a well-defined interpretation as the CCA of any single population. While this may be practically harmless with slow adaptation, the paper should acknowledge and justify this approximation rather than treating it as unproblematic.

- **Table 1 (MTIL/X-TAIL) lacks variance estimates.** The 1.6-point SOTA gap over C-CLIP on MTIL Avg (76.8 vs. 75.2) is reported without error bars or variance, while Table 2 (VLCL, ConStruct-VL) includes $\pm$ ranges. Single-run results without variance make it hard to assess whether the gap is statistically significant, especially given the number of hyperparameters in the method.

- **Power iteration details deferred.** Differentiable SVD via block power iteration is mentioned (line 131, $T_{\text{pow}}$ steps) but convergence criteria and how gradient approximation through iterative SVD affects training stability are not discussed. Deferring to the appendix is acceptable but a brief note on practical behavior would help.

### Trivial

- None.

## Nice-to-Haves

- Adding error bars to Table 1 (even 3 seeds) would significantly strengthen the statistical claims.
- A brief discussion of how the EMA of covariances (Eq. 12) is approximately valid despite a drifting encoder would resolve a methodological concern.
- If the correlations in Figure 3 are genuinely very high (e.g., $r > 0.99$) rather than exactly 1.00, reporting higher-precision values (e.g., $r = 0.998$) would dispel the concern.

## Removed Points

The following points from the inputs were removed with justifications:

- *Code not available*: Removed per hard rule—criticizing availability of code/repositories is not permitted; the paper states code will be released upon acceptance.
- *Prompt invariance mechanism is straightforward*: Removed—this asks the paper to go beyond its stated scope; the contribution is in applying prompt invariance to the CCA certificate, not claiming fundamental novelty in perturbation sampling.
- *Task loss "agnostic to its form" is a weakness*: Removed—misunderstands the paper's intentional design; agnosticism to task loss is framed as a feature, not a bug.
- *Speculation about Table 3 drop interpretation*: Removed—not a concrete weakness, just a subjective reading of the numbers.
- *General hyperparameter complexity critique*: Removed—partially addressed by the existing ablation study (Table 3); sensitivity analysis is deferred to appendix, which is standard practice.
- *Missing related works*: Removed per hard rule—the meta-reviewer does not have external knowledge to verify whether works are actually missing.
- *Formatting/typo/style issues*: Removed per hard rule—these are parser artifacts, not author errors.

## Novel Insights

The correlation coefficients in Figure 3 (r=1.00, ρ=1.00 on multiple plots) should be scrutinized by the authors. If the data genuinely has near-perfect correlation, this is a remarkable finding that warrants explicit discussion of why the relationship is so tight—including what confounders were controlled. If this is a rounding artifact, reporting higher precision would resolve the concern entirely. This issue is the single most impactful thing to fix, as it affects the credibility of the paper's explanatory narrative without undermining the core method contributions.

## Suggestions

1. **Fix Figure 3.** Report exact (non-rounded) correlation coefficients, show the number of data points, and present scatter plots that honestly reflect the variability in the data. If the correlation is genuinely extremely high, explain why (e.g., the drift measure and performance drop are deterministically linked by construction).
2. **Acknowledge the EMA coherence issue.** Add a paragraph explaining why mixing covariances from different encoder states is approximately valid (e.g., slow LoRA adaptation, small $\beta$), or provide an empirical validation showing that the computed CCA still reflects the alignment geometry.
3. **Add error bars to Table 1.** Report standard deviations over at least 3 random seeds for MTIL and X-TAIL.
4. **Tone down "invariant" language.** Replace "invariant" with "slowly-updated reference" or "consolidated certificate" where the EMA update is described, to avoid implying a fixed anchor that the method does not use.

## Score and Decision

**Calibration anchors (all rounds):**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| C-CLIP | sb7qHFYwBc.md | 6.50 | R1, R2 | Direct baseline; PI-CCA has more principled method but Figure 3 issue |
| TiC-CLIP | TLADT8Wrhn.md | 6.25 | R1, R2 | Different contribution (benchmark vs. method); similar quality |
| PROOF (VLM CIL) | k9NYnsC4Mq.md | 5.67 | R1, R2 | PI-CCA is clearly stronger (broader evaluation, more principled method) |
| Complementary Memory | wE1I9IGqeH.md | 6.00 | R2 | PI-CCA is stronger (SOTA across more benchmarks, deeper analysis) |
| Vision-Language Synergy | 9aZ2ixiYGd.md | 5.00 | R2 | PI-CCA is significantly stronger (more benchmarks, more evidence) |
| Low-scoring VL-CL papers | Multiple | 2.0–3.4 | R1 | PI-CCA far exceeds these in scope, rigor, and results |
| High-scoring (non-CL) | Multiple | 8.0 | R1 | Not directly comparable (different subareas) |

**Round 1 bracket:** [5, 7]  
**Round 2 narrowing:** The paper sits between PROOF (5.67) and C-CLIP (6.50). It is clearly stronger than PROOF (5.67) and Complementary Memory (6.00). Relative to C-CLIP (6.50), PI-CCA has a more principled methodological contribution and broader analysis, but the Figure 3 correlation issue is a concrete evidential problem that C-CLIP did not face, pulling the score slightly below C-CLIP. The paper's strengths (geometry-first formulation, SOTA results, thorough ablations) are genuine and well-supported; the weaknesses are fixable. Final score: **6.0**, reflecting a solid paper with one significant evidentiary concern that must be resolved.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>