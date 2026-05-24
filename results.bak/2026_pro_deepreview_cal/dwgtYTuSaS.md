Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper introduces Continuous Online Action Detection (COAD), a task formulation extending online action detection to enable models to learn from streaming video after deployment under causal, single-pass, no-replay constraints. The authors curate Ego-OAD, a large-scale benchmark (263h, 87 classes, 22,991 instances) from Ego4D Moment Queries annotations, and propose training strategies — state continuity, orthogonal gradient projection, and non-uniform loss weighting — that improve both in-stream adaptation and out-of-stream generalization. Experiments on Ego-OAD and EPIC-KITCHENS demonstrate moderate but consistent gains over pretrained-only and naive-continuous-training baselines.

## Strengths

- **Well-motivated task formulation**: The COAD framework (Section 4.5) concretely defines single-pass, causal, memory-constrained training on continuous video streams, directly addressing the mismatch between standard offline OAD training and real-world deployment on resource-constrained wearable devices. The constraints (no future frames, no replay, hidden state continuity) are clearly specified and practically grounded.

- **Large-scale, useful benchmark**: Ego-OAD provides 263 hours of egocentric video with 87 action classes and 22,991 temporally grounded, multi-label action instances (36% overlapping). Curated systematically from Ego4D MQ annotations with semantic grouping of free-form descriptions, this fills a genuine gap — publicly available egocentric OAD benchmarks are scarce. The scale and diversity make it a valuable resource for the community.

- **Clear experimental gains on out-of-stream generalization**: COAD with egocentric pretraining achieves +5.9 mAP and +6.9 Top-5 Recall on out-of-stream data over the pretrained-only baseline (Table 1), and +4.4 Top-5 Recall over the naive continuous-training baseline (w/o COAD). These gains, while moderate, are consistent across pretraining types (ego/exo) and across the EPIC-KITCHENS validation (Table 2), supporting the claim that the training strategies enable effective continuous learning without overfitting.

- **Informative ablation and trade-off analysis**: Table 3 isolates each component's contribution, showing non-uniform loss as the strongest individual factor (+4.2 mAP, +8.3 Top-5 Recall) and orthogonal gradient adding a further +4.5 Top-5 Recall. Figure 3's stride-vs-LR analysis reveals robustness to sparse supervision — at stride 128 (supervision every ~68s), out-of-stream performance degrades minimally, which is an important practical property.

## Weaknesses

### Fatal

None.

### Major

