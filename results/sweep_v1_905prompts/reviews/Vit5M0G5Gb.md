Now I have sufficient information to write the final consolidated review.

---

## Summary

This paper develops a unified theoretical framework for understanding saddle-to-saddle learning dynamics — the characteristic progression through plateaus and rapid improvements — across a wide range of neural network architectures. The key theoretical contributions are: (1) establishing that fixed points of narrow networks are embedded as saddle points in wider networks (Theorem 1, generalizing Fukumizu & Amari, 2000); (2) proving that invariant manifolds exist along which wider networks behave like narrower ones (Theorem 3); and (3) showing that these landscape features combine with timescale separation to produce progressive learning. The paper distinguishes two mechanisms — data-induced timescale separation (linear networks) leading to low-rank weights, and initialization-induced timescale separation (quadratic networks / self-attention) leading to sparse weights — and validates predictions about width, data distribution, and initialization on linear networks and linear self-attention.

## Strengths

- **Architecture-agnostic landscape theory (Theorems 1 and 3).** The embedded fixed points and invariant manifolds are proved for the entire class of networks defined by Equation (1), which subsumes fully-connected, convolutional, and attention-based architectures. Theorem 1 extends the seminal Fukumizu & Amari (2000) construction with two new families of embedded fixed points (Eqs. 6 and 7), and Remark 1 explicitly notes that the newly visited saddles during learning (Figure 1B–G) correspond to these new constructions, not the previously known ones. This is a genuine theoretical advance.

- **Clean mechanistic distinction between two types of timescale separation.** The analysis shows that linear networks exhibit a *between-directions* timescale separation driven by the data spectrum (Theorem 4), while quadratic networks exhibit a *between-units* timescale separation driven by initialization discrepancies (Proposition 5). This directly explains why the observed weight structures are low-rank in the former (Figure 1B–C) and sparse in the latter (Figure 1F–G). The distinction is novel, clearly articulated, and supported by theory.

- **Testable predictions and empirical demonstrations across six architectures.** Figure 1 compellingly demonstrates the signature saddle-to-saddle pattern (loss plateaus, alternating with rapid drops, and corresponding weight structures) across linear fully-connected, linear convolutional, ReLU fully-connected, ReLU convolutional, linear self-attention, and quadratic networks. The paper then derives and tests specific, quantitative predictions about how width, data distribution, and initialization affect learning (Figure 2), including a non-trivial prediction that increasing width shortens plateaus in linear self-attention but not in linear fully-connected networks (Figure 2A).

- **Principled discussion of failure modes.** Section 7 explicitly identifies the two conditions necessary for saddle-to-saddle dynamics (escape path follows invariant manifolds; initialization near a low-effective-width manifold) and gives concrete counterexamples (tanh networks violate the first, large random initialization violates the second). This clarifies the boundaries of the framework rather than claiming universality.

## Weaknesses

### Fatal
None.

### Major

- **Framing overclaims relative to what is dynamically proven.** The title states the paper "explains a simplicity bias across neural network architectures," and the abstract says "we present a theoretical framework that explains a simplicity bias" for "a general class of neural networks." However, the dynamical mechanism — the *explanation* — is fully rigorous only for two-layer linear and quadratic networks. For ReLU, tanh, convolutional, and deep networks, the paper establishes the *landscape* features (fixed points, invariant manifolds) and provides empirical demonstrations of saddle-to-saddle behavior (Figure 1D–E), but does not prove that the dynamics follows the saddle-to-saddle path. Section 7 honestly acknowledges that "the analysis of dynamics in Section 5 only applies to two-layer networks," but this limitation is not reflected in the title or abstract. A reader encountering the title alone would reasonably expect a fully general dynamical theory. This is a structural issue affecting the paper's central framing, though the underlying contributions remain valuable.

### Minor

- **Subsequent saddle-to-saddle transitions are analyzed heuristically, not rigorously.** Theorem 4 provides a rigorous bound for the initial phase (small initialization leading to approximately rank-\(r\) weights). However, the analysis of subsequent transitions (Eq. 12 and surrounding text) states that "the dynamics near a rank-\(r\) saddle is again approximately a linear dynamical system" and references Appendix G.3. The paper does not prove that the trajectory stays sufficiently close to the invariant manifold across multiple transitions, nor does it provide error bounds for the approximation. The quadratic case (Proposition 5) relies on an even more heuristic scalar example (Eqs. 15–16) to motivate the timescale separation, with the full analysis deferred to the appendix. This is standard for theoretical work at this level, but the gap between the rigorous early-phase treatment and the heuristic later-phase extension should be more clearly marked in the main text.

