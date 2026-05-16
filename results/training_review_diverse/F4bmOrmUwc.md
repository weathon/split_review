Now I have all the information I need. Let me construct the final consolidated review.

## Summary

The paper proposes a **Fixed Non-negative Orthogonal (FNO)** classifier for neural network classification. It introduces **zero-mean neural collapse (ZNC)** as a theoretical framework to explain the collapse of last-layer features when using fixed orthogonal classifiers (since standard neural collapse requires simplex ETF geometry, which fixed orthogonal classifiers cannot satisfy). The paper shows that non-negativity combined with orthogonality yields **Feature Dimension Separation (FDS)** — disjoint active-feature indices per class — which is then exploited for two applications: (1) enhancing masked softmax in continual learning by reducing class-wise interference, and (2) enabling a novel **arc-mixup** for imbalanced learning that preserves hypersphere geometry. Experiments on continual learning and long-tailed classification benchmarks show improvements over baselines.

## Strengths

- **Novel theoretical framing for fixed orthogonal classifiers (ZNC).** The paper identifies a genuine gap: existing neural collapse theory assumes the classifier converges to a simplex ETF, but fixed orthogonal classifiers cannot do so. Proposing zero-mean neural collapse (centering class means to the origin rather than the global mean) as an alternative collapse geometry for this setting is a conceptually interesting extension of neural collapse theory (Section 4, Table 1).

- **Feature Dimension Separation (FDS) is a clean and well-motivated property.** The observation that non-negativity + orthogonality yields disjoint active-feature indices per class (Definition 3) is clearly explained and provides intuitive grounding for the downstream applications. The connection from FDS to reducing class-wise interference in masked softmax (Section 6.1) and to enabling interference-free arc-mixup (Theorem 2, Section 6.2) is logically coherent.

- **Theorem 2 (arc-mixup without class-wise interference) is proved and provides a crisp theoretical link.** The proof (lines 218–226) cleanly shows that orthogonality is necessary and sufficient for the mixed class weight vector to remain on the hypersphere without interference, and that non-negativity follows naturally from FDS. This gives a principled justification for using the FNO classifier with arc-mixup.

- **Consistent empirical gains across multiple settings.** The method outperforms baselines in continual learning (Table 2) and imbalanced learning (Tables 3–4) across diverse datasets (CIFAR, TinyImageNet, ImageNet-LT, Places-LT) and architectures, suggesting the approach has practical value.

## Weaknesses

### Fatal

None.

### Major

- **The empirical evaluation lacks controlled ablations that would attribute improvements to the claimed mechanism (FDS).** In continual learning (Table 2), the comparison is between masked replay with a learnable classifier vs. with FNO. The large gap (e.g., S-TinyImageNet: 16.83% → 51.93%) could come from the fixed classifier itself, from non-negativity, from orthogonality, from the weighted softmax scale parameter, or from FDS. In imbalanced learning (Tables 3–4), FNO is combined with arc-mixup, but there is no ablation of (a) FNO without arc-mixup, (b) FNO with standard (linear) mixup, (c) a learnable classifier with arc-mixup, or (d) a fixed orthogonal classifier without non-negativity. Without these controls, it is unclear whether FDS is the driver of the reported gains, or whether other factors (e.g., the fixed classifier acting as a regularizer, or arc-mixup itself) are responsible. This weakens the paper's central explanatory claim that FDS is the beneficial mechanism.

- **The core theoretical motivation — zero-mean neural collapse — is asserted but not empirically demonstrated.** Section 4 states that "we analyzed the zero-mean neural collapse in the same environments to neural collapse by conducting comprehensive experiments" (line 100), but no measurements (e.g., NC1–NC4 style metrics adapted for ZNC, such as within-class variability, convergence to orthogonality, self-duality, or NCC simplification) are reported in the paper. The central claim that the FNO classifier induces ZNC as a "natural phenomenon" therefore rests solely on the unproven Theorem 1 (see removed points) rather than on any empirical evidence. This is an evidential gap for a paper that makes the ZNC framework a centerpiece of its contribution.

### Minor

- **The paper does not explain why the large improvements in continual learning occur.** In Table 2, FNO improves masked replay from 16.83% to 51.93% on S-TinyImageNet class-incremental — a >3× relative gain. The paper offers only a high-level statement that "FNO enhances the masking effect" without analyzing why the improvement is so dramatic or whether hyperparameter tuning favors FNO. The large standard deviation (±6.55 for that setting) also raises questions about stability.

- **The construction of the fixed non-negative orthogonal matrix is underspecified.** The paper says the classifier is "initialized as a random fixed non-negative orthogonal matrix by Eq. 8" (line 107), but Eq. 8 does not appear in the extracted text, and the method for generating a non-negative orthogonal matrix (a non-trivial constraint) is not described. This affects reproducibility.

