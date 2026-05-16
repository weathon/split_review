Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper proposes Wigner kernels, a class of body-ordered rotationally equivariant kernels for atomistic machine learning. The core innovation is an iterative evaluation (the "Wigner iteration") that computes body-ordered density-correlation kernels directly in kernel space, avoiding the exponential explosion of explicit feature-space expansions that plagues methods like ACE. The approach achieves state-of-the-art accuracy on QM9 (4.3 meV for energies, outperforming Allegro and other equivariant NNs), demonstrates systematic convergence with body order on gold clusters, and provides a unified treatment of scalars, vectors, and tensors.

## Strengths

- **Wigner iteration eliminates the exponential feature growth of body-ordered expansions.** The iterative kernel construction (Eq. 12) costs linearly in maximum body order ν for fixed angular truncation, in contrast to ACE-like expansions where the feature count scales as (a_max · n_max · λ_max)^ν. This is the paper's central intellectual contribution and is clearly motivated and derived (Sec. 2.3–2.4).

- **State-of-the-art accuracy on QM9 for both scalar and tensorial properties.** Table 1 reports 4.3 meV test MAE for QM9 energies, surpassing Allegro (4.7 meV), PaiNN (5.9 meV), and other specialized equivariant architectures. For dipole moments (Fig. 3), Wigner kernels avoid the saturation seen in λ-SOAP methods at large training set sizes. That a kernel method can still outperform extensively tuned deep networks on a decade-old benchmark is noteworthy.

- **Systematic convergence with body order on a genuinely many-body system.** The gold cluster experiments (Fig. 1) show monotonic improvement from ν=2 to ν=6, with ν=6 matching LE-ACE. This directly validates that the kernel captures physically meaningful high-order correlations and that the body-ordered truncation is well-founded.

- **Unified equivariant formulation for scalars, vectors, and tensors.** The same Wigner iteration (Eq. 12) constructs kernels satisfying exact SO(3) equivariance (Eq. 4) for any angular channel λ. The paper demonstrates this for both scalar energies (λ=0) and vector dipole moments (λ=1), avoiding the heuristic mixing of invariant and covariant components used in SA-GPR.

- **Theoretical insight into why low λ_max suffices.** Section 3.2 provides a concrete explanation: the tensor-product structure of the Wigner iteration "incorporates higher frequency components in their functional form, much like sin² ωx contains components with frequency 2ω." This rationalizes why λ_max=3 works where explicit feature models require λ up to 20, and is a genuine intellectual contribution beyond the method itself.

- **Chemical-element scalability.** The Kronecker-delta construction in Eq. 13 keeps the kernel cost independent of the number of elements, a practical advantage directly leveraged on the 5-element QM9 dataset.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **λ_max not reported for the gold cluster experiment.** The paper states λ_max=3 for methane (line 215) and QM9 (line 250), but the gold cluster experiments (Sec. 3.1) do not specify λ_max used. Since computational cost scales as λ_max⁷, and the paper's own argument is that low λ_max works, this omission should be fixed. (It is likely small — the paper notes "aggressive truncation" in the conclusions — but the experiment section should state the exact value.)

- **No ablation study on λ_max for any dataset.** The paper's central practical claim is that low λ_max is sufficient, yet it never systematically sweeps λ_max to show where accuracy saturates or degrades. An ablation on even one dataset (e.g., QM9 or gold) showing that increasing λ_max does not materially improve accuracy would significantly strengthen the evidence. Without it, the reader cannot assess whether reported performance is robust or an artifact of a particular truncation.

- **Learning curves lack error bars except for the final QM9 point.** The QM9 final point is averaged over 16 splits (Table 1), and the early QM9 points over 10 runs (Fig. 4 caption). But for gold clusters and methane (Figs. 1–2), the paper does not state whether multiple seeds or error bars are shown. Variance in the low-data regime is important for judging model capacity and statistical robustness.

- **The computation of the ν=1 kernel's rotation integral is not explicitly described.** Equation 13 defines the ν=1 kernel with an integral over SO(3) weighted by a Wigner D-matrix. The paper states these "yield a Gaussian overlap, which can be computed analytically," but the sentence is truncated (likely a parser artifact removing what would be a brief explanation or reference). While the existence of closed-form expressions for such integrals is standard knowledge, the main text should either provide the formula or cite a reference that does, to keep the method section self-contained.

- **Force training is not supported.** The paper acknowledges this (Fig. 2 caption) but does not discuss it as a limitation in the conclusions. For many atomistic applications (e.g., molecular dynamics), force predictions are essential. This limits the method's current applicability relative to competing approaches.

