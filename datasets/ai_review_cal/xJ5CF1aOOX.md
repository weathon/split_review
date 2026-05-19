- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 3, 3, 1
I now have all the information I need. Here is the consolidated final review.

---

## Summary

This paper proposes DPTSC, a self-supervised pre-training framework for time series classification. The method introduces three components: a "platform filtering" and self-adaptive FIR filter for data pre-processing, a sorting-based similarity (replacing cosine similarity in the NT-Xent loss) that sorts time series by amplitude and computes Hausdorff distance, and a CNN+transformer architecture inspired by prior work. The paper claims state-of-the-art results across 8 datasets, but **the experimental results section (Section 5.3) is entirely empty** — no tables, figures, or numerical data are presented. Without this core evidence, the paper's central claims are unverifiable.

## Strengths

- **Novel sorting similarity using Hausdorff distance on sorted values**: Section 4.5 proposes replacing cosine similarity in the NT-Xent loss with a similarity computed by sorting each time series by amplitude and measuring the Hausdorff distance between the sorted sequences. This is a concrete, novel idea for handling cases where large intra-class morphological differences cause cosine similarity to fail. The general approach of using distributional similarity (via sorting) for time series contrastive learning is a distinctive design choice.

- **Self-adaptive FIR filter (SAFF)**: Section 4.2 describes a low-pass FIR filter whose cutoff frequency is automatically set to \( \sqrt{2}/2 \) times the maximum frequency of the current curve. The concept of adapting filter parameters to each sample's spectral content is a reasonable direction for reducing manual pre-processing tuning.