- **Predictions validated on only two of the six claimed architectures.** The quantitative predictions about width, data distribution, and initialization (Figure 2) are tested on linear fully-connected networks and linear self-attention, but not on ReLU, convolutional, or quadratic networks (beyond linear self-attention, which is already the quadratic case). The prediction that increasing width shortens plateaus in the quadratic case (a central prediction of the theory) is tested via linear self-attention but not on the toy quadratic network shown in Figure 1G or on any other genuinely quadratic architecture. Testing on even one additional non-linear architecture (e.g., a ReLU network with synthetic data having a known spectral decomposition) would substantially strengthen the claim that the theory applies "across architectures."

- **Loss curves appear to be single runs without error bars.** The plots in Figure 2 show no uncertainty estimates; they appear to be individual trials. While single-run plots are common in this literature, the predictions are about the *effect* of parameters (width, exponent, initialization scale) and would benefit from multi-seed statistics to establish reliability, especially for effects that are gradual (e.g., the smooth shortening of plateaus with width in linear self-attention).

### Trivial
None.

## Nice-to-Haves

- The quadratic case analysis would be strengthened by including a two-unit quadratic network in closed form (or a local stability analysis) in the main text rather than deferring entirely to the appendix.
- A direct measurement of the distance from initialization to the rank-1 invariant manifold, correlated with plateau duration, would strengthen the argument connecting initialization scale to feature learning strength.
- A brief discussion of discretization effects (gradient flow vs. gradient descent with finite learning rate) would be useful, especially for the quadratic case where growth can be explosive.

## Removed Points

The following points from the reviewer inputs were removed with justification:

1. **Criticism about "lack of rigorous dynamical analysis" being critical/fatal.** The harsh critic claimed the approximation in Eq. 12 is "not rigorously justified." The paper explicitly states "approximately a linear dynamical system" and references Appendix G.3. This is a reasonable approach for a paper at this level. The point is retained as Minor (above) rather than the "critical" framing it received.

2. **Criticism about the quadratic case being "noticeably weaker" / "heuristic."** The paper is transparent about the level of analysis: Proposition 5 analyzes the approximate dynamics, and the scalar example (Eqs. 15-16) is clearly presented as intuition with the full analysis in the appendix. This is standard practice.

3. **Criticism about "the paper does not provide a rigorous link to saddle-to-saddle dynamics beyond the examples shown" for the general nonlinear activation discussion (Section 5.3).** The paper explicitly says this is speculative: "We discuss the implications for general nonlinear activation" and provides intuition via Taylor expansion. This is appropriately scoped as discussion, not a claimed proof.

4. **Criticism about missing related works.** Per policy, we do not flag missing references.

5. **Strength about "unified theoretical framework across six architectures" from the Strength Finder.** This is genuine evidence and retained in Strengths.

6. **Strength about "principled conditions for when saddle-to-saddle dynamics fails."** This is genuine and retained.

## Novel Insights

None beyond the paper's own contributions. The paper's core insight — that the combination of embedded fixed points, invariant manifolds, and two distinct types of timescale separation provides a unified mechanistic explanation for simplicity bias — is itself the novel contribution, and the reviews do not surface an independent synthesis beyond it.

## Suggestions

- Revise the title and abstract to more precisely reflect the scope of the *dynamical* theory. Something like "Embedded Fixed Points, Invariant Manifolds, and Saddle-to-Saddle Dynamics Explain a Simplicity Bias in Two-Layer Linear and Quadratic Networks" would be more precise but may over-narrow. A balanced alternative: "Landscape Structure and Saddle-to-Saddle Dynamics Explain a Simplicity Bias Across Neural Network Architectures," with the abstract explicitly stating that the full dynamical analysis is worked out for two-layer linear and quadratic networks while the landscape structure holds generally.
- Add at least one architecture beyond linear/linear self-attention to the prediction validation set (Figure 2). Even a simple ReLU network with synthetic data where the target function has known spectral structure would meaningfully broaden the evidence.
- Clarify in the main text (not just the appendix) the gap between the rigorous early-phase bound (Theorem 4) and the heuristic treatment of subsequent transitions.
- Report multi-seed statistics or confidence bands for the loss curves in Figure 2.

