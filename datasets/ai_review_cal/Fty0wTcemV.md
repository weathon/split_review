- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces DELIFT, a data selection algorithm for LLM fine-tuning that uses a novel pairwise utility metric (measuring how well one sample serves as an in-context example for another) combined with submodular optimization. It targets three fine-tuning stages (instruction tuning, task-specific, continual) with different submodular functions, and reports results on two model families (Qwen2-72B, Phi-3) across multiple benchmarks, showing that selecting 30% of data can match or approach full-dataset performance while outperforming existing selection methods like LESS and SelectIT.

## Strengths

- **Novel utility metric that avoids per-sample gradient computation (Eq. 1–2)**: The ICL-based pairwise influence measure uses only forward passes and does not require gradient backpropagation for individual samples, making it conceptually distinct from gradient-matching approaches like LESS or GradMatch. This is a genuinely different approach to estimating data informativeness.

- **Comprehensive evaluation across three distinct fine-tuning stages with two model scales**: The paper evaluates on instruction tuning (MixInstruct, P3), task-specific fine-tuning (HotpotQA→MMLU, MixInstruct→MT-Bench), and continual fine-tuning (SQuAD→HotpotQA, IBM→Government), using both Qwen2-72B and Phi-3 models. This breadth convincingly demonstrates the framework's applicability beyond a single setting.

- **Consistent outperformance over strong baselines (SelectIT, LESS, Random)**: In nearly every configuration, DELIFT at 30% data beats other selection methods at the same budget. For example, on MixInstruct Qwen2 ICL ROUGE: DELIFT 48.46 vs. SelectIT 43.08 vs. LESS 42.08 (Table 1). On MMLU accuracy (HotpotQA→MMLU): DELIFT 81.70 vs. LESS 80.35 vs. SelectIT 79.13 (Table 5).

- **Clean ablation isolating the utility kernel from the submodular framework**: The DELIFT-SE variant (replacing the utility kernel with sentence embeddings while keeping the same submodular functions) consistently underperforms DELIFT, demonstrating that the utility metric itself — not just the submodular selection — drives the improvement.

- **Real-world continual learning task**: The IBM/government query-rewriting task (Table 6) shows DELIFT's practical value on a proprietary, domain-specific dataset where it even outperforms full-data fine-tuning (69.49 vs. 66.08 on Qwen2 ICL ROUGE).

## Weaknesses

### Fatal
None.

### Major

1. **The central efficiency claim is unsubstantiated and likely contradicted by the method's design.** The paper claims "at least 70% reduction in computational time compared to gradient-based methods on benchmark tasks" (line 42) and highlights computational efficiency as a core contribution. However, **no runtime measurements, wall-clock comparisons, or complexity analyses appear anywhere in the paper.** By design, computing the utility kernel requires evaluating UF_{ij} for all N(N−1) pairs — approximately 441 million forward passes for the 21,000-sample subsets used. Each forward pass processes a concatenated ICL example and query. Gradient-based methods like LESS require only N LoRA gradient computations (backward passes). Since a backward pass is roughly 2× the cost of a forward pass, LESS's selection cost is O(N) while DELIFT's is O(N²). Without any timing data, the claimed efficiency advantage is unsupported and appears implausible given the method's quadratic scaling. This is a major evidential gap for one of the paper's headline contributions.

2. **The subset-size ablation study is described entirely qualitatively with no supporting evidence.** Section 4.5 (lines 318–320) claims that "performance gains plateau beyond 50%" and that "DELIFT outperforms all baselines across subset sizes from 5% to 100%" — but provides no table, figure, or numerical results. This ablation is critical for justifying the 30% selection budget used throughout the paper. Its absence means the central claim that 30% is a "sufficient" subset size rests on an unverifiable assertion.

### Minor

3. **The "26% improvement" claim compares against the worst baseline without clarification.** The contribution statement (line 44) says "up to 26% in effectiveness across diverse tasks and model scales." In the results (line 311), this is revealed to be a 26.21% advantage over the *worst-performing* baseline (Random/Initial). Against the next-best competitive baseline (SelectIT or LESS), improvements are typically in the 2–6% range. The contribution-level claim is technically true but misleadingly selective in its reference point.

