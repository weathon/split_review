Now I have a complete picture. Let me produce the final consolidated review.

---

## Summary

This paper introduces DELIFT, a data-selection framework for LLM fine-tuning that combines a pairwise utility metric (measuring how much one data point improves the model's prediction for another when used as an in-context example) with stage-specific submodular functions. The framework is applied to three fine-tuning stages — instruction tuning, task-specific fine-tuning, and continual fine-tuning — and claims 70% data reduction with minimal performance loss. Experiments on Qwen2-72B and Phi-3 across multiple datasets show that DELIFT's selected subsets consistently outperform or match baselines (Random, SelectIT, LESS) and often approach full-data performance.

## Strengths

- **Novel and well-motivated utility metric**: The core idea — measuring pairwise ICL-style informativeness via teacher-forced forward passes (Equation 1) — is conceptually elegant and distinguishes DELIFT from gradient-based methods. The ablation against a sentence-embedding variant (DELIFT(SE)) confirms that the model-aware utility kernel adds real value over static semantic similarity (e.g., Table 1: 48.46 vs. 47.43 ROUGE on MixInstruct).

- **Strong and consistent empirical results across multiple settings**: Using only 30% of the data, DELIFT achieves performance close to the full dataset in 5 out of 6 evaluation settings (P3: 0.76% drop; HotpotQA→MMLU: +5.51% *improvement*; IBM→Government: 0.31% drop; SQuAD→HotpotQA: 1.94% drop; MixInstruct→MT-Bench: 2.91% drop). In the HotpotQA→MMLU setting, DELIFT with 30% data *improves* 3.34% over the full dataset, suggesting it can prune harmful or noisy data. DELIFT also consistently beats LESS, SelectIT, and Random across nearly all metrics and settings.

- **Unified framework spanning three fine-tuning stages**: While each stage uses a different submodular function (FL, FLMI, FLCG), the same utility kernel and greedy selection algorithm apply across all three, which is more comprehensive than prior work that targets a single stage.

## Weaknesses

### Fatal
None.

### Major

- **The computational cost of the utility kernel is unaddressed, undermining the central efficiency claim.** Computing $UF_{ij}$ for *all* pairs $(i,j)$ in a dataset of size $N$ requires $O(N^2)$ forward passes through the model. For $N=21{,}000$ (the instruction-tuning experiments), this is ~441M forward passes through the *full model* (up to 72B parameters). The paper claims "at least 70% reduction in computational time compared to gradient-based methods" (line 42) and repeatedly emphasizes "computational efficiency" as a contribution, yet provides zero runtime measurements, FLOP counts, or GPU-hour comparisons. The $O(N^2)$ cost is never acknowledged or analyzed. If the claim refers only to training time (70% less data = 70% less training), this must be clarified; if it refers to the total pipeline including selection, it requires substantiation. A forward pass is cheaper than a backward pass, but 441M forward passes through a 72B model is not obviously cheaper than 21K forward+backward passes through a LoRA adapter (as in LESS). This gap affects the believability of one of the paper's four stated contributions.

### Minor

- **The mapping from $UF_{ij}$ (directional, sign-indefinite) to $s_{ij}$ in the submodular functions is never specified.** The submodular functions in Section 3.3 use $s_{ij}$ as a similarity measure, and standard theory for greedy maximization assumes $s_{ij}$ is non-negative (for monotonicity) and often symmetric. $UF_{ij}$ is explicitly directional ($UF_{ij} \neq UF_{ji}$) and can be negative (line 87). The paper never states whether $s_{ij} = UF_{ij}$, $|UF_{ij}|$, $(UF_{ij}+UF_{ji})/2$, or something else. If raw $UF_{ij}$ is used, the $1-1/e$ approximation guarantee may not hold. This does not invalidate the empirical results (the method clearly works) but creates a disconnect between the theoretical framing and the actual algorithm.

- **Ablation on subset size is reported only qualitatively.** Section 4.4 describes performance trends but provides no table or figure with actual numbers or standard deviations. Given that the 70% reduction claim is central, the full ablation data (5% to 100% in, say, 10% increments) across all use cases should be presented numerically.

- **Duplicate and broken tables in the final section of the paper.** Tables 1–4 (in \scriptsize) appear again as Tables 5–10 (in \small with underlining for second-best). Table 7 (lines 371–390, labeled "MixInstruct and MT-Bench") has empty data cells — all numeric values are missing. This suggests a copy-paste error during paper formatting and reduces confidence in the care taken with the experimental reporting.

- **No error bars, confidence intervals, or variance metrics.** Many of the performance differences between DELIFT and the second-best baseline are small (1–3%), and without variance estimates it is unclear whether these differences are meaningful. This is common in large-scale LLM evaluations but should still be noted.

### Trivial
- The paper uses length-normalized L2 distance over flattened probability vectors (Equation 2) for the utility metric without justifying this choice over cross-entropy or perplexity, which would be more standard. This does not affect the validity of the results but makes the metric harder to interpret and reproduce.

## Nice-to-Haves
- A comparison of the wall-clock time (or FLOPs) for the full DELIFT pipeline (utility kernel computation + greedy selection) vs. LESS (LoRA gradient computation + selection) on a fixed dataset size, to verify the claimed efficiency advantage.
- Clarification on whether a smaller proxy model could be used to compute the utility kernel and whether the selected subsets transfer across model scales.
- Reporting standard deviations or confidence intervals for the main results.
- Clarification on how $GT_i$ is normalized across sequences of different lengths in Equation (2).

## Removed Points

These points were flagged by reviewers but are removed per the meta-reviewer guidelines:

- **"The metric definition conflates probability distributions across tokens and sentences in a way that is not well-defined."** — The description of $GT_i$ as "a vector of ones for each token to signify perfect prediction" is standard in sequence-level distillation (one-hot encoding per token position). While cross-entropy would be more conventional, the L2 formulation is mathematically well-defined and the reviewer's characterization as "not well-defined" is inaccurate.

- **"The claimed data reduction ('up to 70% without compromising performance') is not consistently supported because of the MixInstruct 10.44% drop."** — The paper's table captions honestly report the specific drops (10.44% for MixInstruct, 0.76% for P3, etc.), and the abstract's "up to 70%" with "without compromising" is an acknowledged oversimplification but not a factual error. The paper's stated drop of 10.44% is in the table and is transparently reported. This is more of a language precision issue than a weakness in the results.

- **"Baseline comparisons: LESS is designed for pre-training not instruction tuning."** — Per the meta-reviewer rules, missing related works / baseline criticisms of this form are removed. LESS is a reasonable baseline for the settings tested, and the paper tests methods designed for similar settings.

- **"Unified framework claim: three separate strategies, not a single framework."** — Having different submodular objectives for different stages under the same utility kernel + greedy selection pipeline is a meaningful sense of "unified." This criticism is a matter of framing preference, not a factual flaw.

- **"The metric can't be computed efficiently."** — This is kept as a major weakness above (it is a real issue). What is removed is the reviewer's specific claim that it is a "structural contradiction" that invalidates the paper. The efficiency claim is ambiguous but not necessarily contradictory — it may refer to training time. The paper should clarify this; the data is there to judge.

## Novel Insights

The most interesting observation from the review process is that DELIFT's performance is *strongest in the settings where one might least expect it*. On instruction tuning (MixInstruct), the drop from full data is 10.44% — the largest across all experiments. Yet on the task-specific and continual learning settings — where one might worry about forgetting or domain mismatch — the method performs nearly indistinguishably from the full dataset or even exceeds it. This suggests the utility metric's ICL-style pairwise framing is particularly well-suited to tasks where *which* examples are selected matters more than *how many*, and less suited to broad-coverage instruction tuning where diversity across the full space is paramount. The method's success on HotpotQA→MMLU (+5.51% over full data) is noteworthy: it shows that in some settings, aggressive pruning of a training set actually improves generalization, presumably by removing noisy or misleading examples.

## Suggestions

1. **Address the computational cost directly.** Provide a wall-clock or FLOP comparison of the utility kernel computation vs. LESS's gradient computation for at least one setting. Alternatively, show that using a much smaller proxy model (e.g., 125M–1B) to compute $UF_{ij}$ transfers well to the target model, which would make the method practical at scale.

2. **Remove the duplicate tables** (Tables 5–10) and fill in the missing data in Table 7. The first set of tables is sufficient.

3. **Specify how $UF_{ij}$ is transformed into $s_{ij}$** for use in the submodular functions, and discuss whether negative values affect the greedy algorithm's guarantees.

4. **Add a numeric ablation figure** showing the 5%–100% subset-size sweep with error bars for at least one representative use case.

5. **Clarify the efficiency claim.** State explicitly whether the "70% reduction in computational time" refers to training time only (because 70% less data is used) or to the total pipeline including selection, and provide evidence for whichever is claimed.

6. **Soften the "without compromising performance" language** in the abstract or contributions to account for the 10.44% drop on MixInstruct (e.g., "with minimal or no performance loss on most tasks").

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>