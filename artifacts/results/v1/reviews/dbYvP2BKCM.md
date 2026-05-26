## Summary

This paper proposes ZNet, a neural network method that learns instrument (Z) and confounder (C) representations from observed covariates X by enforcing covariance-based versions of the three IV conditions (unconfoundedness, exclusion restriction, relevance) through a multi-task loss. The learned representations are then used with standard downstream IV estimators (TSLS, DeepIV, DFIV) for causal effect estimation. The key claimed advantage is that ZNet can construct valid instrument representations even in settings where no explicit instrument exists among the observed variables.

## Strengths

1. **Empirical recovery of ground-truth instruments.** ZNet learns Z representations that are highly correlated with known instrument variables when they exist. Figure 5a shows univariate correlations up to ~0.8 between ZNet's Z and true instruments X₁₃, X₁₄, X₁₅ in a linear mixed candidate dataset. Figure 4 shows near-perfect recovery of a 5-class latent categorical instrument (confusion matrix with 1.0 along the diagonal). The ablation study in Figure 5c confirms that each loss constraint contributes to this recovery.

2. **Lemma 1 relaxes a restrictive assumption.** The theoretical lemma shows that if Z ~ N(0,σ²) and Cov(Z, e_Y−𝔼[e_Y|X,T]) = 0, then Cov(Z, e_Y) = 0. This provides a principled loss term for unconfoundedness that does not require the (standard but restrictive) assumption that unobserved confounders U do not influence the observed covariates X. This is a genuine theoretical advance over prior IV-generation methods (AutoIV, VIV, GIV) that make this assumption.

3. **Competitive ATE estimation across multiple data generation processes.** In Table 1, ZNet combined with downstream estimators wins in 18/30 estimator-dataset combinations among IV generation methods (vs. AutoIV: 7, VIV: 5, GIV: 5), supporting the paper's claim of strong average performance. The evaluation spans 8 data-generation types (linear/nonlinear × 4 instrument scenarios) with 3 downstream estimators and 3 competitive baselines.

## Weaknesses

### Major

1. **Loss functions encode necessary (covariance) conditions, not sufficient (independence) conditions for the IV criteria — the central guarantee claim is unsupported.**  
The paper defines the IV conditions as (i) Z ⟂ e_Y | C (unconfoundedness), (ii) Z only enters φ through T (exclusion restriction), and (iii) Z ⟂̸ T | C (relevance). Yet the loss enforces only: Cov(Z, residual)=0 (with normality), Cov(C,Z)=0 plus Cov(C,Y)>0, and Cov(T,Z)>0. Covariance zero ≠ independence (except under joint normality, which is not established), and these are all *unconditional* constraints. The paper states: "Solutions to the ZNet loss minimization problem will always give a representation that serves as an instrument" (Section 7). This claim is not supported — the loss minimization does not guarantee Z ⟂ e_Y | C (conditional independence), does not guarantee Z has no direct effect on Y, and does not guarantee Z ⟂̸ T | C (conditional relevance). The footnote indicates the authors aim to construct Z,C independent to make Z an unconditional IV, but even then, zero covariance between Z and C does not guarantee independence, and zero covariance between Z and e_Y does not guarantee Z ⟂ e_Y. The gap between what is optimized and what is required for valid IV inference is nontrivial and unaddressed. **This is the most significant weakness — it means the core claim of guaranteed instrument validity is overstated.**

2. **Empirical evaluation uses a single base dataset (IHDP, N=985).** While the paper creates 8 distinct data-generation configurations, all are built from the same 25 covariates of the IHDP dataset (a common causal inference benchmark with 985 units). This limits the generality of the findings. Claims about "plug-in causal inference estimator" for general observational settings would be substantially strengthened by results on other benchmarks (e.g., News simulated data, ACIC frameworks, or a real-world application with a known instrument). The strong practical motivation given in the introduction (EHR data, consumer AI tools) is not matched by any non-IHDP experiment.

3. **Non-significant test-set relevance in the No Candidate setting.** In the Nonlinear No Candidate dataset (Figure 6a), the test-set F-statistic for relevance (Z predicting T) is F=1.83, p=0.0813 — not significant at conventional levels. The paper nonetheless reports good ATE estimates for this setting (Table 1: Nonlinear No Candidate, ZNet+DFIV error = 0.049). When the learned Z is not significantly related to T on held-out data, it is unclear what is identifying the treatment effect. The paper does not discuss this discrepancy or provide a mechanism by which ATE estimates could remain valid despite weak/redundant relevance.

