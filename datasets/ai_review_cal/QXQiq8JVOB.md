- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5
Now I have all the information needed. Let me construct the consolidated review.

---

## Summary

This paper develops a Hamiltonian mechanics framework for understanding feature learning in Leaky ResNets. It derives a Lagrangian formulation over representation paths \(A_p\), decomposing the objective into a kinetic energy (penalizing fast changes) and a potential energy driven by the "Cost of Identity" (COI), which measures representation dimensionality. The key insight is that for large effective depth \(\tilde{L}\), the Hamiltonian reveals a separation of timescales: representations rapidly jump from high-dimensional inputs to a low-dimensional bottleneck, evolve slowly inside it, then jump to outputs. This explains the Bottleneck structure observed in deep networks and motivates an adaptive layer discretization scheme.

## Strengths

1. **Lagrangian/Hamiltonian reformulation of Leaky ResNets (Sections 1.3, 1.5):** The paper derives a clean continuous formulation where optimal weight matrices are expressed in terms of activations, leading to a Lagrangian \(\frac{\tilde{L}}{2}\|A_p\|_{K_p}^2 + \frac{1}{2\tilde{L}}\|\partial_p A_p\|_{K_p}^2\) and a conserved Hamiltonian \(\mathcal{H}\). This provides a principled physics-inspired framework for analyzing representation geodesics and is clearly connected to prior work (Owhadi et al. 2020), with the novelty being the large-\(\tilde{L}\) analysis.

2. **Stable energy decomposition theorem (Theorem 1):** The paper provides a rigorous bound (stated in full) that overcomes the instability of pseudo-inverses by replacing \(K_p^+\) with \((K_p+\gamma I)^+\). The theorem shows that for large \(\tilde{L}\), the Hamiltonian is close to the minimal regularized COI along the path, and the derivative norm scales as \(\tilde{L}\) times the "extra-COI" — a direct mathematical characterization of the separation of timescales. This is the paper's core theoretical result.

3. **Proposition on stable minima (Proposition 2):** Proves that stable local minima of the COI are non-negative and equal to the rank, with a detailed proof in the main text (lines 341–357) using a perturbation argument. This is important because it links the COI to an integer dimension at the minima the network actually reaches.

4. **Symmetry analysis (Section 1.2):** Cleanly demonstrates that changing \(\tilde{L}\) is equivalent to scaling the integration range or scaling the outputs. This justifies interpreting \(\tilde{L}\) as effective depth and connects non-leaky ResNets (trained on cross-entropy with growing outputs) to the leaky case — a useful theoretical observation.

5. **Empirical illustration of bottleneck structure (Figure 1):** For increasing \(\tilde{L}\), the Hamiltonian and COI approach the true rank \(k^*=3\) from below and above respectively, while kinetic energy concentrates near input/output layers. This provides concrete experimental support for the predicted separation of timescales.

## Weaknesses

### Fatal
None.

### Major

1. **The proof sketch for Proposition 1 (COI \(\ge\) stable rank) is mathematically incomplete as presented.** The proof states that the minimum of \(\min_{\|B\|_F \le \|A\|_F} \|AB^+\|_F^2\) is attained at \(B = \frac{\|A\|_F}{\sqrt{\|A\|_*}}\sqrt{A}\) and "yields the result." However, \(\sqrt{A}\) is ambiguous for non-square or non-PSD matrices, the constraint set for \(B\) is not fully characterized, and the claimed equality to \(\|A\|_*^2/\|A\|_F^2\) is asserted without derivation. The result itself may be true, but the argument is not a valid proof. Since this proposition is used to motivate the COI as a dimensionality measure, the gap is significant — though the paper's main theoretical contributions (Theorem 1, Proposition 2) do not depend on this bound.

2. **The adaptive discretization experiments lack basic validation practices.** The "small but consistent" test error improvement (Figure 2) is presented without error bars, number of seeds, or statistical tests. For a method the paper presents as a concrete application of the theory, this is insufficient to establish practical benefit. Additionally, there is no ablation varying key parameters (e.g., the \(\gamma\) in the stable decomposition) to verify the claimed mechanism drives the improvement.

### Minor

1. **Theorem 1's connection to the separation-of-timescales narrative is stated but not fully unpacked.** The bounds involve \(\ell_{\gamma,\tilde{L}}\) (a path length under the same regularized norm) and \(\gamma c\), and the interpretation as a rigorous separation of timescales requires choosing \(\gamma = \gamma(\tilde{L})\) and arguing that \(\ell_{\gamma,\tilde{L}}\) is well-behaved. The paper gestures at this (e.g., "choosing e.g. \(\gamma = \tilde{L}^{-1}\)") but does not provide a concrete worked example or verify the required conditions for a nontrivial class of geodesics. The intuition is clear; the rigorous bridge could be tighter.

