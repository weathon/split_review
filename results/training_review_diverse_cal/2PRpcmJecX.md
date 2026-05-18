I now have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper presents the first finite-time global convergence analysis of projected policy gradient for infinite-horizon average-reward tabular MDPs. The key technical contribution is proving that the average reward is smooth with respect to the policy (removing an assumption that prior work relied on without verification), using a projection technique to resolve the non-uniqueness of the value function. The authors establish a sublinear convergence rate of the form \(1/(1/(\rho^*-\rho^{\pi_0}) + \nu k)\) and a regret of \(O(\log T)\), with constants that capture MDP-specific complexity. They also extend the analysis to discounted MDPs and provide simulations illustrating how MDP structure affects convergence.

## Strengths

1. **First finite-time global convergence analysis for average-reward PG without a smoothness assumption.** Prior work (Bai et al. 2023, Ganesh et al. 2024) assumed the average reward is smooth—an unverified premise. This paper provides a framework to prove smoothness from first principles via projection onto the subspace orthogonal to \(\mathbb{1}\), addressing the fundamental challenge that the value function is only defined up to an additive constant in the average-reward setting. (Lemma 1, Section 3.1.1)

2. **Explicit, MDP-dependent convergence bounds that go beyond state/action space cardinality.** The analysis introduces constants \(C_m, C_p, C_r, \kappa_r\) (Table 1) that capture transition structure, reward structure, and mixing properties of the specific MDP. The convergence bound in Theorem 1 and the smoothness constant \(L_2^\Pi\) in Lemma 4 depend on these parameters, meaning the theory predicts faster convergence for MDPs with simpler structure. This is a genuine refinement over bounds that only scale with \(|S|\) and \(|\mathcal{A}|\).

3. **Meaningful bound from the first iteration.** The suboptimality bound \(\frac{1}{1/(\rho^*-\rho^{\pi_0}) + \nu k}\) is tight at \(k=0\) (recovering the initial suboptimality) and decreases monotonically. This improves upon prior bounds of the form \(C/k^p\) where the constant \(C\) can be so large that the bound is vacuous for small \(k\). (Section 3, Remark)

4. **Strict improvement for simple discounted MDPs.** For MDPs with action-independent transitions (\(C_p=0\) or \(\kappa_r=0\)), the discounted extension yields \(O(|S|/\epsilon)\) iteration complexity versus the prior \(O(|S||\mathcal{A}|/\epsilon)\) (Xiao, 2022a). This demonstrates that the MDP-dependent constants capture meaningful problem structure. (Section 3.2)

5. **Simulations illustrating structural dependence.** Experiments vary reward variance and transition determinism while keeping state/action spaces fixed, showing convergence rates change in ways predicted by the theory's complexity constants. (Figures 1(b), 2)

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Unaddressed finiteness of \(C_{PL}\).** Lemma 7 defines \(C_{PL} = \max_{\pi\in\Pi, s\in\mathcal{S}} d^{\pi^*}(s)/d^\pi(s)\). Under Assumption 1 (irreducibility and aperiodicity), each \(d^\pi\) has full support, but the minimum entry of \(d^\pi\) over all \(\pi\) could be arbitrarily small, making \(C_{PL}\) potentially unbounded. The paper notes "We do not know if the appearance of such a constant is inevitable or not" but does not argue that it is finite. Since \(C_{PL}\) appears in the convergence rate of Theorem 1, this gap weakens the quantitative guarantee. (Section 3.1.2)

2. **Discounted MDP claim is overstated.** The paper says "Our approach improves on this bound" and presents \(O(|S|L_2^\Pi/\epsilon)\), but then shows that in the worst case \(L_2^\Pi = O(1/(1-\gamma)^5)\), recovering the same dependence as Xiao (2022a). The improvement is real only for MDPs with low \(L_2^\Pi\) (e.g., \(C_p=0\)). The paper acknowledges this after the claim, but the initial framing is misleading. (Section 3.2)

