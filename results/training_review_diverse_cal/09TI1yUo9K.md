Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper proposes IGB-AD, a 3D anomaly detection framework with three main components: (1) Rotation-Invariant Farthest Point Sampling (RIFPS) to produce order-invariant FPFH feature matrices without requiring registration, (2) stacked Information Gain Blocks (IGB) that take Gaussian noise and reference features as input and produce additive feature perturbations trained with a Smooth L1 + variance-maximization loss, and (3) Packet Downsampling (PD) using K-Means clustering with Mahalanobis distance for memory bank subsampling. The paper also introduces the ICD dataset, designed for high intra-class variance. IGB-AD achieves SOTA results on Anomaly-ShapeNet (P-AUROC 81.5%, I-AUROC 80.9%) and ICD (P-AUROC 57.4%, I-AUROC 60.2%).

## Strengths

- **Strong empirical performance on standard and challenging benchmarks**: IGB-AD achieves SOTA on Anomaly-ShapeNet (40 categories), outperforming RegAD, IMRNet, R3D-AD, and other baselines across both P-AUROC and I-AUROC. It also achieves the best results on the new ICD dataset. The consistent margin over prior work across two datasets with very different properties (standard vs. high intra-class variance) strengthens the evidence for the method's effectiveness.

- **RIFPS provides a clean, principled solution for rotation invariance**: Selecting the farthest point from the geometric center as an anchor before applying FPS and FPFH is a simple and well-motivated approach that reduces reliance on registration. This component is clearly described, implementable, and addresses a genuine limitation in prior 3D anomaly detection methods.

- **Introduction of the ICD dataset fills a gap**: The ICD dataset is the first 3D anomaly detection benchmark with multiple morphologically distinct subspecies per class, targeting the under-explored problem of high intra-class variance. This is a useful community resource.

- **Packet Downsampling strategy is a reasonable approach to subsampling under multi-subclass conditions**: Using K-Means clustering followed by Mahalanobis distance-based greedy selection with adaptive density handling is a sensible design. The ablation shows a consistent (though small) improvement from PD (0.4% I-AUROC).

## Weaknesses

### Fatal

None. The empirical results are valid and the method components are sufficiently specified to be implementable. The weaknesses below are major but addressable.

### Major

1. **The core claim that noise serves as "prior information" is not substantiated by the evidence presented.** The loss function (Eq. 7) does not involve the noise input Z at all — it only constrains F+X relative to F via SmoothL1 loss and maximizes variance of F+X via the Richness loss. The MLP takes Z and F as input, but the loss provides no explicit pressure for X to be "extracted from Z" rather than produced as a deterministic function of F alone. The paper presents no ablation that verifies whether the noise input actually contributes: no comparison against feeding constant input instead of Z, no experiment removing Z entirely, no variation of noise type or scale, and no analysis showing what information is "extracted." Without these controls, the "noise as prior information" narrative is unsupported — the method is better described as a learned feature perturbation module, and the paper's claimed novelty hinges on an unvalidated interpretation.

2. **The mathematical justification (CLT, MLE) is misleading and disconnected from the actual training objective.** The Central Limit Theorem is invoked to justify decomposing Gaussian noise Z into X+Y, but CLT concerns the distribution of a *sum* of random variables approaching normality, not the decomposition of a single Gaussian into meaningful components — Z is defined as Gaussian, so no decomposition via CLT is needed or justified. The MLE framing writes $\hat{X}_{\mathrm{MLE}} = \arg\max_X p(Z|X)$ but never defines the likelihood $p(Z|X)$, and the actual loss function (Eq. 7) does not maximize any such likelihood. These equations create an appearance of principled inference that does not match the implementation, making it difficult for readers to understand what the IGB module actually learns and why.

3. **Missing critical ablation: the most relevant baseline is not tested.** The paper does not compare IGB-AD against a version that removes the IGB module entirely (i.e., RIFPS + FPFH + PatchCore scoring, without any feature perturbation). Table 1 compares against BTF(FPFH), but BTF uses a different overall pipeline. The question of whether IGB contributes beyond simply using the raw FPFH features with the same scoring mechanism is not cleanly isolated. Also absent is a simple noise injection baseline (adding Gaussian noise directly to FPFH features at equivalent variance with the same PatchCore scoring), which would test whether the MLP-based "information extraction" does anything beyond random perturbation.

### Minor

