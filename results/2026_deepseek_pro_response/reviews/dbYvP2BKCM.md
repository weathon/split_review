Now I have enough calibration data to make a final assessment. Let me compile the final review.

**Calibration summary across all rounds:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `jFox1iMWUa` (Causal NN for continuous TE) | 3.40 | R1 weak | ZNet clearly stronger — better architecture, more comprehensive experiments |
| `AvXrppAS2o` (Causal structure learning) | 3.00 | R1 weak | ZNet clearly stronger |
| `4u0ruVk749` (DFITE diffusion model) | 3.00 | R1 weak | ZNet clearly stronger |
| `5AJ8R4z5g0` (Potential outcomes w/ hidden confounders) | 3.25 | R1 weak | ZNet clearly stronger |
| `F7XPZnIUHh` (ADR decomposed representations) | 4.20 | R1 middle | ZNet stronger — cleaner architecture, more comprehensive evaluation, no derivation errors |
| `q07DDpu8Xb` (Distribution shifts for identifiability) | 5.25 | R2 narrow | ZNet comparable — both have theory gaps, ZNet has better empirical contribution |
| `kz5igjl04W` (Latent space causal inference) | 5.50 | R2 narrow | ZNet comparable, different domains |
| `DqD59dQP37` (Causal fairness) | 5.67 | R2 narrow | Different domain, hard to compare directly |
| `wFf9m4v7oC` (CFDiVAE — front-door VAE) | 5.75 | R2 narrow | CFDiVAE has stronger theory but weaker experiments; ZNet has slightly worse theory but much better experiments. ZNet slightly below. |
| `hjROBHstZ3` (Causal representation from multimodal) | 5.80 | R2 narrow | Different domain, stronger theory |
| `qDhq1icpO8` (CBRL.CIV) | 6.75 | R1 middle | CBRL.CIV clearly stronger — rigorous theory, accepted |
| `Oc4ji1iCjQ` (ShadowCatcher) | 6.75 | R1 middle | ShadowCatcher stronger — better theoretical grounding despite rejection |
| `3cuJwmPxXj` (Intervention extrapolation) | 8.00 | R1 strong | ZNet clearly below — these are top-tier papers |

**Round 1 bracket**: 4.5–6.5

**Round 2 narrowing**: ZNet sits between `q07DDpu8Xb` (5.25, rejected) and `wFf9m4v7oC` (5.75, accepted). ZNet is stronger than the 5.25 paper but has more significant theoretical issues than the 5.75 paper. The theoretical gap (Lemma 1 misapplication), structural insufficiency of the exclusion enforcement, and overclaiming of results place ZNet at approximately **5.0**.

---

## Summary

ZNet proposes a deep learning method that decomposes observed covariates X into a confounder representation C = f(X) and an instrument representation Z = g(X) by encoding the IV structural causal model directly into the network architecture and multi-term loss function. The method enforces the three IV conditions (relevance, exclusion restriction, unconfoundedness) through explicit covariance constraints, with a Lemma providing theoretical motivation for the unconfoundedness loss. ZNet serves as a front-end for downstream IV estimators (TSLS, DeepIV, DFIV) and is evaluated on semi-synthetic datasets derived from IHDP across nine data-generation settings including scenarios with and without pre-existing instruments. The core practical contribution is the ability to construct instruments from observational data even when no pre-existing instrument is available among observed covariates.

## Strengths

- **SCM-encoding architecture as a clean alternative to variational methods**: ZNet's architecture (Section 5, Figure 3) directly encodes the IV structural causal model through four sub-networks (Φ, f, g, π) with explicit loss terms targeting the three IV conditions. This contrasts with prior IV generation work (AutoIV, VIV, DVAE.CIV, GDIV) that relies on variational distributions or VAEs without architectural guarantees for IV condition satisfaction. The direct encoding of the causal structure into the loss function is conceptually appealing and provides interpretable constraints.

