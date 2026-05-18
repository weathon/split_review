Now I have all the information I need. Let me produce the final consolidated review.

## Summary

The paper proposes Tree-Sliced Wasserstein on Systems of Lines (TSW-SL), a generalization of Sliced Wasserstein that replaces one-dimensional projection lines with tree-structured systems of intersecting lines. The key technical innovations are: (1) defining tree systems as metric spaces with tree metrics (enabling closed-form Wasserstein-1 computation), (2) introducing a Radon transform on systems of lines with provable injectivity, and (3) the TSW-SL distance itself with claimed matching complexity to SW. Experiments on gradient flows, color transfer, GANs, and diffusion models show consistent improvements over vanilla SW.

## Strengths

1. **Novel tree-structured projection domain enabling closed-form OT.** The paper replaces 1D lines with tree systems—connected sets of lines equipped with a tree metric. Theorem 3.2 proves each tree system is metrizable by a tree metric, and Equation (13) gives a closed-form Wasserstein-1 expression on that metric. This directly addresses a key limitation of SW (loss of topological information from 1D projection) while preserving computability.

2. **Generalized Radon Transform with injectivity.** Definition 4.1 introduces a Radon transform on systems of lines, parameterized by splitting maps α. Theorem 4.2 proves injectivity of this transform, generalizing the classical Radon transform. This is a genuine theoretical contribution independent of the specific application.

3. **Consistent empirical improvement over SW across diverse tasks.** In gradient flows (Tables 1–2), the method reduces Wasserstein distance vs. SW; in GANs (Table 3) it improves FID/IS on CelebA and STL-10; in diffusion models (Table 4) it outperforms SW and several SW variants on CIFAR-10. The improvements appear consistent across settings.

4. **Explicit construction algorithm (Algorithm 1) and Monte Carlo estimation (Algorithm 2).** The paper provides concrete, implementable procedures for sampling tree systems and computing TSW-SL, making the method readily usable in existing SW-based pipelines.

## Weaknesses

### Major

1. **Underspecified splitting map α undermines interpretability of all experiments.** The paper states only that α is "selected either as a trainable constant vector or a random vector" (Section 6). It does not specify: which experiments use which variant, the distribution of the random vector, whether α is optimized per task, or how its parameters are chosen. Since α controls how mass is distributed across the k lines of each tree system, the source of empirical improvement over SW is ambiguous. TSW-SL could outperform SW because the tree structure captures more topological information, or because α provides additional degrees of freedom that are optimized per task (effectively an unfair advantage over fixed-projection SW). This ambiguity is the single largest obstacle to evaluating the paper's empirical claims. *Impact: Without specifying α per experiment, the core empirical results cannot be properly interpreted.*

2. **Gap between the injectivity theorem and the metric property of TSW-SL.** Theorem 4.2 proves injectivity of the full Radon transform R^α over *all* systems of lines L∈L_k^d. However, TSW-SL integrates only over tree systems sampled from a specific distribution σ (which the paper acknowledges produces only chain-like trees). For TSW-SL to be a metric, one needs that the *restricted* map μ → E_{L∼σ}[δ_μ^L] is injective — i.e., that equality of the projected measures for σ-almost every sampled tree system implies equality of the original measures. The paper does not address whether injectivity for all L∈L_k^d implies injectivity for the expectation under σ, nor does it provide additional arguments for the restricted domain. Theorem 5.2's claim that TSW-SL is a metric therefore rests on incomplete justification. *Impact: A central theoretical claim is not fully supported.*

3. **Mismatch between claimed generality (tree systems) and actual implementation (chain-like trees).** The paper's title, abstract, and theoretical development (Sections 3–4) discuss general tree systems with arbitrary topology. However, the construction in Section 3.3 and Algorithm 1 explicitly produces only *chain-like* trees where line i intersects line i+1 sequentially — no branching or non-chain topology is sampled. All experiments use this chain construction (k=3–5). While the paper acknowledges this ("chain-like tree structure," line 117), the framing throughout claims generality to "tree systems." The theoretical framework genuinely supports arbitrary trees, but the paper's practical contribution is a chain-of-lines projection. This discrepancy means the claimed advantage over using multiple independent 1D lines is not clearly separated from simply using more projection directions. *Impact: The paper's scope is narrower than advertised; the reader cannot evaluate whether the tree metric itself or merely having more projection directions drives improvement.*

### Minor

4. **Computational complexity analysis omits tree Wasserstein computation cost.** The paper claims O(L k n log n + L k d n) complexity (Section 5.2 Remark), asserting it matches SW. This counts projection and per-line sorting. However, computing the tree Wasserstein (Equation 13) requires mapping projected points onto the tree Ω_L and summing weighted differences over edges. For a chain of k lines, this adds overhead that is modest for k=3–5 but not accounted for in the asymptotic analysis. The claim of equivalent complexity to SW is slightly overstated as presented. *Impact: Minor — the practical difference for small k is small, but the analysis should be honest about what is included.*

