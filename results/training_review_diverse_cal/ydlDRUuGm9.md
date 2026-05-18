Now I have a thorough understanding of the paper. Let me construct the final consolidated review by verifying each reviewer claim against the actual paper content.

---

## Summary

This paper theoretically and empirically compares KANs with MLPs along two axes: representation/approximation capability and spectral bias during training. It provides clean representation theorems (any ReLUᵏ MLP can be exactly represented by a KAN of comparable size; any KAN without SiLU can be represented by an MLP with width scaling O(GW)), a Hessian conditioning analysis showing that single-layer KANs avoid the ill-conditioning that drives spectral bias in MLPs, and experimental evidence on 1D wave fitting, Gaussian random fields, and a 1D Poisson equation that KANs learn high-frequency content earlier than equivalently-trained MLPs.

## Strengths

- **Clean representation equivalence results (Thm 1, Thm 2)**. Theorem 1 proves any ReLUᵏ MLP (including standard ReLU) can be exactly represented by a KAN with at most twice the depth, the same width, and only G=2 grid points, establishing that KANs are at least as expressive as MLPs. Theorem 2 provides the converse (KAN→MLP) with a width scaling of O(GW), giving a concrete argument for why KANs with large grids may be more parameter-efficient for certain function classes.

- **Novel Hessian conditioning analysis for shallow KANs (Thm 3)**. The paper proves that the Hessian of the least-squares loss for a single-layer KAN has a condition number bounded by C·d (independent of grid size G) away from a small nullspace of dimension d′(d−1). This is concretely contrasted with two-layer ReLU MLPs whose Hessian condition number scales like n⁴, providing a rigorous theoretical basis for why shallow KANs should not exhibit the same spectral bias as MLPs.

- **Convincing 1D frequency-domain experiment**. Figures 1–2 directly track the Fourier content of learned functions during training, showing that KANs converge on all frequency components nearly simultaneously, while even deep/wide MLPs (with 10× more training iterations) still struggle with high frequencies. This is the cleanest and most direct evidence for the paper's central claim.

- **Systematic experimental exploration across task types**. The GRF experiment (varying smoothness scale σ across dimensions 2–4) and the Poisson equation experiment (varying solution frequency k=2,4,8,16,32) both show the same qualitative pattern: KAN performance degrades much less than MLP performance as frequency increases or smoothness decreases. The paper also honestly documents the overfitting trade-off that arises from reduced spectral bias, connecting theoretical properties to practical hyperparameter choices.

## Weaknesses

### Fatal
None.

### Major
- **The theory of spectral bias does not extend to the deeper KANs used in experiments.** Theorem 3 analyzes a *single-layer* KAN, which is a linear model (linear combination of fixed B-spline basis functions). The paper's experiments use KANs of depth 2–4 with SiLU nonlinearities and compositional structure. The paper explicitly acknowledges this gap ("The analysis given is necessarily highly simplified and heuristic") but does not bridge it. The nonlinear composition of layers could reintroduce frequency bias through the interaction of basis functions across layers, and no theoretical argument (e.g., NTK eigenvalue analysis, even under simplifying assumptions) is provided to connect the shallow theory to deeper behavior. This leaves the paper's central theoretical claim about spectral bias formally supported only for the degenerate single-layer case.

### Minor
- **The higher-dimensional experiments (GRF, PDE) lack direct frequency-domain measurement.** While the 1D wave experiment tracks Fourier content during training, the GRF and PDE experiments rely on loss curves and error metrics alone. The GRF experiment does control for smoothness via σ and the PDE experiment varies k, which are reasonable indirect approaches, but the claim of *reduced spectral bias* specifically would be substantially strengthened by showing the frequency content of learned functions (or error per frequency band) for these tasks. Without it, alternative explanations — different effective capacity, optimization differences from grid extension, different inductive biases unrelated to frequency — are not fully ruled out.

- **Grid extension's effect on spectral bias is not experimentally isolated.** The paper claims that grid extension specifically helps with high-frequency learning, but the KAN experiments always use grid extension while the MLP experiments do not. An ablation comparing KANs with and without grid extension (or with the final fine grid from the start) would clarify whether the advantage comes from the multi-resolution training procedure or from the KAN architecture itself.

