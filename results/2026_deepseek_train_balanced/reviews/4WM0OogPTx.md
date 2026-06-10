Here is my final synthesized review.

---

## Summary

This paper proposes Conservative Density Estimation (CDE), an offline RL method that applies explicit pessimism in the stationary-distribution space rather than in Q-value space. CDE combines ideas from DICE-based methods (marginal importance sampling with f-divergence regularization) and conservative Q-learning by introducing a constraint d^π(s,a) ≤ εμ(s,a) on the occupancy density of out-of-distribution state-actions. The method obtains closed-form solutions for the importance ratio w* and the Lagrange multiplier λ*, and provides theoretical bounds on the concentrability coefficient and performance gap. Experiments on D4RL sparse-reward and scarce-data settings show CDE achieving competitive or best results on most tasks.

## Strengths

1. **Novel formulation of conservatism in stationary-distribution space.** Rather than penalizing Q-values of unseen actions (CQL) or relying solely on divergence regularization (OptiDICE), CDE directly imposes the constraint d^π(s,a) ≤ εμ(s,a) on the occupancy density (Eq. 6–7). This is a genuinely different locus for conservatism, and the paper provides both the constrained optimization formulation and a practical algorithm.

2. **Closed-form optimal λ* with principled conservatism adjustment.** Proposition 3 gives λ*(s,a) = max{0, A*(s,a) − αf'(ε̃)} for OOD state-actions (Eq. 11), providing a theoretically grounded mechanism for determining the degree of conservatism — in contrast to CQL's heuristic penalty coefficient tuning. The heatmap study (Fig. 2) visually supports that this avoids both overly conservative "trapped" behavior and overconfident failures.

3. **Theoretical bound on the concentrability coefficient as an output of optimization.** Proposition 4 and Theorem 5 prove that w*(s,a) ≤ ε̃ for OOD state-actions and extend this to function approximation with a finite-sample bound. Prior works typically assume the concentrability coefficient is bounded as an input condition; CDE instead guarantees it from the optimization, which is a stronger theoretical property.

4. **Performance gap theorem that cleanly separates failure modes.** Theorem 6 bounds V*(ρ₀) − V^π(ρ₀) ≤ (2R_max/(1−γ))·TV(d^D(s)∥d*(s)) + e_N, separating the influence of state-distribution mismatch from dataset size. This provides formal support for the paper's claim that CDE addresses both sparse rewards and scarce data.

5. **Strong results on maze2d-large and scarce-data settings.** CDE achieves 210.0±13.5 on maze2d-large vs. the next-best OptiDICE at 155.7±33.4 (Table 1). The scarce-data experiments (Fig. 1) show CDE maintaining performance at 1% trajectory subsampling while prior methods collapse, directly supporting the claim that the mixed proposal distribution addresses support mismatch.

## Weaknesses

### Fatal

None.

### Major

- **Baseline scores borrowed from original papers under inconsistent evaluation protocols.** The paper states (line 234): "We adopt the scores of baselines if they are reported in original paper." CDE's own scores are produced under a specific protocol (5 seeds, last-5-evaluation averaging, 20 trajectories per eval). Baseline scores from original papers were produced under different protocols — different numbers of seeds, evaluation frequencies, trajectory counts, and potentially different environment versions. This means observed margins (e.g., CDE's 72.1±15.8 vs. BCQ's 68.9 on pen-human, well within one standard deviation) could be artifacts of protocol mismatch rather than genuine algorithmic differences. The headline empirical claims of state-of-the-art performance are weakened by this comparison protocol. The authors should re-run all baselines under identical conditions. (This is the single most impactful improvement.)

### Minor

- **Textual overclaiming relative to actual results.** The paper claims CDE "consistently matches or surpasses" baselines, but across ~17 tasks CDE is clearly behind on at least 4 (hammer-human: CQL 4.4 vs. CDE 1.9; door-human: CQL 9.9 vs. CDE 7.7; pen-expert: BCQ 114.9 vs. CDE 105.0; halfcheetah-medium: CQL 97.6±4.1 vs. CDE 82.0±8.6). CDE is best or tied on the remaining tasks, which is a solid but mixed result — not "consistently matches or surpasses." The bolding criterion (≥0.99×highest) is reasonable for near-ties but the textual characterization should be more measured.

- **Sparse-reward conversion of MuJoCo is non-standard and unvalidated.** The paper converts dense-reward MuJoCo to sparse by thresholding at the 75th percentile of trajectory returns and assigning reward 1 to the top 25% and 0 to the rest (lines 229-230). This creates a fundamentally different optimization landscape than the original tasks. Whether this conversion favors CDE's stationary-distribution optimization over value-function-based methods is unclear but plausible. Standard D4RL MuJoCo tasks are dense-reward; the paper neither validates that this conversion produces meaningful goal-reaching problems nor clarifies whether baselines on these converted tasks were re-run or their published dense-reward scores were used.

- **Key hyperparameters not disclosed.** Values of α (f-divergence coefficient), ε (density constraint threshold), Δa (OOD radius), n (number of OOD samples per state), along with network architectures (layer sizes, number of layers), learning rates, and optimizers are not reported. The paper states "we keep hyperparameters the same for experiments in the same domain" but never states what those hyperparameters are. This significantly hinders reproducibility.

- **No ablation isolating the two core components.** The paper does not ablate (a) the OOD density constraint alone without the mixed proposal, nor (b) the mixed proposal alone without the OOD constraint. Without this, it is unclear which mechanism drives the gains over OptiDICE, and the paper's central claim about the source of improvement is not empirically supported.

- **Theoretical bounds have practical limitations not discussed.** Theorem 1's finite-sample bound scales with (Δa^d + (M^d/N)log(1/δ))^{1/d}, which grows with action dimension d — a curse-of-dimensionality issue that is not discussed. Theorem 2's convergence rate of N^{−1/(4+h)} is considerably slower than the standard parametric rate N^{−1/2} but not commented on. Both observations limit the practical significance of the bounds.

- **Scarce-data results presented only qualitatively.** The scarce-data experiments (Section 5.2) describe results with reference to a figure and qualitative text but report no numerical scores. Without quantitative results, these claims cannot be independently evaluated.

### Trivial

None.

## Nice-to-Haves

- Report standard dense-reward D4RL MuJoCo results to contextualize CDE's trade-offs when data coverage is good.
- Include explicit statistical testing (confidence intervals or significance tests) for comparisons with overlapping standard deviations.
- Report computational cost (wall-clock time, training iterations) relative to baselines.
- Perform sensitivity analysis for ε and α with quantitative scores rather than heatmaps alone.
- Include a hyperparameter table with all values used in each domain.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Automatic" bound phrasing (harsh critic, Section-by-Section):** The critic says the bound is "imposed, not 'automatic.'" This is a semantic criticism of the phrasing "automatically bounds" (line 23). The bound does follow from the method's design, and "automatic" is not misleading enough to warrant inclusion. REMOVED as trivial phrasing nitpick.

- **Missing related work on stationary-distribution methods (harsh critic):** The critic notes the paper "does not discuss prior work on stationary-distribution-based offline RL methods that also address the support mismatch issue." Rule: DO NOT mention missing related works, as you do not have external sources. REMOVED.

- **Proposition 3 being "a direct consequence of the constraint" (harsh critic):** The critic says this is "not a surprising finding." This is a commentary on a proposition's nature, not a weakness; all propositions are consequences of their premises. REMOVED as not a weakness.

- **Concern about Δa sensitivity not being analyzed (harsh critic):** The critic says "the paper does not analyze sensitivity to Δa" — this is true but is already covered by the general missing-hyperparameter concern and the broader lack-of-ablation weakness. REMOVED as duplicate.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the review synthesis is the conceptual tension in CDE's approach: the method introduces an explicit density constraint on OOD state-actions (d^π ≤ εμ), yet the effectiveness of this constraint depends on μ's coverage, which is defined by a hard threshold Δa around observed actions. This creates a design dilemma — too small a Δa leaves OOD regions unconstrained, too large a Δa makes the bound vacuous. The paper acknowledges this only briefly ("our method is also compatible with other OOD sampling distribution") without exploring the implications, and the absence of sensitivity analysis on Δa means the robustness of the core mechanism is untested.

## Suggestions

1. Re-run all baselines under the identical evaluation protocol used for CDE — this is the single highest-leverage improvement.
2. Add an ablation study that isolates the OOD density constraint from the mixed proposal distribution.
3. Report numerical values for all key hyperparameters (α, ε, Δa, n), network architectures, and learning rates.
4. Tone down the "consistently matches or surpasses" claim to reflect the 4/17 tasks where CDE is clearly behind.
5. Clarify whether baselines on sparse-MuJoCo were re-run by the authors or borrowed from dense-reward original papers.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>