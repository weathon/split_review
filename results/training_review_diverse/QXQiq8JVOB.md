## Summary

This paper studies Leaky ResNets through the lens of representation geodesics — continuous paths in representation space from input to output. It derives a Lagrangian/Hamiltonian reformulation that decomposes the objective into a kinetic energy (favoring small layer-to-layer changes) and a potential energy based on the "Cost of Identity" (COI, a measure of representational dimensionality). The central claim is that for large effective depth \(\tilde{L}\), a separation of timescales emerges: the network spends most layers in a low-dimensional bottleneck with rapid high-dimensional jumps at the beginning and end. This insight motivates an adaptive layer-spacing scheme. The paper is a **theoretical/empirical paper** aiming to bridge an elegant mathematical framework with architectural insights.

## Strengths

1. **Hamiltonian reformulation avoids the unstable pseudo-inverse.** The paper derives a conserved Hamiltonian \(\mathcal{H}(A_p,B_p)=\frac{\tilde{L}}{2}\|B_p\sigma(A_p)^T\|^2-\tilde{L}\,\mathrm{Tr}[B_pA_p^T]\) that dispenses with the pseudo-inverse \(\sigma(A_p)^+\) required by the Lagrangian formulation (Section 1.4, lines 429–435). This is a genuine technical improvement that enables tractable analysis of the separation of timescales.

2. **Theorem 1 provides a rigorous bound linking the Hamiltonian to the Cost of Identity.** The theorem shows that for large \(\tilde{L}\) (with \(\gamma\sim\tilde{L}^{-1}\)), the Hamiltonian is close to \(-\frac{\tilde{L}}{2}\) times the minimal COI, and the norm of \(\partial_p A_p\) scales with \(\tilde{L}\) times the "extra-COI." This formally quantifies the separation-of-timescales narrative: slow layers have near-optimal COI, fast layers have COI far above the minimum (Section 2.1, lines 498–520).

3. **Rigorous characterization of the Cost of Identity as a dimensionality measure.** Proposition 1 connects COI to stable rank (\(\|A\|_*^2/\|A\|_F^2\)), and Proposition 3 shows that stable local minima of the COI are non-negative and equal to \(\mathrm{Rank}(A)\) (Section 1.3–1.4, lines 301–379). These results ground the intuition that low COI ↔ low-dimensional representations.

4. **Figure 1 provides a direct, targeted empirical validation.** The experiment with a known target rank \(k^*=3\) shows the (stable) Hamiltonian approaching \(-(\tilde{L}/2)k^*\) and the minimal COI approaching \(k^*\) from above, while kinetic energy spikes at the input/output boundaries. This provides a concrete illustration that the theory aligns with observed behavior in a controlled setting.

5. **Clear conceptual framework.** The paper is well-structured and the writing is clear, making the connection between Hamiltonian mechanics, the COI, and bottleneck structure accessible.

## Weaknesses

### Major

1. **Experimental validation is far too thin for the strength of the claims.** The paper makes strong predictions about Hamiltonian conservation, the approach of the minimal COI to the bottleneck rank, and the advantage of adaptive discretization. Yet the experiments are limited to two synthetic regression tasks (30→3→30 and 30→6→3→30), each presented without multiple random seeds, without across-run error bars, and without statistical significance tests. The "error bars" in Figure 1a report min–max *across layers within a single run*, not run-to-run variability. The test-error advantage of the adaptive scheme in Figure 2a is modest (often <0.02 in squared error) with no variance estimate. This level of evidence cannot rule out that the observed patterns are idiosyncratic to a particular random initialization or training run. **The paper is primarily theoretical and the experiments can be illustrative, but they need not be encyclopedic — however, even for an illustration, single-run evidence without error quantification is insufficient to support the claimed generality of the phenomena.**

2. **Critical experimental details are omitted, preventing reproducibility.** The paper does not state the optimizer used (SGD? Adam? BFGS?), the learning rate, batch size, number of training steps/epochs, initialization scheme, or the value of the regularization parameter \(\lambda\) used in any experiment. The entire experimental description is essentially contained in the figure captions. This makes it impossible to reproduce or independently assess the results. At minimum, the optimizer, \(\lambda\) value, and training length must be reported.

3. **The adaptive discretization method is under-specified to the point of being non-reproducible.** The description (Section 3, lines 622–634) is: choose \(\rho_\ell\) so that \(\|A_\ell-A_{\ell-1}\|/\|A_p\|\) is uniform across layers, leading to the update \(\rho_\ell \leftarrow c_\ell^{-1}/\sum c_\ell^{-1}\) where \(c_\ell = \|A_\ell-A_{\ell-1}\|/(\rho_\ell\|A_p\|)\). The paper says this can be done "at every training step or every few training steps" but does not specify: (a) whether the \(\rho_\ell\) are updated online during a single training run (changing the architecture during training) or computed post-hoc and then the network is retrained from scratch with fixed \(\rho_\ell\); (b) any convergence or stability behavior of this iterative scheme; (c) how the initial \(\rho_\ell\) are set before adaptation begins. Without these details, the method cannot be implemented or evaluated.

### Minor

1. **The discrete–continuous gap is not addressed.** The theory is developed for critical points of a continuous optimal control problem (NeuralODE with leak), but the experiments train discrete networks with a finite number of layers. The paper does not discuss how large the discretization error is, whether the trained network satisfies the continuous optimality conditions approximately, or how well the separation-of-timescales prediction survives discretization with finite \(L\). A direct comparison (e.g., solving the continuous problem numerically via shooting/collocation for the synthetic task and comparing to the discrete-trained activations) would significantly strengthen the paper.

