- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 6, 5, 6
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper introduces Stable and Expressive Positional Encodings (SPE), a learnable architecture for processing Laplacian eigenvectors as graph positional encodings. The core insight is a "soft partition" of eigenspaces via eigenvalue-dependent weighting, replacing the hard eigenspace partition used in prior basis-invariant methods (e.g., BasisNet). The paper proves that SPE is stable with respect to Laplacian perturbations (Theorem 5), universally expressive for basis-invariant functions (Proposition 6), and can count graph substructures (Proposition on cycle counting). Empirically, SPE achieves strong results on ZINC (0.0693 MAE), Alchemy, DrugOOD OOD generalization, and substructure counting.

## Strengths

1. **Novel architecture combining stability and expressivity.** SPE's soft eigenspace partition via \(\mV\text{diag}(\phi_\ell(\boldsymbol{\lambda}))\mV^\top\) is a principled resolution of the stability–expressivity tension in Laplacian PE methods. The paper clearly identifies that hard partitions (BasisNet) cause instability, and eigenvalue-agnostic methods (PEG) sacrifice expressivity. SPE's approach is well-motivated.

2. **Strong empirical results on ZINC.** On ZINC (Table 1), SPE achieves 0.0693 test MAE, substantially outperforming SignNet (0.0853), BasisNet (0.1555), and PEG (0.1444). This is a clear empirical validation that the combination of stability and expressivity translates to better predictive performance.

3. **Provable universal expressivity for basis-invariant functions.** Proposition 6 shows that SPE can approximate any continuous basis-invariant function, matching BasisNet's theoretical expressivity while adding stability. Proposition 2 further shows that with 2-layer MLPs, SPE can distinguish inputs with identical eigenvectors but different eigenvalues — a capability not present in BasisNet's original form.

4. **Cycle counting capability.** Proposition 3 (theorem counting cycles) and Figure 4 show that SPE can provably and empirically count 3–5 cycles with exponentially lower MAE than SignNet, demonstrating that the architecture retains high expressivity.

5. **Empirical demonstration of stability–expressivity trade-off.** Figure 3 systematically varies SPE's stability (via Lipschitz constants and spline pieces) and shows the expected trade-off: more stability → larger training error but smaller generalization gap. This controlled experiment directly validates the paper's central thesis.

## Weaknesses

### Major

