Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

This paper proposes that the vulnerability of adversarial training in certain regions can be explained by the classifier's "perceived curvature" of the data manifold — a model's distorted ratio between semantic and pixel distances. It introduces a sensitivity measure \(s_y(p_i)\) as a proxy for this perceived curvature, provides theoretical and qualitative evidence (diffusion model clones, MDS visualizations), and modifies the Wang et al. (2023) pipeline to focus stronger PGD-40 attacks on the few least-robust training points, yielding small test-time robustness improvements.

## Strengths

- **Novel conceptual framework linking data robustness to perceived curvature.** The paper identifies a genuinely underappreciated phenomenon: standard margin-based reasoning cannot explain why adversarial training underperforms in non-robust regions, since the minimal \(l_\infty\) distance between non-robust CIFAR-10 images (~0.2118) is more than six times the perturbation radius (~0.0314). The curvature-perception intuition — that models learn spurious pixel-label correlations in high-curvature regions — is creative and worth exploring.

- **Diffusion model evidence is qualitatively consistent with the curvature story.** Clones of the least robust images exhibit larger semantic changes per pixel change than clones of the most robust images (Table 1, Fig. 3). The pattern (smaller pixel distances but larger semantic variation for non-robust clones) matches what the curvature hypothesis predicts, and this generative experiment is a novel way to probe the data manifold.

- **MDS visualizations and Theorem 1 support local consistency of sensitivity.** Figures 2c–2d show that label-agnostic MDS clusters points by sensitivity values, corroborating the Lipschitz-continuity result of Theorem 1. This is a clean sanity check that sensitivity is a meaningful local property.

- **Consistent improvements across settings and norms.** The core training modification (stronger PGD-40 on the 1024 least-robust points) yields small but directionally consistent robustness gains on CIFAR-10 (\(l_\infty\), \(l_2\)) and CIFAR-100 (\(l_\infty\)), including with new random seeds (Table 3) and extended settings (Table 4). The improvement on unseen test data exceeds the local improvement on the focused set, suggesting genuine robust generalization beyond memorization.

## Weaknesses

### Major

- **The theoretical derivation linking sensitivity to perceived curvature is not rigorous, despite the paper's "new and rigorous explanation" claim.** The chain of reasoning has two weak links. First, the assumption that a model perceives \(\tilde{d}_{\text{perc}}(y,p_i,p_j)=\delta(y)\) (a constant) for all differently-labeled pairs is not adequately justified: the cited evidence (Zhang et al., 2016; Frankle et al., 2020; Maennel et al., 2020) shows that networks can fit random labels, but this does **not** imply that perceived manifold distance collapses to a constant across all cross-class pairs. Second, the ordering argument linking \(\Delta_4=\{(\lambda-d)/d^3\}\) to \(\Delta_1=\{d^{-1}\}\) implicitly assumes \(d \leq \delta(y)\) for the curvature expression to have the same monotonicity as the other sets — the paper does not state or justify this condition, and the derivation is sloppy at this critical juncture. The paper would benefit from either a proper mathematical connection or an honest framing as intuition rather than a "rigorous" explanation.

- **The "glitch" in the baseline pipeline is never explained, undermining the core comparison.** The paper mentions uncovering a glitch in Wang et al.'s (2023) code that was "used to include stronger adversarial noise," then claims it was later circumvented. But the nature of the glitch, its impact on results, and how circumvention was achieved are never described. Without this information, readers cannot assess whether the baseline numbers are truly comparable or whether the improvements stem from fixing a bug rather than from the curvature-inspired method.

- **No direct empirical test of the curvature hypothesis.** The paper's central conceptual claim is that *perceived curvature* explains adversarial training's weakness in non-robust regions. Yet no experiment directly measures curvature in a trained network's feature space, nor does any experiment show that the ordering of empirical curvatures matches the ordering of sensitivity values. The diffusion model experiment (Table 1, Fig. 3) probes a diffusion model's generation behavior, not the classifier's internal representation — it is indirect evidence at best.

### Minor

- **The empirical improvements are small (0.1–0.3 pp) and statistical significance is not established.** The paper reports only 1–2 random seeds per configuration with no standard deviations or confidence intervals. Given run-to-run variance in large-scale adversarial training (data shuffling, random crops, non-determinism), improvements of this magnitude could fall within noise. The claim that the gain is "equivalent to 800 extra epochs" relies on a single observation from Wang et al. (2023) rather than a properly measured comparison.

- **No ablation isolates the sensitivity-based selection from the learning-rate schedule changes.** Rows 8–12 of Table 2 combine the least-robust focus *with* modified LR schedules. There is no run testing the LR schedule alone (without the sensitivity-based focus), so the marginal contribution of the curvature-informed selection cannot be quantified.

