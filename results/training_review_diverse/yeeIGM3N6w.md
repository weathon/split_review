Now I have all the information I need. Let me produce the consolidated final review.

## Summary

This paper proposes HC-SMoE, a retraining-free, task-agnostic framework that reduces the number of experts in sparse MoE models by (1) computing averaged expert outputs on a calibration set, (2) clustering those output vectors with hierarchical clustering (average linkage), and (3) merging experts within each cluster via frequency-weighted, average, or fixed-dominant merging. The method is evaluated on Qwen (60 experts) and Mixtral (8 experts) across eight zero-shot tasks, consistently outperforming three pruning baselines (O-prune, S-prune, F-prune) and one merging baseline (M-SMoE).

## Strengths

1. **Expert outputs as a similarity metric are convincingly shown to be more effective than router logits or weights.** Table V (tab:ab-hc) shows that under average-linkage hierarchical clustering, expert-output similarity achieves 0.5459 average accuracy on Qwen45, substantially outperforming router-logits (0.3153) and weights (0.5234). This direct evidence supports the paper's core insight that functional similarity is better captured by output behavior than by routing patterns or parameter distances.

2. **HC-SMoE (the full framework) consistently and significantly outperforms all baselines across two model families and two reduction levels.** In Tables 2 and 3 (tab:qwen, tab:mixtral), HC-SMoE (avg) achieves the highest average accuracy in all four settings: Qwen45 (+2.14% absolute over best baseline F-prune), Qwen30 (+6.95% over F-prune), Mixtral6 (+0.62% over O-prune), and Mixtral4 (up to +2.49% over O-prune). These margins are meaningful and demonstrate that the overall framework works well on both a large (60-expert) and compact (8-expert) SMoE architecture.

3. **Scalable by design, avoiding combinatorial explosion.** The paper explicitly contrasts with O-prune, which requires ~10¹⁸ combinations per layer for Qwen, and shows that HC-SMoE's O(N²) hierarchical clustering is practical. This is a genuine practical advantage for models with many experts.

4. **Merging strategy is shown to be secondary to clustering quality.** Table IV (tab:ab-merge) demonstrates that with hierarchical clustering, all three merging methods (frequency, average, fixed-dominant) yield nearly identical scores (0.5712–0.5716 for Qwen45, 0.5208–0.5240 for Qwen30), all outperforming every baseline. This cleanly isolates the clustering stage as the driver of performance retention.

## Weaknesses

### Fatal

None.

### Major

1. **The claim that hierarchical clustering (HC) is meaningfully superior to K-means is overstated.** Table VI (tab:ab-kmeans) shows that on Qwen45, HC-SMoE achieves 0.5426 while K-means-fix with expert-output achieves 0.5415 — a difference of ~0.1% with no uncertainty quantification. On Qwen30, the gap is larger (4.75%), but the paper's narrative ("hierarchical clustering is able to outperform K-means," "underscoring the superiority of HC") does not acknowledge how small the gap is in the 45-expert setting. The paper highlights the 4.75% result while the near-tie at Qwen45 receives no caveat. Since Contribution #3 explicitly claims that hierarchical clustering provides "robust and reliable results for expert grouping" relative to alternatives, this evidence is weaker than claimed. The strongest evidence for HC over K-means is its *stability* (deterministic, no initialization sensitivity) — this is valid and should be emphasized instead of marginal accuracy differences. The accuracy-based superiority claim needs tempering.

2. **Absence of statistical rigor for fine-grained comparisons.** No experiment is repeated, and no measure of variance (standard deviation, confidence intervals) is reported. This matters most for the small-margin comparisons (HC vs. K-means-fix on Qwen45, linkage method differences, and some close baseline comparisons on Mixtral4). The large-margin wins (Qwen30, Qwen45 vs. baselines) are robust even without replication, but the paper makes several claims that rest on very small differences.

### Minor

1. **The cross-model scalability argument is confounded.** The paper claims: "Qwen 45x2.7B and Mixtral 4x7B achieve comparable scores despite a twofold difference in parameter count. This observation substantiates the scalability of HC-SMoE to SMoE models with a higher number of experts." However, Qwen and Mixtral differ in architecture, training data, total parameters, and baseline performance — the comparison is not a clean test of scalability. The scalability claim is better supported by the computational complexity analysis (O(N²)) and the fact that HC-SMoE works well on both models individually. This specific paragraph weakens rather than strengthens the paper.

2. **No analysis of cluster quality.** The paper hypothesizes that HC maintains intra-cluster similarity and inter-cluster diversity, and that this is why it works, but never measures this directly (e.g., silhouette scores, Davies–Bouldin index). A cluster validation index on the expert-output vectors would directly test this hypothesis and potentially explain why HC and K-means-fix produce similar downstream accuracy despite different clustering properties.

