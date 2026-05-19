## Summary
This paper tackles the massive storage footprint of 4D Gaussian Splatting (4DGS) with two complementary ideas: (1) replacing the expensive 144-parameter 4D spherical harmonics color representation with a per-Gaussian 3-parameter DC color component plus a lightweight shared MLP "AC" predictor, and (2) an entropy-constrained deformation technique that expands each Gaussian's action range while using an opacity-based entropy loss to prune redundant Gaussians. Results show dramatic compression (up to 190× on Technicolor, 125× on Neu3DV) while maintaining rendering quality close to the original 4DGS and real-time speeds.

## Strengths
1. **DC-AC color decomposition cuts per-Gaussian parameters by ~8× while maintaining or improving quality.** Original 4DGS dedicates 144 parameters to 4D spherical harmonics; MEGA replaces them with 3 DC color parameters plus a three-layer MLP. On *Birthday* (Table 2 ablation), "w/ DAC" achieves PSNR 31.60 vs. 4DGS 31.00 while total parameters drop from 2093.56M to 308.65M — a ~6.8× reduction with a quality *gain*. This directly validates the central design choice.

2. **Entropy-constrained deformation reduces Gaussian count by >10× while improving rendering quality.** The full pipeline on *Birthday* (ablation Table 2) cuts Gaussians from 13.00M (4DGS) to 0.91M and raises PSNR from 31.00 to 32.02. Figure 2(a) shows the Gaussian participation ratio increases from <50% to ~75%, directly demonstrating that the deformation field expands each Gaussian's action range.

3. **Storage reductions of ~190× (Technicolor) and ~125× (Neu3DV) with real-time rendering speed.** Table 1 reports MEGA uses 32.45 MB vs. 4DGS 6107.07 MB on Technicolor (50 frames); Table 2 reports 25.05 MB vs. 3128.00 MB on Neu3DV (300 frames). Simultaneously, rendering speed reaches 83 FPS (Technicolor) and 77 FPS (Neu3DV) — competitive with 4DGS and well within real-time range.

4. **Opacity entropy loss effectively prunes redundant Gaussians without degrading quality.** On *Fabien* (Table 2 ablation), "w/ DAC+ℒₒₚₐ" reduces Gaussians from 4.57M to 2.32M while PSNR stays within 0.25 dB of the unregularized variant, validating that binary-entropy regularization successfully isolates non-contributing Gaussians.

5. **Simple half-precision and zip delta compression provide a clean ~10% storage reduction.** Section 3.3 explicitly documents these off-the-shelf post-processing steps, making the pipeline practical and reproducible.

6. **Comprehensive four-scene, two-dataset ablation isolates each component's contribution.** Table 2 systematically tests DAC alone, deformation alone, opacity loss alone, and their combinations, revealing the key design insight: deformation without entropy loss causes Gaussian proliferation, while the joint configuration is essential for the large reduction.

## Weaknesses
### Fatal

None.

### Major

None.

### Minor

1. **Per-scene quality variance is acknowledged implicitly (via ablation data) but not discussed.** On *Flame Steak* (ablation, Table 2), the full method reaches 32.27 dB PSNR vs. 4DGS's 33.19 dB — a 0.92 dB drop that is more than the "comparable" framing in the abstract suggests. The paper's average numbers (Technicolor: +1.5 dB; Neu3DV: −0.08 dB) fairly represent the overall trade-off, but the *Flame Steak* outlier is not discussed. Adding a brief note on which scene types challenge the method would strengthen the paper.

2. **Equation (5) uses "×" for quaternion deformation without specifying the operation.** For the center μ₄D and scale s₄D, element-wise multiplication is clear. For quaternions (qₗ, qᵣ), "×" could mean quaternion multiplication or scaling. This should be specified for reproducibility.

3. **Deformation predictor takes view direction as input, but cross-view consistency is not analyzed.** The deformation predictor (Eq. 3) takes γ(sg(𝒅ᵥ)) as input, meaning a Gaussian's position, scale, and rotation can vary with viewpoint. This is an unusual design choice — in standard 4DGS, geometry is time-dependent but not view-dependent. The reported metrics suggest it works, but the paper does not discuss whether this leads to cross-view inconsistencies (e.g., a point appearing in different locations from different viewpoints). A simple analysis would strengthen the paper.

4. **Frequency positional encoding L is not specified.** The paper defines γ as (sin(2^l π p), cos(2^l π p))_{l=0}^{L-1} (Eq. 3) but never gives the value of L. This is needed for exact reproduction.

5. **Stop-gradient rationale is not explained.** The sg(·) operators on μ₃D and 𝒅ᵥ (Eq. 2) and on μ₄D and 𝒅ᵥ (Eq. 3) are noted but not justified. The likely reason (preventing position/view gradients from destabilizing the predictors) is a short sentence away.

6. **STG comparison on Neu3DV could be framed more precisely.** MEGA achieves 31.49 PSNR and 77 FPS on Neu3DV, while STG achieves 32.04 PSNR and 273 FPS — MEGA wins heavily on storage (25 MB vs. 175 MB) but trails on quality and speed. The paper's text ("higher rendering quality and smaller storage overhead compared to most Gaussian-based methods") is technically accurate ("most" — MEGA beats 4 of 5 Gaussian methods), but a direct acknowledgment of the STG trade-off on this dataset would improve clarity.

7. **The C-D3DGS entry in Table 2 shows PSNR 30.46 with LPIPS 0.1500, which is substantially worse on LPIPS than other methods at similar PSNR.** This may be a valid result from the original paper, but the authors might want to double-check this number.

### Trivial

- None beyond the minor points above (none of which are formatting/style issues).

## Suggestions
1. Specify the quaternion deformation operation (Eq. 5) — element-wise multiplication, quaternion multiplication, or normalization+re-normalization.
2. Report the positional encoding L value.
3. Add a brief paragraph discussing per-scene variance in the quality-compression trade-off, citing *Flame Steak* as an example and hypothesizing why (e.g., turbulent motion, fire/smoke dynamics).
4. Include a brief note on cross-view consistency — either an explicit check or a justification for why view-dependent deformation does not cause instability.
5. Clarify the stop-gradient rationale in one sentence.
6. On Neu3DV, add a sentence directly comparing to STG on quality and speed (not just storage) for full transparency.

---

**Evaluation axes:**
- **Originality:** Strong. First work to systematically compress 4DGS with DC-AC decomposition and entropy-constrained deformation.
- **Importance of research question:** High. 4DGS produces gigabytes of storage; practical deployment demands compression.
- **Claims well supported:** Yes. Claims are backed by clear numbers, comprehensive ablation, and two datasets. Minor overclaim on "comparable" for one outlier scene.
- **Soundness of experiments:** Solid. Appropriate baselines, proper metrics, thorough ablation.
- **Clarity of writing:** Good. Method description is clear; a few technical details (quaternion operation, L value) need specification.
- **Value to community:** High. The storage reductions (125–190×) are practically meaningful, and the DAC + deformation+entropy design is transferable.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
