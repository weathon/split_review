Now I have enough information to write the consolidated review. Let me compose it.

## Summary

This paper investigates whether uncertainty-based abstention can improve LLM reliability in three settings: correctness (on answerable QA tasks), hallucinations (distinguishing answerable from unanswerable questions), and safety (identifying unsafe responses to adversarial prompts). It compares statistical uncertainty measures (negative log-likelihood, predictive entropy, semantic entropy) with a verbalized measure called In-Dialogue Uncertainty (InDU), operationalized as hedge-word count, across pretrained and RLHF-tuned Llama2 models. The central empirical finding is that the best uncertainty measure depends on the scenario: statistical measures work for correctness and safety, while InDU works for unanswerable questions. RLHF preserves uncertainty awareness for correctness, enhances InDU for unanswerable questions, and is critical for identifying unsafe responses.

## Strengths

1. **Task-specific optimal uncertainty measures are cleanly identified.** The paper demonstrates across three distinct failure modes that no single uncertainty measure works universally: statistical uncertainty (semantic entropy) is best for correctness (Table 1, average AUROC 0.69 on RLHF models) and safety (Table 3, AUROC up to 0.99 on AutoDAN with RLHF), while InDU is best for detecting unanswerable questions (Table 2, AUROC 0.75 on RLHF). This conditional finding is non-obvious and practically actionable.

2. **Quantified abstention gains are concrete and non-trivial.** The paper reports specific operating points: correctness improves from 84.4% to 86.0% by rejecting the 5% most uncertain samples on TriviaQA (Section 6.1); ~50% of unanswerable questions are detected at a 10% false refusal rate (Section 6.2); safety improves from 92.1% to 95.1% on AttaQ and from 92.5% to 99.4% on AutoDAN by rejecting the 10% most uncertain responses (Section 6.3). These numbers make the practical value of uncertainty-based abstention tangible.

3. **RLHF's effect on uncertainty is characterized with nuance.** The paper shows that despite prior work documenting RLHF-induced overconfidence and miscalibration, RLHF *preserves* the model's ability to rank correct vs. incorrect responses (comparable AUROCs in Table 1), *enhances* InDU for unanswerable questions (AUROC 0.75 vs. 0.69, Table 2), and is *essential* for safety-aware uncertainty (AUROC up to 0.99 vs. near-random for base/instruction-tuned, Table 3). This refines the current understanding of RLHF's impact on model self-awareness.

4. **The InDU metric is simple, interpretable, and requires no extra prompting or training.** It operates purely on the model's generated text via a fixed hedge-word list, yet outperforms statistical measures for detecting unanswerable questions. This offers a computationally cheap alternative for practitioners.

5. **Reproducibility is facilitated through use of open-source models (Llama2 family) and publicly available datasets.** The paper specifies model sizes (7B, 13B, 70B) and uses standard Hugging Face interfaces for log-probability access.

## Weaknesses

### Fatal
None.

### Major

1. **The near-perfect safety AUROCs on AutoDAN (0.96–0.99) lack transparency about dataset characteristics and label quality.** The paper reports these very high scores without providing (a) the number of adversarial prompts per dataset, (b) the class balance (safe vs. unsafe response proportions per model), or (c) any analysis of ground-truth label reliability (the paper uses both Llama Guard and keyword matching but never reports their agreement). While AUROC is class-balance-robust, the extreme scores on AutoDAN compared to AttaQ (0.78) warrant explanation. Without knowing whether AutoDAN has few prompts, an easy distribution, or noisy labels, readers cannot assess whether these headline results are robust or artifactually inflated. This is the most significant weakness because the paper's strongest safety claim ("99% of unsafe responses filtered") rests on these numbers.

### Minor

2. **The hallucination analysis rests entirely on one dataset (SelfAware) with no category-level breakdown.** The paper mentions five categories of unanswerable questions (Section 4.2) but never analyzes whether InDU works equally well across them. If InDU's effectiveness is concentrated in categories with obvious linguistic markers (e.g., counterfactual questions that naturally elicit hedge words), the result may not generalize as broadly as claimed. Adding category-level AUROCs would substantially strengthen this finding.

3. **No confidence intervals or error bars are reported for any AUROC or ARC numbers.** For an empirical study comparing multiple measures across datasets and model variants, the lack of uncertainty estimates makes it impossible to determine whether observed differences (e.g., InDU 0.69 vs. semantic entropy 0.60 for hallucinations) are meaningful. Bootstrapping AUROC is standard and straightforward. This weakens the reliability of the comparative claims.

