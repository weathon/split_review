Here is the consolidated final review.

## Summary

This paper introduces FOBAR, a verification method that combines forward reasoning (sampling multiple CoT chains as in Self-Consistency) with backward reasoning: for each candidate answer, a number in the question is masked, and the LLM is asked to predict that number given the candidate answer. The forward and backward probabilities are combined via geometric mean (α=0.5). Experiments on six math datasets and three LLMs (text-davinci-003, GPT-3.5-Turbo, GPT-4) show consistent improvements over Self-Consistency, with the highest average accuracy across all settings.

## Strengths

- **Combined forward-backward reasoning consistently outperforms each alone (Table 3).** The ablation study (Section 4.4) clearly demonstrates this: for text-davinci-003 with CoT, forward-only achieves 81.4%, backward-only 82.1%, and the combined FOBAR achieves 83.5%. This pattern holds across all three LLMs and both base prompts, providing direct evidence for the core claim that combining both directions is better than either alone.

- **Achieves highest average accuracy across six math datasets and three LLMs (Table 1).** FOBAR with ComplexCoT achieves the best average for each model (text-davinci-003: 85.0%, GPT-3.5-Turbo: 87.0%, GPT-4: 91.9%), consistently beating Self-Consistency, Self-Verification, PHP, and prior methods. The trend is robust across most individual datasets.

- **Simple backward reasoning template avoids rewriting errors (Sections 3.2–3.3).** Unlike Self-Verification, which requires an LLM to rewrite a question-answer pair into a declarative statement, FOBAR simply appends a template ("If we know the answer… what is the value of x?") to the masked question. This avoids a source of potential rewriting mistakes and uses only string comparison for verification.

- **Robust to the combination weight α (Figures 2–3).** The ablation on α ∈ [0,1] shows stable performance across all three LLMs, and arithmetic vs. geometric mean yields comparable results. This means the method does not require careful hyperparameter tuning.

- **Backward reasoning intuition is empirically validated (Figure 4).** Using the correct candidate answer yields roughly 2× higher accuracy in predicting masked numbers compared to wrong candidates, confirming that backward reasoning can discriminate correct from incorrect answers.

- **Failure-case analysis quantifies improvements over Self-Consistency (Tables 5–6).** Out of 294 Self-Consistency failures that had at least one correct reasoning chain, FOBAR rectifies 54 (≈18%). The analysis also shows that ≈60% of Self-Consistency failures contain at least one correct chain, providing a clear upper bound on potential improvement from verification.

## Weaknesses

### Fatal

None.

### Major

- **Self-Verification comparison is confounded by candidate set size.** The paper defines Self-Verification as operating on the top-2 candidate answers (Section 4.1, line 462–465), while FOBAR uses the full set of candidates from forward sampling. This design difference alone could explain much of the performance gap — backward reasoning has more opportunities to correct errors when it evaluates all candidates, and the baseline is effectively handicapped by discarding information. The paper does not run Self-Verification with all candidates, nor FOBAR restricted to top-2 candidates. Since the paper claims that FOBAR's "simple template" and "combination" are the source of improvement over Self-Verification (lines 523–524, 129–131), the confound weakens this specific comparison. The authors should match setups or explicitly discuss how much of the gain comes from candidate coverage vs. the template itself.

### Minor

- **No statistical significance or variance estimates are provided.** The paper follows a standard protocol (single run, line 502–503), but on GPT-4 — the most interesting model — gains over Self-Consistency are often 0.3–0.5 percentage points (e.g., CoT: 91.1→91.4; ComplexCoT: 91.6→91.9). These differences could be within sampling noise, and without any error characterization the reader cannot assess whether the improvements on the strongest model are reliable. The authors could have provided variance estimates for a subset of settings (e.g., bootstrap resampling on the forward samples, or 3–5 seeds on one or two datasets).

