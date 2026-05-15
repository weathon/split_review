Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual text. Let me produce the final consolidated review.

## Summary

The paper proposes I-LoRA, a pipeline for multi-task learning with vision-language models that combines (1) **Routing Tuning** — a fine-tuning procedure that augments standard LoRA training with KL-divergence and L2-norm losses on general data to constrain adapter activations — and (2) **Iterative Merging** — a method that applies SVD truncation (80% of singular values retained) followed by element-wise max-of-absolute-values to fuse adapters without adding parameters. Experiments on Atari games using LLaVA-Interleave-Qwen-7B show competitive single-task performance and improved multi-task merging compared to DARE and TIES baselines.

## Strengths

- **The Routing Tuning objective is a novel and principled approach to reduce parameter interference**: Adding KL-divergence (aligning LoRA output with base model on general data) and L2-norm (minimizing LoRA B-layer output magnitudes) is well-motivated by model-unlearning literature and targets the composability problem directly. Table 2 indicates that single-task performance is largely preserved after routing tuning.

- **SVD truncation + max-absolute merging yields clear empirical improvements over existing PEFT merging methods**: Table 4 reports that I-LoRA achieves retention ratios (0.552 on the best game) substantially above DARE (0.203) and TIES (0.000), and Table 5 demonstrates that iterative merging across five diverse Atari games maintains performance on all tasks without catastrophic collapse. This is a concrete advance over prior off-the-shelf merging.

- **The method requires no extra inference parameters**: Unlike MoE-style router-based adapter fusion, the merged model has exactly the same architecture as the base model. This makes iterative integration practical for lifelong learning scenarios where adding routing modules for each new task is prohibitive.

- **Strong single-task VLM baseline on Atari**: The paper constructs a high-resolution Atari dataset with chain-of-thought annotations and shows that a VLM fine-tuned with LoRA outperforms state-of-the-art RL algorithms (SPR, DreamerV3, DART) on the mean/median human-normalized score across 16 games (Table 1).

## Weaknesses

### Fatal
None.

### Major

- **No ablation isolating the contribution of Routing Tuning to merging quality**: The paper evaluates the *combined* pipeline (Routing Tuning + SVD+max merging) against DARE and TIES, but never compares merging *with* Routing-Tuned adapters versus merging *without* Routing Tuning (i.e., standard LoRA adapters followed by the same SVD+max procedure). Without this control, it is impossible to attribute the merging improvements to the routing-tuning loss rather than to the SVD+max merging technique itself. This is the most critical gap in the experimental evaluation, as it leaves the paper's core claim — that Routing Tuning reduces interference between adapters — empirically unverified.

- **Missing key baselines for the multi-task and iterative merging experiments**: (a) Simple averaging of adapter weights (element-wise mean), the most natural baseline, is not reported. (b) The joint fine-tuning baseline in Table 4 ("mixing the dataset of 4 games") is mentioned but per-game performance breakdown is not given, making it impossible to assess whether trade-offs exist. (c) For the iterative merging results (Table 5), there is no comparison to sequential fine-tuning (standard LoRA trained on tasks one after another), which would directly measure catastrophic forgetting — the central problem the paper claims to address. (d) The claim of order independence ("without being influenced by task order") is stated in the abstract but never tested by varying the merging order.

- **Conceptual confusion between stated properties and the merging function**: The paper lists "Equality" (each adapter has equal opportunity) as a desired property, then acknowledges that linear addition satisfies this but causes sign-cancellation/amplification, and finally adopts the max-of-absolute-values function. The paper never clarifies whether or how max satisfies the Equality property — it clearly does not (it is winner-take-all per parameter position). This undermines the claimed theoretical grounding. The method may be empirically effective, but the narrative about properties is inconsistent and should be clarified or dropped.

### Minor

- **Ambiguity in the merging procedure description**: It is unclear (a) whether the max operation is applied to the SVD-truncated matrices or the original matrices, (b) whether the LoRA scaling factor s = alpha/rank is folded into the weight matrices before merging or applied separately, and (c) how the "0.8 quantile" rule works in the iterative case when the cumulatively merged adapter and the new adapter have different ranks. While the high-level idea is understandable, these details matter for exact reproducibility.

- **No SVD truncation sensitivity analysis**: The paper states that the proportion of retained singular values "did not significantly impact performance" but provides no supporting data or ablation. The 80% threshold appears heuristic.

- **Missing reproducibility details for the general dataset and training setup**: The general-purpose dataset combines "LLava model's training data" with "general game data sampled from publicly available datasets from the Internet" — neither is specified with enough precision to reconstruct. The ratio of general to task data in each batch is not reported.

