Now I have sufficient evidence from the paper. Let me construct the final consolidated review.

---

## Summary

This paper introduces DeepSPF, a learnable backbone for point cloud processing that combines Spherical Patch Fields (SPF) — a patch-wise SO(3)-equivariant representation based on Spherical Gaussians — with a Patch Gaussian Layer (PG-Layer) that adaptively adjusts patch sizes and incorporates low-frequency information via Legendre polynomials. The authors demonstrate improvements across three Scan-to-CAD tasks (registration, retrieval, and completion) by integrating DeepSPF into existing pipelines such as DeepGMR and PCN, showing notable reductions in rotation error and Chamfer Distance.

## Strengths

- **Substantial empirical improvements across three tasks.** On registration (ModelNet40 zero-intersection noise), replacing PointNet with DeepSPF in DeepGMR reduces rotation error (RRMSE) from 17.5° to 5.3°. On retrieval (ShapeNet), Top-1 Chamfer Distance drops from 0.158 (SGConv) to 0.131 (~17% improvement). On completion (ShapeNet), seen-category Chamfer Distance decreases from 0.0037 (PCN) to 0.0025 (~32% reduction). These gains are consistently positive and the pattern of improvement across tasks is the paper's strongest evidence.

- **Ablation study decomposes the contribution of each component.** Table 1 evaluates three conditions (E: patch-wise graph only, U: adding Legendre polynomials for low-frequency information, V: adding adaptive radial patches), showing monotonic improvement. This gives readers a clear picture of what each design choice contributes.

- **Integration into multiple existing pipelines is demonstrated.** DeepSPF is shown to replace encoders in at least two distinct frameworks: DeepGMR (registration, Tables 1–2) and PCN (completion, Table 5). The ablation conditions (E, U, V) also use the SGPCR decoder, demonstrating compatibility with at least three decoder architectures. This supports the claimed integrability.

- **Evaluation on real-world Scan2CAD data confirms practical relevance.** Table 3 shows that DeepSPF improves the Scan2CAD benchmark metric (from 26.1% for SGConv to 27.8%) when used with VoteNet detections, demonstrating effectiveness beyond synthetic data.

## Weaknesses

### Fatal
None.

### Major

1. **Equivariance claim relies on an unquantified approximation with no error analysis.** The derivation in Section 3.2 invokes \(R_\nu \approx R_p\) — that the rotation applied to the spherical sampling approximately equals the rotation applied to the point cloud — in both Eq. (9) and Eq. (11). The paper explicitly writes "\(R_\nu \approx R_p\)" and "under the introduced assumptions," so it is transparent about the approximation. However, **no justification is given for why this approximation holds**, nor is there any discussion of when it might break down or what the equivariance error is. Since the spherical sampling \(\nu\) is fixed *a priori* and is not dynamically rotated with the input, the approximation \(R_\nu \approx R_p\) is not guaranteed to hold in general. The paper compares itself to exact SO(3)-equivariant methods (e.g., Vector Neurons) without characterizing the degree of equivariance violation. This is a structural gap: a central theoretical property of the representation is asserted on the basis of an unexamined approximation. At minimum, an empirical measure of equivariance error (e.g., rotation consistency of latent vectors under random rotations) is needed.

2. **The PG-Layer "convolution" is not rigorously derived, and the claim about enabling deeper networks is untested.** Equation (12) correctly observes that a true convolution of two SGs does not yield an SG. Equation (13) then defines an operation composed of pointwise multiplications of the SPF representation combined with edge functions (E), radial volume (V), and upscaling (U). This is **not a convolution in any standard sense** — it is a custom fusion of pointwise and graph operations. The derivation in Eqs. (13)–(14) then assumes \(\lambda_G \approx \lambda_H \approx 2\lambda_R\) without any justification, and concludes that the output matches the original SPF form. These are strong assumptions that are asserted rather than established. Furthermore, the paper claims this enables "deeper networks" without ever testing deeper architectures — the experiments use at most three Set Abstraction layers, each with a single PG-Layer. The practical benefit of the form-preserving property is therefore unsubstantiated.

### Minor

3. **Baseline comparisons are partially uncontrolled.** The paper compares DeepSPF+DeepGMR against standalone DeepUME and SGPCR in Table 1, but DeepUME and SGPCR do not use DeepSPF encoding — these are system-level comparisons, not controlled encoder swaps. The controlled comparison (same decoder, different encoder) is properly done for DeepGMR (DeepGMR+PointNet vs. DeepGMR+DeepSPF) and for PCN (PCN vs. PCN+DeepSPF vs. PCN+VN), and the ablation uses the SGPCR decoder, so integration is shown across multiple decoders. Nonetheless, the framing "a significant reduction in the rotation error of existing registration methods" overclaims by implying parity of comparison, as the DeepUME and SGPCR rows are not apples-to-apples encoder comparisons.

