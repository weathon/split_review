Here is my final consolidated review:

## Summary

Pi-CCA proposes a replay-free continual learning framework for vision-language models that preserves cross-modal alignment by directly constraining the spectrum and subspace of the whitened cross-covariance (CCA certificate), rather than acting on proxy signals (logits, similarities, parameters) as prior methods do. The certificate is compactly stored via random orthonormal sketches and updated via streaming EMA. Experiments across four VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL) show state-of-the-art results among replay-free methods, along with ablations confirming the importance of each loss term, a task-order sensitivity analysis, and a prompt-invariance stress test.

## Strengths

1. **Principled geometry-first formulation.** The paper identifies a genuine structural limitation of prior VL-CL work — that it regularizes proxy quantities rather than the actual alignment object underlying zero-shot transfer. Targeting the canonical spectrum and subspaces of the whitened cross-covariance is a well-motivated conceptual contribution, distinct from distillation, off-diagonal matching, and parameter-regularization approaches. The ablation study (Table 3) cleanly validates this: removing the spectral term (λ₁=0) or subspace term (λ₂=0) causes the largest performance drops (MTIL Avg −2.5 and −2.2 p.p., respectively).

2. **Strong empirical performance across diverse benchmarks.** Pi-CCA achieves top replay-free results on four distinct tracks covering classification (MTIL Avg 76.8 vs. next-best 75.2), task-agnostic classification (X-TAIL Avg 68.1 vs. 67.4), retrieval (VLCL I2T R@1 48.6 vs. 46.1), and structured concepts (ConStruct-VL AF 2.7 vs. 3.3). It even surpasses the synthetic-replay method GIFT without storing or generating data. The Pareto analysis (Figure 2) demonstrates a broad efficient ridge for certificate size, confirming practical constant-memory operation.

3. **Task-order insensitivity and prompt robustness explicitly validated.** Figure 5 provides boxplots over 20 random task orders with narrow IQRs (Avg ~76.0–77.4, AF ~2.6–3.0), a robustness dimension rarely quantified in VL-CL. Figure 4 demonstrates that the prompt-invariance loss ℒₚᵢ meaningfully flattens degradation under both ID and OOD prompt perturbations (e.g., +2.44 p.p. R@1 at s=1.0), which no prior replay-free VL-CL method addresses.

4. **Effective use of sketching for constant memory.** The certificate stores only h×k sketched projectors (h ≪ d_v, d_t), and the streaming EMA (Eq. 12–13) avoids storing past samples. The Pareto analysis confirms that a broad range of (k, h) settings near the knee (k=64, h=256) achieve near-optimal performance with modest memory and time cost.

## Weaknesses

### Fatal
None.

### Major

1. **Figure 3 correlation statistics require clarification to be credible.** The figure reports Pearson r = 1.00 and Spearman ρ = 1.00 on three of four panels (1.00/0.99 on the fourth), alongside a "95% confidence interval shaded area." Spearman ρ = 1.00 across multiple panels on real experimental data — even with a small number of swept settings — is extremely unusual and undermines the reader's trust in the quantitative analysis. The presence of a visible CI shading alongside r = 1.00 (which would imply zero-width CI) creates an internal contradiction in the figure's reporting. This is the paper's primary correlational evidence linking alignment-geometry drift to performance loss; the authors must clarify: (a) the number of data points, (b) the precision to which statistics are reported (rounded? to how many decimals?), and (c) whether the reported statistics are on raw pointwise data or aggregated data. Without this clarification, the paper's central empirical thesis is weakened. *This does not invalidate the paper's other contributions (which are supported by ablations, SOTA comparisons, and robustness analyses independent of Figure 3), but it must be rectified for the paper to be acceptable.*

2. **Missing variability measures on main classification benchmarks (Table 1).** Table 2 (retrieval, structured concepts) reports standard deviations (e.g., ±1.0, ±0.8), but Table 1 (MTIL, X-TAIL) reports single values without error bars. Since the reported improvements over prior best are modest (e.g., 76.8 vs. 75.2 on MTIL Avg; 68.1 vs. 67.4 on X-TAIL Avg), the absence of variability information makes it impossible to assess whether these differences are statistically meaningful. The paper mentions multiple seeds in Figure 5 — these same seeds should yield variance estimates for Table 1.

### Minor

1. **Baseline reproduction status is not disclosed.** The paper does not state whether baseline numbers (ZSCL, Mod-X, C-CLIP, etc.) were re-run under identical conditions (same backbone, LoRA settings, learning rate search) or transcribed from original papers. Table 2 reports error bars for baselines, suggesting these may have been re-run, but the paper should explicitly state this. This is a standard disclosure issue common to the field but still important for fair comparison.

2. **The EMA certificate refresh (Eq. 13) introduces a tension with the core invariant-preservation motivation.** The paper frames EMA refresh as "controlled plasticity," but if the certificate slowly absorbs new-task information, it is less clear whether the method preserves the *original* pre-continual alignment invariant or merely maintains a recency-weighted regularizer. The paper does not analyze how much the certificate drifts from its initial values over a long task sequence, or whether zero-shot retention would degrade if measured against the original certificate rather than the EMA-refreshed one. This does not invalidate the empirical results but dilutes the conceptual crispness of the "invariant" framing.

3. **The subspace-angle loss (Eq. 10) uses sketched Frobenius distance as a surrogate for true principal angles, but the surrogate quality is not directly validated.** The paper acknowledges this is a surrogate and cites near-isometric sketch guarantees, but provides no diagnostic (e.g., relative Frobenius error between sketched and true projectors on a held-out batch). The Pareto analysis (Figure 2) partially addresses this by showing that performance does not degrade catastrophically with sketch size, but a direct comparison of surrogate vs. true angle drift would strengthen confidence in the sketched approximation.

