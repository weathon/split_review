Now I have all the information needed. Let me produce the final review.

## Summary

The paper proposes Regularised Jump Models, adapting Regularised K-means (Witten & Tibshirani, 2010) to the Jump Model framework for joint regime identification and feature selection in time series. Instead of the Sparse Jump Model's approach of learning a separate weight vector via BCSS maximisation, the proposed models penalise cluster centres directly using L0, Lasso, Ridge, or Group-Lasso penalties. A simulation study compares these variants against Standard and Sparse Jump Models.

## Strengths

- **Direct penalisation of cluster centres is a well-motivated structural change.** The paper correctly identifies that the Sparse Jump Model selects features through a proxy weight vector **w** optimising BCSS (Definition 1.2), while the proposed models penalise the centre matrix **μ** directly (Definition 1.4, Eq. 1.6). The adaptation from Regularised K-means is clearly derived and the connection to the Jump Model framework is clean.

- **Systematic evaluation of four penalty variants.** The paper tests all four penalty functions (L0, Lasso, Ridge, Group-Lasso) within the Jump Model framework, yielding practical guidance: P1, P2, P3 outperform, P0 roughly matches the Sparse baseline.

- **Appropriate sparsity-aware initialisation.** Algorithm 3 adapts the initialisation from Witten & Tibshirani (2011) — candidate state sequences generated from subsets of features with the largest centre norms (1%, 2%, 5%, 10%, 25%, 50%, 100%) — for the Regularised Jump Model, acknowledging that sparsity-aware initialisation matters for convergence (Section 2.3, lines 168–170).

## Weaknesses

### Fatal
None.

### Major

1. **BAC is never defined.** The entire simulation study reports BAC values in Tables 2 and 3, but the paper never states what BAC stands for or how it is calculated. Balanced accuracy is the likely interpretation, but a reader cannot verify whether the metric is computed correctly, handles imbalanced regime durations, or aligns with prior work. The paper's central empirical evidence rests on an undefined quantity — this is unverifiable as presented.

2. **The feature-selection metric "(3.2)" is referenced but absent from the text.** Line 274 states that Table 3 reports "the BAC … of (3.2)" as the feature-selection performance metric. No equation (3.2) appears in the visible text — Section 3 contains Definition 3.1, Definition 3.2, and equation (3.1), but no equation (3.2). The feature-selection metric by which all methods are evaluated is therefore undefined. This makes Table 3, a core part of the contribution, uninterpretable.

3. **The data generating process is not described.** The simulation states only: "We adopt the same data generating process as in (9)" (line 271). The number of regimes *K*, the nature of regime means (how *μ* controls separation), the transition structure, the distribution of irrelevant features, and the noise distribution are all absent. A reader cannot interpret the simulation settings, assess their realism, or reproduce the study without consulting an external reference. Key details (e.g., the first 15 features being relevant) must be inferred from the results discussion.

4. **The central interpretability claim is asserted without demonstration.** The abstract and conclusion state that Regularised Jump Models perform "feature selection that is more interpretable" and "more direct" than the Sparse Jump Model's "feature selection by proxy." The paper never defines what "interpretable" means, never explains what "by proxy" entails (the Sparse Jump Model learns explicit feature weights **w** — a standard, interpretable mechanism), and provides no interpretability analysis (example weights, sparsity patterns, stability comparisons). This claim is rhetorical rather than evidential.

5. **The clustering-stability tuning method is proposed but never tested.** Section 3 devotes substantial space to a hyperparameter tuning method based on clustering instability, motivated by the inapplicability of the FTIC criterion to Regularised models. However, Section 4 never states whether this method was used to select hyperparameters, what hyperparameter values were chosen, or whether the method was validated. The tuning proposal is entirely disconnected from the paper's only empirical evidence.

6. **The instability estimator has a label-alignment flaw.** Equation (3.1) computes instability as $\binom{10}{2}^{-1}\sum_{i<j}\sum_{t}\mathbf{1}_{\{\hat{s}_t^i \neq \hat{s}_t^j\}}$ — counting per-time-step disagreements between state sequences from different bootstrap samples. This comparison requires that state labels (1,...,K) are aligned across samples; otherwise, permutation-invariant clusterings can produce arbitrarily inflated instability. The paper does not mention any alignment procedure (e.g., the Hungarian algorithm), which is a standard requirement when comparing clusterings.

### Minor

- **Ridge (P2) is evaluated for feature selection without explanation.** The Ridge penalty ($\mathcal{P}_2$, sum of squared L2 norms) shrinks coefficients but never drives them exactly to zero. Table 3 reports feature-selection BAC for $\mathcal{P}_2$, but the paper never explains whether post-hoc thresholding is applied or how this variant produces discrete feature selection. This is internally inconsistent with the paper's framing.

- **Outperformance is modest and context-dependent.** Regularised models outperform the Sparse Jump Model only for $\mu \geq 0.5$ and $P < 300$, and even there only "some cases" are statistically significant (bold entries). For $\mu=0.25$ and $P=300$, all models produce nearly identical BACs (0.334–0.344). This qualifies the findings.

- **No correction for multiple comparisons.** The Wilcoxon signed-rank test ($\alpha=0.05$) is applied across 4 penalty variants × multiple settings without adjustment for multiple testing.

- **The Spearman correlation p-value is of questionable validity.** The p-value of $\mathcal{O}(10^{-24})$ (line 278) is computed on "unbundled" BACs across all conditions, which are not independent observations (they are means of 100 simulations at each setting). The reported p-value is not a valid test statistic as presented.

### Trivial
- References to "Step 8.1" and "Step 8.2" (lines 172, 180) do not correspond to numbered steps in Algorithm 4.

## Nice-to-Haves
- Including a non-Jump baseline (e.g., HMM) would position results relative to standard alternatives; the paper's scope-bound justification for excluding them (line 271–272) is noted but the limitation remains.
- The DGP could be summarised in a brief table (K, transition probabilities, how μ controls separation) rather than only citing (9).
- The label-alignment issue could be resolved by describing a simple alignment scheme for the instability estimator.

## Removed Points
These points were flagged during review but are removed with justification:
- **"No non-Jump baselines"** — The paper explicitly justifies this (line 271–272). Criticising its absence when the paper scopes the comparison to "within Jump Model framework" is scope creep. Included as Nice-to-Have instead.
- **"Algorithm percentages lack justification for time-series setting"** — These percentages are taken directly from (11); criticising them without evidence that they are inappropriate for Jump Models is speculative.
- **"Notation confusing (Definition 1.2 vs equation 1.3)"** — Minor notation issue that does not affect correctness; parser may have altered numbering.
- Formatting/style nitpicks — Parser artifacts, not author errors.
- Strength about clustering-stability tuning being a "principled non-parametric alternative" — This is an overstatement since the method is proposed but never validated; removed from strengths.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Define BAC explicitly (including the formula) and define the feature-selection metric clearly — these are the paper's only quantitative evidence.
- Describe the DGP in sufficient detail (at minimum: K, transition matrix, how μ controls feature separation, noise distribution) so the reader can evaluate the simulation without consulting (9).
- Either demonstrate interpretability concretely (show example weights/shrunken centres, sparsity patterns) or remove the claim from abstract and conclusion.
- Either use and report the proposed tuning method in the simulation, or state how hyperparameters were chosen and drop Section 3.
- Acknowledge the label-alignment requirement for the instability estimator and describe how it is addressed.
- Explain how the Ridge (P2) variant produces feature selection, or treat it as a regularisation-only variant not expected to select features.
- Report whether multiple comparisons were controlled in the Wilcoxon tests.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>