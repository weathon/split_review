- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3
Now I have all the information I need. Let me compose the final review.

## Summary

This paper proposes WIN, a LiDAR upsampling network that decouples the standard range-view representation into two orthogonal virtual views (Horizon Range View and Vertical Range View), performs implicit interpolation in each view, and fuses the results via a contrast selection module that probabilistically models per-point view confidence. The motivation is strong — single-view range-image interpolation loses geometric fidelity on vertical surfaces, edges, and ground planes — and the method achieves consistent improvements over prior SOTA (ILN) on both synthetic (CARLA) and real (KITTI) benchmarks, with growing advantages at higher upsampling scales.

## Strengths

- **Well-motivated and novel view-decoupling design**: The paper identifies a genuine limitation of range-view interpolation (geometric distortion from spherical projection) and addresses it by decoupling RV into two orthogonal projections (HRV, VRV). This is a simple but effective idea that is grounded in geometric reasoning (Section 3.3, Figure 1). The reuse of shared local features and separate lightweight MLPs keeps the parameter overhead minimal (+0.4M over ILN), making the approach practical.

- **Principled probabilistic fusion via contrast selection module**: Rather than using a hard binary classifier to select between views, the CSM models per-point confidence via a Gaussian-derived soft label (Eq. 7–8) and a sign-aware loss (Eq. 9). The ablation (Table 4) and loss curves (Figure 5) confirm that this probabilistic approach substantially outperforms binary cross-entropy, which diverges during training. This is a technically sound and non-obvious contribution.

- **SOTA quantitative results across multiple settings**: On CARLA (Table 1), WIN improves MAE by 4.53% and IoU by 7.01% over ILN with only 0.4M added parameters. The advantage grows at higher upsampling ratios (Table 2: e.g., 16→256 lines), consistent with the claim that view decoupling becomes more beneficial when distortion is more severe. Results on KITTI (Table 1) and on the downstream depth-completion task (Table 3) confirm generalization to real data and application-level benefit.

- **Ablation study cleanly isolates each component**: Table 4 systematically removes the variable-view design, the CSM, and the confidence loss, showing that each contributes to the final performance. The CSM alone contributes ~2.4% MAE improvement on average, and the full model always outperforms any single-view variant.

## Weaknesses

### Fatal
None.

### Major

- **The fusion equation (Eq. 6) is incomplete, impeding reproducibility.** The equation reads:
  ```
  R = { R_d   where G < 1/2,
  ```
  with an opening brace but no second case and no closing brace. The text around it describes the intent (select between R_d and R_z based on G), but the formal definition of the final range image is never completed. Additionally, variable ℛ_h is referenced in Section 3.1 ("back project the fused range images ℛ_h") but never formally defined. This is a concrete barrier for anyone trying to implement the method from the paper alone. The fix is straightforward (rewrite the equation with both cases and define ℛ_h), but it is essential to address before publication.

### Minor

- **The value of λ (Gaussian std-dev scaling constant) is not reported or ablated.** The confidence label (Eq. 7–8) depends on λ as the sole free parameter in the Gaussian model. The paper states "λ is a constant" but never gives its value or shows sensitivity analysis. Since the ablation shows that the confidence loss is critical to performance, the sensitivity of results to λ should be documented.

- **No variance or statistical significance is reported.** All tables report single numeric outcomes. It is not stated whether results are averaged over multiple runs, whether seeds were fixed, or whether performance differences are stable under re-training. While the improvement margins are large, the omission is a weakness for papers making comparison claims.

- **The specific depth completion algorithm used in the downstream task (Section 4.4) is not identified.** The paper describes the pipeline (downsample → upsample → complete → compare) but never names the depth completion method. While relative comparisons are valid if the same method was applied uniformly, the absolute numbers and the validation protocol cannot be assessed without this detail.

- **No qualitative results on KITTI.** Figure 4 shows CARLA qualitative comparisons only. Given the known projection issues on KITTI (non-unique projection center, discussed in Section 4.1), a qualitative comparison on real data would strengthen the claim that improvements are visually meaningful.

- **The claim that orthogonal views "provide more perspectives… without losing any geometric information" could be clarified.** The statement is technically true of the view representation itself — (d, z) is a bijection of (r, v) — but a reader could conflate this with the CSM's hard selection, which does discard one view's estimate per pixel. A brief clarification would prevent this confusion.

### Trivial

- **Table 4 row labels**: The "removing CSM" rows could be more clearly labeled as "HRV only" and "VRV only" rather than leaving the reader to infer which view corresponds to which row.
- **Line 158**: The gradient-interruption statement appears only at the end of Section 3.5; moving it earlier (when CSM is introduced) would help readability.
- **Line 24**: Typo "cooresponding."

## Nice-to-Haves

- A scatter plot or heatmap showing which view the CSM selects (ground vs. objects, edges vs. interiors) would visually validate the motivation that HRV is better at vertical surfaces and VRV at flat areas. The ablation already confirms this indirectly, but direct visualization would strengthen the contribution.
- A brief intuition for why binary cross-entropy fails on the selection task (beyond the empirical evidence in Figure 5) — e.g., a note about how the "best view" label changes during training due to different branch convergence speeds.
- Reporting inference runtime per point or per frame would back up the claim of "minimal memory and computation time" (line 34), which is stated but not quantified.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Reproducibility details for retrained baselines in supplementary are unavailable"** — Removed per hard rules: supplementary material is stripped by the parser and exists in the original submission. Criticisms about missing appendix content are not valid.
2. **"Why BCE doesn't work — no explanation given"** — Removed: the paper already addresses this empirically via ablation (Table 4) and loss curves (Figure 5). The critic's request for additional intuition is a nice-to-have, not a weakness.
3. **"The 'HRV/VRV descriptions are vague' — imprecise use of 'ignore z values'"** — Removed: the actual mathematical formulas are provided in Eq. 3 (lines 97–99), which makes the quantities precise. The textual description is a high-level summary, not a substitute for the equations.

## Novel Insights

The most interesting finding emerging from the reviews — and one the paper does not fully discuss — is that **most of the performance gain comes from switching from range-view interpolation to *any* of the orthogonal views, not from the fusion mechanism itself**. Table 4 shows that individual VRV-only performance already substantially exceeds RV-only (ILN), and the CSM adds a further ~2.4% MAE improvement on top. This suggests that the dominant contribution is the decoupling itself (eliminating spherical-projection distortion), while the CSM provides a meaningful but secondary refinement. This is a clean decomposition of the method's sources of improvement that the paper could highlight more explicitly.

## Suggestions

1. **Fix Equation 6** to show both cases of the selection explicitly: ℛ = ℛ_d if 𝒢 < 1/2, ℛ_z otherwise — and define ℛ_h as the resulting fused range image.
2. **Report the value of λ** used in experiments and add a sensitivity ablation varying λ over at least one order of magnitude.
3. **Add variance information** (e.g., 3-run means and std devs) to the main tables, or at minimum state whether results are stable across seeds.
4. **Name the depth completion method** used in the downstream pipeline (Section 4.4).
5. **Add KITTI qualitative results** to Figure 4 or a supplementary figure.
6. **Clarify the "without losing geometric information" phrasing** (Section 1, line 24) to distinguish representation equivalence from the CSM's per-pixel selection.
