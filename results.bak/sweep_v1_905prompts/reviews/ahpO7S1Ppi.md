I now have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper proposes Pctx, a personalized context-aware tokenizer for generative recommendation. Unlike existing static approaches that assign every interaction with the same item to a fixed semantic ID, Pctx conditions tokenization on the user's full interaction history. It encodes user context via a contrastively trained sequence model (DuoRec), fuses this with item features, clusters the fused representations into multiple prototypes per item, quantizes them into semantic IDs, and merges overly rare IDs to control sparsity. The resulting tokenizer enables an autoregressive GR model to decode multiple possible semantic IDs per item during beam search, reflecting different user interpretations. Experiments on three Amazon review categories show consistent improvements (up to 8.9% NDCG@10) over non-personalized baselines including ActionPiece.

## Strengths

- **Genuinely novel and well-motivated idea.** The paper identifies a real limitation of generative recommendation: static semantic IDs enforce a universal similarity standard across users, which is at odds with the fact that the same item can represent different intents for different users. The proposed solution — conditioning tokenization on the user's full interaction history — directly addresses this gap and, to the best of the paper's knowledge, produces the first personalized action tokenizer in GR. The framing is clear and the motivating example (Figure 1) is effective.

- **Consistent empirical superiority across all metrics and datasets.** Pctx outperforms 13 baselines (including conventional sequential recommenders, TIGER, LETTER, and ActionPiece) on all 12 metric-dataset combinations in Table 2. The improvements over the best baseline (ActionPiece) range from 2.44% to 12.32%. The ensemble analysis in Table 4 further rules out the trivial explanation that gains come from combining DuoRec's and TIGER's strengths — Pctx substantially exceeds the best ensemble, demonstrating that the personalization mechanism itself drives the improvement.

- **Comprehensive ablation study with 10 carefully designed variants.** The ablation (Table 3) tests three categories of design choices (context source, tokenization strategy, training/inference strategy), and each ablation is interpretable. Especially insightful is the comparison of variants 1.1–1.3, which shows that DuoRec's contrastive representations (which have *worse* next-item prediction accuracy than SASRec) produce better personalization than SASRec's representations — a non-obvious finding that validates the design rationale. Variant 3.4 (w/ Random Target) controls for the confounding effect of increased token diversity, confirming that the gains are from meaningful personalization rather than sheer diversity.

- **Case study provides concrete evidence of personalization.** Figure 4 shows StarCraft II receiving different semantic IDs under story-driven vs. RTS user contexts, with only the second token differing ([53,395,576,770] vs. [53,412,576,770], sharing the first, third, and fourth tokens). This provides direct qualitative evidence that the tokenizer actually differentiates based on user context.

## Weaknesses

### Major

- **Statistical significance claim is undersupported.** The paper states that results are "statistically significant based on a paired t‑test with p < 0.05" (Table 2 caption) but does not report the number of independent runs, standard deviations, or error bars anywhere. A paired t‑test requires paired observations (e.g., across random seeds); without stating how many runs were performed, the significance claim cannot be evaluated. Given the consistency across datasets and the large ablation drops, the results are likely reliable, but the current reporting falls short of standard experimental rigor for the claimed level of significance. **The paper is not fatally weakened — the pattern of results is strong — but this is a genuine evidential gap that must be addressed.**

- **Inference procedure is underspecified.** The paper states: "We then aggregate semantic ID probabilities within each beam search result to obtain the next-item probabilities" (Section 2.3). It does not explain: (a) how beam search outputs are mapped back to items when an item can be represented by multiple semantic IDs, (b) how probabilities for the same item from different decoding paths are aggregated (average? max? sum?), and (c) whether evaluation is over the full item corpus or a sampled candidate set. The paper references Appendix C.2 and prior work (Rajput et al., 2023; Zheng et al., 2024) for evaluation details, but the main text should make the inference protocol self-contained enough for a reader to understand what is being reported. The reported Recall@10 values (0.06–0.09) are plausible for full-ranking evaluation on these Amazon subsets, but the ambiguity is a reproducibility concern.

### Minor