- **Overclaimed personalization narrative**: The paper repeatedly frames its contribution around "adaptation to individual users," "personalized egocentric AI," and "user-specific environments" (abstract, introduction, contributions list). However, the evaluation does not test per-user adaptation: the in-stream metric is computed on the same data the model adapts to (effectively measuring training fit, not generalization to a specific user's future behavior), and the out-of-stream set is a general held-out split, not unseen data from a user the model has adapted to. The experimental design evaluates online adaptation from streaming data — which is a valuable contribution — but does not support claims about personalization or user-specific adaptation. This mismatch between stated motivation and experimental evidence is a significant framing problem that weakens the paper's contribution as presented.

### Minor

- **Limited analysis of component interactions**: Table 3 reveals that state continuity + orthogonal gradient without non-uniform loss performs worse on out-of-stream mAP (21.8) than having no components at all (25.5). The paper notes this in passing ("uniform loss, effective alone, underperforms when combined with other components") but provides no diagnosis of why. Understanding this interaction would increase trust in the method's robustness and help practitioners avoid brittle configurations.

- **EPIC-KITCHENS adaptation failure underexplored**: On EPIC-KITCHENS, COAD fails to improve in-stream adaptation (Table 2), which the paper attributes to "fine-grained nature of the actions and annotations." While this is a plausible explanation, the paper misses an opportunity to analyze whether specific COAD components (e.g., orthogonal gradient decorrelation on highly similar consecutive actions, non-uniform loss with sparse fine-grained labels) are responsible, which would illuminate the method's boundary conditions.

- **No inter-annotator agreement or class distribution statistics for Ego-OAD**: The paper notes that Ego4D MQ annotations come from "multiple annotation passes from independent annotators, who may disagree on the precise temporal boundaries or even on the action labels" and merges them by taking the union. No inter-annotator agreement statistics or class-distribution analysis are provided, making it difficult to assess label noise and class imbalance — factors that directly affect benchmark difficulty and reliability.

### Trivial

- The paper title contains a typo: "Countinuous" in the contributions list (Section 1).

## Nice-to-Haves

- A comparison or discussion of why standard continual-learning strategies (replay buffers, elastic weight consolidation, etc.) are inapplicable or suboptimal under COAD's strict no-storage, single-pass constraints would strengthen the methodological framing.
- A per-user evaluation split — e.g., holding out a portion of each user's future data for testing adaptation to that specific user — would substantiate the personalization claims the paper currently makes without evidence.
- Computational cost analysis of the orthogonal gradient projection step, which is relevant to the resource-constrained wearable-device deployment scenario the paper motivates.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The core method components are lifted directly from prior work" (from Harsh Critic)**: REMOVED as a standalone weakness. The paper explicitly cites Han et al. (2025) for orthogonal gradient projection and An et al. (2023) for non-uniform loss, and presents them as adapted from prior work, not as novel inventions. The contribution lies in their combination and adaptation to the OAD streaming setting, which is a reasonable level of novelty for a task/benchmark paper. The lack of comparison against alternative continual-learning methods is addressed in Nice-to-Haves rather than as a major methodological gap.

- **"Out-of-stream split is still drawn from the same overall dataset collection, so the claim of 'unseen environments' is inflated" (from Harsh Critic)**: REMOVED. The paper never claims "unseen environments" — it uses "out-of-stream" and "unseen data" which are standard held-out-set terminology. The out-of-stream split is a proper held-out set disjoint from pretraining and in-stream data.

- **"In-stream metric is effectively training-set evaluation" (from Harsh Critic)**: PARTIALLY RETAINED but merged into the Major weakness about overclaimed personalization. The in-stream metric is presented transparently as measuring adaptation during training, which is fine as one axis of evaluation. The problem is not the metric itself but the framing of it as evidence for "personalization to the user's environment."

- **Demand for deeper analysis of why non-uniform loss works (from Harsh Critic)**: MOVED to Nice-to-Haves. The paper provides a plausible motivation (reducing train-inference mismatch, label efficiency) and the ablation demonstrates the effect empirically. While further analysis would strengthen the paper, this is not a flaw.

- **"No quantitative sensitivity analysis of window stride and learning rate beyond the figure" (from Harsh Critic)**: REMOVED. Figure 3 already provides a quantitative sensitivity analysis across stride and learning rate values with both mAP and Top-5 Recall.

- **"No discussion of computational cost of orthogonal gradient projection" (from Harsh Critic)**: Retained as Nice-to-Have rather than a weakness.

## Novel Insights

The consolidation of reviews does not yield insights beyond the paper's own contributions. The core tension — that COAD makes a genuine task-level contribution (continuous, streaming adaptation for OAD) and provides a useful benchmark, but overclaims the personalization angle — is apparent from the paper itself and is simply validated by cross-referencing the evaluation against the stated claims.

## Suggestions

- Reframe the paper around online adaptation from streaming video, dropping or significantly toning down claims about personalization and user-specific adaptation. The experiments support "continuous online adaptation improves generalization" but not "personalized egocentric AI." This reframing would align the motivation with the evidence and make the paper substantially stronger.
- Add a brief analysis of why state continuity + orthogonal gradient without non-uniform loss underperforms (Table 3). Even a hypothesis-driven discussion (e.g., dense per-frame supervision creates gradient conflicts that orthogonal projection alone cannot resolve) would help readers understand the method's internal logic.
- Include basic class-distribution statistics for Ego-OAD in the main text. A table or histogram of per-class instance counts would help users understand benchmark difficulty and potential biases.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| PARSE-Ego4D (Kh5OS3oNlg) | 5.50 | R2 | Our paper has more substance (benchmark + method vs. annotations only) |
| CL-WSVAD (Y7jJN0VQ4y) | 5.71 | R2 | Similar: new task + method, both have framing/methodological weaknesses |
| StreamingBench (qnAZqlMGTB) | 5.75 | R1/R2 | Benchmark only; our paper adds a method |
| StreamChat (JbPb6RieNC) | 5.80 | R1/R2 | Both benchmark + method; StreamChat's method is more novel, ours has larger benchmark |
| EgoVideo (P6G1Z6jkf3) | 6.00 | R2 | Stronger methodological novelty |
| MMEgo (67sSPPAZiG) | 6.00 | R2 | Larger-scale contribution (7M QA pairs, novel architecture) |
| EgoHOIBench (M8gXSFGkn2) | 7.00 | R1 | Clearly stronger: more novel method, deeper analysis, larger gains |

**Bracket from Round 1:** 5.0–7.0.  
**Narrowed from Round 2:** 5.5–6.0.

The paper sits near the lower end of this narrow bracket. It is comparable to CL-WSVAD (5.71) in having a well-motivated new task formulation with moderate methodological novelty and some framing issues, and slightly below StreamChat (5.80) which has more methodological novelty but a smaller benchmark. The overclaiming about personalization — a central framing element — is a real weakness that pulls the score down from what would otherwise be a solid 6.0. The paper is clearly stronger than PARSE-Ego4D (5.50, annotations only) but clearly weaker than EgoHOIBench (7.0, more novel method, stronger analysis).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>