Now let me compile my final review after careful analysis of the paper and all review inputs.

## Summary

This paper identifies a theoretical limitation of HiResCAMs (they are determined only up to an additive matrix *M* due to softmax invariance), proposes **ContrastiveCAMs** as *M*-invariant alternatives that provide granular class-versus-class explanations, and introduces **Core-Focused Cross-Entropy (CFCE)**, a loss that penalizes contributions from user-specified non-core image regions. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC show that CFCE-trained models achieve substantially higher IoU with core regions and improved downstream segmentation performance.

## Strengths

1. **Theoretical identification of HiResCAM ambiguity and construction of M-invariant ContrastiveCAMs (Theorems 3.2, 3.5).** The observation that HiResCAMs are not uniquely determined under softmax and that ContrastiveCAMs remove this redundancy is a genuine conceptual contribution, supported by Proposition 4.1 which expresses softmax probabilities directly as a function of ContrastiveCAMs. This formal connection between explanations and model outputs is absent in previous CAM-family methods.

2. **CFCE loss is well-motivated theoretically.** Proposition 4.2 shows that standard cross-entropy does not distinguish core from non-core contributions, providing a theoretical basis for feature misalignment. Theorem 4.6 (consistency with core-constrained risk minimization) connects the proposed loss to a principled optimization objective, establishing classification-calibration.

3. **Strong empirical results across multiple settings.** ContrastiveCAM IoU improves from 30% (CE w/ Arch) to 89–93% (CFCE/CFCE+KL) on Hard-ImageNet. On Oxford-IIIT Pets, IoU increases from 78% to 93% (multiclass) with virtually no accuracy loss. Downstream segmentation on PASCAL VOC shows consistent gains, especially for challenging classes (Cat, Dog, Horse). These results are reproduced across binary, multiclass, and multilabel settings.

4. **Practical robustness to mask quality.** Table 3 shows that CFCE performs competitively with SAM-generated masks or bounding boxes compared to ground-truth masks, demonstrating that the method does not require expensive pixel-level annotations.

5. **Redundancy ratio γ (Table 1) and class-versus-class granularity (Figure 2)** provide novel diagnostic information about how much of HiResCAM explanations are attributable to the softmax redundancy, offering practical insight beyond the theoretical analysis.

## Weaknesses

### Major

- **Core-region ablation metric is partially confounded with the training objective.** The primary metric in Table 2 (accuracy under core-region ablation) directly measures whether the model fails when core regions are removed — which is exactly what CFCE was designed to enforce. Baseline methods (CORM, DFR, CE) never saw the masks, so their low sensitivity to ablation is expected. The paper has less confounded metrics (IoU, downstream segmentation) but gives them less prominence. The narrative should explicitly acknowledge this bias and restructure to center the independent evidence.

- **Missing baseline comparisons.** The paper compares only to CORM and DFR (both from core-risk minimization). Despite citing saliency regularization (Ismail et al., 2021) and other interpretability-guided training approaches in the related work, none are included as baselines. Adding at least one natural competitor — e.g., Right for the Right Reasons, Attention Branch Networks, or a simple saliency-penalty loss — would substantially strengthen the claim that CFCE is uniquely effective for feature alignment.

- **Computational cost for many-class problems not discussed.** CFCE requires computing $\text{CAM}_{(c_t,c)}^{\text{Cntrst}}$ for every $c \neq c_t$. For 1000-class ImageNet this is a serious practical burden with no discussion of approximations, minibatch sampling over classes, or other mitigation strategies.

### Minor

- **Tension between IoU and ablation for CFCE+KL unexplained.** In Table 2, CFCE+KL has *higher* ContrastiveCAM IoU than CFCE (93.39% vs. 89.22%) yet its accuracy under core-region ablation is *higher* (37.07 vs. 31.66 for Gray BBOX), indicating *less* reliance on core regions. This contradicts the intuition that higher IoU implies better alignment and needs explanation.

- **CE w/ Arch IoU collapse not explained.** In Table 3 (Oxford Pets), "CE w/ Arch" shows dramatically lower IoU than plain CE (39% vs. 78% binary; 60% vs. 80% multiclass). The paper does not discuss why the architectural modifications alone harm alignment, though the implication is that CFCE recovers from this.

- **CFBCE used but never defined.** The multilabel variant appears in Table 4 but is not defined in the main text. While presumably defined in the (stripped) appendix, a brief main-text definition is needed.

- **Hyperparameters not reported or analyzed.** The values of $\lambda_1, \lambda_2, \lambda_3$ in Eq. (18) and the softmax temperatures are absent. No sensitivity analysis is provided.

- **Standard deviations missing for some baselines.** CORM and DFR results in Table 2 lack standard deviations, making significance comparisons difficult.

### Trivial

- No pseudocode or algorithm sketch summarizing the training procedure.
- The KL regularization (softmax over spatial locations, Eq. 18) is an unusual choice that is not justified or ablated.

## Nice-to-Haves