5. **Notation ambiguity between measure and density views.** The paper defines "probability distributions on L" as functions f∈L^1(L̅) with ||f||_L=1 (a density), but then works with discrete measures and uses the same notation for both views. The paper acknowledges this (line 177) but the switch can confuse readers, especially around Equation (13) where ℛ_ℒ^α μ(Γ(v_e)) requires integrating the projected density over a subtree but is applied to discrete measures. *Impact: Minor — does not affect correctness but harms readability.*

### Trivial

6. **No comparison with a simple "independent multiple lines" baseline.** The paper compares TSW-SL (e.g., 25 trees × 4 lines = 100 lines) against SW (100 lines). A more controlled baseline would be SW on 100 independent lines plus a post-hoc merging step without tree structure. This would isolate whether the tree metric itself drives gains. The critic's suggestion for this comparison is well-taken but the omission is not fatal.

7. **Missing ablation on k (number of lines per tree).** The paper uses k=3–5 in experiments but never studies how performance changes with k at a fixed total line count. Understanding the trade-off between tree complexity (k) and number of Monte Carlo samples (L) would strengthen the paper.

## Nice-to-Haves

- A controlled experiment with *fixed uniform* α (α(x)_l = 1/k) would isolate the benefit of the tree structure from the benefit of optimizing α. This is the most informative single experiment the authors could run.
- An ablation varying k (lines per tree) while keeping total lines L×k constant would help understand the role of tree complexity.
- A comparison against independent multiple lines (SW with L×k projections, no tree structure) would test whether the tree metric itself provides benefit over just having more projection directions.
- Brief qualitative comparison with tree-based Wasserstein approaches (Le et al., 2019, already cited as background) would help position the contribution relative to tree OT literature.

## Removed Points

These points from the reviewers were identified as not valid weaknesses and are listed here only for completeness:

- **"Caveat vs. results contradiction"** — The critic claimed the paper's modest caveat ("without expecting TSW-SL to outperform more recent SW variants") is undercut by the strong results. This is not a weakness; the paper is simply being cautious, and the fact that results exceed expectations is a positive. *Removed as not a weakness.*
- **"Probability distribution definition conflates densities and measures"** — The definition (f∈L^1(L̅), f≥0, ||f||_L=1) is standard notation for densities representing absolutely continuous measures. The paper separately handles discrete measures, which is standard practice. *Removed as a non-issue.*
- **Generic strengths from Strength Finder that conflict with verified weaknesses** — The claim that "TSW-SL is a metric with the same computational complexity as SW" is partially undermined by the injectivity gap (Weakness 2) and the complexity omission (Weakness 4). These caveats are reflected in the weaknesses above.
- **"Missing related work on tree-based Wasserstein"** — The paper already cites Le et al. (2019) for tree Wasserstein. The critic's suggestion for broader comparison is moved to Nice-to-Haves. *Removed per instruction not to mention missing related works.*

## Novel Insights

The most novel observation from synthesizing the reviews is that the paper's theoretical contribution (general tree systems) and practical contribution (chain-like trees) are decoupled to an unusual degree. The Radon transform and injectivity proof work for arbitrary tree topologies, but the actual algorithm and experiments only use linear chains. This suggests a two-tier publication strategy: the theoretical framework (Sections 3–4) could stand as a separate contribution, while the empirical method (Section 5–6) is properly a "Chain-Sliced Wasserstein" that happens to use tree metric computation as a subroutine. Connecting these tiers more honestly would strengthen the paper.

## Suggestions

1. **Specify α for every experiment.** For each table/figure, state whether α is fixed uniform, fixed other, random (and its distribution), or trainable (and how it is optimized). This is the single most critical missing piece.

2. **Run an ablation with fixed uniform α (α_l = 1/k).** This isolates the tree structure benefit from the α optimization benefit and provides a fair comparison to standard SW.

3. **Address the injectivity → metric gap.** Either provide additional arguments showing that the restricted Radon transform over the sampled distribution σ is injective, or note this as a limitation of Theorem 5.2 and reframe the metric claim conditionally.

4. **Rename or reframe to match scope.** Either extend the sampling algorithm to support branching tree topologies, or retitle the method to something like "Chain-Sliced Wasserstein" and adjust the theoretical framing to match the chain construction.

5. **Revise the complexity analysis** to account for tree Wasserstein computation, and include empirical runtime comparisons that scale with k and n.

6. **Add a baseline with independent multiple lines** (SW with L×k projections, no tree structure) to better isolate the benefit of the connected tree structure.

## Score and Decision

**Originality:** 7/10 — The tree-structured projection domain is a genuinely novel generalization of SW. The Radon transform variant is new.

**Importance of research question:** 7/10 — Improving SW's topological capture is an important direction given SW's widespread use.

**Claims support:** 4/10 — The α underspecification and the injectivity gap mean central empirical and theoretical claims are not fully supported.

**Soundness:** 5/10 — The theoretical framework is sound in its general form, but the connection to the practical method has gaps. The empirical methodology has an unresolved ambiguity.

**Clarity:** 6/10 — The paper is generally well-structured but the α specification is critically unclear.

**Value to community:** 6/10 — The core idea is valuable, but the paper needs tightening before the community can rely on its claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>