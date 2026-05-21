Now I have enough anchoring. Let me synthesize the final review.

**Calibration summary (for the score report):**

**Round 1 bracketing (all scores on "instrumental variable neural network causal inference"):**
- Low band (avg ≤3.5): papers at 3.0-3.4 — papers with very weak methods, unclear contributions, or major errors
- Middle band (3.5-7.5): CBRL.CIV at 6.75 (accepted poster), DFIV at 6.67 (accepted poster), a rejected exposure shift paper at 5.0, and Learning Latent SCM at 4.0 (rejected)
- High band (7.5+): papers at 8.0 — Ooral/spotlight-level work

**Initial bracket:** Between 4.0 and 6.5 (the lower end of the middle band, below accepted papers)

**Round 2 narrowing (4.0-6.0 and 5.5-7.5):**
- ADR (avg 4.20, rejected) — decomposed representation learning with adversarial modules. Had theoretical errors and was rejected. Most similar to ZNet conceptually. ZNet is somewhat stronger empirically.
- CBRL.CIV (avg 6.75, accepted) — conditional IV with representation learning. Solid theory, competitive results. ZNet is significantly weaker.
- Post-treatment covariates paper (avg 5.50, rejected) — different problem.
- A variational framework (avg 7.33, accepted) — different focus.

**Final anchor comparison:** ZNet is stronger than ADR (4.20) but substantially weaker than CBRL.CIV (6.75). The Lemma 1 flaw is analogous in severity to ADR's theoretical errors. ZNet has more comprehensive experiments than ADR, so it's marginally above 4.2 — placing it around 4.5.

Now let me write the consolidated review.## Summary

This paper proposes ZNet, a deep learning architecture that learns instrumental variable (Z) and confounder (C) representations from observed covariates X by encoding three IV conditions (relevance, exclusion restriction, unconfoundedness) into a multi-part loss function. The method is designed to work both when true instruments exist in the data and when they do not. Experiments on semi-synthetic IHDP-based datasets across four data classes (disjoint/mixed/latent/no candidate) show ZNet can recover known instruments and produce competitive ATE estimates when paired with downstream estimators (TSLS, DeepIV, DFIV).

## Strengths

- **Empirical recovery of known instruments is well-demonstrated.** Figure 4 shows near-perfect recovery of a latent categorical instrument (diagonal confusion matrix). Figure 5 shows learned Z dimensions achieving R² ~0.84 in predicting true candidate instruments, with ablation verifying all three constraints contribute to recovery. This is concrete, replicable evidence that the method works when a ground-truth instrument exists.

- **Comprehensive evaluation across diverse instrument-existence scenarios.** The paper tests four data classes (disjoint candidate, mixed candidate, latent categorical, no candidate) with linear/nonlinear variants and with/without unobserved confounding — 10 distinct settings in Table 1. This is the most extensive head-to-head comparison of IV-generation methods (ZNet vs AutoIV, VIV, GIV) in the literature.

- **Demonstration of a valid proxy instrument when no explicit instrument exists.** In the non-linear no-candidate setting, ZNet's learned Z achieves F=15.34 for predicting T (relevance), passes the exclusion restriction test (p=0.813), and has low average absolute correlation with U (0.126 on test). This directly supports the paper's core claim that useful instrument representations can be constructed from data alone.

- **SCM-based architecture design.** Instead of learning variational distributions (as in AutoIV, VIV, GDIV), ZNet directly encodes IV conditions as loss terms derived from the structural causal model, giving direct control over each IV condition.

## Weaknesses

### Fatal
None.

### Major

- **Lemma 1 is mathematically incorrect, undermining the theoretical justification for Constraint 1 (unconfoundedness).** The proof in lines 95-98 contains a clear error: the step `𝔼[Z·e_Y] − 𝔼[Z]·𝔼[e_Y|X,T]` treats `𝔼[e_Y|X,T]` (a random variable) as a constant when factoring it out of the expectation. Since Z = g(X) is measurable w.r.t. (X,T), the covariance `Cov(Z, e_Y − 𝔼[e_Y|X,T])` is identically zero regardless of any properties of Z — the premise of Lemma 1 is always true, so the lemma does not establish that minimizing `Cov(Z, Y−Ŷ)` forces `Z⟂e_Y`. The paper's claim to "relax the assumption that observed variables are not influenced by U" (Section 7, Abstract) is therefore unsupported by theoretical argument. The decorrelation loss `PC(Y−Ŷ, Z)²` may still be useful as a heuristic, but the paper presents it as theoretically grounded. This is a meaningful gap between what is claimed and what is justified.

