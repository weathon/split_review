Now I have all the evidence needed. Let me compose the final consolidated review.

## Summary

This paper identifies the phenomenon of **local dimensional collapse** in self-supervised learning — where representations may globally span a high-dimensional space but collapse in the vicinity of individual data points. The authors derive an asymptotic Fisher-Rao metric for comparing local distance distributions, which leads to theoretical insights (LID values should be compared on a logarithmic scale, aggregated via the geometric mean). They propose **LDReg**, a regularizer that increases the local intrinsic dimensionality (LID) of encoder representations, and show consistent (if small) improvements across SimCLR, BYOL, and MAE on ImageNet and transfer tasks.

## Strengths

1. **Identifies local dimensional collapse as a phenomenon distinct from global collapse, with real empirical evidence.** The paper shows that BYOL achieves a high effective rank (583.8/2048, indicating minimal global collapse) but a low geometric-mean LID (15.9, indicating significant local collapse). This contrast between global and local measures is a concrete demonstration that global metrics alone miss locally collapsed representations (Figures 2c–d in the paper). This goes beyond prior work that studied collapse only at the representation-subspace level.

2. **Provides a principled theoretical derivation connecting Fisher-Rao geometry to LID aggregation.** Lemma 1 derives the exact Fisher-Rao distance between asymptotic tail distributions as |ln(θ₂/θ₁)|. Theorem 2 and Corollary 1 show that under this metric, the Fréchet mean of a set of local distance distributions corresponds to the geometric mean of their LIDs, and logarithmic averaging is the natural aggregation rule. This elegantly justifies the LDReg loss formulation.

3. **Consistently improves downstream performance across multiple SSL paradigms, architectures, and training regimes.** LDReg improves linear evaluation accuracy on ImageNet for SimCLR (+0.5%), SimCLR-Tuned (+0.3%), BYOL (+0.9%), and MAE (+0.6%) at standard 100/200-epoch schedules (Table 1). With longer 1000-epoch training, gains are larger (+0.8% ImageNet, +4.3% Stanford Cars, Table 2). LDReg also improves COCO object detection and segmentation (Table 3). The method works on both ResNet-50 and ViT-B, and across sample-contrastive (SimCLR, BYOL) and generative (MAE) methods, demonstrating generality.

4. **Computationally lightweight and easy to integrate.** LDReg adds only LID estimation within each batch (pairwise distances with k=64 neighbors) and a simple regularization term. It requires no architectural changes and can be plugged into existing SSL methods by adding one loss term with a single hyperparameter β.

## Weaknesses

### Fatal
None.

### Major
None. The paper has a coherent core contribution, a sound theoretical framework, and empirical support across multiple settings.

### Minor

1. **No error bars or multiple-seed results.** The main ImageNet linear evaluation gains are modest (+0.3% to +0.9% at 100 epochs). Without standard deviations or multiple seeds, it is impossible to assess whether these improvements exceed run-to-run variation. The 1000-epoch results show larger gains, but these are also single-run. This is the single most impactful improvement the authors could make.

2. **No ablation studies for key hyperparameters.** The neighborhood size $k$ (fixed at 64) and balancing coefficient $\beta$ (one value per method) are not varied. The $L_1$ vs $L_2$ regularization variants are described theoretically but never compared experimentally. Ablations are standard for any method with tunable hyperparameters and would substantially strengthen empirical rigor.

3. **No experimental comparison with alternative collapse-mitigation techniques.** Global-collapse mitigators such as VICReg, Barlow Twins, or spectral normalization are mentioned in related work but never compared. A direct comparison (even on a single dataset) would contextualize LDReg's benefits against existing approaches.

4. **The claim that local collapse is a distinct problem would benefit from a cleaner controlled experiment.** The BYOL result (high effective rank + low LID) is suggestive, but the paper does not include an experiment where a method known to prevent global collapse is shown to still suffer local collapse, and then LDReg is shown to fix local collapse while preserving the global property. Such an experiment would strengthen the central conceptual narrative. (As is, LDReg increases *both* local and global measures, which is consistent with a generic dimensionality regularizer.)

5. **No discussion of computational overhead, batch-size sensitivity, or limitations.** LID estimation scales quadratically with batch size (pairwise distances within a batch of size 2048–4096). The paper does not report runtime or memory costs, nor does it discuss how small batch sizes might affect LID estimates. A limitations paragraph acknowledging the modest effect sizes, the added hyperparameter $\beta$, and potential interference between LDReg and the SSL objective would improve credibility.