4. **No prompt-based abstention baseline is included.** For the hallucination setting in particular, a natural comparison is whether simply instructing the model to say "I don't know" achieves similar or better abstention performance than post-hoc InDU analysis. While the paper's focus is on post-hoc measures, including this baseline would clarify whether the uncertainty-based approach adds value over a zero-cost prompting alternative. The paper discusses prompting-based methods in Related Work (as having computational and distribution-shift limitations) but never directly compares.

5. **The claim "almost no additional computational overhead" is too broad.** Negative log-likelihood requires a single inference, which indeed has minimal overhead. However, predictive entropy and semantic entropy require multiple (N) response samples. The paper follows the sampling approach of Kuhn et al. but does not specify N. For large models, multi-sample inference is non-negligible. The claim should be qualified to distinguish single-inference from sampling-based methods.

6. **No limitations section.** The paper ends with a brief Discussion (Section 7) but does not discuss its own limitations: narrow model scope (Llama2 family only), reliance on single datasets for hallucinations, the absence of confidence intervals, or potential distribution shifts when deploying abstention filters in practice.

7. **Model scope is limited to the Llama2 family (plus Vicuna, which is also Llama2-based).** This is a reasonable choice given the need for log-probability access, but it means the findings may not generalize to models with different architectures, training distributions, or RLHF procedures. The paper would benefit from acknowledging this scope limitation.

### Trivial

- None that warrant listing separately after the above.

## Nice-to-Haves

- An analysis of why the AutoDAN and AttaQ results differ so substantially (e.g., prompt length, topic distribution, class imbalance). The paper observes that "99% of unsafe AutoDAN responses can be filtered at 10% false refusal" vs. "70% of unsafe AttaQ responses at 30% false refusal" — discussing why would deepen the safety analysis.
- A small human evaluation or comparison of the two label sources (Llama Guard vs. keyword matching) for safety ground truth.
- A brief discussion of threshold selection for practitioners deploying abstention in practice.

## Removed Points

- **"Formatting issue in column header of Table 1"** — This is a parser artifact from PDF extraction, not an author error. Removed per formatting/style nitpick rule.
- **"N=10 as per Kuhn et al."** with associated computational criticism — The reviewer attributed a specific N value to the paper that the paper itself does not state. However, the underlying concern about multi-sample overhead is valid and kept in Minor weakness #5 above.
- **Reviewer's framing of the hallucination issue as "critical"** — Downgraded from critical to minor because the SelfAware result (InDU AUROC 0.75) is still meaningful and informative even without category breakdown or additional datasets. The core finding is not invalidated, just less thoroughly supported than it could be.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated findings and identify constructive areas for strengthening rather than offering new synthetic insights.

## Suggestions

1. **Add dataset sizes and class balances for all experimental settings.** This is the single highest-priority addition. Report the number of prompts and the proportion of correct/incorrect, answerable/unanswerable, and safe/unsafe responses per model for every dataset.

2. **Add confidence intervals (bootstrapped) or error bars to all AUROC and AUARC numbers.** Bootstrapping AUROC is standard (e.g., 1,000 bootstrap iterations) and would allow readers to assess whether observed differences between uncertainty measures are statistically meaningful.

3. **Provide a category-level breakdown of the SelfAware results.** Show whether InDU's effectiveness is uniform across the five categories of unanswerable questions or driven by specific types.

4. **Validate safety ground-truth labels by reporting inter-method agreement** between Llama Guard and the keyword-based approach, or conduct a small human evaluation.

5. **Add a limitations section** acknowledging the narrow model scope, reliance on single datasets for the hallucination setting, and the absence of confidence intervals.

6. **Qualify the "almost no additional computational overhead" claim** to distinguish between single-inference (NLL) and multi-sample (predictive/semantic entropy) methods.

## Score and Decision

The paper makes a solid empirical contribution: it systematically evaluates multiple uncertainty measures across three important LLM failure modes, identifies which measure works for which scenario, and provides concrete, quantified abstention gains. The finding that RLHF is actually essential for safety-aware uncertainty (despite increasing overall miscalibration) and that InDU is useful specifically for unanswerable questions are non-obvious and practically relevant.

The main weaknesses are that (a) the strongest safety results lack transparency about dataset size, class balance, and label quality, and (b) the findings are presented without confidence intervals, making it hard to assess the significance of observed differences. These are addressable and do not invalidate the core contribution—the correctness results are well-supported across 5 datasets, the hallucination results are informative if not exhaustive, and the safety trend is consistent across two datasets even if the AutoDAN numbers need scrutiny.

The paper is a well-designed empirical study whose limitations can be addressed in a rebuttal or revision. I recommend acceptance.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>