Now let me finalize with the full review, incorporating all Round 2 comparisons.

Let me produce the final consolidated review:

## Summary

This paper proposes Classifier-Constrained Alternating Training (CCAT), a two-stage framework for mitigating modality imbalance in multimodal learning. Stage 1 pretrains a shared classifier using bidirectional cross-attention with contribution-balancing regularization to produce an unbiased initialization. Stage 2 freezes that classifier and performs modality-alternating training, with per-modality LoRA adapters providing flexibility and a sample-level secondary update mechanism targeting severely imbalanced samples. The method is evaluated on CREMA-D, Kinetic-Sound, and MVSA, achieving consistent SOTA improvements — most notably +6.76% on Kinetic-Sound.

## Strengths

- **Strong empirical results across diverse benchmarks**: Table 1 shows CCAT achieving SOTA on all three datasets: 85.89% on CREMA-D (vs. LFM 83.62%), 79.29% on Kinetic-Sound (vs. LFM 72.53%), and 80.73% on MVSA (vs. MMPareto 78.81%). The +6.76% gain on KS is substantial and directly validates the claim that constraining the classifier during alternating training effectively addresses modality imbalance. The weak-modality improvements are particularly striking (e.g., CREMA-D Video: 73.79% vs. LFM's 45.83%).

- **Thorough and systematic ablation across all three datasets**: Table 2 ablates all four components (classifier freezing, alternating training, secondary updates, LoRA) with consistent patterns. Removing classifier freezing drops CREMA-D from 85.89 to 82.80 and KS from 79.29 to 77.26, directly validating the paper's central claim. Each component independently contributes, and the rankings are consistent across datasets.

- **Clean architectural decomposition**: The method separates (a) learning an unbiased decision boundary via cross-attention fusion with contribution regularization (Section 3.2) from (b) modality-specific adaptation via frozen classifier plus per-modality LoRA (Section 3.3). This separation is principled and well-motivated.

- **Representation-level evidence beyond accuracy**: Figure 5 provides t-SNE visualizations and quantitative clustering metrics (CH: 242.55 vs. 198.98 for MLA; SH: 0.24 vs. 0.19; DB: 1.28 vs. 1.42) showing that CCAT produces more discriminative feature representations, not just better predictions.

- **Transparent hyperparameter reporting**: Table 3 and Figure 4 report full grid-search results for LoRA rank r and threshold β across all three datasets. Sensitivity is explored and reported rather than hidden.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Abstract contains an incorrect accuracy gain for CREMA-D**: The abstract claims "+1.35% on CREMA-D," but Table 1 shows the gap over the strongest baseline LFM is +2.27% (85.89 vs. 83.62). The +1.35% figure does not match any comparison in Table 1. This is a factual error in a prominent location that should be corrected, though the actual gains are larger than the stated number.

- **Section 3.1 overclaims as a "theoretical framework"**: The paper lists "providing a new theoretical framework" as contribution (i). Section 3.1 derives standard cross-entropy gradients and observes that dominance begets more dominance — a useful conceptual analogy, but not a theory. No formal conditions, convergence guarantees, or testable predictions are derived. The section is better described as a motivational analysis.

- **No standard deviations reported**: The paper states results are averaged over three random seeds but reports no standard deviations in Table 1. For the MVSA gain of +1.92%, confidence intervals would strengthen the claim.

- **Computational cost not discussed**: CCAT requires a full pretraining stage, per-batch MI estimation, and extra forward/backward passes for secondary updates. A runtime comparison against baselines like MLA or LFM would help practitioners assess the cost-benefit trade-off.

- **No discussion of limitations or failure cases**: The conclusion restates contributions without noting scenarios where CCAT might not help or where the pretraining + alternating pipeline could fail.

### Trivial

- The t-SNE analysis (Figure 5) compares against MLA and a non-fixed variant but omits the strongest baseline (LFM on CREMA-D), which would strengthen the representation-quality claim.

- The paper does not discuss whether LoRA modules could partially reintroduce modality-specific classifier bias despite the frozen classifier, though the low-rank constraint (r=2 or r=8) and the small performance impact of removing LoRA (~1.2% on CREMA-D) suggest this is not a practical concern.

## Nice-to-Haves

- An experiment directly testing the "classifier bias" hypothesis — e.g., probing the classifier of an MLA-trained model on unimodal features to demonstrate biased decision boundaries — would make the motivation more concrete.
- Analysis of what LoRA learns per modality (e.g., subspace similarity between modality-specific LoRA weights) would address the design tension around whether LoRA can reintroduce bias.
- Ablation of the bidirectional cross-attention design vs. simpler fusion alternatives during pretraining.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic's "Figure 1 contradiction" (claimed fatal)**: The critic asserted CCAT produces *more* imbalanced contributions than MLA, calling this a structural flaw invalidating the paper's core narrative. This is factually incorrect. The actual Figure 1 data (lines 36-43) shows CCAT Modality A=0.65, B=0.35 (gap=0.30) vs. MLA A=0.90, B=0.10 (gap=0.80). CCAT achieves substantially *better* balance — consistent with the paper's narrative of mitigating imbalance. The critic apparently misread the graph values. REMOVED as factually wrong.

- **Harsh Critic's "LoRA could reintroduce classifier bias"**: Speculative criticism without evidence from the paper. The low-rank constraint severely limits how much LoRA can skew decisions, and the ablation shows LoRA removal costs only ~1.2%, confirming it provides bounded adaptation. Demoted to Trivial.

- **Harsh Critic's "LFM video anomaly" (45.83% video, 83.62% multi on CREMA-D)**: Not anomalous — multimodal accuracy can substantially exceed weak unimodal accuracy when the model relies on the dominant modality (audio at 63.17%). This is common in multimodal learning and requires no special explanation. REMOVED.

- **Harsh Critic's "β threshold varies dramatically — not principled"**: Hyperparameter tuning varies by dataset, which is standard practice. The grid search in Figure 4 shows systematic tuning. Different datasets have different imbalance patterns, so different optimal thresholds are expected. REMOVED.

- **Harsh Critic's "Missing cross-attention details from main text"**: The paper describes the bidirectional cross-attention module at the block-diagram level (Figure 2) and defers details to Appendix A.1. Standard organizational choice. REMOVED.

- **Harsh Critic's "No discussion of related work on fixed classifiers for class imbalance"**: While the paper cites the relevant work (Yang et al., 2022b, line 24) and explicitly draws inspiration from class imbalance remedies, the critic wanted expanded discussion. The paper's scope is multimodal learning, and the single citation establishes the connection adequately. MOVED to nice-to-have.

## Novel Insights

The paper's most interesting insight is the explicit analogy between modality imbalance in multimodal learning and class imbalance in traditional classification — specifically, that both suffer from an early-dominance bias where the classifier develops entrenched preferences that persist even after weaker components begin learning effectively. While both problems have been studied separately, the bridge via gradient dynamics provides a useful lens for transferring solutions between domains (here, fixed classifiers from class imbalance to multimodal learning). The Figure 1 contribution curves provide concrete empirical evidence for this analogy.

## Suggestions

- Correct the abstract's CREMA-D accuracy gain from "+1.35%" to the actual figure (+2.27% vs. LFM or +5.11% vs. MLA, with clear specification of the baseline).
- Report standard deviations for Table 1 results, or note explicitly that they are negligible.
- Add a brief computational cost comparison (e.g., wall-clock time per epoch vs. MLA/LFM).
- Add a limitations paragraph to the conclusion.
- Consider including LFM in the t-SNE comparison to strengthen the representation-quality claim.

---

## Calibration Summary

**Round 1 bracket**: 6.0–7.5

**Anchor papers (all rounds)**:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `5BXWhVbHAK` (modality synergy) | 6.33 | 1,2 | CCAT is stronger: better empirical results, more thorough ablation |
| `ul1cjLB98Y` (unimodal bias theory) | 5.25 | 1 | Different type (theory paper); CCAT has stronger empirical contribution |
| `uAFHCZRmXk` (modality gap analysis) | 8.00 | 1 | Stronger than CCAT: fundamentally deeper analysis, broader scope, more thorough |
| `3UaOlzDEt2` (CREMA, modular fusion) | 6.80 | 2 | Comparable: both have solid empirical results and ablations; CREMA has broader scope (7 tasks) but CCAT has cleaner design and more direct validation of its central hypothesis |
| `uV9KFBVaFI` (MoReS, modality steering) | 6.25 | 2 | CCAT is stronger: better ablation, cleaner motivation, SOTA rather than "comparable" results |
| `aPTGvFqile` (AlignCLIP) | 6.29 | 2 | CCAT is comparable-to-stronger |
| `ftGnpZrW7P` (GRAM) | 7.00 | 2 | Comparable quality; CCAT has more focused contribution |

**Round 2 narrowing**: CCAT sits between MoReS (6.25) and CREMA (6.80), closer to CREMA. Compared to CREMA, CCAT has: fewer benchmarks (3 vs 7) but cleaner ablation design, more direct validation of its central hypothesis, and consistent SOTA results. CCAT's weaknesses are all minor (abstract error, missing std devs, no compute cost). 

Final score: **7.0** — a solid accept with minor presentational issues to fix.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>