- **No comparison against alternative selection heuristics.** The paper never benchmarks its sensitivity-based selection against other plausible methods — e.g., random up-weighting with the same attack budget, points closest to the decision boundary, or highest-loss examples. Without these controls, it is unclear whether the small improvements are due to the curvature rationale or simply to the fact that *any* stronger attack on a *any* small set of points yields marginal gains.

- **Sensitivity computation details are underspecified.** Equation (1) requires O(\(n^2\)) pairwise computations (~2.5B for 50k images). The paper gives no details on how this was computed efficiently (GPU batching, KD-trees, approximations) and does not consistently specify whether the sensitivity values guiding training were computed with the \(l_2\) or \(l_\infty\) norm. This hurts reproducibility.

- **The base architecture used for all adversarial training experiments is not explicitly stated.** The paper follows Wang et al. (2023) but never names the model (presumably WideResNet-28-10). This should be stated explicitly.

### Trivial

- The claim that "the minimal \(l_\infty\) distance between two non-robust CIFAR-10 images is ≈0.2118" is presented without derivation or citation. While the authors likely computed this from their data, the value should be justified.
- The sentence "All sensitivity values were calculated according to the formula in Equation (1) w.r.t." is syntactically incomplete (likely a parser artifact from "w.r.t. the \(l_2\)/\(l_\infty\) norm").

## Nice-to-Haves

- A controlled experiment measuring curvature in the feature space of a trained classifier (e.g., via local PCA or geodesic distances in the penultimate layer) to directly validate the curvature–sensitivity link would substantially strengthen the paper's core contribution.
- Comparisons to related hard-example mining methods (Zhang et al., 2020b; Xu et al., 2023; Zeng et al., 2021) under matched computational budgets would help isolate what the sensitivity-based criterion adds.
- If O(\(n^2\)) sensitivity computation is a bottleneck, a brief note on approximations or runtime would aid reproducibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The theoretical contribution of Theorem 1 is minor/unnecessary."** Theorem 1 provides a formal Lipschitz continuity result that supports the claim that sensitivity is a local property, which is used to justify the locality of the curvature connection. This is a reasonable supporting result, not a weakness.
- **"The MDS figures are not convincing."** The Strength Finder's claim about MDS clustering is reasonable; the critic's dismissal of this as "a minor point" undervalues what is actually a clean empirical validation of the local consistency claim.
- **"The claim about 0.2118 being unsupported."** This is a trivial presentation issue (the number should come with a brief justification), not a structural weakness. Kept in Trivial above.
- **Strength Finder item about "learning rate adjustments exploit curvature dynamics."** This strength overstates the connection — the LR adjustments (versions a–e) are heuristic modifications based on observed PGD-40 robustness behavior, not derived from the curvature theory. Moving to Removed Points.

## Novel Insights

The reviews surface a central tension that the paper does not fully resolve: the conceptual framework (perceived curvature) is qualitatively appealing and partially supported by indirect evidence (diffusion clones, margin counterexample), but the paper claims "rigorous" status for what is still a speculative theoretical connection. The most interesting empirical finding — that focusing on 0.005% of training points yields measurable generalization improvements — is obscured by the lack of ablation against other selection methods. A deeper insight from the reviews is that the paper's value may lie more in the *phenomenon* it identifies (the inadequacy of margin-only explanations and the promise of sensitivity-aware training focus) than in the particular theoretical apparatus used to explain it.

## Suggestions

1. **Clarify the theory's status.** Either tighten the derivation (explicitly state the condition \(d \leq \delta(y)\) needed for the ordering argument; justify or remove the constant-\(\delta(y)\) assumption) or reframe the curvature link as a motivating intuition rather than a "rigorous" explanation.
2. **Describe the glitch.** Explain what the Wang et al. (2023) pipeline glitch was, how it affected results, and how the circumvention works. Provide a baseline run that includes the same code fix without the sensitivity focus.
3. **Add ablations.** Run the PGD-40 focus on random sets of the same size, on the most robust set, and on sets selected by loss value or proximity to the decision boundary.
4. **Report variance.** Add multiple-seed runs (3–5) with means and standard deviations for the main robustness results (Tables 2–4).
5. **Describe sensitivity computation.** Provide pseudocode or a brief note on computational strategy (e.g., GPU-parallel pairwise distances for the 50k-image case) and state which norm was used for the training selection.

## Score and Decision

The paper introduces a genuinely novel perspective on adversarial robustness and provides several pieces of suggestive evidence (margin counterexample, diffusion clones, consistent small improvements). However, the theoretical derivation is not rigorous as claimed, the "glitch" in the baseline code is never explained (undermining the central comparison), and the empirical evidence for the core curvature hypothesis is indirect and statistically unvalidated. The practical improvements are small and not cleanly attributed to the curvature-inspired component.

While the ideas are promising and worth disseminating, the paper in its current form does not deliver on its stated contributions. The theoretical explanation is not rigorous, and the empirical claims are not established with sufficient rigor.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>