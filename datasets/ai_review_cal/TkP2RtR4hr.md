- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 5, 1, 3
Now I have a thorough picture. Let me produce the final consolidated review.

## Summary

This paper addresses the "level of manipulation" problem in text augmentation — balancing diversity against label reliability. It proposes two novelties: (1) a **logistic range-ratio equation** that uses cosine similarity between a seed sentence and candidate pool sentences to dynamically widen or narrow the candidate pool (controlling randomness/manipulation), and (2) a **combined sentence embedding** that fuses sentence-level BERT embeddings, a document-level embedding, and token-level SHAP (XAI) values to train a Bi-LSTM for pseudo-labeling augmented data. Experiments on three sentiment-classification datasets (IMDB, SEM-Eval17, YELP) with seven baselines show the method achieves the best performance on all three, though the YELP gain is very small (+0.65 percentage points).

## Strengths

- **Novel approach to controlling manipulation level**: The core idea of using the cosine similarity between a seed sentence and candidates to dynamically adjust the candidate pool size is genuinely novel. The range-ratio equation (Eq. 3) produces a value in (0,1) that controls what fraction of the sorted pool is available, creating a principled mechanism for trading off diversity vs. label reliability. This addresses a recognized gap in text augmentation.

- **Integration of XAI information into sentence embeddings for pseudo-labeling**: The idea of concatenating token SHAP values with sentence and document embeddings from BERT to create a 769-dimensional representation, then using a Bi-LSTM trained on these embeddings for pseudo-labeling, goes beyond simple weighted-sum or interpolation methods. This is a reasonable architectural contribution.

- **Consistent improvement over seven baselines on two of three datasets**: On IMDB (+2.18% average gain) and SEM-Eval17 (+3.0% average gain), the method produces clear improvements over EDA, WordNet, Back-Translation, SSMBA, AEDA, Pegasus, and NLP Albumentation. The low-resource setup (500 training samples, multiple augmentation sizes) is appropriate for the task.

## Weaknesses

### Fatal

None. The methodology is coherent, the equations are mathematically valid, and the experimental results (while incomplete) show positive trends.

### Major

1. **No ablation study isolating the two claimed novelties**. The paper proposes two distinct components: (i) the range-ratio-based systematic randomness assignment, and (ii) the combined sentence embedding (with SHAP) for pseudo-labeling. Every experiment uses both together, so there is no way to attribute the reported gains. A minimal ablation would include: (a) random pool selection without the range ratio, (b) plain sentence-BERT embeddings without SHAP/document information, (c) range ratio without the combined embedding. Without this, the core contribution is uninterpretable — the improvement could come from the larger, cross-document pool alone, independent of the logistic control mechanism.

2. **No statistical significance or variance reporting**. The paper states "All experimental results are averaged of 5 runs" but reports no standard deviation, standard error, confidence intervals, or any significance test. This is especially problematic because the YELP gain is only +0.65 percentage points — well within the range of random variation for 5 runs on a small (500-sample) training set. Without variance information, the reader cannot assess whether the improvements (particularly on YELP) are reliable.

3. **Ambiguous description of the augmentation algorithm**. Section 3.2.2–3.2.3 describes computing a "scaled input value x" based on a randomly selected sentence, then using the range ratio to "adjust the range" of the candidate pool. It is unclear whether the random sentence used to compute x is the same sentence ultimately selected, whether the range refers to a fraction of the sorted list (and if so, top or bottom), and how the final selected sentence is chosen from within that range. This ambiguity makes the method difficult to reproduce precisely.

### Minor

4. **The specific form of the range-ratio equation lacks justification and hyperparameter sensitivity analysis**. The equation uses a constant 10 in the denominator (rather than the standard 1 in a logistic function), and the hyperparameters are set to α=5, m=4.4 with no analysis of how these choices affect behavior or results. While the equation is mathematically valid (outputs in (0,1)), the paper provides no rationale for this specific parameterization and no sensitivity study showing whether results are robust to these choices.

