Now I have a good calibration picture. Let me write the consolidated review.

**My round-1 bracket:** I placed this paper in the 4–6 range based on the calibration anchors. Papers in the 4-5 range (Rejected or borderline Accept) have similar issues of missing baselines and narrow scope. The paper is stronger than the 4.0 paper (Reject) but weaker than the 5.0+ papers with broader validation.

**Round-2 narrowing:** The round-2 anchors at 4.5-5.0 show papers with similar strengths/weaknesses patterns. The paper under review is comparable to these but with fewer baselines, landing it at 4.5.

Now let me write the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None

### Major
1. Missing baseline comparisons against the most relevant prior work
2. Limited evaluation scope

### Minor
1. VI metric limited to separable problems
2. Weak vanilla PINN baseline for 10D comparison

## Score: 4.5

Let me draft this carefully.## Summary

This paper proposes Dimension Domain Co-Decomposition (3D), a PINNs framework that combines dimension decomposition (via a shared MLP processing coordinate-index pairs) with MoE-driven automatic domain decomposition. It also introduces Variable Interpretability (VI), a metric that quantifies how well learned per-dimension latent subspaces align with ground-truth solution factors. Experiments on Poisson, Wave, Burgers, and Transport equations show parameter reductions of up to 10× and accuracy improvements over vanilla PINNs, with the MoE router automatically partitioning domains at shock locations without predefined regions or interface conditions.

## Strengths

- **Parameter efficiency via shared-MLP dimension decomposition is convincingly demonstrated.** Table 1 shows the shared MLP uses 5,392 parameters across all problems versus 26,640–53,280 for independent per-dimension MLPs (5–10× reduction). The parameter count is independent of input dimension, a concrete and well-supported architectural advantage over prior dimension-decomposition approaches that assign separate networks to each coordinate.

- **The MoE router automatically identifies salient subdomain boundaries without manual partition design or interface losses.** Figure 4 shows that for Burgers' equation (ν=0.01/π), two experts consistently partition at x=0—the shock location—and error drops from 0.2108 (K=1) to 0.0011 (K=2). The router's behavior is consistent across five random seeds, demonstrating that the decomposition is driven by problem geometry, not initialization artifacts. This is a clear qualitative advance over XPINNs/APINNs, which require predefined partitions.

- **The VI metric provides the first quantitative notion of interpretability for dimension decomposition in PINNs.** Table 2 shows VI reaching 99.99–100% for separable problems (5d/10d Poisson, 1d/2d Wave) with modest rank (r=4–5), confirming that the learned per-dimension subspaces fully contain the ground-truth factors. While the metric has scope limitations (discussed below), it is technically sound (subspace alignment via QR + SVD) and fills a genuine gap in the literature.

## Weaknesses

### Major

1. **No experimental comparison against the most relevant prior work (SPINNs, XPINNs, APINNs).** The paper frames 3D as a unified framework that improves upon both dimension decomposition and domain decomposition approaches. For dimension decomposition, SPINNs (Cho et al., 2023) is the most directly comparable method—the paper discusses differences (shared vs. per-dimension MLPs, AD compatibility with MoE) but never evaluates against it. For domain decomposition, XPINNs (Jagtap et al., 2020c) and APINNs (Hu et al., 2023) are the relevant baselines, yet none appear in any experiment. The improvement over vanilla PINNs is well-documented but expected: any decomposition strategy that encodes problem structure will beat a flat MLP on separable or shock-containing PDEs. Without comparisons against the methods this framework claims to improve upon, the central claim that 3D advances the state of the art is not supported.

2. **Evaluation scope is narrower than the paper's framing suggests.** (a) MoE-driven domain decomposition is tested only on two (1+1)-D problems (Burgers, Transport). This does not demonstrate that automatic expert partitioning scales to higher dimensions or geometrically irregular domains. (b) High-dimensional experiments (5d/10d Poisson) use only separable solutions where the product ansatz (Eq. 2) exactly matches the solution structure—a best-case scenario, not a stress test. Performance on high-dimensional PDEs with cross-term interactions remains unexamined. (c) The 2D Poisson L-shaped domain test, cited as evidence of irregular-domain capability, is deferred to the appendix without results in the main text.