4. **Incomplete reporting of experimental uncertainty.** Table 1 reports mean ATE error across 50 bootstrap resamples with significance stars (*/**), but no standard deviations or confidence intervals are provided, and the statistical test used for the significance stars is not described. This makes it impossible to assess the variability and reliability of the reported comparisons.

### Minor

5. **No real-world data experiment.** Despite the strong practical motivation (Section 1), the paper contains no real-world application. A single experiment with a validated instrument on real data would substantially strengthen the claim of practical utility.

6. **Dimension of learned representations (C, Z) not discussed.** The paper mentions Z is 10-dimensional in one specific setting but does not discuss how this is chosen in general, whether sensitivity analysis was performed, or what the dimensionality of C is. This is a critical architectural choice whose impact on downstream performance is not analyzed.

7. **The significance test used for Table 1 is not described.** The caption states that "*" indicates "the two best are significantly better than the third best" and "**" indicates "the best is significantly better than the second best," but the statistical test (e.g., paired bootstrap, permutation test) is not specified.

### Trivial

None.

## Nice-to-Haves

- A comparison with a simple "all X as instruments" baseline (over-identified linear IV) would help gauge whether the learned representation adds value beyond naively using all covariates.
- A sensitivity analysis of the Z and C dimensionality hyperparameter would be informative.
- The three-stage training procedure and gradient surgery suggest the loss landscape is complex; an analysis of training stability and convergence would strengthen the paper.

## Removed Points

- The harsh critic's claim about "mixed experimental evidence" and "no consistent or substantial advantage" (point 3) is removed. A direct count from Table 1 shows ZNet wins in 18/30 settings among IV generation methods, which is a consistent advantage. The critic overstated this weakness.
- The criticism about Section 3 Figure 2 "omitting the direct edge from C to T" is removed — the graph shown is a high-level transformation diagram, and the paper's SCM (Equation 1) does include C→T.
- The criticism about the paper "repeatedly asserting" solutions always give a valid instrument has been merged into Major weakness 1 above; it is a single assertion in the Discussion section, not repeated.
- The formatting/style nitpicks and missing appendix references are removed per filtering rules.
- The strength about "comprehensive and systematic evaluation" (Strength Finder point 2) is retained but noted as limited by reliance on a single base dataset.
- The strength about "interpretable architecture" (Strength Finder point 3) is removed as generic — the claim is stated but not evidenced with a concrete analysis.

## Novel Insights

The reviews surface an interesting tension that the paper itself does not fully confront: the method's empirical success at recovering known instruments (Figures 4, 5) and producing Z that passes IV validation checks (Figure 6) suggests that the covariance-based constraints may be *practically sufficient* even though they are *theoretically insufficient* for the full IV conditions. This raises a potentially valuable research question — under what conditions do covariance-based proxy constraints suffice for valid IV construction? — that is more precise and actionable than the paper's current framing. Additionally, the fact that ZNet works in "No Candidate" settings where no observed variable satisfies the IV criteria (Table 1 rows with TrueIV = "–") implies the learned representation might be exploiting a specific functional cancellation between observed covariates and unobserved confounders; the paper provides no analysis of when such cancellation is possible, which would be a natural next contribution.

## Suggestions

1. **Tone down the guarantee claim.** Replace "Solutions to the ZNet loss minimization problem will always give a representation that serves as an instrument" with a more measured statement such as "The loss encourages representations that approximately satisfy the IV criteria, and our experiments show these representations enable competitive ATE estimation." The current phrasing is not supported by the theoretical analysis.

2. **Add at least one additional base dataset** (e.g., News or an ACIC simulation) to demonstrate that the IHDP-based results are not coincidental.

3. **Report standard deviations or confidence intervals** alongside the mean ATE errors in Table 1, and describe the statistical test used for the significance stars.

4. **Add a discussion** of the non-significant test-set relevance in Figure 6a explaining how the ATE estimates remain valid despite this.

5. **Discuss the dimensionality** of C and Z and its impact on performance; add a sensitivity analysis.

## Score and Decision

### Calibration Anchors

| Anchor ID | Avg Score | Query Bucket | Comparison to Paper Under Review |
|-----------|-----------|--------------|-----------------------------------|
| qDhq1icpO8 (CBRL.CIV) | 6.75 | Topic-high | Stronger theory (proved soundness), uses real-world data, but also limited to representation learning for IV. Our paper has weaker theoretical guarantees. |
| F7XPZnIUHh (ADR) | 4.20 | Topic-mid | Similar issues: heuristic loss design, insufficient theoretical guarantees for the independence constraints, competitive but not dominant empirical results. |
| 0gqCIaBRQ9 (Regularized DeepIV) | 5.25 | Topic-mid | Solid theoretical analysis of IV regression but only simulated experiments. Our paper has broader experiments but weaker theory. |
| 5AJ8R4z5g0 (Potential Outcomes Under Hidden Confounders) | 3.25 | Topic-low | Strong but implausible assumptions, limited evaluation, missing theoretical justification for key claims. Our paper has better empirical evaluation but similar issues with central claim support. |
| 3cuJwmPxXj (Rep4Ex) | 8.00 | Topic-high | Exceptionally well-written, strong theoretical results, identifiability guarantees, convincing experiments. Our paper does not reach this level of rigor or clarity. |

**Comparison to low-band anchors:** The low-band topic anchor (3.25) was criticized for strong assumptions not defensible in practice, limited evaluation scope, and missing theoretical justification. The paper under review shares the "missing theoretical justification for key claims" problem — specifically, the guarantee that loss minimization yields a valid instrument is not theoretically supported. However, the paper under review has a broader evaluation (8 data-generation types vs. 1 synthetic + 1 real) and provides more compelling evidence of the method's practical utility (instrument recovery, competitive ATE). It does not have the "implausible assumptions" problem of the low-band anchor. So it sits above that anchor.

**Comparison to mid-band anchors:** The ADR paper (4.20) had a very similar profile: a method for learning decomposed representations with heuristic loss, insufficient theoretical guarantees for the independence constraints, and mixed but competitive empirical results. Our paper is comparable in quality — similar issues, similar scope of empirical work. The Regularized DeepIV paper (5.25) had stronger theoretical foundations but narrower experiments. Our paper has weaker theory but broader experiments. An intermediate score of 4.5 reflects that the paper has genuine empirical contributions but a significant overclaim in its central guarantee.

### Score and Decision

**MY FINAL SCORE:** <score>4.5</score>  
**MY FINAL DECISION:** <decision>Reject</decision>