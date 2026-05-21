Now let me write the consolidated review. I have enough information from the calibration to determine the score.

**Round 1 Bracket:** Based on the calibration, the paper sits well above the weak anchors (2.0–3.0) and above the 6.0 anchor (rejected sharpness paper). It is comparable to the 7.00–7.33 range of accepted posters/spotlights. My initial bracket is 6.5–7.5.

**Round 2 Narrowing:** Reading the full reviews of ogKE7LcvW6 (avg 7.00, Accept Poster) and J4Dvxv7WnG (avg 7.00, Accept Poster), both share similar heuristic dynamics analysis issues. The current paper covers more architectures, has more rigorous landscape theorems, and makes testable predictions. It is somewhat stronger than these 7.00 anchors but not as strong as the 7.75 anchor (more rigorous proofs). So 7.0 is the right score — comparable to the upper end of the accepted poster range.

---

## Summary

This paper proposes a unified theoretical framework for understanding the "simplicity bias" in neural networks — the phenomenon where networks learn solutions of progressively increasing complexity during training. The framework combines three components: (1) a rigorous theorem showing fixed points of narrow networks are embedded as saddles in wider networks (Theorem 1), (2) a theorem identifying invariant manifolds that correspond to effectively narrower networks and connect these saddles (Theorem 3), and (3) a heuristic dynamics analysis showing that timescale separation — either between directions (linear case, data-driven) or between units (quadratic case, initialization-driven) — steers trajectories along these invariant manifolds. The theory is validated across six architectures (linear, ReLU, convolutional, quadratic, linear self-attention) and makes testable predictions about the effects of width, data distribution, and initialization on learning dynamics (Figure 2).

## Strengths

- **Rigorous embedded fixed-point and invariant-manifold theorems (Theorems 1, 3) with novel constructions.** Theorem 1 extends prior work (Fukumizu & Amari 2000) with new constructions (Equations 6, 7) that are crucial for connecting the fixed-point hierarchy to the specific saddles visited during learning. Theorem 3 identifies invariant manifolds that correspond to effectively narrower networks and exist across all architectures covered by Equation (1). These results are rigorous and independently valuable.

- **Identification of two distinct dynamical mechanisms for saddle-to-saddle dynamics.** The paper cleanly disentangles data-induced timescale separation (linear case: Theorem 4, driven by singular value gaps in Σ_yz) from initialization-induced timescale separation (quadratic case: Proposition 5, driven by random initialization differences between units). This distinction yields non-trivial, testable predictions that successfully differentiate the two mechanisms (Figure 2A–B).

- **Novel, architecture-specific predictions validated by simulation.** Figure 2 tests three non-trivial predictions: (A) widening shortens plateaus in linear self-attention but not in linear networks; (B) equalizing singular values eliminates plateaus in linear networks but not linear self-attention; (C) initializing near an invariant manifold but away from saddles still produces saddle-to-saddle dynamics. These predictions distinguish the two mechanisms and would not follow from existing theories.

- **Unification across six architectures in a single framework.** Figure 1B–G demonstrates saddle-to-saddle dynamics and consistent weight-structure categories for linear FC, linear convolutional, ReLU FC, ReLU convolutional, linear self-attention, and quadratic networks, mapped to the three fixed-point types from Theorem 1. This provides concrete evidence for the framework's breadth.

- **Honest delineation of scope and failure modes.** Section 7 explicitly discusses conditions for saddle-to-saddle dynamics and gives concrete counterexamples (tanh violates condition (i); large isotropic initialization violates condition (ii)). This turns a potential weakness into a strength by clearly circumscribing the theory's domain.

## Weaknesses

### Major

- **The core dynamical explanation is heuristic where it needs to be most precise.** The paper's central thesis — that timescale separation steers trajectories along invariant manifolds to produce saddle-to-saddle dynamics — is supported by rigorous analysis of *approximate* systems (linearized dynamics in Theorem 4; simplified quadratic dynamics in Proposition 5) but no formal bound is provided on how close the true trajectory stays to these approximations over the duration of a saddle transition. The paper is honest about this (Section 4 explicitly says "we develop heuristic arguments"), but this means the "explanation" in the title is more a plausible mechanism supported by simulations than a proven theorem. The mismatch between the rigor of Sections 3–4 and the heuristic nature of Section 5 is the paper's most significant limitation.

