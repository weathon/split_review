- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 5, 6, 6
I now have a complete understanding of the paper and all reviewer claims. Let me write the final consolidated review.

## Summary

This paper presents an empirical study of how the feature learning strength ߡγ (the output scaling parameter in μP networks) interacts with the learning rate η in the online training setting. It maps a phase portrait in the γ–η plane exhibiting distinct regimes (lazy, rich, ultra-rich), identifies novel scaling laws for the optimal learning rate (η* ∝ γ² for γ≪1 and η* ∝ γ^{2/L} for γ≫1), and catalogs dynamical phenomena (catapults, silent alignment, stepwise loss drops). A one-parameter linear network model analytically reproduces the key scaling relationships. The paper also demonstrates that in the online setting, large-γ networks can match or exceed γ=1 performance, contradicting prior offline findings.

## Strengths

- **Comprehensive phase portrait across architectures and datasets**: The paper sweeps over 10+ orders of magnitude in both γ and η for MLPs (MNIST-1M), CNNs (CIFAR-5M), ResNets, and ViTs (TinyImageNet), producing consistent phase diagrams (Figures 1c,d) that match the analytical predictions. No prior work provides this breadth of empirical coverage for the γ–η plane in the online setting.

- **Novel depth-dependent learning rate scaling**: The identification that η* ∝ γ^{2/L} for γ≫1 (Section 3.1, Table 1) goes beyond prior treatments that only considered the lazy (γ²) scaling. This is derived analytically from a linear network model (Equation 7) and validated across architectures.

- **Demonstrates large-γ networks match/exceed γ=1 in the online setting**: Figure 2b shows that with sufficient training time, larger γ yields equal or better generalization than γ=1, directly contradicting prior offline results (Petrini et al., Sclocchi et al.). This resolves an apparent inconsistency by highlighting the role of data repetition.

- **Analytical derivation from a one-parameter linear network model**: The simple model in Section 4 reproduces all scaling boundaries (η_min, η_max, η_crit) for both MSE and cross-entropy (Table 1, Figure 7), providing a closed-form explanation that goes beyond prior toy models focused only on specific regimes.

- **Systematic Hessian analysis across γ**: Section 3.2 documents the Hessian spectrum transitioning from γ⁻² scaling (lazy) to γ^{-2/L} scaling (rich), and shows that in the rich regime many eigenvalues grow rather than just a few outliers (Figure 4d), providing mechanistic evidence for the sharpness bounds governing η scaling.

## Weaknesses

### Fatal

None.

### Major

- **Silent alignment evidence is thin relative to the generality claim.** The paper states that silent alignment "arises in a much broader class of realistic settings" (line 243) compared to prior work, but the only empirical demonstration in the main text is a single curve for an MLP on MNIST-1M (Figure 5b). The paper references additional experiments via figure labels (rich_consistency2, SA_MNIST_MLP, SA_CIFAR_CNN, ViT_plateau) but these are not visible in the main text. For a phenomenon highlighted as a central finding in the abstract and introduction, the evidence as presented in the main paper is insufficient to establish generality across architectures and datasets. This is a meaningful gap because the paper's broader claim about the value of the ultra-rich regime partly depends on these dynamical phenomena being robust.

- **Scaling exponents lack quantitative verification.** The paper claims scaling relationships η ∝ γ², η ∝ γ^{2/L} (phase boundaries), and λ_max ∝ γ^{-2/L} (Hessian), but these are supported only by dashed lines overlaid on figures (Figures 1c,d, 3a) that are described as visually matching. No quantitative fits (e.g., log-log slopes with confidence intervals) are reported. Given that the paper's core theoretical contribution is the *exact* scaling exponents, the absence of rigorous fitting weakens the precision of these claims. Small deviations from the predicted exponents would be masked without quantitative measurement.

### Minor

- **The "first convergent η" sweep procedure lacks an operational definition.** Line 151 describes sweeping "until the first convergent η is reached" without specifying the convergence criterion (loss threshold, accuracy plateau, gradient norm, or other). While the phase boundaries in Figures 1c,d are visually clear enough that different reasonable criteria would likely produce similar exponents, the procedure as described is not independently reproducible. The sensitivity of the reported boundaries to the choice of criterion is not discussed.

- **Progressive sharpening claim is not clearly linked to the evidence.** The text claims that sharpness growing to ≈2/η at the end of silent alignment is "shown in \cref{fig:SA}" (line 253), but the Figure 5b caption describes only loss and alignment curves. While sharpness evolution across time does appear elsewhere (Figure 3b-d), it is not explicitly aligned with the silent alignment phase. The connection between the two phenomena is asserted but not visually demonstrated in a single coherent presentation.

