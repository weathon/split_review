## Summary

This paper presents a unified theoretical framework for approximate quantum loaders (AQLs) and derives information-theoretic bounds (Theorem 3.1) showing that infidelity scales linearly with an entanglement measure $\mathcal{S}(U^\dagger|\psi_{\text{target}}\rangle)$. Guided by this insight, the authors propose AQER, an AQL method that constructs loading circuits via a three-step pipeline (entanglement reduction, product-state approximation, parameter refinement). Extensive experiments on classical (MNIST, CIFAR-10, SST-2) and quantum (S-RQC, GS-TFIM) datasets with up to 50 qubits show that AQER consistently outperforms MPS-, HEC-, and AQCE-based methods in both accuracy and gate efficiency.

## Strengths

- **First information-theoretic bounds for AQL.** Theorem 3.1 provides lower and upper bounds on infidelity as a function of an entanglement measure, establishing a principled theoretical foundation that was previously lacking (Section 3.1). The bounds are algorithm-independent and the linearized forms as $S \to 0$ are explicitly given.

- **AQER achieves state-of-the-art results across all benchmarks.** In Table 1, AQER attains the lowest infidelity on all five datasets. The improvement is largest on S-RQC (infidelity 0.067 at $G=81$ vs. 0.367 for the next-best AQCE — a >5× reduction) and on MNIST, CIFAR-10, and SST-2 at every gate budget.

- **Scalability demonstrated to 50 qubits with stable trainability.** Figure 4(a) shows that Step III optimization on 50-qubit GS-TFIM states avoids barren-plateau collapse (initial infidelity well below 1, decreasing steadily). Figure 4(b) confirms that when $T$ scales linearly with $N$, infidelity remains nearly constant across $N \in \{20,30,40,50\}$.

- **Explicit product-state approximation without numerical optimization.** Corollary 3.2 provides a closed-form solution for the single-qubit rotation parameters in Step II, eliminating a costly optimization subproblem (Section 3.2, Step II).

- **Downstream task performance validates practical utility.** AQER-loaded states correctly detect the quantum phase transition in TFIM (Figure 4(c)) and achieve classification error on SST-2 approaching the exact-loading baseline (Figure 5(b)).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Abstract imprecision regarding the entanglement measure.** The abstract states that infidelity scales with entanglement "when the loading circuit is applied to the target state." Theorem 3.1 and the introduction correctly define the quantity as $\mathcal{S}(U^\dagger|\psi_{\text{target}}\rangle)$ — the entanglement of the target state *after the inverse of the loading circuit*. These are not equivalent ($U|\psi_{\text{target}}\rangle$ vs. $U^\dagger|\psi_{\text{target}}\rangle$). The body of the paper is consistently correct, but the abstract should be aligned to avoid misrepresenting the central theoretical insight.

- **No ablation study isolating the three pipeline steps.** AQER's three-step design (entanglement reduction → product-state approximation → parameter refinement) is the core algorithmic contribution, yet no experiment removes individual steps to quantify their standalone contributions. For example, how much accuracy is lost if Step II is omitted? How much does Step III improve over the results after Step II alone? Without this, the causal claim that "principled entanglement reduction drives the advantage" remains partially associative. Adding even a simple ablation (e.g., reporting infidelity after Steps I+II vs. after all three steps, or skipping Step I) would substantially strengthen the paper's internal argument.

- **Complexity analysis deferred to the appendix.** The main text mentions that evaluating $\mathcal{S}$ is efficient ("involves only local measurements") and points to Appendices D and G for complexity analysis, but does not give an explicit scaling expression (e.g., in terms of $N$, $T$, and bond dimension or state-vector size) that would justify the "scalable" claim for a general audience. Including a brief complexity statement in Section 3.2 or Section 4 would improve accessibility without relying on the appendix.

### Trivial
None.

## Nice-to-Haves

- **Direct gradient-variance measurements.** The trainability analysis in Figure 4(a) shows loss curves, which are a valid indicator. The barren-plateau literature typically measures gradient variance directly; reporting it would rigorously substantiate the claim of mitigated vanishing gradients.
- **Baseline curves at matched $G$ on Figure 3(b).** Adding the baselines (MPS, HEC, AQCE) on the same axes as AQER's infidelity-vs.-$T$ curves would make the comparison more informative.
- **Brief derivation sketch for Corollary 3.2 in the main text.** The explicit optimality of Step II is a highlight; a short intuition in the main body (even one sentence explaining that it follows from tracing out correlations in the low-entanglement state) would be helpful.
- **Rationale for the $R_{ZZ}R_YR_Z$ block structure.** A brief note on why this specific gate structure was chosen for Step I's two-qubit blocks would aid reproducibility.

## Removed Points

- *"Scalability and complexity reasoning omitted from the main text"* (Harsh Critic's point 3) — **weakened to Minor.** The main text does address efficiency (Remark (i): "evaluating and optimizing $\mathcal{S}$ is efficient since it involves only local measurements") and explicitly cites Appendix G for the detailed analysis. The critic's framing that this is "omitted entirely" is overstated; the real issue is that an explicit scaling expression does not appear in the main body.
- *"The paper's central claim that 'principled entanglement reduction' drives the advantage remains an associative claim"* — **retained in Minor** as the ablation point, but the hyperbolic framing ("associative rather than validated causal") is removed. Figure 3(a) already shows a strong correlation between $S$ and infidelity, which provides causal evidence; an ablation would further strengthen it.
- *Section-by-Section minor preferences* (derivation sketch, matched baselines in Fig. 3(b), gate-structure rationale) — **moved to Nice-to-Haves** as they are presentation preferences, not weaknesses.
- *Gradient variance measurements* — **moved to Nice-to-Haves** as a constructive suggestion, not a weakness of the presented experiments.

## Novel Insights

None beyond the paper's own contributions. The review surfaces a genuine abstract imprecision and the absence of an ablation study as the two most actionable areas for improvement, but these observations derive straightforwardly from reading the paper against its own claims.

## Suggestions

1. **Fix the abstract** to say "when the *inverse* of the loading circuit is applied to the target state" (or equivalent), matching the introduction and Theorem 3.1.
2. **Add a simple ablation** (e.g., report infidelity after Steps I+II vs. after all three steps, or skip Step I entirely) to causally validate the three-step design.
3. **Include an explicit complexity expression** in Section 3.2 or Section 4 (e.g., scaling in terms of $N$, $T$, and bond dimension or state-vector size) to support the "scalable" claim in the main text.

## Score and Decision

**MY FINAL SCORE:** <score>8.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>