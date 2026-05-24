Now let me write the final consolidated review.

## Summary

This paper establishes a first-order equivalence between activation steering and influence functions for neural networks. It provides closed-form mappings (IAS vector, Theorem 4.2), a principal-angle diagnostic γ that bounds when steering can match influence (Theorem 5.1), a spectral optimality result for principled direction selection (Theorem 5.3), and generalization bounds for low-rank steering (Theorem 6.1). The core insight—that steering vectors and influence-based data weightings are projections of the same sensitivity tensor—is novel and theoretically clean.

## Strengths

- **Closed-form duality connecting activation steering and data influence.** Theorem 4.2 proves that any infinitesimal steering vector corresponds to a signed influence weighting over training data and vice versa, with explicit norm bounds. This provides the first constructive mathematical bridge between two previously separate lines of work. The primal-dual formulation (Section 3) makes the geometry transparent.

- **Alignment diagnostic with rigorous error bound.** Theorem 5.1 gives a precise bound √(1−γ²) on how well activation steering can match a parameter-space influence update, where γ is the minimum principal-angle cosine between the two Jacobian subspaces. This is cheap to compute (two small SVDs) and yields a principled pre-check for whether steering is even feasible. Figure 2 confirms γ increases with layer depth, supporting the theory.

- **Spectral optimality for steering direction selection.** Theorem 5.3 derives the optimal steering vector under an ℓ₂ budget as the top eigenvector of a Fisher-influence matrix Σ, replacing ad-hoc direction choices (e.g., contrastive activation addition) with a theoretically grounded recipe. The power-iteration procedure makes this practical.

- **Generalization guarantee for low-rank interventions.** Theorem 6.1 proves the excess Rademacher complexity from a rank-k IAS correction is bounded by αL√(2k/(dn)), showing that steering interventions have benign generalization impact when layer width d and sample size n are large. This provides formal comfort that steering does not silently degrade out-of-distribution performance.

## Weaknesses

### Fatal

None. The core theoretical results hold mathematically; the issues are empirical rather than foundational.

### Major

- **The data-attribution pipeline—arguably the most practically significant claim—is never demonstrated.** Corollary 1 and Section 4.1 promise that ρₛ pinpoints the fewest training examples reproducing a steering-induced behavioral change. The paper explicitly writes "see Section 7" (line 134) for this validation, but Section 7 contains no example retrieval, no qualitative inspection of top-weighted examples, and no comparison to existing attribution methods (e.g., Koh & Liang 2017, TracIn). This is the killer application of the theory and its absence is the paper's most significant evidential gap.

- **Implausible perplexity values.** Table 1 reports perplexity values of 14333 (baseline), 13291 (CAA), and 13701 (IAS) for GPT-2 Medium on WikiText. GPT-2 Medium's typical perplexity on WikiText is ~30. A perplexity of 14333 corresponds to a model performing near chance, which cannot be correct for GPT-2 Medium on a standard benchmark. Either the metric is mislabeled (e.g., it is raw loss sum rather than exponentiated average loss) or there is a code error. This undermines trust in the quantitative results of Table 1.

- **Unexplained slope of 1.5 in the first-order equivalence experiment.** Figure 1 reports predicted vs. actual logit shifts with cosine 0.978 but slope 1.50. A slope of 1.5 means the IAS vector produces a 50% larger logit shift than the influence prediction, which is a systematic—not random—deviation. The paper describes this as "consistent with the expected linear regime" (line 243) without acknowledging, let alone explaining, the discrepancy. If the first-order equivalence were exact, the slope should be near 1.0 (up to noise and higher-order terms). The paper should either explain why 1.5 is expected (e.g., from the damping parameter λ, the chosen magnitude α, or regularization in the pseudoinverse), or correct the computation.

- **Experimental evaluation is far too narrow for the breadth of the claimed contributions.** Language experiments use only GPT-2 Medium on one task (detoxification) with one baseline (CAA). No results are shown on other LLMs (LLaMA, OPT), other tasks (factual editing, bias mitigation, instruction following), or other steering baselines (e.g., functional interventions, contrastive search). Given that the paper positions IAS as "a unified first-order framework" applicable to "billion-parameter models," this single-model, single-task evidence base is insufficient.

