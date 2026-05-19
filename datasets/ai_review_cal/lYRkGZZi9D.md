- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper analyzes why weight matching (WM) achieves linear mode connectivity (LMC) between independently trained neural networks. The authors first show empirically that WM reduces the L2 distance between models by only 6–20%, and a second-order Taylor expansion fails to predict the barrier, indicating distance reduction alone does not explain LMC. Through SVD analysis, they find that singular value spectra are nearly identical across independently trained models and that WM preferentially aligns singular vectors associated with large singular values. They connect this alignment to LMC by showing that inputs project more strongly onto these large-singular-value singular vectors, so aligning them suffices to keep per-layer outputs close. The paper extends the analysis to activation matching (AM) and contrasts with the straight-through estimator (STE), showing STE does not align singular vectors and therefore performs worse when merging three or more models.

## Strengths

1. **SVD-based reformulation of the WM objective (Theorem 4.1)**. The paper derives that minimizing the L2 distance between permuted weight matrices is equivalent to maximizing a weighted sum of inner products between their singular vectors, weighted by the product of corresponding singular values. This is a clean mathematical insight that reframes what WM is actually optimizing, and it provides the foundation for all subsequent analysis.

2. **Empirical demonstration that WM preferentially aligns large-singular-value singular vectors (Figure 2, R metric)**. Using the proposed alignment metric R with threshold γ, the paper shows that after WM, alignment is substantially higher for singular vectors with large singular values (γ=0.3) than when all singular vectors are considered (γ=0), and that without WM, alignment is near zero. This is direct quantitative evidence for the paper's central claim.

3. **Discovery that singular value spectra are nearly identical across independently trained models (Figure 1, Appendix Figure 7)**. This finding is clean and important: it establishes that the differences between models lie primarily in singular-vector orientation, not in the spectrum. This observation justifies the paper's focus on vector alignment and is a genuine contribution to the understanding of SGD solutions.

4. **Connecting singular-vector alignment to output similarity via input distributions (Theorem 4.2 + Figure 4)**. Theorem 4.2 bounds the per-layer output difference in terms of inner products between right singular vectors and inputs. Figure 4 empirically shows that inputs align with right singular vectors having large singular values. Together these pieces explain why aligning those particular singular vectors via WM leads to similar layer outputs, even when the full weight matrices remain far apart in L2 distance.

5. **Contrast with STE shows practical implications for multi-model merging**. The paper demonstrates that STE does not align singular vectors (Table 2, R ≈ 0), and this leads to a measurable disadvantage when merging three models (Table 3: WM achieves lower barriers between the non-anchor pair than STE, e.g., CIFAR-10 MLP: −0.098±0.040 for WM vs. 0.296±0.003 for STE). This is a clean empirical differentiation that goes beyond the core analysis to show practical relevance.

## Weaknesses

### Fatal
None.

### Major
1. **Causal framing exceeds the correlational evidence.** The paper's central contribution is phrased as "revealing the reason why WM and AM satisfy LMC" (abstract and contribution list). The evidence presented is correlational: WM aligns large singular vectors, the merged model inherits this alignment, and inputs project onto those vectors. Each piece is consistent with the hypothesis that alignment *causes* LMC, but the paper does not establish causation. No intervention experiment is performed (e.g., forcing alignment of only large singular vectors without minimizing full L2 distance, or taking a WM solution and breaking only the alignment of large singular vectors). The paper would be strengthened by either providing such causal evidence or systematically softening its framing (e.g., "evidence consistent with the hypothesis that..." or "a plausible mechanism is..."). The paper's own conclusion acknowledges that multi-layer propagation effects remain unclear, which further undermines the strength of the causal claim. This is the most significant weakness.

2. **The quantitative relationship between the R alignment metric and barrier reduction is not established.** The paper shows that WM produces modest R values (around 0.2 for VGG11 and ResNet20 at γ=0.3) and that barriers are low, but it never plots barrier vs. R across multiple runs to demonstrate a monotonic or otherwise systematic relationship. Without this, a reader cannot assess whether the observed degree of alignment is sufficient to explain the observed barrier, or whether alignment could be an epiphenomenon that happens to correlate with LMC without being its cause. The paper acknowledges the modest R values but does not quantify what level of alignment is "enough."

3. **The analysis is per-layer, with no treatment of multi-layer propagation effects.** Theorem 4.2 bounds the per-layer output difference, but the paper does not analyze how this bound propagates through multiple layers or whether alignment at each layer independently suffices to keep the full-network outputs close. The authors acknowledge this in the conclusion ("it remains unclear why our analysis can explain the phenomenon so effectively"), which is honest, but it means the central explanatory chain has a significant gap. Steps (ii)→(iii)→(iv) in the argument (per-layer alignment → per-layer output closeness → full-network output closeness → low barrier) are connected by intuition, not by analysis.

### Minor
1. **The three-model experiment is a single comparison.** The paper's claim that WM is "more advantageous" than STE for three or more models rests on one experimental comparison (Table 3) with one architecture and dataset per condition, without statistical tests or variation of architecture, dataset, or number of models. The data are consistent with the paper's theory but insufficient to confirm it over alternative explanations (e.g., STE simply finding worse local minima for the 3-way objective).

