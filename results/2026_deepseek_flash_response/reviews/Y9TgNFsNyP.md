Now let me finalize.

Based on my calibration analysis:

**Round 1 bracket**: 4.5–6.5

**Round 2 narrowing**: I read full reviews of 8 anchor papers in the 4.20–5.75 range. The strongest comparable papers (Decoupling Class Label at 5.75, Oblivious Unlearning at 5.67) had more comprehensive experiments and multiple baselines, though with other issues. Papers at 5.0–5.25 (Contrastive Unlearning, Unlearning via Sparse Rep) had similar rigor levels to FF-Erase but without the same severity of missing error bars.

**Final score**: 5.0. The paper has genuine novelty (first FF unlearning method), a well-motivated technique, and a strong ablation. But the complete absence of any uncertainty quantification, limited baselines (only GA + RE), and only one model-dataset combo in the main text for the core unlearning results are significant evaluation gaps. At ICLR's standards, this places the paper in the weak reject range.

---

## Summary

The paper proposes FF-Erase, the first machine unlearning framework for Forward-Forward (FF) neural networks, along with G-MIA, a goodness-based membership inference attack for verifying unlearning. The key insight is that naive gradient ascent causes catastrophic model collapse in FF models due to their layer-wise independent training, so FF-Erase uses a guidance model to provide stable target goodness distributions and minimizes KL divergence to achieve stable forgetting while preserving utility. Experiments show 1.9–3.1× speedup over retraining with comparable unlearning effectiveness on VGG13/CIFAR-10.

## Strengths

1. **Principled solution to a genuinely novel problem**: This is the first work to identify and address the unique challenges of unlearning in FF models (sensitivity to parameter tuning, layer-wise independent training causing model collapse). The KL-divergence-based forgetting forward (Eq. 5) that shifts goodness distributions toward a guidance model rather than directly minimizing goodness is a well-motivated design. The ablation study (Table 1) provides direct causal evidence: a randomly initialized guidance model collapses Acc_f to 55.53%, while properly guided models preserve utility.

2. **G-MIA outperforms existing black-box MIAs and can match white-box attacks**: Figure 3 shows G-MIA consistently beats the standard black-box final-layer MIA (FL) across all datasets and architectures. On VGG13 with CIFAR-100, G-MIA achieves the highest accuracy among all methods including white-box attacks (GR, GAP, ST), which is a strong empirical result.

3. **Systematic demonstration that gradient ascent fundamentally fails on FF models**: Section 6.3 (Figure 5) thoroughly tests GA across λ = 10¹ down to 0, showing a clean trade-off where high λ causes model collapse (Acc_t below 60%) and low λ fails to unlearn (G-MIA scores of ~0.6 vs. retraining's 0.55). No λ value simultaneously achieves both effectiveness and utility, robustly supporting the paper's motivating claim.

4. **Two practical guidance-model strategies with explicit trade-offs**: The mini-retrained and fast-distilled strategies (Section 4.2) are clearly motivated by different data availability scenarios, and Table 1 systematically maps the (α₁, α₂) hyperparameter space with concrete efficiency-effectiveness numbers, giving practitioners actionable guidance.

## Weaknesses

### Major

1. **No uncertainty quantification across any experiment**: Every result (Table 1, Figure 3, Figure 4, Figure 5) is reported as a single number with no standard deviation, confidence interval, or replication count. This is a serious concern because key comparisons hinge on small numerical differences. In Table 1, the best FF-Erase variant D-(0.5,0.5) gets a G-MIA ACC of 0.556 vs. RE's 0.551 — a 0.005 difference that falls well within single-run noise. Similarly, Figure 3's claims of G-MIA superiority lack any indication of whether visual gaps are statistically significant. For a paper making quantitative claims about being "comparable" to retraining and achieving specific speedup ratios, this omission undermines confidence in every claimed result.

2. **Limited baseline comparisons**: The only unlearning baselines are naive gradient ascent (GA) and retraining (RE). The paper argues that other methods "are not applicable" to FF models but does not attempt a single adaptation — e.g., of SCRUB's teacher-student framework (which shares structural similarities with FF-Erase's own distillation approach) or influence-function-based methods. Without broader comparisons, it is difficult for readers to assess whether FF-Erase's specific technical choices are genuinely necessary or whether simpler adaptations could achieve similar results. The thorough GA ablation (Section 6.3) is informative as a motivating demonstration but insufficient to establish FF-Erase as the definitive solution.

### Minor

1. **Main unlearning results only shown for one model-dataset combination**: Section 6.2 presents unlearning results for VGG13 on CIFAR-10 only, with all other combinations relegated to the appendix (which was stripped by the parser). The abstract and conclusion claim "extensive experiments on various datasets and model architectures," but the main text cannot substantiate this for the core unlearning claims. While a space constraint, the paper's central claims should be visible in the main text for at least one additional combination.

2. **Counterintuitive G-MIA result unaddressed**: In Figure 4(c), both FF-Erase variants achieve *lower* G-MIA scores (0.5245, 0.5260) than the retraining gold standard RE (0.5320). If lower G-MIA means more effective forgetting, FF-Erase appears to outperform retraining — which is counterintuitive and could indicate that G-MIA is not well-calibrated. The paper does not discuss this.

