Now I have carefully verified all claims against the paper. Let me synthesize the final review.

## Final Review

## Summary
This paper introduces Scrubbed Conditional VAEs (SC-VAE), a framework for disentangling nuisance variables (speed, heading direction, animal identity) from 3D animal pose sequences. The key innovation is replacing neural-network-based adversarial discriminators with analytically computed "scrubbers" — linear (MALS), polynomial (MAQS/MACS), quadratic discriminant (QD), and kernel-density mutual information (MI) estimators — whose sufficient statistics are maintained via exponential moving averages. The method is evaluated on disentanglement metrics, motion synthesis, behavioral clustering, and disease detection in a mouse model of Parkinson's disease, with the PD application providing the most compelling evidence of practical value.

## Strengths
- **Novel and practical EMA-based scrubber methodology**: The idea of replacing adversarial neural networks with analytically computed scrubbers using exponential moving averages of sufficient statistics (Eqns 4-6) is clever and practically valuable. The self-tuning EMA mechanism (Section 3.5) addresses a real difficulty in adversarial training. This directly supports the paper's core methodological contribution.

- **Effective disentanglement of heading direction validated against a rotationally-preprocessed gold standard**: SC-VAE-MALS achieves linear invariance matching rotationally preprocessed data, and SC-VAE-MAQS/MI reach nonlinear decodability equal to the fully preprocessed optimum (Section 4.2, Fig. 2a). This is a clean validation because the "ground truth" optimal representation (VAE Processed) is known, providing an unambiguous upper bound.

- **Enhanced disease detection in a Parkinsonian mouse model provides strong biological validation**: Scrubbing animal identity with SC-VAE-QD increases the effect size between healthy and PD sessions, improves healthy-vs-disease classification accuracy, and strengthens the correlation between behavioral change and dopamine denervation extent (Section 4.5, Table 2). The "Reverse Control" (scrubbing disease label) further supports the specificity of the effect. This experiment demonstrates real biological utility beyond synthetic metrics.

- **Nuanced treatment of disentanglement strength**: The paper demonstrates that different nuisances require different levels of disentanglement — heading admits complete removal, while speed requires weaker scrubbing to preserve behavioral semantics (Section 4.4, Fig. 3). This insight goes beyond the typical "fully invariant" approach and is a genuine strength of the empirical analysis.

- **Improved conditional motion synthesis**: All scrubbed models improve the $R^2$ between conditioned inputs and generated sequence properties compared to a vanilla C-VAE (Table 1), showing that disentanglement does not harm — and can improve — generative fidelity.

## Weaknesses

### Fatal
None.

### Major
- **Fairness of comparison to adversarial baselines is not fully established**: The paper frames neural-network-based adversaries (SC-VAE-GR, SC-VAE-ND) as unreliable and hard to tune (Sections 1, 3.4, 5), and uses their relatively poor performance as partial motivation for the EMA methods. However, no evidence is provided of systematic hyperparameter search (learning rates, architectures, training schedules) for these baselines. The paper acknowledges they "can work if one carefully tunes separate learning rates" (line 91) but does not document the tuning effort. The EMA methods, by contrast, benefit from dedicated algorithmic design (self-tuning filters, closed-form solutions). Without evidence of symmetric tuning effort, the claimed superiority of EMA scrubbers over neural adversarial methods is suggestive but not conclusive. The paper's core contribution (EMA scrubbers) stands independently, but the comparative claims should be softened or better supported.

### Minor
- **The "hyperparameter-free" claim (Section 5, line 181) is overstated**: The MALS scrubber has an L2 regularization constant β (Equation 4, line 101), and the self-tuning EMA mechanism uses "a small, fixed difference" between parallel smoothing factors (line 107) — both are hyperparameters. The method genuinely has far fewer hyperparameters than neural-network adversaries (no architecture choices, no separate learning rates), which is a genuine advantage. But claiming it is strictly "hyperparameter-free" is imprecise and invites deserved skepticism. The paper would be stronger by saying "effectively hyperparameter-free" or "requiring minimal hyperparameter tuning."

- **Disease analysis (Section 4.5, Table 2) lacks uncertainty quantification for some key metrics**: Classification accuracy and Pearson r are reported without confidence intervals, standard errors, or p-values. With 36 mice, the accuracy values could benefit from bootstrap-resampled confidence intervals. The correlation magnitudes (r = 0.29–0.38 across models) are similar, and the claim that SC-VAE-QD "strengthened the correlation" is not assessed for statistical significance. The effect size (d) does include SEM, which is good, but the other metrics need similar treatment. The "Reverse Control" results should be reported with comparable numerical values alongside the other models for direct comparison.

