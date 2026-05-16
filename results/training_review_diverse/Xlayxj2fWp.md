Now I have thoroughly read the paper and verified all claims. Let me produce the final consolidated review.

## Summary

DNA-GPT proposes a training-free, zero-shot method for detecting GPT-generated text. The approach truncates a candidate text at a midpoint, uses the prefix to prompt an LLM to regenerate the continuation, and then measures divergence (via n-gram overlap in black-box or probability divergence in white-box) between the original continuation and the regenerations. The method is evaluated on five datasets, five LLMs, and against supervised baselines (GPTZero, OpenAI's classifier) and DetectGPT, consistently achieving higher AUROC and TPR at 1% FPR.

## Strengths

- **Training-free zero-shot detection outperforms supervised baselines across multiple datasets.** The black-box BScore achieves higher AUROC and TPR at 1% FPR than both GPTZero and OpenAI's classifier on newly curated datasets (Reddit-ELI5, Scientific Abstracts) that are temporally controlled to avoid memorization, as well as established datasets (PubMedQA, Xsum). This is the paper's central contribution and is well-supported by the reported metrics. The advantage is particularly notable on the new datasets where the supervised baselines underperform, demonstrating the method's practical value when training data for emerging models is scarce.

- **Explainable detection via n-gram overlap evidence.** The method provides human-interpretable evidence (shared 4+-grams between regenerated and original text) rather than a binary prediction, a feature unique among the compared detectors. Section 3.3 formalizes this and gives concrete examples. This directly addresses a real gap: educators and reviewers need evidence, not just scores.

- **Robustness under text revision attacks.** Under T5-3B span-replacement revision, the method's AUROC drops only from 99.09 to 98.48 even when 50% of the text is revised, while GPTZero and OpenAI's classifier "dramatically deteriorate" at revision rates >30%. This supports the paper's claim of robustness and is practically important since AI text is often post-edited.

- **Effective non-English detection.** On the WMT-2016 German split, the white-box method achieves results comparable or superior to OpenAI's supervised classifier, while GPTZero performs no better than random. This demonstrates language-generality beyond English, a gap the paper explicitly notes in prior work.

- **Novel model sourcing capability.** The method can distinguish which LLM generated a given text (e.g., GPT-4 vs. LLaMa-13B vs. GPT-NeoX-20B), a task not addressed by existing human-vs-machine detectors. This is an interesting auxiliary contribution.

## Weaknesses

### Fatal

None. No issue invalidates the paper's core claims.

### Major

None. All identified issues are addressable in a revision and do not threaten the central contribution.

### Minor

- **Regeneration prompt format unspecified.** The paper states "we ask the LLMs to continue generating the remaining sequences purely based on X" (line 65) but does not specify the exact API prompt format used for chat-based models (GPT-3.5-turbo, GPT-4), including whether a system message was provided, how the prefix X was wrapped, or whether the "known prompt" scenario used a different template than the "unknown prompt" scenario. While the method's concept is clear, the missing detail prevents exact replication. This should be documented.

- **No variance or confidence-interval reporting.** All metrics (AUROC, TPR) are reported as single point estimates. The experiments involve randomness from multiple sources — LLM regeneration (K samples), varying thresholds, and the T5 span-replacement attack — yet no standard deviations, bootstrap intervals, or multi-run averages are provided. Given test set sizes of 100–200 instances, some score differences could fall within noise. The large reported gaps mitigate this concern, but variance reporting would strengthen the evidence.

- **Likelihood-Gap theoretical derivation does not guarantee discriminability.** The inequality chain (lines 82–103) bounds the log-likelihood gap in terms of total variation via Pinsker's inequality, but the bound involves ||log p(·|X)||_∞, which can be arbitrarily large when probabilities approach zero. This means the derivation does not guarantee a positive lower bound on d_TV or d_KL. The paper's empirical evidence (Figure 3) amply supports the hypothesis, but the theoretical framing should be qualified as a motivation rather than a proof.

- **Revised text experiments are a limited pilot.** The revision experiment uses only 100 instances from a single dataset (Reddit) with a single synthetic attack (T5-3B span replacement). While the results are suggestive, the claim of "robustness" would be stronger with additional attack types (e.g., human paraphrasing, substitution by other LMs) and larger samples.

- **BScore hyperparameters not ablated.** The paper sets n₀=4, N=25, f(n)=n log n and states these "work well across all datasets" (line 127), but provides no ablation or sensitivity analysis. While the approach is intuitive, the absence of any study on how performance varies with these choices leaves open the possibility of overfitting.

- **No discussion of computational cost.** The method requires K · (L − ⌈γL⌉) tokens of regeneration per test instance (plus the API call overhead). For practitioners evaluating cost vs. accuracy trade-offs, a brief comparison of API cost and runtime relative to baselines would be helpful.

### Trivial

- The model sourcing section (Section 4.7) describes the task and mentions a results table (Table 8) but does not give concrete accuracy numbers or a precise algorithm in the main text. (If these were in the appendix, they are not available in the extracted text.)

## Nice-to-Haves

- Add a sensitivity analysis for BScore parameters (n₀, N, f(n)) on at least one dataset to demonstrate robustness to the defaults.
- Expand the revision experiments with additional attack types (e.g., human paraphrasing, substitution by different LLMs) and larger sample sizes to strengthen the robustness claim.
- Discuss the limitation that the method requires access to the same LLM that may have generated the text (i.e., for detecting text from an unknown model the user cannot prompt, the method does not directly apply).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Data contamination / memorization inflating results on older datasets** — The paper explicitly acknowledges memorization concerns (line 155: "Previous research found that LM can memorize training data, making detection meaningless") and collects two new datasets temporally filtered to avoid this problem. The older datasets (PubMedQA, Xsum, WMT16) are included for comparability with prior work (DetectGPT). Moreover, memorization of human-written text would cause the model to reproduce it during regeneration, increasing n-gram overlap and making human text *harder* to distinguish (more false positives), not easier. The strongest results are on the controlled new datasets. The paper's treatment of this issue is reasonable.

2. **Missing comparisons to methods like Fast-DetectGPT** — This method postdates the paper (ICML 2024); the paper's baseline set (GPTZero, OpenAI Classifier, DetectGPT) is appropriate for its time.

3. **Narrow competitor set / state-of-the-art claim** — The paper compares against the two most prominent supervised detectors and DetectGPT. Claiming SOTA relative to these is defensible and common practice.

4. **BScore denominator numerical stability concerns** — Speculative; no evidence of numerical issues is provided or observed.

5. **Threshold selection not explained** — This is standard practice in detection evaluation (sweep on test set) and does not affect the results.

6. **Model sourcing results not visible** — Parser artifact; the table exists in the original submission.

7. **Missing variance for temperature experiment** — While technically true, the critic acknowledges this is an observation, and the large performance gaps make the qualitative conclusion clear.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated contributions (training-free detection, explainability, robustness) and surface standard concerns (reproducibility details, variance reporting) without identifying a hidden flaw or unexpected implication.

## Suggestions

1. **Specify the exact prompt format** for each model type (chat vs. completion API) in an appendix or the experimental setup, including the system message (if any) and whether the prefix X was passed as a user message or a raw string.
2. **Add variance estimates** — report AUROC and TPR with standard deviations over multiple regeneration runs (or bootstrap over test instances) for key experiments.
3. **Qualify the Likelihood-Gap derivation** as a motivating heuristic rather than a proof, noting that the bound involves ||log p||_∞ and does not guarantee a positive gap in all cases.
4. **Add an ablation study** for BScore parameters (n₀, N, f(n)) on at least one dataset to show the default choices are not brittle.
5. **Expand the revision robustness experiments** with additional attack types and larger samples to strengthen the robustness claim.

## Score and Decision

This paper presents a novel, well-motivated training-free detection method with strong empirical results across multiple dimensions (English, German, robustness to revision, model sourcing). The approach is intuitive, the method is clearly described, and the evidence supports the central claims. The weaknesses — unspecified prompt format, missing variance estimates, informal theoretical derivation — are substantive but addressable and do not undermine the paper's core contribution. The paper makes a clear contribution to the AI-generated text detection literature.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>