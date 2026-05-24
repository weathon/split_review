Now I have enough information. Let me produce the final consolidated review.

## Summary

This paper investigates length volatility in long-form LLM generation through three stages: benchmarking, probing, and mitigation. It introduces VOLTBench, a benchmark designed to quantify output length volatility across multiple generations; presents an attention-trace analysis identifying patterns (Attention Collapse and Attention Instability) associated with volatile generation; and proposes SELB, a training-free, logit-boosting decoding method that enforces structural adherence and suppresses failure modes. Experiments across multiple models and tasks show that SELB substantially improves length accuracy and reduces volatility.

## Strengths

- **First benchmark to systematically measure length volatility across multiple generations:** VOLTBench (Section 3, Table 1) is the only benchmark among those compared that includes both multiple sampling and stability evaluation. This fills a genuine gap, as prior benchmarks evaluate single-generation quality only, overlooking the significant inter-run variation that the paper documents (e.g., LongWriter-8B's standard deviation reaching 103% of its mean output).

- **Training-free, lightweight decoding method with strong empirical results:** SELB (Section 6, Eqs. 2–3) requires no additional training and operates via simple logit manipulation. On the 100-section structured task, compared to LongWriter-8B, it improves Mean Length Accuracy from 31.6% to 78.25% and reduces the Length Variation Coefficient from 45.4% to 14.02%. Figure 5 shows that SELB applied to Qwen2.5-7B, Qwen3-8B, and Llama-3.1-8B produces outputs that closely track the target length reference line, while baselines degrade markedly.

- **Generalization to free-form generation is demonstrated:** Section 6.4 adapts SELB to a hybrid strategy for unstructured tasks (20,000-word novel writing), achieving 97% Mean Length Accuracy and 12.1% LVC, where baselines like GPT-4o-mini and LongWriter-8B collapse to under 600 words.

- **Fine-grained constraint analysis reveals systematic failures at scale:** Section 4.3.1 evaluates models on three types of localized constraints across varying lengths, showing that even the best models collapse after 100 sections — no model delivers more than 40 correct constraints at the 500-section setting. This provides concrete evidence of the severity of instruction-following degradation in long-form generation.

- **Diverse evaluation with multiple models and tasks:** The benchmark covers unstructured (story, dialogue, diary) and structured (code, math) tasks, across English/Chinese and multiple complexity levels. Nine models are evaluated, including reasoning models, SSM architectures, and models specifically fine-tuned for long generation.

## Weaknesses

### Fatal
None.

### Major

- **Headline performance claims (148% length increase, 69% volatility reduction) are presented in a confusing and potentially misleading way.** The abstract and conclusion state that SELB "improves the mean output length of the base model by 148% and reduces the length volatility by 69%." However, Section 6.3 reports these improvements relative to LongWriter-8B — a *different* model, not the base model that SELB is applied to. The paper does not specify which base model SELB is applied to when producing these numbers, and the quantitative claims are never tabulated alongside the same-base-model baselines. For example, Qwen2.5-7B without SELB produces 445 words (Table 2), while SELB on Qwen2.5-7B reportedly produces 15,651 words — a 3417% increase, not 148%. Although Figure 5 provides a visual comparison, the textual presentation conflates "improvement over the same model" with "improvement relative to a different strong baseline," which undermines the interpretability of the headline claims. *(Verified: Section 6.3 compares to LongWriter-8B; abstract says "the base model"; no table gives SELB vs. its own base model.)*

- **SELB is not directly compared to standard decoding strategies on the same base model in a unified table.** Table 2 lists Repetition Penalty, Entropy-Stopping, Length Constraint, and Lookahead Decoding applied to Qwen2.5-7B, but SELB results are discussed only in prose (Section 6.3) and shown visually in Figure 5. This makes it impossible for a reader to compare SELB against these baselines on identical metrics at a glance. Notably, Lookahead Decoding achieves LVC 9.3% vs. SELB's 14.02% on Qwen2.5-7B, yet the paper does not discuss this trade-off or explain why SELB is preferable despite higher relative volatility. *(Verified: Table 2 contains baselines on Qwen2.5-7B; Section 6.3 and Figure 5 contain SELB results; no single table merges them.)*

### Minor

- **Volatility metrics are based on only 5 runs per instruction (N=5).** Section 3.2 explicitly sets N=5. For heavy-tailed output length distributions (as Figure 1 shows for LongWriter-8B), sample standard deviations from N=5 are noisy. The paper does not provide confidence intervals, bootstrap estimates, or any stability analysis for the reported LSD/LVC values. While 5 runs is a common practical choice, for a paper that *centrally* measures volatility, the sensitivity to sample size should be addressed. *(Verified: Section 3.2, line 166.)*

- **Attention-trace analysis remains qualitative, with only two illustrative examples.** Section 5 introduces the concepts of Attention Collapse and Attention Instability based on visual inspection of attention traces from two models (Qwen2.5-7B, Qwen2.5-3B) on one task. The paper states that "output volatility is not random but closely linked to and preceded by measurable failures in the model's internal attention dynamics," but provides no quantitative correlation between attention stability metrics (e.g., variance of \bar{α}^{(t)}) and output-length LVC across models, tasks, or repeated trials. The patterns are plausible and motivate SELB, but the evidence is suggestive rather than confirmatory. *(Verified: Section 5, Figure 4, only two examples shown.)*

- **No ablation of SELB's two components.** SELB combines structural enforcement (M_struct) and proactive failure prevention (M_fail), but the paper never evaluates them separately. It is unclear how much each component contributes to the overall improvement, and whether either alone suffices. *(Verified: Section 6 presents M_struct and M_fail but no ablation study.)*

- **No robustness analysis for key hyperparameters.** SELB depends on τ_max (target section length threshold) and β (boosting strength). The paper does not examine sensitivity to these choices, or what happens when the target length estimate is inaccurate. *(Verified: Section 6 defines τ_max and β but no sensitivity analysis.)*

- **Construction of the banned-token set V_banned is not explained.** Section 6.2 defines V_banned as tokens corresponding to "conversational filler phrases (e.g., 'I hope these...')" but does not describe how this set was constructed, whether it is model-specific, or how it transfers to new models. *(Verified: Section 6.2, line 268.)*

### Trivial

- The computational overhead of SELB (e.g., inference time per token vs. standard decoding) is not stated, though logit manipulation is expected to be cheap.
- The paper refers to "Figure 6" in Section 6.3 for SELB results, but the figure in the extracted text appears to be labeled Figure 5. This may be a formatting reference error in the extracted version.

## Nice-to-Haves

- A quantitative correlation analysis linking attention trace metrics (e.g., variance of constraint attention) to output-length volatility across several models and tasks would strengthen the claimed causal link.
- A single summary table showing, for one base model (e.g., Qwen2.5-7B), performance without intervention, with each standard decoding strategy, and with SELB on identical tasks.
- Evaluating SELB with N ≥ 20 on a subset of settings to demonstrate that volatility metrics stabilize.
- Testing sensitivity to τ_max and β choices.

## Removed Points

- **Criticism that "the 148%/69% numbers are presented in a misleading way" (full form):** This is retained as a Major weakness, only the framing is adjusted. The core observation — that the abstract says "base model" while Section 6.3 compares to LongWriter-8B — is factually correct and substantive.

- **Criticism that "Perfect 100% SCA is suspicious — if the method forces output structure, achieving perfect structural accuracy is a near-tautology":** REMOVED. SCA measures correctness of structured content (code/math chapters that pass execution-based verification). Structural enforcement ensures the right *number* of chapters is generated, but content correctness per chapter depends on the model's generation quality. A perfect 100% SCA means the content *within* the enforced structure is also correct, which is meaningful. The criticism conflates structural compliance with content correctness.

- **Criticism about Claude-3.5-Sonnet's low mean length (176 words) calling into question its fairness as a baseline:** The paper *explicitly* excludes Claude-3.5-Sonnet from quality comparisons for this very reason (Section 4.3, line 215). The critic overlooked this.

- **Criticism about missing related work / "first to introduce output volatility" claim needing qualification:** These are removed per the "do not mention missing related works" rule.

- **Criticism about "UCA numbers are limited without Appendix details":** The paper's UCA evaluation follows standard LLM-as-a-judge practice (common in the field) and references the appendix for details. This is standard practice and not a weakness unique to this paper.

- **Several nitpicks about formatting, appendix deferrals, and reproducibility details** are removed per the hard rules.

- **Strength Finder's claim that "Attention trace analysis reveals concrete internal failure patterns":** Downgraded in the strengths section. The analysis is qualitative and suggestive, not "concrete." The strength is retained but rephrased to accurately reflect the evidence level.

- **"Strengthening the Paper on Its Own Terms" section and generic requests for more data:** These are moved to Nice-to-Haves or Suggestions where they remain actionable but do not inflate the weakness count.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs do not surface a genuinely novel observation that the paper itself does not already make.

## Suggestions

1. **Clarify headline numbers:** In a revision, report SELB's improvements relative to the *same base model* (e.g., Qwen2.5-7B without SELB) in a dedicated table alongside comparisons to LongWriter-8B and other baselines. Be explicit in the abstract about which comparison the 148%/69% refers to, or re-frame them relative to the same-model baseline.

2. **Provide a unified comparison table:** Add a single table showing Qwen2.5-7B without intervention, with each standard decoding strategy (Table 2 rows), and with SELB, all on the same 100-section task with identical metrics.

3. **Ablate SELB components:** Report LVC, MLA, SCA, and UCA for M_struct alone, M_fail alone, and the combined method on at least one base model.

4. **Quantify the attention-volatility link:** For 2-3 models across several tasks, compute a summary statistic (e.g., variance of \bar{α}^{(t)}) and correlate with LVC across repeated runs (N=5 or more). If the data support the claimed link, this would substantially strengthen the probing stage.

5. **Boost N or provide confidence intervals:** Either increase N to ≥20 for a subset of settings, or provide bootstrap-derived confidence intervals for the reported LSD/LVC values.

6. **Describe the banned-token set construction** and its model-specificity.

## Score and Decision

**Calibration summary:**

*Round 1 (bracketing):* Weak anchors (score < 3.5): papers at 3.0 about hallucination rejection, uncertainty estimation, lifelong learning evaluation — notably weaker in scope and rigor. Middle anchors (3.5–7.5): papers at 4.0–6.0 including semantic isotropy for factuality (5.0), expert-level long-form benchmark (5.5), rainbow padding for dLLMs (6.0), speculative decoding benchmark (5.0). Strong anchors (>7.5): multi-turn conversation benchmark (8.0), embodied agent benchmark (8.0) — clearly stronger contributions than the paper under review. Initial bracket: [4, 6.5].

*Round 2 (narrowing):* Within the bracket, the ExpertLongBench paper (5.5, nJvgBolRcR) is the most directly comparable — both contribute benchmarks for long-form generation with evaluation gaps. ExpertLongBench had weaknesses about small sample size (100/task) and LLM judge reliance, comparable in severity to this paper's evaluation gaps. The Rainbow Padding paper (6.0, cznTlh7Msz) had cleaner controlled experiments but narrower scope (dLLMs only). This paper's scope (multi-model evaluation across structured/unstructured tasks + a mitigation method) is broader, but its evaluation is less cleanly controlled. Comparing to the Semantic Isotropy paper (5.0, ROTJZgRp7Q), which had more fundamental methodological questions (metric definition, evaluation circularity), this paper is stronger. Reading these anchors positions the paper at ~5.5.

*Final score:* **5.5** — The paper makes genuine contributions (a novel volatility benchmark, a practical training-free mitigation method, and a well-structured multi-stage investigation) but the evaluation has significant presentation issues (headline numbers compared to the wrong baseline, missing unified comparison table) and several gaps (qualitative attention analysis, N=5, no ablations) that prevent it from reaching a higher score. These are fixable issues that do not undermine the core contributions.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>