3. **G-MIA access assumptions slightly overstated**: G-MIA requires access to goodness vectors from all layers, which goes beyond standard black-box MIA access (final prediction only). While these are part of FF model inference outputs, the paper should more precisely characterize the access level or clarify why it is a natural black-box setting for FF models.

### Trivial

None of significance beyond normal parser artifacts.

## Nice-to-Haves

- Add standard deviations or confidence intervals to all quantitative results, ideally by running each configuration with 3–5 random seeds
- Attempt to adapt at least one existing approximate unlearning method (e.g., SCRUB's teacher-student framework) to FF models as a concrete comparison
- Discuss the counterintuitive result where FF-Erase achieves lower G-MIA scores than retraining

## Removed Points

These points were flagged by the reviewers but removed after verification:

1. **"Incestuous evaluation loop"** (G-MIA verifying FF-Erase): Using MIA to verify unlearning is standard practice in the unlearning literature. The paper also reports accuracy on D_forget and D_test as independent metrics independent of G-MIA. The comparison is against the retraining gold standard, not circular.

2. **Guidance model distribution concern**: The claim that "guidance model is not truly ignorant since D_remain and D_forget share the same distribution" — this is a standard statistical assumption. A model trained on one subset does not retain specific memories of distinct samples from the same distribution.

3. **Synthesized data requirement for G-MIA**: The paper acknowledges this is a "common setting in related works" and cites model inversion techniques. This is standard for the MIA literature.

4. **Missing fine-tuning baseline**: Fine-tuning on remaining data is conceptually similar to the paper's "recovering forward" step.

5. **Formatting/style/spelling nitpicks**: These are parser artifacts from PDF extraction, not author errors.

6. **Missing related works**: Per instructions, these cannot be verified without external sources and should not be speculated upon.

## Novel Insights

None beyond the paper's own contributions. The primary structural observations (that GA causes model collapse in FF layers due to independent layer-wise optimization, and that a guidance model can stabilize forgetting) are well-articulated by the paper itself.

## Suggestions

1. **Add error bars to all experiments.** This is the single most impactful change. Run each configuration at least 3 times with different random seeds and report means ± std. This is essential for claims that hinge on small differences (0.005 in G-MIA ACC).

2. **Attempt at least one non-trivial baseline adaptation.** Adapting SCRUB or an influence-function method to FF models would convert the "not applicable" assertion into a demonstrated result and more convincingly establish FF-Erase's necessity.

3. **Show at least one more model-dataset combination in the main text**, e.g., AlexNet on CIFAR-100, to support generality claims.

4. **Discuss the Figure 4(c) anomaly** where FF-Erase outperforms retraining on G-MIA scores. This could indicate G-MIA calibration issues that should be addressed.

5. **Clarify G-MIA's access model** — describe it as gray-box or explain why goodness vectors constitute natural black-box output for FF models.

---

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| ZyMXxpBfct.md | 1.50 | R1 (low) | Much weaker — nonsensical paper, no method |
| Xagys9QD3T.md | 3.00 | R1 (low) | Weaker — simpler unlearning method, weaker contribution |
| BJfIDS5LsS.md | 2.50 | R1 (low) | Weaker — convoluted multi-agent approach |
| hwXUmwJAq5.md | 3.00 | R1 (low) | Weaker — simpler gradient-based approach |
| 1MHgMGoqsH.md | 3.00 | R1 (low) | Weaker — MPC unifying BP/FF, no unlearning |
| Uv7bWrIucU.md | 4.20 | R1 (mid) | Weaker — auditing framework, limited technical depth |
| xmQuUqSynb.md | 5.75 | R1 (mid) | *Better* — stronger experiments, more baselines |
| KvFk356RpR.md | 4.80 | R1 (mid) | Comparable — similar rigor concerns, missing error bars |
| iQIQT88prm.md | 5.33 | R1 (mid) | Comparable — limited experiments, missing analysis |
| lgnAEBE1Xq.md | 5.00 | R2 (narrow) | Comparable — similar rigor level, but FF-Erase more novel |
| TLBPjECC5D.md | 5.25 | R2 (narrow) | Comparable — similar novelty-vs-rigor trade-off |
| OHOmpkGiYK.md | 5.75 | R2 (narrow) | Better — more comprehensive experiments |
| wAemQcyWqq.md | 5.67 | R2 (narrow) | Better — more extensive experiments, multiple baselines |
| pUOesbrlw4.md | 5.25 | R2 (narrow) | Comparable — training-free approach, similar depth |
| 84n3UwkH7b.md | 8.00 | R1 (high) | Much stronger — rigorous experiments, accepted paper |
| uHLgDEgiS5.md | 8.00 | R1 (high) | Much stronger — accepted paper, rigorous |
| EUSkm2sVJ6.md | 7.60 | R1 (high) | Much stronger — accepted paper, thorough evaluation |

**Round 1 bracket**: 4.5–6.5

**Round 2 narrowing**: The paper is comparable to the 5.0–5.25 anchors (Contrastive Unlearning, Unlearning via Sparse Rep) in terms of evaluation depth. It has stronger problem novelty than those papers, but the absence of *any* uncertainty quantification is a more significant evaluation gap. Papers at 5.67–5.75 (Oblivious Unlearning, Decoupling Class Label) had more comprehensive experiments with multiple baselines. The final score of **5.0** reflects a paper with genuine novelty and a well-motivated method whose evaluation lacks the rigor expected at ICLR — particularly the completely absent error bars.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>