- **The toy model's scope is incompletely delineated.** The one-parameter linear network reproduces the scaling relationships (Section 4), which is its stated purpose. However, the paper also prominently features dynamical phenomena (silent alignment, stepwise loss drops) as characteristic of the ultra-rich regime, and the toy model cannot produce these behaviors (single weight, no symmetry breaking). The paper explicitly acknowledges this limitation for catapults (lines 401–404) but not for alignment or stepwise drops, potentially leaving readers unclear about which observations are explained and which remain purely empirical.

- **Function agreement analysis is qualitative.** Figure 6a is described as showing "nearly identical function outputs" without reporting a correlation coefficient, R², or other quantitative measure of agreement. The CKA plot (Figure 6b) shows small differences between γ values, and the claim that larger γ retains "slightly higher alignment" is not quantified or tested for significance.

### Trivial

None.

## Nice-to-Haves

- A quantitative characterization of stepwise loss drops: number of steps, inter-drop intervals, dependence on γ and depth L, and consistency across random seeds.
- Error bars or confidence intervals on the phase portrait boundaries (e.g., bootstrap over initialization seeds).
- A brief discussion or small-scale ablation of batch size effects, since the paper acknowledges that SGD noise is controlled by η/B (line 135) but B is fixed throughout.
- Reporting of the two-parameter model's results for catapults (currently deferred to appendix) in the main text would strengthen the theoretical narrative.

## Removed Points

These points from the original reviews were removed with justification:

1. **"Toy model section title overclaims by saying 'explains all observed scaling relationships'"**: The actual section title is "A Simple Model Explaining Observed Scalings." The sentence at line 282 says "explains all observed scaling relationships" — but this is explicitly about *scaling relationships*, not dynamical phenomena. The critic conflates the two. The paper's claim is appropriately scoped.

2. **"First to observe that transformers can reach the lazy limit may be overstated"**: This depends on knowledge of prior work outside the paper's citations. Following the rules, I cannot assess whether this claim is novel relative to unidentified references.

3. **"Code availability link not in main text"**: The link was present in the original submission (line 476); the parser stripped the URL. This is a parser artifact, not an author omission.

4. **"Missing appendix content (two-parameter model)"**: The appendix existed in the original submission; the parser strips these sections from all papers.

5. **"Offline vs online comparison needed"**: The paper explicitly discusses this limitation (Section 2.1) and the disagreement with offline results is presented as a finding (line 48). Requesting an offline comparison experiment is scope creep.

6. **"Batch size should be studied"**: Acknowledged but moved to Nice-to-Haves since the paper's scope is the γ–η interaction with fixed B.

7. **Generic criticisms about "evaluation lacks rigor" / "evidence is weak" without concrete anchors**: Removed per filtering discipline.

## Novel Insights

The two original reviews largely echo the paper's own contributions rather than generating outside perspective. One observation worth noting: the paper's finding that optimal online performance is often found at large γ (contradicting offline studies) suggests a deeper principle — that data repetition fundamentally changes the role of feature learning strength. This could imply that many practical recommendations about feature learning (derived from offline experiments) may not transfer to the large-scale, single-epoch training that is increasingly common. The paper stops short of drawing this broader implication, but it is a natural and important direction for future work.

## Suggestions

1. **Define the convergence criterion** used in the phase-portrait sweep (e.g., "η is convergent if test accuracy exceeds 30% after T steps") and report the sensitivity of the scaling exponents to threshold choice.

2. **Provide quantitative fits** for the scaling exponents: fit η_max ∝ γ^a in the lazy regime and η_max ∝ γ^{b(L)} in the ultra-rich regime, reporting a and b with confidence intervals from bootstrapped fits. Do the same for Hessian eigenvalues vs γ.

3. **Strengthen the silent alignment evidence** by showing at least one additional architecture/dataset in the main text (e.g., CNN on CIFAR-5M), or alternatively qualify the claim to match the evidence shown.

4. **Explicitly connect sharpness evolution to silent alignment** in a single figure (or clarify in the text which existing figures, together, support this claim).

5. **Add a correlation coefficient or R²** to the function agreement plot (Figure 6a) and note whether the CKA differences between γ values are statistically significant.

6. **Clarify the scope of the toy model's explanatory power**: state transparently which phenomena it explains (scaling relationships, phase boundaries) and which it does not (stepwise drops, silent alignment dynamics).
