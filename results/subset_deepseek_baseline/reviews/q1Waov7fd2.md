## Summary

The paper proposes Normalized Matching Transformer (NMT), a pipeline for sparse keypoint matching that combines a Swin-transformer backbone, SplineCNN geometric feature refinement, and a normalized transformer (nGPT) with layer-wise hyperspherical normalization. It is trained with InfoNCE and hyperspherical uniformity losses, and uses a differentiable Sinkhorn decoder at inference. The authors claim state-of-the-art results on PascalVOC and SPair-71k, outperforming BBGM, ASAR, COMMON, and GMTR by 5.1% and 2.2% respectively, while converging in 1.7× fewer epochs.

## Strengths

- The idea of enforcing unit-norm embeddings throughout the transformer layers and combining contrastive with hyperspherical losses is well motivated for the keypoint matching task, where cosine similarity is the natural metric.
- The ablation study clearly isolates the contribution of each component (backbone, transformer normalization, losses, augmentations).
- The architecture is conceptually clean—no complex combinatorial solver is needed at training time, and the Sinkhorn decoder is used only at inference.

## Weaknesses

### Fatal

1. **Dataset mismatch and absent baseline comparisons.** The abstract claims state-of-the-art on *Pascal3D+*, but the experiments are conducted on *PascalVOC* (with Berkeley annotations). More critically, the paper claims to outperform BBGM, ASAR, COMMON, and GMTR by specific margins, but *none of these baselines appear in the main result tables* (Tables 2 and 3). Instead, Table 2 includes GMM-PL, PAA, GLM-NE, CE, HBGM, CGMPT, and COMMON; Table 3 includes DMG, BIGM, CMTR, and COMMON. The claimed improvements are therefore unsubstantiated by the presented evidence.

2. **Suspicious table entries.** In Table 2, CGMPT and COMMON are reported as having exactly 75.2% accuracy for *every single object category*—a scenario that is practically impossible for a real method on PascalVOC. This suggests a formatting error or, if not, invalidates the reported numbers. Similarly, Table 3 contains anomalous icon‑placeholders and incomplete entries, making the results untrustworthy.

3. **Inconsistency between abstract claims and reported numbers.** The abstract states a 5.1% improvement on PascalVOC, yet the highest baseline in Table 2 (HBGM) is 80.6% and the authors’ method is 88.7% (a 8.1% absolute increase). The claimed baselines (BBGM, ASAR, COMMON, GMTR) are missing, so the claimed margin cannot be verified from the provided data.

### Major

- **No error bars or statistical significance.** All results are given as single numbers without variance, making it impossible to assess the robustness of the improvements.
- **Missing reproducibility details.** The validation set is described as “1000 image pairs per class,” but the selection process and whether it is held-out from the training set are not specified. The intersection filtering rule is mentioned but not compared against alternative protocols used by baselines.
- **The “faster convergence” claim is not supported by wall‑clock time.** Only epoch counts are given (6 vs. 10–16), but the authors note that the normalized transformer may be slower per epoch due to kernel fusion. Without wall‑clock measurements, the practical training advantage is unclear.
- **Loss definition is unclear.** Equation (3) defines the hyperspherical loss using the cosine similarity matrix \(C\) from Equation (2), but Equation (2) defines \(C\) as cross‑image similarities, while the loss is described as separating keypoints within the *same* image. The notation conflates the two roles; the actual computation is ambiguous.

### Minor

- The algorithm listing includes `Norm. Self-Attn(f^i, f_global^i)` but the transformer formulas in Section 3 do not accept a global feature token; the global feature is later used after cross‑attention.
- The paper claims “pure ML-based architecture” yet relies on Sinkhorn (an optimization algorithm) during inference; this is not a flaw but the phrasing is slightly overstated.
- Figure 1 caption contains a fragment “Weights during” that is not explained.

### Trivial

- Some Greek letters in Table 2 are used as category names (α, β, … ω) instead of the usual class names, making the table hard to read.
- Reference list is truncated (only first 20 references shown, rest removed).

## Nice-to-Haves

- Ablation on the number of transformer layers and the weighting parameter \(p\) in the layer loss would deepen understanding.
- Comparison against the claimed baselines (BBGM, ASAR, GMTR) using the same evaluation protocol is essential.
- Reporting standard deviations over multiple runs would strengthen the conclusions.

## Novel Insights

Beyond its own contributions, the paper does not offer a fundamentally new analytical insight into why layer‑wise hyperspherical normalization helps keypoint matching; the justification is largely empirical. The main novelty is the combination of existing components (Swin, SplineCNN, nGPT, InfoNCE, hyperspherical loss) into a single pipeline, which is a useful engineering contribution but not a conceptual breakthrough.

## Suggestions

1. **Fix the experimental presentation.** Include the claimed baselines (BBGM, ASAR, GMTR) in the main table. Remove or correct the uniformly‑valued entries for CGMPT and COMMON. Ensure the dataset name matches (PascalVOC, not Pascal3D+).
2. **Report wall‑clock training time** alongside epochs to substantiate the faster convergence claim.
3. **Clarify the loss computation** by providing explicit pseudocode or separate equations for the within‑image hyperspherical loss.
4. **Add error bars** (e.g., over 3 random seeds) for the main results and ablations.

## Score and Decision

**Score:** 3 (Reject)

The paper has multiple fatal weaknesses: the claimed state‑of‑the‑art improvements are not supported by the presented baselines, the main tables contain highly suspicious entries, and the dataset in the abstract contradicts the experiments. Even ignoring these issues, the experimental validation is incomplete (no error bars, missing baselines, ambiguous loss definition). While the architectural idea has merit, the current form of the paper cannot be trusted to deliver the claimed contributions.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>