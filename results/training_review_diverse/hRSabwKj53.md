Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the consolidated final review.

---

## Summary

This paper introduces **ReDial**, a human-annotated parallel benchmark of ~1,200 Standard English–AAVE prompt pairs spanning algorithm, math, logic, and comprehensive reasoning tasks. Using this benchmark, the authors evaluate 10 LLMs and find that virtually all models suffer statistically significant performance drops on AAVE prompts — even when the prompts are semantically identical to their Standard English counterparts. The paper further investigates why this gap exists (data skewness only partly explains it; perplexity-matched typo noise hurts less than AAVE for large models) and whether simple fixes like standardization prompting close it (they do not, and they increase cost). The primary contribution is the dataset and the robustly supported finding that LLMs are unfair and brittle to dialect in reasoning tasks.

## Strengths

1. **First end-to-end human-annotated AAVE–Standard English reasoning benchmark.** ReDial fills a concrete gap: prior dialect benchmarks relied on rule-based transformations or LLM translation (which may embed the very biases under study). The authors hire AAVE speakers (including CS experts for algorithm tasks) and conduct multi-round cross-validation for both naturalness and correctness (Section 2, Figure 2). This yields a more authentic and reliable testbed than prior work.

2. **Comprehensive, well-controlled evidence of LLM unfairness to AAVE in reasoning.** The paper tests 10 LLMs (GPT-4o, GPT-4, GPT-3.5-turbo, LLaMA-3/3.1, Mistral/Mixtral, Phi-3) across two prompting settings (zero-shot and CoT). All models except LLaMA-3-8B show statistically significant drops (McNemar's test with Holm-Bonferroni correction, Table 1). GPT-4o drops 0.116 in zero-shot; most models fall below 0.6 pass rate on AAVE even with CoT. This core finding is robustly supported.

3. **The perplexity-matching experiment shows data skewness is not the full story.** Section 5.1 adds character-level typos to Standard English until perplexity exceeds that of AAVE, then compares performance. For LLaMA-3.1-70B and Phi-3-Medium, performance on AAVE is worse than on higher-perplexity noisy text — meaning the model is *more familiar* with AAVE (lower perplexity) yet performs worse on it. This suggests that naive data augmentation alone may not close the gap, an insight not shown in prior robustness work.

4. **Standardization prompting fails to close the gap and increases cost.** Section 5.2 shows that instructing models to rephrase AAVE into Standard English before answering improves performance but still leaves a gap relative to vanilla Standard English performance, while increasing token counts (Figure 5). This demonstrates that the problem is not trivially fixable by prompting and that dialect users may pay more (in tokens) for inferior service.

5. **Evaluation methodology is sound for the primary claims.** Temperature zero, consistent pass/fail metrics across tasks, and per-model McNemar's tests with multiple-comparison correction (Table 1) make the central finding reliable. The model selection spans proprietary and open-source families, small to large scales, and varied training paradigms.

6. **Qualitative error analysis provides concrete failure modes.** Section 5.3 identifies three patterns (wrong question rephrasing, distraction by irrelevant info, failure to execute all steps) with specific examples from GPT-4o on math, giving insight into *why* the gap persists even after standardization.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contribution — the ReDial dataset and the finding that LLMs show significant performance drops on AAVE reasoning prompts — is robustly supported. The issues below are important to address but do not threaten the paper's central claims.

### Minor

1. **Table 2's statistical testing is underspecified.** The caption reports "pass rates by task averaged across responses from all models" with significance from "McNemar's tests applied to AAVE and Standardized English." It is unclear how McNemar's test — which requires paired binary data from a single model — was applied to data aggregated across models. If model–instance pairs were pooled, this inflates sample size and violates the pairing assumption; if per-model tests were run and aggregated, that should be stated. The per-task claim ("all reasoning tasks are brittle to AAVE") is consistent with Table 1's per-model results, so the overall conclusion stands, but the ambiguity should be clarified. The authors should report per-model per-task breakdowns or clarify the aggregation method.

2. **Floor effect confounds the scaling argument for LLaMA-3-8B vs. LLaMA-3-70B.** The paper argues "scaling does not make models more robust" by noting that LLaMA-3-8B's delta (0.009, non-significant) is smaller than LLaMA-3-70B's (0.066, significant). However, LLaMA-3-8B's Standard English pass rate (0.489) is near chance — there is little room to drop further, making absolute delta comparisons misleading. The broader scaling claim is also supported by other evidence (Phi-3 models show inconsistent patterns; Mixtral-8x7B drops more than Mistral-7B), so this does not invalidate the argument, but the floor effect should be acknowledged and relative drops reported alongside absolute ones.

3. **The perplexity-matching experiment supports a nuanced conclusion that the paper mostly gets right, but the "data augmentation might not help" framing could be tempered.** The paper's actual language is hedged ("does not explain the whole picture," "naively... may not diminish"), which is appropriate. However, two subtle gaps remain: (a) perplexity reflects unconditional token probability and may not capture whether the model has learned *systematic* associations with AAVE features (e.g., linking dialect features to informal contexts where reasoning is less reliable); (b) the result for Phi-3-Mini goes in the opposite direction (better on AAVE than on matched-perplexity noise), acknowledged by the authors but not fully discussed. The overall claim is defensible, but a slightly more explicit caveat about what the experiment *cannot* isolate would strengthen the paper.

4. **No inter-annotator agreement metric for the AAVE rewrites.** The paper describes cross-validation between annotators (Section 2.2) but does not report a quantitative measure like Cohen's kappa or percentage agreement on naturalness or correctness. While the multi-round validation pipeline is thorough, a formal agreement metric would strengthen confidence in the dataset's consistency.

### Trivial

- The typo perturbation experiment (Section 5.1) should clarify whether perturbations were applied to the full prompt (task instructions + query) or just the query portion. The description says "Standardized ReDial," which is the full prompt, but explicit confirmation would help reproducibility.
- LLaMA-3.1-8B is not tested, which would have made the LLaMA-3 vs. 3.1 scaling comparison cleaner (noted by the critic; the paper acknowledges this indirectly by omission).

## Nice-to-Haves

- **Report relative (percentage) performance drops** alongside absolute deltas, especially for the scaling comparison where baseline performances differ substantially.
- **Per-model per-task breakdowns** (as a heatmap or supplementary table) would make the per-task analysis more transparent than the current aggregated Table 2.
- **Cost analysis in dollars** for the standardization experiment (GPT-4o and GPT-4 price per token) would strengthen the fairness implication — dialect users pay more for worse service.
- A controlled comparison of AAVE+standardization vs. **Standard+standardization** is already implicit in Figure 5; making the explicit comparison in the text would sharpen the finding that standardization benefits Standard English too (suggesting it acts partly like CoT).
- An ablation separating **lexical vs. syntactic AAVE features** would be interesting but is well outside the paper's scope — this is a natural direction for follow-up work.

## Removed Points

These points were flagged for removal; treat them with caution if referenced elsewhere.

- **Criticism that the perplexity experiment's conclusion is "too strong":** The paper's actual text uses hedging language throughout ("does not explain the whole picture," "may not," "might be"). The claim is appropriately scoped for what the experiment demonstrates. Moved here because it mischaracterizes the paper's actual strength of claim.
- **Criticism about missing LLaMA-3.1-8B as a "cleaner comparison":** The paper already tests multiple model families and the missing model does not undermine any conclusion; this is a minor wishlist item.
- **Criticism that the paper should discuss why standardization improves Standard English:** This is an interesting question but not a weakness — the paper reports the empirical finding, and the effect (standardization prompting acting like additional reasoning steps akin to CoT) is a reasonable speculation that the critic supplies, not something the paper is missing.
- **Criticism that the paper does not ablate lexical vs. syntactic AAVE features:** Scope creep — the paper does not claim to perform this analysis, and requiring it would constitute a different paper.
- **Strength Finder's generic phrasing ("this paper addressed an important problem"):** No such generic strengths were present; all strength-finder entries had specific, citable content.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm what the paper already establishes: the dataset is valuable, the core empirical finding is solid, and the secondary analyses (perplexity experiment, standardization, scaling) are individually suggestive but collectively reinforce the main conclusion rather than adding orthogonal discoveries.

## Suggestions

1. **Clarify the statistical testing methodology for Table 2** (per-model tests followed by aggregation, or some other approach). If the current aggregation is invalid, replace with per-model per-task results (e.g., a supplementary heatmap) or drop the significance claim from the aggregated table and report effect sizes descriptively.
2. **Acknowledge the floor effect** in the LLaMA-3-8B comparison and report relative drops alongside absolute deltas for the scaling discussion.
3. **Add a brief caveat** in Section 5.1 noting that perplexity captures unconditional familiarity but may miss systematic associations between AAVE features and model behavior (e.g., learned correlations with informal contexts).
4. **Report inter-annotator agreement** for the dataset validation (or note its absence as a limitation).

## Score and Decision

**Originality:** High — first human-annotated AAVE reasoning benchmark. **Importance:** High — addresses fairness for a large demographic of dialect speakers. **Claims well-supported:** Mostly yes; the primary claim is robust, secondary analyses have minor gaps. **Soundness:** Good; the core evaluation (Table 1) is properly conducted. **Clarity:** Good, though Table 2's statistical test needs clarification. **Value to community:** High — the dataset enables a line of evaluation that did not previously exist.

The paper's contribution is substantial and the main finding — that LLMs are unfair and brittle to AAVE in reasoning tasks — is well-supported. The weaknesses are concentrated in the secondary analyses and are addressable through clarifications and modest reframing rather than new experiments. This is a clear accept.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>