- **Per-task scores after merging are not reported**: Tables 4 and 5 report summary ratios but not per-task breakdowns. This makes it impossible to assess whether the merged model trades off one task's performance for another.

### Trivial
- The text in Section 4.2.2 contains garbled/truncated sentences ("we applied our Routing Tuning method nothing for all games in our scenario, so the final score is 0"), likely a parsing artifact.
- "0.85%" in the Table 2 caption is clearly meant to be "85%" — a typographical error.

## Nice-to-Haves
- An analysis of how the max-of-absolute-values merging function interacts with the LoRA scaling factor (alpha/rank) would strengthen the presentation.
- Including singular value spectrum visualizations for single-task and fused adapters would help illustrate why truncation helps.
- Measuring a quantitative interference metric (e.g., activation overlap on general data) with and without Routing Tuning would directly support the paper's central motivation.

## Removed Points

Points that were flagged for removal, kept here for traceability:

1. **"Tables are embedded images making data unreadable"** — REMOVED (formatting nitpick; tables in the original PDF are readable; the paper clearly labels each table with a descriptive caption).
2. **"No comparison with AdaMix or MoE-style routers"** — REMOVED (scope creep; the paper explicitly scopes out methods that introduce extra parameters, which is a reasonable design choice for iterative merging).
3. **"The paper does not differentiate I-LoRA from DARE/TIES in the related work"** — REMOVED (the paper does differentiate: it states DARE/TIES do not address parameter interference, which is the paper's focus; this is adequate differentiation).
4. **"Only RL algorithms compared in single-task performance"** — REMOVED (this is a standard comparison for Atari benchmarks; the paper is not claiming to beat all possible VLM baselines, only showing that VLM fine-tuning is effective on this setup).
5. **"Atari dataset quality confound from RL checkpoints"** — REMOVED (the paper acknowledges this as a finding: "Data quality is crucial"; it frames RL-trained checkpoints as the source of training data, which is a valid experimental design choice, not a confound).
6. **Strength Finder strength about "Method works across tasks with significant differences"** — REMOVED (this is generic; any multi-task paper's tasks differ).
7. **"The paper explicitly recognizes the need for properties"** from Strength Finder — REMOVED (this is too generic; recognizing properties without satisfying them is not a strength).
8. **"The focus on iterative merging without extra inference parameters is a worthwhile goal"** — REMOVED (this is already captured in the strengths section as Strength 3 with more specific grounding).

## Novel Insights

Beyond the paper's own contributions, a meta-observation emerges from the review process: the paper's combination of an *unlearning-inspired fine-tuning constraint* with a *winner-take-all merging rule* (max-of-absolute-values) is an interesting design pattern that deserves deeper theoretical analysis. The routing-tuning loss essentially "sparsifies" each adapter's activation on general data, which pairs naturally with max-based merging — if each adapter is largely inactive on non-target tasks, then picking the largest absolute value at each position becomes a kind of soft routing that selects whichever adapter "cares" about that parameter for its task. The paper does not make this connection explicit, but it is a plausible deeper rationale that warrants investigation in future work.

## Suggestions

1. **Add the critical ablation**: Compare merging of Routing-Tuned adapters vs. standard LoRA adapters using the same SVD+max procedure. This single experiment would either validate or refute the paper's central claim and is the most impactful addition.
2. **Add simple averaging as a baseline** and report per-task scores for all merging experiments, not just aggregate ratios.
3. **Test order sensitivity** by performing iterative merging with at least 2–3 different task orders.
4. **Clarify the relationship between the listed properties and the max function** — either explain why max satisfies (or approximately satisfies) the properties, or remove the property-based justification and instead motivate max directly by its empirical benefits and the "distance from zero" criterion.
5. **Provide exact reproducibility details**: general data composition, task-to-general data ratio, baseline hyperparameters (especially for DARE/TIES), and the precise steps of the SVD+max pipeline including how scaling factors are handled.

## Score and Decision

This paper tackles an important problem and puts forward a creative pipeline with two independently interesting components (routing-tuning loss and SVD+max merging). The empirical results on Atari games are promising and show tangible improvements over existing PEFT merging methods. However, the experimental evaluation has critical gaps — most importantly, the missing ablation of Routing Tuning for merging and the absence of basic baselines (simple averaging, sequential fine-tuning) — that prevent the paper from convincingly supporting its core claims. The conceptual confusion about the merging properties further weakens the presentation. These issues are addressable but require substantial additional experiments.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>