4. **Ablation results lack variance estimates.** The improvements in Table 1 appear monotonic across conditions E→U→V, but no error bars, confidence intervals, or multi-run statistics are reported. Without variance information, it is difficult to assess whether the differences between conditions are statistically robust or within the noise of a single run.

5. **Parameter count and runtime claims are not explicitly verified in the text.** The conclusion states DeepSPF does this "without increasing the number of parameters compared to similar state-of-the-art methods," but no parameter counts are given in the prose. Inference time \(R\) is listed as an evaluated metric in Section 4.3, which suggests it appears in the tables, but the parameter claim specifically is unsubstantiated in the text body. The reviewer-imputed baseline retuning procedure ("re-trained with the preferred configurations") is standard practice and not a serious weakness; however, an explicit statement of how baseline hyperparameters were chosen would improve trust.

6. **Limited discussion of the method's limitations.** The only limitation acknowledged is FPS complexity for large point clouds. Missing are: (a) the approximate nature of the equivariance and the \(R_\nu \approx R_p\) assumption, (b) reliance on the assumption \(\lambda_G \approx \lambda_H \approx 2\lambda_R\) in PG-Layer, and (c) the scope of evaluation (synthetic data with limited real-world validation beyond Scan2CAD). Self-critique of these points would strengthen the paper.

### Trivial

7. None.

## Nice-to-Haves

- An empirical equivariance consistency test (e.g., \(\| \mathrm{DeepSPF}(R p) - R(\mathrm{DeepSPF}(p)) \|\) across random rotations) would directly address the main theoretical concern and could be a simple addition.
- Reporting parameter counts and FLOPs for all compared methods would substantiate the parameter-efficiency claim.
- A small experiment with 5–10 stacked PG-Layers (comparing against SGConv) would empirically test whether the form-preserving design actually enables deeper networks as claimed.

## Removed Points

The following criticisms from the reviewer input were removed or downgraded based on verification against the actual paper:

- *"The paper uses images for all tables, making numerical values unavailable"* — Removed. This is a PDF-extraction artifact; the original submission has proper LaTeX tables.
- *"Does not show that DeepSPF improves over stronger equivariant baselines (e.g., VN)"* — Removed. The paper does compare against VN-PointNet+PCN in Table 5 (completion) and explicitly states the comparison.
- *"Integration is only shown for one specific decoder"* — Removed. DeepSPF is integrated with DeepGMR's decoder, SGPCR's decoder (ablation conditions), and PCN's decoder for completion.
- *"No justification for approximation" / "approximate equivariance is treated as exact" (unqualified form)* — The paper does not treat it as exact; it uses \(\approx\) notation consistently and states "under the introduced assumptions." However, the lack of justification and error analysis remains a real weakness (kept in Major #1 with corrected framing).
- From Strength Finder: *"SPF enables patch-wise SO(3)-equivariant representation with proven equivariance"* — Removed (moved here). Conflicts with verified weakness about the unquantified approximation; the weakness wins.
- From Strength Finder: *"PG-Layer retains the original Spherical Gaussian form, allowing deeper networks"* — Removed (moved here). Conflicts with verified weakness about the unsupported derivation and lack of empirical testing.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the theoretical equivariance framing and the empirical results, but this is a critique of the paper's argumentation, not a novel insight.

## Suggestions

1. **Quantify the equivariance error.** Add an empirical measure: apply random rotations to input point clouds and measure the rotation consistency of the latent vectors produced by DeepSPF. Report the distribution of equivariance errors and discuss regimes (e.g., sparse vs. dense point clouds) where the approximation \(R_\nu \approx R_p\) may break down.
2. **Reformulate the PG-Layer derivation.** Drop the label "convolution" for the operation in Eq. (13) and describe it honestly as a pointwise fusion of SPF representations with learned graph and radial components. Either justify the \(\lambda_G \approx \lambda_H \approx 2\lambda_R\) assumption or remove it.
3. **Empirically test the "deeper networks" claim.** Compare a DeepSPF variant with 5–10 stacked PG-Layers against a baseline where SGConv collapses, to show that the form-preserving design provides a concrete benefit.
4. **Report parameter counts** for all compared methods in the main text and add error bars or multi-run statistics to the key ablation table.
5. **Acknowledge limitations upfront** in a dedicated Limitations section, covering the approximate equivariance, the PG-Layer derivation assumptions, and evaluation scope.

## Score and Decision

The paper presents a novel and practically effective approach — adaptive patch-wise spherical representations integrated into existing pipelines yield clear improvements on three tasks. The empirical evidence is the paper's strongest asset. However, the theoretical framing is materially weaker than claimed: the equivariance property is approximate and unquantified, the PG-Layer derivation rests on unjustified assumptions, and the "deeper networks" benefit is asserted without evidence. These issues do not invalidate the empirical results — the method clearly works — but they mean the paper overstates its theoretical contributions relative to what is actually demonstrated. The paper would benefit from major revision to align claims with evidence.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>