- **Simulations lack statistical reliability measures.** Figure 2 shows only single runs with no error bars or multiple trials. For claims about the effect of random initialization (Quadratic case, where the mechanism depends on the relative ordering of randomly sampled initial weights), showing that the phenomena are robust across seeds is essential. Without variance estimates, it is unclear whether the observed patterns are reproducible or coincidental.

### Minor

- **Dynamics analysis is limited to two-layer networks.** While Theorems 1 and 3 apply to deep networks, the dynamics analysis in Section 5 covers only two-layer networks. The treatment of deep networks (Section 7) is explicitly conjectural and references figures in the (stripped) appendix. This is a clear limitation that the paper acknowledges, but it restricts the scope of the "unified explanation" claim.

- **No direct comparison with alternative explanations of simplicity bias.** The paper discusses related work but does not systematically compare its framework to alternative theories (spectral bias, frequency bias in the Fourier domain, NTK-based accounts of learning order). Such a comparison would help position the contribution relative to existing mechanistic explanations.

### Trivial

- None worth listing.

## Nice-to-Haves

- Adding error bars or multiple-seed visualizations to Figure 2 would substantially increase confidence in the predictions.
- A formal bound (e.g., via Gronwall-type arguments) on the distance between the true gradient flow trajectory and the approximate linearized dynamics for the linear case would significantly strengthen the core contribution, even if only for the first escape from zero.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic: "Figures 3–5 are not available" / "Deeper networks in Figures 3–5 are not available."** These figures exist in the original submission; the PDF parser stripped appendix content. Not a valid weakness.

- **Harsh critic: "Paper does not discuss the effect of SGD, finite learning rates, or weight decay."** Gradient flow is the paper's stated framework (Equation 3, "Gradient flow captures the behavior of gradient descent in the limit of a small learning rate"). Criticizing absence of effects outside the paper's scope is inappropriate.

- **Harsh critic: "The claim that saddle-to-saddle dynamics 'has been hypothesized to be universal' is not followed up."** The paper addresses this by showing it holds for six architectures and discussing conditions under which it fails. This is a reasonable level of follow-up.

- **Harsh critic: "The prediction about width in the linear case (no effect) is somewhat trivial given the analysis."** This describes a straightforward consequence, which is exactly what a good prediction should be. Triviality is a subjective assessment, not a weakness.

- **Harsh critic: "Single runs" claim about the dynamics.** This is kept as a weakness (see Minor section) since it's a real issue. However, the critic's framing as a fatal flaw is excessive — many theory papers show qualitative behavior without error bars.

- **Strength points about "Unification across six architectures" and "Conjectures for deep networks."** These are kept as strengths because they are concrete and specific.

## Novel Insights

The harsh critic's framing of the dynamics analysis as heuristic rather than rigorous is accurate and important, but it does not diminish the paper's substantial contributions. The more interesting observation — which neither reviewer fully developed — is that the paper's framework can be read as identifying a *general structural condition* (embedded fixed points connected by invariant manifolds) that is *necessary* for saddle-to-saddle dynamics, plus two *sufficient* mechanisms (direction-based and unit-based timescale separation) that realize this structure in specific architecture classes. This decomposition into necessary structure + sufficient mechanisms is the paper's true intellectual contribution, and future work could target either missing sufficiency (other mechanism classes) or tighter necessity (proving that saddle-to-saddle dynamics implies embedded fixed points).

## Suggestions

- For the camera-ready version, consider adding at least one experiment with multiple random seeds and error bars for the predictions in Figure 2, especially panels A (width effect on quadratic networks) and B (data distribution), where randomness in initialization is central to the mechanism.
- To strengthen the core contribution, add a formal bound for the linear case: prove that the distance between the true trajectory and the rank-\(r\) invariant manifold remains \(O(\epsilon)\) over the time interval \([0, T]\) where \(T\) is the escape time from the saddle. This can likely be done using the explicit solution structure and Gronwall's inequality.
- Include a brief discussion (1–2 paragraphs) comparing the framework to spectral bias / frequency bias explanations and the NTK-based account of learning order, to help readers position the contribution.

## Score and Decision

**MY FINAL SCORE:** <score>7.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>