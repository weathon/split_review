## Summary

Critique-RL proposes a two-stage reinforcement learning approach for training LLMs to critique model outputs (assess correctness and provide feedback) without relying on stronger supervisors. It first identifies a failure mode where RL with indirect reward signals (actor refinement correctness) improves helpfulness but degrades discriminability (ability to judge response quality), leading to overly conservative or aggressive critics. The method then addresses this via Stage I (optimizing discriminability through direct judgment-correctness rewards) and Stage II (optimizing helpfulness through refinement rewards while maintaining discriminability via regularization). Experiments on math reasoning tasks (MATH, GSM8K, AQuA) show consistent gains over SFT, STaR, Retroformer, and CTRL baselines across model sizes.

## Strengths

1. **Empirical diagnosis of a specific failure mode in RL for critique models.** Section 4.1 convincingly demonstrates (with training dynamics in Figure 3 and metrics like Acc@Dis, Δ^{c→i}, Δ^{i→c}) that indirect reward signals (r_refine, r_Δ, r_correction) fail to optimize discriminability, producing either conservative or aggressive critics. This diagnosis is non-obvious and concretely measurable.

2. **Two-stage design validated through clean ablation.** Table 3 directly attributes gains to the two-stage design: removing Stage I drops Acc@Dis from 82.8→79.7 and Acc@Refine from 48.6→47.6; removing Stage II drops Acc@Refine from 48.6→45.9; removing discrimination regularization in Stage II drops Acc@Dis from 82.8→77.7. Critically, all ablations use the same RL algorithm (RLOO), confirming the design, not the algorithm choice, drives improvement.

3. **Consistent gains across models, datasets, and settings without stronger supervisors.** Critique-RL outperforms all baselines on MATH (58.40% vs. next-best CTRL 53.86%), GSM8K (87.72% vs. 81.35%), and AQuA (65.75% vs. 64.96%) for Qwen2.5-7B, with similarly consistent results for 3B. Gains hold on OOD tasks (Table 4), with/without oracle verifier (Figure 5), and across iterative training rounds (Table 2). The critique SFT data is obtained by prompting Qwen2.5-3B-Instruct (same-scale model), not a stronger supervisor.

4. **Informative evaluation decomposition.** Beyond standard accuracy, the paper tracks discriminability (Acc@Dis), conservativeness (Δ^{c→i}), and helpfulness (Δ^{i→c}) — metrics that reveal behavioral patterns hidden by aggregate accuracy.

## Weaknesses

### Major

None. The core contribution is well-supported and no identified weakness invalidates it.

### Minor

1. **No variance estimates for smaller quantitative claims.** Neither error bars, confidence intervals, nor statistical significance tests are reported. This is consequential for smaller-magnitude claims: e.g., Critique-RL's 65.75% vs. CTRL's 64.96% on AQuA (7B) and 0.3–2.0 point gains on TheoremQA. While temperature-0 evaluation is standard, the absence of uncertainty information weakens confidence in these fine-grained comparisons.

2. **β₂ hyperparameter value is not reported.** The Stage II objective (Equation 9, Algorithm 1 line 213) includes β₂ as the scaling factor for KL regularization against the Stage I model, but its value is never stated. β₁ is reported as 0.2; β in Stage I as 0.01; β₂ is absent. This is a straightforward reproducibility omission.

3. **Stage I discriminability reward is purely judgment-based, with no direct signal for explanation quality.** The Stage I reward r_dis = 𝟙(f(x,y,c) = r_oracle(x,y)) only rewards correct final-answer judgment, not the quality of step-level explanations. SFT initialization and Stage II's r_refine reward (which depends on the actor's ability to refine based on the full critique) partially address this, but the paper does not discuss this disconnect or provide analysis of whether Stage I preserves explanation quality.

4. **Scope limitation of oracle reward during training could be more clearly stated.** The paper emphasizes "without stronger labeling" and training "without oracle reward function during testing," but the method still requires oracle rewards (correct-answer verification) during training. This is a meaningful scope condition — it reduces supervision from "expensive human/model critiques" to "verifiable correct answers" — which works well for math/code but limits applicability to open-ended tasks without such verification. The paper acknowledges this implicitly through its math focus and by mentioning summarization experiments in the appendix, but upfront clarification would strengthen the framing.

5. **Headline comparisons conflate RL algorithm with reward design (partially addressed).** Primary baselines Retroformer (PPO) and CTRL (GRPO) use different RL algorithms than Critique-RL (RLOO), so reported gains could partly stem from algorithm choice. However, the ablation study (Table 3) partially controls for this by using RLOO across all ablation variants, confirming the two-stage design's contribution. A direct RLOO-reimplementation of baseline reward designs would fully isolate the reward-design contribution.