### Minor

- **The γ diagnostic is computed but never validated as predictive of steering success.** Figure 2 shows γ increases with layer depth, but there is no experiment demonstrating that low-γ layers actually fail at steering or that γ-based layer selection improves downstream performance over, say, always picking layer 11. The heuristic "pick γ ≥ 0.7" is presented without supporting evidence. The no-free-lunch theorem (6.2) remains a theoretical bound with no empirical test.

- **The spectral optimality experiment (Figure 3) does not validate steering performance.** The ResNet-50 experiment only shows that the spectral radius for the true label is statistically significant (p=0.005) against a null distribution from random labels. It does not demonstrate that the spectral direction actually *steers* effectively—there is no steering performance metric (logit change, accuracy under intervention, comparison to CAA or contrastive directions). The theorem's practical relevance is asserted but untested.

- **Missing error bars and statistical rigor.** Table 1 reports point estimates without standard errors, confidence intervals, or significance tests. The detoxification comparison shows IAS numerically worse than CAA on both metrics, but the reader cannot assess whether this gap is meaningful. The ResNet-50 permutation test (Figure 3) appears to use only ~100 random draws (histogram counts peak at 14), which is small for a robust null distribution.

- **Possible equation error in Section 3.2.** Equation (2) on line 88 states Δh* = J_{h→y}ᵀ J_{θ→y} Δθ, but substituting λ* gives Δh* = −J_{h→y}ᵀ (J_{h→y}J_{h→y}ᵀ)† J_{θ→y} Δθ = −J_{h→y}† J_{θ→y} Δθ. The expression as printed is missing the pseudoinverse. However, this could be a parser artifact; the correct form (J_{h→y}† J_{θ→y} Δθ) appears in Theorem 5.2, suggesting the error is in presentation rather than understanding.

### Trivial

- The ResNet-50 experiment (Figure 3) should state the number of random draws and the full permutation-test protocol.

## Nice-to-Haves

- Demonstrate the data-attribution pipeline: pick a steering vector, compute ρₛ, retrieve the top-10 training examples, show qualitative/quantitative evidence they are causally related to the behavior, and compare against an influence-function baseline.
- Validate the γ diagnostic: compare steering success (logit change per unit norm) when a low-γ vs. a high-γ layer is chosen, showing the no-free-lunch bound is predictive.
- Add an ablation on steering magnitude α to show when the first-order approximation breaks down (e.g., at what α does cosine drop below 0.9?).
- Discuss the computational cost of the spectral recipe (per-example gz computation).
- Add a discussion of influence-function fragility (Basu et al., 2021) as a limitation of the proposed workflow.

## Removed Points

- *"The empirical core of the equivalence claim is contradicted by the paper's own data (slope 1.50 is a fatal flaw)"* — Kept but demoted from "Fatal" to "Major." A slope of 1.5 indicates a systematic discrepancy but is not fatal: the cosine of 0.978 shows very high linear alignment, and the deviation could stem from damping regularization λ or the chosen magnitude α. The paper's core claim is about first-order equivalence of *structure*, not exact numerical equality of scale. This is a serious issue but not structurally fatal.
- *"The primal-dual framing is not essential"* — Removed. The framing is mathematically natural for the paper's results and helps exposition.
- *"Lemma 4.1 is basic chain rule, not a contribution"* — Removed. It is a standard lemma used to set up the subsequent theorems, not presented as a standalone contribution.
- *"Theorem 6.1 is a straightforward application of Pinto et al."* — Removed. Many useful results build on prior bounds; the paper properly cites the source and provides a concrete application to steering.
- *"Section 8 does not engage with Basu et al. on influence function fragility"* — Removed as a weakness. Moved to Nice-to-Haves as a suggestion.
- *"No reproducibility information"* — Removed per instructions (hyperparameters, random seeds trivial to list; appendix sections stripped by parser).
- Various formatting nitpicks and speculation about missing appendix sections — Removed per instructions.
- *"The ResNet-50 permutation test uses only ~100 random draws"* — Kept as part of the minor weakness on spectral optimality validation.
- Strength Finder's strength #5 ("Empirical validation of first-order equivalence"): the claim that "the theoretical duality is numerically accurate in practice" is overstated given the 1.5 slope. Modified to note the qualification.
- Strength Finder's strength #7 ("Minimal data re-weighting guarantee"): the practical payoff is claimed but never experimentally shown. Kept as a theoretical strength but made clear it is not validated.
- Generic strengths from Strength Finder ("addressed an important problem," "targeted an interesting question") — Removed.