4. **The HotpotQA→MMLU result (Table 5) is framed selectively.** DELIFT achieves 81.70 vs. Full Data's 78.36 — an improvement of 3.34% over full-data fine-tuning. However, the *Initial* model (no fine-tuning on HotpotQA) scores 82.10, meaning every selection method (including DELIFT) underperforms doing nothing. The paper presents this as "DELIFT outperforms Full Data" without acknowledging that the best result is still worse than the starting point. The hidden comment (line 408: "%Results show that by fine-tuning on HotpotQA, there is a drastic performance degradation of MMLU performance") is more honest but was commented out. This framing exaggerates the positive result.

5. **No justification for the ICL-to-fine-tuning transfer assumption.** The utility metric measures how well sample j serves as an ICL example for sample i *at the current model state*. However, the selected data is used for *fine-tuning* where the model's weights change. The paper assumes these correlate without any analysis (e.g., correlation with per-sample gradient norms or loss reduction). While correlation is plausible, a brief discussion or simple validation would substantially strengthen the contribution.

6. **Imprecise definition of the ground-truth distribution.** Equation (1) defines GT_i as "a vector of ones for each token" (line 76). The intended meaning is a one-hot vector or target token assignment, but "vector of ones" literally means [1,1,…,1], which is not a valid probability distribution. This is a minor notational imprecision — the metric itself is coherent under the intended interpretation — but it will confuse readers.

### Trivial
- The scaling factors η and ν in Equations (4) and (5) are set to 1 with no sensitivity analysis.
- No confidence intervals or standard errors are reported for any experiment; results are presented as point estimates from single runs.

## Nice-to-Haves
- A runtime/efficiency comparison (wall-clock time) measuring total cost (selection + training) for DELIFT vs. LESS vs. full-data training would resolve the most significant open question about the method's practical value.
- A validation experiment showing that UF scores correlate with per-sample fine-tuning utility (e.g., gradient-norm alignment or leave-one-out loss changes) would strengthen the conceptual foundation.
- An ablation comparing different submodular functions for the same stage (e.g., FLMI vs. FL for instruction tuning) would clarify the design choices.

## Removed Points
- **"Unified framework claim is misleading (three separate objectives)"**: The paper presents a coherent methodology (utility kernel + submodular optimization) where the choice of submodular function is part of the framework's design. Using different objectives for different stages is a feature, not a bug. This criticism overinterprets what "unified" means.
- **"Duplicate tables in the paper"**: These are parser artifacts from PDF extraction, not author errors. The original submission does not have this issue.
- **"Related work overstates limitations of existing methods" / "LESS is closer to DELIFT than implied"**: The paper accurately describes LESS as using LoRA gradients with random projection — a fundamentally different approach from DELIFT's forward-pass-based pairwise influence. The distinction is valid.
- **"Missing runtime as specific experiment (point 4 in Strengthening)"**: Already covered in Major weakness #1 above; merged.
- **"ICL evaluation is tangential"**: ICL is presented as a secondary application, which is reasonable for a data selection paper. The primary evaluation is QLoRA fine-tuning.

## Novel Insights
None beyond the paper's own contributions. The reviews primarily surface gaps in evidence (runtime, ablation) rather than independent novel observations about the method.

## Suggestions
1. **Provide runtime measurements.** Report wall-clock time for utility kernel construction, for the greedy submodular selection step, and for the combined selection + fine-tuning pipeline. Compare against LESS (gradient computation + selection) and training on 100% data. This single addition would resolve the most significant weakness.
2. **Include the subset-size ablation as a figure.** Even a single metric on one dataset (e.g., LAJ on MixInstruct, Qwen2 QLoRA) across 5/10/30/50/100% would substantiate the claim that 30% is a reasonable budget.
3. **Clarify the "26% improvement" framing** by specifying the baseline (worst vs. best) in both the contribution list and the conclusion.
4. **Acknowledge the HotpotQA→MMLU limitation explicitly** — i.e., that all methods underperform the initial model, and DELIFT's contribution is minimizing negative transfer rather than improving absolute performance.
5. **Fix "vector of ones" to "one-hot vectors" or "ground truth token indices"** for clarity.
