Here is my consolidated final review.

## Summary
IntentGPT proposes a training-free framework for few-shot intent discovery that chains frozen LLMs (GPT-4, GPT-3.5, Llama-2) with automatic prompt generation (ICPG), semantic few-shot example retrieval (SFS), and a known-intent feedback loop (KIF) that injects discovered intents back into the prompt during inference. Experiments on CLINC and BANKING show competitive or state-of-the-art results against semi-supervised methods that use substantially more labeled data and multi-stage training.

## Strengths
1. **Training-free method achieves competitive performance with far fewer labels.** Table 1 shows IntentGPT-4 (50-shot) reaches NMI 96.06 / ARI 84.76 on CLINC and NMI 85.94 / ARI 66.66 on BANKING, matching or exceeding semi-supervised methods (SCL, LatentEM, DeepAligned) that require extensive labeled data and task-specific training. This is the paper's core contribution and is well supported by the main table and the KIR curves (Figures 3–4).

2. **Known Intent Feedback (KIF) is demonstrated to be critical through controlled ablation.** Table 2 shows that removing KIF causes NDI to explode from ~150 to >1000 on CLINC for both GPT-3.5 and GPT-4, while NMI drops by 7–10 points. This cleanly quantifies the mechanism that enables the model to reuse known intents rather than over-segmenting.

3. **Semantic Few-Shot Sampling (SFS) provides consistent gains over random few-shot selection.** Table 2 shows SFS improves NMI and ACC across both datasets and both LLMs (e.g., GPT-4 BANKING NMI: 81.70→83.18, ACC: 64.51→70.42), confirming that embedding-based example retrieval adds meaningful signal.

4. **Automatic prompt generation (ICP) yields measurable improvements over a manually written prompt.** Table 2 shows ICP adds 1–2 NMI points on top of KIF+FS+SFS (GPT-4 CLINC NMI: 93.89→94.99; GPT-4 BANKING NMI: 81.71→83.18), validating the design choice.

5. **Systematic ablation study covering five feature combinations across two LLMs and two datasets.** Table 2 tests KIF, FS, SFS, ICP, and SKIF in a logical progression, reporting not only clustering metrics but also NDI (number of discovered intents), which provides interpretability for how each component affects the model's behavior.

## Weaknesses

### Fatal
None.

### Major
- **Test-order sensitivity from the batch-wise KIF update is unexamined.** The pipeline processes the test set in batches of 16 and updates the known-intent database at the end of each iteration (Section 3.3, line 79; Section 5, line 209). This means the first batch sees only the original known intents, while later batches benefit from newly discovered intents injected into the prompt. The order in which test examples are presented can therefore change the set of intents available for downstream predictions and, consequently, the final results. The paper reports no analysis of this effect — no runs on shuffled test orders, no discussion of the sensitivity, no variance estimates. Without this, the reported numbers are a single point in a potentially wide distribution, and the results may not be reproducible without knowing the exact test set order. This is the most significant methodological gap in the paper.

### Minor
- **No error bars or variance estimates reported for any metric.** On several metrics the margin over the best semi-supervised baseline is narrow (e.g., BANKING NMI: 85.94 vs. 85.04 for SCL; BANKING ARI: 66.66 vs. 65.43 for SCL). Without confidence intervals or standard deviations, it is impossible to assess whether these differences are reliable. The KIR curves (Figures 3–4) and the NDI metric provide corroborating evidence, which helps, but the main comparison table would be substantially strengthened by reporting variance.

- **Post-hoc clustering hyperparameter (DBSCAN ε = 0.5) is not analyzed for sensitivity.** The evaluation pipeline uses DBSCAN with ε = 0.5 to determine the number of K-Means clusters from the predicted intents (Section 3.4, line 86). This parameter is fixed without any analysis of how results might change with different values. While this is a standard post-hoc evaluation step (not part of inference), the sensitivity should be acknowledged or the choice justified.

