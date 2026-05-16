Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes MolJO, a joint gradient-guidance framework for structure-based molecule optimization (SBMO) built on Bayesian Flow Networks (BFNs). It derives joint guidance over both continuous atom coordinates and discrete atom types within a unified SE(3)-equivariant framework, and introduces a backward correction sampling strategy that aggregates past history via a sliding window to balance exploration and exploitation. Experiments on the CrossDocked2020 benchmark show strong results (Success Rate 51.3%, Vina Dock -9.05, SA 0.78), substantially outperforming the prior gradient-based method TAGMol and remaining competitive with oracle-based approaches, with extensions to constrained optimization tasks.

## Strengths

- **First joint gradient guidance over continuous and discrete modalities**: The paper derives a principled way to guide both atom coordinates (continuous) and atom types (discrete) within a unified SE(3)-equivariant framework (Section 4.1, Proposition 4.1). This directly addresses the modality-inconsistency issue of prior gradient-based methods (e.g., TAGMol guides only coordinates). The ablation in Figure 5 quantitatively confirms that joint guidance consistently outperforms single-modality guidance, with affinities benefiting more from coordinate guidance and drug-likeness from type guidance.

- **Backward correction strategy with sliding window**: The proposed strategy (Section 4.2, Algorithm 1) allows the model to correct past sampling steps by maintaining a sliding window of history. Figure 2 shows that intermediate window sizes yield higher gradient cosine similarity at later timesteps, and Table 4 demonstrates that backward correction boosts both unguided sampling and guided optimization (Success Rate improves from 46.5% for Full B.C. to 51.3% for B.C. under guidance).

- **Strong empirical performance with 4× improvement over the gradient-based baseline**: On CrossDocked2020, MolJO achieves Vina Dock -9.05, SA 0.78, and Success Rate 51.3% (Table 1). This is a >4× improvement in Success Rate over the best gradient-based baseline TAGMol (12.7%), and the "Me-Better" Ratio shows a 2× advantage over other 3D baselines.

- **Versatility for constrained optimization tasks**: MolJO is extended to R-group optimization and scaffold hopping (Section 5.3, Table 3), achieving the highest validity (100% for in-fill tasks) and best Success Rate (e.g., 67.5% for R-group growing vs. next best 44.2%), demonstrating practical utility for lead optimization.

- **SE(3)-equivariance guarantee**: Proposition 4.4 formally shows that the guided sampling preserves SE(3)-equivariance when both the generative network and energy function are equivariant and the complex is centered at the protein's center of mass.

## Weaknesses

### Fatal
None.

### Major

- **"Me-Better" Ratio is never formally defined.** The metric is invoked in the abstract, contributions, Figure 1B, and conclusion as a headline result ("2× Me-Better Ratio as much as other 3D baselines"), but the paper provides no definition at all—not even in the Metrics paragraph (Section 5.1), which defines Success Rate, Vina scores, QED, SA, and Diversity. Without knowing how "Me-Better" is computed (fraction of molecules improving over a reference? improvement on which criteria? improvement threshold?), this key claim is unverifiable.

- **No statistical uncertainty reported.** Table 1, Table 3, and Table 4 report only point estimates (means) with no standard deviations, confidence intervals, or error bars. Given the stochasticity of the generative and guidance processes, the reader cannot assess whether the reported differences (e.g., 51.3% vs. 46.5% Success Rate) are significant or within noise. This is a standard expectation for empirical ML papers.

- **The energy function used to produce guidance gradients is underspecified.** The paper relies on an energy function $E(\theta, \mathbf{p}, t)$ to predict molecular properties and provide gradients, and Proposition 4.4 asserts it should be SE(3)-equivariant. However, no details are given about its architecture, training data (clean molecules, noisy intermediates, or the $\theta$ representation?), loss function, or procedure for obtaining labels at intermediate timesteps. This component is central to the method—without it, there is no guidance. *Note: some implementation details may reside in sections stripped by the parser, which would mitigate this concern if present in the original submission.*

### Minor

- **The novelty of the backward correction strategy is incremental and transparently positioned as such.** The paper itself acknowledges (line 179) that the sliding window "unifies" Graves et al. (2023) ($k=1$) and Qu et al. (2024) ($k=n$). The contribution is the empirical demonstration that an intermediate $k$ works best and the gradient-similarity analysis (Figure 2). This is a solid but modest extension—the paper would benefit from framing it as a practical improvement rather than a novel mechanism. The ablation (Table 4) is informative but does not systematically sweep $k$ to characterize the trade-off landscape.

