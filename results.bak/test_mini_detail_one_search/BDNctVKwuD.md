Now I have sufficient calibration. Let me write the final consolidated review.

---

## Summary

The paper identifies a theoretical limitation of HiResCAM explanations — they are not uniquely determined due to softmax shift-invariance, which can be amplified to an arbitrary matrix shift M (Theorem 3.2). To address this, the authors propose ContrastiveCAMs, which are invariant to M and provide granular class-versus-class explanations (Theorem 3.5). Using ContrastiveCAMs, they then develop Core-Focused Cross-Entropy (CFCE), a loss that penalizes non-core region contributions and encourages feature alignment. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC demonstrate that CFCE-trained models improve alignment metrics and downstream segmentation performance.

## Strengths

1. **Novel theoretical result: HiResCAM non-uniqueness (Theorem 3.2).** The paper proves that HiResCAM explanations admit an arbitrary matrix shift M without changing the predicted probabilities. This is a clean, rigorous identification of a fundamental limitation of a widely-used explanation method, and prior work had not formalized it.

2. **Principled resolution via ContrastiveCAMs (Theorem 3.5).** ContrastiveCAMs are shown to be invariant to the spurious M-shift, providing a principled way to recover faithful attention maps. The construction is simple and the invariance proof is straightforward. The additional class-versus-class granularity is a useful byproduct.

3. **Proposition 4.2 + Remark 4.3: theoretical basis for why cross-entropy does not penalize non-core features.** The paper decomposes CE loss into core and non-core ContrastiveCAM contributions, formally showing that CE does not inherently incentivize core-region attention. This provides a theoretical explanation for shortcut learning that goes beyond empirical observation.

4. **Strong results on Hard-ImageNet using an independent alignment metric.** The paper reports **GradCAM IoU** (not ContrastiveCAM IoU) for Hard-ImageNet: CFCE+KL raises it from 16.25% (CE w/ Arch) to 51.52%. Since the loss directly operates on ContrastiveCAM, not GradCAM, this provides independent evidence that the method genuinely improves feature alignment. Relative Foreground Sensitivity also flips from negative (−0.23) to positive (+0.236).

5. **Downstream segmentation improvements on PASCAL VOC.** CFCE+KL-trained backbones improve segmentation IoU across most classes in both fine-tune and end-to-end settings. This demonstrates that the alignment gains transfer to a different task, providing further validation beyond the primary metric.

6. **Practical viability with approximate masks.** The method works competitively with auto-generated SAM masks and bounding-box supervision on Oxford-IIIT Pets (e.g., 83.54% IoU with SAM masks in binary setting), demonstrating robustness to imperfect supervision and practical deployability.

## Weaknesses

### Major

- **IoU metric unspecified for Oxford Pets and PASCAL VOC (Tables 3, 4).** The paper's alignment evaluation for Pets and PASCAL reports only "IoU (%)" without stating which explanation method (GradCAM, ContrastiveCAM, or other) was used to compute it. For Hard-ImageNet the paper explicitly reports GradCAM IoU and separates it from ContrastiveCAM IoU, establishing independent validation. The Pets and PASCAL tables lack this crucial detail. If the IoU was computed using ContrastiveCAM — the same explanation the CFCE loss directly penalizes and the KL term explicitly fits — then the headline numbers (e.g., 93.12% IoU on Pets valid set with CFCE+KL) conflate the training objective with the evaluation metric. The authors must specify and, at minimum, also report GradCAM or another independent IoU metric for these datasets.

- **KL regularization on binary masks is underspecified.** Definition 4.7 applies softmax to `λ₂H` where `H` is a binary mask. The per-spatial-location semantics of this operation are not explained — it is unclear how softmax normalizes a binary value at each spatial position. The three hyperparameters `λ₁, λ₂, λ₃` receive no sensitivity analysis.

### Minor

- **Figure 3's `ℒ_core` and `ℒ_Non-Core` values are undefined.** The table embedded in Figure 3 reports numerical values labeled `ℒ_core` and `ℒ_Non-Core` for CE and CFCE models. These quantities are never formally defined in the paper text (e.g., which classes they are summed over, what normalization is applied). This makes the quantitative comparison in the figure unreproducible as written.

- **Accuracy drop on Hard-ImageNet not discussed as a trade-off.** CFCE reduces unablated accuracy from ~94% (CE/CE w/ Arch) to ~90% (CFCE+KL), a ~4-point drop. While core-region ablation accuracy and alignment improve dramatically, the paper does not explicitly discuss whether this accuracy trade-off is acceptable or how practitioners might navigate it.

- **Hyperparameter sensitivity absent.** The three hyperparameters `λ₁, λ₂, λ₃` in the KL regularization term are given fixed values with no ablation study showing how performance varies across a range of settings. An ablation of at least `λ₁` on Hard-ImageNet would help establish robustness.

### Trivial

- None beyond standard presentation formatting that is likely a parser artifact.

## Nice-to-Haves

