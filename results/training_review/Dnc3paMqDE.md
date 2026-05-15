Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces DeepSPF, a learnable encoder for 3D point clouds that represents a point cloud as a collection of rotation-equivariant spherical patches (Spherical Patch Fields, SPF) and proposes a Patch Gaussian Layer (PG-Layer) for adaptive multi-scale encoding. The encoder is evaluated on registration, retrieval, and completion tasks on ModelNet40, ShapeNet, and Scan2CAD, showing consistent improvement when replacing baseline encoders (PointNet, SGPCR) in existing pipelines.

## Strengths

- **Well-motivated patch-wise rotation-equivariant representation.** The idea of extending global spherical Gaussian representations to local, learnable patches with graph-based inter-patch and intra-patch relations is a natural and promising extension of prior work (Salihu & Steinbach, 2023). The three issues identified (pose-agnostic features, fixed patches, zero correspondence) are legitimate limitations in existing approaches.

- **Consistent improvements across three diverse tasks.** DeepSPF reduces rotation error by ~50% relative to DeepGMR on zero-intersection ModelNet40 registration (RRMSE 0.027 vs. 0.057, Table 1), improves Top-1 retrieval Chamfer Distance on ShapeNet from 0.0272 to 0.0225 (Table 4), and raises completion F-score on seen ShapeNet data from 0.472 to 0.568 (Table 5). These gains are achieved by swapping only the encoder while keeping decoders and loss functions fixed.

- **Real-world validation on Scan2CAD.** Beyond synthetic benchmarks, the method achieves +3.6% absolute alignment accuracy on the Scan2CAD benchmark (19.5% vs. 15.9%, Table 3), providing evidence that the improvements transfer to real RGB-D scans.

## Weaknesses

### Fatal
None.

### Major

- **The PG-Layer derivation that claims to "retain the original SG form" (Section 3.3) is not mathematically sound as presented.** The transition from Eq. (13) to Eq. (14) requires the exponent to change from a sum \( \lambda_G(\nu^T p_G - 1) + \lambda_H(\nu^T p_H - 1) \) to \( \lambda_G(\nu^T(p_G p_H) - 1) \), with the assumption \( \lambda_G \approx \lambda_H \approx 2\lambda_R \). Even under this assumption, the algebra does not close: \( 2\lambda_R(\nu^T p_G - 1) + 2\lambda_R(\nu^T p_H - 1) = 2\lambda_R(\nu^T(p_G + p_H) - 2) \), which is not equal to \( \lambda_G(\nu^T(p_G p_H) - 1) \) without additional steps that are never stated. The notation \( p_G p_H \) is also never defined (concatenation? elementwise product? learned composition?). Since the claim that PG-Layer preserves the SG form — and thereby enables deeper networks — is a central contribution, this gap is serious.

- **The rotation-equivariance proof (Section 3.2) rests on the unsubstantiated assumption \( R_\nu \approx R_p \).** The paper states this approximation without derivation, error bound, or empirical verification. The claim that "the mean is not affected by the rotation, for \( \mu(\nu) \approx \mu(p) \)" is also problematic: the mean of points on \( S^2 \) is not rotation-equivariant in general and is ill-defined for antipodal distributions. The paper provides no ablation or quantitative test (e.g., rotate input by known angles and measure equivariance error) to empirically verify equivariance. Without this, the foundational theoretical claim is unsubstantiated.

- **The mathematical formulation of SPF (Eq. 2) is underspecified to the point of irreproducibility.** The output is declared \( z \in \mathbb{R}^{|\nu| \times 3} \), but it is a product of: (i) \( E(\nu, p) \) — an edge function whose output dimension is never defined, with learnable parameters \( \theta, \phi \) whose functional forms (linear layer? MLP? scalar?) are never specified; (ii) \( V(r) = \frac{4}{3}\pi r^3 \) — a scalar; (iii) \( U(P(\nu,p)) \) — a fully connected layer mapping to \( \mathbb{R}^A \); and (iv) \( e^{\lambda(\nu^T p - 1)} \) — a scalar. How the product of these heterogeneous terms yields \( \mathbb{R}^{|\nu| \times 3} \) is never explained, making the core representation impossible to reconstruct from the paper alone.

### Minor

