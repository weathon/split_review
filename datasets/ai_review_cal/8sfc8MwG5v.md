- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 5, 5, 6
Now I have all the evidence needed to verify claims against the paper. Let me produce the consolidated review.

## Summary

This paper proposes CONDA, a test-time adaptation (TTA) framework for Concept Bottleneck Models (CBMs) paired with foundation models (FMs). It identifies three failure modes of CBMs under distribution shifts (non-robust bottleneck, non-robust classifier, incomplete concept set) and designs three corresponding adaptation components: Concept-Score Alignment (CSA), Linear Probing Adaptation (LPA), and Residual Concept Bottleneck (RCB). Experiments across five datasets with multiple CBM construction methods show accuracy gains of up to 28% over unadapted CBMs.

## Strengths

- **Formal categorization of distribution shifts and failure modes** (Sections 2.2–2.3): The paper formally defines low-level and concept-level shifts (Eqns. 2–3) and maps them to three concrete failure modes. This theoretical grounding directly motivates the three-component design and is not merely decorative — the ablation study (Figure 3, described in Section 4.3) empirically confirms that CSA is critical for low-level shifts while LPA/RCB drive improvement under concept-level shifts, supporting the design rationale.

- **Consistent accuracy gains across diverse settings** (Table 1, Section 4.2): CONDA improves test-time accuracy over the unadapted CBM on five datasets (CIFAR-C, Waterbirds, Metashift, Camelyon17) using three different CBM construction methods (PCBM, unsupervised, GPT-3), and the adapted performance often matches or exceeds non-interpretable baselines (zero-shot, linear probing).

- **Generality across FM backbones and CBM construction methods**: The framework is evaluated with CLIP:ViT-L/14 (standard and adversarially robust variants), BioMedCLIP, and three distinct concept-bottleneck construction approaches (Section 4.1), showing the method is not tied to a specific backbone or concept-generation technique.

- **Robust pseudo-labeling strategy** (Section 3): The ensemble of zero-shot and linear-probe predictions for pseudo-labeling leverages the FM's pre-trained robustness, avoiding naive self-labeling that would suffer from shift-induced errors. The paper notes that more sophisticated methods could further improve this.

## Weaknesses

### Fatal
None.

### Major

