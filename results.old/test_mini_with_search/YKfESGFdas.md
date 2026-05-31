## Summary

GeONet proposes a neural operator (based on a DeepONet-style architecture) that learns the Wasserstein-2 geodesic between pairs of probability measures. The key idea is to avoid requiring ground-truth geodesic data for training: instead, the network enforces the KKT optimality conditions of the Benamou-Brenier dynamic OT formulation — a coupled PDE system consisting of the continuity equation and the Hamilton-Jacobi equation — through a physics-informed loss. After offline training, inference is a single forward pass, yielding orders-of-magnitude speedup over traditional per-pair OT solvers. The method also supports mesh-invariant prediction and zero-shot super-resolution.

## Strengths

- **Training does not require ground-truth geodesic data.** The physics-informed loss (Eqs. 5–8) enforces the continuity equation, Hamilton-Jacobi equation, and boundary conditions via automatic differentiation. Only boundary distribution pairs are needed. This is a genuine advantage over supervised approaches that depend on expensive solver-generated labels (Section 1, lines 28–31).

- **Mesh-invariant output enables zero-shot super-resolution.** GeONet can be trained on low-resolution grids and evaluated on high-resolution grids without retraining. The high-resolution experiments in Table 1 (1D and 2D) show errors comparable to the in-distribution case, confirming that the operator learned is not tied to a particular discretization.

- **Inference is orders of magnitude faster than traditional OT solvers.** Section 4.4 and Figure 4 (runtime comparison) demonstrate that after offline training, GeONet's forward pass is near-instantaneous and substantially outperforms POT, especially on fine meshes, with the advantage growing with resolution. This is the paper's strongest empirical contribution and directly addresses a real computational bottleneck.

- **Outperforms flow-matching baselines on point-cloud geodesic estimation.** Table 2 shows that on 2D Gaussian mixture point clouds, GeONet achieves L¹ errors of ~28–30 at intermediate times, while CFM and RF yield errors of ~92–112. Although CFM/RF are not designed as geodesic solvers, the comparison usefully demonstrates that standard generative flow methods do not capture the geodesic property.

- **Method is the first to combine operator learning with physics-informed constraints for the Wasserstein geodesic problem.** Table 1 systematically positions GeONet against four method categories; it is the only approach that simultaneously provides operator learning, PDE satisfaction, no need for geodesic training data, and output mesh independence.

## Weaknesses

### Fatal

None.

### Major

- **Reference geodesic validation is insufficient.** The paper computes L¹ errors against a reference obtained via the Convolutional Wasserstein Barycenter (CWB) framework in POT. While the conceptual claim that "barycenter ≠ displacement interpolation" is incorrect — for the Wasserstein-2 metric, the barycenter of two measures *is* their geodesic interpolation — the CWB algorithm introduces *entropic regularization* and convolutional approximations that bias the reference. The paper does not quantify this bias (e.g., by comparing against an exact solver for Gaussian distributions where the geodesic is known analytically, or by studying sensitivity to the regularization parameter). Because all quantitative accuracy claims in Tables 1 and 2 rely on this reference, the reader cannot assess how much of the reported error is method error vs. reference bias. This is fixable (e.g., validate on Gaussians, test multiple regularization levels, or use a direct Benamou-Brenier discretization), but as presented the central accuracy numbers are not properly grounded.

- **No ablation of the physics-informed losses.** The paper uses three loss components: CE residual (ℒ_cty), HJ residual (ℒ_HJ), and boundary conditions (ℒ_BC). There is no experiment that removes or varies these components (e.g., training with only boundary conditions, or omitting the HJ equation). Since the claim that "the PDE constraints drive learning" is central to the method, an ablation study is standard practice and its absence is a meaningful gap. The ablation also makes it difficult to diagnose whether the 2–3× error increase on OOD data stems from PDE violation or from the architecture.

### Minor

- **The CFM/RF baseline comparison is informative but incomplete.** CFM and Rectified Flow are generative (sampling-based) methods, not geodesic solvers. Table 2 shows they do not produce the W₂ geodesic, which is expected. The comparison would be much stronger if it included at least one amortized OT method (e.g., Lacombe et al. or Amos et al., cited in the paper) or a PINN-based single-pair geodesic solver. Without such a baseline, the reader cannot tell whether GeONet's advantage comes from the physics-informed operator approach or simply from being an amortized method.

