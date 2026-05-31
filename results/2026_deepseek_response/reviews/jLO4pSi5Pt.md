Now I have good calibration context. Let me finalize the review with the calibrated score.

**Round 1 bracket:** The weak anchors (2.33-2.50) are clearly below this paper. The strong anchors (8.0) are above. This paper sits in the middle band (3.5-7.5). Within the middle band, we have BLG (4.67), ROSITA (4.67), DOTA (6.0), Noisy TTA (6.0), and the Concept Drift paper (7.0).

**Round 2 narrowing:** Reading DOTA (6.0) and Noisy TTA (6.0) in full — DOTA got 6,6,6,6 (Reject) with issues around unclear method and weak human-in-the-loop gains; Noisy TTA got 6,6,6 (Accept) with solid problem framing but a simpler method. L-TTA has stronger experimental validation (15 datasets, 12 baselines, 3 benchmarks, 3 imbalance ratios, multiple backbones) and a more clearly defined methodological contribution. Its weaknesses (K inconsistency, overclaim of "first") are fixable, unlike DOTA's structural issues. I'd place L-TTA above 6.0 — closer to the Concept Drift paper's 7.0 but with the synthetic evaluation limitation pulling it slightly down.

## Summary

This paper proposes L-TTA, the first method specifically designed for test-time adaptation of vision-language models under long-tailed test distributions. It identifies two VLM-specific failure modes (text-induced tail erosion, modality-bias amplification) and introduces three co-designed components: Synergistic Prototypes (SyPs) with Deterministic and Exclusionary Prototypes to enrich tail-class representations, Rebalancing Shortcuts (RSs) with a class re-allocation loss for adaptive rebalancing, and Balanced Entropy Minimization (BEM) with theoretical justification. Extensive experiments across 15 datasets, three benchmark types (OOD, cross-domain, corruption), three imbalance ratios (10, 20, 50), 12 baselines, and multiple backbones demonstrate consistent improvements in both accuracy and macro-F1.

## Strengths

1. **First systematic study of VLM TTA under long-tailed test distributions**: The paper identifies two VLM-specific failure modes (text-induced tail erosion, modality-bias amplification) that go beyond general class-imbalance challenges. Figure 1 provides qualitative illustration, and the method design is directly grounded in this analysis. The problem formulation is novel within the VLM TTA literature, which has overwhelmingly focused on balanced settings.

2. **Empirical superiority across diverse benchmarks**: L-TTA consistently outperforms 12 baselines on OOD (Table 1), cross-domain (Table 2), and corruption (Table 3) benchmarks under imbalance ratios 10, 20, and 50. For example, on the OOD average at Imb=10, L-TTA achieves 65.97% Acc / 61.18% Mac vs. the next best (DPE) at 64.50% / 57.57%. Gains are larger on macro-F1 than accuracy, confirming genuine class-balancing improvement. Results are averaged over 5 runs.

3. **Three well-motivated components with ablation support**: The ablation (Table 6) shows each component contributes, and SyP+RS+BEM consistently outperforms subsets. The Exclusionary Prototype design (Eq. 5) — updating all classes' EPs based on prediction confidence — is a principled departure from prior methods like TDA that only update the predicted class.

4. **BEM with theoretical grounding**: Propositions 1 and 2 formally analyze why standard EM biases head classes and show that BEM reduces the optimization gap between head and tail gradients. While proofs are deferred to the appendix, the empirical confirmation (Table 6) supports the theoretical claim.

5. **Efficiency without performance sacrifice**: Table 4 shows L-TTA runs in 1.45h with 1.89G memory (ImageNet, Imb=10), achieving the highest harmonic mean (67.20 on LT-CDB) among all methods. Competitors like RLCF (18.30h) and WATT (27.70h) are an order of magnitude slower.

6. **Backbone-agnostic gains**: Table 5 shows consistent improvements across ViT-L/14, ViT-H/14, SigLIP-L/16, and MetaCLIP-BigG, supporting generality beyond the default ViT-B/16.

## Weaknesses

### Major

