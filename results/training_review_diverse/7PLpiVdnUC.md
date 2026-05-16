Now I have a thorough understanding of the paper. Let me synthesize the final review, carefully cross-checking each criticism against the actual paper text.

## Summary

This paper introduces Lie Algebra Canonicalization (LieLAC), a framework for making pre-trained neural models equivariant under non-compact Lie groups by wrapping them with an energy-based canonicalization module. The key contributions are: (1) extending the theory of canonicalization and frame averaging to handle non-compact groups through weighted closed canonicalizations and orbit-closure arguments; (2) practical guidelines for constructing energy functions and performing Lie-algebra-based optimization; and (3) demonstrations on invariant image classification (affNIST/homNIST) and Lie-point-symmetry-equivariant neural PDE operators.

## Strengths

1. **Solid theoretical extension of canonicalization to non-compact groups**: The paper introduces weighted closed canonicalizations (Definition 3, Section 3.1) and shows that the sequential closure of weighted orbit canonicalizations is precisely weighted closed canonicalizations (Theorem 1). This addresses genuine limitations in prior work (Dym 2024, Ma 2024) that was restricted to finite or compact groups, and is essential for handling Lie point symmetry groups of PDEs.

2. **Strong empirical performance on invariant image classification under non-compact groups**: LieLAC applied to a standard CNN achieves 0.972 on affNIST and 0.960 on homNIST, outperforming the dedicated equivariant architectures affConv (0.943) and homConv (0.927) from Macdonald et al. (2022), while maintaining competitive MNIST accuracy (Table 1, Section 5.2). This convincingly demonstrates that canonicalization can match or exceed specialized architectures on challenging non-compact groups (affine and homography).

3. **Data-efficient equivariance for a pre-trained PDE foundation model**: LieLAC applied to the Poseidon foundation model on the Allen-Cahn equation reduces OOD test error from 7.619e-3 (Poseidon baseline) to 1.143e-3 (LieLAC [Poseidon + ft.]), and average error from 4.132e-3 to 1.055e-3 (Table 1, Section 5.3.3). Fine-tuning requires only 100 trajectories, demonstrating practical data efficiency.

4. **Explicit treatment of solvable Lie algebras for PDE symmetry groups**: Sections 5.3.1–5.3.2 provide complete global parameterizations of the heat and Burgers' symmetry groups (e.g., $G^H = SL(2,\mathbb{R}) \ltimes H(1,\mathbb{R})$, $G^B = SL(2,\mathbb{R}) \ltimes \mathbb{R}^2$), and Section 4 explains how solvability enables reduction to Euclidean optimization — a useful technical bridge between abstract theory and implementation.

## Weaknesses

### Fatal
None.

### Major

1. **Heat and Burgers PDE experiments lack quantitative evaluation.** Two of the three PDE examples presented as central to the paper's "equivariant neural operator" claim contain only qualitative canonicalization illustrations (Figure 1) with no test errors, no comparisons to non-equivariant baselines, and no measure of equivariance violation. For a paper whose title and motivation emphasize neural operators, this is a critical evidential gap. The Allen-Cahn experiment provides the only quantitative PDE result, which alone is insufficient to support the paper's broader claims about neural operator equivariance.

2. **No comparison to data augmentation or loss augmentation baselines.** The paper explicitly discusses data augmentation (Brandstetter 2022) and loss augmentation (Akhoundsadegh 2023, Li 2023) as prior approaches for incorporating PDE symmetries (Section 1), yet includes none of these as experimental baselines. For the Allen-Cahn experiment, one could train Poseidon on data augmented with SE(2)-transformed initial conditions and compare the resulting OOD error to LieLAC's. Without this, it is unclear whether LieLAC offers practical advantages over simpler, well-established approaches. The paper's claim in Section 5.3.3 that fine-tuning on canonicalized data is more efficient than augmentation is an assertion, not a demonstrated result.

### Minor

3. **Theoretical machinery not clearly connected to experimental design.** Sections 3–4 introduce substantial apparatus (weighted closed canonicalizations, Hausdorff-measure constructions, orbit-closure arguments, Theorem 2 on energy representation) that is only loosely tied to the empirical evaluation. The practical algorithm uses simple gradient descent with multiple restarts over a Lie-algebra parameterization (Eq. 6). Non-compactness issues that drive the theory are handled in experiments by either restricting to a discrete subgroup (Allen-Cahn: C₄) or using explicit global parameterizations (heat, Burgers). The theoretical guarantees about continuity and closure under limits are neither tested nor shown to be necessary for the results. This does not invalidate the theory, but the claimed "unified framework" is only partially realized in the experiments.

4. **In-distribution error degradation on Allen-Cahn not adequately explained.** LieLAC without fine-tuning increases the ID error from 6.448e-4 (Poseidon baseline) to 1.592e-3 — a 2.5× increase. Fine-tuning recovers to 9.667e-4, still above the baseline. The paper attributes this to canonicalized data falling off the training manifold (Section 5.3.3), but provides no quantitative analysis (e.g., measuring distance to the training distribution pre/post canonicalization). This leaves the reader uncertain whether the canonicalization is actively harming the model's core capability.

