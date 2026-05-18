Now I have a comprehensive picture. Let me produce the final consolidated review.

## Summary

This paper proposes a Riemannian framework for learning the spectral factorization S = B diag(d) Bᵀ of a curvature/preconditioning matrix on the fly, enabling cheap application of arbitrary fractional powers S^{-1/p} via elementwise operations on d rather than expensive matrix eigendecompositions. The method handles the orthogonal constraint on B and eigenvalue-sorting ambiguities through local coordinate transformations (Cayley and exponential maps) that diagonalize the Fisher-Rao metric. A Kronecker-structured extension (with a learnable scalar α and determinant constraints to resolve factorization redundancy) scales the approach to neural network training. Experiments include synthetic curvature-matching tasks, a positive-definite matrix optimization problem, and low-precision (FP16) training of three vision transformers on ImageWoof.

## Strengths

1. **Novel algorithmic approach for cheap fractional powers.** The paper correctly identifies that computing matrix fractional powers is the bottleneck for non-diagonal second-order methods and proposes a principled solution: learn the spectral factors directly, so that any root reduces to elementwise exponentiation on d (Section 2, Figure 1). This is a genuine and non-trivial advance over prior work that relies on explicit decompositions.

2. **Riemannian machinery to handle spectral constraints.** The paper constructs local coordinate transformations (exponential map for d, Cayley map for B) that diagonalize the Fisher-Rao metric at evaluation points (Claim 4, Section 3.1). This is a technically solid extension of prior work on Riemannian adaptive methods (Glasmachers et al., 2010; Lin et al., 2021, 2023) to the spectral parametrization, which introduces new constraints and ambiguities not present in Cholesky or dense parametrizations.

3. **Resolution of Kronecker-factorization redundancy.** The paper correctly identifies that Kronecker factorization is non-unique and addresses this by imposing determinant constraints on each factor while introducing a learnable scalar α (Section 3.2). This is a clean resolution of a known practical issue that prior Kronecker-based methods (including Shampoo, K-FAC) often ignore.

4. **Connections to existing methods are explicitly shown.** Section 2.3 demonstrates that the framework recovers RMSprop, fractional diagonal methods (Chen et al., 2021), and root-free RMSprop as special cases when B is constrained to be diagonal. This unification is a nice property.

5. **Synthetic curvature-matching experiments are well-designed.** Figures 2 and 3 provide a clean sanity check that the spectral update scheme tracks the default full-matrix update and existing Kronecker-structured baselines (including the projection-based oracle) in both fixed-point and iterate-matching settings.

## Weaknesses

### Fatal
None.

### Major

1. **NN experiments on a single dataset with no error bars and no multiple seeds.** All neural network results come from ImageWoof only. The paper states that "random search... using 200 runs" was used for hyperparameter tuning, but the plotted curves (Figure 4) appear to be single trajectories — there is no mention of running multiple seeds with the chosen hyperparameters, no error bars or confidence intervals, and no indication of whether the curves are best/median/mean runs. Without this basic statistical rigor, the reader cannot assess whether observed improvements over baselines are reliable or are artifacts of hyperparameter search or random variation.

2. **Asymmetric comparison with Shampoo conflates multiple variables.** The paper compares its method (preconditioner updated every 10 iterations) against Shampoo (updated every 100 iterations) under a fixed time budget matched to AdamW. This comparison is framed as a practical advantage, but several asymmetries are not controlled:
   - **Grafting is used for Shampoo but not for the proposed method.** The paper explicitly states "We use grafting to improve Shampoo's performance" (Figure 4 caption). This means the comparison is not method-vs-method but method-vs-(method+heuristic grafting). Without ablating grafting, the reader cannot tell whether the proposed method's advantage is intrinsic or simply reflects that grafting helps Shampoo.
   - **No wall-clock timings are reported.** The claim that both methods "match AdamW's runtime" is stated as a fact (10 vs 100 steps), but no actual runtime measurements, hardware details, or FLOPs counts are provided to verify this.
   - **What Shampoo could achieve with 10-step updates under a longer wall-clock budget is not explored.** The paper's framing suggests that frequent updates are better, but this is asserted rather than demonstrated for Shampoo itself.

3. **No controlled low-precision stability study.** The paper claims the method "is stable in half precision" in the abstract and introduction, but the only evidence is that training succeeds in FP16. There is no controlled comparison (e.g., running the same spectral algorithm in FP32 vs FP16 on a simple test problem and measuring the eigenvalue trajectory divergence or the Frobenius norm of the difference). Without this, the claim of "stability" is not empirically distinguished from the basic observation that training converges.

4. **The fractional-power advantage is barely demonstrated.** One of the paper's central selling points is enabling "arbitrary fractional powers," yet the NN experiments show only one comparison (p=1 vs p=2) on one ViT architecture, with no error bars. A systematic sweep over p (e.g., p ∈ {1, 2, 4, 8}) across all three architectures under controlled conditions is needed to support the claim that non-standard p values consistently improve optimization.

### Minor

1. **Claim 1 is invoked but its content is never stated in the main text.** Line 77 reads "Claim 1." with no accompanying statement. While the context suggests it asserts equivalence between the spectral update and the default scheme, the claim itself is absent. This is confusing for a reader trying to follow the theoretical development.