1. **Inconsistent reporting of hyperparameter K**: The Implementation Details (line 208 in the paper) explicitly state "$K = 0.3$" for the number of hyper-class vectors in Rebalancing Shortcuts. However, the ablation study on vector number (line 334) reports that "setting $K = 0.2$ yields the best performance." This is a direct factual contradiction within the paper. It undermines confidence in which value was used in the main experiments and what the correct specification is. The authors must resolve this discrepancy in the rebuttal.

2. **Overclaim of "first"**: The abstract and contribution list claim "the first attempt to solve this problem" and "the first TTA for long-tailed settings." Yet Section 2.1 (related work) itself cites SAR (Niu et al., 2023) and DELTA (Zhao et al., 2023a), which explicitly address non-i.i.d. test data including class imbalance during TTA. The paper's actual novel contribution is in the VLM-specific cross-modal challenges (text-induced tail erosion, modality-bias amplification), which is legitimate and sufficient. The "first" framing should be qualified to "first for VLMs" or "first to address the unique cross-modal challenges in long-tailed TTA." This does not weaken the contribution — it makes it more precise.

### Minor

1. **Synthetic construction of long-tailed test sets limits real-world claims**: The paper constructs long-tailed test sets by random sampling from balanced benchmarks (line 206: "we conduct random sampling to manipulate the cardinality distribution into an exponentially decayed curve"). The abstract and introduction claim the method addresses "real-world test sets that exhibit long-tailed distributions." In real-world TTA, long-tailed streams arise from natural prevalence patterns, not random downsampling — the sequential arrival order, visual characteristics of rare categories, and semantic relationships may all differ. The dynamic head/tail class shift ablation (Table 7) partially addresses this by varying class ordering, but the core evaluation remains synthetic. A limitations paragraph explicitly acknowledging this gap would strengthen the paper.

2. **Failure modes argued qualitatively, not quantified**: The two failure modes (text-induced tail erosion, modality-bias amplification) are well-motivated but demonstrated only through qualitative visualization (Figure 1b). The paper never quantitatively measures these effects — for example, showing that text embeddings of certain classes consistently have higher similarity to visual features regardless of head/tail status, or that applying unimodal TTA methods on VLMs produces larger performance degradation than on pure visual backbones. Quantitative evidence would strengthen the already clear motivation.

3. **Theoretical propositions are suggestive rather than decisive**: Propositions 1 and 2 are presented as theoretical justification for BEM, with proofs deferred to Appendix A. The paper presents Proposition 2 as if it alone validates BEM, without acknowledging the gap between the gradient-magnitude claim and actual non-convex optimization dynamics. The empirical ablation (Table 6) carries most of the weight, which is acceptable — the paper should be more explicit about this.

4. **No limitations section**: The paper lacks an explicit discussion of limitations. Specifically, it should discuss (a) the synthetic nature of the long-tailed distributions, (b) the assumption that class priors can be reliably estimated from pseudo-labels during TTA, and (c) potential failure cases (e.g., when tail classes are extremely rare or the datastream is very short).

### Trivial

1. **Table 4 clarity**: Some entries in the efficiency table are unclear (e.g., "1.54<×n" for WATT memory, and missing entries for RLCF and WATT on corruption benchmark).

## Nice-to-Haves