2. **The adaptive \(\rho_\ell\) update is self-referential:** computing \(c_\ell = \|A_\ell - A_{\ell-1}\|/(\rho_\ell \|A_p\|)\) requires knowing \(\rho_\ell\), which is what one is trying to compute. The paper notes it "can be done at every training step or every few training steps," but the stability and convergence properties of this iterative scheme are not analyzed. This limits the practical deployability of the method.

3. **No comparison to standard Neural ODE adaptive solvers.** Given the continuous formulation, adaptive ODE solvers (e.g., dopri5) are a natural baseline for the discretization scheme. The paper compares only equidistant and hand-designed irregular schemes.

### Trivial
None.

## Nice-to-Haves

- A diagnostic experiment explicitly demonstrating that adaptive \(\rho_\ell\) concentrates steps where \(\|\partial_p A_p\|_{(K_p+\gamma I)}\) is large, confirming the mechanism rather than only measuring test error.
- A small-scale (e.g., 2D) exactly solvable toy model where the separation of timescales can be verified analytically.
- Brief discussion of the computational overhead of the adaptive update relative to the forward/backward pass.

## Removed Points

These points are flagged to be removed from the harsh critic's analysis; treat them with caution:

- **"Theorem 1 stated without proof (deferred to an appendix that is not available)"** — Removed per rule: appendix proofs are stripped by the parser; they exist in the original submission.
- **"Proofs of Propositions 2, 3, 6 (stable path positive) are absent"** — Proposition 2 has a full proof in the main text (lines 341–357). Removed as factually incorrect. Others are appendix-deferred.
- **"The Hamiltonian reformulation is not new, and the paper does not show that it yields new rigorous results"** — The paper explicitly acknowledges prior work (Owhadi et al. 2020) and identifies its novel contribution: the large-\(\tilde{L}\) analysis connecting the Hamiltonian to COI and separation of timescales, culminating in Theorem 1. The critic's framing ignores this clear scope statement.
- **"The experimental component is too weak to support the claimed practical benefit"** — This is over-pitched as a fatal flaw. The paper's primary contribution is theoretical; the adaptive discretization is presented as an "inspiration" from the theory, and the empirical results are described as "small but consistent." The claim is modest, so the weakness is at most minor, not structural.
- **"No analysis of computational cost"** — Useful but not a core weakness for a theory paper.
- **"The synthetic experiments use only random networks"** — Appropriate for illustrating the theoretical phenomenon; requesting real-data experiments is scope creep for this type of paper.
- **"No error bars, statistical tests" for Figure 1** — Figure 1 is a qualitative illustration of the bottleneck phenomenon, not a competitive benchmark. Error bars would be nice but are not standard for this kind of diagnostic plot.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's strengths (Hamiltonian framework, Theorem 1, COI concept) and weaknesses (sketchy proof for one proposition, light experimental validation of the adaptive scheme). The harsh critic's framing of structural theoretical unsoundness is not supported by a careful reading: the paper acknowledges the limitation of the decomposition (Remark, lines 278–298) and addresses it via Theorem 1. The core theoretical narrative is coherent even if one particular proof is sloppy and some connections could be tightened.

## Suggestions

1. **Fix the proof of Proposition 1** by either (a) providing a correct, rigorous argument (e.g., using known inequalities relating \(\|A\sigma(A)^+\|_F\) to the stable rank via the SVD), or (b) downgrading it from a "Proposition" to an "Observation" and noting it is heuristic.
2. **Provide a concrete example** (e.g., 2-layer linear network with \(\sigma=id\) and explicit rank) where the stable energy decomposition and separation of timescales can be verified analytically, to ground the asymptotic intuition.
3. **Add error bars and seed counts to the adaptive discretization experiments** (Figure 2), or explicitly state that the results are from a single illustrative run and reposition the scheme as speculation rather than a demonstrated method.
4. **Clarify the self-consistency of the adaptive \(\rho_\ell\) update** — state the fixed-point equation being solved and describe the iterative procedure's convergence in practice.
5. **Define \(\sqrt{A}\) for general matrices** or replace it with a well-defined operation (e.g., using the SVD: the positive semidefinite square root of \(AA^T\)).