2. **Theorem 1's bounds involve quantities that depend on the unknown solution.** The error bounds involve an upper bound \(c\) on \(\|B_p\|^2\) and the path length \(\ell_{\gamma,\tilde{L}}\), both of which depend on the specific geodesic being analyzed. While the form of the bound shows that errors vanish as \(\tilde{L}\to\infty\) and \(\gamma\to0\), the practical tightness of the bound for finite \(\tilde{L}\) is unclear. The paper would benefit from at least one numerical evaluation of both sides of the inequality for a trained network.

3. **Limited discussion of limitations.** The conclusion does not acknowledge that the theory applies directly only to MSE regression with weight decay, that the stable COI/minima results rely on specific assumptions (non-negativity, stability under neuron addition), or that the adaptive scheme's overhead/cost is unexplored.

### Trivial

None.

## Nice-to-Haves

- Reporting results with at least 5–10 random seeds (mean ± std) for the synthetic experiments would dramatically increase credibility without adding a different task domain.
- A pseudocode listing for the adaptive \(\rho_\ell\) scheme would resolve the under-specification issue.
- A brief discussion of how the theory might apply to classification (building on the output-scaling symmetry in Section 1.2) would broaden relevance.

## Removed Points

These points were flagged by reviewers but are removed from the main evaluation for the reasons stated below. Treat them with caution.

- **"No comparison to standard ResNet training"** — The paper's contribution is a theoretical framework for Leaky ResNets and an adaptive discretization; a full comparison to standard ResNets on non-synthetic tasks would constitute a different, broader paper. This is scope creep.
- **"The paper does not release code"** — This is a standard request but not a weakness of the scientific content; many papers do not release code at submission time. The instruction also warns against doubting the existence of artifacts cited.
- **Complaints that Figure 1a error bars show across-layer rather than across-run variation** — The caption transparently states what the error bars represent. The reviewer's observation is accurate but does not reveal a concealment; it is already a weakness (Weakness #1) that across-run variation is not reported.
- **Claim that the adaptive update rule is "circular"** — The rule is not circular: \(c_\ell = \|A_\ell - A_{\ell-1}\|/(\rho_\ell\|A_p\|)\) is approximately independent of \(\rho_\ell\) because \(\|A_\ell - A_{\ell-1}\| \propto \rho_\ell\) (it approximates \(\rho_\ell \|\partial_p A_p\|\)). The iterative update is well-defined. The real issue is under-specification (Weakness #3), not circularity.
- **"No mention of appendix"** — The parser strips appendix sections; they exist in the original submission.
- **Various formatting/style nitpicks** — These are parser artifacts, not author errors.
- **Strength Finder's claim that Theorem 1 "proves the separation of timescales with explicit bounds"** — This overstates; the bounds depend on quantities (\(c\), \(\ell_{\gamma,\tilde{L}}\)) that are not controlled. This is acknowledged as a Minor weakness above.
- **Strength Finder's generic strengths** — E.g., "this paper addressed an important problem" (no specific content). Dropped.

## Novel Insights

The reviews collectively surface an important observation: the paper's main weakness is not in its theoretical framework (which is sound and elegant) but in the gulf between the mathematical narrative and the empirical support. The Hamiltonian reformulation genuinely avoids the pseudo-inverse problem that has plagued prior Lagrangian approaches to NeuralODE analysis. But the paper presents this theoretical machinery with experimental validation that is too thin to distinguish between genuine emergent structure and artifacts of a specific synthetic setup. A more insightful framing would be: how large must \(\tilde{L}\) be before the separation-of-timescales prediction becomes quantitatively accurate, and can this threshold be predicted from the theory? The current paper does not engage this question.

## Suggestions

1. **Run the synthetic experiments with ≥5 random seeds**, report means and standard deviations for the Hamiltonian estimates and test errors. This single change would transform the credibility of the empirical claims.
2. **Provide a complete experimental specification** (optimizer, learning rate, \(\lambda\), number of steps, initialization) either in the main text or a supplementary document.
3. **Write a clear pseudocode algorithm** for the adaptive \(\rho_\ell\) scheme, specifying whether updates are online or offline, how initial \(\rho_\ell\) are set, and any safeguards for numerical stability.
4. **Quantify the discrete–continuous gap** for at least one configuration (e.g., solve the continuous optimal control problem with a fine numerical solver and compare activations to the discrete-trained network).
5. **Acknowledge the limitations** of the current experiments and theory explicitly in a "Limitations" paragraph in the conclusion.

## Score and Decision

**Originality:** 4/5 — The Hamiltonian reformulation and connection to COI are novel extensions of prior NeuralODE and bottleneck rank work.
**Importance of research question:** 4/5 — Understanding feature learning and bottleneck structure is a central problem.
**Claims well supported:** 2/5 — The theory is plausible but the experiments are too thin to fully support the central claims.
**Soundness of experiments:** 2/5 — Single runs without error bars on a single synthetic setup, with critical hyperparameters unreported.
**Clarity of writing:** 4/5 — Well-structured and clearly written.
**Value to the research community:** 3/5 — The framework is interesting but the lack of robust validation limits its immediate impact.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>