- **No sensitivity analysis for critical hyperparameters.** The method relies on several knobs: the fusion weight α, the frequency threshold τ for merging infrequent semantic IDs, the augmentation probability γ, and the cluster-count determination. None of these are analyzed for sensitivity. The ablation shows that removing redundant SID merging causes a catastrophic drop (e.g., Instrument Recall@5 from 0.0409 to 0.0270, below SASRec's 0.0333), indicating that the method's success depends heavily on how aggressive the merging is. A sensitivity plot over a range of τ values would substantially strengthen confidence that the reported results are not fragile.

- **The paper's own data shows personalization is concentrated on a small subset of IDs.** Figure 3 shows most items have only 1–3 semantic IDs. This is by design (the merging strategy prunes aggressively), and the paper acknowledges it. However, the fact that the base Pctx *without* merging performs *worse* than a static tokenizer (SASRec) on several metrics deserves more explicit discussion. The net benefit of personalization is achieved only after most personalized IDs are merged away, which raises the question: is the method primarily benefiting from a small number of strategically split items, rather than broad personalization? A quantitative analysis of how often the same item receives different SIDs in different contexts in the training data would directly address this.

- **Only one case study example.** The qualitative demonstration in Figure 4 is helpful, but a second example or a small-scale quantitative analysis (e.g., for items with 2+ SIDs, how often does the assigned SID flip when the same item appears in different user sequences?) would make the personalization claim more concrete.

### Trivial

- None that survive filtering. The paper is generally well-written and the formatting artifacts in the extracted text are parser issues, not author errors.

## Nice-to-Haves

- A brief analysis of how often the assigned semantic ID changes for the same item across different user contexts in the training data. This would directly quantify the degree of personalization and complement the qualitative case study.
- A short discussion of computational cost: how does the personalized tokenization affect training and inference time compared to TIGER or ActionPiece?

## Removed Points

These points were raised in the reviewer inputs but are removed for the stated reasons:

- *"The paper doesn't specify whether ranking is over all items or sampled."* → The paper explicitly cites Rajput et al. (2023) and Wang et al. (2024a) for evaluation settings and refers to Appendix C.2. Following established protocols from prior work is standard practice; the criticism is reasonable as a clarity request but inflated as a weakness.
- *"Potential overcomplication / too many components."* → The ablation study shows each component contributes; complexity that is justified by ablation is a design choice, not a weakness.
- *"Missing related works."* → I cannot verify missing citations without external knowledge; this is excluded per guidelines.
- *"Formatting/style nitpicks."* → Parser artifacts, not author errors.
- *"The method's success hinges on careful tuning of the merging threshold."* → This is a real observation but it is already covered under "no sensitivity analysis" above, so it is merged there rather than duplicated.

## Novel Insights

The most novel observation that emerges from the reviews is this: the ablation shows that DuoRec (worse next-item prediction accuracy) outperforms SASRec (better next-item prediction accuracy) as the context encoder for Pctx. This is a genuinely non-obvious finding that the paper itself highlights: contrastive sequence representations are more effective for personalization than high-accuracy prediction-oriented representations, because the task is to produce *distinguishable* context representations, not accurate next-item predictions. This insight could influence how auxiliary models are selected for representation learning in recommendation more broadly.

## Suggestions

1. **Report variances and number of runs.** Add standard deviations or error bars for Pctx and the top baselines (at least 3–5 random seeds), and clarify how the paired t‑test is conducted. If the protocol follows the standard leave-one-out evaluation (as is common in this literature), state this explicitly.
2. **Clarify the inference protocol.** Provide a short description or pseudocode of how beam search outputs are mapped to item probabilities and how ties between multiple semantic IDs of the same item are resolved.
3. **Add a sensitivity analysis** for the merging threshold τ (and optionally α and γ), showing that performance is stable over a reasonable range.
4. **Quantify token-level personalization.** For items with multiple SIDs, report the fraction of occurrences where different contexts lead to different SIDs being assigned. This would directly validate that the tokenizer actually implements context-dependent tokenization rather than just adding static duplicates.

## Score and Decision

**Calibration details:**

*Round-1 bracket (3.5–7.5)*: Weak-band anchors (avg 2.5–3.0) are tangential tokenization papers with fatal flaws; this paper is clearly stronger. Strong-band anchors (avg 8.0) are on unrelated LLM topics at exceptional quality; this paper does not reach that level.

*Round-2 narrowing*:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| IqGVIU4rvM — VQ-VAE+Diffusion Tokenizer for Image Gen | 2.50 | 1 | Much weaker: fundamental methodological errors, poor results. |
| z3DMFpaP6m — Entropy of LMs in Semantics from Tokens | 3.00 | 1 | Much weaker: tangential topic, minimal empirical contribution. |
| EMCXCTsmSx — IRGen (generative image retrieval) | 5.50 | 1 | Weaker: significant missing comparisons, unclear contributions; Pctx has stronger ablations and clearer writing. |
| bePaRx0otZ — URI (unified retrieval and indexing) | 6.00 | 1 | Slightly weaker: URI has missing sensitivity analysis and missing comparisons; Pctx's ablations are more thorough and the idea is more novel. |
| v7YrIjpkTF — MQL4GRec (multimodal quantitative language for GR) | 6.50 | 1,2 | Comparable: similar level of novelty, similar reporting gaps (statistical significance, implementation details). |
| Ke2BEL4csm — NCL-SR (non-contrastive learning for SR) | 6.50 | 2 | Comparable: thorough experiments, some missing implementation details; Pctx's problem formulation is arguably more novel. |
| 6GATHdOi1x — PreferDiff (diffusion for recommendation) | 5.75 | 2 | Weaker: more significant novelty concerns (high similarity to DPO), limited dataset diversity. |
| xQCXInDq0m — CoS (context steering for LLMs) | 6.67 | 2 | Comparable quality on a different topic; Pctx is similarly rigorous. |

The paper sits above URI (6.0) and PreferDiff (5.75) due to stronger novelty and ablations, and is comparable to MQL4GRec (6.5) and NCL-SR (6.5). Its weaknesses (missing variance reporting, underspecified inference, no sensitivity analysis) are real but addressable, and do not undermine the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>