## Summary

This paper introduces Continuous Online Action Detection (COAD), a task formulation that extends standard online action detection (OAD) by enabling models to continuously learn from streaming egocentric videos in a single causal pass without data storage. The method combines three components: maintaining RNN hidden state continuity across streaming windows, orthogonal gradient projection to reduce correlation between consecutive gradient updates, and non-uniform loss weighting (loss only at window end). To support evaluation, the authors curate Ego-OAD, a large-scale benchmark from Ego4D Moment Queries covering 263 hours, 87 action classes, and 22,991 labeled instances. Results on Ego-OAD and EPIC-KITCHENS demonstrate gains in both in-stream adaptation and out-of-stream generalization over a model trained offline on the pretraining set.

---

## Strengths

- **Well-motivated problem formulation.** The COAD task is grounded in a genuine practical gap: OAD models trained offline must operate on dynamic, user-specific egocentric streams under resource constraints. The alignment between the in-stream training regime and actual deployment conditions is a sound conceptual contribution.
- **Substantial dataset contribution.** Ego-OAD provides 263 hours of diverse first-person video with 87 fine-grained action classes and 22,991 temporally grounded multi-label instances—a considerable improvement over existing egocentric OAD datasets in scale and diversity.
- **Thorough ablation study.** Table 3 disentangles the effects of state continuity, orthogonal gradient projection, and non-uniform loss weighting. Figure 3 systematically maps the in-stream vs. out-of-stream trade-off across learning rate and stride hyperparameters, and Figure 4 tracks the evolution of out-of-stream performance over training, showing steady convergence toward an IID upper bound.
- **Label-efficiency insight.** The paper shows (Figure 3, stride=128) that COAD retains near-full out-of-stream performance when a ground-truth label is seen approximately once every 68 seconds, which is practically significant for annotation-scarce deployment.

---

## Weaknesses

### Fatal
None.

### Major

1. **EPIC-KITCHENS in-stream results undermine generality.** In Table 2, both w/o COAD and COAD fail to improve over Pretrained Only in several in-stream metrics (Verb in-stream: Pretrained 29.0, COAD 29.0; Noun in-stream: Pretrained 3.8, COAD 3.9; Action in-stream: Pretrained 9.6, COAD 7.9). The w/o COAD baseline is substantially worse than Pretrained Only in-stream for all categories. The paper attributes this to "fine-grained annotation difficulty" but provides no ablation, alternative protocol, or deeper diagnostic on EPIC-KITCHENS. A second dataset is expected to corroborate the core claim, not merely survive it.

2. **Limited methodological novelty; borrowed components lack application-specific justification.** All three technical components are adapted directly from prior work: non-uniform loss from MiniROD (An et al., 2023), orthogonal gradient projection from Han et al. (2025), and the overall continuous video learning framework from Carreira et al. (2024a/b). The paper does not provide ablations or discussions that show the OAD context requires these components differently than their original settings. Crucially, there is no direct performance comparison against Carreira et al. (2024a/b) despite COAD being positioned as their adaptation to OAD.

3. **In-stream mAP degradation with COAD.** In the egocentric backbone setting (Table 1 in-stream), COAD achieves 36.8 mAP vs. 39.0 mAP for w/o COAD—a non-trivial 2.2-point drop. While COAD is presented as balancing adaptation and generalization, the in-stream cost is non-negligible and the paper does not adequately analyze when sacrificing in-stream mAP for generalization is justified.

### Minor

1. **Asymmetric data splits may inflate COAD's relative gains.** Assigning 1,177 videos to in-stream vs. only 186 to pretraining yields a weak Pretrained Only baseline by design. While the rationale is stated, the effect of this split ratio on the claimed deltas (Δ mAP, Δ Recall) is not analyzed.

2. **State continuity contributes negligibly in ablation.** Table 3 shows that removing state continuity changes out-of-stream mAP by only 0.1 (26.0 → 25.9) and recall by 0.2 (76.0 → 75.8). Despite being described as a key COAD component enabling "long-term reasoning," its marginal contribution is not reconciled with this framing.

3. **Quantitative claims in abstract lack precision.** "Up to 20% in top-5 accuracy" appears to refer to the in-stream exocentric Δ Top-5 Recall of 22.5%, yet the abstract does not specify which split or backbone, making verification non-trivial.

### Trivial
None worth noting.

---

## Nice-to-Haves

- A direct comparison to Carreira et al. (2024a) under a common protocol would clarify how much of COAD's performance stems from adapting their framework versus OAD-specific innovations.
- Discussion of actual inference latency and memory footprint for on-device deployment (the core motivation) would strengthen the practical case.
- Analysis of failure modes—particularly why COAD struggles in-stream on EPIC-KITCHENS—would deepen understanding of when the approach generalizes.

---

## Novel Insights

The most transferable insight is the empirical finding that OAD-specific non-uniform loss weighting (computing loss only at each window's final step) disproportionately benefits out-of-stream generalization in the continuous learning regime, outweighing both gradient decorrelation and state continuity as a standalone component (Table 3). This suggests that decoupling the temporal supervision density from the temporal context window is a particularly effective design choice for preventing overfitting to correlated in-stream samples—a finding that goes slightly beyond what An et al. (2023) observed in the standard IID OAD setting.

---

## Suggestions

- Investigate why in-stream adaptation fails on EPIC-KITCHENS: is it the fine-grained label space, the shorter video durations in the in-stream split, or the TSN features? A mini-ablation (e.g., grouping verbs/nouns into coarser categories) would distinguish these.
- Report wall-clock time per training step and memory consumption for COAD vs. offline training to concretely validate on-device feasibility claims.
- Vary the pretraining split size to decouple the effect of data allocation from the COAD training strategy itself.
- Provide a direct protocol-aligned comparison to Carreira et al. (2024a), even on a shared subset.

---

## Score and Decision

COAD is a well-motivated task formulation with a substantial dataset contribution and a competent experimental framework. The Ego-OAD benchmark alone has clear value for the community. However, the method's novelty is limited—all components are borrowed and the paper offers limited insight into why or when they need adaptation for OAD—and the EPIC-KITCHENS results raise unresolved questions about generality. The in-stream mAP regression under full COAD relative to the naive baseline is a real trade-off that deserves deeper treatment.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>