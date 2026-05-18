Now I have a complete picture. Let me produce the final consolidated review.

---

## Summary

The paper proposes DPTSC, a self-supervised pre-training model for time series classification that combines data pre-processing (platform filtering + self-adaptive FIR filter) with a sorting-based similarity to replace cosine similarity in the NT-Xent contrastive learning framework. The model uses a dual-encoder (time/frequency domain) Transformer with a post-encoder CNN module. The paper claims extensive experiments on 8 real-world datasets across 5 metrics.

## Strengths

- **Novel data pre-processing pipeline targeting real-world time series non-idealities**: The paper identifies that industrial time series data often contains "platform-like" segments and amplitude spikes that confuse standard contrastive learning methods, and proposes dedicated filtering strategies (platform filtering and a self-adaptive FIR filter) to address them. This problem formulation is well-motivated even if the implementation description is lacking.

- **Sorting-based similarity as an alternative to cosine similarity in NT-Xent**: The core idea — sorting waveforms by amplitude and computing distance on the sorted ordering to handle intra-class morphological variation — is an interesting departure from standard cosine-similarity-based contrastive learning. The motivation (cosine similarity fails when the same class has different waveform shapes) is clearly stated.

- **Dual-encoder architecture with CNN post-processing**: The combination of a Transformer (which amplifies peak features) followed by a CNN (which suppresses excessive peak feature extraction) is a plausible architectural response to the specific challenge of time series with abrupt amplitude changes (e.g., bearing fault data).

## Weaknesses

### Fatal

1. **No experimental results are reported anywhere in the paper.** Section 5.3 ("Experiments Analysis") consists of only the section heading with no content. Section 6 ("Discussion") merely asserts *"our algorithm performs better than other algorithms"* qualitatively without a single numerical comparison — no accuracy, precision, F1, AUROC, or AUPRC values. The paper describes the experimental setup (8 datasets, 5 baselines, 5 metrics, 3 runs) but never presents any outcomes. For an empirical paper whose third claimed contribution is *"extensive experiments ... show that our proposed method has better accuracy, precision, recall, F1 score and AUROC and AUPRC, than the state-of-art,"* the complete absence of results data means the paper's central claim is entirely unsupported. This alone is a fatal flaw that makes the paper unpublishable in its current form.

### Major

2. **Critical method components are severely underspecified.** The paper's contribution is a new method, yet several components cannot be understood or reproduced from the provided description:
   - **Section 4.1 (Platform Filtering):** Consists of a single incomplete sentence starting with *"5). For example..."* (suggesting points 1–4 are missing) that does not define what a "platform" is, how to detect one, or any algorithmic steps.
   - **Section 4.2 (Self-Adaptive FIR Filter):** The cutoff frequency is set to *"the maximum frequency of the current curve multiplied by √2/2"* without specifying how "maximum frequency" is computed from the curve. The paper explicitly states pseudocode is omitted due to space (line 68).
   - **Section 4.4 (Model Structure):** The CNN placed after the Transformer is described only conceptually (*"CNN cuts off the high-dimensional features"*) with no architectural details — number of layers, kernel sizes, pooling, dimensionality, or how the time-domain and frequency-domain branches are recombined.
   - Without these specifics, the method cannot be built, compared against, or independently verified.

3. **The sorting similarity mechanism is poorly specified and potentially self-contradictory.** The paper states that sorting the time series *"preserves the time attribute"* (line 106), but sorting by amplitude destroys temporal ordering — if the method retains the original x-axis coordinates as ordered pairs, this needs to be stated explicitly and the distance formula clarified. Further, the integration with the NT-Xent loss is ambiguous: does the sorting-based distance replace cosine similarity in the pre-training stage, the fine-tuning stage, or both? The paper says *"a rough similarity is used in the pre-training stage, while our sorting loss function is used in the fine-tuning stage"* (abstract), but Section 4.5 never formalizes this distinction or specifies the loss function.

### Minor

4. **The writing quality impedes comprehension throughout.** The prose contains numerous unclear passages (e.g., *"The transformer precisely increases the weight of the peak part of the data, while the CNN cuts off the high-dimensional features of the data to prevent the extraction of too many peak part features"*) and grammatical issues that collectively hinder the reader's ability to assess the technical merit of the proposal. While individual grammatical issues are minor, the aggregate effect is substantive for a paper whose main contribution is a new method.

5. **The paper does not clearly articulate how its proposed components address the stated limitations of prior work.** The Related Works section identifies that existing contrastive learning methods have *"higher requirements for the form and regularity of data"* and that there are *"issues with intra-class offsets and non-standard data,"* but it never traces a clear causal chain from these problems to the specific design of the platform filter, SAFF, or sorting similarity. The method reads as a collection of loosely motivated components rather than a targeted solution.

### Trivial

- The formulas in Section 4.5 contain formatting issues (e.g., `s o r t` rendered with spaces, incomplete parentheses in the text).
- Table 1 (dataset information) is an image placeholder with no tabular content visible in the extracted text.

## Nice-to-Haves

- Providing pseudocode for the SAFF algorithm rather than deferring it would significantly improve reproducibility.
- Architectural details of the CNN (layers, kernel sizes, dimensionality) would allow the method to be reproduced.
- Clarifying whether the sorting similarity is used in pre-training, fine-tuning, or both, and how it replaces the cosine term in NT-Xent, would resolve the current ambiguity.

## Removed Points

- **Criticism about missing Algorithm 2 / appendix content for Section 4.3**: The paper references "pseudocode is shown in Algorithm 2" which may have been in a section stripped by the parser. Removed per hard rules.
- **Criticism about missing hyperparameters / trivial implementation details**: The reviewer's request for extensive hyperparameter disclosure goes beyond what is reasonable for a conference submission. Downgraded.
- **Strength Finder's claim about "comprehensive evaluation on 8 datasets with 5 metrics outperforming baselines"**: This strength is factually inaccurate — the paper does not report any experimental results. Removed.
- **Strength Finder's generic phrasing about the paper addressing "an important problem"**: Generic strength without specific evidence. Removed.
- **Criticism that the paper should also cover additional domains/datasets beyond the 8 listed**: This is scope creep; 8 datasets across diverse domains is a reasonable set.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel perspective that the paper itself does not already claim.

## Suggestions

- **Report all experimental results as a minimally necessary condition for an empirical paper.** This means populating Section 5.3 with numerical tables showing accuracy, precision, F1, AUROC, and AUPRC for all baselines on all 8 datasets, with standard deviations.
- **Rewrite the methodology section to provide complete algorithmic descriptions.** Each component (platform filtering, SAFF, sorting similarity, CNN placement) needs an unambiguous specification that would allow a competent researcher to implement it without guessing.
- **Clarify the sorting similarity mechanism.** Explain exactly how temporal information is preserved after amplitude sorting, how the Hausdorff distance is computed on the sorted representation, and precisely how this replaces or augments cosine similarity in the NT-Xent loss during each training stage.
- **Tighten the problem-to-solution narrative.** For each proposed component, state the specific failure mode in prior work it addresses and how it addresses it, rather than listing components alongside generic critiques of the literature.

## Score and Decision

The paper as submitted does not meet the standard for publication. The absence of any experimental results is fatal — a paper that claims empirical superiority over baselines but provides zero numerical evidence cannot be accepted. Additionally, the method description is critically incomplete across multiple sections, making the contribution unverifiable even in principle. These issues are not fixable within minor revision; the paper would need to supply complete experimental results and substantially rewrite the methodology section. 

MY FINAL SCORE: <pineapple>2.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>