- **Abstract and introduction overstate the method's generality.** The abstract claims ZNet works "regardless of whether the (untestable) assumption of unconfoundedness is satisfied." The paper later acknowledges (Section 7) that "IV estimation in general is limited by a lack of theoretical guarantees of identifiability in the general case." The abstract claim conflates relaxing one specific assumption with removing all relevant assumptions, and the Lemma 1 flaw means even the relaxation of the unconfoundedness assumption is not theoretically supported.

- **No standard errors or confidence intervals in the main ATE table (Table 1).** Results are reported as mean ATE error across 50 bootstrap resamples, but without variance estimates the reader cannot assess reliability. The asterisk convention ("* indicates that the two best are significantly better than the third best; ** indicates best is significantly better than second best") is non-standard and the underlying significance test is not explained. For instance, in the Linear No Candidate dataset, ZNet TS2SLS gives 2.718 while ZNet DeepIV gives −0.033 — the same learned representation produces wildly different errors across estimators, but without error bars it is unclear whether this reflects high variance, tuning mismatch, or genuine estimator incompatibility.

### Minor

- **The hyperparameter weighting scheme (α₁–α₇) and the handling of gradient surgery are not reported.** The paper states that weights and PC/MI choices were tuned via Bayesian optimization with Pareto-front selection, but the final α values, architecture dimensions, and gradient surgery details (threshold/projection method) are not given. This limits reproducibility and makes it impossible to assess sensitivity to these choices.

- **The three-stage training procedure (pretrain Φ, pretrain f/g with only α₃,α₆, then full training) is presented without ablation.** It is unclear whether simpler end-to-end training would suffice or whether the staged procedure is critical. The use of gradient surgery suggests conflicting loss terms, raising the question of whether all constraints can be satisfied simultaneously, but this is not investigated.

- **The 1−PC² formulation for maximizing correlation is not equivalent to maximizing covariance.** As noted in the methods section, maximizing correlation by minimizing 1−PC² allows a trade-off with variance (since PC = Cov/(σ_A·σ_B)). The paper does not discuss whether this choice affects the learned representations compared to directly maximizing covariance.

- **Comparison to TrueIV is mixed.** In many settings (e.g., Linear Mixed, TS2SLS: TrueIV 0.263 vs ZNet 0.437; Nonlinear Disjoint, TS2SLS: TrueIV 0.266 vs ZNet 0.524), the ground-truth instrument outperforms ZNet. The paper's narrative of "comparable" performance is not consistently supported across cells.

### Trivial
- The proof layout in Lemma 1 uses `𝔼[Z]·𝔼[e_Y|X,T]` which is a random variable on one side of an equation of scalars — a clear typographic/notational error that reflects the deeper mathematical error.

## Nice-to-Haves
- Report ATE errors with 95% bootstrap confidence intervals across all datasets and methods.
- Add an ablation study where the three-stage training is compared to end-to-end training.
- Provide a corrected or removed Lemma 1, replacing it with a discussion of why the decorrelation of Z and Y−Ŷ is a reasonable heuristic for reducing dependence, without claiming it guarantees unconfoundedness.
- Include a real-world or externally validated semi-synthetic benchmark beyond IHDP.
- Report the final α weights and architecture dimensions obtained from Bayesian optimization.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Tuning procedure may favor ZNet because ZNet's architecture directly includes these objectives as loss terms"** — This is speculation, not a verified weakness. The paper uses the same multi-objective Bayesian optimization procedure for all IV-generation methods (ZNet, AutoIV, VIV, GIV), tuning each to maximize F-statistic and minimize C-Z correlation. Without evidence that the hyperparameter spaces differed in difficulty, this is conjecture rather than a concrete problem.

2. **"No standard errors or confidence intervals are reported" re: Figure 6** — Figure 6 reports F-statistics and p-values for relevance and exclusion restriction tests. These are inferential statistics; the critic's request for confidence intervals on top of p-values for this specific figure is reasonable as a nice-to-have but not a genuine weakness given that standard F-tests are reported.

