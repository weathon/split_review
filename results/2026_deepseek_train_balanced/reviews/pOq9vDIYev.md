## Summary

This paper proposes Diverse Preference Learning (DPL), which decouples the entropy and cross-entropy terms in the KL divergence regularizer used in DPO/RLHF. This allows independent control over generation diversity during alignment without the rapid quality degradation that occurs with inference-time temperature scaling. The method is evaluated on diversity-quality tradeoffs (HH-RLHF), best-of-N math problem-solving (GSM8K, MATH), and logit calibration (TruthfulQA, MMLU), showing that DPL Pareto-dominates DPO with standard temperature scaling across diversity and quality metrics.

## Strengths

- **Multi-faceted diversity evaluation with complementary metrics**: The paper measures diversity via three distinct, complementary metrics — embedding cosine similarity, logical disagreement scores, and content diversity ratings via an LLM judge (Section 4.1, line 44) — going beyond the single-metric approach common in prior diversity studies (Kirk et al., 2024; Tevet & Berant, 2021).

- **Pareto-frontier comparison against multiple sampling baselines**: Figure 2 (lines 40, 46–48) constructs explicit diversity-quality Pareto curves contrasting DPL against DPO with token-level temperature scaling, min-p, top-p, and top-k sampling — all with hyperparameter ranges justified by prior recommendations. The claim that DPL Pareto-dominates DPO with standard temperature scaling across all nine metrics is a concrete, falsifiable benchmark.

- **Difficulty-stratified best-of-N analysis reveals nuanced results**: In Section 4.2 (lines 54–55), the paper breaks down GSM8K and MATH results by difficulty, showing that DPL's advantage concentrates on hard problems where diverse solution strategies matter, while standard DPO suffices on easier ones. This honest stratification is more informative than aggregate reporting.

- **Specific, testable claim about nonsensical generation**: The paper asserts that "unlike token-level temperature scaling, DPL never results in predominantly nonsensical generations, even at very high global temperatures" (line 49) — a strong, empirically falsifiable differentiator that addresses a practical failure mode of existing approaches.

- **Calibration improvements demonstrated across two benchmarks**: Section 4.3 (lines 67–71) shows that DPL models achieve lower Expected Calibration Error (ECE) and Brier Score on TruthfulQA and MMLU while maintaining or slightly improving accuracy, addressing the known tension where alignment often hurts calibration.

## Weaknesses

### Fatal
None.

### Major

- **Central framing claim about societal viewpoint diversity is never evaluated.** The abstract claims DPL models "are capable of representing a wider range of societal viewpoints," the conclusion asserts they "can proportionately represent a wider range of societal viewpoints" (line 83), and the introduction motivates the paper with an income inequality example about representing minority political views (lines 12–18). Yet **none of the experiments evaluate representation of societal viewpoints, political diversity, or minority-opinion faithfulness**. The diversity metrics (Section 4.1) measure generic semantic diversity, logical disagreement, and content diversity on the HH-RLHF chat dataset; the other experiments use math problems and MCQ benchmarks. The paper makes a strong societal-impact claim that its evidence does not support, creating a significant gap between framing and evaluation. This can be fixed by either adding appropriate evaluation (e.g., using political survey datasets such as Kirk et al. 2024, which the paper already cites) or removing/qualifying the claim.

### Minor

- **No variance or statistical significance reported.** Across all three experiments (diversity-quality tradeoffs, best-of-N, calibration), the paper reports single values without confidence intervals, standard errors, or statistical tests. Given the experimental scale (500 inputs × 16 responses for diversity; 200 problems × 128 samples for math; two MCQ datasets), there is sufficient data to compute meaningful intervals. This makes it impossible to assess whether observed differences are meaningful. The joint claim that "DPL models with global temperatures slightly greater than 1 consistently attain both higher accuracy and lower calibration error" (line 71) is the sort of claim that requires confidence intervals or paired tests to support.

- **The same LLM judge (gpt-4o-mini) is used for both quality and diversity metrics.** The judge evaluates Arena-Hard quality (win-rate assessment, line 37) and also evaluates logical disagreement and content diversity (line 44). Using the same judge for both axes of the Pareto curve risks confounding the judge's biases with the measured quantities — any systematic preference of gpt-4o-mini could affect both the "quality" and "diversity" measurements in correlated ways.

- **GSM8K difficulty categorization is model-dependent.** The paper defines difficulty levels for GSM8K based on how many samples Mistral-Instruct-7B needs to solve each problem (line 54: "easy if they take 4 or fewer samples to solve, medium if they take 5-64 samples, hard if they take more than 64"). This creates a circular dependency: the difficulty labels depend on the specific model being evaluated, making them non-portable and potentially conflating model capability with inherent problem difficulty.

- **Missing training-time baseline: DPO with varied β.** The comparison is exclusively against DPO with inference-time sampling strategies (temperature, min-p, top-p, top-k). Since DPL is a training-time intervention, the most natural training-time baseline is DPO trained with different β values (which also changes the effective KL strength). The paper fixes β=0.1 throughout; including varied-β DPO would clarify whether the paper's mechanism (decoupling entropy from cross-entropy) matters beyond simply having a different effective KL weight.

### Trivial

- **Inconsistent claim about "four experimental settings."** Line 29 says "we consider four experimental settings" but enumerates only three (4.1, 4.2, 4.3). This appears to be either a miscount or a reference to a fourth setting that was in the stripped sections.

## Nice-to-Haves

- Report the actual numerical values behind the Pareto curves in a table, so readers can verify the claimed Pareto dominance and assess the magnitude of improvements.
- Add a societal/political viewpoint diversity evaluation to directly test the paper's motivating example, using datasets such as those from Kirk et al. (2024).
- Provide qualitative examples of DPL vs. DPO outputs to help readers understand what "increased diversity" looks like in practice.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the paper that the paper itself does not articulate.

## Suggestions

1. **Align framing with evidence.** Either add experiments that directly test societal viewpoint diversity (the paper's motivating use case) or explicitly qualify the scope of claims about representing societal perspectives. The technical contribution (improving diversity-quality tradeoffs) stands on its own without the broader societal claim.
2. **Add error bars and significance tests** to all reported metrics to help distinguish signal from noise, especially for the joint accuracy-calibration claim.
3. **Include DPO with varied β** as a training-time baseline to isolate the effect of the entropy/cross-entropy decoupling mechanism.
4. **Use distinct judges** (or different evaluation protocols) for quality and diversity metrics to avoid confounding.
5. **Fix the "four experimental settings" claim** if it is an error, or clarify the fourth setting.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>