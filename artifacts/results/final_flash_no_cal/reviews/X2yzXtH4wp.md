Now I have a thorough understanding of the paper. Let me compile the final review.

## Summary

The paper introduces Ambig-SWE, a benchmark for studying how LLM agents handle underspecified instructions in code generation tasks. It pairs each SWE-Bench Verified issue with a GPT-4o-generated underspecified version, preserving the full specification as ground truth. The paper decomposes the resolution process into three capacities—detection of missing information, quality of clarification questions, and leveraging interaction for task completion—and evaluates six models (proprietary and open-weight) across three settings (Full, Hidden, Interaction). The key empirical findings show that interaction can significantly improve performance on underspecified tasks (up to 74% recovery of the gap to full specification), but models vary dramatically in their ability to detect underspecification and ask effective questions.

## Strengths

- **Controlled benchmark for underspecificity in agentic code tasks.** Ambig-SWE's paired design (each fully-specified SWE-Bench Verified issue + an underspecified version) enables causal measurement of the value of interaction—something impossible with naturally occurring underspecified issues that lack validated correct specifications (Section 2.1).

- **Decomposition into three independent capacities.** The paper separately evaluates detection (RQ2), question quality (RQ3), and task completion via interaction (RQ1). This fine-grained diagnostic framework isolates where models succeed or fail, going beyond a single aggregate accuracy number (Sections 3–5).

- **Clear within-model evidence that interaction recovers substantial performance.** Claude Sonnet 4 improves from 40.0% (Hidden) to 61.4% (Interaction), recovering ~76% of the gap to the Full setting (68.0%). Wilcoxon signed-rank tests confirm the Hidden-vs-Interaction difference is significant for all models (Table 4, Section 3.1).

- **Identification of critical failures in detection.** Most models rarely interact without explicit prompting; Qwen 3 Coder never asks a single question even with strong encouragement (100% FNR). Claude Sonnet 4 achieves only 89% accuracy but only under the strongest prompt, revealing that prompt engineering alone is insufficient for reliable detection (Section 4.2, Table 2).

- **Insight that question strategy matters as much as quantity.** Claude Sonnet models achieve information gain comparable to Qwen 3 Coder (0.171 vs. 0.179 cosine distance) while asking ~50% fewer questions (4.03 vs. 6.02) by exploring the codebase first and asking only what cannot be independently discovered. This shows that integration efficiency is a distinct skill from information extraction volume (Section 5.3, Table 6, Figure 5).

- **Rigorous simulated user design.** The GPT-4o proxy answers only from the full issue text and responds "I don't have that information" when queried about missing details, avoiding hallucination and isolating the agent's ability to detect and recover from missing information (Section 2.2).

- **Quantitative comparison to natural underspecification.** The paper analyzes how its generated underspecified issues differ from naturally occurring ones (fewer code snippets, error messages), showing that the synthetic data is a deliberately more challenging—but still ecologically valid—form of underspecificity (Section 2.1).

- **Differential effect of navigational vs. informational details.** Table 1 reveals that acquiring file locations boosts performance for most models but actually hurts Qwen 3 Coder (52.38% resolve with navigational info vs. 55.43% without), exposing rigid protocol-following behavior that undermines the benefit of interaction.

## Weaknesses

### Fatal
None. The paper's core contributions (the benchmark, the diagnostic framework, the within-model experiments, and the qualitative behavioral insights) are not invalidated by the weaknesses below. The confounded cross-model comparisons and overreaching training claims are significant but fixable issues.

### Major

- **Unequal agent turn budgets confound cross-model comparisons.** The paper restricts most models to 30 interaction turns but allocates 100 turns to Claude Sonnet 4 and Qwen 3 Coder, justified by their "greater reasoning and planning capacity" (Section 3.1, line 106). Because the budget simultaneously controls exploration depth, solution-attempt count, and interaction capacity, it is a direct confound for every cross-model comparison in Figure 3 and Table 1. Claims such as "Claude Sonnet 4 attains the highest relative performance (89%)" and "proprietary models generally demonstrate greater effectiveness in utilizing interaction" cannot be cleanly attributed to model capability or interaction effectiveness when the favored models operated under a 100-turn horizon that lower-performing models were categorically denied. The paper does not discuss this as a limitation, provide an ablation, or attempt to control for budget. This is a basic experimental control failure for the cross-model comparisons. Within-model comparisons (Hidden vs. Interaction for the same model) are not affected because the budget is consistent per model, but the paper's narrative frame centers on cross-model contrasts that are unreliable.

- **Unwarranted causal attribution of observed behaviors to training methodology.** The paper repeatedly claims that specific agent behaviors imply identifiable training deficiencies, e.g.: "current training practices insufficiently optimize for effective integration of interactive feedback" (Section 7), "suggesting fundamental limitations in certain training approaches" (Section 4.3), and "current training paradigms may insufficiently promote adaptive integration of interactive feedback" (Section 3.3). The paper provides no evidence about how these models were trained—no training ablations, no inspection of training data, no comparison across checkpoints. It observes behavioral patterns in a benchmark environment and leaps to causal statements about pre-training or fine-tuning practices. These claims should be reframed as behavioral observations with implications for agent policy design, prompt engineering, and evaluation, not as evidence of training deficiencies.

