## Summary

This paper presents a system for language-based audio retrieval on the CLOTHO dataset using a dual encoder architecture augmented with three techniques: (1) soft-label distillation from a pretrained ensemble of audio-text models, (2) LLM-driven caption augmentation via back-translation and mixed-audio captioning, and (3) cluster-guided auxiliary classification using BERTopic-derived pseudo-labels. The best single model reaches mAP@16 46.6 and a weighted ensemble attains 48.8 on the CLOTHO development test split.

---

## Strengths

- **Systematic ablation across three audio backbones**: Testing PaSST, EAT, and BEATs provides evidence that findings are not backbone-specific and the improvements from distillation and augmentation are consistent (SID 1 → 3, across all three backbones).
- **LLM-based mixed-audio caption generation**: Generating 50,000 new audio-text pairs by mixing audio signals and prompting GPT-4o to merge captions is a practical and reproducible augmentation strategy, and it produces consistent gains (SID 2 → 3: +0.2–0.8 mAP@16).
- **Honest reporting of mixed results**: The paper clearly states that cluster guidance yields mixed gains, including cases where SID 4/5 slightly underperform SID 3, avoiding over-claiming.

---

## Weaknesses

### Fatal
*(None that outright invalidate the core claims.)*

### Major

1. **Central novel contribution shows negligible and mixed results.** The only component the paper presents as novel—cluster-guided auxiliary classification (SID 4, 5)—barely moves the needle. For PaSST: SID 3 (46.41 mAP@16) vs. SID 4 (46.39) vs. SID 5 (46.50). For EAT: SID 3 (46.05) vs. SID 4/5 (both 45.34). For BEATs: SID 3 (44.66) vs. SID 4 (44.58) vs. SID 5 (43.88). The cluster head actually hurts EAT and BEATs. With differences of 0.0–0.8 mAP@16 and no statistical uncertainty reported, the paper cannot convincingly support the claim that cluster-guided classification "contributes to additional performance gains."

2. **Primary gain is entirely from prior work.** The dominant improvement is the transition from SID 1 to SID 2 (+4.5 mAP@16 for PaSST), which the paper explicitly credits to Primus et al. (2024), the DCASE 2024 Task 8 winner. The paper offers no new insight into *why* or *when* soft-label distillation works well; it merely applies it as a recipe.

3. **No comparison to published state-of-the-art methods.** All comparisons are internal ablations between variants of the same system. There is no table comparing the proposed approach to other published methods on CLOTHO (e.g., prior DCASE submissions or published cross-modal retrieval systems). Without such a baseline, it is impossible to assess the contribution's position in the broader landscape.

4. **Single-dataset evaluation.** All experiments are on CLOTHO only. It is unclear whether any of the three proposed components generalize beyond this specific dataset, undermining the paper's claim of improving "robustness."

### Minor

1. **Cluster ablation is underdeveloped.** The abstract promises "ablations on topic granularity," but Table 2 only compares two cluster sources (finetuned model vs. BERTopic), not different numbers of clusters. The theoretical basis for why audio-topic alignment would help retrieval is also underdeveloped.

2. **Ensemble weight selection is opaque.** The coefficients in Table 3 (e.g., E1: SID4-PaSST=0.325, SID4-EAT=0) appear to come from a grid search on the validation set, but the search space and selection criterion are not described, raising concerns about overfitting to the validation set.

3. **No uncertainty quantification.** No confidence intervals or multiple-run variance are reported. Given the small performance differences between SID 3–5, statistical significance is essential to the claims.

### Trivial
*(None worth listing given the major issues above.)*

---

## Nice-to-Haves

- An ablation varying the number of BERTopic clusters to understand sensitivity.
- Comparison to the Primus et al. baseline and at least one other published CLOTHO retrieval system to contextualize absolute numbers.
- Analysis of which cluster assignment source (finetuned model vs. BERTopic) captures semantically meaningful groupings and why one might be preferred.

---

## Novel Insights

The combination of LLM-driven mixed-audio caption generation with soft-label distillation is a sensible engineering workflow: mixing audio at the signal level and generating a coherent joint caption with a generative LLM adds plausible training diversity without manual annotation. However, this combination is a straightforward integration of Wu et al. (2024) and Primus et al. (2024), and the paper does not provide analysis explaining *why* caption mix helps or which types of audio ambiguity it resolves. None beyond the paper's own engineering contribution.

---

## Suggestions

- Replace the cluster classification ablation (SID 4 vs. 5) with a stronger analysis: vary cluster count from 5 to 200, plot mAP@16 vs. granularity, and identify whether there is a sweet spot.
- Add a comparison table with at least three published CLOTHO retrieval systems to enable readers to judge absolute progress.
- Report mean and standard deviation over 3 runs to address the statistical uncertainty issue around the cluster component's mixed gains.
- Analyze the LLM mix pairs qualitatively: show examples where mixing and caption generation adds meaningful training signal versus degenerate cases.

---

## Score and Decision

This is a competition-style system description paper presenting three components, two of which (distillation, back-translation) are directly from prior work, and one of which (cluster-guided classification) shows mixed, marginal, and often negligible effects. The paper is short, evaluated on a single dataset without comparison to published methods, and the main novelty claim is not convincingly supported by the experiments. While the engineering is solid and the ablation is honest, the contribution does not meet the bar for an ICLR main-track paper.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>