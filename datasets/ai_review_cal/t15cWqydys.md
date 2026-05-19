- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have a thorough understanding of the paper and can cross-reference each reviewer claim against the actual text. Let me construct the final consolidated review.

## Summary

This paper provides the first systematic evaluation of decoding-free candidate selection methods — techniques that estimate candidate probabilities from the logits of the first decoding step without full autoregressive generation. It evaluates five estimation methods (first-token, last-token, token-average, token-sum, sample-average) across nine tasks spanning small candidate pools (MCQA) and massive candidate pools (clinical coding with up to 94k options), using LLaMA3, Mistral, Flan-T5, and GPT-2 families. The paper distills the results into nine empirical "insights" about when and how these methods work.

## Strengths

1. **First systematic evaluation across diverse tasks and models** — The paper covers 5 MCQA tasks and 4 clinical decision tasks, with models spanning different architectures (decoder-only vs. encoder-decoder), sizes (137M to 11B), and training paradigms (pre-trained vs. instruction-tuned). This breadth, documented in Sections 4.1–4.2 and Tables 3–4, is a genuine contribution — no prior work has mapped this space.

2. **Non-obvious finding that estimation can outperform full decoding for weak models** — The paper shows (Table 3, green cells; Table 4) that for non-instruction-tuned models on challenging tasks (GPQA, CommonsenseQA, clinical decisions), estimation methods can surpass full decoding by substantial margins (e.g., +29.25 recall for Mistral v0.3 on lab orders). This is a practically useful, non-obvious insight.

3. **Empirical demonstration that first-step logits are optimal** — Figure 2(a) systematically shows that estimation performance peaks at step 1 and degrades at intermediate steps before recovering at later steps. This provides empirical justification for a widely-used design choice that previously lacked evidence.

4. **Concrete efficiency measurements** — The paper reports per-instance runtime and speedup factors (e.g., 2.6×–145.9× on CommonsenseQA) in Table 3, quantifying the practical efficiency advantage of decoding-free methods.

5. **Ablation on candidate token selection** — Using GPT-4o to select variable numbers of important tokens per candidate, Figure 2(b) shows that the full candidate sequence outperforms any keyword subset. This provides principled guidance countering the intuition that focusing on keywords might improve estimation.

## Weaknesses

### Fatal
None.

### Major

1. **Potential confound in clinical task comparison between estimation and full decoding** — In clinical tasks (Table 4), full decoding outputs free-form text that must be mapped to candidate codes via "task-specific mapping rules" (Section 3.2). Estimation methods directly select from the candidate pool. If the mapping function (regex or semantic similarity) fails for reasons unrelated to the model's knowledge — e.g., the model produces "pneumonia" but the ICD-10 code is "J18.9" — the full-decoding baseline is penalized by the mapping brittleness rather than genuine inferiority. The paper acknowledges this asymmetry (Section 2.4) but does not control for it. As a result, the important claim that "estimation methods can outperform full decoding" on clinical tasks (Insight 1, Insight 4 for weak models) may be partially confounded. The authors should either (a) provide a controlled experiment where full decoding generates the code directly, or (b) quantify mapping failure rates on a sample.

### Minor

2. **Insight 3 is overstated** — The paper claims estimation results are "similar" and instruction tuning makes "no significant difference" for decoding-free methods. However, across Table 3, estimation methods show consistent improvements of 2–8 points from instruction tuning (e.g., CommonsenseQA first-token: ~0.50 to ~0.56; token-sum: ~0.49 to ~0.56). These are not large compared to full-decoding gains, but they are systematic and non-trivial. A more accurate characterization would state that instruction tuning provides smaller but consistent benefits to estimation methods (e.g., ~2–8 points) compared to full decoding (~larger gains), rather than positioning the effect as negligible.

3. **Sample Avg. method lacks justification** — The paper introduces "Sample Avg., which calculates average logits for every other token in candidate sequences" (Section 5) without explaining why "every other token" is a principled choice rather than all tokens or a random subset. Since this method sometimes achieves the best results (e.g., on lab orders with LLaMA3), the reader cannot interpret whether this is meaningful or an artifact of an arbitrary design decision.

