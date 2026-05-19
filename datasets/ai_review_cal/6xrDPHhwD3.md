- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 3, 8
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes MFC-MIL, a plug-and-play framework for whole-slide image classification that integrates three modules: a Multiscale Spatial Representation Module (MSRM) for multi-level spatial features, a Frequency-domain Structural Representation Module (FSRM) using the Hilbert transform, and a Causal Memory Intervention Module (CMIM) designed to perform front-door causal intervention via a learnable memory. The framework is evaluated on Camelyon16 and TCGA-NSCLC across five MIL baselines, showing consistent accuracy and F1 improvements, with ablation studies confirming the contribution of each module.

---

## Strengths

1. **Consistent accuracy/F1 gains across multiple MIL architectures and two datasets.** The paper reports (Section 4.4) that all five baseline methods (ABMIL, DSMIL, TransMIL, CLAM-SB/MB, DTFD-MIL) improve in accuracy and F1 when augmented with MFC on both Camelyon16 and TCGA-NSCLC. For example, DSMIL gains 5.27% accuracy on Camelyon16 and 2.08% on TCGA-NSCLC. This multi-baseline, multi-dataset validation provides reasonable evidence that the framework has general utility.

2. **Ablation studies isolate each module's contribution.** Table 3 (summarized in Section 4.5) shows that removing CMIM, MSRM, or FSRM individually degrades performance relative to the full model on the TransMIL backbone, supporting the claim that each component contributes positively and that the design is not redundant.

3. **Systematic memory size sensitivity analysis.** Section 4.5.1 and Figure 3 examine how varying memory slot counts \(k\) (4, 8, 16, 32, 48) for both high-level and low-level features affects ACC, AUC, F1, and specificity. The analysis reveals an interpretable inverted-U pattern and provides practical guidance for hyperparameter selection.

4. **Frequency-domain transform comparison.** Section 4.5.3 compares the Hilbert transform against FFT, DCT, and DWT within the same framework, showing that the Hilbert-based FSRM achieves the best AUC (97.68% vs. 91.66% for FFT). This gives concrete evidence that the choice of transform matters and that the Hilbert variant is effective.

---

## Weaknesses

### Major

1. **CMIM implementation is critically underspecified, preventing evaluation of the core methodological contribution.** Section 3.1 presents the front-door adjustment formula (Eq. 5) and states that a memory module with \(k\) trainable slots is used with "attention-weighted inputs" and "Normalized Weighted Geometric Mean (NWGM)" to approximate the intervention. However, the paper does not specify: (a) how the memory is initialized or updated during training, (b) how attention weights over memory slots are computed from input features, (c) how attention-weighted sampling relates to the terms \(P(X=\hat{x})\) and \(P(M=m|X=x)\) in the front-door adjustment, or (d) how NWGM is specifically applied to approximate the double sum \(\sum_m \sum_{\hat{x}}\). The description (lines 75–87) is a high-level sketch, not an operationalized algorithm. Since the causal intervention mechanism is the paper's headline novelty, this gap undermines reproducibility and scientific evaluation. The "likely invalid" speculation from the reviewer is unwarranted (the formulation is mathematically standard); the real problem is that *what is actually computed* is not disclosed.

2. **AUC drops on CLAM-SB and CLAM-MB are acknowledged but not adequately resolved.** The paper reports (Section 4.4) that on Camelyon16, CLAM-SB and CLAM-MB show *decreased* AUC relative to their baselines despite gains in accuracy, F1, and specificity. The offered explanation — that MFC "alters the sample distribution... handling of non-boundary samples is less balanced" — is speculative and not supported by additional analysis (e.g., ROC curves, per-threshold behavior, or partial AUC). Since AUC is the standard metric for medical diagnosis, particularly in class-imbalanced settings, these drops are a significant concern for a method claiming improved "generalization ability." This weakens the core claim.

3. **No experimental comparison with CaMIL, the most directly related prior work.** The paper discusses CaMIL (Chen et al., 2024) in Sections 1 and 2.2, critiques its reliance on feature clustering and preprocessing, and motivates MFC as an alternative front-door approach. Yet the experiments include no comparison with CaMIL — only IBMIL is compared (on a single baseline, DSMIL, on Camelyon16). Since CaMIL shares the same causal front-door framing, the absence of a direct comparison means the claimed advantages (simpler, more efficient, more interpretable) are entirely unsubstantiated by evidence.