3. **"The MI approximation via KDE with Gaussian kernels may be inaccurate in high dimensions"** — Speculative criticism without evidence of actual inaccuracy. The paper uses MI as an alternative to PC loss across all constraints, not as the primary mechanism.

4. **"The construction is described, but the specific covariates chosen as instrument candidates or confounders are not listed (they are said to be in the appendix)"** — The appendix is stripped by the parser; this information exists in the original submission. The data generation description in Section 6.1 is clearly described at the class level.

5. **Strength Finder: "Relaxation of the assumption that unobserved confounders do not influence observed data"** — This strength directly conflicts with the verified weakness about Lemma 1. Since Lemma 1 is flawed, the claimed relaxation is unsupported. This strength is removed.

6. **Strength Finder: "Practical training strategy with gradient surgery and Bayesian tuning"** — Generic. Using gradient surgery and Bayesian optimization is standard practice, not a distinctive strength.

7. **Strength Finder: Generic statements about the problem being important** — Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The review process revealed one insight the paper does not address: because `Cov(Z, e_Y − 𝔼[e_Y|X,T])` is identically zero when Z is a function of (X,T), any attempt to minimize this quantity is optimizing a tautology — the loss term `PC(Y−Ŷ, Z)²` only has empirical content to the degree that the estimate Ŷ = Φ(X,T) is imperfect. This means the unconfoundedness constraint is implicitly dependent on the quality of the first-stage regression, which is not discussed or analyzed in the paper.

## Suggestions

1. **Fix or remove Lemma 1.** The simplest path is to remove the lemma entirely, acknowledge that the decorrelation loss between Z and the residuals Y−Ŷ is a heuristic for encouraging unconfoundedness, and rely on the empirical evidence (Figure 6c shows low correlation with U) as justification rather than a flawed mathematical argument. This is honest and does not weaken the empirical contribution.

2. **Tone down the abstract.** Replace "regardless of whether the (untestable) assumption of unconfoundedness is satisfied" with a more precise statement like "relaxes the requirement that observed variables be known a priori as instruments, and provides empirical evidence of reduced bias due to unobserved confounding."

3. **Add bootstrap confidence intervals to Table 1.** Report the standard deviation or 95% CI alongside each mean ATE error. Without variance, the reader cannot judge whether ZNet's improvements over baselines are meaningful.

4. **Report the tuned hyperparameters** (α weights, hidden layer sizes, activation choices) and the gradient surgery details to aid reproducibility.

5. **Consider adding a real-data experiment or a widely-used semi-synthetic benchmark** (e.g., from the causal inference competition benchmarks) to strengthen external validity beyond the IHDP-based data generation.

## Score and Decision

**Calibration details:**

*Round 1 — Bracketing*: Three queries on "instrumental variable neural network causal inference" across score bands. Low band (avg ≤3.5): papers at 3.0-3.4, all rejected with serious flaws. Middle band (3.5-7.5): CBRL.CIV at 6.75 (accepted), DFIV at 6.67 (accepted), exposure shift paper at 5.0 (rejected), Learning Latent SCM at 4.0 (rejected). High band (7.5+): papers at 8.0 (oral/spotlight). Initial bracket: 4.0–6.5.

*Round 2 — Narrowing*: Two queries in (4.0, 6.0) and (5.5, 7.5). ADR paper (avg 4.20, rejected) — similar decomposed representation learning with adversarial modules; had theoretical errors (incorrect independence statements in proofs) and was rejected. ZNet is empirically stronger than ADR (more comprehensive evaluation, clearer instrument recovery) but has a similar theoretical flaw. CBRL.CIV (avg 6.75, accepted) — solid theory, competitive results. ZNet is substantially weaker due to the Lemma 1 flaw. Post-treatment covariates paper (avg 5.50, rejected) — different setting, hard to compare directly.

*Final positioning*: ZNet is above ADR (4.20) due to more comprehensive experiments and clearer evidence of instrument recovery, but well below CBRL.CIV (6.75) and DFIV (6.67) which have rigorous theoretical foundations. The Lemma 1 flaw is a serious gap between claimed and justified contribution, but the empirical results still have value. Score of 4.5.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>