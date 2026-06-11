## Summary

Critique-RL proposes a two-stage reinforcement learning framework for training critique language models (models that assess and provide feedback on other models' outputs) without requiring stronger supervisors. The key insight—supported by clear empirical demonstration in Section 4.1—is that single-stage RL with indirect reward signals (derived from actor refinement correctness) fails to optimize the critic's discriminability, leading to either "conservative" or "aggressive" failure modes. Critique-RL addresses this by (Stage I) directly rewarding correct discrimination of response correctness and (Stage II) optimizing helpfulness of feedback while preserving discriminability via regularization. Experiments on math reasoning tasks (MATH, GSM8K, AQuA) with Qwen2.5-3B and Qwen2.5-7B show consistent improvements over SFT, STaR, Retroformer, and CTRL baselines, with OOD generalization to SVAMP and TheoremQA.

## Strengths

1. **Clear diagnosis of the discriminability bottleneck (Section 4.1, Figure 3)**: The paper empirically demonstrates that indirect reward signals (r_refine, r_correction, r_Δ) produce critics whose discriminability (Acc@Dis) plateaus or degrades during RL training, while helpfulness metrics (Δ^{i→c}, Δ^{c→i}) show conflicting trends. This diagnosis goes beyond prior work (Retroformer, CTRL) which used indirect rewards without analyzing this failure mode. The breakdown into "conservative" vs. "aggressive" behavior patterns, visualized through Δ^{c→i} and Δ^{i→c} trajectories, is genuinely informative and directly motivates the two-stage design.

2. **Two-stage design validated by controlled ablation (Table 3)**: The ablation study isolates each component using the same RL algorithm (RLOO): removing Stage I drops Acc@Dis from 82.8→79.7 on MATH; removing Stage II drops Acc@Refine from 48.6→45.9; removing both discrimination components from Stage II drops Acc@Dis to 77.7. This provides clean evidence that both stages contribute and that the discrimination-preserving regularization in Stage II matters.

3. **Consistent and substantial gains across 5 datasets and 2 model sizes (Table 1)**: Critique-RL outperforms all baselines on every metric for both Qwen2.5-3B and Qwen2.5-7B. Notable results include MATH 7B Acc@Dis at 85.20% vs. CTRL's 71.42% (a ~13.8 point gap) and GSM8K 7B Acc at 87.72% vs. CTRL's 81.35%.

4. **OOD generalization to held-out tasks (Table 4)**: Critique-RL generalizes to unseen SVAMP and TheoremQA, with Qwen2.5-7B achieving 89.7% Acc on SVAMP vs. CTRL's 85.1%. This supports the claim that the method produces critique models useful beyond the training distribution.

5. **Iterative training yields additional gains (Table 2)**: A second iteration further improves performance (Acc: 48.6→51.0, Acc@Dis: 82.8→86.5 on MATH 3B), showing the method does not saturate after a single pass and can compound improvements.

## Weaknesses

### Fatal
None.

### Major

1. **Confounded comparison: baselines use different RL algorithms than Critique-RL (Table 1).** The paper uses RLOO for Critique-RL, while Retroformer uses PPO and CTRL uses GRPO (Section 5.1, lines 250–252). This means the reported gains (e.g., 58.40% vs. 53.86% on MATH 7B) cannot be cleanly attributed to the two-stage reward design—they could partially reflect RLOO being more sample-efficient or stable for this training setup. The internal ablations (Table 3) are controlled (all use RLOO) and show the two-stage design matters, which partially mitigates this concern. But the headline comparisons in Table 1 against the two closest prior methods are not apples-to-apples. A controlled experiment holding the RL algorithm fixed across methods would substantially strengthen the attribution.

2. **No variance or statistical significance reporting for any result.** All tables report single-run results without standard deviations. This is particularly consequential for the OOD results on TheoremQA where gains are small (21.4% vs. 21.1% for 7B, Table 4) and could be within noise. RL training is notoriously noisy; reporting means and standard deviations across at least 3 random seeds is standard practice for empirical RL papers.

### Minor

1. **Stage I reward is a sparse binary signal that does not directly reward critique quality beyond the final judgment (Eq. 7).** The discrimination reward r_dis = 1(f(x,y,c) = r_oracle(x,y)) rewards only whether the critique's extracted final judgment matches ground truth. A critique that outputs the correct binary judgment with boilerplate or shallow analysis receives the same reward as one with detailed step-by-step reasoning. While Stage II is designed to recover helpfulness, the paper does not analyze whether Stage I models actually produce informative critiques (beyond Acc@Dis). An analysis of Stage I critique quality would strengthen the claim that the two-stage decomposition works as intended.

2. **The judgment-extraction function f(x,y,c) is not specified (Algorithm 1, Eq. 7).** The paper defines f as "the critique model's judgment of the correctness of the original response" (line 232) but does not describe how this judgment is extracted from the free-form critique text—whether via regex, prompt-based extraction, model-based parsing, or another method. This is a reproducibility gap.

3. **KL coefficient β₂ in Stage II is listed in Algorithm 1 and Eq. 9 but its value is never specified.** Only β₁ = 0.2 is given (line 274). The overall KL coefficient β = 0.01 is given for "RL" but it is unclear whether this applies to both stages uniformly.

4. **SFT data construction may introduce selection bias (Section 4.1, line 148).** The critique SFT data is filtered "based on the correctness of refinement," meaning only critiques that lead to correct actor refinements are kept. This could produce a training set skewed toward easy questions or a specific critique style. The paper does not analyze the difficulty distribution or potential bias.

5. **Modest OOD gains on the harder TheoremQA task (Table 4).** On TheoremQA with 7B, Critique-RL achieves 21.4% vs. CTRL's 21.1%—a 0.3 point gap. Without variance reporting, the significance of this result is unclear. The OOD generalization claim is better supported by SVAMP (89.7% vs. 85.1%).

### Trivial

1. The abstract's phrasing "without stronger labeling" could be read as fully unsupervised. In practice, the method requires ground-truth answer keys for every training example (to compute r_dis, r_refine, and filter SFT data). This is lighter supervision than needing a stronger model to write critiques but is still labeled supervision. Clarifying this upfront would help.

## Nice-to-Haves
- Implementing all baselines (Retroformer, CTRL reward functions) using the same RL algorithm (RLOO for all, or PPO/GRPO for Critique-RL) to enable clean attribution of gains to the two-stage reward design.
- Reporting means and standard deviations across at least 3 random seeds for all main results.
- Including an analysis of Stage I critique quality beyond Acc@Dis (e.g., informativeness of step-by-step analysis) to verify that Stage I produces genuinely informative critiques, not just correct binary judgments.
- Moving a summary of the summarization (open-ended task) results from Appendix G to the main text, since the method's broader applicability beyond answer-verifiable domains is relevant to the scalable oversight claim.

## Removed Points
These points were excluded from the main weaknesses per the filtering guidelines:
- **Summarization results should be in main text**: The parser strips appendices; these results exist in the original submission. Not a valid weakness.
- **Critique about Stage II KL regularization limiting helpfulness improvement**: The ablation (Table 3) already addresses the practical question, and the concern is speculative without empirical evidence.
- **Critique about the paper overstating contributions**: The paper's claims are appropriately scoped around math reasoning; the RL algorithm confound is real but acknowledged and partially mitigated by Table 3.
- **"Hit-picking" about missing confidence intervals**: Already captured under Major weakness #2 (variance reporting).
- **Strength Finder's generic strengths** (e.g., "the paper addressed an important problem"): These lack specific evidence anchors and were dropped.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Run Retroformer and CTRL reward functions with the same RL algorithm (RLOO) as Critique-RL, or run Critique-RL with PPO/GRPO, to enable clean attribution of gains to the two-stage reward design rather than the RL optimizer.
- Report means and standard deviations across 3+ random seeds for all main tables.
- Specify the extraction function f(x,y,c) and the value of β₂ for reproducibility.
- Add an analysis of Stage I critique quality (e.g., does Stage I produce informative step-by-step analysis or just correct binary judgments?) to verify the two-stage mechanism.

## Score and Decision

**Calibration details:**

Round 1 bracket: 5.5–7.5. Round 2 narrowed to 6.0–7.0 via comparison against topically similar anchors.

**Anchors (all rounds):**

| Path | Avg Score | Round | Comparison to Critique-RL |
|------|-----------|-------|--------------------------|
| uMxiGoczX1 (Creative writing RLHF) | 2.50 | 1 | Much weaker; different topic, rejected |
| zEhTnQZB3D (Continual RL) | 2.33 | 1 | Much weaker |
| oqRe1KvD17 (Reward-RAG) | 3.00 | 1 | Much weaker; rejected |
| 38E4yUbrgr (RL Contemplation) | 6.00 | 1,2 | Slightly weaker; similar self-improvement theme but less specific contribution |
| 6UQaXJm53B (DfPO) | 5.25 | 1 | Weaker |
| cK7yrw5g5Q (Segment Rewards) | 5.25 | 1 | Weaker; rejected |
| 4KqkizXgXU (Curiosity red-teaming) | 8.00 | 1 | Stronger; more thorough |
| mMPMHWOdOy (WizardMath) | 8.00 | 1 | Stronger; more comprehensive experiments |
| JEehcb48Vp (Critic-CoT) | 5.75 | 2 | Weaker; relies on GPT-4 distillation, less novel contribution |
| Sx038qxjek (CRITIC) | 6.50 | 2 | Comparable; different approach (tools), similar quality |
| vf8iou7FNF (RLSF) | 5.75 | 2 | Weaker |
| KFjCFxiGk4 (Certified Deduction) | 6.00 | 2 | Weaker |
| 3OyaXFQuDl (Compute-Optimal Sampling) | 7.00 | 2 | Slightly stronger; more thorough analysis |

**Final judgment:** Critique-RL is stronger than the middle-band anchors (5.75–6.00) due to its specific, well-motivated contribution and clean ablation evidence. It is comparable to CRITIC (6.50) but weaker than the 7.00+ papers which have broader or more thorough experimentation. The RL algorithm confound and lack of variance reporting prevent a higher score, but the core idea is solid and the evidence for the discriminability bottleneck is a genuine contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>