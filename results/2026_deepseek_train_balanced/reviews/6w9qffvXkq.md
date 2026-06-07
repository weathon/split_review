Now I'll produce the final consolidated review.

## Summary

This paper extends Riemannian optimization for CNNs from the standard Stiefel manifold ($X^T X = I$) to the *generalized* Stiefel manifold ($X^T S X = I$) with a learnable overlap matrix $S$. The authors adapt the iterative Cayley SGD and Cayley ADAM algorithms (Li et al., 2020) to this setting, and propose a gradient-based method to learn $S$ via its Cholesky decomposition $S = R^T R$ using the differentiable mapping $X_{i+1} = R_{i+1}^{-1} R_i X_i$. The training procedure optimizes $S$ for 20 epochs, then fixes it and applies standard Riemannian optimization for the remaining 180 epochs. Experiments on CIFAR10/100, SVHN, and Tiny ImageNet32 with Wide ResNet and VGG models indicate improved or matching test accuracy relative to the fixed-orthonormality baseline.

## Strengths

- **First application of generalized Stiefel manifold optimization to CNN training.** The paper correctly identifies a gap in the literature: generalized Stiefel manifolds have received theoretical attention (Sato & Aihara, 2019; Shustin & Avron, 2023) but had not been implemented for deep learning. This is a genuine novelty (Section 2, lines 27–28).

- **Gradient-based optimization of $S$ via a differentiable mapping.** Rather than treating $S$ as an intractable hyperparameter, the decomposition $S = R^T R$ and the mapping $X_{i+1} = R_{i+1}^{-1} R_i X_i$ (Eq. 4, Section 4.2) allow $S$ to be learned through standard backpropagation. This is a concrete technical contribution that prior work on generalized Stiefel manifolds did not provide.

- **Generalization of the iterative Cayley transformation convergence proof.** Section 3.2 (line 87) extends the contraction-mapping convergence proof from Li et al. (2020) (which required $S = I$) to arbitrary symmetric positive definite $S$, with the adapted step-size condition $\bar{\alpha} \in (0, \min\{1, 2/\|W S\|\})$. This provides theoretical grounding for the adapted retraction.

- **Empirical evaluation across multiple datasets, models, and optimizers.** Experiments span four datasets, two architectures (WRN, VGG), and two optimizers (Cayley SGD, Cayley ADAM), each with three runs and standard deviations reported. The proposed method ("gen St") matches or improves upon the baseline ("Unit" = $S = I$) for most of the 16 combinations (Table 1, Section 5.4).

## Weaknesses

### Major

- **The main results (Table 1) are confounded by the unequal training procedure.** The method spends the first 20 epochs in a qualitatively different regime: the manifold search actively updates model weights via $X_{i+1} = R_{i+1}^{-1} R_i X_i$ at roughly 2× per-epoch cost (Table 2). The baseline receives no analogous phase. Table 1 compares both methods after the same number of epochs (200), which conflates the benefit of learning $S$ with the benefit of 20 additional (slower) training epochs. The paper partially addresses this with Figure 2 showing test accuracy over wall-clock time, but the primary accuracy table does not control for this confound. Without a controlled comparison—e.g., running the baseline for 220 epochs or aligning by wall-clock time—it is unclear how much of the reported improvement is attributable to the learned manifold vs. extra effective compute.

- **No characterization of what $S$ actually learns.** The paper's central claim is that optimizing $S$ discovers a better constraint manifold, but $S$ is treated as a black box. We never see its eigenvalue spectrum, its distance from $I$ over time, or any interpretation of what structure it learns (e.g., does it emphasize certain frequency bands in the filter space?). This missing analysis makes it impossible to ground the claim that the method "finds a fitting manifold" rather than simply benefiting from early training dynamics. Section 4.2 acknowledges that optimizing $S$ expands the solution space to every full-rank matrix—i.e., the constraint is temporarily absent—yet the paper does not quantify how far $S$ actually drifts or whether the learned $S$ is meaningfully different from $I$.

### Minor

- **Convergence evidence rests on a single curve.** Figure 1 shows training loss for only one condition (SVHN + WRN + Cayley SGD). The paper states that "the training loss shows similar behavior for the other datasets" (line 166) without providing corresponding plots. For a central claim about "faster convergence," this is thin evidence.