- **No variance estimates or statistical significance reported.** All tables (1–5) report single-point numbers without standard deviations, confidence intervals, or run counts. Given the modest absolute improvements (e.g., Top-1 from 0.162 to 0.151 in Table 4, RRMSE from 0.026 to 0.019 in Table 1), it is impossible to determine whether these gains are reproducible or within noise.

- **The ablation study is limited to one task (registration, Table 1) and one decoder (SGPCR).** The paper claims all three components (E, U, V) contribute, but does not ablate them for retrieval or completion. The claim that the model adds "no increase in the number of parameters" (Conclusion, line 251) is asserted without any parameter count table or comparison.

- **The value of \( m \) (number of PG-Layer modules per SA layer) is never specified.** This is a key architectural hyperparameter needed for reproduction.

- **The mean of points on \( S^2 \) used in Eq. (4) is not well-defined for antipodal or near-antipodal distributions** (the Fréchet mean on a sphere is non-unique in this case). The paper provides no discussion or justification for this design choice.

- **The claim in Related Work that "we show improvements over VN due to acquiring local and global information" is only supported for completion (Table 5)**, not for registration or retrieval where VN results are absent from the comparison.

### Trivial
- Figure 2 is referenced but the caption provides more detail than the body text.
- The volume term \( V(r) = \frac{4}{3}\pi r^3 \) is described as enabling "differentiable" adjustment of patch size, but it is a scalar multiplier with no spatial dependency — its role in the SPF computation is mathematically trivial and could be more clearly explained.

## Nice-to-Haves
- An empirical equivariance test (rotate input by known angles, measure feature stability) would substantiate the theoretical claim.
- A sensitivity analysis for the initial patch radii per SA layer would verify the method is not brittle to this hyperparameter.
- An experiment with 4–6 SA layers would demonstrate the claimed benefit of PG-Layer enabling deeper networks.

## Removed Points

**These points are flagged to be removed, treat them with caution:**

1. **"The paper does not quantitatively compare its patch-based method against the global method's performance on local tasks."** — Table 1 directly compares DeepSPF (with SGPCR decoder) against SGPCR (global method), showing improvements. The comparison exists.

2. **"Figure 2 is referenced but not described in text."** — Section 3.4 (line 152) explicitly says "In Figure 2, we show our presented architecture." The description is brief but present.

3. **"More recent completion methods (PointTr, SnowflakeNet) are not included."** — The paper explicitly scopes itself to encoder comparisons: "to provide a fair comparison between encoder structures, we restrict ourselves to PointNet-based networks" (line 37). This is a stated design choice, not an omission.

4. **"The improvement could be artifacts of a single train/test split."** — While the paper lacks error bars (kept as a Minor weakness), the claim of "artifact" is speculative without evidence of cherry-picking.

## Novel Insights

None beyond the paper's own contributions. The review process surfaces a significant gap between the paper's ambitious theoretical framing and the actual rigor of its derivations, but this is a critique rather than a novel insight about the field.

## Suggestions

1. **Fix the PG-Layer derivation.** Either provide a correct step-by-step proof that Eq. (13) reduces to the SPF form, or remove the claim that PG-Layer "retains the original SG form" and instead present it as an empirically-motivated architecture. Clarify the notation \( p_G p_H \).

2. **Replace the \( R_\nu \approx R_p \) assumption with an empirical equivariance test.** Measure \( \| \text{SPF}(R_p) - R(\text{SPF}(p)) \| \) for random rotations and report the error. This would either validate or bound the approximation.

3. **Clarify all dimensions and functional forms in Eq. (2–3).** Specify the output dimensions of \( \theta, \phi, E(\nu,p) \), and explain how the product of terms yields \( \mathbb{R}^{|\nu| \times 3} \).

4. **Add standard deviations** to all tables (at least 3–5 runs) and include a parameter count comparison to substantiate the "no increase in parameters" claim.

5. **Specify \( m \)** (number of PG-Layer modules per SA layer) in the implementation details.

## Score and Decision

**Overall assessment:** The paper addresses a well-motivated problem and shows consistent empirical improvements across three tasks. However, the core theoretical contributions (SPF equivariance proof, PG-Layer derivation preserving SG form) contain mathematical gaps that undermine the paper's foundational claims. The mathematical presentation of SPF is underspecified, and the evaluation lacks statistical rigor. The empirical results are promising but cannot be fully evaluated without variance estimates. The paper needs substantial revision to its theoretical framing and presentation before the contributions can be properly assessed.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>