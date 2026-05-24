## Summary

This paper proposes a simplified spectral algorithm for two-community SBM community detection that eliminates both the degree-based row/column deletion step and the separate Correction step from Chin et al. (2015). The authors argue that Spectral Partition alone achieves the information-theoretic inverse-log error rate, supported by Chernoff-based bounds on the γ–sinθ relationship, normal-approximation Monte Carlo analysis, and experiments on synthetic graphs. The paper claims the simplified algorithm recovers the optimal bound of Theorem 1.3 without the Correction step.

## Strengths

- **Entrywise eigenvector characterization via Abbe et al. approximation.** The paper leverages the approximation w₂ ≈ Au₂/(a−b) to model the second eigenvector entries as differences of binomial random variables (Section 3.3). This concrete distributional assumption enables the subsequent Chernoff and normal-approximation analyses and is a genuinely clever observation.

- **Optimization framework establishing looseness of Theorem 3.2.** The formulation in Section 3.2 that expresses cos θ in terms of ordered eigenvector entries under fixed misclassification budget cleanly demonstrates that the quadratic bound γ ≤ sin²θ is achievable by worst-case vectors but not tight for vectors with the structure produced by the spectral algorithm. This is a useful insight.

- **Demonstration that perfect recovery is possible with imperfect eigenvector alignment.** The finding (Section 3.5) that γ = 0 can be achieved even when sin θ > 0 is interesting and clarifies that the eigenvector's entry *distribution*, not merely its angular alignment, determines recovery success. This is a concrete conceptual contribution.

- **Removal of the degree-based deletion step is reasonably justified.** The argument that the spectral-norm bound (Theorem 2.2) holds without zeroing high-degree rows/columns, requiring only adjusted constants, is plausible and supported by references to Füredi & Komlós and Krivelevich & Vu.

## Weaknesses

### Major

- **No theorem is proved for what the simplified algorithm guarantees.** The paper's central claim is that the simplified Spectral Partition achieves the information-theoretic bound of Theorem 1.3. Yet the paper states no theorem that specifies an error guarantee for the modified algorithm, nor does it provide a rigorous proof. The bridge from the empirical fit (Equation 13) to Theorem 1.3 is asserted in one sentence (lines 272–276: "The functional form in Equation 13, combined with the claims of Theorems 2.2 and 3.1, directly yields the final result stated in Theorem 1.3") without derivation. An empirical fit cannot substitute for a proof. This undermines the paper's main contribution claim.

- **Experiments are conducted in the dense regime, not the sparse regime of the theoretical bounds under discussion.** The paper's theoretical framing (Theorem 1.3, the Chin et al. algorithm, the information-theoretic lower bounds) concerns the sparse SBM where *a* and *b* are constants and edge probabilities are *a/n*, *b/n* → 0. However, all experiments use *a* = 0.06*n*, *b* = 0.04*n*, giving constant edge probabilities and linear expected degree — a dense regime where recovery is fundamentally easier. The experiments therefore do not test whether the simplified algorithm works in the regime where the Correction step was originally needed, nor do they support claims about the sparse information-theoretic limits.

- **The Chernoff and normal-approximation analyses are heuristic, not rigorous proofs.** Section 3.4 attempts to derive constraints on sorted eigenvector entries from Chernoff concentration inequalities, but the critical step from tail bounds for a single random variable to simultaneous constraints on all order statistics is not rigorously justified. The paper acknowledges the O(1/√n) approximation error from Abbe et al. but never quantifies how this propagates through the subsequent bounds. The normal approximation in Section 3.5 assumes unit variance and corrects only with an OLS scaling factor, which is not theoretically derived. These analyses are presented as "theoretical" but function as heuristic motivation.

### Minor

- **The paper oscillates between sparse and dense framing without clear scoping.** The abstract mentions "constant edge density assumptions," the introduction frames the problem in the sparse SBM (a, b constants), and the experiments use dense parameters. The paper should clearly state which regime it addresses and align all analysis accordingly.

- **The derivation connecting the fitted empirical curve (Equation 13) to Theorem 1.3 is omitted.** Even accepting the empirical fit, the algebraic steps showing how sin θ = C/∛(log(2/γ)) combines with Theorems 2.2 and 3.1 to produce the bound on (a−b)²/(a+b) are not shown. The reader cannot verify this crucial link.

- **Parameter exploration is too narrow.** The experiments fix a/n = 0.06 and b/n = 0.04 and vary only n. No exploration of how the relationship depends on the signal-to-noise ratio (a−b)²/(a+b) is conducted, which is the central quantity in all theoretical bounds.

### Trivial

- Figure 5 caption and description contain inconsistencies (e.g., the text refers to "yellow" and "purple" points while the description uses "orange" and "purple"; the figure description in lines 343-347 repeats and garbles content).

## Nice-to-Haves

