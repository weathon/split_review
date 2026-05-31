Now I have a complete picture. Let me produce the final consolidated review.

---

## Summary

This paper introduces PH-DGN, a framework that models node-level information propagation in deep graph networks as a port-Hamiltonian dynamical system. The conservative (purely Hamiltonian) variant provides theoretical guarantees — purely imaginary eigenvalues, divergence-free vector field with constant energy, and non-vanishing backward sensitivity — that directly support long-range propagation. A port-Hamiltonian extension adds damping and external forcing, enabling controlled deviation from conservative behavior. The paper validates the approach through synthetic experiments (energy conservation, gradient non-vanishing at 1000+ layers), graph transfer tasks, graph property prediction, and the LRGB benchmark, where PH-DGN achieves competitive or state-of-the-art results without requiring global attention or positional encodings.

## Strengths

1. **Theoretical guarantees for the conservative case.** Theorems 2.1–2.3 provide rigorous proofs that the conservative PH-DGN has purely imaginary Jacobian eigenvalues (Theorem 2.1), a divergence-free vector field with constant Hamiltonian (Theorem 2.2), and a backward sensitivity matrix bounded below by 1 in any sub-multiplicative norm (Theorem 2.3). These guarantees directly address the problem of vanishing gradients in deep MPNNs and are a genuine theoretical contribution.

2. **State-of-the-art empirical results on long-range benchmarks.** On Graph Property Prediction (Table 1), PH-DGN achieves a log₁₀(MSE) improvement of 0.81 over the best baseline, with a 1.36 gap on the eccentricity task. On the Peptides-func/struct benchmarks (Table 2), PH-DGN matches or exceeds graph transformers, rewiring-based methods, and other DE-DGNs — without requiring positional encodings or global attention. The ablation PH-DGN_C (conservative-only) already outperforms all baselines, confirming that the Hamiltonian bias itself drives much of the gain.

3. **Port-Hamiltonian extension enables principled non-conservative behavior.** Equation (11) introduces damping \(D(\mathbf{q})\) and external forcing \(F(\mathbf{q},t)\) within the same port-Hamiltonian formalism. The ablation comparison (PH-DGN vs. PH-DGN_C) shows that the full model outperforms the purely conservative version on tasks where selective forgetting is beneficial (e.g., distance-counting tasks), while the conservative variant suffices on others. This demonstrates the practical value of the port-Hamiltonian generalization.

4. **General formulation compatible with any aggregation function.** The framework allows \(\Phi_{\mathcal{G}}\) in Equation (5) to be any permutation-invariant neighborhood aggregation (Section 2), and the paper demonstrates this with both GCN aggregation and a custom linear aggregation (Eq. 6). This makes PH-DGN a plug-in inductive bias rather than a single monolithic architecture.

5. **Clean numerical verification at extreme depths.** Section 3.1 validates energy conservation (Figure 2a) and the BSM lower bound (Figures 2b–2c) empirically on a Carbon-60 graph with up to 1000 layers, directly confirming that the theoretical guarantees translate to practical non-vanishing gradients.

## Weaknesses

### Fatal
None.

### Major
1. **Theorem 2.4's upper bound argument does not support the conclusion drawn.** The paper states that PH-DGN's upper bound on node-to-node sensitivity is "at least \(N^\ell\) times bigger" than MPNN's, and concludes that this "holds the capability of PH-DGN to perform long-range propagation effectively" (line 132). A larger *upper* bound does not imply better propagation — a looser bound may simply be more vacuous. The relevant quantities for propagation are *lower* bounds (which the paper supplies in Theorem 2.3 and Theorem A.2). Using the upper bound comparison as a headline theoretical argument oversells this result. This does *not* invalidate the empirical findings or the lower-bound results, but it weakens the theoretical narrative. The paper should either reposition this as a stability/instability bound or drop the claim that it supports long-range capability.

### Minor
1. **Experimental comparisons do not fully control for the confound of depth and weight-sharing vs. architectural bias.** PH-DGN uses weight sharing (via ODE discretization) and naturally supports many layers. While the paper notes that "DE-DGN baselines are implemented with weight sharing" (Table 1 caption) and includes A-DGN and other ODE-based competitors, the effective number of layers and parameter counts are not reported in the main text. A controlled ablation — comparing PH-DGN_C against a non-Hamiltonian ODE-based DGN with the same weight sharing, discretization scheme, and layer count — would isolate whether the Hamiltonian *structure* (rather than ODE depth alone) drives the improvement.

2. **Theoretical scope could be framed more precisely.** The abstract claims the paper "reconciles under a single theoretical and practical framework both non-dissipative long-range propagation and non-conservative behaviors" and "provides theoretical guarantees on information conservation in time." Theorems 2.1–2.3 and their guarantees (energy conservation, non-vanishing sensitivity) apply strictly to the conservative case with driving forces set to null (Eq. 5). The full port-Hamiltonian framework describes both regimes, but the theoretical guarantees do not extend to the non-conservative setting. The paper acknowledges this in several places ("when driving forces are null," "when pure conservative dynamic is employed") but the broader framing in the Abstract and Introduction occasionally suggests the guarantees apply to the framework as a whole. Adding an explicit statement that the guarantees hold for the conservative subsystem, and discussing how damping degrades these properties, would tighten the presentation.

