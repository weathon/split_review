Now I have enough calibration data. Let me finalize the review.

**Calibration comparison:**
- PARSE-Ego4D (5.50, rejected): Egocentric benchmark from Ego4D, mainly a dataset contribution with minimal methodological novelty. Our paper has both a benchmark AND a method with thorough ablation → our paper is stronger.
- MMEgo (6.00, accepted): Egocentric multimodal LLM with data engine, benchmark, and model. More breadth but our paper has clearer methodological contribution with systematic ablation → comparable quality.
- Video CL with Bootstrapped Compression (4.50, rejected): Video continual learning, weaker baseline evaluation. Our paper has better motivation, cleaner task formulation, better ablation → our paper is stronger.
- Anomalies are Streaming (5.71, rejected): Continual learning for video anomaly detection. Similar structure but our paper has better ablation and a larger benchmark → our paper is somewhat stronger.

**Round-1 bracket**: 4.5–7.0. **Round-2 narrowing**: 5.5–6.5. **Final score**: 6.0.

The paper is clearly better than the 4.50–5.0 range anchors (which were rejected for weaker methodology and evaluation) but comparable to the 6.0 MMEgo anchor. The main limiter preventing a higher score is the absence of alternative continual learning baselines, which prevents the reader from understanding if COAD's specific strategies are genuinely superior to generic alternatives. However, the thorough ablation partially addresses this by demonstrating that each component contributes meaningfully.

---

## Summary
This paper introduces Continuous Online Action Detection (COAD), a task formulation enabling models to continuously learn from streaming egocentric video after deployment using single-pass training without data storage. The authors curate Ego-OAD (87 action classes, 263h from Ego4D) and adapt an RNN-based OAD model with three strategies: state continuity, orthogonal gradient projection, and non-uniform loss weighting. Experiments on Ego-OAD and EPIC-KITCHENS evaluate both adaptation and out-of-stream generalization.

## Strengths
- **Well-motivated task formulation and benchmark**: COAD is a practically relevant extension of OAD to continuous learning, and Ego-OAD (87 classes, 22,991 instances, 263h, 36% action overlap) fills a genuine gap beyond kitchen-only datasets like EPIC-KITCHENS. The curation process—merging annotation passes and manually grouping semantically similar actions—is described in Section 3.
- **Thorough component ablation (Table 3)**: Systematically evaluates all combinations of the three COAD strategies. The full method achieves best out-of-stream generalization (26.0 mAP, 76.0 Top-5 Recall), with non-uniform loss being most impactful (−4.2 mAP, −8.3 Top-5 Recall when removed), and orthogonal gradient contributing +4.5% Top-5 Recall.
- **Consistent out-of-stream generalization gains (Table 1)**: COAD improves out-of-stream Top-5 Recall over Pretrained Only by +6.9% (ego) and +6.5% (exo), substantially outperforming w/o COAD (+2.5% and +2.3%). Figure 4 shows steady improvement approaching the IID upper bound during single-pass training.
- **Insightful trade-off analysis (Figure 3)**: Demonstrates that higher strides (~68s between supervision) maintain strong out-of-stream generalization with minimal in-stream supervision, providing practical guidance for resource-constrained deployment.

## Weaknesses

### Fatal
None.

### Major
- **No comparison to standard continual learning baselines**: The only baselines are "Pretrained Only" (no adaptation) and "w/o COAD" (naive adaptation without any COAD strategies). There are no comparisons to established continual learning methods (EWC, experience replay, learning rate regularization, etc.) or to other OAD architectures (transformer-based models like LSTR/TeSTra) in the COAD setting. Table 3 shows w/o COAD already provides substantial in-stream improvements (+14.9 mAP, +13.4 Top-5 Recall), meaning much of the gain may stem from *any* continual adaptation rather than the specific COAD strategies. The orthogonal gradient projection is from Han et al. (2025) and the non-uniform loss from An et al. (2023); without alternative baselines, the paper cannot demonstrate that these are better than generic continual learning approaches for this task.

- **In-stream degradation on EPIC-KITCHENS Action**: On EPIC-KITCHENS Action in-stream, COAD underperforms Pretrained Only on both mAP (7.9 vs. 9.6) and Top-5 Recall (20.5 vs. 22.9) per Table 2. Since EPIC-KITCHENS is one of only two evaluation benchmarks and in-stream adaptation is a core claim, this is concerning. The paper attributes it to "fine-grained nature of the actions" but provides no deeper diagnostic (e.g., per-class analysis, failure mode categorization) to explain when and why the method fails.

### Minor
- **Abstract headline numbers do not match reported results**: The abstract claims "up to 20% in top-5 accuracy" for adaptation. From Table 1, the in-stream improvements over Pretrained Only are Δ = 16.0 (Ego Top-5 Recall) and Δ = 22.5 (Exo Top-5 Recall). Neither is exactly 20%, and the abstract says "accuracy" while the metric is "Top-5 Recall." The generalization claim of "up to 7%" matches Δ = 6.9 for Ego out-of-stream Top-5 Recall, but if these are absolute values, the adaptation number should be "up to 22.5%" or "~16–23%"; if relative, both should be relativized consistently. The authors should align abstract claims with actual reported numbers.

