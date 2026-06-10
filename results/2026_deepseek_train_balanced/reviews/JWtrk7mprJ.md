## Summary

This paper proposes residual deep Gaussian processes on Riemannian manifolds, a novel model class that constructs manifold-to-manifold hidden layers by composing Gaussian vector fields (GVFs) with the exponential map. The architecture generalizes Euclidean deep GPs to non-Euclidean domains, enabling expressive, uncertainty-aware models for functions on manifolds. The authors demonstrate improvements over shallow geometry-aware GPs on synthetic benchmarks, a real-world wind velocity interpolation task (where they achieve state-of-the-art results), and a Bayesian optimization setting, while also adapting interdomain inducing variables for computational efficiency.

## Strengths

- **Principled, elegant construction of manifold-to-manifold GP layers.** The formulation $f^l(x) = \exp_x(g^l(x))$ (Eq. 248) reduces the challenging problem of defining GP outputs on manifolds to modelling a Gaussian vector field on each tangent space. The connection to residual networks (He et al., 2016) is clearly motivated, and the relationship to the Euclidean deep GP architecture is well-explained. This is a genuine methodological contribution.

- **State-of-the-art results on real-world wind interpolation with interpretable uncertainty calibration.** The wind velocity experiment (Section 4.3) is the strongest evidence for the paper's claims. Residual deep GPs improve upon shallow Hodge GVFs (the previous state-of-the-art, Robert-Nicoud et al., 2024) in both NLPD and MSE across multiple altitudes. Critically, the deep model produces uncertainty estimates that follow physically meaningful patterns (monsoon boundaries, continental edges) — a qualitative advantage that is fundamentally impossible for shallow GVFs, whose posterior covariance depends only on observation locations (lines 565–568).

- **Practical adaptation of interdomain inducing variables to manifold-valued GVFs.** The extension of interdomain inducing variables to the GVF setting (Section 3.3, lines 387–422) yields diagonal covariance matrices that are trivial to invert. The synthetic experiments confirm this consistently improves over standard inducing locations (line 471), and the speed comparison (Figure 7) shows benefits that compound with depth. This is a practical contribution with clear utility.

- **Clean synthetic evidence that depth helps when data is sufficient.** The synthetic experiments (Section 4.1) show that residual deep GPs recover the shallow solution under data sparsity and outperform shallow models as data becomes abundant (lines 468–472). This directly supports the robustness claim in the abstract.

## Weaknesses

### Major

- **The Bayesian optimization experiment does not isolate the effect of depth from the effect of model refitting.** The protocol (lines 506–509) performs 180 iterations with a shallow GP, then switches to a deep GP for 20 more iterations. There is no control arm that continues with the shallow GP for all 200 iterations. Thus, the observed improvement (line 514: "significantly improves performance") could partly reflect the benefit of retraining/refitting the model on 180 iterations' worth of accumulated data, rather than the deep architecture per se. The Ackley control shows the improvement is specific to the irregular function, which partially mitigates this concern, but a proper "shallow-only for 200 iterations" baseline is needed to fully disentangle the effects. This does not invalidate the paper's core contribution, but it weakens the BO experiment as evidence.

### Minor

- **The "reverting to shallow models" claim is asserted at the mechanistic level but demonstrated only at the performance level.** The abstract claims models "revert to shallow models when additional complexity is unneeded" (line 8). The synthetic results (line 469) show deeper models match shallow performance under data sparsity — but this only demonstrates that overall predictive performance is not worse. It does not show that individual layers actually approach the identity (e.g., via analysis of learned GVF norms, effective layer depths, or KL divergence per layer). Given this is a headline claim in the abstract, the evidence is thinner than the claim warrants. The robustness observation is valid; the "reverting mechanism" is unsubstantiated.

- **Limited scope of synthetic evaluation.** The synthetic experiments use only one target function (a custom function with singularities on $\mathbb{S}_2$) and one manifold (the 2-sphere). The paper's thesis turns on function irregularity, but this dimension is not parameterized or systematically varied. Broader evaluation (varying irregularity, testing on at least one additional manifold) would strengthen the contribution.

- **The BO experiment uses coordinate-frame GVFs without explanation.** The synthetic experiments identify Hodge GVFs + interdomain variables as the best configuration, but the BO experiment uses coordinate-frame GVFs (line 507). The paper does not explain this choice — whether it is due to Hodge GVFs being harder to train in the BO loop, $\mathbb{S}_3$ not being supported, or another reason. This makes it harder to assess whether better GVF choices could further improve the BO results.

- **The Euclidean acceleration experiment is framed too positively in the abstract and conclusion.** The abstract (line 10) frames this as showing "potential for speeding up inference for non-manifold data." The body reports that predictive quality (NLPD and MSE) is worse than Euclidean deep GPs (lines 597–602). The conclusion (line 615) uses similarly positive language ("superior in terms of inference time") without immediately qualifying the predictive trade-off. The paper's honesty in the discussion section is appreciated, but the abstract/conclusion framing should be adjusted to avoid misleading a casual reader.

### Trivial

- **The description of the Salimbeni & Dieng (2017) architecture imposes a residual interpretation that was not originally present.** The paper writes "each layer $f^l: \R^d \to \R^d$ is of the form $f^l(x) = x + g^l(x)$ where $g^l$ is a zero-mean GP" (lines 237–242) as a description of the Salimbeni & Dieng architecture. The original architecture uses zero-mean vector-valued GPs without an explicit residual decomposition. The residual structure is a retrospective framing that enables the manifold generalization; the paper should be clearer that this is an interpretation or modification, not a literal description.

## Nice-to-Haves

- A runtime/computational cost analysis (wall-clock time per layer, convergence behavior) for the main manifold experiments would help practitioners gauge practical feasibility.
- The synthetic experiments would be strengthened by systematically varying the irregularity/complexity of the target function to directly probe the conditions under which depth helps.
- Per-layer analysis of learned GVF norms or effective KL divergences would substantiate the "reverting" claim at the mechanism level.

## Removed Points

These points were considered but removed for the reasons stated:

- **Pathwise conditioning not fully described in main text:** Removed per policy — deferring implementation details to an appendix is standard practice for conference papers. The main text provides a sufficient sketch at lines 424–431.
- **Lack of systematic tuning for Euclidean acceleration experiment:** Removed because the paper openly acknowledges this limitation (lines 599–602) and appropriately scopes it as future work.
- **The Salimbeni architecture description as "historically inaccurate":** Demoted to Trivial (from a more severe framing). The residual decomposition is a valid reinterpretation; the paper's core contribution does not depend on this framing being historically literal.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **BO experiment:** Add a control arm that continues with the shallow GP for all 200 iterations, or refit the shallow GP at iteration 180 on the same accumulated data for a fair comparison. This would cleanly isolate the effect of depth.
2. **"Reverting" claim:** Either qualify the abstract (e.g., "performance reverts to that of shallow models") or add a simple analysis of per-layer GVF norms to support the mechanistic claim.
3. **Framing:** Adjust the abstract and conclusion to transparently state the predictive quality trade-off in the Euclidean acceleration experiment.
4. **BO choices:** Add a brief explanation for why coordinate-frame GVFs were chosen instead of Hodge GVFs for the BO experiment.
5. **Synthetic evaluation:** Broaden to vary function irregularity systematically and consider at least one additional manifold.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>