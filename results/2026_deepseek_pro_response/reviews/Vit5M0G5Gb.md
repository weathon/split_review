Now I have a clear calibration picture. Let me finalize the review.

**Round 1 bracket**: The paper is clearly above the 2.0-3.5 weak anchors and below the 8.0 strong anchors. Compared to middle anchors at 5.50-6.00 (all rejected, narrower scope, more restrictive assumptions), this paper is more ambitious and has stronger contributions.

**Round 2 narrowing**: Against accepted papers at 7.00-7.50, this paper is comparably ambitious but has a more significant gap between claims and proofs. The 7.00 EOS paper also had overclaiming issues but was more rigorous within its core scope. The 7.33 scaling laws paper was narrow but fully rigorous.

**Final assessment**: Score = 6.5. The paper's static framework (Theorems 1, 3) and the identification of two distinct dynamical mechanisms are genuine contributions with strong empirical validation. However, the dynamics analysis (Section 5) is limited to early-phase approximations with heuristic extensions for subsequent transitions, and the abstract/title overclaim relative to what's proved. This places it above the rejected 6.0 papers but below the clearly accepted 7.0+ papers. Borderline accept/reject.

---

## Summary
This paper presents a unified theoretical framework for saddle-to-saddle (stage-like) learning dynamics across fully-connected, convolutional, and attention-based neural network architectures. The framework consists of three parts: (1) a structural analysis showing that fixed points of narrower networks embed as saddles in wider networks (Theorem 1), with four weight-configuration categories depending on activation function properties; (2) invariant manifold results showing that weight relationships corresponding to lower effective width are preserved under gradient flow (Theorem 3); and (3) a dynamics analysis identifying two distinct timescale-separation mechanisms — data-induced (linear φ) and initialization-induced (quadratic φ). The theory generates testable predictions about the effects of width, data distribution, and initialization on learning dynamics, validated through simulations (Figures 1–2).

## Strengths
- **Unified architectural abstraction (Eq. 1):** The paper frames fully-connected, convolutional, and self-attention layers in a single mathematical formulation where a "unit" maps to a hidden neuron, kernel, or attention head respectively. This enables Theorems 1 and 3 to be stated and proved once for all architectures, giving the notion of "simplicity as number of effective units" a rigorous, architecture-agnostic definition.

- **Theorem 1's four-case characterization of embedded fixed points:** The theorem extends Fukumizu & Amari (2000) with cases (iii) homogeneity-based and (iv) linearity-based constructions that are novel and empirically relevant — Figure 1B–G shows that the weight structures at intermediate plateaus map cleanly onto Equations (5)–(7), with Equation (4) saddles avoided during learning.

- **Data-induced vs. initialization-induced timescale separation:** The paper identifies two distinct dynamical mechanisms — spectral gaps of Σ_yz driving direction-wise separation in linear networks (Theorem 4), and a rich-get-richer process driving unit-wise separation in quadratic-φ networks (Proposition 5). This distinction generates differential, falsifiable predictions validated in Figure 2: width scaling affects self-attention but not linear FC networks (2A), and κ=0 eliminates plateaus in linear nets but only shortens them in self-attention (2B).

- **Theorem 3's invariant manifolds as the mechanistic bridge:** The invariant manifold result — that weight relationships like equal weights, proportional weights, zero weights, and linear dependence are preserved under gradient flow — connects static landscape analysis to dynamic trajectories, giving a precise mechanism for how a perturbation breaking one constraint transitions the trajectory from one effective-width manifold to the next.

- **Predictive validation across four manipulated factors (Figure 2):** The theory generates concrete, non-obvious predictions about width, data spectrum, initialization structure, and initialization scale, all confirmed. The large-low-rank initialization regime (2C) — where saddle-to-saddle dynamics still occurs despite starting far from a saddle — is a particularly novel observation that challenges the common assumption that small initialization near a saddle is required for stage-like learning.

- **Clearly stated boundary conditions:** Section 7 explicitly identifies when saddle-to-saddle dynamics should *not* occur (tanh networks, large isotropic initialization), and the Taylor-expansion heuristic (Section 5, final paragraph) provides a principled way to classify which nonlinear activations will exhibit the phenomenon.

