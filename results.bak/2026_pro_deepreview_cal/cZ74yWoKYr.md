Now I have a clear picture. Let me synthesize the final review.

**Bracket from Round 1**: The paper sits between the earlier version of itself (5.75) and the strong CAKE paper (7.00), so bracket is approximately **6.0 – 7.0**.

**Round 2 narrowed it**: The paper is substantially stronger than PyramidKV (5.60) and its own earlier version (5.75). It is comparable to or slightly below CAKE (7.00) but brings a different type of contribution (formal theory + universal plug-in vs. a specific new eviction method). The current paper has more comprehensive evaluation than CAKE (29 datasets across 3 benchmarks vs. LongBench + NeedleBench; 3 models including 32B; 3 integrated methods).

Now producing the final review:

---

## Summary

This paper formalizes critical KV cache selection as minimizing attention output perturbation under a budget constraint. It derives an upper bound involving both attention weights and value states projected through W^O, and proposes a two-stage greedy algorithm (perturbation-constrained selection) that directly minimizes this bound. Integrated as a plug-and-play enhancement into SnapKV, AdaKV, and HeadKV, the algorithm consistently reduces compression loss by more than half on average across 29 datasets (Ruler + LongBench) on three LLMs (Llama-3.1-8B, Mistral-7B, Qwen2.5-32B), with negligible overhead.

## Strengths

- **Genuine formal contribution**: Theorems 3.2 and 3.3 derive a concrete upper bound θ on output perturbation ℒ that surfaces the role of value states projected through W^O (Equation 5). This provides principled motivation for why attention-weight-only heuristics are suboptimal — a point prior work only assumed empirically.

- **Algorithm directly instantiates the theory**: Theorem 3.5 shows that the two-stage greedy algorithm (Algorithm 1) minimizes an upper bound \(\hat{\theta}\) of the output perturbation. Stage 1 guarantees sufficient attention mass (Assumption 3.4, validated in Appendix A), and Stage 2 greedily optimizes the remaining bound using both attention weights and projected value norms (Equation 6).

- **Substantial and consistent empirical gains across diverse conditions**: Tables 1–3 and Figure 2 show loss reduction across 3 models × 3 eviction methods × multiple cache sizes on both synthetic (Ruler, 13 tasks) and real-world (LongBench, 16 tasks) benchmarks. Gains persist in multi-turn SCBench (Table 3). On LongBench with AdaKV at 40% cache, the algorithm reduces average loss from 6.0% → 2.4% (Llama), 4.9% → 2.4% (Mistral), and 5.3% → 3.2% (Qwen).

- **Minimal overhead with strong efficiency**: Section 4.6 and Figure 3 show TTFT increase of only 0.06s at batch-1 32K context (3.54→3.60s), with identical decoding latency to the base eviction method, while achieving 2.49× speedup over full cache at batch-4.

- **Perturbation analysis validates the theory**: Section 4.7 shows that the algorithm reduces actual output perturbation in 92% of attention heads for Llama-3.1-8B (Figure 4), with benefits accumulating across layers (Figure 5) and persisting across cache budgets from 2.5% to 40% (Figure 6). This directly corroborates the theoretical motivation of constraining worst-case perturbation.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Theory–practice gap in attention-weight proxy**: The theoretical bound (Theorem 3.3, Equation 5) depends on attention weights \(A_i\) that would be produced by the *actual decoding query*. The algorithm, as integrated in Algorithm 2, uses accumulated attention weights from a prefill observation window (lines 2–4) because compression occurs before the question is seen (Section 4.1). Those accumulated scores are a heuristic proxy for the future query's attention weights. The perturbation analysis (Section 4.7) shows the algorithm works in practice, and the paper mentions the simple setting (question available at compression time) is in Appendix F, but the paper never explicitly discusses *why* the accumulated proxy remains informative for the bound. This does not invalidate the results — the empirics speak clearly — but the theoretical narrative would benefit from acknowledging and discussing this mismatch.

- **No variance estimates**: All tables and figures report point estimates without confidence intervals or standard errors. Ruler uses 100 instances per task, and LongBench datasets vary in size, yet no measure of statistical variability is provided. While the improvements are large and consistent across 88/90 long-dependency test cases, a few comparisons (e.g., SnapKV on Mistral-7B at 40% cache, where loss goes from 58.9% → 46.9%) are less dramatic than others, and variance estimates would help readers assess reliability.

### Trivial

- The α=0.0 vs. α=0.5 comparison for Llama in Table 4 shows α=0.0 scores slightly higher (44.35 vs. 43.77). The paper discusses robustness but does not note this specific inversion; acknowledging it would add nuance to the sensitivity analysis.