1. **Mismatch between stability definition and the theorem's bound.** Definition 4 requires *universal* constants \(c, C > 0\) such that for any Laplacians \(\mL, \mL'\), \(\|\text{PE}(\mL) - \text{PE}(\mL')\| \le C \cdot \|\mL - \mL'\|^c\). Theorem 5 gives a bound with a term \((\alpha_2 d/\gamma + \alpha_3)\|\mL - \mL'\|\) where \(\gamma = \lambda_{d+1} - \lambda_d\) is the eigengap. Since \(\gamma\) can be arbitrarily small (nearly-repeated eigenvalues), the effective coefficient can become arbitrarily large, meaning no universal \(C\) exists for all inputs when \(d < n\). The paper acknowledges this dependence and notes it is "inevitable as long as \(d < n\)" (line 138), but the central claim of being "provably stable" (abstract, lines 5 and 32) is stated without this caveat. The method *is* continuous (small perturbation → small output change), but the bound does not strictly satisfy the stated definition. **Impact:** This weakens — but does not invalidate — the core theoretical claim. The paper should either revise Definition 4 to permit constants that depend on the eigengap (e.g., a local or input-dependent stability notion) or explicitly state the caveat in the abstract and introduction.

2. **OOD generalization advantage over stable baselines (PEG, No PE) is modest, despite strong theoretical framing.** In Table 2 on DrugOOD, SPE's OOD-Test AUC on Size (66.02) is virtually identical to No PE (66.04) and PEG (66.01). On Scaffold, SPE (69.64) is only marginally ahead of PEG (69.15). Standard deviations overlap. The paper's claim that unstable methods perform "much worse than stable methods" (line 290) is accurate when comparing the group {No PE, PEG, SPE} against {SignNet, BasisNet}, but the advantage of SPE specifically over *simpler* stable baselines is small. This does not undermine the paper's contribution (SPE still outperforms on ZINC, and the stable-vs-unstable group comparison holds), but the OOD experiments do not strongly isolate an advantage attributable to SPE's specific design beyond general stability.

3. **Missing discussion of computational cost.** SPE constructs \(m\) copies of the \(n \times n\) matrix \(\mV\text{diag}(\phi_\ell(\boldsymbol{\lambda}))\mV^\top\). For large \(n\) or large \(m\), this is \(O(m n^2 d)\) memory and computation, which practitioners would need to consider. No runtime, memory usage, or scaling behavior is reported, and no discussion of how \(m\) or \(d\) affect computational cost.

### Minor

1. **No systematic ablation of the hyperparameter \(m\) (number of channels).** The number of \(\phi_\ell\) functions is a key architectural choice, but its effect on performance is not studied. How does performance vary with \(m\), and what guides the choice of \(m\)?

2. **Limited exploration of the number of eigenvectors \(d\).** The paper tests \(d = 8\) and \(d = \text{full}\) but does not report results for intermediate values of \(d\), which could more clearly reveal the stability–expressivity trade-off.

3. **The domain generalization bound (Proposition 7) assumes the base GNN is \(C\)-Lipschitz continuous with respect to Laplacians and node features.** This is a standard assumption in theoretical GNN analysis and reasonable for norm-bounded weights, but the bound's practical relevance would be strengthened by any discussion of how to estimate or control \(C\) in practice.

### Trivial

- None.

## Nice-to-Haves

- Adding a brief proof sketch for Proposition 6 (basis universality) in the main text would help readers assess the plausibility of the claim without diving into the appendix.
- Comparing SPE against a variant of BasisNet or SignNet augmented with eigenvalue-dependent soft averaging (similar to SPE's design) would better isolate the effect of the soft partition from other architectural differences.
- Releasing code would improve reproducibility.

## Removed Points

These points were flagged by the reviewers but are removed after cross-checking against the paper:

- **"Specformer novelty distinction is thin" (Harsh Critic).** The paper explicitly addresses this on lines 99–100 and 183, noting that SPE targets positional encodings (not convolution), uses general permutation-equivariant \(\phi_\ell\) (not just transformers), and provides stability analysis (which Specformer lacks). The distinction is adequately justified.
- **"Proposition 6 result relegated entirely to the appendix"** – This is standard practice for theory papers with page limits. The statement is clear enough in the main text. However, a proof sketch would be nice-to-have.
- **"Domain generalization bound lacks connection to experiments" (Harsh Critic).** The assumption that GNNs are Lipschitz continuous with respect to their inputs is standard in the GNN theory literature. This is a reasonable theoretical assumption, not a weakness unique to this paper.
- **"Trade-offs section does not isolate SPE-specific advantage" (Harsh Critic).** The experiment is explicitly designed to test the paper's *own* hypothesis about the stability–expressivity trade-off, not to demonstrate a unique SPE-specific phenomenon. This is appropriate framing.
- **"Sensitivity to \(d\)" as a separate weakness.** This is already covered under Minor weakness #2 above (merged).
- Various formatting nitpicks and reproducibility concerns about undisclosed hyperparameters (these are parser artifacts or standard practice).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the stability definition/theorem alignment.** Either revise Definition 4 to allow constants that depend on the eigengap (making it a local or input-conditional stability notion) or add the caveat to the abstract that the stability bound's constants depend on the spectral gap when \(d < n\). The paper's acknowledgment of this on lines 138–139 is good, but it needs to be reflected in the central claims.
2. **Add a brief computational cost discussion** (runtime, memory, scaling with \(n\), \(d\), and \(m\)).
3. **Ablate the hyperparameter \(m\)** to provide guidance for practitioners.
4. **Report intermediate values of \(d\)** (e.g., \(d = 4, 16, 32\)) to reveal the stability–expressivity trade-off more clearly.