### Minor

3. **VI metric is restricted to separable solutions.** The paper acknowledges this limitation and proposes a Fourier-series workaround in the conclusion, but this workaround is not implemented or evaluated. As a result, the metric's practical value outside the narrow class of separable problems is unsubstantiated. The claim of providing "quantitative interpretability" is therefore limited to problems where the solution already factorizes.

4. **The vanilla PINN baseline for the 10D Poisson experiment uses a small (4-layer, width-64) network.** While the parameter count is comparable to the shared MLP (4,929 vs. 5,392), using only 4 hidden layers is a weak configuration for a 10D problem; deeper networks are standard in the PINN literature. The large error gap (1.29×10⁻¹ vs. 1.25×10⁻³) may partly reflect under-parameterization of the baseline, making the comparison less informative.

5. **No ablation on router architecture or principled selection of the number of experts K.** The paper reports that K=2 works for Burgers and K=3 for Transport, but provides no guidance on how to choose K a priori—beyond the post-hoc observation that "additional experts yield similar errors." The router is fixed as a 5-layer MLP without ablation of simpler alternatives.

### Trivial

None.

## Nice-to-Haves

- Testing MoE domain decomposition on a higher-dimensional or irregular-domain problem (e.g., 2D elliptic PDE with discontinuous coefficient, 2D+time convection-diffusion) would substantially strengthen the generality claim.
- An ablation study on the router architecture (simpler MLP, linear gating) and a formal discussion of expert load balance would address the reviewer's open questions about MoE behavior.
- A non-separable high-dimensional test (e.g., Poisson with a quadratic cross-term) would probe the limits of the product ansatz and clarify where VI can meaningfully apply.

## Removed Points

The following points from the inputs were evaluated against the paper and removed:

- *"The paper does not test runtime or memory when training with MoE as dimensionality grows"* — The paper reports memory reduction (30.4–77.8% of independent MLP usage) and training times (1,579s vs. 1,184s for the 10D case). This is partially addressed, and the criticism overspecifies what should be in a conference paper.
- *"Missing related work"* — The paper's related work section adequately covers SPINNs, XPINNs, APINNs, BPINNs, and CP-decomposition, among others. The missing-reference concern is a strawman (the paper discusses these methods).
- *"The hyperparameter K selection lacks principled approach"* — This is retained in Minor weakness 5 but softened; the paper does discuss K selection post-hoc, so it is not a full omission, just a lack of systematic analysis.
- *Strength Finder's generic strengths* — Removed several generic claims (e.g., "the paper addressed an important problem") that lack concrete evidence. Only specific, evidenced strengths are retained.
- *"No discussion of load balancing or whether expert collapse occurs"* — The paper explicitly mentions that dense MoE "avoids expert collapse" and notes that for K=3 the additional expert gets small weights. This is discussed, though not deeply analyzed. Retained as minor observation.

## Novel Insights

The paper's core insight is that dimension decomposition (factorizing a PDE solution along coordinates) and domain decomposition (partitioning space into regions handled by separate models) can be layered within a single architecture: each MoE expert internally uses a shared-index MLP for dimension decomposition, while the router assigns soft domain-level specialization. This layering is clean and practically motivated—the shared MLP makes each expert parameter-efficient, and the MoE avoids manual partition design. The VI metric, while limited in scope, is the first attempt to give a quantitative interpretability score for such factorizations, going beyond the purely qualitative visual inspection used in prior work. The paper's honest documentation of VI failure modes (rank sensitivity for high-frequency wave components, dependence on separable reference solutions) is also a useful contribution to the community.

## Suggestions

1. **Add direct comparisons against SPINNs (for dimension decomposition) and XPINNs/APINNs (for domain decomposition) on the same benchmarks.** This is the single most impactful revision: without these comparisons, the paper cannot substantiate its claims of improvement over the most relevant prior work. A fair comparison should control for parameter count and problem configuration.