- **OOD generalization test is limited.** The out-of-distribution experiment (Section 4.5) only varies the variance of Gaussian mixture components. More challenging shifts — different numbers of modes, different spatial domains, or entirely different distribution families — are not tested. The paper acknowledges this implicitly but does not discuss how GeONet would fare under more severe distribution shift.

- **MNIST experiment does not validate geodesic correctness in pixel space.** The paper encodes MNIST digits to a 32-d latent space, learns the geodesic there, and decodes back. As the paper honestly states, "the ambient-space error is much larger than the encoded-space error, meaning that the geodesics in the encoded space and ambient image space do not coincide." This limits the experiment to a feasibility demonstration; it does not provide evidence that GeONet computes the true Wasserstein-2 geodesic between MNIST distributions. The paper would benefit from either applying GeONet to data where geodesics are meaningful in the original space (e.g., rotating shapes, translations) or repositioning the experiment more modestly.

- **Training cost not reported.** The paper emphasizes inference-stage speedup but never reports training time, number of epochs, or GPU hours. For a method that requires offline training, a practitioner needs to know whether the training cost is prohibitive. A single line summarizing training resources would suffice.

### Trivial

- **Section 3 mentions a "Fourier feature architecture" (line 195) and references a label `\ref{Fourier_feature}` that does not exist in the paper.** This appears to be a vestigial paragraph; the Fourier feature approach is neither implemented nor evaluated. The authors should either remove the paragraph or implement the variant.

- **"where" after Eq. (10) is grammatically detached** (line 163: "cf. Here" starts a new sentence mid-description). Minor editing would improve readability.

## Nice-to-Haves

- Comparing against an amortized static-OT method (e.g., Lacombe et al. or Amos et al.) would strengthen the positioning. Even training a standard DeepONet with supervised MSE against POT geodesics as a sanity check would help isolate the benefit of the physics-informed loss.

- Reporting PDE residual values (ℒ_cty, ℒ_HJ) on test data would help readers assess how well the trained network satisfies the optimality conditions, which is more direct than L¹ error against a biased reference.

- A brief discussion of how entropic regularization in the CWB reference interacts with the physics-informed training (which targets the unregularized Benamou-Brenier problem) would clarify the evaluation.

## Removed Points

- **Criticism that the CWB reference is conceptually wrong ("barycenter ≠ displacement interpolation").** This criticism is factually incorrect. In the Wasserstein-2 space, the barycenter of two measures μ₀ and μ₁ with weights (1−t, t) *is* the geodesic point at time t (this is a standard result: the McCann displacement interpolation solves the barycenter problem). The real concern is about entropic regularization bias in the CWB *algorithm*, not a conceptual mismatch. This has been downgraded to a Major weakness above about insufficient validation.

- **Criticism that the runtime figure is missing or a placeholder.** The paper contains `\includegraphics{GeONet_runtime_comparison.pdf}` (line 488) with a caption; the PDF extraction produces a placeholder, but the original submission has the figure.

- **Criticism about missing appendix content, proofs, or references.** These are parser artifacts; the original submission includes appendices as per the statement "Due to the space limit, we defer simulation setups, model training details and error metrics to Appendices" (line 219).

- **Claim that CFM/RF comparison is "staged to make GeONet look superior."** The comparison is asymmetric but informative — it demonstrates that generative flow methods optimized for sampling do not produce geodesic flows. The paper explicitly notes that CFM/RF achieve zero error at t=0 because they are conditioned on the initial sample, confirming the difference in objectives.

- **Generic formatting/style nitpicks** (typos, line breaks, missing parentheses in equations due to extraction).

- **Generic strengths from the Strength Finder** that are superficial (e.g., "the problem is important") or duplicate the core strengths already listed.

## Novel Insights

None beyond the paper's own contributions. (The reviews did not surface any observation about the method or results that the authors themselves had not already made.)

## Suggestions

1. **Validate the reference solver.** Show that the CWB-based reference converges to the exact geodesic as entropic regularization → 0, ideally on Gaussian distributions where the analytic geodesic is known. Report sensitivity to the regularization parameter.

2. **Add an ablation study.** Train GeONet with: (a) only boundary losses, (b) BC + CE but no HJ, (c) all three. Report L¹ errors and PDE residuals for each configuration.

3. **Add at least one amortized OT baseline** (Lacombe et al., Amos et al.) or a supervised DeepONet trained on POT geodesics, to disentangle the benefit of the physics-informed loss from the benefit of amortization.

4. **Report training cost** (GPU hours, number of epochs, convergence behavior) alongside the inference speedup.

