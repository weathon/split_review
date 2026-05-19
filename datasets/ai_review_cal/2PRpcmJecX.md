- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6
Now I have a thorough understanding of the paper and can verify the reviewer claims directly.

Let me compile the final review.

---

## Summary

This paper provides a finite-time global convergence analysis of projected policy gradient for infinite-horizon average-reward tabular MDPs under an ergodicity assumption. The key technical contribution is *proving* the smoothness of the average reward (using a projection technique to handle the non-uniqueness of the value function) rather than assuming it, as prior work by Bai et al. (2023) and Ganesh et al. (2024) did. This yields a sublinear convergence rate of O(1/k) per iteration (cumulative regret O(log T)), with bounds that depend on MDP-specific complexity constants rather than solely on state/action cardinality and discount factor.

## Strengths

- **First proof of smoothness for average reward in tabular MDPs without assuming it.** Prior work (Bai et al., 2023; Ganesh et al., 2024) relied on an unverified smoothness assumption. The paper introduces a projection matrix Φ (Lemma 1) to obtain a unique relative value function and then establishes smoothness of both the value function (Lemma 2) and the average reward itself (Lemma 4) using only properties of the underlying MDP. This is a genuine theoretical advance.

- **Sublinear convergence with explicit MDP-dependent rates.** Theorem 1 provides bounds of the form 1/(1/(ρ\*−ρ^{π₀}) + νk), yielding O(1/k) per-iteration suboptimality and O(log T) cumulative regret. The bound is meaningful from the first iteration (unlike prior bounds with large multiplicative constants), and for simple MDPs the paper also identifies conditions for exponential convergence (Theorem 1, second bullet).

- **Convergence rates that depend on problem structure, not just cardinalities.** The bounds involve constants (C_m, C_p, C_r, κ_r, C_PL) that reflect transition sensitivity, reward variance, and mixing time. The paper shows these can improve on worst-case bounds — e.g., for MDPs with action-independent transitions the iteration complexity improves from O(|S||A|/ε) to O(|S|/ε) (Section 3.2).

- **Qualitative experimental support for complexity-dependent convergence.** The simulations (Section 4) show that convergence speed varies with state/action space size, reward variance, and transition kernel determinism in directions predicted by the theory. While qualitative (not a rate verification), these illustrations are useful sanity checks on the theoretical predictions.

## Weaknesses

### Major

None fatal to the paper's core claims. The main theoretical result is sound in structure; remaining concerns are about the sharpness of the bounds.

### Minor

- **The constant C_PL = max_{π,s} d^{π\*}(s)/d^π(s) can be large and is not bounded in terms of standard MDP parameters.** This ratio (the "distribution mismatch coefficient") could grow with the size of the state space and mixing time. The paper notes "C_PL is a constant that is proportional to the size of the state space" and acknowledges "We do not know if the appearance of such a constant is inevitable or not" (line 247). While a similar constant appears in discounted-reward analyses (Agarwal et al., 2020; Xiao, 2022a), its magnitude affects practical relevance. The paper does not provide explicit bounds on C_PL from primitive MDP parameters, so the convergence guarantee could be arbitrarily loose in worst-case instances.

- **Experiments are purely qualitative and do not verify the claimed convergence rate.** The simulations show that average reward increases over iterations and that convergence speed varies with MDP structure, but they do not compute suboptimality gaps, attempt to verify the O(1/k) rate (e.g., via log-log plots), or compare against the theoretical bound. The claim that "These observations further validate the theoretical bounds" (Section 1.2) overstates what the qualitative evidence supports. The step size used in the experiments is also not reported.

- **The extension to discounted MDPs (Section 3.2) is presented without a rigorous derivation.** The paper states the iteration complexity improves to O(|S|L₂^Π/ε) and uses a single "trivial MDP" example (C_p = 0 or κ_r = 0) to illustrate the improvement. However, the derivation of L₂^Π for the discounted setting is not given; the paper says it "can be derived through a process analogous to the one described in this paper" (line 261). The claimed improvement over Xiao (2022a) is suggestive but not proven in the submitted text. (This does not affect the primary contribution on average-reward MDPs.)