- **Comprehensive empirical evaluation**: Table 1 reports ATE errors across 9 dataset variants spanning linear and non-linear versions of Disjoint, Mixed, Latent, and No Candidate settings, with 50 bootstrap resamples. ZNet is compared against TrueIV, three competing IV generation methods (AutoIV, VIV, GIV), TARNet, and Diff Means, each evaluated with three downstream estimators (TSLS, DeepIV, DFIV). ZNet is on average the highest performing among IV generation methods.

- **Validated recovery of ground-truth instruments**: Figure 4 demonstrates perfect recovery (1.00 on all diagonal entries) of a 5-class latent categorical instrument via K-Means on ZNet's Z. Figure 5 shows that ZNet's 10-dimensional Z achieves high multivariate regression R² (0.84, Figure 5c) in predicting the true instruments X₁₃, X₁₄, X₁₅. The ablation in Figure 5c confirms that removing any single constraint degrades recovery, and removing all constraints drops R² to near zero (0.02–0.05), establishing that the architectural constraints are causally responsible for instrument recovery.

## Weaknesses

### Fatal

None.

### Major

- **The theoretical justification for the unconfoundedness loss is unsound in practice**: Lemma 1 proves that if Z ∼ N(0,σ²) and Cov(Z, e_Y − E[e_Y|X,T]) = 0, then Cov(Z, e_Y) = 0. The paper uses a trained neural network Φ to approximate E[Y|X,T] and minimizes PC(Y − Φ(X,T), Z)² as a proxy for Cov(Z, e_Y − E[e_Y|X,T]) = 0. But Y − Φ(X,T) = (e_Y − E[e_Y|X,T]) + (E[Y|X,T] − Φ(X,T)), where the second term is model approximation error. The Lemma's premise requires Φ = E[Y|X,T] exactly, which is never satisfied with finite-capacity networks and finite samples. Z could be correlated with the model error component, so minimizing PC(Y−Φ(X,T), Z)² does not guarantee Cov(Z, e_Y − E[e_Y|X,T]) = 0. The unconfoundedness loss term (Equation 6) does not rest on the theoretical bridge the paper claims. The loss may serve as a reasonable heuristic, but the paper presents it as theoretically grounded when it is not.

- **The exclusion restriction is not structurally enforced by the proposed losses**: The paper enforces exclusion restriction via (i) maximizing PC(C,Y) and minimizing MSE(C,Y), and (ii) minimizing PC(C,Z). This is insufficient: zero correlation between C and Z plus C predicting Y does not prevent Z from carrying Y-relevant information through nonlinear pathways orthogonal to C in correlation. The condition that Z is excluded from the outcome equation means Z carries no information about Y beyond what C and T already capture. The loss provides no structural barrier to Z encoding X→Y information that happens to be decorrelated from the learned C. The empirical test in Figure 6b partially addresses this for one dataset, but does not resolve the architectural gap.

- **Evidence for instrument validity in the "No Candidate" setting is weaker than claimed**: Figure 6, the centerpiece demonstration that ZNet works when no instrument exists, shows test-split relevance of F = 1.83 with p = 0.0813 — not significant at α = 0.05 (line 292). The paper nonetheless claims the instrument is "relevant" (Figure 6 caption, line 319). Meanwhile, non-significant exclusion p-values (0.446, 0.461, 0.813 on train/val/test) are interpreted as confirmatory evidence that Z adds nothing to Y prediction, despite the test having negligible power on the test split (F = 0.06). The paper applies asymmetric standards: borderline non-significance is dismissed for relevance but treated as confirmation for exclusion. With only ~200 test points, these tests have limited power in either direction, and the conclusions drawn exceed what the statistical evidence supports.

### Minor

- **Hyperparameter tuning may favor ZNet**: All IV generation methods (ZNet, AutoIV, GIV, VIV) are tuned via Bayesian optimization to maximize relevance F-statistic and minimize C-Z correlation (line 165) — metrics that ZNet's loss function is explicitly designed to optimize. Methods using variational objectives may not map cleanly to these metrics. Tuning all methods against ZNet's design criteria creates a circularity that weakens the comparative conclusions.