4. **No precision or F1 reported for multi-label clinical tasks** — The clinical tasks require selecting *multiple* candidates per instance, yet only recall is reported (Table 4). In multi-label settings, recall alone is insufficient — a model that predicts all candidates would achieve perfect recall but be useless. Without precision, precision@k, or F1, the clinical task results are incomplete and potentially misleading.

5. **No confidence intervals or statistical significance** — For a benchmark paper reporting empirical comparisons, the absence of any uncertainty estimates (confidence intervals, bootstrap estimates, or significance tests) weakens the conclusions, especially given variability across tasks and models. This limits the reader's ability to assess whether reported differences between methods are reliable.

6. **Tokenization handling for estimation methods is underspecified** — When candidates are subword-tokenized (e.g., "natural habitat" → ["natural", "habi", "tat"]), it is ambiguous which token-level logits are used for methods like "last-token" estimation. The paper acknowledges this obliquely with the misspelling "flowser" in Example 1 (Section 3.1), but a clear specification is needed for reproducibility.

### Trivial

- Random guess baseline is mentioned (Section 4.2) as being included but does not appear in any result table.
- Decoding hyperparameters (temperature, top-p, greedy vs. sampling) for the full-decoding baseline are not specified.

## Nice-to-Haves

- Reporting confidence intervals or bootstrap estimates would strengthen the benchmark character of the paper.
- Including random guess performance in the tables would help calibrate reader expectations.
- Clarifying subword tokenization handling would improve reproducibility.
- Precision@k for the clinical tasks would provide a more complete picture.

## Removed Points

*These points were flagged in the reviews but are removed or demoted per the filtering rules:*

- **"DPR baseline is oddly included"** — A subjective opinion about baseline selection, not a substantive weakness. The paper frames DPR as a reference model (Section 3.2), which is a standard practice. *Removed.*
- **"Full decoding hyperparameters not specified"** — Moved to Trivial (see above) rather than remaining a standalone criticism.
- **"Figure 2(a) claim about first step optimality is only partially supported"** — The paper's Insight 6 already acknowledges that "the estimation performance rises after generating the lead phrase starting from the 10th output step." The claim is properly qualified. *Removed (paper already addresses this).*
- **"Conclusion mentions text summarization as future direction, which feels tangential"** — This is an opinion about scope; future work directions do not constitute a weakness. *Removed.*
- **"Missing related works"** — Per rules, the reviewer cannot verify the existence of missing citations. *Removed.*

## Novel Insights

The most valuable cross-review observation is that the paper's core weakness — the confounded clinical task comparison — and its core strength — the breadth of the evaluation — are two sides of the same coin. The breadth lets the authors draw general insights, but it also means that individual task settings (especially the clinical ones) may have task-specific confounds that the one-size-fits-all evaluation framework cannot fully address. This tension between breadth and depth is the central methodological challenge for benchmark papers of this type, and the authors would benefit from explicitly addressing it — e.g., by running a controlled clinical experiment that isolates the mapping confound.

## Suggestions

1. **Address the clinical mapping confound directly.** Run an additional experiment where the full-decoding baseline is prompted to output the code identifier directly (e.g., "J18.9") and evaluate exact match. This isolates the effect of decoding vs. estimation without confounded mapping. Alternatively, manually annotate a sample of full-decoding outputs to quantify how often generation is correct but mapping fails.

2. **Re-calibrate Insight 3** to accurately describe the magnitude of instruction-tuning benefits for estimation methods (e.g., "estimation methods improve by 2–8 points on MCQA tasks after instruction tuning, compared to larger gains for full decoding").

3. **Either justify Sample Avg. with a principled rationale** (e.g., to avoid position bias from common stopwords at token positions) or remove it and focus on the better-motivated methods.

4. **Add precision or F1** to the clinical task results (Table 4) to account for the multi-label nature.

5. **Add random guess baselines to the result tables** and a brief note on statistical reliability.