- **Problem formulation**: Section 3 formally defines the two-stage setup (unlabeled pre-training dataset \(\mathbb{T}\), small labeled fine-tuning dataset \(\mathbb{T}'\)), which provides clear framing for the self-supervised pre-training + fine-tuning paradigm.

## Weaknesses

### Fatal

- **Experimental results are completely absent.** Section 5.3 ("Experiments Analysis") exists only as a section heading — there is no content between it and Section 6 (Discussion). The paper claims in its contributions (line 21) that "extensive experiments on 4 groups of 8 real data sets show that our proposed method has better accuracy, precision, recall, F1 score and AUROC and AUPRC, than the state-of-art," yet provides zero evidence. No tables, figures, numerical comparisons, or statistical analyses are presented anywhere in the manuscript. Without experimental results, the paper's core claims cannot be assessed, reproduced, or verified. This is a structural incompleteness that makes the paper unpublishable in its current form.

### Major

- **The sorting similarity discards temporal structure without justification.** Section 4.5 sorts each time series by amplitude, thereby removing all temporal ordering. The paper asserts that this "preserves the time attribute while retaining the graphic features of the time series" (line 106), but this claim is unexplained and arguably contradictory. For many time series classification tasks (EEG, gesture recognition, bearing vibration), temporal dynamics are the primary discriminative signal. Using a sorting-based similarity means two samples with very different temporal patterns but similar amplitude distributions would be deemed similar in the embedding space. The paper provides no theoretical analysis, toy example, or empirical evidence to show when this similarity is beneficial versus harmful, nor does it address which types of time series would be appropriate for this approach.

- **Critical methodological details are undefined.** Several components are referenced but never specified:
  - **"Platform filtering"** (Section 4.1) is not defined. The section consists of a single incomplete sentence. What constitutes a "platform" in quantitative terms, what the "winscale value" (referenced in Section 4.3) is, and how the procedure operates are never explained.
  - **The fine-tuning loss function** is promised in the abstract ("our sorting loss function is used in the fine-tuning stage") and contributions (line 20), but Section 4.5 only defines the similarity for contrastive pre-training. The actual loss used during fine-tuning is never specified.
  - **The baseline algorithms** against which the method is compared are never named. Line 118 states "compare 5 baseline algorithms" without identifying them, so the reader cannot judge whether the claimed comparisons are against state-of-the-art methods or weak baselines.
  - **The SAFF cutoff computation** is given as \(\sqrt{2}/2 \times\) "maximum frequency of the current curve" (line 68), but no method is provided for computing the "maximum frequency" of a sample, nor is the choice of \(\sqrt{2}/2\) motivated.
  - **"4 pairs of datasets"** (line 118) is mentioned but never explained — it is unclear which datasets are paired for pre-training and fine-tuning.

- **The model architecture motivation is asserted without evidence.** Section 4.4 states that "CNN weakens the impact of peaks, while the transformer increases the weight of the peak part" as a rationale for embedding CNN behind the transformer. This claim is presented as fact with a citation to prior work (Li et al., 2021), but no analysis, ablation, or experiment in the current paper supports or tests this behavior. Even the referenced prior work is not described in a way that connects to this specific architectural choice.

### Minor

- **Hyperparameter settings are not reported.** The paper does not specify learning rate, batch size, number of epochs, architecture dimensions, optimizer choice, or any training hyperparameters — even though it claims to have run experiments (line 118: "All experimental results were obtained by running three times and taking the average value").

- **Single-channel assumption conflicts with listed datasets.** Line 47 states "we focus only on data from a single channel," but several of the 8 datasets listed in Section 5.2 (e.g., SleepEEG with EOG, EEG, and EMG signals; HAR with smartphone sensor data) are multivariate. It is unclear how the method handles or is applied to such data.

- **Related works section reads as a catalogue rather than a targeted analysis** that identifies specific gaps motivating the proposed design choices. The transition from discussing limitations of prior work to explaining why the sorting similarity or CNN+transformer architecture addresses those limitations is not drawn.

### Trivial

- None that are substantive to call out beyond the issues already listed.

## Nice-to-Haves

- Provide pseudocode or algorithmic descriptions for platform filtering and the adaptive FIR filter to improve reproducibility.
- Include an ablation study isolating the contribution of each component (platform filtering, SAFF, CNN module, sorting similarity).
- Report standard deviations and statistical significance tests for the (missing) experimental results.
- Explain why sorting similarity might preserve class-relevant information despite discarding temporal order, e.g., via a toy example or theoretical argument.

## Removed Points

- **"Comprehensive evaluation setup" (from Strength Finder)**: The paper lists metrics and datasets, but since no actual evaluation results are presented, calling the setup a "strength" is misleading. The setup is described; the evaluation was not conducted (in the manuscript). This is not a strength of the paper as submitted.

- **Criticism about code not being referenced** (from Harsh Critic's "Missing Parts"): Subsumed by the far more fundamental problem that no results exist to reproduce. Not independently actionable.

- **"The method is not reproducible because pseudocode is omitted"** (from Harsh Critic): While the paper is too vague, the explicit statement "Due to space limitations, we will omit the pseudocode" (line 68) indicates this was a formatting choice. The deeper problem is that even the prose description is incomplete.

## Novel Insights

The harsh critic's detailed analysis correctly identified that the sorting similarity is conceptually misaligned with time series tasks where temporal structure is critical. This is a genuinely insightful observation: the paper proposes a similarity designed to be invariant to temporal warping (by sorting amplitudes) while claiming to improve time series classification — but it never addresses the obvious tension. The Strength Finder's identification of the sorting similarity as a specific, concrete contribution is also accurate: it is a distinctive technical proposal. The conflict between these two observations (novel idea vs. unaddressed conceptual gap) is the paper's central tension, but without experimental results neither the usefulness nor the harmfulness of the approach can be determined.

## Suggestions

1. **Foremost: present complete experimental results.** Without tables showing accuracy, precision, recall, F1, AUROC, and AUPRC across all datasets with comparisons to named baselines, the paper cannot be evaluated.
2. **Clarify the sorting similarity.** Provide a rigorous justification — with examples — for how discarding temporal order via amplitude sorting can still yield class-discriminative representations. Alternatively, reframe the approach as distributional similarity and evaluate it on tasks where amplitude distributions are known to be discriminative.
3. **Define all pre-processing steps algorithmically.** This includes platform filtering (with a quantitative definition of "platform" and "winscale"), the maximum frequency computation for SAFF, and the fine-tuning loss function.
4. **Name the baselines** and ensure they are appropriate state-of-the-art competitors for the chosen datasets.
5. **Add ablation studies** to isolate the effect of each claimed contribution.
