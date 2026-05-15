## Summary

This paper presents SC-VAE, a framework that combines conditional VAEs with parametric "scrubber" adversaries to disentangle nuisance variables (speed, heading direction, animal identity) from learned latent representations of 3D animal pose sequences. The method introduces several scrubber variants — linear (MALS), quadratic (MAQS), categorical quadratic discriminant (QD), and kernel-density MI estimation — that remove information about specified nuisance factors from latent codes while preserving behaviorally relevant structure. The authors demonstrate that parametric scrubbers (especially MALS, MAQS, QD) outperform adversarial neural-network scrubbers (gradient reversal, neural discriminator) on decodability metrics, that scrubbing reduces nuisance-driven over-segmentation in behavioral clustering, and that identity scrubbing via SC-VAE-QD improves disease detection in a Parkinsonian mouse model.

## Strengths

- **Parametric scrubbers reliably outperform adversarial neural-network baselines**: The paper shows that linear and quadratic scrubbing (SC-VAE-MALS, -MAQS) and QDA-based categorical scrubbing (SC-VAE-QD) achieve systematically lower nuisance decodability than gradient-reversal or neural-discriminator approaches across all three nuisance variables (Fig. 2a–c). This directly addresses a known practical difficulty in adversarial disentanglement — the sensitivity to architectural and hyperparameter choices of secondary networks.

- **Controlled disentanglement preserves behaviorally relevant structure**: The analysis of speed scrubbing is particularly thoughtful — the authors show that linear scrubbing (MALS) consolidates walking clusters that were previously split by speed differences, while nonlinear MI scrubbing goes too far and destroys meaningful behavioral group structure (Fig. 3e–g). This demonstrates a principled ability to *specify the degree* of disentanglement (linear vs. nonlinear), which is a genuine practical advance over methods that default to full invariance.

- **Improved biological phenotype detection by scrubbing animal identity**: In the Parkinsonian mouse model, SC-VAE-QD (identity scrubbing) yields the largest effect size, highest healthy/disease classification accuracy, and strongest correlation with dopamine denervation extent (Table 2). A reverse control (scrubbing the disease label) degrades performance, confirming that identity scrubbing specifically enhances disease-relevant signal rather than being a general artifact.

- **Practical self-tuning EMA removes hyperparameter search for the adversary**: The adaptive EMA smoothing factor (Appendix A.2) makes the MALS, MAQS, and QD scrubbers effectively hyperparameter-free in the sense that the adversary itself requires no manual tuning — a genuine practical improvement over gradient-reversal methods that need careful learning-rate balancing.

## Weaknesses

### Fatal
None.

### Major

- **The strongest biological validation is limited to identity scrubbing**: The PD experiment (Section 4.5, Table 2) — which is the paper's most compelling result — only tests identity scrubbing. Speed and heading disentanglement are evaluated on clustering metrics and motion synthesis consistency, but these are not validated against any biological ground truth (e.g., neural recordings, disease state, or behavioral assay). The paper's title and framing suggest a general framework for disentangling animal pose dynamics, but the evidence for practical biological benefit from speed/heading disentanglement is indirect. This does not invalidate the contribution, but it narrows what is directly demonstrated.

- **Missing comparison to relevant weakly-supervised or disentanglement baselines**: The paper compares only to VAE, C-VAE, gradient reversal, and neural discriminator. While these are reasonable baselines for the specific setting, a comparison to at least one standard disentanglement method from the broader ML literature (e.g., β-VAE or FactorVAE, which are cited in the related work) would strengthen the claim that SC-VAE offers a practical advantage. Without this, it is unclear whether the benefits come from the scrubbing framework per se or simply from the supervised/conditioned nature of the approach compared to purely unsupervised alternatives.

- **The motion synthesis evaluation (Table 1) is a sanity check, not a disentanglement test**: The R² between the conditioned input v and the resulting motion's measured speed/heading tests whether the decoder still uses v after scrubbing — a necessary sanity check. However, it does not test whether changing v while holding the latent code z fixed changes only the conditioned factor while leaving other behavioral attributes (gait, posture, action type) invariant. This weaker evaluation limits what can be concluded about the quality of disentanglement in the generative setting.

### Minor

- **No guidance on scrubber selection**: The results show that different scrubbers work best for different variables (MI for heading, MALS for speed, QD for identity), but the paper does not provide practical guidance on how to select the appropriate scrubber or scrubbing strength a priori for a new nuisance variable. The "different scrubbers for different independence levels" framing is honest about this trade-off, but it leaves practitioners without clear methodology.