2. **The R metric definition has unanalyzed properties.** The paper says "if R is close to one, the singular vectors are well-aligned," but the metric sums over all i,j pairs, including cross terms (i≠j). For independently trained models, singular vectors from different models are not orthogonal to each other, so cross-term contributions are not guaranteed to be zero even with perfect per-index alignment. An analysis of what R=1 actually requires, or an alternative metric that isolates diagonal alignment, would strengthen the paper.

3. **The threshold γ=0.3 is arbitrary and only two values (0 and 0.3) are compared.** The paper's central claim that WM "preferentially aligns large singular vectors" depends on showing higher R at higher γ. Showing this for only a single nonzero threshold weakens the evidence — it could be that R gradually increases with γ, or that 0.3 happens to be a special point. Results for a sweep of γ values (e.g., 0, 0.1, 0.2, 0.3, 0.5, 0.7) would be more informative.

4. **The AM analysis is suggestive but not probative.** The paper shows that AM produces similar R values and barriers to WM, and concludes the "reason AM achieves LMC is likely to be similar to that for WM." This is a reasonable suggestion but lacks a direct analysis of whether AM's permutation solutions converge toward the same kind of singular-vector alignment. The similarity could be coincidental.

### Trivial
None.

## Nice-to-Haves

1. **Intervention experiment**: Forcing alignment of only the top-k singular vectors (without full distance minimization) and testing whether LMC emerges would turn the correlational evidence into causal evidence.
2. **Barrier vs. R scatter plot**: Showing barrier as a function of R across many random seeds would reveal whether the relationship is monotonic, as the hypothesis predicts.
3. **Separate analysis of left vs. right singular vectors**: Since right singular vectors directly interact with inputs, distinguishing their contribution from that of left singular vectors would clarify the mechanism.
4. **Multi-layer bound or simulation**: Even a simplified analysis of how per-layer alignment propagates through multiple layers would strengthen the explanatory chain.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that the Taylor-approximation argument is a "straw man."** The harsh critic argued that no prior work claimed WM reduces distance enough for a quadratic approximation to hold, so the experiment does not advance the positive thesis. However, the paper directly cites Zhou et al. (2023), who argued that WM finds permutations approximately satisfying commutativity (exact zero distance). Showing that distance reduction is only 6-20% and that a second-order expansion fails is a valid refutation of the claim that commutativity/distance-reduction is the mechanism. The experiment serves its stated purpose: motivating the need for a better explanation. This criticism is factually inaccurate and is removed.

- **Criticism about the R metric's denominator and cross-term interpretation.** The harsh critic claimed the metric's denominator Σ n_ℓ implies R=1 means perfect alignment but that cross terms (i≠j) could prevent this interpretation. However, when i=j and vectors are perfectly aligned, (u_i)^T(P u_j)=1 and (v_i)^T(P v_j)=1, yielding R=1 regardless of cross terms. The paper's interpretation of "R close to 1 means well-aligned" is standard for a correlation-style metric and is not misleading.

- **Generic "strengths" from the Strength Finder that are generic/superficial** — e.g., claims about the paper addressing an important problem. These are removed as they lack specific content anchored to the paper's contributions.

- **Criticism about learning rate and weight decay being "sketched but not developed."** The paper mentions these observations and states they are addressed in Appendix Sections 4-5, which are missing due to parser truncation. This is not assessable from the available text, so the criticism is removed.

- **Criticism about missing statistical tests.** The paper reports means and standard deviations over 3-5 trials and uses t-tests in Table 1. For an empirical analysis paper operating within standard experimental norms, this is adequate. Requesting more extensive statistical machinery is a scope-creep nitpick.

- **Criticism about the Taylor-approximation not advancing the positive thesis.** As noted above, the section serves to motivate the analysis, not to prove the positive thesis. This is a standard scientific paper structure.

## Novel Insights

The harsh critic's suggestion to run an intervention experiment (forcing alignment of large singular vectors only) is a genuinely useful methodological insight that the paper itself does not consider. The critic correctly identifies that the paper's evidence chain is correlational and that a causal claim requires stronger experimental design. This is not a novel insight about the phenomenon itself but a valuable observation about how the paper could be strengthened. Otherwise, the paper's own contributions (SVD reformulation of WM, recognition that singular-value spectra are near-identical across seeds, preferential alignment of large singular vectors) are the novel elements here; the reviews do not surface additional scientific insights beyond the paper's own content.

## Suggestions

1. **Reframe the central claim** from "revealing the reason why" to "presenting evidence consistent with a mechanism where" or "proposing and empirically supporting an explanation." This would align the paper's language with the actual strength of the evidence.

2. **Add a scatter plot** of barrier vs. R across multiple random seeds (or training hyperparameters) to show a monotonic or systematic relationship between alignment and connectivity.

3. **Sweep the γ threshold** over a wider range (0, 0.1, 0.2, 0.3, 0.5, 0.7) to demonstrate the trend is not dependent on a single arbitrary choice.

4. **Expand the three-model experiment** to include at least one additional architecture-dataset combination per category to support the claim about WM's multi-model advantage.

5. **Acknowledge the correlational nature of the evidence more explicitly** in the abstract and introduction, and note that intervention experiments would be needed to establish causation.