- **"CODA" typo (line 66)**: "Continuous OAD (CODA)" should be "Continuous OAD (COAD)."

### Trivial
None.

## Nice-to-Haves
- Statistical significance or variance over multiple runs would strengthen confidence, given small pretraining sets (186 videos for Ego-OAD, 293 for EPIC-KITCHENS).
- Sensitivity analysis on pretraining set size (186 vs. 1,177 in-stream) would clarify how pretrained model quality affects downstream results.
- Inter-annotator agreement metrics for the Ego-OAD manual action class grouping would strengthen the benchmark contribution.
- Per-class analysis on EPIC-KITCHENS to understand which action categories COAD helps or hurts would be informative.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Formatting/style nitpicks beyond the CODA typo — parser artifacts, not paper issues.
- Claims about missing related works — cannot verify external literature existence.
- The harsh critic's suggestion that Table 4 (feature extractor comparison) is tangential — Table 4 provides useful architectural insight (clip-level vs. frame-level features) directly relevant to OAD deployment, and is a reasonable supporting experiment.

## Novel Insights
The paper's most notable insight is that non-uniform loss (supervising only the final frame of each window) is the single most impactful component for out-of-stream generalization in continuous video learning, while orthogonal gradient projection is critical for Top-5 Recall. The finding that models can maintain strong out-of-stream generalization even with very sparse supervision (~68 seconds between loss signals, stride 128 in Figure 3) is practically valuable for resource-constrained wearable device deployment and suggests that annotation efficiency and generalization can be jointly optimized in the COAD setting.

## Suggestions
- Add comparisons to at least 2–3 standard continual learning baselines (e.g., EWC, experience replay with small buffer, learning rate regularization) to demonstrate that COAD's specific strategies outperform generic alternatives — this is the single most important improvement.
- Investigate the EPIC-KITCHENS in-stream Action failure more deeply (e.g., per-class breakdown, comparison of action granularity between datasets) to clarify the method's boundaries.
- Correct the abstract to align with reported numbers: specify "Top-5 Recall" and match the absolute improvement values.

## Calibration Anchors Retrieved

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| WM5G2NWSYC.md | 2.00 | 1 | Weak: projected subnetworks for continual learning, much less relevant and weaker methodology |
| JIlIYIHMuv.md | 2.50 | 1 | Weak: LVLM continual learning, different domain and weaker contribution |
| 2HdZPEQUig.md | 3.00 | 1 | Weak: efficient object-centric video learning, less relevant |
| 10fsmnw6aD.md | 2.50 | 1 | Weak: class incremental learning, weaker evaluation |
| Y7jJN0VQ4y.md | 5.71 | 1&2 | Middle: continual learning for video anomaly detection, similar structure but weaker ablation → our paper is somewhat stronger |
| 7L2bpe7lfm.md | 4.50 | 1&2 | Middle: large-scale video continual learning, weaker baseline evaluation and novelty issues → our paper is stronger |
| jawV7vhGHw.md | 4.25 | 1 | Middle: online video classification, less directly relevant |
| A18zU6cgQ0.md | 4.20 | 1 | Middle: video anomaly detection, different setting |
| 6r0BOIb771.md | 5.33 | 2 | Middle: sequential Bayesian continual learning, theoretical focus |
| YGflij9S6x.md | 4.25 | 2 | Middle: continual learning with contrastive replay, weaker contribution |
| SctfBCLmWo.md | 8.00 | 1 | Strong: dataset bias analysis, broader impact than our paper |
| 7gUrYE50Rb.md | 8.00 | 1 | Strong: embodied QA, more comprehensive multimodal contribution |
| 9Cu8MRmhq2.md | 8.00 | 1 | Strong: long-term video-language correspondence, more novel methodology |
| Q6a9W6kzv5.md | 8.00 | 1 | Strong: VLM physical understanding benchmark, larger scale |
| M8gXSFGkn2.md | 7.00 | 2 | Upper-middle: egocentric video-language model with benchmark, broader scope |
| Kh5OS3oNlg.md | 5.50 | 2 | Middle: PARSE-Ego4D, egocentric benchmark — mostly dataset, less method → our paper is stronger |
| 67sSPPAZiG.md | 6.00 | 2 | Middle-upper: MMEgo, egocentric multimodal LLM with benchmark → comparable quality |
| vlg5WRKHxh.md | 7.00 | 2 | Upper-middle: F3Set benchmark for fine-grained events, more comprehensive |

**Bracket rationale**: The paper is clearly stronger than the 4.0–5.5 range anchors (which were rejected for weaker evaluation, limited novelty, or narrower contribution) but comparable to the 6.0 anchor (MMEgo, accepted). It falls below the 7.0+ anchors which typically have broader scope or more novel methodology. The absence of alternative continual learning baselines is the primary factor preventing a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>