Now I have all the evidence I need. Let me construct the final consolidated review.

## Final Consolidated Review

## Summary

This paper presents Scaff-PD, an algorithm for distributionally robust federated learning that combines accelerated primal-dual (APD) updates with SCAFFOLD-style control variates to correct client drift. The algorithm targets the min-max DRO formulation and achieves, for the first time in federated DRO, accelerated O(1/T²) convergence in the strongly convex–concave setting and linear convergence in the strongly convex–strongly concave setting. Experiments on CIFAR-100 and TinyImageNet show improved worst-20% accuracy compared to baselines like DRFA, AFL, and SCAFFOLD, particularly under high data heterogeneity.

## Strengths

1. **First accelerated and linear convergence rates for federated DRO.** The paper proves O(1/T²) (Theorem 1) and linear (Theorem 2) rates for Scaff-PD, matching centralized accelerated primal-dual methods and significantly improving over prior federated DRO algorithms (which achieved only O(1/R) or O(1/√R)). This is clearly stated and is the paper's central theoretical contribution.

2. **Novel algorithmic integration.** The combination of extrapolated dual updates (Eq. 7) with bias-corrected local steps (Algorithm 2) is a clean and well-motivated design. The control variates correct client drift while the extrapolation provides acceleration — neither alone suffices for the federated DRO setting. The synthetic experiments (Figure 1) confirm linear convergence while DRFA converges much more slowly, directly validating the theory.

3. **Superior empirical performance under high heterogeneity.** On CIFAR-100 with α=0.01, Scaff-PD achieves 29.30% worst-20% accuracy vs. 26.77% for DRFA and 18.04% for AFL (Table 1). Similar improvements hold on TinyImageNet. These gains are largest precisely where heterogeneity is most severe, supporting the method's motivation.

4. **Unified framework for existing fair FL objectives.** The paper shows that the min-max formulation (Eq. 1) with appropriate choices of ψ and Λ recovers AFL, q-FFL, CVaR, and Nash bargaining solutions. This provides generality and practical relevance beyond a single objective.

5. **Optimal stochastic sample complexity.** Corollary 1 shows O(1/T) convergence with stochastic gradients, improving over the O(1/√T) rate of prior federated DRO methods and matching the sample complexity of the average objective. This is a genuine advance.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Exact loss computation for the dual update is not discussed.** Algorithm 1 computes L_i^r = f_i(x^r) — the full local loss — each round for the dual update, while the primal update uses stochastic gradients. This asymmetry is standard design (scalar loss is cheap compared to vector gradients; in cross-silo settings with moderate dataset sizes, computing the full loss is entirely feasible). However, the paper never acknowledges this choice or justifies it. A brief discussion of why exact loss computation is practical in the cross-silo setting (the paper's stated focus) would preempt the concern and clarify the intended deployment scope.

2. **The theoretical scope (strongly convex f_i) could be signaled more prominently.** The contribution paragraph (line 44) clearly states the theory holds "when f_i are strongly convex," and the experiments use a convex linear classifier on pre-trained features via Train-Convexify-Train. However, the abstract and title do not qualify the convexity assumption. While this level of detail is common in conference papers, adding a brief qualification to the abstract would prevent misreading by practitioners who may apply the method directly to non-convex deep networks without the convexification step.

3. **The Bregman divergence D(·,·) is never specified.** The algorithm (Eq. on lines 159, 174) and analysis use a general Bregman divergence, but the paper never states which divergence is used in practice (presumably squared Euclidean distance) or whether the theory applies to general Bregman divergences. This makes the algorithmic description harder to compare with baseline methods like SCAFFOLD that use explicit gradient descent, and leaves readers wondering what the actual update is.

4. **The "trade-off between average vs. worst-20% vs. best-20%" claim is asserted without a supporting figure or table.** Lines 449–451 state: "Without sacrificing much on average accuracy and best-20% accuracy, our algorithm largely improves the worst-20% accuracy." While Table 1 provides average and worst-20% data, the best-20% numbers are not reported, and no figure visualizes the three-way trade-off. This claim should be backed with evidence.

### Trivial

1. **Theorem constants C₁ and C₂ are not quantified** in terms of condition numbers or problem parameters. Making the dependence on L_{xx}, L_{λx}, μ_x, μ_λ explicit would make the bounds more informative.
2. **No per-round communication cost comparison** in bits. The paper compares algorithms by communication rounds, which is standard, but a brief note confirming that the extra scalar loss value adds negligible overhead would strengthen the "communication efficient" claim.

## Nice-to-Haves

- An ablation on the number of local steps J and its effect on communication rounds vs. per-round cost would give practitioners concrete guidance.
- A comparison with FedProx or other heterogeneity-tolerant baselines would strengthen the empirical evaluation, though the chosen baselines (FedAvg, SCAFFOLD, q-FFL, AFL, DRFA) are already reasonable.

## Removed Points

- **"Missing trade-off figure" as a missing/lost figure** — The harsh critic claimed this appears to be a missing figure lost during extraction. The paper contains a textual description of the trade-off (lines 449–451) without referencing a figure number. There is no evidence a figure was removed by the parser; the claim is speculative. The underlying issue (unsupported claim) is kept as Minor #4 above.
- **"No comparison with FedProx"** — Keeping this would amount to demanding additional baselines that the paper's already adequate set does not include. Moved here as scope-creep.
- **"Paper never states upfront that results are limited to strongly convex"** — The contribution paragraph (line 44) explicitly states "We provide strong convergence guarantees for Scaff-PD when f_i are strongly convex." The critic's claim that it is "never stated upfront" is factually wrong. The milder version (abstract could signal this more prominently) is kept as Minor #2.
- Several formatting/style nitpicks and reproducibility nitpicks from the harsh critic are removed per the hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an angle, limitation, or implication that the paper itself does not already address or clearly motivate.

## Suggestions

1. Add a short paragraph in Section 4 discussing the exact loss computation: state that computing the full loss f_i(x^r) is a single forward pass per client (no backpropagation needed), is practical in the cross-silo setting, and is far cheaper than computing a full gradient. This directly addresses concern #1.
2. In the abstract or first paragraph of the introduction, add a brief phrase like "for strongly convex client objectives" to qualify the convergence guarantees.
3. Specify which Bregman divergence is used (e.g., "with D(x, y) = ½‖x − y‖² for the Euclidean case") in the algorithm description.
4. Either provide the best-20% accuracy numbers (e.g., in Table 1) or remove the unsupported trade-off claim about best-20% accuracy.

## Score and Decision

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>