### Trivial
None.

## Nice-to-Haves
- The "constant memory" characterization could be clarified: the certificate is O(hk) but the per-step computation involves full-dimensional O(d²) covariance matrices. Separating memory (O(hk) for the certificate + O(d²) for streaming statistics) from computation cost would avoid potential misinterpretation.
- An analysis comparing the original vs. EMA-drifted certificate on a held-out zero-shot set would clarify whether the "invariant" is truly preserved or gradually adapting.

## Removed Points
- **"Fabrication-level suspicious" framing for Figure 3**: Downgraded to "requires clarification." A high (r ≈ 1.00; ρ = 1.00 with small N) correlation is unusual but mathematically possible and should not be characterized as suspicious of fabrication without stronger evidence. The criticism is valid as a call for transparency, not as an accusation.
- **"Scatter plots show a dense cloud of points"**: This language comes from the image parser's alt-text, not the authors' own caption. The authors' text says "scatter" without characterizing its density. Removed as a parser artifact.
- **"Self-fulfilling prophecy" criticism of correlation analysis**: The claim that D_ang and D_ρ are computed on the same statistics that the losses regularize is technically true but does not undermine the correlational evidence — it simply means the method successfully optimizes its objective, which is expected. The interesting finding is that optimizing these specific quantities correlates with retention, which is not tautological.
- **Generic strengths** from Strength Finder ("this paper addressed an important problem"): Removed as superficial; only concrete, evidence-grounded strengths retained.
- **Missing appendix / proof concerns**: Appendix sections are stripped by the parser; these exist in the original submission.

## Novel Insights

The two reviews complement each other usefully. The harsh critic correctly identifies the Figure 3 statistics and missing error bars as the paper's most significant weaknesses — these are genuine evidential gaps, not nitpicks. However, the critic overstates the severity by framing Figure 3 as "fabrication-level" and the method's EMA tension as a fundamental flaw, when it is better understood as an uncharacterized trade-off. The core insight that survives scrutiny is this: the paper's *conceptual* contribution (targeting alignment invariants rather than proxy signals) is well-supported by the ablation study (Table 3) independently of Figure 3, but the paper frames Figure 3 as its primary mechanistic evidence. This creates a mismatch — the paper would be stronger if it either downplayed the correlational evidence relative to the ablation evidence, or presented Figure 3 with transparent statistics. The broader lesson for the field is that "geometry-first" CL is a promising direction, but claims about *causal* relationships between geometric drift and forgetting require stronger statistical reporting than is currently standard in the CL literature.

## Suggestions

1. **Clarify Figure 3**: Report the exact N, the statistics to 3–4 decimal places, and confirm whether correlations are computed on raw pointwise data. If N is small, state this explicitly and consider whether correlation is the right framing or whether a fitted regression with confidence intervals on the slope would be more informative.
2. **Add error bars to Table 1**: Report standard deviations over at least 3 seeds for MTIL and X-TAIL. This is standard practice in the VL-CL literature and is needed to support the claimed SOTA.
3. **Disclose baseline reproduction status**: State for each baseline whether numbers are independently reproduced or cited from original papers. If re-run, describe the conditions.
4. **Acknowledge the EMA trade-off more explicitly**: Add a brief discussion of how much the certificate drifts from its initial values and whether zero-shot retention against the *original* certificate differs from retention against the EMA-refreshed one.
5. **Add a sketch quality diagnostic**: A simple scatter plot of sketched vs. true subspace-angle drift on a held-out batch would directly validate the surrogate assumption.

## Score and Decision

**Calibration anchors:**

| Paper | Path | Score | Round | Comparison |
|-------|------|-------|-------|------------|
| CoLaP | /home/.../6qyRiyI5Ky.md | 2.00 | 1 (low) | Basic flaws; Pi-CCA is clearly stronger |
| CoFiCL | /home/.../fQTw3w3hnA.md | 3.00 | 1 (low) | Similar topic but weaker execution |
| RLAP-CLIP | /home/.../rMHZfCznhZ.md | 6.00 | 1 (mid) | Classification-only; Pi-CCA broader but has reporting issues |
| Compo-ReAlign | /home/.../eiTy6AYeQi.md | 6.00 | 1 (mid), 2 | Similar scope, cleaner reporting; Pi-CCA slightly weaker |
| CoMem | /home/.../xp7wDU9JBW.md | 5.00 | 1 (mid), 2, 3 | Complex system; Pi-CCA has stronger conceptual contribution |
| KeepLoRA | /home/.../T3Vc5fkTzV.md | 5.50 | 2, 3 | Narrower scope, cleaner execution; Pi-CCA comparable |
| ECA | /home/.../svxlmwLGEc.md | 5.00 | 3 | Rejected; Pi-CCA is stronger |

**Round 1 bracket:** [4, 7] — initial bracketing placed this paper in the mid range of VL-CL papers.

**Narrowing:** Round 2 anchors in [5.0, 6.0] show that accepted papers at this level (KeepLoRA at 5.5, Compo-ReAlign at 6.0, CoMem at 5.0) have cleaner reporting or narrower scope than Pi-CCA. The paper is comparable to KeepLoRA in overall quality — both have genuine contributions with manageable weaknesses — but Pi-CCA's reporting issues (Figure 3, Table 1) are more consequential than KeepLoRA's scope limitations. Pi-CCA is stronger than CoMem (5.0) and weaker than Compo-ReAlign (6.0). I place it at **5.5**.

**Final:** The paper has a novel and well-motivated contribution with broad experimental validation. However, the Figure 3 correlation statistics and the missing error bars on the main classification benchmarks prevent the evidence from fully supporting the claims in its current form. The paper would benefit from revision and could be a strong candidate upon resubmission.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>