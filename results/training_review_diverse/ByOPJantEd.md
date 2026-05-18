Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

The paper introduces "Wigner kernels" — body-ordered, rotationally equivariant kernels for atomistic machine learning that are computed iteratively via Clebsch-Gordan contractions (the "Wigner iteration"). The key idea is to evaluate body-ordered kernels directly in kernel space, avoiding the exponential growth of explicit feature-space methods like ACE. The method is demonstrated on gold clusters, random methane configurations, and the QM9 benchmark, achieving competitive accuracy (4.3 meV MAE on QM9 energies) with low angular momentum cutoffs.

## Strengths

1. **Exponential-to-linear cost reduction in body order**: The Wigner iteration computes body-ordered kernels without ever constructing the exponentially large feature vector. Gold cluster results (Fig. 1) show systematic improvement up to ν=6, with ν=4 already outperforming squared-kernel methods — confirming the practical benefit of the kernel-space approach.

2. **Strong QM9 energy accuracy**: Table 1 reports 4.3 meV (±0.1) MAE on the full QM9 dataset, surpassing Allegro (4.7 meV) and all other models in the comparison — the single strongest quantitative evidence for the method's predictive power.

3. **No explicit radial-element basis truncation**: The method requires no radial or chemical-element basis (Sec. 2.3, Eq. 5). On QM9 (5 elements, 110k training points), the learning curve shows no saturation (Fig. 4), consistent with approaching the full-basis limit.

4. **Systematic body-order ablation**: Gold cluster results (Fig. 1) provide a clean ablation: ν=2 saturates, ν=3 improves, ν=4−6 yield progressively lower errors — confirming the kernel correctly isolates body-order contributions and that high-body-order terms are physically needed.

5. **Competitive accuracy despite low λ_max**: On methane (Fig. 2) and QM9 (Fig. 4), the model uses only λ_max=3 and outperforms methods requiring much higher angular cutoffs (e.g., LE-ACE uses λ_max=10 on methane). The paper provides a mechanistic explanation (tensor products of low-λ kernels intrinsically generate higher angular frequencies).

6. **Tensorial targets without saturation**: On QM9 dipole moments (Fig. 3), Wigner kernels avoid the saturation seen in λ-SOAP kernels as training set size increases, demonstrating complete body-ordered equivariant kernels can capture long-range tensorial behavior from local correlations.

## Weaknesses

### Fatal
None.

### Major

1. **Missing derivation connecting the Wigner iteration to the body-ordered kernel definition.** The paper defines body-ordered kernels via an integral over rotated densities (Eq. 5), then presents an iterative formula (Eq. 9) said to compute them. No reasoning is given for why the iteration yields the same object as the integral definition. The recursion resembles the tensor-product structure of ACE features, but the paper neither shows the equivalence nor cites a source where it is established. Since the contribution rests on the iteration being correct and complete, a sketch of the derivation or a clear reference is needed before the reader can assess whether the method implements the claimed kernel or some different subspace of correlations.

2. **No description of how KRR was actually solved for datasets with ≥10⁵ training points.** The paper reports learning curves for gold clusters (105k structures) and QM9 (training sets up to 110k structures) stating "Kernel ridge regression (KRR)" is used throughout. A dense KRR solve scales as O(N³), which is infeasible at N=110k on ordinary academic resources. The paper mentions sparse KRR only as a future possibility (line 163: "it would be comparatively simple to avoid this scaling implementing a sparse KRR framework"), implying it was NOT used. No iterative solver, low-rank approximation, or other strategy is disclosed. Line 292 states "The steep computational cost is largely due to the use of full KRR models," confirming the experiments used full KRR without describing how the linear system was solved. This makes the results unverifiable and the method's practical feasibility impossible to assess. The authors must specify the actual algorithm (e.g., conjugate gradient, Nyström approximation, or other) and report its computational cost.

### Minor

3. **No empirical runtime or memory benchmarks.** Section 2.4 discusses theoretical scaling (λ_max⁷, worse than traditional SO(3) products at λ_max⁵) and notes favorable properties, but no wall-clock times, memory footprints, or inference costs are reported for any experiment. For a methods paper claiming a practical computational advantage, this is a notable omission. Training time, inference time, and memory usage for each benchmark — alongside a representative baseline (e.g., LE-ACE) — would substantiate the claimed benefits.