- A rigorous theorem stating what the simplified algorithm actually guarantees, even with a weaker bound, would greatly strengthen the paper.
- Experiments in the sparse regime (a, b constant independent of n) would properly test the claims.
- Scanning the (a, b) parameter space to probe dependence on (a−b)²/(a+b) would make the empirical evidence considerably more convincing.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic's claim that "The fit with OLS to account for the unit normalization is not explained"** — The paper does explain this at lines 226-228 and 242-244: OLS is used to fit the theoretical prediction to the data while accounting for the fact that the normalization constraint ∑x_i² = 1 changes the effective variance. The explanation is present, though thin.
- **Harsh Critic's complaint about Figure 4 "labeling errors"** — The caption is confusing (it swaps descriptions between subplots), but this is a presentation issue rather than a substantive error. Demoted to Trivial.
- **Strength Finder's claim that "the direct experimental evaluation in Figure 5... directly recovers the optimal bound of Theorem 1.3"** — This overstates the evidence; the empirical fit does not constitute a proof. Removed as a standalone strength and incorporated into the criticism about missing proof.
- **Strength Finder's "Rigorous justification for removing the degree-threshold deletion step"** — The justification is plausible but the proof is deferred to the stripped appendix, so "rigorous" cannot be verified. Kept as a strength but toned down.
- **Strength Finder's "Reproducible experimental setup and scaling analysis"** — Generic; dropped.
- **Harsh Critic's claim about "The paper's structure makes it impossible to assess whether an improved performance guarantee has been established"** — This is essentially restating the missing-theorem criticism; merged rather than duplicated.

## Novel Insights

The paper's most genuinely novel observation is that spectral community detection can succeed with γ = 0 even when the computed eigenvector is not perfectly aligned with the population eigenvector (sin θ > 0), because what matters is the *distributional shape* of the eigenvector entries, not just the angular distance. This insight, concretely demonstrated through the optimization framework and Monte Carlo simulations, sharpens our understanding of why spectral methods work and suggests that angle-based guarantees (like Theorem 3.2) systematically underestimate performance for structured eigenvectors.

## Suggestions

- State and prove a theorem that gives a concrete error guarantee for the simplified algorithm. Even a weaker bound derived rigorously from the Chernoff or normal-approximation framework would be a meaningful contribution.
- Either run experiments in the sparse regime (a, b constant) or explicitly scope the paper as addressing the dense regime and adjust the theoretical comparisons accordingly.
- Show the algebraic derivation connecting Equation 13 to Theorem 1.3 so the reader can follow the claimed bridge between empirics and theory.

## Score and Decision

**Round 1 bracketing:** Based on three queries across score bands, the paper was initially bracketed between 3.0 and 5.75, with the most topically relevant anchor being zhFyKgqxlz (5.75, exact community recovery with spectral algorithms). This paper is clearly weaker than that anchor.

**Round 2 narrowing:** Retrieved anchors in the 2.5–5.5 range. Key comparisons:
- VyMW4YZfw7 (3.00): A "simplifying GNN" paper rejected for insufficient novelty and limited experiments. This paper has more technical content (Chernoff analysis, optimization framework) but shares the problem of insufficient theoretical backing for its central claim. The paper under review is somewhat stronger.
- Feg9xrbFcn (4.50): Proposed simplified k×k spectral clustering; rejected with mixed reviews citing limited testing and unclear differentiation. The paper under review has comparable issues (narrow experiments, overclaiming) and a more serious theoretical gap (no proof for main claim).
- G8U2nGP3Vi (5.40): A theory paper with genuine technical novelty in singular subspace perturbation bounds. The paper under review is substantially weaker — it lacks rigorous proofs and its experiments are in the wrong regime.
- 5dpuLgwQ0d (4.75): A nearly-linear time algorithm for finding cluster count with novel technical contributions. The paper under review does not reach this level of technical contribution.

**Final assessment:** The paper has interesting ideas — the entrywise eigenvector characterization and the demonstration that Theorem 3.2 is loose for structured eigenvectors are genuine contributions. However, the central claim (that the simplified algorithm achieves the optimal bound without correction) is not proved, and the experiments are conducted in a regime that does not test this claim. The paper falls between VyMW4YZfw7 (3.00) and Feg9xrbFcn (4.50), closer to the latter due to its more substantial technical ideas, but held back by the missing theorem and regime mismatch.

**Anchor comparison summary:**
- VyMW4YZfw7 (3.00, round 1): Weaker — less technical depth, similar overclaiming issues.
- Feg9xrbFcn (4.50, round 1): Similar tier — the paper under review has more interesting theoretical ideas but a more severe gap between claims and evidence.
- zhFyKgqxlz (5.75, round 1): Much stronger — rigorous proofs, proper theoretical contribution.
- G8U2nGP3Vi (5.40, round 2): Stronger — genuine theoretical novelty with rigorous proofs.
- 5dpuLgwQ0d (4.75, round 2): Stronger — clear algorithmic contribution with provable guarantees.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>