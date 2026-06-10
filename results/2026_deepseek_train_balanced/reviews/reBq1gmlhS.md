Here is the final consolidated review.

---

## Summary

This paper addresses the problem of achieving differential privacy in reinforcement learning from human feedback (RLHF) under the linear reward parametrization. It proposes differentially private variants of existing non-private RLHF algorithms and provides suboptimality bounds of \(O(\sqrt{d/n} + (d\log(1/\delta))^{1/4}/\sqrt{\epsilon n})\) for both contextual bandits and general MDPs, asymptotically matching non-private minimax-optimal rates when \(\epsilon\) is constant. The paper identifies a genuine technical challenge—the "seminorm mismatch" between spherical DP noise and RLHF's data-dependent geometry—but the main text is missing crucial details needed to evaluate the contribution.

## Strengths

1. **First DP analysis for RLHF with rate-preserving guarantees**: The paper addresses an underexplored problem—privacy in RLHF—and derives suboptimality bounds (Eq. 38, 50) that, in the constant-\(\epsilon\) regime, asymptotically match the non-private minimax-optimal rates of Zhu et al. (2023). This extends the DP-in-bandits literature to the setting where rewards must be learned from preferences rather than observed directly.

2. **Explicit identification of the seminorm mismatch challenge**: Lines 170–172 clearly identify a non-trivial technical obstacle: the MLE loss in RLHF is strongly convex with respect to the data-dependent seminorm \(\|\cdot\|_{\Sigma_{\mathcal{D}}}\), but the Gaussian perturbation required for DP is spherical, causing error that scales with \(\|\cdot\|_{(\Sigma_{\mathcal{D}}+\lambda I)^{-1}}\). This diagnosis goes beyond routine application of existing DP mechanisms and explains why the RLHF setting is uniquely challenging.

3. **Modular privacy guarantees enabling public release**: The paper's framework (lines 41–42) ensures that privately learned reward parameters and perturbed data covariance each satisfy \((\epsilon,\delta)\)-DP individually, decoupling private reward estimation from downstream policy optimization and enabling public release of the learned reward weights.

## Weaknesses

### Fatal
None.

### Major

1. **Broken equation reference and undefined symbols in the main text**: Theorem 5.2 (line 211) defines the suboptimality bound using \(F(n,d,\eta,\epsilon,\delta)\) "as in (3)" — but no equation (3) appears anywhere in the visible text. The same theorem (lines 214–215, 220) uses the term "\(v\)" which is never defined in the main body. These are not appendix-deferral issues; they are concrete missing elements that render the stated theorem uninterpretable from the main text alone. The paper's central theoretical result cannot be properly understood as presented.

2. **Unspecified regularity assumptions**: Every theorem (1.1–1.4, 5.1, 5.2) is qualified by "under appropriate regularity assumptions." The only concrete condition stated is Assumption 2.1 (bounded features, bounded parameter). For the BTL/PL log-likelihood to be strongly convex in the relevant seminorm — the central requirement for the analysis — additional conditions are needed (e.g., on the covariance spectrum, preference noise variance, or feature span). Without these, the reader cannot assess how restrictive the setting is or whether the conditions hold in realistic RLHF scenarios with high-dimensional, potentially ill-conditioned feature maps. This is particularly problematic given the qualitative conclusions about LLM privacy (line 230).

3. **Algorithms referenced but not described in the visible text**: Algorithm 1 (objective-perturbed MLE), Algorithm 2 (private covariance estimation), and Algorithm 3 (pessimistic policy optimization) are referenced repeatedly (lines 170, 172, 197, 199, 203, 209, 211) but never described — not even sketched. The reader never learns what noise is added, to what quantities, at what scale, or how the privacy budget is allocated. While detailed pseudocode may reside in the (parser-stripped) appendix, even a brief sketch in the main body is needed for the reader to understand the proposed approach.

4. **The central technical resolution is opaque**: Lines 170–172 convincingly diagnose the seminorm mismatch problem, but the paper provides no sketch — not even a high-level lemma statement — of how this difficulty is overcome. The reader is told "a more delicate analysis is required" but not what form that analysis takes. For a theory paper whose main intellectual claim is solving this mismatch, the resolution is invisible from the main text.

### Minor

1. **The suboptimality bound in Theorem 5.2 depends on the unknown optimal policy without discussion**: The bound involves \(\|(\Sigma_{\mathcal{D}}+\lambda I)^{-1}(\mathbb{E}_{s\sim\rho_{\pi}}[\phi(s,\pi^{*}(s))-v])\|_2\), which depends on \(\pi^{*}\) and the undefined \(v\). The paper claims this simplifies to \(\widetilde{O}(\sqrt{d/n})\) without arguing that the multiplicative factor is bounded by a constant. The claimed rate may therefore depend on problem-instance-specific quantities without acknowledgment.

### Trivial
None.

## Nice-to-Haves

- A brief technical sketch (1–2 paragraphs) in Section 4.1 stating the key lemma that overcomes the seminorm mismatch would transform the paper's transparency.
- A comparison to alternative approaches (e.g., DP-SGD during RL optimization, or output perturbation of the non-private MLE) would help contextualize the contribution.
- A note on the computational cost of the private MLE relative to the non-private version would be useful.

## Removed Points

These points from the input reviews were evaluated against the paper and removed or demoted:

1. **"Minimax optimality claim is overstated"** — Removed. The paper explicitly qualifies its claim with "in the typical differential privacy setting \(\epsilon\) is a constant" (lines 40–41). The bound is transparently stated and the regime is specified. The critic's objection about the high-privacy regime (\(\epsilon\) small) would apply generically and the paper does not claim to dominate that regime.

2. **"Does not distinguish between privacy for raters vs. prompts"** — Removed as scope-expansion. The paper defines DP for the entire tuple (lines 14–15), which is the standard principled approach. A theoretical paper need not justify which aspect "matters most."

3. **"Related work is thin"** — Removed. Section 3 adequately covers the most relevant prior work (Zhu et al., 2023) and surveys DP in bandits/RL. It is appropriate for a conference paper scope.

4. **"No comparison to DP-SGD alternatives" and "No discussion of computational cost"** — Moved to Nice-to-Haves. These are suggestions for enrichment, not weaknesses.

5. **Criticism framed as "the paper does not make its own case" (fatal)** — Demoted from Fatal to Major (see Weakness #3 and #4). The paper has genuine structural deficiencies but these are addressable with revision, not fundamental invalidity. The algorithms and proofs likely exist in the stripped appendix; the core issue is insufficient presentation in the main text.

6. **Strength Finders' strengths about "first DP guarantee" and "modular privacy"** — Retained but calibrated as genuine strengths that are contingent on correctness of the technical approach, which cannot be fully verified from the visible main text.

## Novel Insights

None beyond the paper's own contributions. The identification of the seminorm mismatch between spherical DP noise and RLHF's data-dependent geometry is the paper's key insight, and both input reviewers correctly recognized it as the central technical challenge.

## Suggestions

1. Add a concrete definition of \(F(n,d,\eta,\epsilon,\delta)\) and define \(v\) in the main text, or explicitly reference the appendix equation where these appear.
2. State the "regularity assumptions" explicitly in the main body (e.g., conditions on the covariance matrix spectrum, preference noise variance).
3. Include at least a one-paragraph sketch in Section 4.1 of how the seminorm mismatch is resolved — the key norm bound or covering argument that makes the analysis work.
4. Provide brief descriptions of Algorithms 1–3 in the main text stating each algorithm's inputs, outputs, and the key step (what noise is added, to what, at what scale).

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>