### Minor

- **Incomplete Hidden baseline for Claude Sonnet 4.** Sonnet 4 is evaluated on only 100 of the 500 issues in the Hidden setting due to cost (footnote 4). The paper states the results remain "statistically significant," but significance does not guarantee the magnitude of the improvement is unbiased. The 100 issues may not reflect the same difficulty distribution as the full set. Since Sonnet 4 is the paper's flagship model and its headline "89% relative performance" depends on the Hidden baseline, an explicit characterization of the representativeness of the 100-issue subset is needed.

- **RQ2 detection metric conflates detection with action policy.** The paper measures whether models *ask* questions when given underspecified inputs and frames this as "detection of incomplete task specifications." However, a model could detect that information is missing but still refuse to ask (e.g., Qwen 3 Coder's 100% FNR could reflect a training bias against asking questions rather than a detection failure). The metric measures *agentic discrimination*—the joint capacity to detect underspecification *and* act on it—not pure cognitive detection. The paper should reframe its conclusions (e.g., "LLMs struggle to detect missing information") accordingly. The three prompting levels partially mitigate this concern but do not fully disentangle detection from action.

- **No human validation of the Ambig-SWE dataset.** The dataset is generated by GPT-4o, its underspecificity is characterized by LLM annotations, and the proxy user is GPT-4o. While the distributional analysis comparing to natural underspecification is a useful step, a small-scale human judgment study confirming the plausibility and realism of the underspecified issues would substantiate the claim that the benchmark captures realistic underspecificity.

### Trivial

- **Missing confidence intervals for key metrics.** Figure 3 reports Resolve Rates without error bars or confidence intervals. Given that the evaluation covers 500 issues (or 100 for Sonnet 4 Hidden), bootstrapped CIs would help readers gauge the reliability of the reported improvements.

## Nice-to-Haves

- **Analyze sensitivity to user proxy behavior.** The proxy is designed to be maximally cooperative and honest—it never hallucinates and says "I don't know" when it lacks information. Real users do neither. The paper acknowledges this as a limitation but does not analyze how varying proxy behavior (e.g., a user who provides misleading information or is impatient) would affect results. This would be a natural extension for future work.

- **Complete the Sonnet 4 Hidden baseline** on the full 500 issues (or at minimum characterize the difficulty distribution of the 100-issue subset to defend its representativeness).

## Removed Points

These points are flagged to be removed; treat them with caution:

- *Harsh Critic's claim that "The paper's narrative arc relies heavily on comparing how different models leverage interaction"* — While cross-model comparisons are present, the paper's core structure (benchmark, three-stage framework, within-model experiments, qualitative analysis) does not *rely heavily* on them. The within-model demonstrations stand independently. However, the cross-model comparisons that *are* made remain confounded, so this point was partially demoted from the critic's framing but the core concern (budget confound) is kept as Major.

- *Harsh Critic's speculation that "a paper about X should be evaluated on whether it does X well"* regarding scope creep — Not a specific weakness, just a methodological observation. Removed as non-actionable.

- *Harsh Critic's mention that "the evaluation of the user proxy is under-discussed"* as a separate weakness — This overlaps with the Nice-to-Haves and is already acknowledged in the paper's limitations. Demoted from the weakness list.

- *Strength Finder's claim about "Public release of code and data"* — This is generic and applies to most papers. Moved here as a supporting point that doesn't merit being a formal strength in the evaluation.

## Novel Insights

The most striking finding that emerges across the reviews is the disconnect between information extraction volume and task resolution. Qwen 3 Coder asks the most questions (6.02 avg.) and achieves the highest cosine-distance information gain (0.179), yet its resolve rate improvement from interaction is modest and navigational information actually hurts its performance. Meanwhile, Claude Sonnet 4 asks 50% fewer questions (4.03) with comparable information gain (0.171) and substantially better task outcomes. This reveals that the critical bottleneck is not whether models can ask for information, but whether they can *integrate* that information into their problem-solving—a capability that is not directly measured by question-asking frequency or information-theoretic metrics. The paper's decomposition into detection → clarification → integration is thus well-motivated, and its evidence suggests that integration is the least-addressed capacity in current models.

## Suggestions

1. **Equalize turn budgets** across models (e.g., run all models at 30 and at 100 turns on a representative subset) to enable valid cross-model comparisons, or alternatively, retract cross-model comparative claims and reframe the paper around within-model and qualitative analyses.

2. **Replace causal training claims** with behavioral characterizations. E.g., instead of "current training practices insufficiently optimize for effective integration," say "the observed behavior suggests that current models struggle to integrate interactive feedback, which points to a need for policy-level or evaluation-level interventions."

3. **Reframe RQ2** as measuring "agentic discrimination" or "interaction policy in response to underspecification" rather than purely "detection," and adjust the associated conclusions.

4. **Characterize the 100-issue subset** used for Sonnet 4's Hidden baseline: report difficulty statistics, compare resolved rates on overlapping issues, or at minimum add a caveat about possible magnitude bias.

5. **Add bootstrapped confidence intervals** to the main resolve-rate bar charts (Figure 3).

6. **Add a brief human evaluation** of Ambig-SWE's plausibility (e.g., 50–100 issues rated by 2–3 developers) to strengthen the dataset contribution.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>