- **Llama-2 model size is inconsistently specified.** Figure captions (lines 220, 227) state "Llama-2 70B," but the text and Table 1 refer only to "Llama-2" without indicating the variant. This should be consistent throughout.

- **The size of the Few-Shot Pool is never stated.** The paper mentions it is "10% of the samples for each known intent" (line 74), but never states the absolute number of examples. For CLINC with KIR=0.75 (~75 known intents, ~120 examples/intent), this is roughly 900 examples; for BANKING (~9000 examples across 77 intents), roughly 900 as well. Making this explicit would help readers assess how much labeled data underlies the approach.

### Trivial
- The phrase "at the end of an iteration" (Section 3.3, line 79) could be more explicit about whether updates happen per batch or per test example. The batch size of 16 (Section 5) clarifies this indirectly, but stating it directly in Section 3.3 would improve clarity.

## Nice-to-Haves
- **Run the pipeline on 3–5 random permutations of the test set** and report mean ± std for the main metrics. If variance is small, the order-dependence concern is resolved; if large, it becomes a critical finding the authors should analyze.
- **Report precision/recall of new intent discovery** (not just NDI) to assess whether KIF may bias the model toward reusing existing intents at the expense of discovering genuinely new ones.
- **Quantify ICPG cost** (approximate token usage for prompt generation) so readers can assess the one-time setup trade-off.

## Removed Points
*These points were raised by reviewers but are removed for the reasons stated below. Treat them with caution if referenced.*

1. **"Margin over LatentEM (CLINC ACC: 88.99 vs. 88.76)" framing.** The reviewer claimed a "margin over" LatentEM, but LatentEM (88.99) actually outperforms IntentGPT-4 (88.76) on this metric — the paper itself acknowledges this. Removed as factually inaccurate in this specific framing; the broader point about narrow margins is retained in Minor weaknesses above.

2. **Missing generated prompts from ICPG.** The generated prompts may have been included in an appendix (stripped during parsing). Following the hard rule that parser-stripped appendix content is not a valid weakness, this is removed.

3. **Critique that the paper doesn't ablate over the prompt generation model / prompt template.** The paper's ablation (Table 2) does compare with vs. without ICP on the same single generated prompt, which is a reasonable first analysis. A full study varying the generation model is outside the stated scope and more appropriate as future work.

4. **"The '0-shot' label is misleading."** The paper explicitly defines what 0-shot means in its setting (line 212: "we do not use any few-shot samples, the prompt is simply a basic description of the task, and we activate Known Intent Feedback (KIF) to reuse intents"). This is a reasonable definition given the context.

5. **Request to quantify ICPG cost (tokens consumed).** This is a nice-to-have, not a weakness, and is moved to Nice-to-Haves above.

## Novel Insights
The reviews surface a genuine methodological blind spot: the batch-sequential KIF update creates an order-dependence that standard evaluation protocols for intent discovery do not account for. This is not just a reproducibility nitpick — it is a structural property of any method that iteratively expands its label set during inference without controlling for the sequence in which test examples are encountered. Most prior work on semi-supervised intent discovery (DeepAligned, SCL, DSSCC) does not have this property because they are trained offline; IntentGPT's "learning at test time" introduces a temporal dependency that the evaluation does not monitor. This observation extends beyond the specific paper and applies to any method that uses test-time feedback loops with frozen LLMs.

## Suggestions
1. **Address the order-dependence issue head-on.** Run the full pipeline on 3–5 random shuffles of the test set (or at minimum, a batch-shuffled variant) and report mean and standard deviation. If variance is negligible, this resolves the concern. If not, analyze why and discuss implications.
2. **Add standard deviations or confidence intervals to Table 1**, even if based on a small number of runs. This is essential given the narrow margins on some metrics.
3. **State the absolute size of the Few-Shot Pool** explicitly (e.g., "the pool contains ~900 examples for CLINC and ~900 for BANKING") to make the data requirements transparent.
4. **Make the Llama-2 variant explicit throughout the paper**, not just in figure captions.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>