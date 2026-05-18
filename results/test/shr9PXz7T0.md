Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper identifies and characterizes "selection bias" in LLMs — the tendency to prefer certain option ID tokens (e.g., "A" over "C") when answering multiple-choice questions, regardless of option content. Through experiments with 20 LLMs across three benchmarks, the authors show selection bias is pervasive, cannot be fixed by prompting, and stems primarily from token bias (not position bias). They propose PRIDE, an inference-time debiasing method that estimates the model's prior over option IDs from a small subset of test samples (2–5%) and subtracts it from the prediction distribution, achieving strong debiasing with minimal overhead and demonstrating cross-domain transferability.

## Strengths

1. **Extensive and systematic empirical characterization.** The paper evaluates 20 LLMs from 5 families across 3 benchmarks (MMLU, ARC, CSQA) with both 0-shot and 5-shot settings. Table 1 quantifies the dramatic accuracy swings caused by simply moving golden answers to specific positions (e.g., llama-30B jumps from 53.1 to 68.2 when moved to A), establishing concrete practical stakes. This breadth makes the claim that selection bias is prevalent and varies with model families, not a single-model artifact.

2. **Controlled causal attribution via ablation.** The paper carefully separates token bias from position bias through two complementary ablations: shuffling option IDs (isolating token bias) and removing option IDs (isolating position bias). Table 2 shows that shuffling IDs leaves RStd nearly unchanged (5.5 → 5.1 for gpt-3.5-turbo on MMLU) while removing IDs drops it dramatically (5.5 → 1.0). This provides substantially stronger evidence than prior work (e.g., Pezeshkpour et al., 2023) that conflated the two.

3. **Efficient, interpretable, and transferable debiasing (PRIDE).** The method requires only 2–5% of test samples for prior estimation yet matches or outperforms the ×n-cost Cyclic Permutation baseline in RStd reduction and accuracy improvement (Figure 3). The estimated priors are stable, interpretable (matching the recall imbalance pattern), and transfer across domains (Figure 4). The analysis in Section 4.4 further shows that PRIDE primarily corrects low-confidence predictions where the model is most susceptible to bias, rather than flattening all predictions indiscriminately.

4. **Demonstrated inadequacy of simple fixes.** Table 2 shows that explicit debiasing instructions (RStd=6.1) and Chain-of-Thought prompting (RStd=4.5) fail to substantially reduce selection bias compared to the default (RStd=5.5), validating the need for the proposed inference-time approach rather than prompt engineering.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The "removing-IDs" ablation changes the evaluation task, introducing a confound.** When option IDs are removed, the model must select via likelihood comparison over full option contents rather than by predicting an ID token. While accuracy remains similar, the change in format could systematically affect bias measurement — e.g., length-normalized likelihoods may be less sensitive to certain forms of bias, or the model may adopt a different decision strategy. The paper acknowledges this format change but does not fully address whether it confounds the causal attribution of selection bias to token bias. This does not invalidate the core finding (the ablation evidence is strong even with this caveat), but it weakens the precision of the causal claim. The paper appropriately hedges ("one primary intrinsic cause"), so this is a note for careful interpretation rather than a fatal flaw.

2. **PRIDE's decomposition assumptions are stated but not directly validated.** The derivation assumes conditional independence between the option-ID prior and the content belief, and invariance of the debiased distribution to permutations. These are mathematically convenient and yield tractable estimation, but they are only validated through end-to-end performance (reduced RStd, improved accuracy) and prior stability. A more direct test — e.g., comparing estimated priors against a ground-truth prior from a controlled setting where correct answers are balanced across IDs — would strengthen scientific confidence that the method truly separates the model's "prior" from its "content-based belief" rather than just shifting predictions in a useful way. The method clearly works empirically, but the assumptions' validity is somewhat undersupported.

3. **PRIDE requires a set of test samples for prior estimation, limiting applicability to isolated queries.** The method samples K test samples (e.g., 5%) for permutation-based prior estimation. In scenarios where the model receives a single isolated query or test samples arrive sequentially, PRIDE cannot be directly applied as described. The paper acknowledges an "estimation budget" but does not discuss how to handle the K=0 case or sequential test-time deployment. This is a practical constraint that users should be aware of. (A brief discussion of using a precomputed prior from a calibration set or a default uniform prior as a fallback would strengthen the practical contribution.)

