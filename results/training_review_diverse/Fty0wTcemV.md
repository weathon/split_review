Now I have a thorough understanding of the paper and all the claims. Let me write the consolidated review.

---

## Summary

This paper introduces DELIFT, a data subset selection algorithm for LLM fine-tuning that combines a novel pairwise utility metric (measuring how much one sample's inclusion as an in-context example improves prediction on another) with submodular optimization. The method is evaluated across three fine-tuning stages (instruction tuning, task-specific fine-tuning, continual fine-tuning), two model scales (Phi-3 3.8B, Qwen2-72B), and multiple datasets, consistently outperforming baselines (SelectIT, LESS, Random) while reducing data by 70% with minimal or no performance loss.

## Strengths

1. **Novel pairwise utility metric grounded in model feedback**: The metric \(UF_{ij}\) quantifies the improvement in predictive accuracy on sample \(i\) when sample \(j\) is used as an in-context example, using only forward passes with teacher forcing. This is model-aware, dynamically reflects the model's current capabilities, and avoids the expensive gradient computations of methods like LESS (Section 3.2, Equation 1).

2. **Unified framework across three fine-tuning stages**: DELIFT tailors three submodular functions (FL for instruction tuning, FLMI for task-specific fine-tuning, FLCG for continual fine-tuning) within a single greedy selection algorithm, sharing the same utility kernel across all stages. This is more comprehensive than existing methods that target only a single stage (Section 3.3, Section 4.1).

3. **Consistent and substantial outperformance of baselines**: Across extensive experiments (24 evaluation settings: 2 models × 2 paradigms × 3 metrics × 2 datasets for each use case), DELIFT (Util. Feat.) achieves the best performance among all subset selection methods on the vast majority of metrics. For example, on Use Case 1 (MixInstruct), it outperforms the next-best baseline by 2.27% and the worst baseline by 26.21% (Table 1 and surrounding text).

4. **Data reduction with minimal or no performance degradation**: DELIFT reduces the fine-tuning dataset by 70% while incurring only a 0.76% performance drop on P3 (Table 2), a 1.94% drop on SQuAD→HotpotQA (Table 6), and actually *improving* over full-data training by 5.51% on the HotpotQA→MMLU transfer task (Table 5). This demonstrates that strategic selection can match or exceed full-data performance.

## Weaknesses

### Fatal
None.

### Major

1. **Missing runtime/complexity analysis for a paper claiming computational efficiency**: The paper prominently lists "Computational Efficiency" as Contribution 3, claiming "at least 70% reduction in computational time compared to gradient-based methods on benchmark tasks" (line 42). However, **zero runtime measurements, wall-clock times, or FLOP counts are provided anywhere in the paper**. For the 72B-parameter model (Qwen2-72B) and the smallest dataset used (21,000 samples), computing \(UF_{ij}\) for every pair would require ~441M forward passes through the model. The paper offers no analysis of how this cost scales, whether pairs are subsampled, or whether a proxy model is used. Without this information, the central efficiency claim is unsubstantiated, and a reader cannot assess whether the method is practically viable at the claimed scales. This is the most significant gap in the paper.

2. **No explanation of how the O(N²) pairwise kernel is computed at scale**: The methodology section (line 149) states "Calculate \(UF_{ij}\) for all relevant pairs of data points" with no clarification of what "relevant" means. The paper does not describe any approximation strategy, subsampling scheme, or computational optimization for the pairwise utility matrix. For any real-world dataset (e.g., 21k samples), a naive all-pairs computation is prohibitive, especially for a 72B model. This is not a minor omission—it is a fundamental detail about whether the method can be deployed.

### Minor

3. **"Performance percentage drop" is undefined and aggregates across heterogeneous metrics**: The captions report single aggregate numbers like "10.44% performance percentage drop from Full Data to DELIFT" without specifying how this is computed across different metrics (ROUGE, BGE, LAJ), models (Qwen2, Phi-3), and paradigms (ICL, QLoRA). Per-metric variation is substantial—e.g., on MixInstruct Qwen2 ICL, ROUGE drops ~17% (58.65→48.46) while LAJ drops ~3% (3.45→3.35). Averaging these into one number obfuscates the variance and makes the metric uninterpretable. The raw data is in the tables, but the summary figures need clarification.

4. **Subset size ablation lacks numerical results**: Section 4.3 describes the ablation study qualitatively ("performance gains plateau beyond 50% subset size," "DELIFT outperforms all baselines across subset sizes from 5% to 100%") but provides **no table, figure, or numerical data** to support these claims. The reader cannot verify the trend or inspect the actual numbers. This weakens what could otherwise be a valuable robustness analysis.

5. **Imprecise description of the ground truth distribution**: Equation (1) defines \(GT_i\) as "modeled as a vector of ones for each token to signify perfect prediction" and calls it a "ground truth distribution" and "probability distribution." A vector of ones is not a probability distribution (its entries do not sum to 1). However, the actual computation—\(d(GT_i, p) = \sqrt{\sum_{k=1}^N (1 - p_k)^2 / N}\) where \(p_k\) is the model's predicted probability of the correct token at position \(k\)—is mathematically well-defined and meaningful as an RMSE between perfect confidence and actual confidence. The description needs correction but the metric itself is valid.

6. **Duplicated tables with different formatting**: Several tables appear twice (e.g., Tables 1 and the later version with "Util. Feat." labeling; the IBM-Government and SQuAD-HotpotQA tables appear twice with different styling). This suggests editorial carelessness and could confuse readers.

### Trivial

7. **"Flattened probability distributions" in Equation (2) could be clarified**: The term "flattened" is not explicitly defined. From context (teacher forcing, sum over \(k=1\) to \(N\)), it is clear that \(p_k\) refers to the model's probability of the correct token at position \(k\), but stating this explicitly would avoid ambiguity.

## Nice-to-Haves

- A runtime comparison table (wall-clock time or forward-pass count) for each selection method, broken down by dataset size and model scale, would directly substantiate the efficiency claim and is the single most impactful addition the authors could make.
- An analysis of how the pairwise utility matrix can be approximated (e.g., via random pair sampling, clustering, or using a smaller proxy model) would address scalability concerns.
- The "task-specific fine-tuning" experiments (Use Case 2: HotpotQA→MMLU, MixInstruct→MT-Bench) are better described as "selecting data from a heterogeneous pool to improve a target task" rather than standard task-specific fine-tuning. A clarifying sentence would prevent misinterpretation.

## Removed Points

These points were identified in the provided reviews but are removed or downgraded after verifying against the paper:

- **"The ground truth distribution issue is fatal"** (Harsh Critic, Critical Issue 2): The reviewer claims this invalidates the method. However, while "vector of ones" is not technically a probability distribution, the computation \(d(GT_i, p) = \sqrt{\sum_k (1 - p_k)^2 / N}\) is mathematically well-defined and measures the RMSE between perfect confidence and the model's confidence on the correct token. The description is imprecise but the metric is valid. Downgraded from fatal to minor.

- **"Use Case 2 does not measure task-specific fine-tuning"** (Harsh Critic, Critical Issue 3): The reviewer claims this measures catastrophic forgetting rather than task-specific adaptation. However, the FLMI function explicitly selects data from the training pool that maximizes mutual information with the target dataset. Selecting data informative for a target task from a heterogeneous pool is a legitimate formulation of task-specific fine-tuning. The fact that the experiment also reveals forgetting-mitigation properties is a feature, not a flaw. Removed.

- **"Unified framework claim is overstated"** (Harsh Critic): The three submodular functions are indeed applied to different stages, but the utility kernel is the shared core that unifies them. This is a reasonable use of "unified framework." Removed.

- **"Several tables appear twice"** is a genuine observation, kept as minor weakness #6.

## Novel Insights

The reviews collectively highlight a tension that the paper itself does not fully engage with: the pairwise utility kernel's O(N²) nature creates a tension between model-awareness and scalability. The method requires a forward pass for every pair (i, j), which is O(N²) in the number of forward passes, while gradient-based methods like LESS require O(N) backward passes. Forward passes are cheaper than backward passes per-unit, but the quadratic vs. linear factor means the comparison depends critically on N, model size, and whether approximations are used. The paper's failure to provide any complexity analysis or runtime data means this tension goes unresolved, and the claimed "70% reduction in computational time" cannot be evaluated. Beyond the paper's own contributions, the reviews reveal that the real question for this line of work is not just "does the metric work?" but "can the metric be computed at the scales where it matters?"—a question the paper leaves unanswered.

## Suggestions

1. **Add a runtime analysis table** showing wall-clock time (or number of forward/backward passes) for each selection method, including DELIFT (utility kernel), DELIFT (sentence embedding), LESS, SelectIT, and Random, across at least the two dataset sizes and two model scales used in the paper. This is essential to substantiate Contribution 3.

2. **Define the "performance percentage drop" metric explicitly** and consider reporting per-metric breakdowns alongside the aggregate.

3. **Add a table or figure for the subset size ablation** (Section 4.3) with actual numerical results across 5%, 10%, 25%, 50%, 75%, and 100% for at least one representative use case.

4. **Correct the description of \(GT_i\)**: Clarify that it is a vector of ones representing perfect prediction confidence at each token position (not a probability distribution) and that the distance in Equation (2) computes the RMSE between this ideal and the model's actual predicted probability for the correct token.

5. **Discuss the scaling of the pairwise kernel**: Even a brief complexity analysis (e.g., "computing the full UF matrix requires \(O(N^2)\) forward passes, but in practice we [subsample pairs / use a smaller model / exploit greedy selection to avoid full computation]") would significantly strengthen the paper.

## Score and Decision

The paper presents a genuinely interesting approach to data-efficient fine-tuning with strong empirical results. The pairwise utility metric is novel, the unified framework is well-motivated, and the experiments are comprehensive across multiple stages, models, and datasets. However, the paper makes an explicit computational efficiency claim ("70% reduction in computational time") without providing any runtime measurements, and it does not address how the O(N²) pairwise kernel scales to realistic dataset sizes. These are not fatal—the core data-selection contribution is still valid—but they are significant gaps that prevent acceptance at the current level of completeness. The paper would benefit from a major revision that adds a runtime analysis and scaling discussion, after which it could be a strong contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>