- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6
Now I have all the information needed. Let me construct the consolidated review.

## Summary

This paper proposes HC-SMoE, a retraining-free, task-agnostic expert merging framework for Sparse Mixture-of-Experts (SMoE) models. The key idea is to use hierarchical clustering based on averaged expert outputs (rather than router logits or weights) to group functionally similar experts, then merge within each cluster. The method is evaluated on Qwen (60 experts) and Mixtral (8 experts) across eight zero-shot tasks at two reduction levels each, with extensive ablations on linkage methods, similarity metrics, clustering strategies, and merging approaches. Results show consistent improvements over pruning and merging baselines, particularly at higher compression rates.

## Strengths

1. **Consistent performance gains over existing retraining-free baselines across multiple models and reduction levels.** Tables 1 and 2 show HC-SMoE outperforms all baselines (O-prune, F-prune, S-prune, M-SMoE) on both Qwen and Mixtral at both reduction levels. On Qwen 45x2.7B, HC-SMoE achieves 0.5716 vs. the best baseline (F-prune) at 0.5502; on Qwen 30x2.7B the gap widens to 6.95 percentage points. On Mixtral 6x7B, HC-SMoE scores 0.6425 vs. the best baseline (O-prune) at 0.6363. These gains are consistent across both architectures and both reduction settings.

2. **Clear evidence that expert-output-based similarity is superior to router-logit or weight-based alternatives.** Tables 3–5 consistently show that using expert outputs as the similarity metric for clustering substantially outperforms router logits (e.g., 0.5459 vs. 0.3153 for average linkage on Qwen 45x2.7B in Table 3) and moderately outperforms weight-based similarity. This claim is well-supported across multiple ablations.

3. **Hierarchical clustering demonstrates robustness over K-means, especially at higher reduction rates.** Table 6 shows that on Qwen 30x2.7B (50% reduction), HC-SMoE (0.4993) outperforms the best K-means variant (K-means-rnd + expert-output, 0.4518) by 4.75 points, and HC-SMoE is deterministic while K-means exhibits sensitivity to initialization (e.g., a 12.96% drop when switching from fixed to random initialization with weight metric).

4. **Comprehensive ablation study justifying each design choice.** The paper systematically ablates: (a) similarity metrics (expert-output vs. router-logits vs. weight), (b) linkage methods (single vs. complete vs. average), (c) clustering algorithms (hierarchical vs. K-means vs. one-shot), and (d) merging strategies (frequency, average, fixed-dominant). This thoroughness strengthens confidence in the design decisions.

## Weaknesses

### Fatal

None.

### Major

1. **No variance or sensitivity analysis across calibration data.** All experiments use a single calibration set (32 sequences of 2,048 tokens sampled once from C4). The method is deterministic given this data, but there is no reporting of variance across different calibration samples or analysis of sensitivity to the calibration set's size or composition. Since improvements at lighter reduction levels are small (e.g., ~0.6% on Mixtral 6x7B), it is unclear whether these margins are robust. This is the most impactful missing piece — error bars or a sensitivity analysis would substantially strengthen the evidence.

### Minor

2. **Unclear how hierarchical clustering achieves the target number of experts.** The paper describes merging experts "progressively" based on distance but never specifies the stopping criterion used to obtain exactly 45 or 30 experts (Qwen) or 6 or 4 experts (Mixtral) per layer. Standard practice is to cut the dendrogram at a height that yields the desired cluster count, and the paper should state this explicitly. The same issue applies to the comparison with K-means, which also requires a target cluster count.

3. **M-SMoE baseline comparison is applied outside its intended setting with limited discussion.** Table 1 marks M-SMoE as requiring retraining and being task-specific. The paper applies it without retraining in a task-agnostic setting (line 143), which is transparent but handicaps M-SMoE against a method designed for this setting. While comparing component-level behavior is informative, the paper should more clearly frame this as "components of M-SMoE applied in a retraining-free setting" rather than treating it as a full baseline. The current framing could mislead readers about M-SMoE's capabilities.

4. **No analysis of how the unchanged router behaves after merging.** The paper acknowledges that the router network is left unmodified (line 98) and that "if a token was originally routed to any expert in a merged group, it will be routed to the corresponding new expert." However, there is no empirical analysis of whether routing behavior changes meaningfully (e.g., routing entropy shifts, changes in top-1 expert assignment overlap, per-layer routing distributions). Since the router was trained on the original expert set, understanding how its decisions interact with merged experts would strengthen the claim that the approach is sound.

### Trivial

