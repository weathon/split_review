Now I have enough information. Let me synthesize the final review.

## Summary

The paper proposes GSR (Group-robust Sample Reweighting), a two-stage method that uses influence functions with last-layer retraining (LLR) to iteratively optimize sample weights for improving worst-group accuracy under subpopulation shifts. The key technical contribution is using implicit differentiation (via the influence function with the Hessian inverse) to compute exact gradients for sample weight updates within the LLR framework, avoiding the one-step truncated backpropagation approximation used by prior work (MAPLE). The method is evaluated on four standard benchmarks (Waterbirds, CelebA, MultiNLI, CivilComments), achieving competitive results with the state-of-the-art method DFR that uses the same amount of group labels.

## Strengths

- **Clean technical integration of influence functions with LLR**: The paper identifies that LLR yields a strongly convex inner objective, making implicit differentiation via the influence function tractable and exact (Equation 6). This is a legitimate engineering advantage over MAPLE's one-step truncated backpropagation, and the GSR-HF ablation (which removes the Hessian) consistently underperforms the full GSR across all datasets in Table 1, empirically validating the Hessian's importance.

- **Competitive empirical results across multiple benchmarks**: GSR achieves the best reported worst-group accuracy on MultiNLI and CivilComments among methods using the same amount of group labels, and is competitive with DFR on Waterbirds and CelebA. The paper reports results over 5 random seeds with standard deviations.

- **Interesting label-noise analysis**: The experiment in Section 5.3 shows that GSR degrades minimally even with 40% class-label corruption in the held-out set, and the weight distribution analysis (Figures 4b-4c) reveals that the method automatically assigns near-zero weights to corrupted minority samples. This demonstrates a practically useful property and is well-motivated.

- **Interpretable learned weights**: The analysis in Figures 1-3 shows that the learned sample weights align with intuitive expectations (minority groups upweighted, majority spuriously-correlated groups downweighted), and GSR can even correct misannotated group labels by assigning high weights to minority samples despite wrong annotations.

## Weaknesses

### Fatal
None.

### Major

- **The central empirical claim is overstated**: The abstract and introduction state that GSR "outperforms the previous state-of-the-art" and achieves "an average improvement of 1.0%" over DFR. However, the paper's own Section 5.1 describes results on Waterbirds and CelebA as "close-to-SoTA" rather than surpassing it. Since the table data is presented as an image and cannot be verified from the extracted text, the precise arithmetic cannot be confirmed, but the paper's own hedging language indicates that GSR does not clearly dominate DFR across all datasets. The claim of "outperforming" is too strong for results that are mixed — better on two datasets, comparable or slightly worse on two others. The paper would benefit from a more precise framing that acknowledges GSR is *competitive with* DFR rather than superior to it.

- **The improvement over DFR does not justify the added complexity**: DFR (Kirichenko et al., 2022) already performs last-layer retraining on a group-balanced validation set, achieving strong results with minimal complexity. GSR adds bilevel optimization, Hessian computation, iterative projected gradient descent on sample weights, and multiple outer-loop hyperparameters (T, β, τ, α). The gains are marginal at best (positive on two datasets, negative on two) and there is no evidence that this complexity provides meaningful benefit over simple group-balanced subsampling. The paper does not demonstrate a clear advantage that would motivate adopting GSR over DFR in practice.

### Minor

- **The "theoretically sound" claim is overbroad**: The paper states GSR is "theoretically sound" in the abstract, deriving the exact gradient for the influence function under strong convexity. This gradient computation is indeed exact for infinitesimal weight perturbations of a single point. However, the algorithm performs iterative, potentially large reweighting of many points simultaneously using projected gradient descent with these influence-based gradients as descent directions. The paper does not analyze whether this iterative procedure converges to a stationary point of the bilevel minimax objective, or discuss the gap between infinitesimal theoretical guarantees and the actual algorithmic operation. The method is well-motivated and technically clean, but the "theoretically sound" label should be qualified.

- **Missing hyperparameter reporting**: The paper states that a randomized hyperparameter search was performed but does not report the searched ranges or selected values for key hyperparameters (outer learning rate β, scaling temperature τ, L2 regularization strength λ, held-out fraction α). This makes exact reproducibility difficult and raises the question of whether the same search was applied uniformly to baselines.

- **Sensitivity to the held-out fraction α is not studied**: The algorithm reserves α fraction of training data (stated as 10% example) for the reweighting stage — data that is never seen during representation learning. This is a critical design parameter: larger α means more data for reweighting but less for representation learning. No ablation studies the trade-off.