- **The added constraint in the OLPM (∑_{j≠k} h^T q_j^* ≥ 0, Eq. 5) is introduced without motivation.** The paper adds this non-negativity-of-logits constraint for non-ground-truth classes but does not explain why it is needed or how it relates to the theory.

- **No statistical significance testing is reported.** Many of the reported standard deviations overlap across methods (e.g., Tables 3–4). While single-run or few-trial evaluation is common in this area, the paper does not provide confidence intervals or significance tests for the key comparisons where the numerical gap is small.

### Trivial

- The paper does not analyze empirically how close the feature dimension D is to the number of classes K, nor whether the FNO classifier remains effective when D is only slightly larger than K (the paper acknowledges D ≥ K as a limitation in Section 8 but provides no analysis).

## Nice-to-Haves

- Reporting adapted NC metrics (e.g., within-class variability collapse, convergence to orthogonality) for the FNO classifier on a small-scale dataset (e.g., CIFAR-10) would directly validate the ZNC claim and anchor the theoretical contribution.
- An ablation study that isolates the effects of the fixed classifier, orthogonality, non-negativity, and arc-mixup would substantially strengthen the empirical contribution. Minimal additions: (i) FNO with standard mixup, (ii) learnable classifier with arc-mixup, (iii) fixed orthogonal classifier without non-negativity.
- Including confidence intervals or statistical tests for borderline comparisons would improve reliability assessment.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism that Theorem 1 is "not proved" / "proof is absent."** Theorem 1 states that a global minimizer of the OLPM is a max-margin solution converging to ZNC. The main text reads "Proof 1." with no content. However, per the review guidelines, the parser strips appendix/supplementary sections from all papers; proofs deferred to an appendix exist in the original submission. This criticism is therefore removed, though the paper would benefit from at least referencing where the proof appears.

- **Criticism about a "malformed" reference "(Papyan et al.1)."** This is a parser-induced formatting artifact (garbled citation), not an author error, and is removed per guidelines.

- **Criticism that the paper does not report FNO without arc-mixup.** Table 4 (image) appears to include an "FNO" row without arc-mixup, based on the caption description. The reviewer may have missed this entry. The broader ablation concern (lack of controls isolating FDS) is retained as a Major weakness above.

- **Criticism that Theorem 1's proof structure borrowing is insufficient.** The paper says "maintaining a similar proof structure to Theorem 1 in Yang et al. (2022b)." This is a reasonable approach for a conference paper; the missing proof is already covered by the appendix removal rule.

## Novel Insights

The most interesting observation from the reviews is that the paper would be substantially stronger if it (a) demonstrated the ZNC phenomenon empirically with standard neural collapse metrics adapted to the non-negative orthogonal setting, and (b) methodically ablated which of the classifier's properties (fixedness, orthogonality, non-negativity, FDS) actually drives the empirical gains. The current review process reveals that the paper's theoretical framing and its empirical contributions are somewhat decoupled — the ZNC theory predicts how the FNO classifier *should* behave, but the experiments don't test this prediction directly. Bridging this gap would transform the paper from a collection of interesting ideas into a cohesive scientific contribution.

## Suggestions

1. **Show empirical evidence of ZNC.** Add a small-scale experiment (e.g., CIFAR-10/100 with FNO classifier) tracking adapted NC metrics: within-class variability, cosine similarity between class weight vectors and class means, and convergence to orthogonality in non-negative space. Even a single figure would substantiate the claim.

2. **Add ablations to isolate FDS.** Add at least: (a) FNO without any mixup, (b) FNO + standard (linear) mixup, (c) learnable classifier + arc-mixup, (d) fixed orthogonal classifier without non-negativity. This would clarify which component drives the improvement.

3. **Describe how the non-negative orthogonal matrix is constructed.** Provide the algorithm or explicit formula (Eq. 8) for generating a random non-negative orthogonal matrix, since this is central to reproducibility.

4. **Explain the large gains in continual learning.** Discuss whether hyperparameters were re-optimized for the FNO variant, and why FNO produces such a dramatic improvement over the learnable classifier baseline.

5. **Motivate the added constraint in Eq. 5.** Explain why ∑_{j≠k} h^T q_j^* ≥ 0 is needed in the OLPM formulation.

## Score and Decision

The paper presents a genuinely novel theoretical perspective (ZNC) for fixed orthogonal classifiers and a cleverly derived practical property (FDS) with two well-motivated applications. The empirical results are promising across multiple benchmarks. However, the contribution is undermined by (a) the absence of empirical validation for its central theoretical claim (ZNC), and (b) the lack of controlled ablations that would attribute the reported gains to FDS rather than to other confounded factors. These gaps prevent the paper from presenting a convincing causal narrative. The paper has the ingredients of a solid contribution but needs significant additional experimental work to substantiate its claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>