- A controlled toy experiment that isolates the effect of CFCE by systematically varying core/non-core correlations with the label.
- Faithfulness evaluation of ContrastiveCAMs vs. HiResCAMs on insertion/deletion or ROAD benchmarks to empirically support the claim that ContrastiveCAMs are more faithful.
- Runtime comparison of CFCE vs. standard cross-entropy.
- Analysis of the gradient properties of the $|\cdot|$ term in CFCE (Definition 4.5) near zero.

## Removed Points

The following points raised by the reviewers are removed or demoted under the filtering rules described in the instructions:

1. **"Proofs deferred to appendix"** — REMOVED. The appendix was stripped by the PDF parser; it exists in the original submission. This is a parser artifact, not an author omission.
2. **"Missing related works"** — REMOVED per hard rule (cannot confirm existence of missing citations, and paper already cites relevant literature).
3. **"Formatting, typos, grammar, whitespace"** — REMOVED per hard rule. These are parser artifacts.
4. **"HiResCAM limitation overstatement"** — DEMOTED to implicit in the narrative. The claim is technically correct (the mapping from probabilities to explanations is not one-to-one). For a *fixed* model the HiResCAM is deterministic, but the paper's focus is on the theoretical non-uniqueness in the explanation space. The practical significance is debatable but the mathematical claim stands.
5. **"Absolute value in CFCE not discussed for gradient properties"** — Moved to Nice-to-Haves. This is a minor implementation detail.
6. **"Reproducibility: undisclosed hyperparameters"** — Partially removed. The λ values are verifiably missing → kept as Minor. Broader reproducibility nitpicks removed.

## Novel Insights

None beyond the paper's own contributions. The review confirms that ContrastiveCAMs' *M*-invariance and the CFCE training objective are the core novel ideas, and the empirical results generally support their effectiveness, but the evaluation has confounds (ablation metric coupling) and gaps (missing baselines, undiscussed computational cost) that weaken the strength of the conclusions as currently presented.

## Suggestions

1. Acknowledge the coupling between the core-region ablation metric and the CFCE objective explicitly; restructure the narrative to give more weight to IoU and downstream segmentation as independent evidence.
2. Include at least one interpretability-guided training baseline (saliency regularization, RRR, or similar) in the main comparison.
3. Discuss the computational overhead of CFCE for large-class problems and propose practical approximations (e.g., negative class sampling).
4. Investigate and explain why CFCE+KL increases IoU but reduces ablation sensitivity compared to plain CFCE.
5. Report λ values and include a hyperparameter sensitivity study.
6. Define CFBCE explicitly in the main body; add a training procedure summary or pseudocode.

## Score and Decision

**Calibration protocol summary:**

**Round 1 (Bracketing):** Queried three bands on topics similar to the paper.
- *Weak band* (avg < 3.5): FTpdQBoBd0 (3.00), BwQUo5RVun (3.00), MbtUctg3KW (2.50), wl1Kup6oES (3.00), HXwrppoSPc (3.25) — reject-level papers with thin contributions.
- *Middle band* (3.5 < avg < 7.5): Tj3xLVuE9f (6.80), bkdWThqE6q (6.00), ONhLaNbxVV (5.75), GjfIZan5jN (7.33), 57NfyYxh5f (6.25), g6Qc3p7JH5 (5.80), ozZG5FXuTV (6.00), 7TZYM6Hm9p (6.00), vVxeFSR4fU (6.50), OZWHYyfPwY (7.00), Q95MaWfF4e (7.00) — solid papers with clear contributions but evaluation limitations.
- *Strong band* (avg > 7.5): PBjCTeDL6o (8.00), 25kAzqzTrz (8.00), hrqNOxpItr (8.00), 4xWQS2z77v (8.00), STUGfUz8ob (7.60) — strong accepts with thorough evaluation.
- **Round 1 bracket:** 5.5–7.0

**Round 2 (Narrowing):** Focused on interpretability-guided training/CAM-based feature alignment in the middle band.
- *bkdWThqE6q* (6.00, INTR): Comparable quality. Both have strong ideas but evaluation limitations. Our paper has stronger theory (theorems, proofs) but similar evaluation gaps.
- *57NfyYxh5f* (6.25, How to Probe): Slightly stronger than our paper due to cleaner, less confounded evaluation across diverse settings.
- *g6Qc3p7JH5* (5.80, Feature Monosemanticity): Comparable quality. Both have interesting contributions with evaluation gaps (confounded metrics, missing controls).
- *OZWHYyfPwY* (7.00, Don't trust your eyes): Clearly stronger paper with more thorough analysis; ours does not reach this level.

**Final score:** 6.0 — The paper sits between the 5.80 anchor (similar quality, comparable evaluation gaps) and the 6.00–6.25 anchors (slightly stronger evaluation). The theoretical contributions (ContrastiveCAMs, CFCE) are solid and the results are generally positive, but the confounded ablation metric and missing baselines prevent the empirical evaluation from being as convincing as it could be.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>