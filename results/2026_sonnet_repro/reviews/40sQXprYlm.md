Now let me do the calibration search to anchor the score.Initial bracket: **4–6**. The paper is a feasibility/exploration study with real contributions (competitive with dense baselines, emergent specialization in vision) but the language efficiency claim fails against a simple baseline, and the headline structural finding (power-law paths) also holds for random models. Let me narrow within this range.Now I have enough context to write the full review. Let me synthesize everything.

---

## Summary

This paper introduces *Distributed Neural Architectures* (DNAs), a framework in which each token/patch follows its own content-dependent path through an unordered collection of shared computational modules, with routing learned end-to-end. DNAs generalize several existing sparse architectures (MoE, MoD, weight sharing, early exit) as special emergent cases. The authors train DNA models at ViT-small and GPT-2-medium scale, report competitive performance against dense baselines, and analyze emergent path distributions, module specialization, and learned compute allocation across vision and language domains.

---

## Strengths

- **Competitive performance against dense baselines**: The top-1 DNA achieves 79.1% ImageNet top-1 accuracy vs. ViT-small's 79.8% at matched active parameter count (22M active). In language, the top-2 DNA (433M active params) attains a lower validation loss (2.674) than GPT-2-medium (2.720) and outperforms it on most zero-shot benchmarks (ARC-E: 59.2 vs 58.9, BoolQ: 61.0 vs 60.5, HellaSwag: 41.8 vs 40.5, PIQA: 67.9 vs 66.9, Table 3). This concretely establishes feasibility of fully dynamic per-token routing without degrading model quality.

- **Rich emergent path specialization in vision**: Figure 3 shows that frequently used paths group patches with global features (edges, flat color) while rare paths cluster semantically specific patches (brass instruments, puzzle pieces). The deep-dream visualization in Figure 4 shows a clear progression from texture/edges (steps 1–3) to semantic features (steps 7–10) as routing decisions are progressively matched — a compelling qualitative demonstration of hierarchical emergent routing structure. The compute allocation analysis in Figure 5 further shows that high-compute images contain complex textures/boundaries while low-compute images are visually simple backgrounds, suggesting interpretable content-aware resource allocation.

- **Honest scoping and candid reporting of negative findings**: The paper explicitly states that it is "not focused on beating SOTA models in any domain, but on showing that distributed models are feasible and on analyzing their emergent structure." It includes language efficiency comparisons and reports that language parameter reuse "is most likely random" (Sec. 4.3) — a genuinely informative negative finding for the community.

- **Unified unifying framework**: The DNA formulation (Eq. 1–2) cleanly subsumes MoE, MoD, weight sharing, and early exit as sub-cases that can emerge from optimization, providing a useful conceptual umbrella for this class of architectures.

---

## Weaknesses

### Fatal
None.

### Major