### Trivial

- The paper should explicitly clarify that the phrase "without a basis" refers to avoiding a radial/element basis expansion — angular truncation (λ_max) remains, and the paper acknowledges this. The title and abstract could be read as claiming no basis at all, which is slightly imprecise. (The paper itself mostly gets this right by specifying "radial-chemical basis" in the abstract.)

## Nice-to-Haves

- **Wall-clock timing or memory benchmarks.** The paper gives theoretical scaling (λ_max⁷, linear in ν) but no actual runtime or memory measurements. Even a rough comparison (e.g., "training on 110k QM9 molecules takes X hours on Y hardware") would help readers gauge practical applicability.

- **Sensitivity analysis on the cutoff radius.** The locality assumption is central; showing how results vary with cutoff would strengthen the evaluation.

- **Investigation of whether increasing λ_max closes the gap to LE-ACE on methane.** The methane comparison shows Wigner kernels (λ_max=3) competitive with LE-ACE (l=20). A brief check of whether higher λ_max further improves WKs would settle whether the method is truly data-limited or angular-resolution-limited here.

## Removed Points

These points were raised by reviewers but are removed for the following reasons:

1. **"Method requires an angular basis despite claiming 'without a basis'"** — The paper's claim is about avoiding the *radial-chemical* basis explosion. Angular truncation λ_max is explicitly acknowledged as a remaining limitation (lines 166–168). The reviewer conflates two different truncation axes. The paper's terminology is precise enough in context.

2. **"Does not compare to Glielmo et al. 2018"** — Factually wrong. The paper cites and discusses Glielmo et al. 2018 in the Related Work section (line 61): "Ref. [glie+18prb] introduces density-based body-ordered kernels, and it proposes their analytical evaluation for low body orders."

3. **"Handling of multiple chemical elements is not explained"** — Factually wrong. Line 150 explains: "where the δ_{a_i a_{i'}} term simply indicates that kernels between atoms of different chemical species are set to zero."

4. **"Scaling discussion is misleading"** — The paper explicitly states "the steep scaling with λ_max is a potential drawback" (line 166) and discusses λ_max⁷ vs. λ_max⁵. The claim of linear scaling with ν is explicitly qualified as being for fixed λ_max. The paper is balanced and not misleading.

5. **"Baseline comparisons are not controlled"** — The gold cluster comparison uses the same radial transform and optimizes a single hyperparameter for LE-ACE. The QM9 comparison follows the Allegro protocol with 110k/10k/test split, which is standard and fair. Methane comparisons reference published values. These are standard practices in the field; the reviewer's demands for controlled re-training of every baseline would be unusual.

6. **"One-body kernel never used in results"** — The paper states it "will be useful in Section~[appendix] to define non-linear kernel functions" (line 158). The appendix is stripped by the parser; this is an artifact, not an omission.

7. **Various formatting/style nitpicks and demands for appendix content** — Per hard rules, these are parser artifacts or out of scope.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation: the paper's explanation for why low λ_max suffices (Sec. 3.2) — that the iterative tensor-product construction intrinsically mixes higher angular frequencies — provides a principled justification for a phenomenon observed empirically across many recent equivariant ML models (NequIP, MACE, Allegro). The reviews helpfully contextualize this as potentially the paper's most broadly impactful insight, extending beyond kernel methods to equivariant neural network design.

## Suggestions

1. Report λ_max for all experiments explicitly, especially the gold cluster dataset.
2. Add a λ_max ablation study for at least one dataset (gold or QM9) to empirically support the claim that low λ_max is sufficient.
3. Include error bars / multiple-seed information in all learning curves.
4. Add a brief explanation or citation for the analytical evaluation of the ν=1 kernel's rotation integral to make the methods section self-contained.
5. Consider adding wall-clock timing information to help readers assess practical cost.
6. Explicitly discuss the force-training limitation and potential extensions in the conclusions.

## Score and Decision

Based on the above: the paper's core contribution is novel and clearly explained; the experimental validation is strong across multiple diverse benchmarks (gold, methane, QM9 energies and dipoles); and the method achieves genuine state-of-the-art results. The weaknesses are real but minor — mostly missing hyperparameter reporting, one missing ablation, and presentation gaps. None undermine the central claims. This is a solid acceptance.

MY FINAL SCORE: <pineapple>8</pineapple>
MY FINAL DECISION: <orange>Accept</orange>