- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5
Now I have a thorough understanding of the paper. Let me verify the specific NLP results the Harsh Critic flagged.

**Verified from the paper (lines 239-244):**
- Ties-Merging on 7 NLP tasks: baseline 71.6 → +LiNeS 72.0 (+0.4 points). This is a tiny improvement.
- Consensus Merging on 11 NLP tasks: baseline 67.5 → +LiNeS 67.5 (+0.0 points). No improvement at all.

And the claim about "consistently improves" (line 226) is somewhat overstated for these specific cases, though the overall trend across NLP benchmarks is positive.

Now let me finalize the review.

---

## Summary

The paper proposes LiNeS (Layer-increasing Network Scaling), a post-training method that applies a linear scaling to parameter updates based on layer depth: shallow layers are scaled down more aggressively to preserve general features, while deeper layers retain task-specific adaptations. The method is applied to both single-task forgetting mitigation and multi-task model merging. It is simple, requires no additional training, and is complementary to existing merging techniques.

## Strengths

- **Consistent improvements across diverse merging baselines and benchmarks**: Table 1 (vision) shows LiNeS improves Task Arithmetic, Ties-Merging, and Consensus Merging on 8-task, 14-task, and 20-task benchmarks for both ViT-B/32 and ViT-L/14, with typical gains of 2–4% absolute accuracy. For example, on the 20-task ViT-L/14 benchmark, gains are +3.1%, +4.0%, and +2.3% respectively — showing the method reliably boosts state-of-the-art merging techniques.

- **Clear demonstration of the forgetting-mitigation trade-off**: Table 1 (line 81) shows the fine-tuned model loses control task accuracy (38.0% vs. pre-trained 48.3%), but after LiNeS the control accuracy recovers to 48.0% while target accuracy only drops from 90.5% to 90.3%. This directly quantifies the core trade-off improvement.

- **Generality across modalities, model scales, and application scenarios**: LiNeS is evaluated on vision (CLIP ViT-B/32, ViT-B/16, ViT-L/14), NLP (T5-large), and LLM alignment (LLaMA-2 7B, Rewarded Soups). It also shows benefits in OOD generalization (WiseFT, Figure 1), single-task model soups (Table 3), and multi-task merging — covering a wide range of settings.

- **Simple and practical method**: LiNeS requires tuning only one hyperparameter (β) in most settings, with a principled heuristic for α. It operates post-training with no additional training or memory overhead, unlike learned layer-wise scaling methods (Ada-merging, aTLAS) that require backpropagation through the full model.

## Weaknesses

### Major

- **α heuristic for multi-task merging is not ablated or validated**: In the multi-task setting (Section 5.2, line 187–191), the intercept α is set by a heuristic (α = (1/N) × (||τ_sum|| / ||τ_MTL||)) that depends on the number of models and the merging method. The paper relies on this to reduce tuning to a single parameter (β), but provides no ablation study, sensitivity analysis, or comparison against alternative α choices. This makes it unclear how critical this heuristic is to the reported multi-task gains and whether simpler defaults (e.g., α=0) would work as well.

- **No accuracy comparison with Ada-merging and aTLAS**: The Discussion section (lines 327–328) compares scaling patterns of LiNeS against Ada-merging and aTLAS in Figure 5, claiming LiNeS "achieves scaling very close to Ada-merging or aTLAS, but with much less computational cost." However, no accuracy numbers are provided for these methods on the same benchmark, so the reader cannot verify whether the similar scaling translates to similar accuracy. The paper would benefit from a direct accuracy comparison (or reframing the claim more modestly as a qualitative similarity in scaling behavior).

### Minor

- **No variance or statistical significance reporting**: Every reported result is a single point estimate with no standard deviations, confidence intervals, or error bars. While single-run evaluation is standard in the model merging literature (the process is deterministic once checkpoints are fixed), the absence of any variability information makes it impossible to gauge whether the reported improvements (e.g., the 2–4% gains in vision) are reliable or could fluctuate significantly. Adding per-task breakdowns or variance estimates over the hyperparameter search would strengthen the evidence.

- **Some NLP improvements are negligible, but the paper claims "consistently improves":** Table 2 shows Ties-Merging + LiNeS on 7 NLP tasks yields only +0.4 points (71.6→72.0), and Consensus Merging + LiNeS on 11 NLP tasks yields +0.0 points (67.5→67.5). The paper states (line 226) that LiNeS "consistently improves multi-task performance across baseline merging methods and benchmarks with a notable margin," which is slightly overstated for these two specific cases. The overall trend remains positive across most NLP settings, so this does not undermine the method, but the claim should be tempered.

### Trivial

None.

## Nice-to-Haves

- Per-task breakdowns of accuracy for the multi-task merging results would allow readers to see whether the average improvement is broadly distributed or driven by a subset of tasks.
- An ablation study for the α heuristic (e.g., comparing fixed α values against the proposed heuristic) would strengthen confidence in the method's multi-task formulation.

## Removed Points

1. **"The α heuristic is a function of the merging method and number of models, introducing unexamined dependence"** — This is essentially the same point as the Major weakness above (the heuristic is not ablated). Keeping the ablation criticism but removing the redundant "unexamined dependence" framing.

2. **"Cannot tell whether the improvement is driven by a few tasks or is a reliable shift"** — This is subsumed under the variance reporting weakness. The paper reports across many benchmarks, making systematic bias unlikely. Kept as part of the Minor weakness above.

3. **Harsh critic's claim that the comparison with Ada-merging/aTLAS "lacks direct performance validation" for "similar scaling"** — The paper claims similarity in scaling patterns (shown in Figure 5), not similarity in accuracy. However, the claim is still weak without accuracy numbers, so it remains as a Major weakness above.

## Novel Insights

None beyond the paper's own contributions. The key observation — that post-training layer-wise downscaling of shallow-layer updates can recover generalization while preserving task accuracy, and that a simple linear schedule suffices — is the paper's core contribution, which the reviews corroborate rather than augment.

## Suggestions

1. Add an ablation study for the α heuristic in the multi-task setting (e.g., α=0, α=1/N, and the proposed norm-adjusted version) to validate its importance.
2. Include accuracy numbers for Ada-merging and aTLAS on at least one benchmark, or reframe the comparison to focus solely on scaling pattern similarity.
3. Add per-task accuracy breakdowns for the multi-task merging results (perhaps in a table or figure) to show the distribution of improvements.
4. Slightly temper the claim of "consistently improves with notable margin" for NLP given the two near-flat results.