4. **"State-of-the-art" claim is somewhat stronger than the evidence.** The abstract and results state Wigner kernels "reach[ed] state-of-the-art accuracy on QM9." The comparison table (Table 1) is explicitly drawn from the Allegro reference and includes 7 models, the most recent being Allegro (2022). Within this set, the claim holds, but the unqualified "state-of-the-art" suggests dominance over all published methods, when the comparison is limited. The paper would benefit from a more precise qualifier (e.g., "competitive with the best published models" or "state-of-the-art among the methods compared in Ref. [allegro]").

5. **Element handling via δ-functions and its consequences underexplored.** Kernels between different chemical species are set to zero (Eq. 8, line 150). The paper presents this as an advantage of avoiding an explicit element basis, but a δ-function on elements is itself a strong basis choice that decouples the representation of different species. The consequences of this choice for multi-element transferability and for datasets with many elements are not discussed.

6. **Missing hyperparameter details.** The paper mentions cross-validation and dual annealing but does not report the ranges searched for ν_max, λ_max, cutoff radius, regularization α, or how these were chosen. This makes the experiments difficult to reproduce or compare fairly.

### Trivial

7. **Body-order vs. angular resolution are conflated in the analysis**, but the paper itself acknowledges this (lines 219–220: "The combined effect of increasing ν complicates the interpretation of ablation studies, making it difficult to disentangle the effects of correlation order and of angular resolution"). This self-awareness is commendable. A simple ablation comparing ν=3/λ_max=3 vs. ν=2/λ_max=6 would strengthen the mechanistic claim, but its absence is not a weakness — it is a natural direction for future work.

## Nice-to-Haves

- Algorithm pseudocode for the Wigner iteration (initialization, Clebsch-Gordan contractions, termination condition) would aid reproducibility.
- Error bars on all learning curves (not just the final QM9 point) would strengthen statistical claims.
- An ablation experiment separating body-order effects from angular resolution effects (e.g., ν=3/λ_max=3 vs. ν=2/λ_max=6 on methane) would clarify the mechanistic explanation in Sec. 3.2.

## Removed Points

- **"KRR on ≥10⁵ points is practically impossible"** — downgraded from fatal/implausible to Major (missing implementation detail). Iterative solvers (conjugate gradient) are standard for large KRR and do not require O(N³). The concern is the lack of disclosure, not inherent impossibility.
- **"State-of-the-art claim is overstated because MACE/Equiformer achieve <4 meV"** — removed per the rule that I cannot verify missing related works without external sources. The paper's comparison table is self-contained and shows Wigner kernels leading all models listed.
- **"Missing derivation" characterized as fatal** — downgraded to Major. The method is clearly defined and can be implemented from Eq. 9; the missing connection to Eq. 5 is a conceptual gap that affects understanding but does not invalidate the empirical results.
- **Various formatting/style nitpicks** — removed per parser-artifact rules.

## Novel Insights

The Harsh Critic correctly identifies that the paper's two most consequential gaps are at the exact points where the authors took intellectual shortcuts: (1) asserting the equivalence between the integral definition and the iterative construction without proof, and (2) treating the KRR solver as a black box when its computational demands are extraordinary for the dataset sizes involved. These are not random omissions — they are the two steps where the paper transitions from known mathematics (body-ordered expansions, spherical tensor contractions) to its claimed novelty (kernel-space evaluation without basis truncation). The fact that both transitions are underspecified suggests the authors may be overestimating how much of the connection is "obvious" to readers outside the immediate ACE community. Conversely, the Strength Finder's identification of the non-saturating dipole learning curves (Fig. 3) as a key finding is well-placed: this result is arguably more interesting than the raw QM9 energy number, because it demonstrates a qualitative capability (tensorial targets without feature-space explosion) rather than a quantitative increment on a saturated benchmark.

## Suggestions

1. Provide a self-contained derivation or explicit reference showing that the Wigner iteration computes the kernel in Eq. 5. Even a short paragraph explaining that the ν-fold tensor product of the ν=1 density overlap, when symmetrized via the SO(3) integral, yields the Clebsch-Gordan recursion would suffice.

2. Disclose the actual algorithm used for the KRR linear system at N=110k. If conjugate gradient was used (standard practice), state that. Report training time, inference time, and memory footprint for at least one representative benchmark.

3. Replace unqualified "state-of-the-art" with a precise qualifier matching the comparison scope.

4. Report the hyperparameter search ranges and final selected values for ν_max, λ_max, cutoff radius, and regularization α.

5. Add algorithm pseudocode showing the full computation of a kernel between two atomic environments.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>