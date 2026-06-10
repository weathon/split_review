Now I have a comprehensive picture. Let me write the final review.

## Summary

This paper addresses test-time adaptation (TTA) for vision-language models under long-tailed test distributions — a realistic but underexplored setting. It proposes L-TTA with three co-designed components: Synergistic Prototypes (DPs + EPs to enrich tail-class representations), Rebalancing Shortcuts (learnable cross-attention with a class re-allocation loss), and Balanced Entropy Minimization (a modified entropy loss with confidence-weighted class priors). Experiments across 15 datasets, three benchmarks, three imbalance ratios, and five backbones show consistent improvements over 11 baselines.

## Strengths

1. **First systematic study of VLM TTA under long-tailed distributions with identified failure modes.** The paper diagnoses two specific failure modes — text-induced tail erosion and modality-bias amplification (Section 1, Figure 2) — that go beyond merely applying existing LT techniques to TTA. This diagnostic framing provides mechanistic understanding of why prior VLM TTA methods collapse under imbalance.

2. **Consistent and substantial gains across an unusually broad evaluation.** Tables 1–3 and 5 demonstrate L-TTA outperforms 11 baselines on 15 datasets across OOD, cross-domain, and corruption benchmarks at imbalance ratios 10/20/50, with 5 backbones (ViT-B/16, ViT-L/14, ViT-H/14, SigLIP-L/16, MetaCLIP-BigG). The gains are larger at harder imbalance ratios (e.g., at imb=50 on OOD Average: +0.97% Acc / +4.35% Mac over the next best), showing the method's advantage grows where the long-tail problem is hardest.

3. **Exclusionary Prototypes provide a principled solution to the cold-start problem for tail classes.** Unlike prior prototype-based methods (TDA, DPE) that update only the predicted class's prototype, EPs (Eq. 5) update all class prototypes at every step using prediction-weighted scores. The ablation (Table 6) shows dropping EPs reduces macro-F1 by ~3.22%, confirming their concrete contribution.

4. **Favorable efficiency-performance trade-off.** Table 4 shows L-TTA achieves the highest harmonic mean on both LT-CDB (67.20) and LT-CB (46.08) while using only 1.45h and 1.89G memory — versus WATT at 27.70h (19× slower) with lower HM. This demonstrates practical deployability.

5. **Robustness to dynamic head/tail ordering.** Table 7 varies ε (probability tail classes appear early) and L-TTA's accuracy varies by only ~0.2% on ImageNet and ~0.5% on Flowers, confirming resilience to sample ordering.

## Weaknesses

### Major

1. **K hyperparameter inconsistency.** The Implementation Details (Section 4, line 208) state K = 0.3 for the number of hyper-class vectors in RSs. The ablation on K (Section 4.2, line 334) reports "setting K = 0.2 yields the best performance" — yet K=0.3 is not even tested in the reported ablation range (0.2–1.0). The reader cannot tell which value produced the headline results in Tables 1–3, and the discrepancy between the claimed optimal (0.2) and the used value (0.3) is unexplained. This is a concrete internal inconsistency that undermines trust in the experimental discipline. Additionally, K is introduced as "the number of hyper-class vectors" (line 112), which suggests an integer, yet the values tested (0.1–1.0) and used (0.3) are fractional — implying K is a fraction of C, but this is never stated. The definition must be made explicit.

2. **Circularity concern in BEM class priors.** BEM (Eq. 9) uses class priors π that are "continually updated based on the current predicted pseudo-labels" (line 138). In the long-tailed TTA setting, pseudo-labels are already biased toward head classes — this creates a feedback loop: head-biased predictions → head-biased cardinality estimates → a loss that still favors head classes. The paper does not address how this circular dependency is broken, nor does it report an ablation comparing oracle priors (true test-set frequencies, which are known because the authors constructed the long-tailed sets by subsampling) versus pseudo-label-estimated priors versus uniform priors. Proposition 2's claim (Eq. 10) about narrowing the head-tail gradient gap appears to assume true cardinalities are known. The concern does not invalidate the experimental results (since the authors likely initialize π from the known true frequencies) but limits the claim that BEM would transfer to real deployment where test-set frequencies are unknown.

### Minor

3. **Proposition 1 is too vaguely stated.** The formalization says classes are split "with certain measurements" (line 132), and the notation $\mathbb{E}_{i \sim C_{\text{head}}} \nabla_{z_i} \mathbb{H}$ is ambiguous (expectation over classes or over samples?). The statement's vagueness limits its theoretical contribution. A precise statement would specify the splitting criterion and the distribution of the expectation.

4. **Unclear hyperparameter selection procedure.** The implementation details (line 208) report a single set of hyperparameters ($\eta=1$, $\lambda_1=\lambda_2=6$, $K=0.3$, $\beta=1$) used across all experiments. It is not stated whether these were tuned per dataset, on a held-out validation set from the target distribution (which would be unavailable in real TTA), or held constant. This matters for assessing generality.

