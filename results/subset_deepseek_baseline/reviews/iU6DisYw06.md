## Summary

This paper proposes a behavioral evaluation framework for assessing whether LLMs' self-explanations (highlighted tokens) are **functionally consistent** with their own predictive behavior. The authors adapt three metrics—sufficiency, comprehensiveness, and counterfactuality—to a scalar review score \( [1,10] \) instead of probability, avoiding circularity. Experiments on IMDB and Steam reviews with GPT‑4o‑mini, Gemma3:4B, Granite8B, and two DeepSeek‑R1 variants (1.5B, 14B) reveal that GPT‑4o‑mini shows the clearest alignment, while DeepSeek models exhibit systematic contradictions or over‑sensitivity.

## Strengths

*   **Timely and well‑motivated problem**: The paper addresses a critical gap—whether LLMs’ own explanations faithfully reflect their decision processes, going beyond textual plausibility.
*   **Clean behavioral design**: Using interventions on highlighted tokens (remove, isolate, invert) and measuring changes in a scalar review score avoids the circularity of probability‑based faithfulness tests and the opacity of internal activations (especially for proprietary models).
*   **Systematic multi‑model comparison**: Covers both closed‑source and open‑source LLMs across different families and scales, including an intra‑family comparison for DeepSeek. The results highlight that explanation reliability is not guaranteed by scale or openness.
*   **Interpretable metrics**: Sufficiency, comprehensiveness, and counterfactuality are clearly defined and easy to compute, providing a concrete toolkit for future faithfulness evaluations.

## Weaknesses

### Fatal

None.

### Major

*   **Unnatural interventions undermine metric validity**:  
    - **Sufficiency** feeds the model isolated token spans (e.g., `"boring"`), which are often ungrammatical fragments. The model’s score on such degenerate inputs may reflect confusion rather than genuine functional dependence.  
    - **Counterfactuality** uses WordNet antonyms or a simple `"not"` prefix. For context‑dependent sentiment (e.g., `"long"` in a movie review vs. a computer game review), this crude inversion often fails to produce true semantic opposites, so the measured shift may be due to unnatural language rather than genuine polarity change.  
    - **Comprehensiveness** removes tokens, leaving gaps that can make sentences incoherent; the model’s reaction may be an artifact of broken syntax.

*   **Unclear construction of the experimental corpus**:  
    The paper states that 2,000 *sentences* are sampled from IMDB and Steam reviews, but it does not explain how these sentences are extracted from the original multi‑sentence reviews. If full reviews are split into isolated sentences, the sentiment task becomes artificially simple and loses context (e.g., a sentence with mixed sentiment). The stratification by label suggests the original document‑level label was used, but sentence‑level labels may differ. This ambiguity makes it hard to judge whether the results reflect document‑level or sentence‑level behavior.

*   **Label‑flip criterion is undefined**:  
    The metric \(\pi_{\text{alt}}\) counts the proportion of cases where the predicted class changes after intervention. The paper does not specify how the binary sentiment label is derived from the predicted review score (threshold? e.g., score ≤5 → negative?). Without this detail, the label‑flip numbers are uninterpretable and cannot be compared across models or datasets.

*   **Confounded model comparisons**:  
    The paper attributes differences between DeepSeek‑R1 1.5B and 14B primarily to *scale*, but DeepSeek‑R1 is a reasoning model trained with reinforcement learning, not simply a larger version of a base model. The observed differences could reflect RL training choices, not parameter count. Similarly, comparing GPT‑4o‑mini (proprietary, unknown architecture) with open‑source models introduces confounds that are not controlled.

*   **No statistical uncertainty**:  
    All reported metrics are point estimates without confidence intervals, error bars, or significance tests. Given that many differences between models are small (e.g., \(\overline{\Delta R}\) close to 0), the reader cannot judge whether observed patterns are reliable or due to chance.

*   **Reliance on noisy feature extraction**:  
    The entire analysis depends on the model correctly extracting its own “top features.” The paper acknowledges this limitation but does not validate the extracted tokens (e.g., by checking whether they occur verbatim in the input) or quantify how often extraction fails (e.g., model outputs multi‑word spans not appearing in the input). This noise could explain the anomalous DeepSeek results without requiring any failure of functional consistency.

### Minor

*   The term “auto‑consistency” is introduced but only loosely connected to prior self‑consistency literature; a clearer distinction would improve positioning.
*   The metrics aggregate across all sentences, but the paper does not include example‑level analyses showing how the interventions work (or fail) on specific inputs. One example is given for Steam, but it is not annotated with the actual predicted scores.
*   The Appendix is referenced for prompts (not available in the extracted text), so the prompt design—critical for reproducibility—cannot be assessed here.

### Trivial

*   “Formialization” (Section 3.2) is a typo in the extracted text, but likely an OCR artifact; not counted as a paper flaw.

## Nice-to-Haves

*   A human evaluation of the extracted token spans to verify they are indeed the most influential words according to humans.
*   Robustness checks: e.g., repeating experiments with different random seeds or prompt variations.
*   Analysis of how the number of highlighted tokens per sentence affects metric stability.
*   Use of more sophisticated counterfactual generation (e.g., a small language model trained for sentiment‑preserving paraphrasing) to improve validity.

## Novel Insights

None beyond the paper’s own contributions: the empirical documentation that GPT‑4o‑mini exhibits the strongest alignment with expectation across all three metrics, while DeepSeek models show two failure modes (contradiction vs. over‑sensitivity). However, due to the major methodological concerns, these findings should be treated as suggestive rather than conclusive.

## Suggestions

1. **Clarify corpus construction**: Precisely describe how sentences are extracted from reviews and whether the binary label comes from the original review label or a threshold on the model’s score. If full reviews are used, adapt the intervention metrics accordingly.
2. **Validate interventions**: Show that the model’s score on isolated tokens (sufficiency) or on token‑removed sentences (comprehensiveness) is not dominated by artifacts of ungrammatical input. A simple control is to compare against random token subsets of the same size.
3. **Improve counterfactuality**: Use a more principled method for polarity inversion, such as replacing sentiment words with their antonyms from a sentiment‑specific lexicon and verifying via a separate classifier.
4. **Report uncertainty**: Provide bootstrap confidence intervals or standard errors for all aggregated metrics (\(\overline{\Delta R}\), \(\pi_{\text{alt}}\), \(\pi_{\text{red}}\)).
5. **Disentangle model factors**: Add non‑reasoning DeepSeek variants (e.g., DeepSeek‑LLM) to separate the effect of RL training from scale.

## Score and Decision

The core idea—using behavioral interventions to test functional consistency of LLM self‑explanations—is valuable and well motivated. However, the current implementation has several major weaknesses that compromise the validity of the empirical results: unnatural interventions, unclear corpus construction, an undefined label‑flip criterion, confounded model comparisons, and no statistical uncertainty. These issues are not fatal (the framework itself is still sound in principle), but they prevent the paper from making a reliable empirical claim. A revision that addresses these concerns could significantly strengthen the contribution.

**Score**: 4.5  
**Decision**: Reject  

MY FINAL SCORE: <score>4.5</score>  
MY FINAL DECISION: <decision>Reject</decision>