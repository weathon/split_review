Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper proposes replacing the one-dimensional projection lines in Sliced Wasserstein (SW) with *tree systems* — collections of lines connected in a tree structure, each carrying a tree metric that admits closed-form OT. It introduces a generalized Radon transform with splitting maps to transfer measures onto tree systems, defines the Tree-Sliced Wasserstein distance on Systems of Lines (TSW-SL), proves its metric property and injectivity of the transform, and demonstrates empirical improvements over SW and several variants on gradient flows, color transfer, GANs, and denoising diffusion models.

## Strengths

1. **Novel and principled theoretical framework.** The paper rigorously defines tree systems as metric spaces with tree metrics (Theorem 3.2) and provides a closed-form expression for the 1-Wasserstein distance on these systems (Equation 13). This directly enables the core innovation: replacing 1D lines with a more expressive structure while preserving computational tractability. The theoretical development (tree system topology, generalized Radon transform, injectivity) is coherent and sound.

2. **Generalized Radon transform with injectivity.** Definition 4.1 introduces the Radon Transform on Systems of Lines using splitting maps, and Theorem 4.2 proves its injectivity for all continuous splitting maps. This is a nontrivial generalization of the classical Radon transform, and the injectivity property is essential for TSW-SL to be a metric (Theorem 5.2) and to faithfully capture structural information.

3. **TSW-SL is a metric that reduces to SW as a special case.** Theorem 5.2 establishes TSW-SL as a metric on probability distributions, and the remark in Section 5.1 shows that when tree systems consist of a single line, TSW-SL recovers standard SW. This demonstrates consistent generalization and theoretical hygiene.

4. **Convincing empirical evidence across multiple tasks.** The experiments consistently show TSW-SL outperforming SW, MaxSW, SWGG, and LCVSW in Wasserstein distance reduction on gradient flows (Tables 1–2), color transfer quality (Figure 5), FID/IS in GANs (Table 3), and FID in diffusion models (Table 4). The improvements are demonstrated with fair comparisons using matched total projection directions.

5. **Computational efficiency maintained.** The time complexity analysis (O(L k n log n + L k d n)) shows TSW-SL has the same asymptotic complexity as SW when using the same total number of projection directions. The paper explicitly ensures fair comparisons by matching this budget across methods.

## Weaknesses

### Fatal
None.

### Major

1. **Scope mismatch: general "tree systems" framing vs. chain-only implementation.** The paper formally defines tree systems as arbitrary connected systems of lines with a tree structure derived from their intersection graph (Section 3.1). However, the practical construction (Section 3.3, Algorithm 1) explicitly produces only *chain-like* tree structures ("The tree system produced by this construction has a chain-like tree structure, where the i-th line intersects the (i+1)-th line"), and all experiments use these chains with k=3–5. While a chain is technically a tree, the paper does not test genuinely branching structures (e.g., Y-shaped trees with ≥3 lines meeting at a point), nor does it compare chains against independent multiple lines in a way that isolates the benefit of coupling. The paper's contribution statement (item 1) claims "tree systems" as a general concept, but the empirical support only covers a special case. This limits the generality of what is demonstrated. **Why it matters:** A reader cannot tell whether the benefit comes from the tree metric per se or simply from using multiple coupled lines arranged in a chain, and whether branching structures would add further value.

2. **The splitting map α is empirically unexamined.** The splitting map α (a continuous map from ℝ^d to the simplex) is a central component of the Radon transform on tree systems — it determines how each point's mass is distributed across lines. In experiments, α is chosen as either a trainable constant vector or a random constant vector (independent of location). The paper provides no ablation study comparing different α strategies (e.g., location-dependent α, trained per tree system, uniform vs. learned). A constant α means every point is split identically regardless of its spatial position, which is a strong assumption whose impact on the distance is never analyzed. **Why it matters:** Without understanding α's role, it is unclear whether the method's success is robust to this choice or depends on specific tuning, which weakens reproducibility and scientific understanding.

### Minor

1. **Sensitivity to k (number of lines per tree system) not explored.** All experiments use fixed k values (3–5). A plot showing performance vs. k for at least one task (e.g., gradient flow on 25 Gaussians) would clarify whether improvement plateaus or is sensitive to this parameter. This is a straightforward addition that would strengthen the empirical section.