- **No comparison against existing TTA methods adapted to the CBM pipeline.** The evaluation compares CONDA only against unadapted CBMs, zero-shot prediction, and linear probing — none of which are test-time adaptation methods. Existing TTA approaches (e.g., TENT / entropy minimization on the CBM's linear probe, batch-norm adaptation, or self-supervised consistency) could be straightforwardly applied to the CBM pipeline without adding concept-vector adaptation or residual branches. Without these baselines, the reader cannot assess whether CONDA's multi-component design yields gains over simpler alternatives, or whether the 28% improvement reflects any TTA method's benefit versus specifically CONDA's design. The paper's central claim of being "the first approach for TTA of concept bottlenecks" (line 37) does not exempt it from this comparison. This is the most consequential gap in the evaluation.

### Minor

- **Interpretability evidence is only qualitative and anecdotal** (Section 4.4). The claim that RCB captures concepts "missed during the initial construction" rests on a single example (Waterbirds) showing concept weight shifts and an assertion that three of five residual concepts correspond to "feathers, wings, and beak." No methodology is provided for how residual concepts were labeled or validated. No quantitative interpretability metric (concept purity, intervention accuracy, human evaluation) is used. This weakens the paper's secondary contribution.

- **Gaussian assumption for concept-score distributions is untested** (Section 3.1). CSA models class-conditional concept scores as multivariate Gaussians and uses Mahalanobis distances for alignment. The paper does not validate this assumption (e.g., normality tests, visualizations of concept score distributions) or study sensitivity to violations. If concept scores are multimodal or heavy-tailed, the CSA objective may not align distributions as intended.

- **Pseudo-label quality is not analyzed** (Section 3). The method's success depends on pseudo-label accuracy across all three adaptation stages, but the paper does not study how results vary with pseudo-label quality (e.g., comparison to oracle labels, measuring pseudo-label accuracy on the test set, or diagnosing when the ensemble strategy fails). The paper acknowledges better methods exist but does not evaluate whether its approach is sufficient.

- **Failure mode taxonomy is partially non-operationalized.** Definition 1 ("complete concept set") is stated but never measured or empirically verified — the paper does not quantify whether any concept set is complete or detect whether incompleteness actually occurs in the datasets before applying RCB. The connection between the theoretical taxonomy and empirical results is asserted but not directly tracked (e.g., by measuring concept-score distribution divergence before and after shift, then showing the corresponding CONDA component mitigates it).

- **No error bars, confidence intervals, or statistical significance tests reported.** Given the stochastic nature of online test-time adaptation (random batch splits, sequential adaptation), variance across runs should be reported. This is a standard expectation for empirical papers in this area.

- **Choice of backbone is not justified** (Section 4.1). The paper uses adversarially robust CLIP for CIFAR, standard CLIP for Waterbirds/Metashift, and BioMedCLIP for Camelyon17. Different backbones have different robustness properties, and the choice could affect the relative gains. The paper does not discuss this or show robustness to backbone selection.

### Trivial
None.

## Nice-to-Haves

- A comparison against CAFA (Jung et al., 2023) applied directly to concept scores rather than feature representations would clarify the nontriviality of the CSA adaptation.
- An analysis of whether residual concepts genuinely capture *new* discriminative information (beyond what the cosine-similarity regularization penalizes) would strengthen the RCB contribution.
- Sensitivity analysis for key hyperparameters (λ_frob, λ_sparse, λ_sim, λ_coh, number of residual concepts r) would help assess brittleness.
- A study on how results vary with test batch composition and size.
- Scalability discussion: computing Mahalanobis distances with a full covariance matrix (inverted) per class could be expensive for large m (number of concepts).

## Removed Points

- **Criticism about missing hyperparameter values (λ's, learning rates, batch sizes, optimization steps) in the main text:** Per the rules, minor reproducibility nitpicks about undisclosed hyperparameters are removed as they concern implementation details that are appropriately deferred to supplementary material or a code release, and the paper provides a link to an anonymized repository.
- **Criticism about missing appendix / supplementary:** The parser strips these sections from all papers; they exist in the original submission.
- **Criticism that "Definition 1 is never used later" in an absolute sense:** The paper does use the three failure modes (including incomplete concept set) to motivate RCB, and the ablation study shows RCB helps under concept-level shifts. The definition's non-operationalization is retained as a minor weakness (see above) rather than a fatal gap.
- **Criticism that CSA harmfulness under concept-level shifts is unexplained:** The ablation actually reports the observation (Section 4.3) and provides a reasonable explanation referencing Lee et al. (2023) about fine-tuning different layers for different shift types.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the failure-mode taxonomy cleanly maps to the component design — and that this mapping is empirically validated through the component ablation — is reflected in the strengths above but is essentially the paper's own framing.

## Suggestions

1. **Add TTA baselines.** The single most impactful revision would be to compare CONDA against standard TTA methods adapted to the CBM pipeline: TENT (entropy minimization on the CBM's linear probe), prediction-layer-only adaptation via pseudo-label cross-entropy, and possibly SHOT or TTAC applied to the CBM's components. This would establish whether CONDA's multi-component design is actually necessary.

2. **Quantify interpretability gains.** Provide quantitative metrics for the concept-level analysis — e.g., concept purity (percentage of top-activating images matching the concept), intervention accuracy, or human-rated coherence of residual concepts — for at least the main datasets.

3. **Validate the Gaussian assumption.** Show concept score histograms or Q-Q plots from the source domain, and optionally compare CSA's alignment performance to a non-parametric alternative (e.g., MMD-based alignment). If the assumption holds poorly, discuss how this affects the method.

4. **Report error bars.** Run each experiment multiple times with different random batch splits and report means and standard deviations (or confidence intervals) for the key results in Table 1 and Figure 3.

5. **Analyze pseudo-label quality.** Report pseudo-label accuracy on the test set (when labels are known for evaluation) and compare the ensemble strategy to simpler alternatives (e.g., using only zero-shot or only linear-probe pseudo-labels).