- **Overclaimed "comparable" performance to TrueIV**: The paper states ZNet's performance is "comparable to using the ground truth instrument" (line 323), but Table 1 shows substantial gaps: in Linear Disjoint, TrueIV TSLS error = −0.002 vs. ZNet TSLS = 0.119 (60× larger); in Non-linear Disjoint, TrueIV TSLS = 0.266 vs. ZNet TSLS = 0.524 (97% larger). ZNet is the best among IV generation methods, but the gap to TrueIV is meaningful and the claim of comparability should be qualified.

- **Limited data diversity**: All datasets are constructed from a single base source (IHDP, n = 985, d = 25). While the paper varies the data-generating process in multiple ways, using only one base dataset limits confidence in generalization beyond this distribution.

- **Missing baselines in the No Candidate setting**: The No Candidate setting — the most important for the paper's core contribution — compares only against TARNet (which assumes no confounding) and other IV generation methods. Methods specifically designed for unobserved confounding without instruments (e.g., proximal causal inference, negative control methods) are not compared, though they would be natural competitors in this regime.

### Trivial

- The paper lacks an explicit limitations section despite proposing a method for a difficult problem where failure modes (additive error model violations, poor local minima in multi-objective optimization) deserve honest discussion.

- No ablation comparing PC-based vs. MI-based loss formulations is provided, leaving unclear whether the linear correlation constraint is sufficient or the MI variant meaningfully improves performance in nonlinear settings.

## Nice-to-Haves

- Adding a direct exclusion loss that penalizes the predictive power of Z for Y after conditioning on C and T (e.g., training an auxiliary network to predict Y from (C, T, Z) and penalizing Z's marginal contribution) would more directly target the exclusion restriction.
- Experiments on at least one additional base dataset beyond IHDP (e.g., Twins, Jobs, or a custom simulation) would strengthen generality claims.
- Reporting partial R² of Z in Y ~ C + T + Z and correlation of Z with U (since U is known in simulation) for all datasets, not just the showcase Figure 6 dataset, would improve transparency and allow readers to independently assess instrument validity.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic claim about DVAE.CIV and GDIV not being compared in experiments**: The paper mentions both in related work (Section 4, line 113) but does not compare against them. This is a legitimate missing baseline concern but was already incorporated under "Missing baselines in the No Candidate setting" above. Removed the standalone criticism about these specific methods to avoid duplication.
- **Strength Finder claim that "Lemma 1 provides a theoretical basis for the unconfoundedness loss"**: The lemma is mathematically correct but its application to the training setup is flawed (see Major weakness 1). The lemma alone does not constitute a strength because it does not actually support the method as claimed. Removed.
- **Strength Finder claim about "gradient surgery addresses conflicting multi-objective losses"**: Gradient surgery is mentioned in one sentence (line 163) and tuned as a binary hyperparameter with no ablation showing its effect. This is a reasonable engineering choice but too thin to list as a standalone strength. Removed.
- **Harsh Critic claim about "no limitations section"**: The paper does lack a limitations discussion, but this is a presentation issue. Moved to Trivial.
- **Harsh Critic point about statistical testing protocol (*/**) not formally defined**: True (no formal test type, confidence level, or multiple comparison correction specified) but this is a presentation concern, not a methodological flaw. Removed.
- **Strength Finder's generic claims** about the problem being important or the approach being well-motivated — removed as superficial.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Either fix the Lemma 1 argument (e.g., derive a bound on the bias from model approximation error) or reframe the unconfoundedness loss as a pragmatic heuristic rather than a theoretically-grounded constraint. The current presentation claims a level of theoretical rigor the method does not actually achieve.
- Report a full calibration table of IV condition satisfaction (F-statistics with p-values, partial R² of Z in Y ~ C + T + Z, and correlation of Z with U) for every dataset and method, not just for the Figure 6 showcase.
- Weaken the "comparable to TrueIV" and "recovers true instruments" language to match what the evidence actually supports — ZNet learns representations correlated with true instruments and outperforms other IV generation methods, but does not match TrueIV performance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>