- **Heading disentanglement matches rotation preprocessing, not a novel discovery**: The heading scrubbing results (Fig. 2a) show SC-VAE-MI and -MAQS matching the "VAE Processed" baseline — which is simply a VAE trained on rotationally-aligned data. The paper positions this as validation, which is fair, but it means the heading results are not a novel contribution beyond what standard preprocessing achieves.

- **Characterization of GR/ND training difficulty is qualitative**: The paper claims that gradient reversal and neural discriminator methods are "difficult to fine-tune" and "unreliable" (Section 3.4), which is a reasonable claim based on experience, but no quantitative evidence (convergence curves, variance across runs, hyperparameter sensitivity analysis) is provided to substantiate this. A few training curves or failure statistics would strengthen this claim.

### Trivial
None.

## Nice-to-Haves

- A sweep of the λ hyperparameter (balancing reconstruction vs. scrubbing) for one nuisance variable, showing the trade-off between reconstruction quality, decodability, and downstream clustering quality.
- Qualitative examples of generated sequences with controlled nuisances (same z, different v) to visually demonstrate what "disentanglement" looks like in the pose domain.
- Joint scrubbing of multiple nuisance variables simultaneously, which the paper identifies as future work but is a natural next step.

## Removed Points

- **Criticism about λ not being specified (from Harsh Critic Point 3)**: The paper references implementation details in Appendices B and C, which were stripped by the PDF parser. The λ hyperparameter is a standard balancing weight, and its specific values would typically appear in those sections. This is a parser artifact issue, not an author omission.
- **Criticism about missing Costacurta et al. (2022) comparison**: The paper explicitly explains that Costacurta et al. addresses time-series clustering (ARHMM) while SC-VAE aims to be a more general representation learning tool for broader tasks. Direct comparison is scope creep.
- **Criticism that speed results in Figure 2b are "confusing" (from Section-by-Section Notes)**: The paper's text clearly describes the speed results; the claim of confusion is the reviewer's inference from a figure they could not see clearly and does not reflect a verified error.
- **Several generic/duplicated strengths from Strength Finder** (generic phrasings about importance of the problem) that are already subsumed by the more specific strengths listed above.

## Novel Insights

The reviewers collectively surface an important tension in the paper: the SC-VAE framework's main differentiator — the ability to control *the degree* of disentanglement via parametric scrubber choice — is both its greatest strength and its least resolved aspect. The speed analysis (Section 4.4) shows that linear scrubbing (MALS) usefully consolidates speed-split walking clusters while nonlinear scrubbing (MI) destroys meaningful behavioral group structure. This is precisely the kind of nuanced control that prior adversarial methods lack. Yet the paper does not provide a principled way to determine, for a new variable, which scrubber to use or how strong the scrubbing should be. This creates an interesting design space that future work could formalize: can one estimate the "correct" level of disentanglement from the data itself (e.g., by monitoring how much cluster semantics change under different scrubbing strengths), or does this always require domain-specific judgment? The paper's honest discussion of this trade-off (Section 4.4 and 5) is commendable, but it also reveals that the framework currently shifts the burden of tuning from adversarial network architecture to scrubber family selection — a meaningful but incomplete solution.

## Suggestions

1. **Add a downstream biological validation for at least one of speed or heading scrubbing** — e.g., test whether speed-scrubbed representations improve detection of behavioral differences in a condition where speed is a confound (such as comparing two genotypes with different activity levels). This would directly support the broader claims of the title and abstract.

2. **Include one standard disentanglement baseline** (β-VAE or FactorVAE) on the same data, at least for the decoding and clustering metrics. This would contextualize whether the SC-VAE benefit comes from the conditioning/scrubbing framework or simply from supervised factorization.

3. **Provide a simple decision tree or heuristic** for scrubber selection based on variable type (continuous vs. categorical), expected independence from behavior, and practical tolerance for information loss.

4. **Report λ values and show a brief λ sweep** for one nuisance variable to demonstrate the operating regime and guide reproducibility.

## Score and Decision

This paper makes a genuine contribution to behavioral representation learning: the parametric scrubber family (MALS, MAQS, QD) is practically useful, the identity-scrubbing PD result is compelling, and the nuanced analysis of speed disentanglement (where full invariance is harmful) reflects thoughtful engagement with the problem. The weaknesses are real but not fatal — the main one is that the speed/heading claims lack biological validation, but the paper does demonstrate their utility on clustering and motion synthesis. The missing baseline comparison is addressable. The paper merits acceptance with the expectation that the authors engage with the limitations in the final version.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>