6. **The choice of applying LDReg to encoder (rather than projector/decoder) representations is stated but not analyzed.** The paper notes that "only the encoder is kept for downstream tasks" (line 442), which is a sensible design choice, but does not discuss whether regularizing the encoder space while SSL losses operate on projected/decoded spaces could cause interference or whether alternative choices would work as well.

### Trivial

- The $L_2$ loss in Eq. (2) maximizes the Fréchet variance (average of squared log-LIDs), but the actual loss uses the square root of this quantity (RMS). Since the square root is monotonic, the optimization direction is identical — the inconsistency is cosmetic and does not affect the method.

## Nice-to-Haves

- A controlled experiment isolating local from global collapse (e.g., combining LDReg with a method that already enforces global decorrelation) would sharpen the paper's conceptual contribution.
- A discussion of why the $L_1$ vs $L_2$ choice matters (or does not matter) from an optimization perspective.
- The asymmetric relationship between LID increases and accuracy gains (e.g., BYOL LID jumping from ~16 to ~22 for only +0.9% accuracy) is worth a brief analysis.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The claimed distinction between local and global collapse is not convincingly demonstrated — rests on a single synthetic example."** The paper does provide real empirical evidence: BYOL's high effective rank (583.8) vs. low LID (15.9) in Figures 2c–d. The synthetic example is labeled as an illustration, and the quantitative evidence for real SSL models is in Section 6. The reviewer's claim ignores the BYOL results.

- **"The observation about local collapse is not quantitatively established for real SSL representations (Section 1 note)."** The introduction previews the phenomenon; the quantitative evidence appears later in Section 6. This is standard paper structure, not a flaw.

- **"Figure 2a: LID increase from ~16 to ~22 for BYOL but accuracy gain only +0.9%."** This is an observation about the non-linear relationship between LID and accuracy, not a weakness. The paper never claims a linear relationship.

- **"MAE effective rank doubles but accuracy improves by only 0.6%."** Same as above — this is an interesting finding about the shape of the benefit, not a flaw in the paper.

- **"The Fréchet variance vs RMS concern is a methodological gap."** The square root is a monotonic transformation; maximizing variance and maximizing RMS are equivalent. This is a terminological imprecision, not a gap that weakens the science.

- **"The paper does not discuss whether the Fisher-Rao result is already well-known in the LID literature."** The paper cites Bailey et al. (2022) and discusses KL divergence alternatives. The derivation is claimed as novel, and the reviewer provides no evidence that it is not.

## Novel Insights

The reviews surface an important tension that the paper itself does not fully address: the relationship between LID and downstream accuracy appears to be highly non-linear and method-dependent. BYOL's LID increases by ~40% but accuracy by only 0.9%, while SimCLR's 1000-epoch results show much larger accuracy gains from similar LID increases. This raises a deeper question — what is the *mechanism* by which higher LID improves representations, and under what conditions does it help most? The paper's theoretical framework (Fisher-Rao → geometric mean) suggests logarithmic aggregation is natural, but the empirical results hint that the *distribution* of LIDs (not just the geometric mean) may matter. This could be a promising direction for follow-up work.

## Suggestions

1. **Add error bars or multiple-seed results** for the main ImageNet linear evaluation (Table 1) and the key transfer results. Even 2–3 seeds with standard deviations would substantially increase confidence, especially given the modest gains at 100 epochs.

2. **Include hyperparameter ablations** varying $k$ (e.g., 16, 32, 64, 128) and $\beta$ (e.g., 0.5×, 1×, 2× the reported value), plus an $L_1$ vs $L_2$ comparison. A small-scale study on ImageNet with 50 epochs would suffice.

3. **Add a limitations paragraph** acknowledging the modest effect sizes, the added hyperparameter, the lack of error bars, and the potential for LDReg to interfere with the base SSL objective.

4. **Consider a controlled experiment** where LDReg is applied on top of a global-collapse preventer (e.g., Barlow Twins or a spectral-regularized SimCLR) to demonstrate that LDReg provides additive benefit by specifically addressing local collapse.

## Score and Decision

The paper makes a genuine conceptual contribution (identifying local vs. global dimensional collapse), provides a clean theoretical framework (asymptotic Fisher-Rao metric → logarithmic geometric-mean aggregation), and shows consistent — if modest — improvements across multiple SSL methods. The weaknesses are matters of experimental rigor and presentation, not structural flaws. The paper would benefit substantially from error bars and ablation studies, but the core contributions are valid and interesting.

**Score**: 6.0 (Accept)

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>