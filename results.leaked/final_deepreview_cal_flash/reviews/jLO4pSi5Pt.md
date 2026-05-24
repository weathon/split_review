Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces L-TTA, the first method specifically designed for long-tailed test-time adaptation (TTA) of vision-language models (VLMs). It identifies two failure modes unique to this setting — Text-induced Tail Erosion and Modality-bias Amplification — and proposes three co-designed mechanisms: Synergistic Prototypes (SyPs, consisting of Deterministic and Exclusionary Prototypes), Rebalancing Shortcuts (RSs) with a class re-allocation loss, and Balanced Entropy Minimization (BEM). Experiments across 15 datasets under multiple imbalance ratios (10/20/50) show consistent SOTA performance over 12 recent methods, along with favorable efficiency.

## Strengths

- **First principled study of long-tailed TTA for VLMs.** The paper formally introduces this problem and identifies failure modes unique to VLMs under long-tailed test streams, motivating a new problem direction that prior TTA works do not address. This is a genuine gap and the paper is the first to tackle it.

- **Consistent SOTA across 15 datasets, multiple imbalance ratios, and several backbones.** L-TTA outperforms 12 recent methods on OOD (Table 1), cross-domain (Table 2), and corruption (Table 3) benchmarks under imbalance ratios 10/20/50. For example, on the OOD benchmark at imb=10, L-TTA surpasses the second-best method by 1.47%/1.70% in accuracy/macro-F1. Gains also hold on ViT-L/14, ViT-H/14, SigLIP-L/16, and MetaCLIP-BigG (Table 5), showing robustness to backbone choice.

- **Novel exclusionary prototype (EP) design.** Unlike prior prototype-based TTA methods (e.g., TDA) that only update the negative cache for the predicted class, EPs update for *all* classes based on the full prediction distribution (Eq. 5). This enables tail-class representations to be enriched even when those classes rarely appear, which is a conceptually clean solution to the cold-start problem for tail prototypes.

- **Favorable efficiency–performance trade-off.** L-TTA requires only 1.45h and 1.89GB memory on ImageNet (imb=10), substantially less than training-based competitors (RLCF: 18.30h, WATT: 27.70h), while achieving the highest harmonic mean of accuracy and macro-F1 (Table 4).

- **Robustness to dynamic head/tail shifts.** Table 7 shows that varying the sampling probability ε for tail classes causes minimal variation in performance (≤0.22%/0.29% on ImageNet and Flowers), demonstrating stability under non-i.i.d. streams.

## Weaknesses

### Major

- **Missing comparisons against simpler class-balanced variants of existing TTA methods.** The paper claims BEM is a necessary variant of entropy minimization for long-tailed TTA, yet it never compares against natural alternatives such as class-weighted entropy applied to an existing method like TPT, logit adjustment (Menon et al., 2020) on top of standard TTA, or any other method that injects class priors into the EM loss without BEM's specific gating term. The ablation (Table 6) shows that BEM adds only ~0.66% macro-F1 over SyP+RS — a gain that could plausibly be matched by simpler class-weighting schemes. Without these baselines, the reader cannot tell whether BEM's specific design (the (1−P̃)^β gating) is actually beneficial, or whether *any* method that incorporates estimated class priors into EM would achieve similar gains. This weakens the paper's claim that BEM is a distinct methodological contribution and should be addressed to fully substantiate the method.

### Minor

- **K parameter inconsistency and ambiguity.** In the method description, K is introduced as the number of hyper-class vectors (implying an integer). The implementation details state "K = 0.3", and the ablation (Figure 4c, whose caption uses "b" instead of "K") varies K from 0.1 to 1 — all suggesting K is a fraction of the number of classes, which is never stated explicitly. Moreover, the ablation finds K=0.2 yields the best performance (Sec. 4.2, §Vector number K in RS), yet the main experiments use K=0.3. While the performance is reported to be relatively stable across K values, the inconsistency between the optimal setting and the one used in the main experiments needs clarification.

- **Ablation does not fully isolate each component's marginal contribution within the full model.** Table 6 shows incremental addition from single components to the full system (DP → DP+RS → SyP+RS → SyP+RS+BEM), which demonstrates that adding components helps. However, it does not include "full minus component" ablations (e.g., EP+RS+BEM, DP+RS+BEM, SyP+BEM) that would directly measure the marginal contribution of DPs, EPs, and RS within the complete system. The existing ablation is informative but would be strengthened by these ablations to more cleanly separate each component's contribution.

### Trivial

- Some of the reported ablation numbers in the text (e.g., "a decrement of about -3.95% / -3.22% in macro-F1") do not clearly match the values in Table 6; the authors should verify these numbers for accuracy.

## Nice-to-Haves

