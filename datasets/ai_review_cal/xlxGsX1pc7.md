- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5
Now I have a thorough understanding of the paper and can verify the reviewer claims directly against the text.

## Summary

U-MATH introduces a novel benchmark of 1,100 unpublished university-level math problems (20% visual) sourced from real coursework, along with μ-MATH, a meta-evaluation dataset of 1,084 labeled LLM-generated solutions for studying judge reliability. The paper evaluates ~20 models, finding the best achieves 63.4% on text and 45.0% on visual problems, while the best judge (Gemini 1.5 Pro) attains only 80.7% F1 on μ-MATH.

## Strengths

1. **Unique and well-positioned benchmark composition.** U-MATH is the only benchmark that is 100% university-level, has 1,100 samples (enabling statistical robustness), is 20% visual, and is 100% free-form answer. Table 1 clearly shows how it fills gaps left by 12 existing benchmarks (e.g., OCWCourses: 272 samples, 0% visual; MathOdyssey: 387 samples, 26% university-level; ProofNet: 371 samples).

2. **First university-level meta-evaluation dataset.** μ-MATH provides 1,084 labeled solutions from 271 unseen problems, enabling systematic assessment of LLM-as-judge on advanced mathematics. Prior meta-evaluation datasets (MR-GSM8K, MR-MATH) are based on school-level problems. The finding that the best judge achieves only 80.7% macro F1 (Table 4) is an important empirical result that quantifies the gap in evaluation reliability.

3. **Comprehensive model evaluation across subjects and modalities.** The paper evaluates 18 models with per-subject breakdowns (Table 2), revealing meaningful trends: model size vs. specialization trade-offs, the large gap in visual reasoning, and that math-specialized open-source models (Qwen2.5-Math-72B) can approach proprietary ones on text.

4. **Systematic analysis of judge bias and prompting effects.** The meta-evaluation (Section 4.2, Table 4, Figure 2) goes beyond simple accuracy reporting. It examines bias toward specific solution generators (Llama solutions easier to judge than Qwen solutions), quantifies how manual CoT prompting reduces bias compared to AutoCoT, and demonstrates that being a better solver does not imply being a better judge.

## Weaknesses

### Fatal
None.

### Major

- **U-MATH accuracy numbers are reported without uncertainty quantification, despite depending on an imperfect judge with ~20% error rate.** The primary metric uses GPT-4o as judge, which achieves only 77.4% F1 on μ-MATH (Table 4). The authors acknowledge judge limitations in prose (Section 5: "reliance on LLMs for evaluation introduces potential [bias]") but do not propagate this uncertainty into the reported accuracies. No confidence intervals, error bars in Figure 2, or sensitivity analysis showing how rankings would shift under different judges are provided. Since the paper has μ-MATH data characterizing judge errors, it could at minimum estimate plausible ranges. This does not invalidate the benchmark (it can be re-evaluated), but it weakens the evidential weight of the model comparison as presented.

### Minor

- **The choice of GPT-4o as the primary judge over the empirically better Gemini 1.5 Pro (80.7% vs. 77.4% F1) is justified but the justification could be stronger.** The paper states GPT-4o is "more conservative in terms of false positive rate" and "widely available." However, a single-judge reporting with no alternative column or sensitivity analysis gives a false sense of precision. The authors could report accuracy ranges under multiple judges to show robustness.

- **The filtering process shares a model with the evaluation set.** The problem selection uses LLaMA-3.1-8B among five small models (line 170), and the same LLaMA-3.1-8B appears in the evaluated models. While the authors claim averaging across five models prevents overfitting, this is a methodological gap worth discussing explicitly—especially since LLaMA-3.1-8B is the exact same model, not just a related variant.

- **The μ-MATH selection criterion "assessment difficulty" (line 208) is not defined.** The paper says 271 problems were selected "based on their assessment difficulty" but does not specify whether this was expert judgment, model-based, or how difficulty was operationalized. Since μ-MATH is a central contribution, this omission weakens reproducibility.

### Trivial

- Line 174 reports 4.3% of problems were categorized as school-level but does not state whether those problems were removed from the benchmark or retained. The ambiguity is minor but should be clarified.

## Nice-to-Haves

- Report U-MATH accuracy using the best-performing judge (Gemini 1.5 Pro) as an additional column in Table 2 to bound the effect of judge choice.
- Provide a sensitivity analysis: compute accuracy for a few diverse models under multiple judges and report the range.
- The μ-MATH selection methodology ("assessment difficulty") should be precisely defined.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticisms about missing prompts/reproducibility details (e.g., exact CoT prompt text, extractor prompt).** The paper clearly states it uses CoT prompting and a fixed extractor. Prompts are standard content for appendix, which is stripped by the parser. Per policy, appendix-deferred content is not a valid weakness.
- **Criticism about the GitHub repository being anonymized for review.** This is standard double-blind practice and does not affect the paper's validity.
- **"The abstract does not hint at the uncertainty in the U-MATH accuracy numbers."** Abstracts do not typically discuss methodological uncertainty in this level of detail.
- **Criticism that "the model results could be improved with self-consistency."** Temperature 0 single-generation evaluation is the standard in this literature; requesting self-consistency is scope creep.
- **Criticism that the paper "never directly quantifies how much the U-MATH rankings would change if a different judge were used."** This is a suggestion, not a demonstrated flaw. It is properly moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The synthesis of reviews does not reveal any interpretation that the paper itself misses.

## Suggestions

- Add a column to Table 2 reporting U-MATH accuracy evaluated by Gemini 1.5 Pro (the best judge from μ-MATH) to bound the sensitivity to judge choice.
- Explicitly state whether the 4.3% school-level problems identified during expert validation were retained or removed.
- Define "assessment difficulty" for the μ-MATH selection procedure (line 208).