5. **Computational complexity of EP updates not discussed.** Eq. 5 updates all C prototypes per view per sample. With Q=15 views and C up to 1000 (ImageNet), this is 15,000 prototype updates per test sample. While Table 4 shows acceptable total runtime on ImageNet, the O(C) scaling behavior and its practical limits for larger C are not discussed.

### Trivial

6. The hyper-class vector count is labeled K in the main text (line 112) but appears as "b" in Figure 4(c)'s caption — a minor notation inconsistency.

## Nice-to-Haves

- An ablation comparing oracle vs. estimated vs. uniform class priors for BEM, to directly measure the impact of the circularity concern raised in Weakness 2.
- Reporting results at both K=0.2 (ablation-optimal) and K=0.3 (stated default) to resolve the inconsistency.
- A per-class accuracy plot or head/tail accuracy table in the main paper (currently in Appendix C, which was stripped).

## Removed Points

These points were considered but removed with justification:

- **"First attempt" novelty claim**: Removed. The paper acknowledges SAR/DELTA in Section 2.1 and explicitly distinguishes its focus on VLM-specific long-tailed TTA. The claim is reasonable in context.
- **Missing per-class accuracy breakdown in main text**: Removed. The paper says head/tail accuracy is in Appendix C, which was stripped by the PDF parser.
- **Corruption benchmark limited to Gaussian noise**: Removed. The paper says 16 corruption types with severity 5 are in Appendix J (stripped).
- **Table 7 formatting issue**: Removed — this is a PDF parsing artifact.
- **Proposition 2 proof unseen**: Removed — appendix proofs are standard during review and the appendix was stripped.
- **Head/tail split threshold sensitivity (top-20%)**: Removed as a minor and generic point; any threshold is a reasonable choice.
- **Scalability concern framed as "not discussed"**: Weakened to minor (Weakness 5) since Table 4 already shows practical efficiency on ImageNet.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the K inconsistency** — confirm which value produced the main results, explain the discrepancy between the implementation default (0.3) and the ablation optimum (0.2), and explicitly define K (is it a fraction of C or an absolute count?). Report main results at both values to demonstrate robustness or to correct them.
2. **Add a BEM prior ablation** — compare oracle priors (true test-set frequencies) vs. pseudo-label-estimated priors vs. uniform priors. This would either alleviate the circularity concern (if estimated priors perform comparably) or bound the claim appropriately.
3. **Clarify hyperparameter selection** — state whether η, λ₁, λ₂, K, β were tuned per dataset or held constant, and under what validation protocol.
4. **State the O(C) complexity** of the EP update and discuss practical limits on class count.
5. **Sharpen Proposition 1** with an explicit splitting criterion and a precise definition of the expectation operator.

---

### Calibration Report

**Round 1 — Bracketing**: Queried "test-time adaptation vision-language models long-tailed" with score bands <3.5, (3.5, 7.5), >7.5. Weak anchors (avg ~2.5): clearly weaker than L-TTA. Strong anchors (avg 8.0): clearly stronger. Middle anchors (4.4–7.0): most relevant.

**Round 2 — Narrowing**: Queried two bands within (4.5, 7.5) with broader search terms.

**Anchor comparisons**:

| Anchor Paper | Avg Score | Round | Comparison to L-TTA |
|---|---|---|---|
| Active Test Time Prompt Learning in VLMs | 2.50 | R1 | Much weaker — narrow scope, limited experiments |
| LVLM-CL (Continual Learning) | 2.50 | R1 | Much weaker — different setting, limited evaluation |
| BLG (Long-tailed CLIP) | 4.67 | R1, R2 | Weaker — labeled fine-tuning (not TTA), fewer datasets |
| ROSITA (Open-world VLM TTA) | 4.67 | R1, R2 | Weaker — incremental contribution, fewer experiments |
| Noisy TTA in VLMs (AdaND) | 6.00 | R2 | Comparable — similar novelty level (new TTA setting), L-TTA has broader evaluation |
| Multi-Label TTA with BEM | 6.25 | R2 | Comparable — different niche, similar experimental rigor |
| PROGRAM (Prototype TTA) | 6.20 | R2 | Comparable — similar method complexity, L-TTA has more baselines |
| DOTA (Distributional VLM TTA) | 6.00 | R2 | L-TTA is stronger — DOTA had fundamental issues (unclear estimation, impractical hparam tuning) |
| Concept Drift for MLLMs | 7.00 | R1 | Slightly stronger — more theoretical depth, but less focused experimental design |
| Reliability Bias TTA (READ) | 8.00 | R1 | Stronger — genuinely novel problem framing, cleaner method |

**Final reasoning**: L-TTA sits at the top of the middle band. It is clearly stronger than DOTA (6.00) and ROSITA (4.67). It is comparable to PROGRAM (6.20), Multi-Label BEM (6.25), and Noisy TTA (6.00). It is weaker than the Concept Drift paper (7.00) and the Reliability Bias paper (8.00). The K inconsistency is a concrete error that prevents a higher score, but the extensive evaluation and well-motivated problem justify acceptance at 6.0.

**MY FINAL SCORE**: <score>6.0</score>
**MY FINAL DECISION**: <decision>Accept</decision>