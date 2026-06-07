Now I have a clear picture from the Round 2 anchors. Let me compile the final review.

**Round 1 bracket:** 5.0 – 7.0

**Round 2 narrowing:** Our paper is clearly stronger than StreamingBench (5.75, Reject — pure benchmark, limited novelty) and CL-WSVAD (5.71, Reject — unrealistic assumptions, limited generalizability). It is comparable to MiDl (6.00, Accept — novel problem formulation, well-motivated method, good experiments, but limited benchmarks and modest gains) and EgoVideo (6.00, Accept — similar structure with benchmark+method, limited component novelty). It is slightly below EgoHOIBench (7.00, Accept — stronger cross-model gains, more polished). 

Our paper's novel task formulation and thorough ablation make it clearly better than the 5.7-range papers, but the modest mAP gains and missing baselines prevent it from reaching 7.0 territory. **Final score: 6.0.**

---

## Summary
This paper introduces Continuous Online Action Detection (COAD), a task formulation extending online action detection to enable models to continuously learn from streaming egocentric video in a single pass without storing data. The authors curate Ego-OAD, a large-scale benchmark derived from Ego4D Moment Queries (87 classes, ~23K labeled instances, 263h of video), and propose three training strategies: state continuity across windows, orthogonal gradient projection, and non-uniform loss weighting. Experiments are conducted under a three-split protocol on Ego-OAD and EPIC-KITCHENS.

## Strengths
- **Novel and well-motivated task formulation**: COAD addresses a genuine gap between offline-trained OAD models and the demands of real-world egocentric deployment, where adaptation to dynamic, user-specific contexts is essential. The integration of single-pass training, orthogonal gradients, and non-uniform loss into a coherent streaming framework is clearly motivated.
- **Well-constructed large-scale benchmark**: Ego-OAD fills a gap in egocentric OAD evaluation with 87 classes, 22,991 labeled instances, and 263 hours of video across diverse everyday scenarios. The multi-label annotations with 36% action overlap capture realistic ambiguity, and the three-way split protocol is inherited from established continuous learning work (Carreira et al., 2024a).
- **Rigorous and honest ablation study**: Table 3 systematically isolates each component, revealing that non-uniform loss (+8.3 points out-of-stream Top-5 Recall) and orthogonal gradient projection (+4.5 points) are the key contributors. The ablation transparently shows state continuity contributes minimally — scientific honesty.
- **Convergence toward the IID upper bound**: Figure 4 provides compelling evidence that COAD steadily closes the gap to fully-supervised IID training as more in-stream data is processed, validating the core premise.
- **Meaningful Top-5 Recall improvements**: On Ego-OAD with egocentric pretraining, COAD improves out-of-stream Top-5 Recall by 6.9 points over Pretrained Only (69.1% → 76.0%) and in-stream by 16.0 points (73.3% → 89.3%).

## Weaknesses

### Fatal
None.

### Major
- **mAP improvements over the w/o COAD baseline are marginal, and in-stream mAP is worse**: On out-of-stream with egocentric pretraining, COAD achieves 26.0 mAP vs. 25.5 for w/o COAD — a gain of only 0.5 points. On in-stream, COAD (36.8 mAP) is *worse* than w/o COAD (39.0 mAP). While the paper frames COAD as balancing adaptation vs. generalization, the near-zero out-of-stream mAP gain and negative in-stream delta weaken the claim that the proposed strategies are clearly effective as a package. The headline improvements come almost entirely from Top-5 Recall; the mAP picture — the primary metric in prior OAD work — is substantially less favorable. The paper should either demonstrate stronger mAP gains or make a more explicit case for why Top-5 Recall is the more informative metric.

### Minor
- **State continuity contributes negligibly**: Table 3 shows removing state continuity changes out-of-stream mAP from 26.0 to 25.9 and Top-5 Recall from 76.0 to 75.8 — differences well within experimental noise. While the ablation honestly notes this, the method section (Section 4.5) describes state continuity in strong terms ("improves temporal coherence and enables effective long-term reasoning") that do not align with the empirical evidence. This is a narrative-coherence issue.
- **No comparison to standard continual learning baselines**: The paper introduces a continual learning task but does not compare against well-established methods (e.g., EWC, SI, LwF) compatible with single-pass streaming. The orthogonal gradient projection is adopted from Han et al. (2025) without benchmarking against these alternatives, making it difficult to assess whether COAD's strategies are genuinely superior to off-the-shelf continual learning techniques.
- **EPIC-KITCHENS in-stream results are weak and under-analyzed**: On EPIC-KITCHENS action categories, COAD's in-stream mAP (7.9) is worse than Pretrained Only (9.6). The paper attributes this to "fine-grained nature of the actions" in a single sentence. A diagnostic analysis would strengthen the cross-dataset validation.