2. **Lack of a qualitative synthetic example illustrating when TSW-SL succeeds and SW fails.** The paper shows quantitative improvements and qualitative outputs (style transfer, gradient flow snapshots), but a dedicated synthetic example where two measures are SW-indistinguishable but TSW-SL-distinguishable would make the contribution more intuitive and compelling. The current results suggest this is the case but do not directly demonstrate it.

3. **Metric property conditions on σ not discussed in main text.** Theorem 5.2 states TSW-SL is a metric, and the definition depends on the distribution σ over tree systems (as noted in the remark). The main text does not discuss what condition on σ is sufficient for the metric property or verify that the chain-generating procedure (Algorithm 1) satisfies it. This reasoning presumably appears in the appendix (stripped by the parser), but the main text would benefit from stating the condition explicitly.

### Trivial
None — the paper is reasonably well-written and the minor issues above are already captured.

## Nice-to-Haves

- A brief wall-clock runtime comparison for the GAN and diffusion experiments (in addition to the gradient flow times already reported in Table 1) would help verify that the practical overhead remains similar to SW in all settings.
- Comparison or discussion of subspace-based OT approaches (e.g., Subspace Robust Wasserstein, Projection Robust Wasserstein) could help position the work, though the paper explicitly scopes its comparison to SW and its variants, which is defensible.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about missing formal precision in the definition of "connected" for a system of lines.** The paper states "its points form a connected set in ℝ^d" — this is standard mathematical language and sufficiently precise for the paper's purposes. [Removed as nitpick]
- **Notation nitpicks about dots (e.g., \dot{ℝ}^d, \dot{μ}).** These are parser artifacts, not author errors. [Removed per formatting rule]
- **Criticism about missing comparisons with Subspace Robust Wasserstein / Projection Robust Wasserstein.** The paper cites these works in its related work section and explicitly states "our primary comparison is between TSW-SL and the original SW" (Section 6, line 230). This is a deliberate scope choice. [Removed as scope creep]
- **Claim that the metric property criticism invalidates the theorem.** The proof of Theorem 5.2 is in the appendix (stripped by the parser). The concern about directional coverage is also mitigated because each line in the chain independently samples its direction from U(𝕊^{d-1}), providing rich directional coverage. [Partially removed per "missing appendix" rule; softened version kept in Minor #3]

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the reviews is the tension between theoretical generality and practical convenience: the paper develops a general theory of tree systems but only implements chains, and this gap echoes a broader pattern in the SW generalization literature where the gap between what is formally defined and what is empirically tested often goes unremarked. The reviews surface that the most severe-looking weaknesses (metric property, injectivity) are well-addressed by the theory, while the real empirical gap is more subtle — not in correctness, but in the breadth of what is demonstrated versus what is claimed.

## Suggestions

1. **Narrow the framing or broaden the experiments.** Either (a) explicitly adopt chain-like tree systems as the paper's focus, adjust the title/abstract slightly to reflect this, and add a comparison against an equivalent number of independent (uncoupled) lines to isolate the benefit of the chain coupling; or (b) implement and test genuinely branching tree systems (e.g., 3+ lines meeting at a point) and compare against chains. Option (a) is simpler and likely sufficient given the paper's existing contributions.

2. **Add an ablation study of the splitting map α** for at least one task (e.g., gradient flow on 25 Gaussians). Compare: constant random α, constant trainable α, and a location-dependent α (e.g., distance-weighted). If performance is robust across choices, this is a strength; if it is sensitive, the paper should provide guidance on choosing α.

3. **Add a sensitivity analysis for k** (number of lines per tree system) on at least one task to show whether improvement plateaus.

4. **Clarify the condition on σ** (distribution over tree systems) needed for TSW-SL to be a metric in the main text, even if briefly, rather than deferring entirely to the appendix.

## Score and Decision

The paper presents a novel, technically sound generalization of Sliced Wasserstein with a well-developed theoretical foundation (tree system topology, generalized Radon transform, injectivity, metric property) and convincing empirical results across multiple domains. The main weakness is a scope mismatch — the general "tree systems" framing is only validated on the chain subclass — and the splitting map design is left unexamined. These issues are real but addressable and do not undermine the paper's core contribution. The paper makes a genuine contribution to the OT literature.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>