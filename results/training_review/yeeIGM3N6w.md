Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes HC-SMoE, a retraining-free, task-agnostic framework for reducing the number of experts in Sparse Mixture-of-Experts (SMoE) models. The method uses hierarchical clustering (average linkage) on averaged expert outputs to group functionally similar experts, then merges within each cluster via frequency-weighted averaging. Experiments on Qwen1.5-MoE-A2.7B (60 experts) and Mixtral 8×7B (8 experts) across eight zero-shot NLP tasks show that HC-SMoE consistently outperforms pruning baselines (O-prune, S-prune, F-prune) and an existing merging baseline (M-SMoE) at 25% and 50% reduction rates.

## Strengths

- **Well-motivated problem and clearly described approach.** The paper correctly identifies that expert redundancy exists in SMoE models and that existing merging methods (M-SMoE) rely on router-logit-based grouping, which is brittle in task-agnostic settings. The use of averaged expert outputs as a similarity metric is grounded in the observation that functionally similar experts produce similar outputs (citing convergent learning literature), and the hierarchical clustering framework is clearly described.

- **Comprehensive ablation study isolating each component.** The paper systematically ablates three design choices: (a) similarity metrics (router-logits vs. weights vs. expert-outputs), (b) clustering methods (hierarchical with three linkage types vs. K-means vs. one-shot grouping), and (c) merging strategies (average vs. frequency-weighted vs. fixed-dominant). The ablation results in Table 3 demonstrate that average linkage + expert-outputs yields the best average (0.5459 on Qwen 45×2.7B), while the same clustering with router-logits collapses to 0.3153 — cleanly supporting the claim that output-based metrics are superior. The comparison against K-means (Tables 4–5) and one-shot grouping (Table 6) shows that HC-SMoE achieves higher and more stable performance, with the advantage being particularly clear on Qwen 30×2.7B (0.4993 vs. best K-means at 0.4518, a 4.75-point gap).

- **Consistent positive results across two model families and two reduction ratios.** On Qwen 45×2.7B, HC-SMoE (avg) achieves 0.5716 vs. the best baseline F-prune at 0.5502 (+2.14 points). On Qwen 30×2.7B, it achieves 0.5223 vs. F-prune at 0.4528 (+6.95 points). On Mixtral 6×7B, it achieves 0.6425 vs. O-prune at 0.6363 (+0.62 points). On Mixtral 4×7B, HC-SMoE (single) achieves 0.5877 vs. O-prune at 0.5728 (+1.49 points). The direction of improvement is consistent across all eight settings.

## Weaknesses

### Fatal
None.

### Major

1. **The baseline comparison conflates strategy (pruning vs. merging) with method quality, and the only merging baseline is a weak variant.** HC-SMoE is a merging method, yet the main comparison (Tables 1–2) pits it against three pruning methods (O-prune, S-prune, F-prune) and only one merging baseline (M-SMoE). The paper itself demonstrates that M-SMoE's router-logit-based grouping is ineffective in task-agnostic settings (average 0.3221 on Qwen 30×2.7B vs. 0.5223 for HC-SMoE), so it serves as a weak comparator. A non-trivial merging baseline — such as a ZipIt adaptation (mentioned in related work but never evaluated), simple weight averaging of all experts within each layer to the target count, or K-means-based merging with output similarity (which the paper's own ablation shows can be competitive on some metrics) — is needed to establish that HC-SMoE's specific clustering strategy, rather than the mere act of merging, drives the improvement. Without this, the paper cannot cleanly separate "merging helps" from "hierarchical clustering on outputs helps."

2. **On Mixtral (where O-prune can perform exhaustive search), HC-SMoE's advantage over O-prune is modest.** On Mixtral 6×7B, HC-SMoE (avg) achieves 0.6425 vs. O-prune 0.6363 — a 0.62-point gain. On Mixtral 4×7B, HC-SMoE (single) achieves 0.5877 vs. O-prune 0.5728 — a 1.49-point gain. These are positive but small margins, especially compared to the headline 6.95-point gain on Qwen 30×2.7B. The Qwen gain is partially inflated because O-prune is crippled by random sampling (acknowledged by the authors: 10^5 random combinations instead of the full ~10^18). The paper should explicitly quantify how much of the Qwen advantage is attributable to O-prune's sampling approximation rather than to HC-SMoE's intrinsic superiority, or compare against a more carefully tuned O-prune baseline.

### Minor

3. **The superiority of hierarchical clustering over alternatives is less clear on certain individual metrics.** In Table 4, K-means-fix with expert-output on Qwen 45×2.7B achieves ARC-c of 0.3925 vs. HC-SMoE's 0.3646 — a setting where K-means actually outperforms HC on that specific task. While HC-SMoE wins on average (0.5426 vs. 0.5415), the margin is tiny (0.11 points) on Qwen 45×2.7B. The paper's claim that K-means is "4.75% lower" (line 298) refers to Qwen 30×2.7B, where the gap is indeed larger. On Qwen 45×2.7B, however, K-means-fix with expert-output is competitive. The paper would benefit from acknowledging this nuance rather than asserting categorical superiority.