### Trivial
1. **The BSM lower bound claim for "all sub-multiplicative norms," while technically correct, is presented without justification.** The paper states the bound holds for all sub-multiplicative norms (line 114). This is true because the Jacobian of a Hamiltonian flow is symplectic, symplectic matrices have reciprocal eigenvalue pairs implying spectral radius ≥ 1, and any matrix norm is at least the spectral radius. The paper does not mention this reasoning, which may confuse readers unfamiliar with symplectic geometry. A brief footnote or clarifying sentence would help.

## Nice-to-Haves
1. Add a controlled ablation comparing PH-DGN_C against a non-Hamiltonian ODE-based DGN with identical weight sharing, discretization (symplectic Euler), and layer count. This would directly isolate whether the Hamiltonian structure (as opposed to ODE depth) drives the gain. The inclusion of A-DGN partially addresses this, but the comparison would be cleaner with a purpose-built control.

2. Report effective number of layers (discretization steps) and parameter counts for each model in the experiments, as is standard in ODE-based DGN papers. This would directly address the confound concern about depth vs. architectural bias.

3. Discuss when the conservative inductive bias is sufficient and when non-conservative components help. The paper notes that PH-DGN outperforms PH-DGN_C on property prediction but differences are small on LRGB — a brief discussion of this pattern would deepen the analysis.

## Removed Points
These points from the inputs are flagged to be removed; treat them with caution:

1. **Criticism about Figure 3 missing error bars** — The extracted PDF does not render figures; the caption states "test mean-squared error (and std. dev.)," which implies they were plotted. Cannot verify from parsed text. Removed.

2. **Complaints about hyperparameter details not in main text / deferred to appendix** — The instructions explicitly state that appendix content is stripped by the parser but present in the original submission. This is standard practice. Removed.

3. **Complaints about garbled/truncated text ("We observe that Theorem 2.3).")** — This is a PDF parsing artifact, not an author error. Removed.

4. **Complaint about Equation (4)-to-(5) derivation omitted from main text** — Derivation is in the appendix (which is standard and stripped by the parser). Removed.

5. **Complaint about discretization scheme not sketched in main text** — The scheme (Symplectic Euler) is referenced; details are in the appendix. Standard practice. Removed.

6. **Complaint about duplicated "(i)" label in contribution list** — Formatting/minor typesetting artifact. Removed.

7. **Strength Finder's generic/superficial praise** (e.g., "this paper addressed an important problem," statements without specific citation or concrete content) — These are genuine strengths of the paper but expressed generically in the Strength Finder. They overlap with the evidence-backed strengths already listed above. Removed.

## Novel Insights
None beyond the paper's own contributions. The review process surfaces one useful observation not explicit in the paper: the port-Hamiltonian framing naturally resolves a tension in existing DE-DGN design — methods like A-DGN (anti-symmetric) and GraphCON (oscillatory) each achieve non-dissipation through different inductive biases, but neither provides a principled way to *controllably* introduce non-conservative behavior. PH-DGN's port-Hamiltonian formalism subsumes both the conservative regime (subsuming Hamiltonian-only methods like HamGNN/HANG) and the non-conservative regime (via damping and forcing) under a single mathematical structure. This is a genuinely useful unification. However, the real test of whether the port-Hamiltonian structure adds value *beyond* the ODE discretization itself would require the controlled ablation mentioned in Nice-to-Haves (comparing against a non-Hamiltonian ODE with identical discretization), which the paper does not currently include.

## Suggestions
1. **Reposition Theorem 2.4.** Drop the argument that a larger upper bound implies better long-range propagation. Instead, note that the upper bound characterizes worst-case sensitivity growth — and the *lower bound* (Theorem 2.3) is the relevant metric for non-vanishing gradients. Use Theorem 2.4 only to show that PH-DGN's sensitivity does not grow pathologically faster than MPNN's.

2. **Add an explicit scope statement** at the start of Section 2 stating that Theorems 2.1–2.3 apply to the conservative subsystem (Eq. 5, D=0, F=0) and that the full framework inherits these properties only approximately when non-conservative terms are active. Provide a qualitative discussion (or bound) of how damping degrades energy conservation.

3. **Add a controlled ablation** comparing PH-DGN_C against a purpose-built non-Hamiltonian ODE-based DGN with identical weight sharing, symplectic Euler discretization, and layer count. This would cleanly separate the effect of the Hamiltonian bias from ODE depth.

4. **Report effective layers and parameter counts** for each model in Tables 1–2 to address the fairness concern directly.

## Score and Decision

**Originality**: High. PH-DGN is the first to use port-Hamiltonian dynamics (rather than purely Hamiltonian or anti-symmetric dynamics) as a message-passing framework for graphs, providing a principled unification of conservative and non-conservative regimes.  
**Importance of research question**: High. Long-range propagation is a well-recognized bottleneck in graph neural networks, and principled solutions with theoretical guarantees are valuable.  
**Claims support**: Good, with one clear overstatement. The theoretical lower-bound results are solid; the upper-bound argument (Theorem 2.4) is oversold. The empirical support is strong across multiple benchmarks.  
**Soundness of experiments**: Strong. Multiple benchmarks (synthetic, transfer, property prediction, LRGB), ablations (PH-DGN_C vs. PH-DGN), and comparisons to relevant baselines including other DE-DGNs. The main gap is the absence of a controlled ablation to isolate the Hamiltonian bias from ODE depth.  
**Clarity**: Good. The paper is well-structured and the core ideas are clearly explained. A few framing issues (theoretical scope, upper bound argument) could be sharpened.  
**Value to community**: High. The framework provides a theoretically grounded new design principle for DE-DGNs, with practical gains on challenging benchmarks. The port-Hamiltonian perspective opens a new direction for controllable information propagation in graphs.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>