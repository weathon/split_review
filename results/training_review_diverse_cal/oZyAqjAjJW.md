Now I have a thorough understanding of the paper and can verify the reviewer claims directly. Let me write the consolidated review.

## Summary

This paper identifies and formalizes **local dimensional collapse** in self-supervised learning (SSL) — the phenomenon where representations maintain high global dimensionality but collapse locally around individual data points. The authors propose LDReg, a regularizer that increases the local intrinsic dimensionality (LID) of representations. The regularizer is grounded in a novel derivation of an asymptotic Fisher-Rao metric for LID distributions, which reveals that LID values should be compared on a logarithmic scale and aggregated via the geometric mean. Empirically, LDReg shows consistent improvements across four SSL methods (SimCLR, SimCLR-Tuned, BYOL, MAE) on ImageNet linear evaluation, transfer learning, and COCO detection/segmentation.

## Strengths

1. **Identifies and formalizes local dimensional collapse as a distinct phenomenon in SSL.**  
   Prior work focused on global dimensional collapse (e.g., effective rank). This paper shows that representations can have high global intrinsic dimension while collapsing locally (Figure 1c, synthetic example) and that BYOL — despite resisting global collapse — exhibits low mean LID (Figure 2c–d). This is a genuinely new observation that motivates a different regularization target.

2. **Provides a principled theoretical framework linking LID to the Fisher-Rao metric, yielding the geometric mean as the natural aggregation for LID values.**  
   Lemma 1 derives the Fisher-Rao distance for tail distributions; Definition 3 defines the asymptotic Fisher-Rao metric; Theorem 1 and Corollary 1 show that the Fréchet mean under this metric equals the geometric mean of LIDs. This provides a non-trivial theoretical justification for why LDReg operates on the logarithm of LID rather than raw LID.

3. **Consistent empirical improvements across diverse SSL methods and evaluation protocols.**  
   LDReg improves linear evaluation accuracy for SimCLR (+0.5pp), SimCLR-Tuned (+0.3pp), BYOL (+0.9pp), and MAE (+0.6pp) on ImageNet (Table 1). It also improves transfer learning (Table 2) and COCO detection/segmentation (Table 3). The improvement on BYOL is particularly notable because BYOL already resists global collapse, confirming that local regularization addresses a distinct problem.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Which regularizer variant (L₁ or L₂) was used in experiments is not specified.**  
   Section 5 presents both L₁-style regularization (−β·(1/N)Σ ln ID) and L₂-style regularization (−β·(1/N·Σ (ln ID)²)^{½}) as options, but the experiments (§6) refer only to "LDReg" without stating which variant was deployed. The hyperparameter β is given per method, but without knowing which loss form was used, the results are not fully reproducible. The authors should clarify this in the rebuttal.

2. **No sensitivity/ablation analysis for the neighborhood size k and regularization strength β.**  
   The paper uses k=64 as a default and reports specific β values for each method, but provides no analysis of how results vary with these choices. LID estimates are sensitive to k, and the regularizer's effect depends on β. At minimum, an ablation on k (e.g., {16, 32, 64, 128}) and β for one baseline (e.g., SimCLR on ImageNet) would substantiate the method's robustness.

3. **The asymptotic theory is not empirically validated for the finite-sample regime used in practice.**  
   The theoretical development (§4) relies on the limit w→0⁺, but the LID estimator in practice uses distances to the k-th nearest neighbor within a training batch, where w is not arbitrarily small — especially early in training. This gap between asymptotic theory and finite-sample estimation is a standard limitation in the LID literature, but the paper does not discuss it or provide empirical validation (e.g., checking whether FR distances computed with estimated LIDs approximate the log-ratio form for finite w). A brief acknowledgment or a synthetic-data sanity check would strengthen the paper.

4. **Empirical gains are modest (0.3–0.9pp), and the improvement mechanism for BYOL is not fully explained.**  
   The gains on ImageNet linear evaluation are small but consistent across methods. The BYOL case is the most interesting — BYOL has high effective rank but low LID, and LDReg raises both LID (+40% geometric mean increase from 15.9 to 22.3) and accuracy (+0.9pp). However, the paper does not explain *why* increasing LID should translate to better classification accuracy, beyond the general intuition that higher-dimensional representations are more expressive.

### Trivial

- The notation $\IDstar_F$ is used both as a limit quantity (§4) and as an estimated quantity from finite samples (§5), with only a brief transition between the two. Clarifying this distinction would improve readability.
- In the caption of Figure 2, subfigures (a)–(b) are described as computed on the training set, but the surrounding text ("the geometric mean of LID values over training epochs") is ambiguous about whether the validation set is also used. Error bars are absent across runs.

## Nice-to-Haves

- **Applying LDReg on top of dimension-contrastive methods** (e.g., Barlow Twins or VICReg) would sharpen the central claim that local regularization provides complementary benefits beyond what global decorrelation already achieves. This is scope-creep relative to the current paper but would be a natural follow-up.
- **Computational overhead analysis**: LID estimation requires O(B²) nearest-neighbor distances per batch. Reporting wall-clock training times for one baseline with/without LDReg would help practitioners assess the cost.
- **A brief justification of the LID estimator**: The formula $\widehat{\text{ID}} = -\mu_k/(\mu_k - w_k)$ is cited to Amsaleg et al. but a one-sentence explanation (method-of-moments for a Pareto-type tail) would improve self-containedness.

## Removed Points

- **Criticism about missing comparison with Barlow Twins/VICReg as alternative methods**: Removed because it evaluates the paper against the wrong class of expectations. LDReg is a *regularizer* designed to be added to existing SSL methods, not a standalone SSL method. The paper's evaluation (same method ± LDReg) is the appropriate design for testing a regularizer's contribution. Comparing SimCLR+LDReg against Barlow Twins would not isolate LDReg's effect and is not the paper's claimed contribution.
- **Criticism that the paper should have been included in a separate section:** Not applicable.
- **Generic strengths from the Strength Finder that were dropped:** None — all three identified strengths are specific, evidence-backed, and conflict with no verified weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's central thesis — that local dimensional collapse is a real and distinct phenomenon — and surface the expected concerns about asymptotic theory and missing ablations, without revealing any unaddressed fatal flaw or alternative interpretation that the authors missed.

## Suggestions

1. **Specify which regularizer variant (L₁ or L₂) was used in all experiments**, and if both were tried, report which produced the results shown.
2. **Add an ablation table** showing linear evaluation accuracy for SimCLR on ImageNet with varying k (e.g., {16, 32, 64, 128}) and β (e.g., {0.001, 0.005, 0.01, 0.05}) to demonstrate robustness.
3. **Add a brief discussion or synthetic-data experiment** validating that the asymptotic FR distance formula holds approximately for finite w values encountered during training, or at least acknowledge the limitation overtly.

## Score and Decision

The paper makes a genuine contribution: it identifies and formalizes local dimensional collapse, provides a theoretically grounded regularizer, and demonstrates consistent (if modest) improvements across multiple SSL families. The weaknesses are real but addressable — missing variant specification, absent ablations, and an unvalidated asymptotic gap — none threaten the paper's core claims. The theoretical development is a strength, not a weakness, and the empirical strategy (evaluating LDReg as an add-on to existing methods) is the correct one for a regularizer. The paper is a solid accept.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>