### Trivial

None.

## Removed Points

- **AQuA failure mode underexplored**: SFT and STaR degrade on AQuA — the paper mentions this observation but does not analyze it. This is scope creep (the paper's contribution is about critique training methodology, not dataset-specific post-hoc analysis). Moved to Nice-to-Haves.
- **Inference compute scaling figure labels confusing**: The duplicate column labels in the table description are parser artifacts, not author errors. Removed per hard rules.
- **Strengths that are generic or sycophantic** (from Strength Finder): Filtered out generic praise about "addressing an important problem" and "timely topic." Only kept evidence-grounded strengths.

## Nice-to-Haves

1. **Analyze what makes AQuA different**: SFT and STaR degrade performance relative to No Critic on AQuA, which is unusual. Understanding why this happens could yield insights about task-specific sensitivities in critique training.
2. **Analyze critique content quality beyond judgment accuracy**: A qualitative or quantitative analysis of whether Stage I models actually produce coherent step-level explanations, not just correct final judgments, would strengthen the mechanism argument.

## Novel Insights

None beyond the paper's own contributions. The key insight — that RL for critique models must explicitly optimize discriminability before helpfulness, or it converges to conservative/aggressive failure modes — is already the paper's central contribution.

## Suggestions

1. Add variance estimates (error bars or confidence intervals) for all main quantitative claims, particularly the smaller-magnitude gains on AQuA and TheoremQA.
2. Report β₂ explicitly.
3. Clarify the scope condition (requires verifiable correct answers during training) in the abstract or introduction.
4. Consider adding a controlled comparison where baseline reward designs are re-implemented with RLOO to fully isolate the reward-design contribution from the RL algorithm choice.
5. Discuss the AQuA degradation pattern for SFT/STaR methods to clarify whether it reflects a broader task-specific sensitivity.

## Score and Decision

**Calibration procedure:** 

**Round 1 (Bracketing):** I queried for papers on RL training of critique/feedback models for reasoning. The low-score band (< 3.5) returned anchors like "Improving LLM Fine-tuning for Solving Math Problems" (3.00) and "StepProof" (3.25) — these are much weaker papers. The middle band (3.5–7.5) returned highly relevant anchors including "Critique Ability of LLMs" (4.67, a benchmark paper), "Critic-CoT" (5.75, trains critique models with stronger supervisors), "RLSF" (4.50), and "VerifierQ" (5.25). The high band (> 7.5) returned "WizardMath" (8.00), "miniCTX" (8.00), and others at the top-tier level. The paper is clearly above all middle-band anchors and below the 8.0-level papers. **Round 1 bracket: 5.5–7.5.**

**Round 2 (Narrowing):** I queried within 5.5–7.5 for papers on RL training, critique models, and self-correction. This retrieved "LM Self-improvement by RL Contemplation" (6.00, weaker evaluation, limited model sizes), "CRITIC" (6.50, tool-based self-correction without training), "LLMs Cannot Self-Correct Yet" (6.75, influential critique paper), "Learn from Mistakes" (6.75, pretraining data approach), and "ACC-Debate" (5.75). I read "Critique Ability" (4.67), "Critic-CoT" (5.75), "CRITIC" (6.50), "RL Contemplation" (6.00), "ACC-Debate" (5.75), and "LLMs Cannot Self-Correct Yet" (6.75) in full.

**Comparison:** vs. "Critic-CoT" (5.75): Critique-RL has the major advantage of not relying on a stronger supervisor (Critic-CoT distills from GPT-4-Turbo), has more thorough ablations, and shows larger gains. vs. "CRITIC" (6.50): CRITIC is a prompting framework using external tools; Critique-RL addresses the harder problem of *training* critique models and provides deeper analysis of the discriminability failure mode. vs. "RL Contemplation" (6.00): Critique-RL tests on larger models (3B, 7B vs. 780M Flan-T5), has cleaner ablations, and identifies a non-obvious failure mode. The main weaknesses keeping Critique-RL below 7+ are the missing variance estimates, unreported β₂, and partially confounded baseline comparisons — none fatal, but enough to distinguish it from top-tier contributions.

**Final score: 6.5.** The paper makes a genuine, well-supported contribution to training critique models without stronger supervisors. The empirical diagnosis of the discriminability failure mode is insightful, and the two-stage solution is clean and validated. The weaknesses are real but non-fatal and largely addressable in revision.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>