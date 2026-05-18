Now I have thoroughly read and verified the paper content against all reviewer claims. Let me compose the final consolidated review.

---

## Summary

This paper introduces **ReDial**, the first human-annotated parallel benchmark of 1,216 Standard English–AAVE prompt pairs spanning four canonical reasoning tasks (algorithm, math, logic, and comprehensive reasoning). The authors hire AAVE speakers — including those with CS backgrounds for code tasks — to rewrite existing benchmark instances (HumanEval, MBPP, GSM8K, SVAMP, LogicBench, Folio, AsyncHow) while preserving semantics and ground-truth labels. Evaluating 13 LLMs (GPT-4o/4/3.5-turbo, LLaMA-3/3.1, Mistral/Mixtral, Phi-3), they demonstrate statistically significant performance drops on AAVE queries for nearly every model tested, analyze why simple explanations like data skewness do not fully account for the gap, and show that instructing models to rephrase into Standard English before answering does not close the gap while increasing cost.

## Strengths

- **First human-annotated parallel dialect benchmark for reasoning tasks.** The paper fills a clear gap: prior dialect benchmarks (e.g., Multi-QS) do not cover reasoning, and prior AAVE benchmarks rely on rule-based transformations or LLM translation — both of which introduce biases. ReDial is the first dataset of its kind with end-to-end human annotation (§1, §2).

- **Statistically significant performance drops across nearly all tested LLMs.** Table 1 reports rigorous McNemar's tests with Holm–Bonferroni correction. GPT-4o drops from 0.832 to 0.716 pass rate (Δ=0.116) in zero-shot; similar or larger drops appear across GPT-4, GPT-3.5-turbo, LLaMA-3.1-70B, Mixtral, Mistral, and Phi-3 models. Only LLaMA-3-8B-Instruct shows a non-significant drop (§3.2, Table 1).

- **Evidence that AAVE brittleness is not explained by data skewness alone.** Section 4.1 compares AAVE against character-level typos at matched and higher perplexity levels. LLaMA-3.1-70B-Instruct and Phi-3-Medium-128K-Instruct perform *worse* on human-written AAVE than on more-perplexing typo-ridden English. This shows the problem exceeds a simple "unfamiliarity" account — a non-trivial finding that distinguishes dialectal variation from generic noise.

- **Systematic ablation of a natural mitigation strategy.** Section 4.2 tests whether asking models to "rephrase in Standard English first" closes the gap. Even with standardization, AAVE performance does not reach vanilla Standard English levels, and token costs increase (Figure 3). This demonstrates that simple prompting fixes are insufficient.

- **Multi-faceted evaluation:** 13 models across 4 reasoning categories, 2 prompting methods (zero-shot, CoT), with statistical testing and qualitative error analysis.

## Weaknesses

### Fatal
None.

### Major
None. No single weakness invalidates the core contribution — the dataset and the demonstrated unfairness — nor does any weakness undermine the paper's primary claims beyond repair.

### Minor

- **Limited transparency on annotator verification and inter-annotator agreement.** The paper recruits self-identified AAVE speakers and has them cross-check each other's work, but reports no statistics on the number of annotators, their regional/stylistic diversity, or inter-annotator agreement on naturalness or semantic preservation. The Ethics Statement (§7) explicitly acknowledges not collecting annotator personal information and lacking full control over vendor recruitment. While these choices are ethically defensible (privacy protection, avoiding essentialist definitions of dialect), they leave the representativeness of the AAVE in ReDial unquantified. The core unfairness finding is likely robust to this variation, but it weakens the "high-quality" characterization of the dataset. *This is a real limitation, openly acknowledged by the authors, but they could partially address it by computing agreement metrics on a subset of doubly-annotated items.

- **The perplexity-matching experiment (typo vs. AAVE comparison) conflates qualitatively different kinds of deviation.** Character-level typos (replace/delete/add characters) introduce token-level noise that an LLM can often recover from via shallow spelling correction, whereas AAVE involves rule-governed morphosyntactic and lexical shifts (copula deletion, habitual "be," etc.) that engage deeper linguistic processing. The finding that AAVE causes more brittleness than higher-perplexity typos is genuinely informative — it *does* show that data skewness alone is not the whole story. However, the paper's claim that this "means that naive data augmentation might not solve the problem" is appropriately hedged with "may not" (line 260), but could be sharpened by directly testing a simple augmentation strategy or by including a more linguistically-motivated control (e.g., synonym substitution, word-order scrambling). The current experiment is suggestive but does not directly test augmentation.