- **MAPLE comparison design is not fully controlled**: The paper compares GSR (which uses LLR) against MAPLE (which trains the full network). The GSR-HF ablation correctly isolates the Hessian effect *within* the LLR framework, but the direct MAPLE comparison conflates two differences (LLR vs. full network, Hessian vs. no Hessian). While this does not invalidate the paper's main contributions, the framing that GSR is "better than MAPLE" should be more carefully scoped.

### Trivial
- None.

## Nice-to-Haves
- A convergence analysis or empirical convergence plot of the iterative weight optimization (worst-group accuracy over outer loop steps) would strengthen the method's credibility.
- An ablation of the scaling temperature τ in the adaptive aggregation weights would improve understanding.
- Comparison with Group DRO + LLR (using Group DRO for representation learning, then LLR retraining) would help isolate the value of sample reweighting versus better representations.
- The scaling temperature τ and its effect on optimization dynamics could be discussed more or ablated.

## Removed Points

These points were removed from consideration per the review guidelines:

1. **Criticism that the label noise experiment is "a favorable scenario" because the target set remains clean** — This is not a weakness; the paper's narrative is specifically about investing label quality in the target set. Testing target-set noise would address a different research question outside the paper's stated scope.

2. **Criticism that "no statistical significance tests are performed"** — Single-run evaluation with standard deviations over 5 seeds is the standard practice for these benchmarks in the group robustness literature. Requesting formal significance tests is a methodological standard not commonly applied in this field.

3. **Criticism that the overparameterization issue is "not empirically shown to be solved"** — The paper discusses this in Section 4.1, explaining that LLR with L2 regularization creates strong convexity and that "sufficient regularization is usually needed for the reweighting scheme to be practically meaningful," citing prior work. The empirical results serve as the practical validation.

4. **Criticism that "Figure 1 and 2 show expected behavior" and "is not surprising"** — Demonstrating that the mechanism works as intended is a standard and useful validation; finding expected results is not a weakness.

5. **Strength Finder's claims about "state-of-the-art" performance** on Waterbirds (91.0%) and CelebA (90.8%) — These specific numbers cannot be verified from the extracted text (table is an image). The strength is retained but framed conservatively as "competitive."

## Novel Insights

The most interesting observation emerging from this review is that the paper's primary methodological contribution — using influence functions with the Hessian for sample reweighting in LLR — is technically sound and well-motivated, yet the empirical results are only marginally different from the much simpler DFR baseline. This suggests that either (a) the sample-level reweighting does provide a modest but real benefit that happens to be dataset-dependent, or (b) once you fix the representations via ERM and restrict optimization to the last layer, most reasonable reweighting schemes that emphasize minority-group-like samples converge to similar solutions regardless of gradient sophistication. The GSR-HF ablation shows the Hessian helps, but the gap to the much simpler DFR (which just balances groups via subsampling) remains small. This raises an underexplored question: is the marginal gain from fine-grained sample reweighting worth the complexity, or is group-level balancing already operating near the ceiling of what LLR can achieve under fixed representations?

## Suggestions

1. **Reframe the contribution honestly**: Present GSR as a method that is *competitive with* DFR (not superior to it), emphasizing the technical novelty of the exact Hessian-based gradient and the label-noise robustness as the main contributions rather than raw accuracy gains.
2. **Report hyperparameter search ranges and selected values** for reproducibility.
3. **Add an ablation on the held-out fraction α** (e.g., 5%, 10%, 20%, 30%) to study the trade-off between representation learning data and reweighting data.
4. **Add an empirical convergence plot** showing worst-group accuracy on the target set over outer loop iterations to demonstrate that the weight updates actually improve the objective.
5. **Qualify the "theoretically sound" claim** to clarify that the gradient computation is exact but the iterative optimization procedure is not provably convergent.

## Score and Decision

This paper proposes a technically clean combination of influence functions and last-layer retraining for sample reweighting to improve group robustness. The method is well-motivated and the ablation confirming the Hessian's importance is solid. However, the core empirical results are mixed relative to the much simpler DFR baseline, and the paper's central claim of "outperforming" the state-of-the-art is not fully supported by the evidence presented. The added complexity is not convincingly justified by the empirical gains. The paper would be strengthened by more honest framing and additional ablations. I ultimately lean toward acceptance because the methodological contribution (exact Hessian-based gradients for sample reweighting in the LLR setting) is novel and the label-noise analysis provides practical insight, but the paper needs revision on framing and completeness.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>