### Trivial
- No error bars, multiple seeds, or variance estimates are reported. While single-run evaluation is common for large-scale video benchmarks, variance reporting would help distinguish signal from noise for small-magnitude comparisons.

## Nice-to-Haves
- User-disjoint splits would better align the evaluation with the paper's personalization framing. Currently the splits follow the Ego4D MQ validation partitioning, meaning the same user can appear across splits.
- A longer-stream experiment or analysis of when state continuity becomes important would contextualize the negative ablation result.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *Harsh Critic claim that "up to 20% in top-5 accuracy" is misleading*: The paper correctly reports absolute percentage-point differences, which is standard. The "up to" language accurately describes the maximum observed gain (~22.5 points in exocentric pretraining, in-stream). Not misleading.
- *Harsh Critic claim that "personalized egocentric AI systems" is an overclaim*: The paper uses "personalized" to refer to adaptation to the deployment stream, not to cross-user identity. Reasonable in the on-device learning context.
- *Harsh Critic claim that qualitative results (Fig. 5) are "cherry-picked"*: Generic criticism; qualitative examples are inherently illustrative.
- *Strength Finder claim that state continuity "adds a smaller but consistent gain"*: The gain is within noise; corrected in the final review.
- *Strength Finder claim that EPIC-KITCHENS results corroborate Ego-OAD without qualification*: Gains are real but modest; the final review acknowledges this.
- *Harsh Critic claim that "w/o COAD" includes state continuity*: Incorrect. The paper defines "w/o COAD" as training without any of the three proposed strategies, including state continuity.

## Novel Insights
The most interesting empirical finding is the interaction between non-uniform loss weighting and the other components. Table 3 shows uniform loss combined with orthogonal gradients and state continuity actually *underperforms* (out-of-stream Top-5 Recall drops from 76.0 to 67.7), suggesting non-uniform loss is not merely additive but an enabler for the other strategies. The trade-off analysis (Figure 3), showing models improve with supervision as sparse as once every ~68 seconds, is also practically valuable for deployment.

## Suggestions
- Add at least one standard continual learning baseline (e.g., EWC) to calibrate the orthogonal gradient contribution.
- Either find a regime where state continuity matters (longer streams, different architecture) or honestly reframe it as a conceptual element that does not yet show empirical value in tested settings.
- Expand the EPIC-KITCHENS analysis with diagnostics: is the in-stream failure due to class granularity, shorter streams, or domain gap?
- Report variance across 2-3 seeds to help assess reliability of small-magnitude comparisons.

---

### Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| VidEgoThink | Z5nqeTH24j | 4.40 | R1 | Our paper is stronger: larger-scale benchmark, method contribution, better empirical validation |
| EgoVideo | P6G1Z6jkf3 | 6.00 | R1 | Comparable in structure and contribution level; similar component-novelty concerns |
| EgoHOIBench | M8gXSFGkn2 | 7.00 | R1 | Slightly below: EgoHOIBench has stronger cross-model gains and more polished results |
| StreamingBench | qnAZqlMGTB | 5.75 | R2 | Our paper is stronger: includes method, more thorough ablation, larger benchmark |
| CL-WSVAD | Y7jJN0VQ4y | 5.71 | R2 | Our paper is stronger: more realistic task assumptions, larger benchmark, better ablation |
| MiDl | 1L52bHEL5d | 6.00 | R2 | Comparable: similar problem-formulation contribution, similar-level weaknesses |

**Round 1 bracket:** 5.0–7.0. **Round 2 narrowed to:** 6.0 — the paper sits squarely with EgoVideo and MiDl at 6.0: solid contribution with real but non-fatal weaknesses that prevent it from reaching 7.0 territory.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>