### Minor

4. **The Hilbert transform's application to discrete feature vectors is not explained.** The paper (Section 3.3) introduces the Hilbert transform via the continuous-domain formula (Eq. 6–8), then applies it as an operator \(H: \mathbb{R}^{512} \to \mathbb{R}^{512}\) on projected patch features. It is not specified whether the transform is applied independently to each of the 512 dimensions (treating each as a 1D signal across the feature dimension), or whether the 512-d vector is treated as a sequence. Since the Hilbert transform is defined for signals with a natural ordering, and feature dimensions have no inherent order, this operational gap matters for reproducibility.

5. **The claim that FSRM provides robustness to staining variation is untested.** The paper motivates FSRM by stating that frequency-domain phase information is "robust to staining variations" and reduces "interference from staining techniques and color contrast" (Section 1, Section 3.3). However, no experiment varies staining conditions or tests this claim. A stain-normalization control or a synthetic color-shift experiment would be needed to support this assertion.

6. **Ablation studies are conducted only on the TransMIL backbone.** While the main results (Table 1) span five baselines, the ablations for CMIM, MSRM, and FSRM (Table 3) and the memory-size sensitivity (Figure 3) use only TransMIL. It is unclear whether the relative contributions of each module generalize to other backbones.

### Trivial

None.

---

## Nice-to-Haves

- A wall-clock or FLOPs comparison with IBMIL and (ideally) CaMIL would substantiate the claimed efficiency advantages, which are currently asserted without evidence.
- Statistical significance testing (e.g., paired tests across folds) would strengthen confidence in the observed improvements, given the modest margins (~2–5%).
- Re-tuning the CMIM memory size per baseline rather than using fixed settings (16/32 for all) would rule out the concern that some baselines are disadvantaged by suboptimal hyperparameters.

---

## Removed Points

- **"CaMIL's clustering 'reduce interpretability' is asserted without evidence"** — This is a minor rhetorical point in the related work section, not a core weakness of the paper's contribution. The paper's claims stand or fall on its own evidence, not on how CaMIL is characterized.
- **"Code release is essential"** — Moved to implicit acknowledgment; code availability is always beneficial but not a required part of review evaluation.
- **"Additional backbones for ablation"** — Redundant with Minor Weakness #6; the current set of 5 baselines in main results already provides breadth.

---

## Novel Insights

None beyond the paper's own contributions. The two reviewers largely converge on the same issues: the CMIM specification gap and the insufficient causal validation. The most informative cross-cutting observation is that the paper has a disconnect between its ambitious causal framing (front-door intervention, mediator estimation, deconfounding) and the thinness of the implementation description — the mathematical apparatus is standard, but the procedural bridge from equations to algorithm is missing. This is a pattern common to ML papers that adopt causal terminology without fully operationalizing it.

---

## Suggestions

1. **Provide a complete algorithmic specification of CMIM.** This is the single highest-leverage improvement. Write out the forward pass: how memory \( \mathbf{M} \in \mathbb{R}^{k \times D} \) is initialized, how attention weights \( \alpha_i = \text{softmax}(\mathbf{q}^\top \mathbf{M}_i) \) (or similar) are computed, how the "attention-weighted sampling" selects/reweights \(\hat{x}\), and exactly how NWGM collapses the double sum \(\sum_m \sum_{\hat{x}}\) into the computed loss or prediction. Without this, the contribution is not a method but a sketch.

2. **Compare with CaMIL under the same experimental conditions** (same backbone, same data splits, same metrics). This is necessary to support any claim that MFC improves upon prior causal front-door methods.

3. **Investigate and explain the AUC degradation on CLAM baselines.** Report full ROC curves or partial AUC in the clinically relevant operating range. If the AUC drop is systematic, discuss whether it can be mitigated by threshold calibration or if it reflects a genuine limitation.

4. **Add a direct test for spurious correlation reduction** — for example, train on data with synthetic confounders (color shifts, artificial biases) and measure the degree to which MFC reduces reliance on those features compared to baselines. This would directly validate the causal motivation.

5. **Clarify the Hilbert transform's discrete application.** State whether the transform is applied per-dimension along the feature dimension or whether the 512-d vector is treated as a 1D discrete signal. Since feature dimensions have no natural ordering, a per-dimension application (to each of the 512 features independently) would produce trivial results; the paper should clarify.

---