3. **Simulations are purely qualitative.** The experiments show that varying reward variance and transition determinism affect convergence in the expected direction, but they do not attempt to fit the claimed \(O(1/T)\) suboptimality rate or \(O(\log T)\) regret. For a theory paper this is not a fatal flaw, but the simulations add limited evidentiary support for the quantitative bounds. (Section 4)

4. **Transition from restricted smoothness to the descent inequality is not fully spelled out.** Lemma 4 defines a restricted smoothness condition (second directional derivative bound), while Lemma 5 invokes a standard descent inequality that requires the full gradient-Lipschitz property. The paper sketches the connection but does not show in the main text that restricted smoothness implies the global inequality used. (Section 3.1.2; this would be clarified by the full proof in the appendix.)

### Trivial
None.

## Nice-to-Haves

- Provide an explicit bound on \(C_{PL}\) in terms of standard MDP parameters (e.g., mixing time, state space size) to establish finiteness.
- For the discounted extension, clearly separate the worst-case bound (matching prior work) from the improved bound for low-complexity MDPs.
- Run a quantitative validation of the convergence rate (e.g., curve-fitting the suboptimality decay to check the \(O(1/k)\) prediction).

## Removed Points

These points were flagged by reviewers but removed after verification against the paper:

1. **"Paper does not provide proofs of its main claims."** The paper is labeled as a proof outline (Section 3.1: "KEY IDEAS AND PROOF OUTLINE"); full proofs are standardly deferred to appendices, which are stripped by the parser. The main text states the lemmas and sketches the logic.

2. **"Theorem 1's \(\nu\) expression is garbled / dimensionally nonsensical."** The expression \(\nu = a(1+4a)^{-3/2}\) with \(a = 1/(32C_{PL}^2|S|L_2^\Pi)\) is a well-formed scalar expression. The exponent \(-3/2\) on a scalar is standard.

3. **"The exponential bound does not converge to zero."** The bound \(c^{-k/2}(\rho^*-\rho^{\pi_0})^{1/2^k}\) converges to zero because \(c^{-k/2}\to 0\) (since \(1/c<1\) implies \(c>1\)) and the second factor tends to 1. The reviewer overlooked the \(c^{-k/2}\) factor.

4. **"\(O(1/T)\) and \(O(\log T)\) are inconsistent."** Suboptimality \(O(1/k)\) per iteration summed over \(T\) iterations gives \(O(\log T)\) regret. These are consistent.

5. **"Lemma 5's direction is suspicious."** For an \(L\)-smooth function under projected gradient ascent with \(\eta < 1/L\), the standard smoothness inequality plus the projection property yields \(\rho(\pi_{k+1})-\rho(\pi_k) \ge (1/\eta - L/2)\|\pi_{k+1}-\pi_k\|^2 \ge (L/2)\|\pi_{k+1}-\pi_k\|^2\). The lemma is correct.

6. **"Missing proofs for Lemma 2, 7, 8."** Proofs are in the appendix, which is stripped by the parser.

7. **Formatting/notation nitpicks.** These are either parser artifacts or do not affect the contribution.

## Novel Insights

The key insight that emerges from the reviews is that the paper's main contribution—proving smoothness of the average reward via projection—is structurally novel and addresses a genuine open problem. The qualitative simulation results, while not a quantitative validation, usefully demonstrate that the MDP-dependent constants in the bound correspond to observable convergence behavior (higher reward variance and more deterministic transitions slow convergence). The main gap that would benefit most from attention is the \(C_{PL}\) finiteness, which, if unbounded, could make the convergence rate arbitrarily slow for some MDPs even under the paper's uniform ergodicity assumption.

## Score and Decision

This paper makes a genuine theoretical contribution to an important problem. The main claims are clearly stated, the proof structure is coherent, and the weaknesses are minor or addressable. The harsh reviewer's most severe criticisms were verified against the paper and found to be factually incorrect or based on missing appendix content. The paper should be accepted.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>