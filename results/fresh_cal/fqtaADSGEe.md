Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper identifies significant labeling errors in existing REC benchmarks (RefCOCO/+/g with 14%, 24%, and 5% error rates), releases cleaned versions, and shows that five LMMs gain 1.57–3.08 accuracy points on the cleaned sets. It then introduces Ref-L4, a much larger REC benchmark (45,341 annotations, 365 categories, avg 24.2-word expressions, 22,813-word vocabulary) combining cleaned COCO-derived data with Objects365 data, and evaluates 24 LMMs with multi-threshold, scale-aware, and per-category analyses.

## Strengths

- **Quantified labeling noise in existing benchmarks and its impact**: The paper reports error rates of 14% (RefCOCO), 24% (RefCOCO+), 5% (RefCOCOg) and demonstrates that removing problematic instances yields consistent accuracy gains of 1.57–3.08 across five models (Table 2). This directly quantifies the contamination that prior work only speculated about.

- **Ref-L4's dramatically larger scale and lexical complexity**: Compared to RefCOCO/+/g, Ref-L4 offers 45,341 annotations (vs. 14,498–21,586), 365 categories (vs. 71–78), average expression length 24.2 words (vs. 3.6–8.4), and vocabulary of 22,813 words (vs. 3,525–5,050). These are genuine jumps that make the benchmark substantially more demanding (Table 3).

- **Comprehensive 24-model evaluation with multi-metric analysis**: Table 4 reports Acc₀.₅, Acc₀.₇₅, Acc₀.₉, and mAcc on both validation and test splits. Table 5 provides scale-aware (small/medium/large) breakdowns, and Figure 5 shows per-class accuracy across 365 categories. This granular analysis reveals non-obvious training biases (e.g., CogVLM-Grounding excels on small/medium but drops on large instances relative to SPHINX-v2-1k).

- **Explicit treatment of training-data leakage**: The paper includes Figure 10 breaking down performance on three subsets: COCO-derived, Objects365 with overlapping categories (O365-P1), and Objects365 with novel categories (O365-P2). The authors acknowledge that "most models are trained on the RefCOCO series" and show the expected accuracy gradient (COCO > O365-P1 > O365-P2).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **GPT-4V evaluation is anomalously low and not interpreted**: GPT-4V achieves only 9.91% Acc₀.₅ on Ref-L4 versus 55–82% for other models. The paper mentions the evaluation prompt is in the appendix but provides no discussion of why this result is so low, whether the evaluation protocol is fair to a general-purpose model not designed for bounding-box output, or whether the prompt format is responsible. Without interpretation, the reader cannot tell whether this reflects benchmark fairness or genuine model weakness.

- **Encouraging combined use of validation and test sets is non-standard**: The paper states "we encourage the combined use of both sets for model evaluation" (Section 3.3). Standard practice is to keep a held-out test set for final evaluation and use the validation set for development. Combining them conflates model selection and final assessment and means there is no held-out split for future evaluations that need an unbiased estimate.

- **Limited details about human annotation effort**: The paper states that generated referring expressions undergo "manual review" (Step-3) and "human review" during the expansion phase, but does not specify the number of annotators, their qualifications/ training, inter-annotator agreement, or quality-control measures. This makes it harder to assess the consistency and potential bias of the annotation process.

- **$\dagger$ notation changes meaning between tables**: In Table 2, $\dagger$ denotes "models fine-tuned on the specific dataset." In Table 3 (main results), $\dagger$ denotes "models that output segmentation masks." Using the same symbol for different meanings across tables is confusing and could mislead a reader scanning the results.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- The paper could report confidence intervals on the accuracy improvements from cleaning (Table 2) to strengthen the claim that differences are not noise, though this is not standard practice for large-scale REC evaluations.
- Additional qualitative examples of corrected labeling errors from RefCOCO/+/g would help readers ground the error rate statistics.
- A note on GPT-4V's output format: since the model does not natively produce bounding box coordinates, describing the parsing protocol would clarify the evaluation's fairness.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Labeling error analysis lacks methodological transparency"** (Harsh Critic's #1): The paper references Section~\ref{sec:label_error} and the specific error criteria are described (typos, misalignment, inaccurate bounding boxes). Further methodological details (annotation protocol, inter-annotator agreement) would be in the appendix (Section~\ref{sec:label_error}), which was stripped by the PDF parser. Per review guidelines, criticisms about missing appendix content that existed in the original submission are removed.