- **Lemma 8 contains a notation issue**: ⟨∂ρ_{π_{k+1}}/∂π_{k+1}, π′ − π_{k+1}⟩ should read ⟨∂ρ^{π_{k+1}}/∂π, π′ − π_{k+1}⟩ (the gradient evaluated at π_{k+1}). The bound 4√|S| L₂^Π ‖π_{k+1} − π_k‖ appears without derivation in the main text; full justification would be in the appendix.

### Trivial

- The step size used in the simulations (Section 4) is not reported, making it impossible to verify whether η < 1/L₂^Π was satisfied. The paper should state this value.

## Nice-to-Haves

- Derive explicit upper bounds on C_PL in terms of |S|, the mixing time, or other primitive MDP parameters, to clarify when the convergence guarantee is non-vacuous.
- Provide a concrete numerical verification of the O(1/k) rate (e.g., plot ρ\* − ρ^{π_k} on a log-log scale) in at least one MDP.
- Include a baseline comparison (e.g., natural policy gradient) in the experiments to contextualize the results.

## Removed Points

These points appeared in the inputs but were removed with justification:

- **"Core contribution unsubstantiated / missing proofs"**: The harsh critic's main criticism is that the main text lacks derivations of Lemmas 1–8 and that Theorem 1's ν expression is "garbled." The hard rules require removing weaknesses about missing appendix content (the parser strips appendices, which exist in the original submission). The ν expression (`\prime:=...`) is a legitimate mathematical expression, and the `\prime` is a parser formatting artifact for ν — not garbled. **Removed.**

- **"O(1/T) vs O(log T) inconsistency"**: The abstract states per-iteration suboptimality O(1/T) at iteration T; the contributions state cumulative regret O(log T). Theorem 1 yields ρ\*−ρ^{π_k} ≤ 1/(1/(ρ\*−ρ^{π_0}) + νk) = O(1/k), so at iteration T the gap is O(1/T), and regret Σ_k O(1/k) = O(log T). These are standard and consistent; the reviewer's claimed inconsistency is factually incorrect. **Removed.**

- **"Lemma 5 is implausible"**: For projected gradient ascent on an L-smooth function, the standard optimality condition of projection gives ⟨∇f(x_k), x_{k+1}−x_k⟩ ≥ (1/η)‖x_{k+1}−x_k‖². Combined with the smoothness inequality, this directly yields f(x_{k+1})−f(x_k) ≥ (1/η − L/2)‖x_{k+1}−x_k‖² ≥ (L/2)‖x_{k+1}−x_k‖² when η < 1/L. This is textbook material; the reviewer's claim that this is "implausible" is incorrect. **Removed.**

- **"Scanned table / constants not defined"**: The constants C_m, C_p, C_r, κ_r are defined in Table 1, which exists in the original submission but appears as an image placeholder in the parsed text. This is a parser artifact, not an omission. **Removed.**

- **"Over-claiming novelty"**: The paper's claim is the *first global convergence proof for policy gradient (not natural policy gradient) in average-reward MDPs without assuming smoothness*. The cited prior work either studies natural policy gradient (Even-Dar et al., 2009; Murthy & Srikant, 2023) or assumes smoothness (Bai et al., 2023). The claim is accurate. **Removed.**

- **"Eigenvalue justification needed"**: The paper notes that under Assumption 1 (ergodicity), the non-1 eigenvalues of Φℙ^π are strictly less than 1 in magnitude. This is a standard claim and the assumption is cited. The detailed proof would be in the appendix. **Removed.**

- **"Lemma 6 should be self-contained"**: Citing Cao (1999) for the performance difference lemma is standard and acceptable. **Removed.**

## Novel Insights

None beyond the paper's own contributions. Both reviews accurately characterize the paper's technical content; no hidden finding emerged from cross-examination.

## Suggestions

1. Add a brief intuitive explanation of C_m, C_p, C_r, κ_r in the main text (even one sentence each) so the reader can understand the bound structure without consulting the table.
2. Report the step size used in experiments and note whether η < 1/L₂^Π was satisfied.
3. Add a log-log suboptimality plot for at least one experiment to qualitatively verify the O(1/k) trend.
4. Clarify the notation in Lemma 8: replace ∂ρ_{π_{k+1}}/∂π_{k+1} with (∂ρ^{π}/∂π)|_{π=π_{k+1}}.
