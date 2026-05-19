- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6
Below is the consolidated review, written by verifying each claim against the paper itself.

---

## Summary

This paper introduces Multi-Method Self-Training (MMST), a procedure that uses one generation method (e.g., code) to produce training data for another method (e.g., chain-of-thought text) and vice versa, with a final-answer correctness filter. Using BLOOM-176B on math word problems (SVAMP, GSM8K, MAWPS, MathQA), the authors show that MMST improves both the weaker method (text CoT) and the stronger method (code generation), and also transfers to two out-of-domain reasoning datasets (StrategyQA, CommonSenseQA). Ablation studies isolate the benefit of multi-method diversity from the confound of larger data quantity.

---

## Strengths

1. **Improves the weaker method, making it practically usable.** Table 1 shows that MMST raises chain-of-thought text accuracy from 70.0% (raw BLOOM) to 100.0% on MAWPS, and from 28.6% to 52.2% on SVAMP. These are large absolute gains that substantially close the gap with the stronger code method.

2. **Improves the stronger method using data from the weaker method.** Table 2 reports that code-generation accuracy on SVAMP increases from 53.4% (raw BLOOM) to 85.6% with MMST, and on GSM8K from 32.5% to 52.6%. This is the paper's most surprising result: text pseudo-labels improve code, even though code was already the better method.

3. **Out-of-domain transfer is demonstrated.** Table 5 shows MMST improves text accuracy on CommonSenseQA from 49.3% to 59.6% and on StrategyQA from 61.3% to 68.2%, despite training only on math problems. This suggests the method improves general rationale-generation ability.

4. **Data-quantity ablation convincingly isolates the multi-method benefit.** Table 3 shows that even when the total training examples are capped to match single-method self-training, MMST still outperforms ST (e.g., SVAMP text: 45.3% vs. 40.1%; SVAMP code: 81.1% vs. 80.2%). This directly rules out the trivial explanation that MMST works simply by providing more data.

5. **Anti-correlation between methods is quantified and provides a plausible mechanism.** Table 4 reports negative correlations between which problems text and code each solve correctly (e.g., −0.437 on SVAMP, −0.552 on GSM8K among positive pseudo-labels), supporting the intuition that the two methods succeed on complementary subsets of problems.

---

## Weaknesses

### Fatal
None.

### Major

1. **The translation step is critically underspecified.** The core mechanism of MMST is converting a correct solution from one method into a training example for another method. The method section devotes exactly one sentence to this: "the training examples are used to train all m methods by using the LLM to translate them from the original method used to produce the pseudo-label into the method being trained" (Section 3). No prompt format, no example, no specification of what a "translated" code solution looks like when derived from a text rationale, or vice versa. This is not a minor implementation detail — the entire pipeline hinges on this step. Without it, the method cannot be reproduced or assessed for potential confounds (e.g., could the translation prompt itself be introducing information beyond the raw pseudo-label?). The paper acknowledges in limitations that "LLMs can easily convert text to code and vice versa" but provides no evidence or procedure for this conversion.

2. **The human evaluation compares against the wrong baseline.** Figure 2 shows annotator preferences for MMST over *unfine-tuned BLOOM*. This does not support the paper's claim that "MMST improved not only the correctness of the model, but also the quality of the explanations." The appropriate comparator is single-method self-training (ST), because the question is whether *multi-method* training adds value beyond *single-method* self-training for explanation quality. A preference for MMST over raw BLOOM could simply reflect that any fine-tuning improves output quality. This undermines one of the paper's more interesting claims about explanation quality.

### Minor

1. **The value of *k* (number of generated solutions per problem) is not reported.** The experimental setup states "We generate *k* solutions for each problem" but never specifies *k*. This is a minor but easily fixable omission that affects reproducibility.

2. **The anti-correlation analysis is post-hoc and rests on limited evidence.** The paper observes that datasets with more negative correlations tend to see larger MMST improvements, with MathQA as an exception. This is a correlational observation on four data points, one of which is an exception. The theoretical discussion using Jensen's inequality and convex aggregation functions is speculative and not directly tested. The paper does acknowledge this honestly ("More research would be required to determine the precise cause"), which lessens the concern.

3. **The scope of claims in the abstract slightly exceeds the evidence.** The abstract states "the wide applicability of our method" but the evaluation is on one model (BLOOM-176B) and one task family (math reasoning, plus two related reasoning tasks for transfer). The limitations section appropriately calls the paper an "existence proof," but the abstract's framing is broader than justified. This is a presentation issue, not a scientific one.

### Trivial

None.

---

## Nice-to-Haves

- An error analysis on the training data (e.g., how often does a correct answer arise from an incorrect rationale/code snippet?) would strengthen the paper and address a known weakness of correctness-based filtering.
- Concrete examples of problems where only one method succeeded, paired with examples showing MMST learned to solve them via the other method, would move the anti-correlation analysis from correlational to mechanistic evidence.

---

## Removed Points

These points were raised in the original reviews but are removed for the reasons stated. Treat them with caution if encountered elsewhere.

- *"The paper does not compare against other self-training methods that use execution-based filtering (e.g., STaR)."* — **Removed (factually incorrect).** The paper's single-method self-training (ST) baseline IS STaR: it generates solutions via chain-of-thought, filters by answer correctness, and fine-tunes. The paper explicitly cites Zelikman et al. (STaR) as related work and its ST baseline uses the same mechanism. The comparison is present.
- *"Missing related works on using different decoding strategies or prompts as 'views'."* — **Removed (rule: do not mention missing related works, as external sources cannot confirm their existence).**
- *"The translation details may be in the appendix."* — **Removed (rule: parser strips appendices; they exist in the original submission).** However, the main-paper underspecification is retained as a Major weakness because the method description in the main text is genuinely insufficient for a core procedural step.
- *"The correlation analysis should have concrete examples of problems where only one method succeeded."* — Demoted from a weakness to a Nice-to-Have (it would strengthen the paper but the paper already provides quantitative correlation data).

---

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface an angle not already present in the paper.

---

## Suggestions

1. **Specify the translation step in full detail.** Provide the exact prompt templates used to convert a text rationale to a code solution and a code solution to a text rationale. Include at least one worked example. This is necessary for reproducibility and for readers to assess whether the translation could be introducing information beyond the raw pseudo-label.
2. **Replace the human evaluation baseline** with a comparison between MMST text and single-method self-training text, to isolate the effect of multi-method training on output quality.
3. **Report the value of *k*** used for solution generation.
4. **Scope the abstract's claims** more carefully to reflect the single-model, single-task-family evaluation (or keep the broader language but add a qualifier like "as an existence proof").

---