- A gradient analysis showing how the |CAM| term in CFCE propagates gradients to suppress non-core activations would clarify the mechanism.
- Testing generalization to ViT or other non-convolutional architectures would broaden applicability.
- A systematic perturbation analysis of mask quality (dilation/erosion of core region) would strengthen claims about robustness.

## Removed Points

- **Theorem 4.6 proof inaccessible (Critical Issue 2).** The harsh critic flagged that the proof of Theorem 4.6 is relegated to the appendix. Per instructions, the parser strips appendix content from all papers, and this is a parser artifact rather than an author error. The theorem statement is present and complete in the main paper. Removed on procedural grounds.

- **"Severity of HiResCAM limitation overstated."** The harsh critic claimed the HiResCAM non-uniqueness is a well-known consequence of softmax shift-invariance. However, the paper's result (Theorem 3.2) extends from the standard scalar shift to a *matrix* shift across spatial dimensions, which is not a trivial consequence and is a novel theoretical contribution. Removed as a factual misunderstanding.

- **"Figure 1 conflates scalar logit shift with matrix shift."** The figure is a pedagogical illustration using scalar shifts for visual simplicity. The theorem formally treats the matrix case. Removed as an over-interpretation of an illustrative figure.

- **"Baseline 'CE w/ Arch' poorly described."** The architectural modifications are detailed in Appendix C, which is stripped by the parser. Removed on procedural grounds.

- **"No statistical significance tests."** Standard deviations are reported for all main results, which is adequate for this research setting. Removed as a generic expectation mismatch.

- **"Definition 4.5 is ad-hoc."** Replaced by a minor weakness about underspecified KL regularization, as Theorem 4.6 is the stated theoretical justification. The critic's "ad-hoc" characterization is an opinion, not a verifiable flaw.

- **Several nice-to-haves from the harsh critic's "Missing Experiments"** (independent alignment metric for Pets/PASCAL, ablation of λs, comparison with masking baselines). These overlap with the weaknesses above and are partially retained. The remainder (gradient analysis, failure cases, training dynamics, generalization to ViT) are moved to Nice-to-Haves as they extend beyond what is necessary for the paper's core claims.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the review is that the gap between ContrastiveCAM IoU (93.39%) and GradCAM IoU (51.52%) for CFCE+KL on Hard-ImageNet reveals a genuine empirical finding: optimizing for one explanation method's alignment does transfer to another method, but with a substantial gap. This 42-point discrepancy is not a weakness but an informative signal about how different explanation methods respond to the same feature alignment pressure — and it highlights the importance of reporting multiple metrics, which the paper partially does for Hard-ImageNet but crucially not for the other datasets.

## Suggestions

1. Specify exactly which explanation method (GradCAM, ContrastiveCAM, or other) is used for the IoU metric in Tables 3 and 4. Add at least one independent explanation method's IoU for Pets and PASCAL (as done for Hard-ImageNet's GradCAM column).
2. Add a brief explanation of how softmax applies to a binary mask `H` in Definition 4.7, or clarify the intended semantics.
3. Define `ℒ_core` and `ℒ_Non-Core` in the Figure 3 caption or table, including which classes are summed.
4. Include a sensitivity analysis for at least `λ₁` (the KL regularization weight) on a benchmark like Hard-ImageNet.
5. Discuss the accuracy-versus-alignment trade-off more explicitly — under what conditions is the ~4-point accuracy drop acceptable?

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `fdvSCcB7i8` (Feature Level Instance Attribution) | 3.00 | Much weaker — unclear method, missing novelty, unconvincing experiments. Current paper has stronger theory and results. |
| `HXwrppoSPc` (COMiX) | 3.25 | Much weaker — insufficient novelty relative to prior work, unclear presentation. Current paper has clearer contributions. |
| `3b8CgMO5ix` (Model guidance via explanations) | 5.50 | Somewhat weaker — mixed reviews, poor organization, missing comparisons. Current paper has stronger theoretical and experimental support. |
| `CMqOfvD3tO` (CDAM) | 6.80 | Comparable but cleaner — clear motivation, comprehensive ablations, well-written. Current paper has stronger theory but evaluation gaps. |
| `PBjCTeDL6o` (UNI — Unlearning-based Interpretations) | 8.00 | Stronger — thorough analysis, comprehensive experiments, clear presentation. Current paper is not at this level of polish. |

The paper makes a genuine theoretical contribution (HiResCAM non-uniqueness, ContrastiveCAM invariance) and proposes a novel method that shows real improvements on independent metrics (GradCAM IoU on Hard-ImageNet, downstream segmentation). The main empirical weakness — unspecified IoU metrics for Pets and PASCAL — is verifiable from the paper and should be corrected, but does not invalidate the core evidence from Hard-ImageNet. The paper is clearly stronger than the 3.00–3.25 band (rejected for fundamental flaws) and the 5.50 band (unclear contributions). It is slightly below the 6.80 CDAM paper in terms of experimental clarity and completeness, but has stronger theoretical foundations. A score of 6.0 reflects a solid contribution with addressable weaknesses.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>