5. **Some phrasing in ablations slightly overstates the margins.** The claim that "most post-merged models utilizing K-means experience a substantial decline" (line 298) is too strong for the Qwen 45x2.7B case, where K-means-fix + expert-output (0.5415) is within 0.11% of HC-SMoE (0.5426). The advantage is clear at the higher reduction level (Qwen 30x2.7B: 4.75%), but the wording should be tempered for the lighter reduction case.

6. **No dedicated limitations section.** The paper discusses limitations of prior methods but not its own. The conclusion could briefly note limitations such as reliance on calibration data quality, the assumption that averaged outputs capture functional similarity for all input distributions, and the unchanged router issue.

## Nice-to-Haves

- **Error bars / bootstrapping over calibration samples**: The most impactful addition would be reporting mean and standard deviation across multiple calibration samples (e.g., 5 different C4 subsamples).
- **Router behavior analysis**: A simple experiment showing per-layer routing entropy or top-1 expert overlap before and after merging.
- **Sensitivity of results to calibration dataset size/domain**: Showing graceful degradation as calibration data shrinks or shifts domain.
- **Qualitative cluster visualization**: t-SNE of expert outputs colored by cluster assignments from HC vs. K-means vs. one-shot grouping would visually reinforce the claim.
- **Direct comparison to full ZipIt** (rather than only the adapted fixed-dominant variant).
- **Weight-averaging all experts into one** as a trivial baseline to show the value of selective grouping.

## Removed Points

- **"Lack of statistical significance / sensitivity analysis"** was kept as Major (it is a real issue). Not removed.
- **"M-SMoE comparison may be unfair"** was retained but downgraded from Critical to Minor because the paper is transparent about the adaptation and a comparison must be made somehow in the retraining-free setting. The issue is one of framing clarity, not fundamental unfairness.
- **"Ablation on clustering — complete linkage + router-logits close to best HC-SMoE"** was merged into Trivial weakness #5 (overstated phrasing). The observation itself is correct but the difference (0.5295 vs. 0.5459) is on a 4-task subset, and the full 8-task results in Table 1 show larger margins favoring HC-SMoE.
- **Strength Finder's generic strength about "addressing an important problem"** — removed. The retained strengths are evidence-grounded.
- **"Missing related works"** — not mentioned by either reviewer, so irrelevant.
- **"Code release"** and **"scalability to >100 experts"** — moved to Nice-to-Haves. These are beyond the paper's stated scope and do not threaten the core contribution.
- **"Missing appendix/proofs"** — not applicable, no such complaint was made.
- **Typo/formatting/style nitpicks** — not present in the inputs.
- **The Strength Finder's claim that K-means shows "substantial decline" was kept as a verified observation (it is true for Qwen 30x2.7B) but the overstatement was flagged in Trivial weakness #5.**

## Novel Insights

The most insightful observation that emerges from the reviews is that the paper's ablations reveal a subtle but important asymmetry: **the quality of the clustering step matters far more than the choice of merging strategy**, but the clustering quality itself depends on choosing the right similarity metric (expert outputs) *and* the right linkage method (average). The surprising result that complete linkage with router-logits achieves competitive performance (0.5295) while complete linkage with expert-output collapses (0.3909) suggests that different similarity metrics encode fundamentally different notions of "closeness" — router logits capture decision-boundary separation (favoring complete linkage's maximal-distance criterion), while expert outputs capture functional similarity (favoring average linkage's holistic criterion). This interaction between metric choice and linkage method is worth highlighting as a design principle beyond this specific paper.

## Suggestions

1. Add a brief subsection or note explaining the stopping criterion for hierarchical clustering (cut dendrogram at height yielding desired cluster count).
2. Report performance variance across multiple calibration samples (e.g., 5 random C4 subsamples) to address the statistical-significance concern. If compute constraints prevent full reruns, at minimum discuss sensitivity to calibration data.
3. Include a brief analysis (could be a small table or paragraph) of routing behavior post-merging — e.g., per-layer routing entropy or overlap in top-1 expert assignments between original and merged models on the calibration set.
4. Reframe the M-SMoE comparison more precisely (e.g., "M-SMoE's grouping component applied without retraining" rather than treating it as the full method), and add a sentence acknowledging that the full M-SMoE pipeline would likely perform better with retraining.
5. Add a dedicated limitations paragraph in the conclusion discussing: (a) reliance on a single calibration dataset, (b) the unchanged router assumption, and (c) the scope of validation (two model families, albeit at multiple reduction levels).
6. Temper the language about K-means at the lower reduction level (Qwen 45x2.7B) to avoid overclaiming; the advantage is clear at 50% reduction.
