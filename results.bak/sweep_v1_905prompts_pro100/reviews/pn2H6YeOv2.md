Now I have a thorough understanding of the paper and the calibration anchors. Let me synthesize the final review.

---

## Summary

Pi-CCA introduces a replay-free continual learning framework for vision-language models that directly preserves the geometry of image-text alignment. Rather than regularizing proxy signals (logits, similarities, weights), it maintains a compact certificate of the top-*k* canonical correlation spectrum and subspaces, enforces alignment during adaptation using only mini-batch statistics, and adds prompt invariance via projector averaging over perturbations. Across four standard VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL), Pi-CCA achieves state-of-the-art performance among replay-free methods while remaining generator-free and using constant memory.

---

## Strengths

- **Geometry-first principle is genuinely distinct from prior VL-CL methods.** The paper reframes forgetting as *alignment-geometry drift* and makes the canonical correlation spectrum and subspace the direct optimization target (Section 3.2, Eqs. 4–11), rather than distilling logits, matching similarity distributions, or isolating parameters. This is a principled departure from the proxy-signal paradigm that dominates the literature.

- **Strong and consistent empirical performance across four diverse benchmarks.** Pi-CCA achieves top results among replay-free methods on MTIL (76.8% Avg), X-TAIL (68.1% Avg), VLCL retrieval (I2T R@1 48.6), and ConStruct-VL (FA 75.2, AF 2.7), and even surpasses a synthetic-replay competitor (GIFT) on VLCL (Tables 1–2). The method is evaluated across classification, retrieval, and structured-concept matching tasks, providing broad evidence of effectiveness.

- **Thorough ablation isolates the contributions of each component.** Table 3 shows that removing the spectral preservation term (λ₁=0) or subspace-angle term (λ₂=0) causes the largest performance drops (2.5 and 2.2 p.p. on MTIL Avg, respectively), directly validating that both the canonical spectrum and subspace directions are essential. The prompt-invariance loss and EMA mechanisms each provide measurable gains.

- **Prompt-invariance mechanism is well-motivated and empirically validated.** Figure 4 shows that the prompt-invariance loss (L_pi) flattens degradation curves under increasing prompt-perturbation strength, yielding higher retrieval recall and lower forgetting compared to the no-invariance variant, for both ID and OOD templates.

- **Certificate-capacity Pareto analysis provides practical deployment guidance.** Figure 2 identifies a broad efficient frontier where small certificates (e.g., k=64, h=256) suffice, confirming the "small yet sufficient" hypothesis and offering actionable trade-offs between memory, compute, and accuracy.

---

## Weaknesses

### Fatal

None.

### Major

- **The geometry-drift vs. performance correlation analysis (Fig. 3) reports implausibly perfect correlations.** Two of the four scatter plots show Pearson r = 1.00 and Spearman ρ = 1.00, with the other two at r = 0.99 / ρ = 1.00. These correlations span sweeps over diverse, independent hyperparameter axes (certificate size, EMA rates, invariance strength, whitening, pairing method, LoRA capacity/LR, sketch type). A perfect linear relationship with zero scatter across such a heterogeneous perturbation set is extremely unusual and, absent an explanation, casts doubt on the validity of this specific analysis. The paper's caption even states "Clear positive trends with realistic scatter" — but r = 1.00 implies no scatter at all. While this analysis is supporting evidence rather than the core empirical claim (the method's SOTA performance in Tables 1–2 stands independently), it underpins the conceptual claim that geometry preservation *causally* predicts retention, which is part of the paper's stated contribution ("we furnish analyses linking alignment-geometry stability to retention/transfer trends"). The authors must clarify the number of independent data points, whether any transformation or aggregation artificially produced the perfect correlation, and present the data transparently. This is addressable in rebuttal but currently weakens the paper's evidential claims.

### Minor

- **Memory and computational cost of covariance maintenance are underdiscussed.** The method maintains full EMA covariance matrices Σ_{vv}, Σ_{tt}, Σ_{vt} (each d × d, roughly 3×262K = 786K entries ≈ 3 MB in fp32 for ViT-B/16 with d=512) and performs eigendecomposition for Σ^{-1/2} at every step. While constant with respect to the number of tasks, this cost is not negligible, and the paper's "constant-memory" framing somewhat understates the practical overhead relative to lighter-weight continual learning methods. A brief discussion or breakdown would help readers assess practical trade-offs.