- **The "comprehensive reasoning" (AsyncHow) category's compositionality claim is not directly demonstrated.** The paper observes that AsyncHow has the lowest absolute pass rates and the largest relative drop under AAVE, and states that "LLMs face further difficulty when they are asked in a dialect to compose different skills" (§3.2). This is a plausible observation, but the paper does not control for confounds: AsyncHow is harder in Standard English to begin with (0.191 zero-shot), and the AAVE annotations for this specific dataset may introduce more ambiguity due to its complex structure. A per-category annotation validation pass rate table would clarify whether AsyncHow annotations are of comparable quality to other categories. The claim about compositionality interacting with dialect is interesting but remains speculative without a controlled comparison (e.g., compositional vs. non-compositional versions of the same content).

- **The "scaling widens the gap" claim lacks a formal statistical test.** The paper compares the LLaMA-3-8B drop (Δ=0.009, not significant) to the LLaMA-3-70B drop (Δ=0.066, significant) and concludes scaling widens the gap. The paper correctly notes the 8B drop is not significant, so the claim that scaling "does not close the gap" is supported, but the claim that scaling "widens" it would require a formal interaction test (model size × dialect). This is a small presentation issue but worth correcting.

### Trivial

- The paper does not report whether AAVE prompts differ in average token length from their Standard English counterparts. While temperature 0 and generous max-token limits likely make this irrelevant, reporting it would cleanly rule out length effects.
- Table 4 reports per-category averages, but per-dataset breakdowns within logic (binary LogicBench vs. multi-choice LogicBench vs. Folio) would give a finer-grained picture of where the AAVE gap concentrates.

## Nice-to-Haves

- Reporting chance-adjusted metrics (e.g., Cohen's kappa or normalized accuracy) for logic tasks where binary classification has a 0.5 random baseline would clarify whether the AAVE drop exceeds what random guessing would produce.
- Providing inter-annotator agreement statistics on a subset of doubly-annotated items would strengthen confidence in ReDial.
- Including an additional control in the perplexity experiment (e.g., synonym substitution or word-order scrambling) would make the comparison more linguistically grounded.
- A per-category breakdown of annotation validation pass rates would address the AsyncHow concern directly.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The standardization experiment overstates the gap reduction because the prompt also helps Standard English."** — The paper already notes this effect (§4.2: "standardization improves model performance even when the prompt input is already in Standard English"). The reviewer agrees the paper's conclusion that "standardization does not close the gap" is still valid. This is not a weakness.

2. **"Qualitative error patterns may be due to content changes introduced by rewriting, not dialect features."** — The comparison is between AAVE (with standardization) and the *same content* in Standard English. The lexical choices in the AAVE version *are* the dialectal features under study. The argument presupposes an artificial split between "dialect grammar" and "dialect lexis" that would negate the object of study. The examples given (e.g., "crazy silly school series") are natural AAVE lexical choices — they are not annotation artifacts.

3. **"Missing related works" and "missing appendix" complaints** — The parser strips appendices and some references; these exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews identify useful clarification points and suggest strengthening existing analyses, but do not surface a genuinely novel observation about the paper's findings that the authors missed.

## Suggestions

1. **Report inter-annotator agreement or annotation consistency metrics** on a small doubly-annotated subset (even 50–100 items) to quantify the natural variability in AAVE rewriting and give readers a concrete sense of reliability.
2. **Provide a per-category validation pass rate table** showing how many items from each source dataset passed/failed each stage of the quality pipeline, especially for AsyncHow.
3. **Add a formal interaction test** (model size × dialect) before claiming scaling "widens" the gap, or hedge to "does not close" as the paper already does for the core claim.
4. **Tone down the data augmentation speculation** slightly: the evidence shows data skewness does not explain the *whole* picture, which is a well-supported claim. The stronger inference that augmentation "might not help" is reasonable but speculative — explicitly flag it as such.
5. **Report average token lengths** for Standard English vs. AAVE prompts to rule out simple length effects.

## Score and Decision

**Originality:** High — ReDial is the first human-annotated parallel AAVE reasoning benchmark.  
**Importance of research question:** High — dialect fairness in LLMs is a timely and socially relevant problem.  
**Claims support:** Good — core claims are well-supported by statistical tests and multiple models. Secondary/interpretive claims (data augmentation, compositionality) are appropriately hedged but could be tightened.  
**Soundness of experiments:** Solid — multi-model, multi-task evaluation with proper statistical testing. Some secondary analyses could be deeper.  
**Clarity:** Good — the paper is well-structured and clearly written.  
**Value to the community:** High — ReDial provides a reusable benchmark and the findings document a real, consequential unfairness.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>