2. **Truncation order for the Cayley/exponential maps is not specified.** Section 2.4 describes a Neumann-series approximation and shows the expansion up to (βN)⁸, but the paper never states what truncation order is actually used in the NN experiments. Similarly, the exponential map truncation for d is mentioned but the number of terms is not given. This makes the concrete algorithm difficult to reproduce.

3. **The repeated-eigenvalue update rule is not fully specified.** The paper mentions using the Moore–Penrose inverse when d has repeated or near-repeated entries (Section 3.1, line 240), but does not provide an explicit update rule for B in that regime. The rule in Figure 1 sets [U]_{ij} = 0 when d_i = d_j, but it is not explained whether this is the consequence of the Moore–Penrose treatment or an approximation.

4. **No wall-clock timing or memory cost comparison.** The paper asserts that the method matches AdamW's runtime with 10-step updates while Shampoo needs 100-step updates, but no actual timing data, hardware specifications, or memory usage numbers are provided. This weakens the practical-efficiency claim.

5. **Limited NN baseline coverage.** The Lin et al. (2024) Cholesky-based Kronecker method — which is directly related and also provides root-free updates — is compared only in synthetic experiments, not on the NN tasks. K-FAC, a well-known structured second-order method, is mentioned in the introduction but not included as a baseline. While the comparison with Shampoo is the most directly relevant, adding these would strengthen the positioning.

### Trivial
- The Kronecker update formula in the right box of Figure 1 shows a duplicated term "(S^{(K)})^{-1/p}" at the end of the parameter update, which appears to be a copy-paste error.

## Nice-to-Haves
- A sweep over truncation orders for the Cayley map on the synthetic full-matrix task, showing the trade-off between approximation quality, stability, and cost.
- A direct FP16-vs-FP32 comparison of the spectral algorithm on the fixed-point matching task (Section 2.1) to validate the half-precision stability claim in isolation.
- Reporting actual wall-clock time per iteration for each method on the hardware used.

## Removed Points

The following criticisms from the reviews are removed (with justification):

- **"Derivations are relegated to a missing appendix" / "main text is not self-contained"**: The hard rules require removing criticisms about missing appendix content, as the parser strips these sections from all papers. The paper explicitly states "See Appx. H for a complete derivation" — this content exists in the original submission.
- **"Claim 4's statement is incomplete"**: Claim 4 (lines 292–298) *does* give the full diagonal metric expression in the main text, including explicit forms for F_{δδ}, F_{mm}, and F_{MM}. The reviewer's characterization is factually inaccurate.
- **"The paper should also cover K-FAC as a baseline"**: K-FAC uses different Kronecker factors (from the Fisher matrix) than the gradient-outer-product setup used here and in Shampoo. The paper's choice of Shampoo as the primary Kronecker baseline is defensible. Included as a minor point above only because the reviewer's concern about limited NN baselines has a kernel of validity regarding the Cholesky method of Lin et al. (2024).
- **Generic strength from Strength Finder**: "This paper addressed an important problem" — removed as generic.

## Novel Insights

The key insight that emerges from looking across the reviews is that this paper has a genuine methodological contribution — the spectral parametrization with local coordinate transformations that diagonalize the metric is a non-trivial piece of Riemannian machinery — but its empirical evaluation is operating at a lower standard than what would be needed to support the practical claims the paper makes (half-precision stability, efficient NN training, advantage of non-standard fractional powers). The paper would be significantly stronger if it narrowed its empirical focus: drop the broad claims about "effectiveness for NN training" and instead position itself more honestly as a methods paper with preliminary validation, or substantially expand the experiments to meet the rigor expected for practical claims.

## Suggestions

1. **Run all NN experiments with at least 3–5 seeds** and report mean ± std. Alternatively, clearly state if the plotted curves are from a single best run and qualify the strength of the conclusions accordingly.
2. **Add a controlled low-precision stability experiment**: run the spectral algorithm in FP32 and FP16 on the fixed-point matching task and report the Frobenius norm difference between the eigenvalue trajectories.
3. **Equalize the comparison with Shampoo**: either (a) run both methods with the same update frequency (e.g., every 10 iterations) and compare wall-clock time, or (b) run Shampoo with grafting removed as an additional ablation, or (c) at minimum report actual runtimes.
4. **Systematically vary the fractional power p** (e.g., p ∈ {1, 2, 4, 8}) across all three ViT architectures with error bars to substantiate the claim that non-standard p values are beneficial.
5. **Specify the truncation order** used for the Cayley and exponential map approximations in the NN experiments, and justify the choice.
6. **Complete the statement of Claim 1** in the main text so readers can follow the theoretical claim without inferring it from context.

## Score and Decision

The paper presents a novel and technically interesting Riemannian framework for spectral preconditioning that genuinely addresses an important bottleneck (cheap arbitrary fractional powers). The theoretical development and synthetic validation are solid. However, the NN experiments — which are needed to support the paper's practical claims — suffer from fundamental rigor issues: a single dataset, no error bars, asymmetric baselines (grafting for Shampoo only, unequal update frequencies), no controlled low-precision validation, and minimal demonstration of the fractional-power advantage. These weaknesses collectively prevent the paper from convincingly establishing its claimed practical benefits. Major revisions to the experimental section would be required. I recommend rejection in the current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>