4. **The "Random Perm" baseline (fewer permutations) is mentioned but not evaluated.** Line 394 notes that using 2–3 random permutations could serve as a low-cost alternative, but no results are shown. Since PRIDE is explicitly motivated as a more efficient alternative to permutation-based methods, readers need a direct comparison of RStd and accuracy for, say, 2 random permutations versus PRIDE with α=5%. This missing comparison weakens the efficiency argument somewhat.

5. **No formal limitations section.** The paper touches on limitations (the cross-domain degradation, the estimation budget) in passing but does not synthesize them in one place. Adding a "Limitations" paragraph would improve completeness and help readers calibrate appropriate use of the method.

### Trivial

1. **RStd values reported without confidence intervals or standard errors.** The paper reports averages over 5 runs but does not report standard errors for RStd values across runs or models. For cross-model comparisons, this would help readers assess whether differences in selection bias across models are meaningful.

## Nice-to-Haves

- A controlled experiment where the ground-truth correct answer is randomly distributed across IDs and positions, to directly quantify how much selection bias is removed by a known token prior vs. a position prior.
- A brief discussion of how to handle the isolated-query scenario (e.g., using a calibration-set prior or falling back to a uniform prior), even if a full solution is left to future work.
- Failure-case analysis: when does PRIDE hurt accuracy? The paper notes slight degradation in cross-domain transfer but does not characterize which predictions are most vulnerable to erroneous prior estimation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the shuffling-ID ablation does not eliminate position bias.** This reflects a misunderstanding of the experimental design. When IDs are randomly shuffled, position bias (preference for content at the first position) is distributed across all IDs equally across shuffles, so it does not inflate RStd (which measures ID-level imbalance). The logic of the ablation is sound: shuffling IDs isolates token bias, and the near-unchanged RStd (5.1 vs. 5.5) shows token bias is the dominant factor. The removed-IDs condition (RStd=1.0) then bounds the position-bias contribution. The evidence is clean.
- **Suggestion to test whether the same models exhibit both token and position bias jointly by fixing IDs and shuffling option order.** The paper already addresses this implicitly: the default condition has both biases present, and the ablation results show position bias is "somewhat present but quite irregular" (line 235). The counteraction observed for llama-2 models (line 234) further confirms joint presence.
- **Criticism that the transferability figure's y-axis labels are not fully readable.** This is a formatting/parser artifact; the original figure is assumed to be readable.
- **Request for the derivation to more explicitly state that cyclic permutations satisfy the required property.** The paper already states this on line 315 ("given $\mathcal{I}$ contains either full or cyclic permutations"), which is sufficient.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a controlled experiment directly validating the decomposition assumptions (comparing estimated priors to a ground-truth prior from a balanced-label setting), or at minimum discuss the assumptions' limitations more explicitly.
2. Include the missing "Random Perm" baseline results to directly compare PRIDE's efficiency against the most natural low-cost competitor.
3. Add a "Limitations" paragraph that synthesizes the estimation-budget constraint, cross-domain degradation, and untested assumptions in one place.
4. Report standard errors for RStd values to aid cross-model comparison.
5. Discuss how users could handle isolated-query scenarios (e.g., precomputed calibration-set prior or warm-start strategies).

## Score and Decision

**Originality:** The paper makes a clear empirical contribution by identifying selection bias, providing a more precise causal attribution than prior work, and proposing a practical debiasing method. The finding that token bias dominates position bias is non-trivial and runs counter to common assumptions in the literature.

**Importance of research question:** MCQs are a standard evaluation format for LLMs, and the demonstrated vulnerability to option-position changes (inverting model rankings) has direct implications for how LLM evaluations should be conducted and interpreted.

**Claims support:** The core claims are well-supported by extensive experiments. The causal attribution has a minor confound (task-format change in the removing-IDs ablation), but the overall evidence is strong. The decomposition assumptions are untested but validated end-to-end.

**Soundness of experiments:** Generally sound and thorough. The 20-model, 3-benchmark setup provides solid empirical grounding. The ablation design for separating token/position bias is clever and appropriate.

**Clarity of writing:** Clear and well-structured. The methodology derivation is presented in sufficient detail.

**Value to the community:** High value. The empirical findings should influence how researchers interpret MCQ-based evaluations, and PRIDE provides a practical, low-cost tool for improving robustness.

This is a solid paper with genuine contributions and well-executed experiments. The weaknesses are minor and addressable — they do not undermine the core claims or the practical value of the method.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>