- "First formal study" phrasing (abstract, conclusion) should be softened to "to our knowledge, the first formal analysis from an output perturbation perspective" since formal treatments of related problems exist in adjacent areas.

## Nice-to-Haves

- Reporting the empirical correlation between the bound value \(\hat{\theta}\) and actual observed output perturbation for a sample of heads would further validate that minimizing the bound translates to real perturbation reduction.

- A brief mention of how the \(VW^O\) norm computation is implemented to keep overhead low (e.g., precomputed during prefill, reused across decoding steps).

- Evaluating in the "simple" setting where the question IS available at compression time would provide a clean alignment between the theoretical bound (using true query attention) and the algorithm, complementing the practical compression-scenario results.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Demand for larger-model evaluation (e.g., 70B)*: The paper already evaluates on Qwen2.5-32B in addition to two 7B/8B models, spanning a meaningful range of scales. This is adequate for the paper's scope.

- *Requesting per-head α tuning or data-driven thresholds*: The paper explicitly scopes this out as future work (Section 3.5), and demonstrates that α=0.5 works robustly. This is scope creep.

- *Ambiguity about whether SnapKV-specific max-pooling is retained (Section 4.6 nitpick in harsh critic)*: Algorithm 2 lines 1–4 explicitly retain the original accumulation mechanisms including max-pooling for SnapKV (line 4, commented). This is clear.

- *Demand for confidence intervals as a fatal/major flaw*: While variance would strengthen the paper, single-run evaluation is standard practice in large-scale KV cache eviction benchmarking (as seen in SnapKV, AdaKV, HeadKV, and CAKE papers), and the consistency of gains across 29 datasets and 3 models makes point estimates credible.

- *"Missing related works" claims from the harsh critic's area-of-concern sweep*: No specific missing related work was identified that is verifiable. All standard baselines (H2O, SnapKV, AdaKV, HeadKV) are included.

## Novel Insights

The paper's key insight — that KV cache criticality should be defined through output perturbation rather than attention weight magnitude — is genuinely novel for the cache eviction literature. Prior work treated attention weight magnitude as a self-evident proxy for importance. The derivation showing that the perturbation bound decomposes into a product of attention weights and projected value norms (Equation 5) provides a clean and actionable formalization. The empirical finding that this simple modification, with α=0.5, robustly halves compression loss across 29 datasets without requiring per-model tuning is a strong signal that the theoretical framing captures something real about how attention outputs degrade under compression.

## Suggestions

- Add a paragraph in Section 3.6 or Section 4.1 explicitly discussing the relationship between accumulated observation-window attention weights and the \(A_i\) used in the theoretical bound — specifically, under what conditions the proxy is expected to remain informative, and what failure modes might arise.

- Report standard deviations or bootstrap confidence intervals for the main results in at least one summary table to give readers a handle on variability.

## Score and Decision

The paper makes a clear, well-motivated contribution: it formalizes a problem that prior work treated heuristically, derives a practical algorithm from the formalism, and demonstrates consistent, substantial gains when plugged into three different SOTA eviction methods. The evaluation is among the most comprehensive I have seen in this area (29 datasets across 3 benchmarks, 3 models, 3 methods, multiple cache sizes). The two identified weaknesses (theory–practice proxy gap and missing variance) are real but minor; neither undermines the core claims.

**Anchor comparison:**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4QWPCTLq20.md` (IntelLLM): avg 3.00, Round 1 — clearly weaker; this paper has much stronger theoretical grounding and more comprehensive evaluation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jZVNmDiU86.md` (PyramidKV): avg 5.60, Round 2 — this paper has stronger theory, broader evaluation, and more consistent gains.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lRTDMGYCpy.md` (earlier version of same paper): avg 5.75, Rounds 1+2 — current version is substantially stronger in scope, evaluation, and presentation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/FJFVmeXusW.md` (HeadKV): avg 6.50, Round 2 — the current paper integrates with and improves upon HeadKV; similar quality tier.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EQgEMAD4kv.md` (CAKE): avg 7.00, Round 2 — comparable quality; CAKE has a different focus (layer-wise allocation vs. universal selection enhancement). The current paper has broader evaluation and formal theory the CAKE paper lacks, but CAKE has deeper system-level efficiency analysis.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/STUGfUz8ob.md` (Transformer reasoning): avg 7.60, Round 1 — a fundamentally different type of contribution; stronger theory but narrower evaluation. The current paper does not reach this tier due to the minor theory–practice gap and lack of variance estimates.

The paper is clearly above the 5.75 of its earlier version and comparable to the 6.5–7.0 tier. Given the formal contribution, comprehensive evaluation, and practical impact, I place it at **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>