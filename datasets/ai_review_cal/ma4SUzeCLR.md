- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper presents MathError, a dataset of 23,162 Chinese elementary-level math word problems (drawn from Math23K) annotated with five error types (multiple interpretations, informal wording, unitless, unclear relationship, calculation error) plus a None class. The paper also proposes Prompt Refinement through Self-Optimization (PRO), a framework that iteratively refines error-type definitions and few-shot examples via LLM self-reflection. The work addresses a practical need in educational assessment — helping teachers detect problematic questions before deployment.

---

## Strengths

- **Real-world error annotations, not artificially constructed.** The dataset annotates naturally occurring errors from the Math23K corpus, whereas prior work (Sun et al., 2024) used questions deliberately modified to be unanswerable. This yields a more realistic error distribution (Table 2), including the very rare Calc (67/23,162) and INTPN (136/23,162) types.

- **Iterative annotation process with quantitative quality tracking.** Annotator macro F-scores against the gold set improved from 0.6959 to 0.8240 across five stages (Table 1), and agreement on a held-out set reached Fleiss' κ = 0.8103. The process is well documented in Section 4.

- **Systematic investigation across six research questions.** Section 7 addresses prompting methods (RQ1), multi-label vs. binary classification (RQ2), human- vs. model-generated prompts (RQ3), convergence behavior (RQ4), model size effects (RQ5), and perplexity analysis (RQ6). This provides a more informative picture than a single performance number.

---

## Weaknesses

### Major

1. **PRO's improvement over the strongest baselines is marginal and not statistically significant.** The paper's own text acknowledges that PRO (GPT-4o) "does not significantly outperform the remaining methods in Table 3" — meaning it does not significantly outperform GPT-4o without PRO. The only significant test reported (p < 0.05) is against GPT-3.5, a weaker model. Moreover, PRO uses additional data (the 30-sample reflection set for self-optimization) that is not available to the baselines, making the comparison structurally asymmetric. This substantially weakens the claim that PRO "significantly outperforms other methods."

2. **Annotation gold standard is small and author-derived, raising concerns about label quality.** The golden set used to calibrate annotators contains only 100 questions (23 with errors), all pre-annotated by the authors themselves. With rare error types (e.g., Calc with only 67 total samples, INTPN with 136), label noise in these minority classes can significantly impact evaluation. The inter-annotator agreement on the full dataset (Fleiss' κ = 0.6038) is only "moderate," and whether the label distribution of the gold set matches the real dataset is not discussed.

3. **No robustness checks or variance estimates.** The demonstration set (15 examples) and reflection set (30 examples) are fixed, with no multiple seeds, cross-validation, or sensitivity analysis reported. Given the small size of these sets, results could easily be driven by which specific examples are chosen. Without variance estimates, it is impossible to know whether reported F1 differences (e.g., between PRO and baseline GPT-4o, or between human- and model-generated definitions) are meaningful or due to chance.

### Minor

1. **Mixed findings on model-generated vs. human-written definitions — the conclusion overstates the case.** The paper's conclusion states that "machine-generated definitions of error types... enhance effectiveness," but in the GPT-3.5 few-shot setting (Table 7), human-written definitions with human-written examples achieve higher overall macro F1 (0.2407) than model-generated definitions with human-written examples (0.2229). Model-generated definitions are better only when averaging across the five error types *excluding* the None class, which is a selective metric. The paper acknowledges the discrepancy in the text but the conclusion still makes a blanket claim.

2. **ROUGE-1 as a convergence metric is poorly motivated.** The PRO framework uses ROUGE-1 (lexical overlap) to decide whether definitions have converged (threshold τ = 0.9). Two definitions that are semantically identical but lexically different would be scored as not converged. The choice of threshold is also arbitrary, and its impact is not analyzed.

3. **Perplexity analysis uses a different model family.** The perplexity explanation (RQ6) is conducted on LLaMA3 8B while the main experiments use GPT-3.5 and GPT-4o. Lower perplexity on model-generated prompts for LLaMA3 does not directly explain GPT-4o's performance.

### Trivial

- None.

---

## Nice-to-Haves

- Reporting recall at a fixed precision (or vice versa) that reflects real-world deployment constraints would strengthen practical relevance.
- A small user study where teachers assess the relevance and actionability of detected errors would demonstrate practical utility beyond algorithmic metrics.
- Fine-tuned smaller model baselines (e.g., BERT, T5) would provide a natural lower bound for the "limited data" scenario that the paper claims to simulate.

---

## Removed Points

- **"Inter-annotator agreement concern restated"**: The paper already reports both κ values (0.6038 and 0.8103) and honestly characterizes them. This is merged into major weakness #2 above.
- **"Multi-label vs. binary uses only zero-shot"**: The paper presents this as an exploratory analysis (RQ2), not a main experimental result. It's a valid observation but not a weakness of the paper — the paper doesn't claim this is a main finding. Removed.
- **"Missing fine-tuned baselines"**: Moved to Nice-to-Haves since the paper explicitly focuses on few-shot LLM settings; requesting BERT/T5 baselines is scope-adjacent.
- **"Error type definitions should be grounded in educational literature"**: This is a scope extension request, not a flaw in the paper as written.
- **"PRO's advantage is asymmetric because of additional validation data"**: This is already sufficiently covered in major weakness #1.
- **"Missing appendix/proofs"**: Parser-stripped content; would exist in original submission. Removed per instructions.

---

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the PRO improvement is marginal and not significant against the strongest baselines is simply a clearer articulation of what the paper itself acknowledges. The tension between model-generated vs. human-written definitions across different metrics is genuinely interesting but the paper already surfaces it.

---

## Suggestions

1. **Run PRO and baselines with multiple random splits of the demonstration/reflection sets** (e.g., 5 different seeds) and report mean ± std macro F1. This is the single highest-impact improvement the authors could make, as it would clarify whether the small observed differences are meaningful.

2. **Either statistically control for the reflection set advantage** (e.g., give the baselines the same 30 samples as additional few-shot examples) or clearly frame PRO's improvement as coming from *both* the reflection mechanism *and* additional data exposure.

3. **Present the human- vs. model-generated definition results honestly as "mixed"** in the conclusion: model-generated definitions help in certain settings (GPT-4o, multi-label average excluding None) but not others (GPT-3.5 few-shot, overall macro F1). This would be more accurate than the current blanket claim.

4. **Expand the golden set** to at least 300–500 independently expert-annotated samples to better validate dataset quality, especially for the minority error types.

---