4. **No variance or significance reporting for K-means (random initialization).** K-means-rnd with random initialization is reported as a single run without standard deviation (Table 4). Since K-means is known to be initialization-sensitive, reporting mean±std over multiple trials would allow readers to assess whether the observed performance gaps are significant. This is a standard expectation for comparing clustering methods.

5. **No analysis of the method's sensitivity to calibration data.** The calibration dataset is fixed at one configuration (32 sequences × 2,048 tokens from C4). No ablation varies the dataset size, token count, or domain (e.g., Wikipedia, books). It is therefore unclear whether the results are robust to calibration data choices or coincidental. This is important because the method relies entirely on calibration data to compute expert outputs.

6. **The claim of "scalable" is not supported by complexity analysis.** Hierarchical clustering with average linkage has O(n³) worst-case time complexity (O(n² log n) with optimized implementations). While this is far better than O-prune's exponential search (C(n, k)), the paper provides no formal analysis of time or memory cost as a function of number of experts n, hidden dimension, or calibration token count. For a model like Qwen with 60 experts, this analysis is feasible and would strengthen the paper.

### Trivial
None.

## Nice-to-Haves

- Including a ZipIt-based merging baseline or output-based K-means merging as a direct comparison point would substantially strengthen the evaluation.
- A visualization of the hierarchical clustering dendrogram for a representative layer, along with a similarity matrix comparison between expert-outputs and router-logits, would make the "functional similarity" claim more tangible.
- An analysis of cases where merging improves over the original model (e.g., Mixtral 6×7B on BoolQ, Qwen 45×2.7B on RTE) — e.g., measuring expert specialization before and after merging — would deepen the contribution.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The abstract's 6.95% improvement is not dramatic" when compared to Mixtral's 1.49%.** The abstract explicitly states "6.95% and 2.14% under the 8B and 11B parameters setups" — these refer to Qwen 30×2.7B and Qwen 45×2.7B respectively, not to Mixtral. The critic compared Mixtral's numbers against an abstract claim that was never made about Mixtral. Removed as a misunderstanding.

- **"The framing as 'first retraining-free, task-agnostic SMoE merging strategy' overstates novelty because pruning methods already exist."** The claim is specifically about *merging* (not pruning). The paper's contribution is a merging method that is both retraining-free and task-agnostic, which previous merging work (M-SMoE) was not. The claim is accurate and appropriately scoped. Removed as subjective opinion that does not identify an error.

- **"Fixed-dominant merging's contribution is marginal since it performs similarly to averaging."** The paper itself acknowledges that "the choice of merging method does influence the overall performance, its impact is relatively modest compared to the significance of robust clustering results" (Section 3). This is a feature of the paper's findings, not a weakness. Removed.

## Novel Insights

The reviews surface a genuine tension: the paper's clearest experimental advantage comes on Qwen 30×2.7B (6.95-point gain), but this is precisely the setting where the strongest baseline (O-prune) is handicapped by random sampling. On Mixtral, where all baselines can be run fairly, the gains shrink to 0.6–1.5 points. This suggests that HC-SMoE's real contribution may be better characterized as "competitive performance with guaranteed polynomial-time execution" rather than "large-margin improvement over state-of-the-art baselines." The paper's most novel and well-supported contribution — that expert-output similarity plus hierarchical (average-linkage) clustering produces more robust groups than router-logit or weight-based alternatives — is convincingly demonstrated by the ablations, even if the headline performance numbers are less dramatic than claimed. A revised framing that acknowledges the modest margins against exact-baseline comparisons while emphasizing the deterministic, scalable, and retraining-free advantages would be more honest and ultimately stronger.

## Suggestions

1. Add at least one strong merging baseline (e.g., output-based K-means merging as a direct ablation extension, or a ZipIt adaptation for experts) to disentangle "merging helps" from "hierarchical clustering on expert-outputs helps."
2. Report O-prune with more random samples on Qwen (e.g., 10^6) or provide a trade-off curve to establish a fairer comparison.
3. Add calibration data ablations varying token count (e.g., 1K, 10K, 100K) and domain.
4. Provide time/memory complexity analysis for the clustering step as a function of number of experts and hidden dimension.
5. Report K-means-rnd results with mean and std over multiple initialization trials.
6. Acknowledge in the conclusion that HC-SMoE's margin over exact O-prune on Mixtral is modest, and reframe the contribution around robustness, determinism, and scalability rather than large-margin improvement.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>