- **Computational cost language is potentially misleading.** The paper states that "the additional computation cost of Algorithm 1 is negligible" (line 360), which refers to the arithmetic for combining probabilities. However, the actual backward reasoning procedure — for each candidate answer, for each number in the question, sampling M<sub>B</sub>=8 chains — involves substantial LLM calls. For a question with 4 numbers and 10 candidate answers, this is 320 LLM calls for backward verification alone. The paper does not report total API calls or tokens, nor compare cost-adjusted performance. The claim of "negligible" cost should be scoped to the probability combination step, not the full algorithm.

- **The AQuA deficit on GPT-4 is not discussed.** Under GPT-4 ComplexCoT, PHP achieves 79.9% on AQuA while FOBAR achieves 75.2% — a 4.7-point gap. FOBAR ties Self-Consistency (75.2) but is surpassed by PHP and Self-Verification (75.6). This is not mentioned in the paper despite the claim of "state-of-the-art" performance. Since AQuA is multiple-choice and typically involves fewer numbers, the backward verification may be less effective on this dataset. A brief discussion would help the reader understand the method's limitations.

- **Non-mathematical experiments are thin.** Only two tasks (Date Understanding and Last Letter Concatenation) are presented, with small improvements (0.3–1.2 percentage points) and no significance testing. The masking extension for non-math tasks (Section 3.4) is a hand-crafted heuristic (masking a word, shifting letters for the distractor), and the paper's claim of generality rests on weak evidence. Including more tasks (e.g., Coin Flip, Checkmate) or tempering the generality claim would improve the paper.

### Trivial

None.

## Nice-to-Haves

- A comparison of FOBAR vs. using the same additional computational budget to sample more forward chains (e.g., Self-Consistency with 400 forward chains vs. FOBAR's 10 forward + backward calls). This would clarify whether the gains are from verification or simply from more computation.
- A failure analysis of the ~40% of cases with no correct forward chain (which are unrecoverable by any verifier), to characterize the irreducible error.
- Ablation where FOBAR is restricted to top-2 candidates (matching Self-Verification's setup), directly controlling the candidate set size confound.

## Removed Points

- **"The paper does not compare FOBAR's AddSub result to RCI's result"**: The paper does list RCI in the table as a baseline with † (from original publication). RCI is included for reference, and the paper's claims are about average performance. Removed because the paper already includes these baselines and the critic's concern is about a secondary detail.
- **Criticisms about missing related work**: Removed per instructions — I cannot verify the existence of missing related works.
- **Pure formatting/style nitpicks and missing appendix references**: Removed per instructions — the parser strips these sections; they exist in the original submission.
- **"Strengthening the Paper on Its Own Terms" suggestions** (controlling Self-Verification, variance estimates, reporting API calls): These are merged into the weaknesses and nice-to-haves above rather than kept as separate sections.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem", "the problem is interesting"): Removed for being generic/superficial rather than specific and evidence-backed.

## Novel Insights

None beyond the paper's own contributions. The key insight — that backward verification via masked-number prediction is a natural discriminator for mathematical reasoning — is the paper's own central contribution.

## Suggestions

1. **Control the Self-Verification comparison** by either running Self-Verification with all candidates or running FOBAR restricted to top-2 candidates. This would isolate whether the template+combination or the wider candidate pool drives the gains.
2. **Add variance estimates** for the GPT-4 results (e.g., 3–5 seeds on GSM8K and SVAMP, or bootstrap confidence intervals from the forward samples). This would greatly strengthen the most important results.
3. **Report total LLM calls/tokens** for FOBAR vs. Self-Consistency and Self-Verification, and consider a cost-adjusted comparison where the same budget is allocated to more forward chains.
4. **Discuss the AQuA deficit** relative to PHP on GPT-4 ComplexCoT, explaining why backward verification is less effective for multiple-choice problems with fewer numbers.
5. **Qualify the "state-of-the-art" claim** given the AQuA results and the lack of significance testing.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>