3. **No sensitivity analysis for the calibration set.** The calibration set is fixed to 32 × 2048 tokens from C4. Practitioners would benefit from knowing how robust the method is to calibration set size and composition.

4. **Router behavior after merging is not discussed.** After merging, the router still outputs logits for original expert indices, which are mapped to merged experts. This could cause a mismatch between the router's assignments and the merged experts' actual competence, especially when experts with different routing patterns are merged. The paper silently assumes this is harmless.

5. **Single-shot grouping methods underperform O-prune (which prunes rather than merges) without discussion.** Table VII shows that all one-shot grouping methods (including weight and expert-output based) underperform O-prune on Mixtral. The paper notes this but does not analyze *why* merging can be worse than pruning in this comparison — a natural question for readers.

6. **The paper does not discuss computational cost of clustering/merging.** While scalability is a claimed advantage, no clustering time, merging overhead, or comparison to alternative methods' costs is reported.

### Trivial

- Minor phrasing issues: the sentence about M-SMoE's inferior generalizability (¶2 of Introduction) feels vague; a brief preview of *why* would help.
- The comparison of fixed vs. random K-means initialization showing a 12.96% drop is a nice result but is presented for the weight metric, which is not the paper's recommended approach — the paper could clarify this.

## Nice-to-Haves

- A cluster validation analysis (silhouette score, Davies–Bouldin) on the learned expert clusters would strengthen the argument that HC produces better groupings.
- Sensitivity analysis for calibration set size and composition (e.g., varying the 32×2048 default).
- Reporting runtime/memory cost of the clustering and merging stages would help practitioners assess the practical overhead.
- A brief discussion of the router-mismatch issue and why it is or is not problematic.

## Removed Points

- **"Introduction should preview why M-SMoE fails"**: This is a presentational suggestion, not a weakness. The paper could be clearer, but this does not affect the contribution's validity.
- **"Table I inconsistency about M-SMoE's setup"**: The paper applies M-SMoE in a modified setting (task-agnostic, no retraining) for fair comparison, which is standard practice and is explicitly noted. Not a weakness.
- **"§3.3: High parameter similarity doesn't mean weight-space distance is a poor metric"**: This is a reasonable methodological observation but a) the paper's main argument is that *outputs* work better empirically (Table V shows this clearly), and b) the theoretical justification is secondary to the experimental evidence. This is an arguable nuance, not a weakness of the paper.
- **"§3.4: No discussion of computational cost for very large numbers of experts"**: Hierarchical clustering is O(N²) (as the paper notes), which is already demonstrably feasible for current SMoE scales. Speculating about hypothetical future scales is beyond the paper's scope.
- **"Table VII: O-prune beats one-shot grouping but paper doesn't discuss why"**: This is a minor observation, not a structural weakness. The paper's main finding is that *HC-based* merging (its method) beats O-prune, not that all merging methods do.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface verification of existing claims rather than revealing unexpected patterns.

## Suggestions

1. **Temper the HC-vs-K-means claim.** Acknowledge that on Qwen45, K-means-fix with expert-output achieves nearly identical accuracy to HC, and reframe the advantage of HC as *stability* (deterministic, no initialization sensitivity) rather than universal accuracy superiority. This would be more accurate and equally persuasive.

2. **Add repeat-run statistics for the fine-grained comparisons.** Even 3–5 runs with different calibration samples would allow reporting means and standard deviations, clarifying whether the small differences (HC vs. K-means-fix, linkage methods) are meaningful.

3. **Remove or rephrase the cross-model scalability argument.** The claim that "Qwen 45 and Mixtral 4 achieve comparable scores despite twofold parameter difference" does not support scalability — it's confounded by architectural differences. The scalability argument is already well-supported by the complexity analysis and by the consistent performance across reduction ratios within each model.

4. **Report a cluster quality metric** (e.g., silhouette score) to directly test the hypothesis that HC produces better cluster structure, which would complement the downstream accuracy results.

## Score and Decision

This paper presents a practical, well-motivated method for retraining-free SMoE expert merging. The core results — HC-SMoE consistently outperforms all baselines, and expert-output similarity is the key driver — are solidly supported. The main weaknesses are overclaiming on the HC-vs-K-means comparison (where the evidence is mixed) and the absence of statistical rigor for fine-grained distinctions. These are real but not fatal; they can be addressed in revision. The overall contribution — a task-agnostic, scalable merging framework validated on large models — has clear value to the community.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>