## Weaknesses

### Fatal
None.

### Major
- **Gap between claimed and proved dynamics:** The abstract and introduction frame the paper as providing a dynamical explanation of the full saddle-to-saddle process. However, Section 5's rigorous analysis is limited to *early-phase* dynamics near zero initialization: Theorem 4 covers the approach to the first rank-r saddle for linear networks, and Proposition 5 covers the first unit's growth for quadratic networks. The analysis of subsequent saddle-to-saddle transitions (Eq. 12 for linear, the paragraph after Proposition 5 for quadratic) is heuristic, as the paper itself acknowledges ("we develop heuristic arguments," line 118). The title and abstract do not adequately reflect this limitation. This matters because the paper's central claim — that it *explains* saddle-to-saddle dynamics — requires the dynamics to be characterized beyond just the first transition.

- **ReLU and convolutional dynamics claims rest on empirical demonstration, not analysis:** The abstract states that "ReLU networks learn solutions with an increasing number of kinks" and "convolutional networks learn solutions with an increasing number of convolutional kernels" as if these are derived results. The theoretical framework provides scaffolding for these architectures through homogeneity (Theorems 1(iii) and 3(iii)), but the dynamics analysis in Section 5 treats only linear and quadratic φ analytically. The ReLU and convolutional results in Figure 1(D,E) are empirical observations consistent with the framework, not consequences of a dynamical proof. The abstract overstates what is analytically established.

### Minor
- **Architectural vs. functional simplicity for non-linear φ:** The paper defines simplicity as "expressible with fewer units," which is a weight-space property. For linear networks, effective width maps cleanly to functional rank. For quadratic/self-attention networks, the functional meaning of a given effective width is less characterized — what class of input-output maps can a one-head linear self-attention network represent? This limits the interpretability of the simplicity-bias claim for non-linear architectures, though it does not invalidate the framework.

- **Limited data spectrum in Figure 2B:** The power-law setup uses only 3 singular values (n=1,2,3), which limits the generality of the data-distribution claims. Real data can have richer singular value spectra that might interact with the dynamics in ways not captured here. This is a scope limitation rather than a flaw in what is tested.

### Trivial
- **Notation ambiguity in Eq. (9):** The subscript "ii" on (Σ_{yz} − W Σ_{zz})_{ii} is unclear — Σ_{yz} − W Σ_{zz} is a rectangular matrix, so diagonal indexing is ambiguous. This should be clarified for readability.

## Nice-to-Haves
- Proving (or formalizing) one complete saddle-to-saddle transition beyond the early phase would substantially close the gap between the static framework and the dynamical claims.
- Quantitative metrics (plateau duration measurements, correlation with theoretically predicted quantities) rather than purely visual inspection of loss curves would strengthen the empirical validation.
- A brief discussion of how finite learning rates affect the saddle-to-saddle picture, since the analysis is in the gradient flow limit.

## Removed Points
These points are flagged to be removed, treat them with caution.

- *Harsh critic's claim about missing Figures 3-5 and Appendix I discussion:* The paper references these figures and the appendix in the main text (lines 21-22). The appendix is stripped by the parser but exists in the original submission. Per review guidelines, criticisms about missing appendices or appendix content are removed.

- *Harsh critic's framing of the dynamics gap as "structural" and "does not establish what the paper claims to establish":* This is reframed more precisely. The static analysis (Theorems 1, 3) is rigorous and does establish the structural prerequisites. The issue is specifically with the dynamical analysis, which is captured in the Major weakness above with appropriate nuance.

- *Harsh critic's concern about self-attention being restricted to linear self-attention as a major hidden flaw:* The paper is explicitly transparent that the analysis is for linear self-attention throughout the body text (lines 27, 122, 170, 200, 208). The abstract says "self-attention models" but the introduction immediately clarifies "linear self-attention." This is noted as a minor imprecision in the abstract rather than a hidden limitation.

- *Harsh critic's claim about "simplicity" being architectural rather than functional as a structural flaw:* Retained as a minor weakness rather than major. The paper's definition is internally consistent and the connection between architectural and functional simplicity is direct for linear networks.

