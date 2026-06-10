## Summary

This paper proposes DPTSC (Data Pre-processing Time Series Classification), a self-supervised pre-training and fine-tuning framework for time series classification. The claimed contributions include: (1) data preprocessing via platform filtering and a self-adaptive FIR filter, (2) a sorting-similarity function that replaces cosine similarity in the NT-Xent contrastive loss with a sorted-amplitude Hausdorff distance, and (3) a CNN-behind-transformer architecture to counter peak amplification. The paper claims extensive experiments on 8 real-world datasets demonstrating state-of-the-art performance across six metrics.

## Strengths

- **Sorting similarity as a concrete modification to contrastive learning for time series**: Section 4.5 proposes replacing cosine similarity in NT-Xent loss with a sorted-amplitude Hausdorff distance. This targets a genuine limitation of cosine similarity — that it measures only morphological alignment and not amplitude distance — and offers a computationally cheap alternative compared to DTW. The idea is identifiable and methodologically novel within the contrastive learning framework for time series.

- **CNN-behind-transformer architecture with a specific rationale**: Section 4.4 describes placing a CNN module after the transformer encoder to counteract peak amplification. The paper identifies a concrete failure mode (transformers amplify peak features, harmful for data with abrupt amplitude mutations) and provides a reasoning chain: transformer increases peak weight, CNN truncates the high-dimensional peak representation. This is domain-grounded and addresses a real architectural issue.

- **Self-adaptive FIR filter with a parameter-free cutoff**: Section 4.2 specifies a cutoff at √2/2 × max_frequency, avoiding manual tuning of filter parameters. This is a practical, principled choice that adapts to each curve's frequency content.

## Weaknesses

### Fatal

- **Section 5.3 ("EXPERIMENTS ANALYSIS") is completely empty — the paper contains zero experimental results.** The abstract claims "extensive experiments on 8 different real-world datasets" and contributions list claims superiority over state-of-the-art across accuracy, precision, recall, F1, AUROC, and AUPRC. However, lines 133–136 contain only a section header followed by empty space; no tables, figures, numerical values, or baseline comparisons appear anywhere in the paper. Table 1 (line 127) shows only dataset descriptions. The Discussion section (Section 6) speaks of results as if they exist but presents none. A new-method paper whose central claim is empirical superiority cannot be evaluated as a scientific contribution without presenting the evidence that would support its conclusions. This is not a matter of insufficient or weak evidence — the evidence is entirely absent. This single issue invalidates the paper's core claims regardless of any other merits or flaws.

### Major

- **Method description is critically underspecified across all components, making the approach non-reproducible.** 
  - *Platform filtering (Section 4.1)*: Consists of a single sentence fragment beginning with "5)." that states platform-like parts cannot simply be removed, but provides no definition of what constitutes a "platform," no detection criterion, no algorithm, and no pseudocode.
  - *Self-adaptive FIR filter (Section 4.2)*: The cutoff is stated as max_frequency × √2/2, but there is no explanation of how max_frequency is determined for a given time series, no filter order or window design, and pseudocode is omitted with "due to space limitations."
  - *Model architecture (Section 4.4)*: Described only as "a CNN module behind the transformer" following Zhang et al. (2022). No layer counts, kernel sizes, hidden dimensions, number of transformer layers, attention heads, or embedding sizes are reported.
  - *Missing equation*: Line 98 states the similarity formula is "given by equation 1 and 2," but only Equation 1 (a trivial sorting operation) appears in the paper. The actual similarity computation is never fully specified.
  - *Data augmentation*: "Image-like translation and flipping augmentations" are claimed (Section 4.1) but never defined for time series data.

- **Baselines are not named.** Section 5.1 states the paper "compare[s] 5 baseline algorithms" but never identifies them by name, explains why they were chosen, or describes their configurations. Combined with the absence of results, the reader cannot even know what the paper is being compared against.

- **Sorting similarity discards temporal structure without justification.** The core idea of sorting each time series by amplitude inherently reorders the time indices, destroying the temporal ordering. The paper claims this "preserves the time attribute" (line 106) but provides no explanation or evidence for how temporal information is retained after sorting. Since the method is proposed for time series classification — a domain where temporal ordering is typically essential — this is a significant conceptual gap that the paper does not address. The future work section (line 143) itself acknowledges that the loss similarity "needs to be re-constructed based on the characteristics of time series, rather than relying solely on sorting," which implicitly concedes this limitation.

### Minor

- **No ablation studies.** The paper proposes three distinct components (data preprocessing, sorting similarity, CNN-behind-transformer architecture) but provides no mechanism to disentangle their individual contributions. Even if results existed, the source of any performance gain would be unclear.
- **No hyperparameter reporting.** Learning rates, batch sizes, number of pre-training epochs, optimizer choices, and warmup schedules are absent. This further compounds the reproducibility concerns.

### Trivial

- None.

## Nice-to-Haves

- Full specification of all missing method details (platform filtering algorithm, FIR filter design parameters, complete model architecture with layer-by-layer parameters, Equation 2, and the definition of data augmentation for time series).
- Ablation studies isolating the contribution of each claimed component.
- Statistical significance measures (error bars, confidence intervals) for results.
- If the paper included results, naming and justifying baseline choices would be essential.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism about "RTX 3060 with 11GB" being an unusual specification / "i9-11900H is a laptop processor":** These are trivial hardware nitpicks that carry no weight in evaluating the scientific contribution. Removed per Hard Rules (trivial speculation).
- **Criticism about the ".4." artifact in Section 3 preliminaries:** This is a parser-induced formatting artifact from PDF extraction; the original submission does not have this issue. Removed per Hard Rules (formatting artifacts).
- **Criticism about the SleepEEG URL being correct:** This is not a weakness; it is a neutral observation. Removed per Filtering Discipline.
- **Strength about the problem being "important" or "timely":** Generic; not concrete or specific to this paper's evidenced contributions. Removed per Strength Finder filtering rules.
- **Strength about "well-motivated" framing:** Generic assessment without a specific anchor to the paper's content. Removed per Strength Finder filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel insight that the paper itself does not already claim; the primary finding is that the paper lacks the evidentiary basis for its own claims.

## Suggestions

The paper cannot be accepted in its current form due to the complete absence of experimental results. If the authors wish to resubmit, the highest-priority revisions are: (1) include all experimental results with full tables, baseline comparisons, and statistical variability; (2) fully specify every component of the proposed method so it can be understood and reproduced — the platform filtering algorithm, FIR filter design, complete model architecture, the missing Equation 2, and the definition of data augmentation for time series; (3) name and justify the baseline algorithms; (4) provide a conceptual justification for how the sorting similarity preserves temporal information, or modify the approach to address this tension; and (5) include ablation studies and hyperparameter details.

## Score and Decision

MY FINAL SCORE: <score>1</score>
MY FINAL DECISION: <decision>Reject</decision>