- A corruption-focused ablation showing which component (SyPs, RS, BEM) drives the observed robustness under noisy conditions (Table 3 shows larger gaps under corruption, and the paper attributes this to L-TTA's design but does not ablate this directly).
- Standard deviations or error bars for key comparisons (5 runs are reported but only averages are given).

## Removed Points

The following points from the inputs were removed or downgraded per the filtering rules:

- "Code is promised but not available" — Removed per hard rules about reproducibility expectations; code release is standard for conference submissions and is mentioned in the paper.
- "Missing appendix content / proofs" — Removed per hard rules; appendix sections are stripped by the PDF parser.
- "Missing related works" — Removed per hard rules; I cannot independently verify missing citations.
- "Formatting/typo nitpicks" — Removed per hard rules; parser artifacts are not author errors.
- "Speculative fatal claims about the method not working in certain scenarios" — None present in inputs.
- "The paper should include naturally long-tailed datasets like iNaturalist" — Weakened from a major evidential issue to a minor weakness because the dynamic shift ablation (Table 7) partially addresses the concern, and the paper clearly describes its synthetic construction.

## Novel Insights

The reviews surface a productive tension: the paper has strong, consistent experimental evidence that its three-component design works under controlled conditions, but the synthetic nature of the long-tailed construction means the cleanest evidence for real-world deployment is indirect. The dynamic head/tail shift experiment (Table 7) is a step in the right direction, but a more systematic analysis of how the synthetic construction might differ from natural long-tailed streams (e.g., in terms of inter-class visual similarity among rare categories, or the temporal structure of class arrival) would be valuable. The K inconsistency is a rare genuinely factual error that needs a simple fix.

## Suggestions

1. **Resolve the K inconsistency**: Clarify whether $K=0.2$ or $K=0.3$ was used in main experiments, and ensure consistency between implementation details and ablation.
2. **Qualify the "first" claim**: Change to "first for VLMs" or "first to address cross-modal challenges in long-tailed TTA."
3. **Add a limitations paragraph**: Discuss the synthetic evaluation setup, class-prior estimation assumptions, and potential failure cases.
4. **Quantify the two failure modes**: Add a table or figure showing, e.g., per-class accuracy differences across head/tail status for different methods, or a comparison of unimodal TTA on VLM vs. pure visual backbones.
5. **Add standard deviations** to the main tables for the 5-run averages.

### Anchors Used

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| pdzHpQbGrn.md (Active TPT) | 2.50 | 1 | Significantly weaker — poorly motivated, methodologically thin |
| JIlIYIHMuv.md (LVLM-CL) | 2.50 | 1 | Significantly weaker — different setting, less rigorous |
| ZaudLwn0Hm.md (Prototypical evolution) | 2.50 | 1 | Significantly weaker — few-shot, not TTA |
| gNoqEdT2wO.md (MCIL benchmark) | 2.33 | 1 | Significantly weaker — benchmark paper, different scope |
| b20VK2GnSs.md (Concept drift MLLM) | 7.00 | 1,2 | Slightly stronger — accepted, has new dataset contribution; but L-TTA has stronger evaluation rigor |
| BUDxvMRkc4.md (BLG) | 4.67 | 1,2 | Weaker — long-tailed CLIP but not TTA, some innovation concerns |
| lF9QXpfNHm.md (ROSITA) | 4.67 | 1,2 | Weaker — open-world TTA, incremental contribution noted |
| 9RnTw9YiXV.md (LVLM long-tail) | 4.40 | 1 | Different focus (training data analysis), less method contribution |
| yD2JMeKumt.md (DOTA) | 6.00 | 2 | Comparable but slightly weaker — similar TTA setting but had unclear method details and weak human-in-the-loop component; L-TTA has stronger experiments |
| iylpeTI0Ql.md (Noisy TTA) | 6.00 | 2 | Comparable — accepted, similar evaluation scope; L-TTA has more methodological novelty |
| cpGPPLLYYx.md (VL-ICL Bench) | 6.50 | 2 | Different domain (ICL benchmark) — not directly comparable |
| kZEXgtMNNo.md (LLM aligners) | 6.00 | 2 | Different domain (benchmarking) — not directly comparable |
| TPZRq4FALB.md (Multi-modal reliability bias) | 8.00 | 1 | Stronger — accepted with higher consensus (all 8s), cleaner evaluation |
| WyEdX2R4er.md (Visual data-type) | 8.00 | 1 | Different domain (data-type ID) — much broader scope |
| uAFHCZRmXk.md (Modality gap) | 8.00 | 1 | Different domain (analysis paper) — not comparable |
| 9Cu8MRmhq2.md (Multi-granularity correspondence) | 8.00 | 1 | Different domain (video-language) — not comparable |

**Round 1 bracket:** [4.5, 7.0]
**Round 2 narrowing:** The paper is clearly stronger than BLG (4.67), ROSITA (4.67), and DOTA (6.0). It is comparable to Noisy TTA (6.0, accepted) with stronger evaluation and more methodological novelty. It is slightly weaker than the Concept Drift paper (7.0, accepted) which had a new dataset contribution. The fixable nature of L-TTA's weaknesses (K inconsistency, framing) relative to the strength of its evidence supports a score slightly above 6.0 but below 7.0.
**Final score:** 6.5

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>