5. **The document-level embedding E_D is confusingly described**. The paper states "For Document-level embeddings, we took the average, resulting in a 1-dimensional vector, E_D." It is unclear what is being averaged to produce a scalar. If it is the average of token embeddings, the result should be 768-dimensional, not 1-dimensional. If it is the average of SHAP values or logits, this needs clarification. This ambiguity undermines the description of the combined embedding.

6. **No evaluation of pseudo-label quality**. The paper claims the combined embedding produces "reliable pseudo-labels" but never measures pseudo-label accuracy against ground truth on a held-out set. The downstream task improvement alone cannot distinguish between better labels and simply having more training data. A direct analysis of pseudo-label correctness would strengthen the claims considerably.

7. **Baseline hyperparameter tuning not reported**. The paper states "we set up an experimental environment that was as close as possible" but does not specify whether baselines (EDA, WordNet, SSMBA, etc.) were tuned for the low-resource setting or used default parameters. Differences in hyperparameter choices could affect relative performance.

### Trivial

None.

## Nice-to-Haves

- Including a baseline that controls augmentation strength in a simpler manner (e.g., similarity-thresholded selection from the same cross-document pool, or tuned EDA probabilities) would more directly test whether the specific logistic range-ratio mechanism drives the improvement.
- Reporting per-augmentation-size breakdowns for each dataset (rather than only averages across sizes) would be more informative.
- The paper could benefit from analyzing the distribution of range-ratio values actually used during augmentation to show that the mechanism behaves as intended.

## Removed Points

These points were raised by reviewers but are removed after verification against the paper:

- **"Range ratio equation is mathematically suspect / not a standard logistic"** — Removed. The equation e^{10(αx-m)}/(10+e^{10(αx-m)}) is a valid sigmoid that outputs values in (0,1). The constant 10 merely shifts the midpoint. It is not mathematically incorrect. The concern about *justification* for the form is kept as a Minor weakness above.
- **"Circular augmentation procedure"** — Removed. The description is ambiguous (kept as Major weakness 3) but not circular. The algorithm first picks a seed, computes the range ratio from a random reference sentence, then selects from within the adjusted range. There is no logical circularity.
- **"Table 4 is missing"** — Removed. This is a PDF parser artifact; tables are present in the original submission.
- **"First study claim is overclaimed / prior work exists on controlling augmentation"** — Removed per instructions (cannot verify existence of prior work without external sources).
- **"Missing related works"** — Removed per instructions.
- **"Missing appendix / proofs"** — Removed per instructions (stripped by parser).
- Reproducibility nitpicks about undisclosed implementation details — Removed per instructions.
- **Strength: "Explicit handling of low-resource scenario"** — Removed as generic; 500 samples is common in low-resource augmentation literature.
- **Strength: "Acknowledgment of limitations"** — Removed as superficial; generic post-hoc acknowledgment.
- **Weakness: "YELP baseline comparison"** — The critic's request for baselines that "also modulate augmentation strength" is weakened to nice-to-have; the paper is comparing against standard augmentation methods, which is the standard practice.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the standard concerns (ablation, significance, clarity) but do not contribute a new interpretation or reframing of the work.

## Suggestions

1. **Run a four-condition ablation**: (i) full method, (ii) random pool selection without the range ratio, (iii) range ratio with plain sentence-BERT embeddings (no SHAP, no document embedding), (iv) combined embeddings without range ratio (e.g., pick uniformly from top-k similar sentences). This is essential to validate both claimed novelties.
2. **Report standard deviations** over the 5 runs and use a simple statistical test (e.g., paired bootstrap) to establish significance, especially given the small YELP gain.
3. **Provide pseudocode or a step-by-step numbered algorithm** for the augmentation loop, clarifying what "range" means (fraction of sorted list? top or bottom?) and how the final sentence is selected.
4. **Clarify the document embedding**: specify exactly what is averaged to produce the 1-dimensional E_D, and justify why a scalar is useful alongside a 768-dimensional sentence embedding.
5. **Add a sensitivity analysis** for α and m on at least one dataset, and justify the choice of 10 in the denominator or note that it is absorbed into the other parameters.
6. **Measure pseudo-label accuracy** against ground truth labels on a held-out subset to support the claim of "reliable pseudo-labels."