- **The claim of "state-of-the-art" is ambiguous.** The paper claims "state-of-the-art performance" (abstract) with Success Rate 51.3%, but the text acknowledges DecompOpt "show[s] satisfactory Success Rate" (line 217). If DecompOpt achieves higher Success Rate (the reviewer claims 54.8%), then MolJO is not SOTA on that metric. The paper should explicitly specify which comparison class (gradient-based methods vs. all methods vs. 3D methods) the SOTA claim refers to, and qualify it by metric.

- **No limitations section is provided.** The paper does not discuss potential failure modes (e.g., energy function generalization to out-of-distribution pockets, risk of mode collapse from strong guidance, sensitivity to the choice of $k$ and guidance scale $s$). A brief discussion would improve scientific rigor.

- **Hyperparameter $k=130$ is used without justification.** The paper uses $k=130$ for backward correction (Table 4) but does not explain how this value was selected or how sensitive results are to it. A sweep over $k$ values would strengthen the characterization.

### Trivial
None.

## Nice-to-Haves

- **Energy function training details** — if not in the stripped sections, providing the architecture, training data, and loss formulation would significantly improve reproducibility.
- **Comparison of computational cost vs. oracle-based methods** — the paper positions itself as more efficient than oracle methods but provides no runtime or FLOPs comparison.
- **A systematic sweep of $k$** (e.g., 1, 50, 100, 130, 200) with Success Rate, Vina Dock, and gradient similarity to more rigorously demonstrate the explore–exploit trade-off claimed in Figure 2.
- **Statistical uncertainty estimates** (standard deviations or bootstrapped confidence intervals) for the main results.

## Removed Points

These points were raised by reviewers but removed per the filtering guidelines:

- **"The energy function $E(\theta, t)$ is not specified, preventing reproducibility and undermining the core claim"** — weakened from Fatal to Major and noted that details may reside in parser-stripped sections. The core claim (joint gradient guidance) is not undermined by missing energy function training details alone, as the guidance derivation and framework are self-contained.
- **"TAGMol already uses gradient guidance on coordinates"** — the paper does not claim to be the first gradient-based method overall; it claims "first *joint* gradient-based SBMO framework," which is accurate and properly distinguishes from TAGMol.
- **"The backward correction is equivalent to aggregating multiple BFN steps into a single larger jump"** — the paper explicitly acknowledges this unification (line 179). The contribution is the intermediate-$k$ regime and its empirical validation, not a claim of a fundamentally new mathematical operation. Kept as Minor with adjusted framing.
- **"Generative baselines are not optimized"** — this is expected; the primary comparisons are to optimization methods (TAGMol, DecompOpt, RGA, AutoGrow4), which are correctly positioned.
- **Pure formatting/style nitpicks and sentence-level pedantry** — removed as per guidelines.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an angle the authors themselves missed.

## Suggestions

1. **Define "Me-Better" explicitly** in the Metrics paragraph of Section 5.1: provide the formula (e.g., fraction of generated molecules that improve upon the reference molecule on a composite or individual criterion) and the improvement threshold.
2. **Add error bars or standard deviations** to all main tables (Tables 1, 3, 4). Even reporting results across multiple random seeds (3 runs) would substantially strengthen the empirical claims.
3. **Clarify the SOTA claim** — specify "state-of-the-art among gradient-based methods" or report Success Rate relative to all baselines and discuss where MolJO leads and where it trails.
4. **Systematically ablate $k$** (e.g., 1, 50, 100, 130, 200) with both guided and unguided variants to directly validate the claimed explore–exploit trade-off.
5. **Add a Limitations paragraph** discussing energy function generalization, guidance scale sensitivity, and potential failure cases.
6. **Provide energy function specifications** — architecture, training data, loss function — either in the main text or appendix.

## Score and Decision

The paper makes a genuine contribution: it is the first SBMO framework to jointly guide both continuous coordinates and discrete atom types via gradients, and it demonstrates clear empirical improvements over the prior gradient-based method (TAGMol). The backward correction strategy is a modest but useful extension with empirical support. The constrained optimization results (R-group, scaffold hopping) are particularly compelling for practical drug design.

However, the paper has significant presentation gaps: the headline "Me-Better" metric is undefined, no statistical uncertainty is reported, and the energy function (the very source of the claimed gradients) is underspecified. These are fixable in revision but weaken the current submission.

**Score**: 6.0 — A solid paper with real contributions, but held back by incomplete specification and missing statistical rigor. With the suggested revisions, it would be a strong accept.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>