5. **No runtime or computational cost reporting.** The limitations section (Conclusion) mentions that energy-based canonicalization "tends to be rather slow" but provides no wall-clock times, number of gradient steps, or comparisons to alternative approaches. For a method intended to be practical, this is a notable omission that makes it impossible to assess the speed-accuracy trade-off.

6. **No statistical significance or error bars.** All reported results (Table 1 for MNIST, Table 1 for Allen-Cahn) are point estimates with no standard deviations or confidence intervals. Given the non-convex optimization with multiple restarts, variance across seeds should be reported.

### Trivial

7. **Table 1 (ACE) row labels are ambiguous.** The row "Poseidon + ft (can)" is unclear — does it mean Poseidon fine-tuned on canonicalized data or canonicalization fine-tuned on Poseidon? The row "LieLAC [Poseidon + ft.]" presumably means LieLAC applied to a fine-tuned Poseidon, but this should be clarified.

8. **Section 3.2 Hausdorff measure assumption.** The assumption that the Hausdorff measure of $\mathcal{M}_E(x)$ is non-zero is stated without substantive justification in the main text. While the paper refers to the appendix, the main text would benefit from a brief note on when this condition is expected to hold.

## Nice-to-Haves

- For heat and Burgers, even a single table reporting relative ℓ² error on transformed initial conditions with and without LieLAC would substantially strengthen the paper's central claim.
- A data-augmentation baseline for the Allen-Cahn experiment would directly test whether LieLAC offers advantages over the standard approach.
- Quantitative equivariance metrics (e.g., max logit variation over the group orbit) for the MNIST experiments would complement the t-SNE visualization.
- Runtime comparisons (LieLAC vs. augmentation training time) would contextualize the "rather slow" limitation.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Abstract phrasing criticism ("circumventing the need for knowledge of the full group structure")**: The paper's approach genuinely uses only Lie algebra actions (infinitesimal generators) for optimization; the explicit parameterizations for heat/Burgers are given for completeness but are not required by the method. This criticism misunderstands the paper. **Reason: Factually wrong/misunderstands the paper.**

- **Introduction wording criticism ("encodes a wider range of symmetries into model architectures")**: Canonicalization is a recognized architectural approach for encoding symmetries. This is a semantic nitpick. **Reason: Pure formatting/style nitpick.**

- **Claim that the paper doesn't state which PDE groups are solvable**: The paper explicitly states "6-dimensional solvable Lie algebra" for heat (line 332) and "5-dimensional solvable Lie algebra" for Burgers (line 352); Allen-Cahn's SE(2) is also solvable. **Reason: Factually wrong.**

- **Criticism about missing appendix content for heat/Burgers energy functions**: The appendix (sec:heat_ap, sec:burgers_ap) exists in the original submission and is stripped by the parser. The main text provides general energy construction principles in Section 4. **Reason: Parser-stripped appendix content.**

- **Minor section-by-section nitpicks about optimization variable parameterization**: The paper explains the approach (line 241-242: "optimization over the group can be reduced to optimization over a_6,...,a_1"). The critic's specific technical question about SL(2,R) decomposition is a reasonable implementation detail but not a methodological gap. **Reason: Overly specific implementation nitpick that the paper partially addresses.**

## Novel Insights

The reviews surface a useful structural observation that goes beyond the paper's own claims: the paper's theoretical framework for weighted closed canonicalizations is motivated by non-compact orbit-closure issues, yet the experiments sidestep these very issues (via discrete subgroups or global parameterizations). This creates a disconnect between the theoretical sophistication and the experimental validation that the paper does not fully acknowledge. A clearer discussion of exactly when the theoretical machinery is *necessary* versus merely *sufficient* would strengthen the narrative. The reviews do not surface any other genuinely novel insights beyond the paper's own contributions.

## Suggestions

1. **Add quantitative results for heat and Burgers PDE experiments.** This is the single most important improvement. Report relative ℓ² error of the operator on transformed initial conditions with and without LieLAC, compared to non-equivariant baselines. This is the minimal evidence needed to support the neural operator claim in the title and abstract.

2. **Include a data-augmentation baseline for the Allen-Cahn experiment.** Train Poseidon on data augmented with SE(2)-transformed initial conditions and compare OOD error to LieLAC. This would directly test whether canonicalization offers advantages over the simpler standard method.

3. **Provide error bars** for all reported results. Even 3 random seeds would give readers a sense of variability.

4. **Report wall-clock runtime** for the canonicalization step per sample, and clarify the computational overhead relative to baseline inference.

5. **Clarify Table 1 row labels** ("Poseidon + ft (can)" in particular) and add a brief discussion of why the ID error increases with LieLAC, perhaps with a quantitative analysis of the distance between canonicalized and training-distribution data.

## Score and Decision

The paper makes a genuine theoretical contribution to the canonicalization literature and demonstrates strong results on invariant image classification. However, the experimental core that motivates the paper—equivariant neural operators for PDEs—is critically under-supported: two of three PDE examples lack any quantitative evaluation, and the third shows mixed results without comparison to data augmentation baselines. The paper's framing promises more than the experiments deliver. With substantial strengthening of the PDE experiments, this could become a strong paper; in its current form, the contribution is incomplete.

**MY FINAL SCORE: <pineapple>5.5</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**