2. **Test the MoE framework on at least one nontrivial higher-dimensional or irregular-domain problem** (e.g., 2D Poisson with discontinuous coefficients, or a 2D+time convection-diffusion-reaction equation) to demonstrate that automatic domain decomposition generalizes beyond 1D spatial domains. This does not need to be high-dimensional—2D spatial is sufficient to move beyond the current (1+1)-D examples.

3. **Either implement and evaluate the Fourier-series workaround for VI on a non-separable problem, or explicitly re-scope the VI contribution** to separable PDEs and discuss when practitioners can usefully apply it. The current framing claims "quantitative interpretability" broadly, but the experiments only validate it on separable problems.

4. **Strengthen the 10D Poisson baseline** by using a deeper PINN (e.g., 8–10 layers) to match standard practice, and report whether the large error gap persists. Also consider adding a SPINNs baseline for this experiment.

5. **Add an ablation on the router architecture** (e.g., 2-layer vs. 5-layer MLP, linear gating) and a brief discussion of how K could be selected systematically (e.g., via validation error curves or expert weight entropy).

---

## Score and Decision

### Calibration Details

**Round 1 — Bracketing (3 queries, low/high exclusive bounds):**
- Query "PINNs domain decomposition mixture of experts PDE solving" (score < 3.5): retrieved weak anchors avg 1.50–3.00 (rejected/withdrawn papers). *The paper under review is clearly stronger than these.*
- Query "PINNs dimension decomposition interpretability PDE" (3.5 < score < 7.5): retrieved anchors avg 4.00–5.00 (Accept Poster / Reject). *These are the most relevant comparison group.*
- Query "PINNs interpretable machine learning physics-informed neural networks benchmark" (score > 7.5): retrieved anchors avg 8.00+ on unrelated topics (quantum ML, protein generation). *Not comparable.*

**Round 1 bracket: 4.0 – 6.0**

**Round 2 — Narrowing (inside bracket):**
- Query "PINNs dimension decomposition physics informed neural networks scalability" (4.5 < score < 6.5): retrieved IxAnL4PRsg (5.0, Accept), 8UdCE5nhFl (6.0, Accept), mJiPqOzc3O (4.67, Accept), 9OOmlDrEfn (4.67, Accept)
- Query "PINNs domain decomposition automatic adaptive mixture of experts" (3.5 < score < 5.5): retrieved lAhvPvxBZj (4.50, Withdrawn), IxAnL4PRsg (5.0, Accept), zrQkWSecMR (5.0, Accept)

**Anchors read in full:**
- CC2vIx3GZM (avg 4.0, Reject) — Similar limitation pattern (narrow scope, missing baselines). The paper under review is stronger: clearer contributions, quantitative results, more thorough evaluation within its scope.
- IxAnL4PRsg (avg 5.0, Accept) — Domain decomposition + neural operators; has theoretical analysis and broader experiments. The paper under review has comparable architectural novelty but weaker empirical validation.
- 9OOmlDrEfn (avg 4.67, Accept) — Neural POD solver; stronger baseline comparisons but similar theory-empirics gaps. Comparable overall quality.
- lAhvPvxBZj (avg 4.50, Withdrawn) — MoE for neural operators; similar missing-baselines problem. The paper under review is slightly better structured but shares core weaknesses.
- mJiPqOzc3O (avg 4.67, Accept) — Multiphysics training; heuristic decomposition with missing baselines. Comparable quality.

**Final score determination:** The paper sits near the 4.5–5.0 range of the calibration anchors. It has genuine contributions (shared-MLP design, VI metric, MoE integration) that are clearly presented and partially validated. However, the absence of comparisons against SPINNs/XPINNs—the methods this framework claims to improve upon—is a gap large enough to prevent a score above 5.0. The paper is somewhat stronger than the 4.0 anchor (CC2vIx3GZM, which was Rejected) due to clearer contributions and quantitative results, but weaker than the 5.0 anchor with broader experiments (IxAnL4PRsg). A score of **4.5** reflects a borderline paper with sound ideas that requires a major revision addressing the baseline comparisons and evaluation scope before its contributions can be properly assessed for acceptance.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>