- **Language efficiency claim fails its own baseline (Table 3)**: The top-2 DNA with 30% skip achieves a validation loss of 2.784 and scores of 52.5/52.9/35.5/23.8/64.2/28.1 on ARC-E/BoolQ/HellaSwag/LAMBADA/PIQA/RACE. The "GPT-2 (30% shallower)" baseline wins on *every single metric*: loss 2.772, ARC-E 58.0, BoolQ 54.9, HellaSwag 37.9, LAMBADA 31.4, PIQA 65.9, RACE 30.1. The paper never acknowledges or discusses this comparison. Since the ability to learn efficient compute allocation is one of three headline claims, having the efficiency model lose to the simplest possible baseline — just remove 30% of layers — without any comment is a substantive omission. The vision case (top-2 DNA at 25% skip with 18M active and 18M total params vs. ViT-small's 22M/22M achieving 78.8% vs. 79.8%) is more ambiguous but still shows a real performance gap.

- **Power-law path distribution deflated by random-model baseline**: Figure 1(c)–(d) presents the power-law path distribution as a major structural finding. However, the figure caption itself states: "Surprisingly, the distribution of paths through the *random* model also follows power-law with exponent −1." The trained vision model has the same exponent (−1) as the random model. The trained language model has −1.2 vs. the random model's −1. Since the power-law holds before any training, it is a property of the routing topology, not of learned behavior. The exponent shift from −1 to −1.2 in language is unexplained and unanalyzed. The paper notes this as "surprising" then moves on, leaving the paper's headline structural result — framed prominently in Figure 1 — with substantially weaker evidentiary weight than claimed.

### Minor

- **Specialization evidence is qualitative; null-model comparison is incomplete**: Section 3.2 notes that random DNA models can also cluster patches based on "superficial features," and refers to Appendix G.2 for a comparison. However, no quantitative metric separates trained-model specialization from random-model clustering. A basic measure such as within-path vs. between-path patch similarity (relative to the random model's same ratio) would determine whether trained routing produces meaningfully tighter or more semantically coherent clusters. As written, it is not possible to rule out that trained specialization is simply a stronger version of random clustering.

- **Total-parameter asymmetry for top-1 DNA in vision (Table 1)**: The top-1 DNA is compared against ViT-small at matched active parameters (22M), but its total parameter count is 34M — 55% more than ViT's 22M. Whether having more total parameters provides a capacity advantage at training time (e.g., via better gradient signal or more diverse representations) is not analyzed. This is relevant when interpreting "competitive" for the top-1 model specifically.

- **Language parameter reuse is random (Sec. 4.3)**: The paper acknowledges that "module reuse is most likely random in the language case," meaning the emergent weight-sharing story observed in vision does not generalize to language. This finding is reported honestly but somewhat buried. Given that parameter sharing was advertised as an emergent feature of DNAs, its failure to generalize weakens the general-framework framing.

### Trivial

- The identity module bias update uses hyperparameters $r$ (skip ratio target) and $u$ (update speed), but no ablation or sensitivity analysis is provided for these values. Since the skip ratio is user-specified, the framing that the model "learns" to allocate compute is slightly imprecise — the target ratio is hard-specified, while only the *per-input* allocation is emergent.

---

## Nice-to-Haves

- **Quantify specialization against a null model**: For trained vs. random DNA, compute per-path within-path patch similarity relative to between-path similarity using any standard feature extractor (e.g., DINO features). A single ratio would validate or appropriately temper the specialization claim.

- **Discuss and analyze the language efficiency gap**: Rather than silently tabulating the result where GPT-2 (30% shallower) outperforms the language skip DNA on every metric, provide a post-hoc analysis of why. Is it training instability under the skip objective? A suboptimal bias update schedule? Does the gap shrink at larger scale? This would make the negative result informative.

- **Language efficiency**: The paper notes that 30% skip language DNA mostly produces uniform compute distribution except for outlier documents (HTML, non-Latin scripts). A more detailed analysis of the model's behavior on these outlier segments would strengthen the efficiency narrative.

- **Attention expressivity analysis**: Section 2.1 states that "attention is computed only between tokens that are currently co-located in the same module." This is a potentially significant constraint on information mixing across divergently routed tokens. Even a brief empirical analysis — e.g., how often co-routing tokens are semantically related — would clarify whether this is a feature or a limitation.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "skip ratio is specified, not learned"** — This is noted above as a minor precision issue in framing, not a fundamental flaw. The paper is clear in Eq. 3 that $r$ controls the ratio; the dynamic per-input allocation is the learned component.
- **Harsh critic: "classification confidence values (p=0.48) are low in Fig. 4"** — The paper directly explains this: "the network guesses the group of classes correctly: birds and dogs, but has difficulty deciding the species and breed." Low top-1 confidence for the reconstructed image is expected given the deep-dream generation doesn't reproduce the exact image.
- **Strength finder: "power-law distribution adds principled justification"** — Removed. As shown above, the power-law holds for random models too, so it provides limited justification for the architectural design choices.
- **Strength finder: "unified framework subsumes MoE, MoD, etc."** — Kept as a strength but the description that it provides a "principled justification" overstates the contribution; it is conceptually unifying rather than theoretically derived.

---

## Novel Insights

The paper surfaces a genuinely interesting observation: power-law path distributions emerge from *untrained* DNA models, suggesting this is a topological property of the combinatorial routing graph rather than a learned phenomenon. The shift in exponent from −1 (random) to −1.2 (trained language) is intriguing but unexplored. If this exponent shift is robustly detectable and scales with model capacity or data quality, it could serve as a diagnostic tool for routing quality. Separately, the finding that vision DNA develops interpretable compute-content correlations (complex boundaries → more compute) while language DNA shows random parameter reuse points to a fundamental difference between how spatial vs. sequential data is processed under dynamic routing — a finding with implications for hybrid or multimodal DNA designs.

---

## Suggestions

1. **Add an explicit discussion of Table 3's language efficiency comparison** — acknowledge that the 30% skip DNA model does not outperform GPT-2 30% shallower and hypothesize why (e.g., language token diversity prevents meaningful per-token compute differentiation at this scale).
2. **Quantify specialization vs. random routing** — compute and report within-path vs. between-path patch feature similarity for trained and random models; a single number per condition would validate the qualitative claims.
3. **Clarify the bias update mechanism's role** — frame the emergent component as per-input allocation rather than "learning to use less compute," since the skip ratio $r$ is set by the experimenter.
4. **Analyze the exponent shift from −1 to −1.2** — examine whether this shift correlates with training progress (early vs. late training) or model size; if it is a stable indicator of "learned routing quality," it becomes a useful metric for the field.

---

## Score and Decision

**Axes summary:**
- *Originality*: High — the DNA framework genuinely unifies and generalizes several conditional-computing architectures under one end-to-end trainable formulation.
- *Importance of research question*: High — compute efficiency and emergent specialization in dynamic-routing models are central open questions.
- *Claims well supported*: Partial — vision feasibility is well-supported; language efficiency claim is directly contradicted by Table 3; power-law finding is undercut by the random-model baseline; specialization is qualitative.
- *Soundness of experiments*: Adequate for a feasibility paper; the omission of any comment on the language efficiency baseline result is the clearest gap.
- *Clarity of writing*: Good; the paper is honestly scoped and clearly organized, but the analysis of negative results is insufficient.
- *Value to community*: Moderate-to-high as a framework paper and initial exploration; the interpretability findings are useful.

**Calibration anchors:**

| Path | Avg Score | Round | Comparison to paper |
|---|---|---|---|
| XVHXVdoV11 (Compatible Specialization) | 3.40 | R1 | Much weaker; narrow scope, less novel |
| KaYXsoCxV7 (ViMoE empirical study) | 3.00 | R1 | Weaker; limited contribution, incremental |
| T26f9z2rEe (Dynamic MoE auto-tuning) | 7.00 | R1 | Stronger; clean evaluation, clear contribution, accepted |
| Pu3c0209cx (Tight Clusters MoE) | 7.00 | R1 | Stronger; theoretical grounding plus strong empirical validation |
| QHzzAU7Qf9 (SMEAR) | 6.00 | R1 | Slightly stronger; focused method, clean evaluation, but rejected |
| 1qq1QJKM5q (COMET) | 5.67 | R1 | Similar; exploratory, multi-domain, mixed results |
| iOy2pITOoH (Spark Transformer) | 5.50 | R2 | Comparable; architectural efficiency claim, insufficient baselines, rejected |
| 2pvECsmld3 (SparseFormer) | 6.25 | R2 | Slightly stronger; cleaner evaluation, clearer improvement over baselines, accepted |
| huy8g3iKy0 (Dense Backprop for MoE) | 5.50 | R2 | Comparable; specific MoE improvement, mixed reviewer reaction |
| 1xG3MN1RRW (SparseVLM) | 5.20 | R2 | Comparable; efficiency claim, works vs baselines, borderline |

**Round 1 bracket**: 4–6.5, with most mass between 5 and 6.

**Round 2 narrowing**: Comparing against the 5.0–6.25 range anchors:
- The DNA paper is **better** than iOy2pITOoH (5.5) and huy8g3iKy0 (5.5) in originality and scope.
- The DNA paper is **similar to** 1qq1QJKM5q (COMET, 5.67): both are exploratory, multi-domain, with mixed quantitative results and interesting qualitative findings.
- The DNA paper is **weaker than** 2pvECsmld3 (SparseFormer, 6.25) and QHzzAU7Qf9 (SMEAR, 6.0) in evaluation rigor and specificity of contribution.
- The language efficiency result explicitly failing against a trivial baseline without comment is a meaningful deduction compared to papers that do not have this issue.

**Final score**: **5.0** — The paper is an interesting feasibility study with genuine novel ideas and compelling vision interpretability, but a core efficiency claim fails its own baseline in the language domain (Table 3, unremarked), the headline structural finding is deflated by the random-model comparison, and specialization claims lack quantification. This places it just below the COMET anchor (5.67) and closer to the Spark Transformer (5.5) / SparseVLM (5.2) range, landing at 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>