## Score and Decision

**Calibration anchor summary:**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|-------------------------|
| KNQJtoPZmz (Simplicity Bias in Overparameterized ML) | 3.00 | 1 (weak) | Much weaker — philosophical discussion without mechanistic theory |
| kkVTeMvC9D (Understanding GD through Training Jacobian) | 3.40 | 1 (weak) | Empirically focused, no comparable theoretical framework |
| bU0JMHJ8zL (Questioning Simplicity Bias Assumptions) | 2.50 | 1 (weak) | Opinion piece, no theoretical analysis |
| OcTUquFXfx (Discovering Global Minima) | 2.60 | 1 (weak) | Unrelated problem setting |
| eQggPqESBr (Simplicity Bias and Optimization Threshold) | 5.50 | 1 (middle) | Similar theoretical ambition but narrower scope (two-layer ReLU only); this paper is stronger in breadth and theoretical framework |
| CQF8mTF7qx (Simplicity Bias of SGD via Sharpness Minimization) | 6.00 | 1 (middle) | Similar level of theoretical depth but builds on restrictive assumptions (fixed output weights, d > n); this paper has fewer restrictive assumptions and broader architecture scope |
| X7nz6ljg9Y (No Free Lunch, Kolmogorov Complexity) | 5.00 | 1 (middle) | Different framing, less mechanistic insight |
| S04xvGXjEs (Collective Variables of Neural Networks) | 6.00 | 1 (middle) | Empirically focused, no comparable theoretical results |
| 4xWQS2z77v (Exploring Loss Landscape via Convex Duality) | 8.00 | 1 (strong) | Significantly more complete theory with full proofs; this paper is below this anchor |
| AoraWUmpLU (Exploring Impact of Activation Functions in Neural ODEs) | 8.00 | 1 (strong) | Different subfield, higher mathematical rigor |
| cmfyMV45XO (Feedback Favors Generalization of Neural ODEs) | 8.00 | 1 (strong) | Different subfield |
| P7KIGdgW8S (Hölder Stability of Multiset and Graph NNs) | 8.00 | 1 (strong) | Different subfield, full mathematical rigor |
| 381QSrWdF2 (Law of Balance and Stationary Distribution of SGD) | 5.50 | 2 (narrowing) | More restrictive architecture (diagonal linear only), comparable theoretical depth |
| tMzPZTvz2H (Generalization of Scaled Deep ResNets) | 7.00 | 2 (narrowing) | More complete theory but narrower scope; comparable contribution level |
| qgWJkDiI5p (Fast Equilibrium of SGD) | 6.50 | 2 (narrowing) | Strong theory but more specialized; comparable quality |
| mkNVPGpEPm (Associative memory and dead neurons) | 6.67 | 2 (narrowing) | More specialized theory; comparable rigor |
| s1zO0YBEF8 (Dynamics of Concept Learning) | 6.50 | 2 (narrowing) | Similar theory-practice gap; comparable quality and contribution |
| jXLiDKsuDo (SimBa) | 7.50 | 2 (narrowing) | Applied paper, not directly comparable |
| 5xwx1Myosu (Expressivity with Random Weights) | 6.50 | 2 (narrowing) | Different focus, comparable theoretical contribution |
| UvpuGrd6ey (How DNNs break Curse of Dimensionality) | 6.25 | 2 (narrowing) | Different focus, comparable theoretical depth |

**Bracketing:** Round 1 placed the paper above weak anchors (3.0–3.4) and middle anchors (5.0–6.0) but below 8.0 strong anchors. Narrowest plausible range after round 1: 6.0–7.5.

**Narrowing:** Round 2 anchors include papers with comparable theoretical depth and breadth. The paper is stronger than the 5.50–6.00 anchors (which have more restrictive architectures or assumptions) and comparable to the 6.50–7.00 anchors. It is below the 7.50+ anchors which have more complete theory or broader validation. I place it at **7.0**, reflecting strong theoretical contributions slightly tempered by the framing mismatch and the heuristic nature of the later dynamical analysis.

**Score:** 7.0  
**Decision:** Accept

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>