### Trivial
- **The eigenvalue bound in Theorem 3 omits explicit dependence on the spline degree k.** The theorem states the constant C depends on k but does not sketch how. A brief explanation or reference to the known conditioning of B-spline Gram matrices would improve clarity.
- **The KAN→MLP representation (Thm 2) requires w_b = 0 (no SiLU).** The paper acknowledges this, but the practical significance is minor since most KAN implementations include the SiLU term.

## Nice-to-Haves
- Extending the spectral bias analysis to two-layer KANs (even under linearized/decoupled assumptions) would substantially strengthen the theoretical contribution.
- Direct frequency-domain analysis for the GRF and PDE experiments (e.g., projecting the learned function onto frequency bands or computing NTK eigenvalue decay for deeper KANs).
- An ablation comparing KANs with fixed final grid vs. progressive grid extension to isolate the contribution of the multi-resolution training technique.

## Removed Points
These points are flagged for removal; treat them with caution.

- **"Unfair comparison due to 10× more iterations for MLP in the 1D wave experiment"** — Removed per hard rules. The asymmetry (80K MLP iterations vs. 8K KAN iterations) favors the baseline (MLP), not the author's method. The paper is intentionally making a stronger point: even with an order of magnitude more training, MLPs still fail on high frequencies.
- **"Parameter count differences in GRF/PDE experiments make the comparison unfair"** — Removed per hard rules. The asymmetry (MLP width 256 vs. KAN width 10) favors the baseline (MLP has far more capacity). The paper's claim is about spectral bias, and the fact that a much smaller KAN outperforms a much larger MLP on high-frequency tasks strengthens, not weakens, the claim. The iteration counts are also equal in these experiments (500 vs. 500 for GRF; 200 vs. 200 for PDE).
- **"The representation theorems do not cover the full KAN architecture (w_b ≠ 0)"** — This is a known and explicitly stated limitation of Theorem 2. The paper clearly says "If the functions... have weight w_b ≠ 0... then it is clear that we can not represent the resulting KAN using an MLP with activation σ_k." The converse direction (Thm 1, MLP→KAN) applies to the full KAN architecture. This is a scope note, not a weakness.

## Novel Insights

None beyond the paper's own contributions. The key insight — that KANs' use of B-spline basis functions on edges produces a well-conditioned Hessian for shallow networks, in contrast to MLPs' poorly conditioned Hessian — is the paper's own, and it is clearly presented.

## Suggestions

1. **Add a theoretical bridge for deeper KANs.** Even a simplified analysis (e.g., NTK eigenvalue computation for a two-layer KAN without SiLU) would substantially raise the impact of the theoretical contribution. Alternatively, provide experimental evidence that the shallow theory predicts deeper behavior by computing NTK eigenvalues of multi-layer KANs.

2. **Add frequency-band error analysis for the GRF and PDE experiments.** If the learned function's projection onto frequency bands can be computed, show that KANs maintain lower error across all bands while MLPs concentrate error in high bands. This would directly substantiate the spectral bias claim for the multi-dimensional setting.

3. **Isolate grid extension via ablation.** Compare KANs trained with progressive grid extension against KANs trained from the start with the final fine grid.

4. **Study the effect of SiLU on spectral bias.** Compare KANs with and without the SiLU residual connection (w_b = 0 vs. w_b ≠ 0) to see whether the linear theory applies in practice or whether the nonlinearity changes the spectral bias behavior.

## Score and Decision

The paper makes a genuine contribution: clean representation theorems that establish formal expressiveness relationships, a novel theoretical argument connecting KAN architecture to reduced spectral bias (for shallow networks), and reasonable experimental evidence across multiple problem types. The weaknesses are real — the theory-experience depth gap is the most significant, and the higher-dimensional experiments are indeed less direct than the 1D case — but none are fatal. The paper is transparent about its limitations and the conclusions are appropriately scoped. This is a solid conference paper that would benefit from the suggested extensions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>