2. **"COCO data leakage is a fundamental design flaw"** (Harsh Critic's #2): The paper explicitly addresses training-data leakage in the "Evaluation on Diverse Data Sources" section (lines 329–336) and Figure 10, breaking down performance on COCO-derived vs. Objects365 subsets (O365-P1, O365-P2) and acknowledging "most models are trained on the RefCOCO series." The main results table reports combined metrics (standard practice), and the separate analysis is provided. This is a reasonable design choice adequately discussed, not a fundamental flaw.

3. **"GPT-4V generating descriptions could introduce systematic bias"**: This is a speculative concern about potential bias (GPT-4V's linguistic patterns influencing the benchmark). No evidence is presented that such bias exists, and the human-review step explicitly mitigates it. Removed as speculation.

4. **"High-resolution image bias"** (800px criterion): The harsh critic notes this "is not a flaw per se" — removed as non-critical.

5. **"Statistical significance missing"**: Confidence intervals are not standard for single-run benchmark evaluations in this field. Demoted to nice-to-have.

6. **"Vocabulary type-token ratio"**: A minor analytical suggestion, not a weakness.

7. **Various formatting/style nitpicks and generic "could be stronger" framing**: These are either parser artifacts, appendix gaps, or one-size-fits-all critique templates that fail to identify a specific problem in the paper as written.

## Novel Insights

The most interesting observation from the aggregation of reviews is that neither reviewer challenged the core empirical finding — that cleaning benchmark noise yields consistent 1.5–3 point gains across diverse LMM architectures — nor disputed that Ref-L4 is substantially harder than existing REC benchmarks. The substantive concerns revolve around evaluation protocol design (GPT-4V fairness, combined val+test usage), which are conventions that can be adjusted without altering the paper's fundamental contribution. The data-source breakdown (Figure 10) receives no criticism and is indeed the paper's strongest analytical asset, as it disentangles the confound of training-data familiarity from genuine REC capability.

## Suggestions

1. **Discuss the GPT-4V result explicitly**: Add a paragraph interpreting why GPT-4V scores 9.91% — is it a prompt issue, an output-format mismatch, or a genuine capability gap? If the evaluation protocol is suboptimal for GPT-4V, either adjust it or acknowledge the limitation.
2. **Designate a single held-out test set**: Instead of encouraging combined use, commit to one split (preferably the 70% test set) as the official evaluation set, with the validation set reserved for development.
3. **Clarify human annotation practices**: Even one sentence about the number of reviewers and annotation workflow would improve reproducibility.
4. **Disambiguate the $\dagger$ symbol**: Use different symbols for "fine-tuned on specific dataset" vs. "outputs segmentation masks" to avoid confusion across tables.

## Score and Decision

**Originality**: 7/10 — Cleaning existing benchmarks and creating a larger, more diverse one is a practical contribution that addresses a known need; the approach itself is not novel but the scale and thoroughness are.

**Importance of research question**: 8/10 — Benchmark saturation and noise are recognized issues in REC; providing cleaned versions and a harder benchmark fills a clear gap.

**Claims well-supported**: 7/10 — Most claims are well-supported by tables and figures; the error-rate claims rely on appendix details (stripped), and the GPT-4V result is unexplained.

**Soundness of experiments**: 8/10 — 24 models, multiple IoU thresholds, scale-aware and per-category analyses, data-source breakdown. Thorough by REC standards.

**Clarity of writing**: 7/10 — Well-structured and clear; the $\dagger$ notation inconsistency is a minor blemish.

**Value to community**: 8/10 — Cleaned RefCOCO sets and Ref-L4 will likely be adopted as evaluation resources; the 24-model comparison is immediately useful.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>