- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5
Now I have all the information needed. Let me produce the consolidated final review.

---

## Summary

This paper proposes Set-MI, a method that improves membership inference (MI) for language models by aggregating individual document-level predictions over sets of documents expected to share membership status (all members or all non-members). The authors construct five new MI benchmarks across diverse domains (Wikipedia, Arxiv, Language, License, Instructions) and demonstrate that averaging individual MI scores over documents within sets raises AUROC by 0.14 on average across four baseline MI methods. Additional analyses examine the effects of model size, deduplication, document length, set size, and robustness to noise in the set assumption.

## Strengths

- **Consistent improvement across all 20 comparisons (Table 2):** Set-MI outperforms the corresponding Individual-MI method in every method–benchmark combination, with an average gain of 0.14 AUROC. This supports the core claim that set aggregation reliably enhances prior MI methods, not just in isolated cases.

- **Diverse benchmark suite with clean ground truth on three of five benchmarks:** Section 4 constructs five benchmarks (Wikipedia, Arxiv, Language, License, Instructions). The Language, License, and Instructions benchmarks have unambiguous ground-truth membership determinable directly from the target model's known training data (supported by lines 111–115), providing strong evidence independent of the two benchmarks that rely on a date proxy.

- **Controlled robustness analysis with actionable guidance (Section 6, Figure 5):** The paper systematically varies noise ratios (0.0–0.9) in member and non-member sets, compares MAX, MIN, and FULL aggregation strategies, and finds all three outperform Individual-MI under noise. Specific recommendations are given (e.g., MAX when noise is in member sets, MIN when in non-member sets, FULL when both are noisy), which goes beyond a simple claim of robustness.

- **Informative ablations on factors affecting Set-MI effectiveness:** Figure 3 shows Set-MI gains increase with model size (70M to 12B) more sharply than Individual-MI, and that the gap between duplicated and deduplicated training data is larger with Set-MI. Figure 4 shows even a set size of 3 provides meaningful gains. These give practical insight into when Set-MI is most beneficial.

- **Forward-looking insight from the Individual-MI / Set-MI correlation (Section 5.1):** The paper reports a correlation of 0.824 (p=0.0002) between base Individual-MI and resulting Set-MI AUROC scores, suggesting future improvements to individual-level methods would compound into further gains for Set-MI.

## Weaknesses

### Fatal
None.

### Major

- **Unvalidated date proxy for ground-truth membership on Wikipedia and Arxiv benchmarks (Section 5, lines 107–109):** The paper labels documents as members if their creation date falls before the Pile's data collection cutoff. However, the Pile is a filtered subset — not every pre-cutoff Wikipedia article or Arxiv paper is included. Documents labeled as members may actually be non-members (if excluded by the Pile's filtering), and vice versa. This means: (1) some sets that are assumed to satisfy the set assumption may contain mixed-membership documents, (2) the reported AUROC improvements on these two benchmarks could be inflated or attenuated depending on how the proxy errors interact with the MI signal. The robustness test in Section 6 simulates random noise but starts from a "clean" version (13-gram overlap verified), so it does not validate the proxy itself. The core claim is still supported by the three clean benchmarks (Language, License, Instructions), but the Wikipedia and Arxiv numbers are less trustworthy without validation against actual Pile membership (e.g., by document hash or n-gram overlap).

- **No uncertainty quantification for main results (Table 2):** The paper reports single-point AUROC estimates without standard deviations, confidence intervals, or any measure of variance across random subsamples of sets and documents. Given that the benchmarks are constructed by subsampling, the numerical values have inherent variability. The absence of error bars makes it impossible to assess whether fine-grained differences (e.g., between methods or benchmarks) are reliable or could shift substantially under a different random draw.

### Minor

- **Robustness analysis limited to one MI method and one benchmark (Section 6):** The controlled noise experiment uses only Loss Attack on Wikipedia. While informative, the generalizability of the aggregation recommendations (MAX vs. MIN vs. FULL) to other MI methods (e.g., Min-K% Prob, LiRA) and other domains (e.g., Arxiv, License) is unknown. An additional test with at least one more MI method would substantially strengthen the claim.

### Trivial
None.

## Nice-to-Haves

- **Random-set baseline:** The paper already compares Individual-MI vs. Set-MI with meaningful groupings. An additional control experiment grouping documents into random sets (unrelated to any shared attribute) would confirm that the improvement is due to the semantic validity of the set assumption, not merely the variance reduction from averaging noisy scores.
- **Validate the date proxy directly:** For Wikipedia and Arxiv, the authors could quantify the mismatch rate between date-based labels and actual Pile membership (via 13-gram overlap, as already done in Section 6). If the mismatch rate is low, the proxy is validated; if high, the paper should report results both with and without the proxy.

## Removed Points

- *"The paper does not discuss the cost of obtaining the metadata needed to construct sets."* — **Removed (factually incorrect).** The paper explicitly addresses this in the conclusion (lines 182–183): *"Our work makes an assumption that the metadata about the dataset of interest (D) is available... We highlight that this may not always be the case in practical MI scenarios, and leave relaxing this assumption for future work."*
- *"No comparison against a baseline of averaging the loss over sets without set-based refinement."* — **Removed (misunderstands the method).** Set-MI is precisely averaging over sets; the Individual-MI vs. Set-MI comparison is exactly this comparison. The suggestion to use random sets is a different control experiment (moved to Nice-to-Haves).
- *"The OCR garbles the table"* and other formatting observations. — **Removed (parser artifacts are not errors in the original submission).**

## Novel Insights

The harsh critic raises one genuinely novel observation not articulated by the paper itself: the noise robustness experiment (Section 6) constructs a "clean" version of Wikipedia using 13-gram overlap verification, yet the main experiments (Section 5) for the same benchmark use a coarser date-based proxy. The fact that the authors already have the infrastructure to determine actual membership (used in Section 6) but opted for the date proxy in the main experiments is an inconsistency worth resolving — it is unclear whether this was done for scalability reasons or because 13-gram matching is more expensive. If the 13-gram approach was feasible for the main experiments, using it would eliminate the proxy concern entirely.

## Suggestions

1. **Validate the date proxy** on Wikipedia and Arxiv by computing actual membership (via 13-gram overlap with the Pile, as in Section 6) for a random sample of documents. Report the mismatch rate and, if feasible, re-run the main experiments with corrected labels.
2. **Report error bars** (standard deviations over multiple random subsamples of sets and documents) for Table 2 and the main figures. Even a single sentence describing the number of random trials and the observed range would substantially improve confidence.
3. **Extend the robustness analysis** (Section 6) to at least one additional MI method (e.g., Min-K% Prob) to verify that the MAX/MIN/FULL recommendations generalize beyond Loss Attack.