- *Strength Finder's "Broad empirical coverage" as a standalone strength:* Merged into the evidence for Theorem 1 and the predictive validation.

- *Harsh critic's point about the claim that tanh networks "probably do not have saddle-to-saddle dynamics" following from static rather than dynamical properties:* The paper's reasoning in Section 7 (lines 222-226) is that tanh lacks an invariant manifold for rank-one weights (condition (i) fails), which means the escape path from any saddle would not follow an invariant manifold — this is a structural, not dynamical, argument, and the paper presents it as such. The harsh critic's objection is slightly off; the paper's logic is consistent.

## Novel Insights
The paper's key novel insight is the identification of *two distinct dynamical mechanisms* for timescale separation — data-induced (via spectral gaps) and initialization-induced (via rich-get-richer) — and the demonstration that these two mechanisms generate *differentially testable predictions* about how width, data, and initialization affect learning. This goes beyond prior work that treated these phenomena separately and provides a unified lens. The finding that large low-rank initialization still produces saddle-to-saddle dynamics (Figure 2C) challenges the common assumption that small initialization near a saddle is required for stage-like learning, and adds meaningful nuance to the lazy-vs-feature-learning dichotomy.

## Suggestions
- Reframe the abstract and introduction to more accurately reflect which parts of the theory are proved (embedded fixed points, invariant manifolds, early-phase dynamics) vs. which are heuristically argued (subsequent saddle-to-saddle transitions). A title like "A Structural Framework for Saddle-to-Saddle Dynamics and Simplicity Bias" would better match what is actually delivered.
- For the ReLU and convolutional cases, either (a) develop the dynamics analysis using the homogeneity properties that are already established in Theorems 1(iii) and 3(iii), or (b) explicitly mark these as empirical validations of the structural framework rather than derived dynamical results.
- Add quantitative measurements of plateau duration in Figure 2 experiments and correlate them with theoretically predicted quantities (singular value gaps, initial weight gaps).

---

## Calibration Summary

**Round 1 — Bracketing:**
- Weak band (<3.5): "Discovering Global Minima" (2.60), "Understanding GD through Training Jacobian" (3.40), "Grokking through Dynamical Systems" (2.00), "Continuous-depth Networks via Ricci Flows" (2.33) — all rejected, all clearly below this paper.
- Middle band (3.5-7.5): "Simplicity Bias and Optimization Threshold" (5.50, Reject), "Simplicity Bias of SGD via Sharpness Minimization" (6.00, Reject), "Dichotomy of Early and Late Phase Implicit Biases" (6.00, Accept), "Collective Variables of Neural Networks" (6.00, Reject) — this paper is stronger than these in ambition, scope, and contribution quality.
- Strong band (>7.5): "Loss Landscape of Regularized Neural Networks via Convex Duality" (8.00, Accept) — fully rigorous, complete theory; this paper falls below this anchor due to the dynamics gap.

**Round 2 — Narrowing (5.5-8.0):**
- "Neural Scaling Laws in Two-Layer Networks with Power-Law Data Spectra" (7.33, Accept) — rigorous but narrow scope; this paper is broader but less complete dynamically.
- "Learning Dynamics of Deep Matrix Factorization Beyond EOS" (7.00, Accept) — rigorous for linear nets but overclaims about nonlinear; comparable in having a claims-vs-proofs tension.
- "Implicit Bias of Mirror Descent" (7.33, Accept) — rigorous within its setting.
- "Formation of Representations in Neural Networks" (7.50, Accept) — broad hypothesis with empirical support.
- "Understanding Optimization with Central Flows" (7.00, Accept) — novel framework, good empirical validation.

**Final score rationale:** This paper sits between the rejected 6.00 papers (narrower, fewer contributions) and the accepted 7.00 papers (more rigorous within scope). It has more ambition and broader architectural coverage than any of the 6.00-7.00 anchors, and its static framework (Theorems 1, 3) is a genuine contribution. However, the gap between claimed and proved dynamics is a real limitation that prevents it from reaching the 7.0+ tier where claims are more fully substantiated. Score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Reject</decision>