- **Key experimental details are deferred entirely to the appendix.** The main text does not specify the CLIP backbone variant, LoRA rank/configuration, learning rate, batch size, or other hyperparameters needed for basic comparability. While common in the venue, including these in the main text (even in a compact table) would improve transparency.

### Trivial

- The figure caption for Fig. 3 describes "realistic scatter" when r = 1.00 implies zero scatter — a clear mismatch between text and data that should be corrected.

---

## Nice-to-Haves

- A qualitative illustration or discussion of how the CCA certificate evolves across very different task domains (e.g., from natural images to sketches) would give readers intuition about when the method's plasticity might be challenged.

- A breakdown of peak memory and per-step wall-clock time for Pi-CCA compared to representative baselines (beyond the certificate-capacity Pareto in Fig. 2) would strengthen the efficiency claims.

---

## Removed Points

*These points are flagged to be removed — treat them with caution.*

1. **"Reproducibility concerns about undisclosed hyperparameters"** — removed. The paper states that implementation details are provided in Appendices A.1 and A.2, which is standard practice. The parser strips appendix sections; the original submission contains these.

2. **"Missing related works"** — removed per hard rule. The harsh critic did not raise this, but the instruction prohibits flagging absent citations.

3. **"Typos, formatting, grammar issues"** — removed per hard rule. Any formatting artifacts are parser issues, not author errors.

4. **"The method stores full covariance matrices... a non-negligible memory addition that is never discussed"** — partially retained but downgraded. The paper does discuss memory in the Pareto analysis (Fig. 2), and the memory is indeed constant w.r.t. task count. The concern was retained only as a minor weakness about *underdiscussion*, not as a claim that the method is memory-heavy.

5. **"The paper's main text omits crucial practical details"** — retained as minor. The criticism is valid but common in ML venues; moved from major to minor.

---

## Novel Insights

The conceptual reframing of forgetting in VL-CL as *alignment-geometry drift* — measured through canonical correlation spectra and subspaces rather than through proxy signals — is a genuinely useful lens that the reviews surfaced clearly. The paper shows that directly constraining these geometric invariants (spectrum + subspace angles) produces retention behavior that proxy-based methods only approximate. This is a sharper statement than "regularization helps" and opens the door to geometry-aware continual learning beyond vision-language settings.

---

## Suggestions

- **Address Fig. 3 directly in rebuttal.** State the number of independent configurations swept, show the raw data, and explain why the correlations are so high. If the perfect r = 1.00 is an artifact (e.g., very few points, an aggregation step), correct the figure and claims. If the relationship is genuinely that tight, explain why diverse hyperparameter perturbations all lie on the same line. Either outcome is acceptable; the current presentation is not.

- Consider adding a one-sentence note in the main text about the covariance memory footprint and the cost of the eigendecomposition step, to preempt questions about the "constant-memory" claim.

---

## Score and Decision

**Anchor comparison summary:**

| Anchor | Score | Round | Comparison |
|---|---|---|---|
| JIlIYIHMuv (LVLM-CL) | 2.50 | 1 | Pi-CCA is substantially stronger — proper method, comprehensive benchmarks, SOTA results |
| 9aZ2ixiYGd (VL Synergy) | 5.00 | 1 | Pi-CCA is stronger — more principled approach, more comprehensive evaluation, cleaner method |
| sb7qHFYwBc (C-CLIP) | 6.50 | 1/2 | Pi-CCA is stronger — more novel methodology, directly surpasses C-CLIP on MTIL, broader benchmarks, better ablations |
| TLADT8Wrhn (TiC-CLIP) | 6.25 | 2 | Pi-CCA is stronger — more self-contained contribution, fewer design concerns |
| X1OfiRYCLn (Dynamic Eval) | 7.50 | 2 | Comparable quality but different contribution type. Pi-CCA's Fig. 3 concern pulls it slightly below |
| WyEdX2R4er (Visual Data-Type) | 8.00 | 1/2 | VDT is cleaner with no evidential concerns. Pi-CCA sits below |

**Round-1 bracket:** 6.0–8.0. **Round-2 narrowing:** The paper is clearly stronger than the 6.0–6.5 anchors (C-CLIP, TiC-CLIP) and slightly weaker than the 7.5–8.0 anchors due to the Fig. 3 correlation concern. The method itself is sound, the evaluation is comprehensive, and the results are strong. The Fig. 3 issue is addressable in rebuttal and does not invalidate the core methodological contribution.

**Final score: 7.0.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>