- **The clustering evaluation (Section 4.4) demonstrates nuisance removal but does not directly validate that the resulting clusters correspond to semantically meaningful behaviors**: The walking clusters are identified from a vanilla VAE and defined by their speed/heading distributions. The evaluation shows that scrubbing collapses these clusters — which measures nuisance removal (already shown by decodability). The stronger claim that scrubbing reveals "typical coarse behavioral labels (e.g., walking, rearing, grooming)" (line 159) is asserted but not directly validated with ground-truth annotations. This does not undermine the paper's main contribution, but a small set of human-annotated labels would strengthen the behavioral interpretability claim.

- **SC-VAE-MAQS not affecting speed disentanglement is acknowledged but unexplained**: The paper notes that MAQS "did not affect speed disentanglement" (line 142) without speculation on why — e.g., whether speed has strong nonlinear interactions with pose not captured by quadratic features, or whether the polynomial augmentation requires a different λ. A brief discussion would improve scientific completeness.

### Trivial
- **Notation clarity**: $I_f$ is defined in Equation 2 (line 65) as a max over ψ, then used as $L_{\mathrm{scrub}}(\phi)$ (line 68). After maximization it is a constant w.r.t. ψ but still a function of φ, which is clear in context but could be stated explicitly.

- **Session pairing**: The PD dataset (36 mice, before and after lesion) should state explicitly whether sessions from the same animal are kept paired during evaluation (e.g., leave-one-animal-out for the k-NN classifier).

## Nice-to-Haves
- A β-VAE baseline (without explicit conditioning) would contextualize the benefit of using explicit nuisance variables, though this is not essential given the paper's focus on supervised disentanglement.
- A sweep of λ (the scrubber weight) for a single nuisance (e.g., speed), plotting decodability vs. a behavioral metric, would concretely illustrate the controllable disentanglement the paper claims as an advantage.
- Bootstrapped confidence intervals or permutation tests for the classification accuracy and correlation in Table 2.
- Human-annotated behavior labels (even a few hundred frames) to ground-truth the claim that scrubbing produces semantically coherent clusters.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **Missing appendix content (self-tuning EMA details, architecture specs)**: Removed per hard rules — the parser strips appendix sections from all papers; they exist in the original submission.
- **"β is never discussed"**: The paper explicitly states β is the L2-regularization constant (line 101), though the chosen value is not given. The critic's claim of "never discussed" is inaccurate.
- **"C-VAE heading R² is 0.17 — surprisingly low"**: This is consistent with the paper's own claim that C-VAE does not fully exploit conditioning, and actually supports the paper's motivation for needing stronger disentanglement.
- **"MAQS shows higher linear decodability than C-VAE for speed"**: The paper states MAQS "did not affect speed disentanglement" (line 142). The critic's claim of *higher* decodability is not verifiable from the text and may misread Figure 2b, which is not visible in the text.
- **Missing related work on β-VAE**: Removed per hard rules — do not mention missing related works.

## Novel Insights
None beyond the paper's own contributions. The reviews identify evidential gaps (asymmetric tuning, missing error bars) but do not reveal structural problems or unforeseen implications not already discussed by the authors.

## Suggestions
- Document the hyperparameter search attempted for SC-VAE-GR and SC-VAE-ND (learning rate ranges, architectures tried, compute budget) or soften the comparative claims to "in our experience" rather than presenting failure as an inherent property of the methods.
- Add confidence intervals (bootstrap) for the classification accuracy and Pearson r in Table 2; report the "Reverse Control" with comparable numerical values.
- Qualify the "hyperparameter-free" claim (Section 5) to "effectively hyperparameter-free" or "requiring minimal hyperparameter tuning" and explicitly list the residual parameters (β, EMA delta) and their chosen values.
- Add a brief speculation for why SC-VAE-MAQS did not affect speed disentanglement (e.g., nonlinear interactions beyond quadratic, or an interaction with the choice of λ).
- Include a small human-annotated validation set for the clustering analysis to strengthen the behavioral interpretability claims.

## Score and Decision
The paper presents a novel, well-motivated framework with compelling empirical validation across multiple tasks and a real biological application. The method is clearly described and the experiments are extensive. The weaknesses — primarily concerning the fairness of the adversarial baseline comparison, an overclaimed "hyperparameter-free" statement, and missing error bars in one table — are fixable without undermining the core contribution. The paper makes a clear contribution to behavioral representation learning.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>