5. **Reconsider the MNIST experiment** either by choosing a dataset where geodesics are meaningful in the original space (e.g., image rotations/translations) or by explicitly stating that the experiment only tests feasibility in a latent space and does not validate geodesic correctness.

## Score and Decision

### Calibration

**Round 1 (bracketing):**
- Low band (score ≤3): Queries on neural operator + OT geodesic returned avg scores of 4.0–5.6 for topical papers.
- Middle band (4–7): Most topically similar papers (NCF for OT: 4.0; HOTA: 5.6; Statistical Learning OT: 5.0) sit in 4.0–5.6.
- High band (8+): All returned papers are from unrelated domains (protein generation, rotation estimation) — not informative for this paper.

→ Initial bracket: 4–6.

**Round 2 (narrowing):**
- Anchors inside the bracket: NCF for OT (4.0, avg 4.0) — a closely related paper (HJ-based OT solver) that had experimental errors and synthetic-only evaluation. GeONet is slightly stronger because its central methodological claim is sounder and the evaluation, while gappy, is not demonstrably wrong.
- HOTA (5.6, avg 5.6) — a stronger paper with more polished experiments and a clearer theoretical contribution. GeONet is weaker than HOTA.
- Contact Wasserstein Geodesics (6.0, avg 6.0) — wider experimental validation and a more grounded theoretical contribution. GeONet is weaker.
- Statistical Learning Perspective on OT (5.0, avg 5.0) — well-structured theory and limited experiments. GeONet is comparable, with the edge on empirical breadth.

→ Final score: 4.5. The paper proposes a well-motivated and principled method, but the evaluation has unresolved gaps (reference validation, missing ablation, incomplete baselines) that prevent it from reaching the 5+ tier occupied by HOTA or the CWG paper. It is a clear accept as a poster but not yet at the level of a stronger venue or oral.

**Anchors consulted across all rounds:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews_2026/YbQxus1KEa.md | 4.00 | R1,R2 | NCF for OT — very similar topic; GeONet is slightly stronger |
| /home/wg25r/review_agent/human_reviews_2026/Og1klGbvlM.md | 5.60 | R1,R2 | HOTA — stronger experimental validation; GeONet is weaker |
| /home/wg25r/review_agent/human_reviews_2026/OJupg4mDjS.md | 7.00 | R1,R2 | Wasserstein Geodesic PCA (Oral) — much stronger; GeONet is substantially weaker |
| /home/wg25r/review_agent/human_reviews_2026/FJTdyG8jeJ.md | 5.00 | R1 | Statistical Learning OT — comparable quality |
| /home/wg25r/review_agent/human_reviews_2026/mJiPqOzc3O.md | 4.67 | R1 | Physics-informed neural operator — related but different domain |
| /home/wg25r/review_agent/human_reviews_2026/CsCL9T2PDk.md | 4.50 | R1 | Newton-PINet — similar tier but different problem |
| /home/wg25r/review_agent/human_reviews_2026/sKUUqrezRT.md | 4.50 | R1 | Neural operator PDE work — similar tier |
| /home/wg25r/review_agent/human_reviews_2026/CC2vIx3GZM.md | 4.00 | R1 | PDE learning — weaker scope |
| /home/wg25r/review_agent/human_reviews_2026/VaS6xcDrTb.md | 8.50 | R1 | Unrelated domain (rotation estimation) |
| /home/wg25r/review_agent/human_reviews_2026/DTQIjngDta.md | 8.00 | R1 | Unrelated domain (visual geometry) |
| /home/wg25r/review_agent/human_reviews_2026/248ysaRatx.md | 8.00 | R1 | Unrelated domain (quantum ML) |
| /home/wg25r/review_agent/human_reviews_2026/RDerF20JYT.md | 8.00 | R1 | Unrelated domain (protein generation) |
| /home/wg25r/review_agent/human_reviews_2026/B02EqvyiF3.md | 5.50 | R2 | Spectral-Grassmann OT metric — comparable tier |
| /home/wg25r/review_agent/human_reviews_2026/P5B97gZwRb.md | 4.00 | R2 | Lagrangian OT — synthetic-only experiments; comparable |
| /home/wg25r/review_agent/human_reviews_2026/KWWfLgkySm.md | 6.00 | R2 | PINN convergence theory — not directly comparable |
| /home/wg25r/review_agent/human_reviews_2026/IaEohEBUgi.md | 6.00 | R2 | Contact Wasserstein Geodesics — stronger experimental breadth; GeONet is weaker |

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Accept</decision>