- **Missing ablations that would isolate the mechanism.** The paper never tests: (a) what happens if $S$ is initialized to a random positive definite matrix and frozen (to test whether any non-identity $S$ helps); (b) how sensitive the method is to the 20-epoch switch timing (0, 10, 40, 80 epochs); (c) whether the specific learned $S$ matters or any early-training $S$ would perform similarly. These ablations directly bear on whether the method's stated motivation (finding a better manifold) drives the results.

- **No comparison to unconstrained training or soft orthogonality regularization.** The paper only compares against the hard Stiefel constraint ($S = I$). Without a baseline of unconstrained SGD/Adam or soft orthogonality regularization (e.g., Bansal et al., 2018), the reader cannot tell whether the benefit comes from *relaxing* the constraint or from some other aspect of the two-phase training procedure.

- **Gradient computation through $R^{-1}$ is underspecified.** Section 4.2 describes the update $X_{i+1} = R_{i+1}^{-1} R_i X_i$ and states that gradients with respect to $R$ can be computed via backpropagation, but provides no details on numerical stability or how the matrix inversion is handled in the computational graph. Since $R$ is $n \times n$ and $n$ can be large (number of input channels × kernel height × kernel width), this is a practical concern for both stability and memory.

- **Accuracy improvements are partial and uneven.** The paper's own language hedges with "most combinations" and "largest improvements" for WRN + Cayley SGD specifically (Section 5.4). The benefit appears to cluster in particular architecture–optimizer pairs, which the paper notes but does not analyze or explain.

### Trivial

- The paper contains several minor typographical issues and garbled text (e.g., line 14: "issu bbsepnaecfeic ioafl siinz et") that appear to be parser artifacts rather than author errors; these should be cleaned up in a camera-ready version.

## Nice-to-Haves

- **Statistical significance testing.** Standard deviations are reported, but formal significance tests would help interpret the smaller improvements. However, this is not standard practice for all papers in this subfield.
- **Convergence curves for all dataset–model–optimizer combinations**, at minimum in a supplementary figure, would substantially strengthen the "faster convergence" claim.

## Removed Points

The following points from the inputs were excluded per filtering rules, but are recorded here for completeness:

- **Criticism that Algorithms 1 and 2 are missing from parsed text** — This is a PDF parser artifact; the algorithms exist in the original submission. Removed per rule about missing appendix content.
- **Speculative claim about the 20-epoch head start being a "fundamental" confound** — The paper partially addresses this via Figure 2 (time-based accuracy). Retained as Major but downgraded from the critic's "fundamental" framing.
- **The harsh critic's assertion that the paper "over-claims" in the abstract** — While the convergence evidence is thin, the abstract's claim of "even faster convergence" is supported by Figure 1 for at least one condition and by the overall results for "most combinations." Removed per rule about removing strawman weaknesses; the paper does not claim uniform improvement.
- **Generic "no statistical testing" critique** — Moved to Nice-to-Have since single-run evaluations are standard in this line of work.
- Some strengths from the Strength Finder that were generic or sycophantic ("this paper addressed an important problem") were removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews identify genuine gaps (confound in experimental design, missing S analysis, thin convergence evidence) but do not contribute a novel scientific insight about the paper's subject matter beyond what is already in the paper.

## Suggestions

1. **Control for the extra compute in the manifold-search phase.** The simplest fix: run the baseline for 220 epochs (or align comparisons by wall-clock time in the main accuracy table), so the comparison attributes the benefit to $S$ rather than to extra training.

2. **Characterize the learned $S$.** Show the eigenvalue spectrum of $S$ at the end of training, its distance from $I$ over time, and whether the learned structure correlates with something interpretable (e.g., frequency selectivity). This would transform $S$ from a black box into an understood mechanism.

3. **Ablate the switch timing.** Test 0, 10, 20, 40, 80 epochs of manifold search to show whether 20 is genuinely a good choice and how sensitive the method is to this hyperparameter.

4. **Provide convergence curves for all experimental conditions**, not just one. A concise figure or supplementary table showing when each configuration crosses baseline performance would be far more informative than a single curve.

5. **Add a baseline without any Stiefel constraint** (standard SGD/Adam) and one with soft orthogonality regularization, to isolate whether the benefit comes from relaxing the constraint vs. the two-phase training procedure.

6. **Provide implementation details for the gradient through $R^{-1}$**, including any numerical stabilization techniques used.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>