## Novel Insights

None beyond the paper's own contributions. The key observation—that steering vectors and influence weightings are dual projections of the same Jacobian structure—is the paper's novel contribution; the reviews do not add an independent insight.

## Suggestions

1. **Fix the perplexity metric.** Clarify whether the reported numbers are perplexity, token-level loss sum, or something else. If they are truly perplexity, this suggests a bug that must be resolved before the paper can be trusted.

2. **Explain the slope 1.50 in Figure 1.** Run an ablation varying the damping parameter λ and the steering magnitude α to identify the source of the scaling factor. Even better, show that the slope becomes 1.0 when α→0 (or λ→0), confirming the first-order theory.

3. **Demonstrate the data-attribution pipeline.** This is the paper's most compelling practical selling point and its absence is the biggest weakness. A single qualitative example with top-weighted training examples would significantly strengthen the paper.

4. **Broaden the experimental evaluation.** At minimum add: (a) a second LLM (e.g., LLaMA-7B), (b) a second task (e.g., factual recall steering), (c) error bars on all tables, and (d) a comparison of γ-based layer selection vs. fixed late-layer selection.

## Score and Decision

**Round 1 (Bracketing):**
- Weak anchors (< 3.5): "Influence-based Attributions can be Manipulated" (3.0), "Measuring Effects of Steered Representation" (3.0), "Feature Level Instance Attribution" (3.0). The paper under review is clearly stronger than these—it has a coherent theoretical framework and clean results, while those papers have fundamental motivation or execution problems.
- Middle anchors (3.5–7.5): "Towards Unifying Interpretability and Control" (5.25), "Editable Concept Bottleneck Models" (5.6), "NeurFlow" (6.5). The paper under review has cleaner theory than the first two but weaker experiments than all three.
- Strong anchors (> 7.5): "Influence Functions for Scalable Data Attribution in Diffusion Models" (8.0), "Exploring The Loss Landscape" (8.0). The paper under review is clearly below these—they have comprehensive experiments or tight theoretical analyses that the current paper lacks.

**Initial bracket:** 4.5–6.0.

**Round 2 (Narrowing within bracket):**
- "Towards Unifying Interpretability and Control" (5.25, Reject): similar in combining multiple methods under a unified framework, similarly limited experiments. The paper under review has cleaner, more novel theory, but similarly narrow validation. Comparable, with a slight edge to the current paper on theory.
- "Editable Concept Bottleneck Models" (5.6, Reject): similar structure (influence functions + theory + experiments on one model type). The current paper's theory is cleaner and more original, but the ECBMs paper has more thorough experiments across multiple datasets and editing scenarios. Roughly comparable.
- "Improving Instruction-Following through Activation Steering" (7.0, Accept Poster): stronger empirical validation across 4 models, multiple tasks, with thorough analysis of steering composition and transfer. The current paper's experiments are much weaker; the theory is different in nature (less applied, more foundational). The current paper is clearly below this anchor.
- "Sufficient and Necessary Explanations" (4.8, Withdrawn): pure theory with no experiments. The current paper has weaker theory (applying known techniques rather than developing new concepts) but at least has experiments. Comparable in overall quality, though the current paper's theory is more applied.

These comparisons place the paper at approximately 5.0, comparable to the ECBMs paper (5.6) and the Unifying paper (5.25) when accounting for cleaner theory but weaker experiments.

**Final score: 5.0.** The paper's theoretical contribution is genuine and clean—the first explicit mathematical bridge between activation steering and influence functions. However, the experimental validation is insufficient to support the broad claims made. The data-attribution pipeline (the most practically significant claimed contribution) is not demonstrated at all. The perplexity numbers are implausible. The unexplained slope of 1.5 in the central equivalence experiment undermines confidence. A major expansion of empirical work is needed before this paper meets the acceptance bar for a top conference.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>