- An empirical validation of the gradient gap claim in Propositions 1 and 2 — even a small experiment showing that BEM reduces the gradient gap between head and tail classes — would strengthen the theoretical motivation.
- A discussion of limitations (e.g., sensitivity to the quality of class-prior estimates early in the stream, choice of entropy threshold θ for prototype updates) would improve the paper's completeness.

## Removed Points

These points from the inputs were removed after cross-checking against the paper:

- **"Theory not empirically validated" (Critic's Point 4):** The demand for a gradient-measurement experiment on the propositions is beyond what is standard for theoretical results in ML papers. The propositions provide mathematical justification and the proofs are deferred to the appendix (which exists in the original submission). The method (BEM) is empirically validated through ablation. This criticism applies an unusually strict standard. **Removed.**

- **"Loose mapping between failure modes and method" (Critic's Introduction section):** The paper explicitly states that SyPs mitigate both failure modes by adding multi-modal (visual) information beyond text embeddings, RSs dynamically balance head/tail knowledge, and BEM counteracts head-class bias. The mapping exists — it is present in the method overview on page 2 and in the conclusion of the method section. The connection could be more emphasized but is not absent. **Removed.**

- **"CRA loss link to long-tail performance asserted rather than shown":** The ablation (Table 6, Figure 4b) empirically shows that RSs with CRA improve performance, which is evidence for the claim. This criticism is speculative. **Removed.**

- **Generic strengths from Strength Finder about "importance of the problem":** Strengths that do not reference specific content in the paper (e.g., "this paper addressed an important problem") are removed as generic. The remaining strengths above are all backed by specific tables, equations, or figures.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add comparisons against simple class-balanced variants of TPT and TDA (e.g., class-weighted entropy, logit-adjusted softmax) to directly demonstrate that BEM's specific design is beneficial beyond any class-prior-aware objective.
2. Clarify whether K is an absolute count or a fraction of the number of classes, and reconcile the discrepancy between K=0.2 (optimal in ablation) and K=0.3 (used in main experiments).
3. Include "full minus component" ablations (e.g., EP+RS+BEM vs. full, DP+RS+BEM vs. full) in Table 6 to cleanly isolate each component's marginal contribution.
4. Add a limitations paragraph discussing e.g., sensitivity to early-stream class prior estimates, and the choice of θ.

## Score and Decision

### Calibration

**Round 1 (bracketing):**
- Weak anchors (<3.5): pdzHpQbGrn (2.50, Active Test Time Prompt Learning) — rejected with major methodological issues; L-TTA is substantially stronger.
- Middle anchors (3.5–7.5): BUDxvMRkc4 (4.67, BLG: long-tailed CLIP classification) — rejected, narrower scope than L-TTA; yD2JMeKumt (6.00, DOTA: TTA for VLMs) — rejected for unclear method and weak human-feedback justification; lF9QXpfNHm (4.67, ROSITA: open-world TTA) — rejected for incremental contribution.
- Strong anchors (>7.5): TPZRq4FALB (8.00, Test-time Adaptation against Multi-modal Reliability Bias) — stronger theoretical story and cleaner experiments.

**Initial bracket:** 5.5–7.0. L-TTA is clearly stronger than the 4.67 anchors and DOTA (6.00) because it addresses a new problem, has more comprehensive experiments, and a cleaner evaluation setup. It is weaker than the 7+ papers which typically have tighter theoretical stories or fewer methodological gaps.

**Round 2 (narrowing within bracket):**
- 75PhjtbBdr (6.25, Multi-Label TTA with BEM) — accepted; similar contribution level with some clarity concerns; L-TTA has broader experimental scope.
- 9w3iw8wDuE (7.00, Entropy is not Enough for TTA) — accepted; stronger theoretical framing and cleaner method story; L-TTA is slightly weaker.
- b20VK2GnSs (7.00, Concept Drift MLLM) — accepted; broader scope but more confusing evaluation; L-TTA has clearer experiments.

**Final score:** 6.0. The paper is stronger than DOTA (6.00) due to clearer problem framing and more comprehensive experiments, but the missing baselines for simpler class-balanced alternatives and the K inconsistency prevent it from reaching the 6.5–7 level of the cleaner theoretical papers.

### Calibration Anchors

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| pdzHpQbGrn | 2.50 | 1 | Much weaker; L-TTA has clean problem formulation and experiments |
| BUDxvMRkc4 | 4.67 | 1 | Weaker scope (classification-only, not TTA) |
| lF9QXpfNHm | 4.67 | 1 | Weaker contribution (incremental) |
| yD2JMeKumt | 6.00 | 1 | Similar scope but unclear method; L-TTA is better specified |
| 75PhjtbBdr | 6.25 | 2 | Similar level; multi-label TTA vs long-tailed TTA |
| 9w3iw8wDuE | 7.00 | 2 | Stronger theory and method story |
| b20VK2GnSs | 7.00 | 2 | Broader but more confusing evaluation |
| TPZRq4FALB | 8.00 | 1 | Stronger in all dimensions |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>