4. **ICD dataset description is insufficient for a contribution claimed as a major output of the paper.** The text does not specify: total number of classes (10 — only learnable from Table 1's caption), total sample count, how anomalies are generated, annotation protocol (pixel-level vs. object-level ground truth), or how the dataset compares in scale to existing benchmarks. The paper states it "will be released after acceptance," but the review must evaluate the dataset contribution based on what is described. As written, the ICD contribution cannot be properly assessed.

5. **No error bars or confidence intervals are reported for any result.** Given the modest ablation improvements (e.g., PD adds ~0.4% I-AUROC; adding IGB layers from 1→5 yields a ~2.3% cumulative gain), the lack of variance estimates makes it impossible to determine whether these differences are meaningful or within run-to-run noise.

6. **The PD description borrows terminology inconsistently.** The section describes K-Means clustering (which needs no ε or min_samples parameters), then introduces "adaptive ε" and "min samples" via k-NN as if these were DBSCAN parameters. The method is likely coherent (K-Means → within-cluster Mahalanobis selection with adaptive threshold), but the mixed terminology makes the exact procedure unclear.

### Trivial

- The improvement from PD is marginal (0.4% I-AUROC). The contribution is valid but modest.

## Nice-to-Haves

- The paper would benefit from visualizing the "extracted information" X (e.g., t-SNE of X vs. original F) to demonstrate that the noise input produces structured, semantically meaningful perturbations.
- A comparison against using FPFH features alone with the same scoring pipeline (i.e., removing IGB entirely) would cleanly isolate the IGB contribution from the broader framework.
- An analysis of sensitivity to noise scale (variance of Z) would help readers understand the method's robustness.

## Removed Points

These points from the reviewers were removed per policy; they are listed here for completeness but should not carry weight:

- *"The dataset will be released after acceptance, which means it cannot be verified now"* — Removed per rule: criticisms questioning existence/release status of cited datasets are not valid concerns.
- *"Tables are unreadable in the submitted text"* — Removed per rule: parser-induced formatting artifacts do not reflect the original submission.
- *"State-Of-The-Arts (grammatical error)"* — Removed per rule: typographical nitpicks are not substantive weaknesses.
- *"No code or reproducibility details"* — Removed per rule: the paper provides reasonable implementation details (optimizer, epochs, learning rate, GPU); code release is not expected during review.
- *"The method uses FPFH features, which are hand-crafted and limited in capacity"* — This is a taste-based judgment, not a concrete weakness; the paper's method is designed around FPFH, and a different feature choice would be a different paper.
- *"The PD description mixes incompatible clustering methods"* — Overstated. The method uses K-Means for clustering and k-NN for adaptive selection thresholds, which is coherent; the terminology confusion (ε, min_samples) is a clarity issue, not an incompatibility. Downgraded to Minor.

## Novel Insights

A theme that emerges from reading across the reviews is that the paper's actual contribution — a learned feature perturbation module that enforces controlled deviation from original features via SmoothL1 + variance maximization — is potentially valuable independent of the noise narrative. The idea of intentionally perturbing normal features to expand the representation space during training (rather than denoising or distilling to a canonical representation) is underexplored in 3D anomaly detection. The paper's SOTA results suggest this direction has merit. The key gap is that the paper attributes the success to "extracting information from noise" without evidence, whereas the more plausible explanation (and the one the method actually implements) is that training an MLP to produce bounded, high-variance perturbations of normal features acts as a data augmentation strategy that improves the robustness of the feature bank. Reframing the contribution around this interpretation would both clarify the method and make the paper's novelty easier to evaluate.

## Suggestions

- **Reframe the contribution.** Drop the CLT and MLE rationalizations. Describe IGB as: an MLP conditioned on features F and random noise Z that produces a residual X, trained to keep F+X close to F (SmoothL1) while maximizing variance (Richness loss). The role of noise is to provide stochasticity to the perturbation function — a known technique in self-supervised learning — not to serve as a decomposable information source.

- **Add a critical ablation.** Compare: (a) the full method, (b) removing IGB (RIFPS + FPFH + PatchCore scoring only), (c) replacing learned IGB with direct additive Gaussian noise at matched variance. This would isolate whether the MLP-based perturbation actually outperforms cheap alternatives.

- **Improve ICD dataset documentation.** Add a table specifying number of classes, total samples per class (train/test), anomaly types, annotation granularity, and comparison statistics to existing datasets.

- **Report error bars.** Run at least 3 random seeds and report mean ± std for key results, especially for ablation comparisons.

- **Clarify PD.** Either use consistent K-Means + Mahalanobis terminology throughout (removing ε/min_samples references) or clearly explain how k-NN adapts the selection threshold within clusters.

## Score and Decision

**Originality:** 3/5 — The idea of using noise constructively is novel in concept, but the actual mechanism is a standard feature perturbation approach that is not well differentiated from simpler alternatives. RIFPS and PD are incremental but solid engineering contributions.

**Importance of Question:** 4/5 — 3D anomaly detection with high intra-class variance is a practically important and under-addressed problem.

**Claims Support:** 2/5 — The central claim about noise as prior information is not supported by the experimental design. The method works, but the explanation given for why it works is not backed by evidence.

**Soundness:** 3/5 — The empirical evaluation is adequate (standard benchmarks, multiple baselines) but missing the critical ablation that would validate the core claim. No error bars.

**Clarity:** 2/5 — The mathematical framing is misleading; the PD description mixes terminology; the dataset description is sparse. The method's actual behavior is obscured by the narrative.

**Value to Community:** 3/5 — SOTA results on a standard benchmark and a new challenging dataset are valuable. The ICD dataset is a useful resource. But the unsubstantiated theoretical claims reduce the paper's reliability as a reference.

The paper reports strong empirical results and introduces a genuinely challenging new dataset, both of which have clear community value. However, the paper's central theoretical claim — that noise serves as a decomposable source of useful information — is not supported by the evidence. The loss function does not involve the noise input, and no ablation verifies that noise contributes anything. The mathematical framing (CLT, MLE) is misleading. The rebuttable nature of these issues (they can be fixed by reframing the contribution and adding ablations) means the paper is not fatally flawed, but the gap between narrative and evidence is substantial.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>