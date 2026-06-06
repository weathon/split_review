Now I have read the full paper. Let me analyze the reviewers' claims carefully against the text.

## Summary

ZNet is a multi-armed neural network that automatically decomposes observed covariates into a confounder component C and an instrument component Z, which are then passed into downstream IV estimators (TSLS, DeepIV, DFIV) for causal effect estimation. The key contribution is enabling IV-based causal inference without requiring prior domain knowledge of valid instruments. ZNet encodes IV conditions (relevance, exclusion restriction, unconfoundedness) as explicit loss constraints and is evaluated across eight semi-synthetic settings derived from the IHDP dataset.

---

## Strengths

- **Instrument recovery from data**: In the Linear Mixed Candidate dataset, ZNet generates a 10-dimensional instrument representation whose dimensions are strongly correlated with the three true instruments X₁₃, X₁₄, X₁₅ (Figure 5a,b). Ablation studies in Figure 5(c) confirm that each constraint individually contributes to recovery quality (R² drops from full-ZNet to each ablated variant), providing causal evidence that the loss design drives the recovery.

- **Competitive ATE estimation across diverse settings**: Table 1 shows ZNet consistently among the best-performing methods across eight semi-synthetic settings. Notable examples: on Linear No Candidate (with U) ZNet+TSLS attains signed error 0.025 vs. TARNet's 0.240; on Non-linear No Candidate (with U) ZNet+DFIV achieves 0.049 vs. next-best GIV's 0.345. These results are statistically significant across 50 bootstrapped test sets.

- **Architecture mirrors the SCM of IVs**: Unlike prior variational IV methods (AutoIV, VIV, DVAE.CIV, GDIV) which learn variational distributions without structural encoding, ZNet directly parameterizes the structural equations C = f(X) and Z = g(X) with loss terms enforcing IV conditions. This discriminative (non-generative) formulation is simpler and more transparent.

- **Comprehensive benchmarking**: The evaluation spans 10 data settings (8 in the main table) covering linear/non-linear, all instrument-availability classes (disjoint candidate, mixed candidate, latent categorical, no candidate), and both confounded and unconfounded X. The paper also evaluates CATE (Appendix Tables 3–4), and benchmarks four IV-generation methods against TrueIV and TARNet.

---

## Weaknesses

### Fatal

None.

### Major

- **Proof error in Lemma 1 invalidates the paper's primary theoretical advance.** The proof (Section 3) claims that $\text{Cov}(Z,\, e_Y - \mathbb{E}[e_Y|X,T]) = 0$ implies $\text{Cov}(Z,\, e_Y) = 0$. The critical step is: $\mathbb{E}[Z \cdot (e_Y - \mathbb{E}[e_Y|X,T])] = \mathbb{E}[Z \cdot e_Y] - \mathbb{E}[Z] \cdot \mathbb{E}[e_Y|X,T]$. This factorization implicitly treats $\mathbb{E}[e_Y|X,T]$ as a constant, but it is a random variable (a function of $X$ and $T$). Since $Z = g(X)$, we have $Z$ deterministically dependent on $X$, so $\mathbb{E}[Z \cdot \mathbb{E}[e_Y|X,T]] \neq \mathbb{E}[Z] \cdot \mathbb{E}[e_Y|X,T]$ in general. The correct expansion of step 3 gives $\mathbb{E}[Z \cdot e_Y] = \mathbb{E}[Z \cdot \mathbb{E}[e_Y|X,T]]$, which is $\text{Cov}(Z, e_Y)$ (since $\mathbb{E}[Z]=0$) equals $\mathbb{E}[Z \cdot \mathbb{E}[e_Y|X,T]]$, not zero. The paper explicitly frames Lemma 1 as what distinguishes ZNet from prior variational IV methods that require $X \perp U$ (Section 3: "To allow for our method to produce an instrument even more generally when $X$ may be influenced by $U$..."). Without a valid proof, this claimed theoretical advance over prior work is unsupported. Constraint 1 may still function as a useful empirical regularizer, but it must be reframed as a heuristic rather than a theoretically guaranteed condition. Importantly, this does not invalidate the empirical results, which stand on their own merits.

- **Hyperparameter tuning of downstream estimators uses a biased proxy.** Section 5.3 states the downstream causal inference methods (DeepIV, DFIV, TARNet) are hyperparameter-tuned by minimizing MSE against a nearest-neighbors (NN) ATE. However, NN-ATE is an observational estimator that does not adjust for unobserved confounding. In settings with $X^{\leftarrow U} \neq \emptyset$ — precisely the conditions that motivate the entire paper — NN-ATE converges to the confounded observational association rather than the true causal effect. Selecting hyperparameters to minimize distance to this proxy preferentially selects configurations that match the biased observational ATE, not the true ATE. Since the same tuning applies to all methods (ZNet, AutoIV, GIV, VIV), the relative comparisons in Table 1 are still valid as head-to-head comparisons, but the absolute ATE errors and the comparison against TARNet in confounded settings require careful interpretation.

### Minor

- **Weak instrument on the test split in the hardest setting.** Figure 6(a) reports for the Non-linear No Candidate dataset: Train F=15.34, Val F=4.96, Test F=1.83 (p=0.0813). The test-set F-statistic does not meet the conventional threshold for a strong instrument (F > 10), and p=0.08 is non-significant at the standard 0.05 level. This is the setting where the paper's contribution is most important. While the empirical ATE results in Table 1 for this setting appear favorable (ZNet+DFIV = 0.049), the weak test-set instrument raises the question of whether the favorable result depends on sensitivity to downstream estimator behavior under weak instruments. A brief sensitivity analysis or acknowledgment of this limitation would strengthen the paper.

- **Exclusion restriction enforcement is weaker than claimed.** Section 3 / Constraint 2 enforces exclusion restriction by requiring Cov(C,Y) > 0 and Cov(Z,C) = 0. However, orthogonality of Z to C does not ensure that Z has no direct effect on Y not mediated by C or T. This is acknowledged implicitly by the F-test in Figure 6(b) (which shows Z does not improve Y prediction after C and T in the test setting), but that test is specific to one dataset under a linear null hypothesis, not a general guarantee.

- **Ablation operates at the instrument-recovery level, not ATE level.** Figure 5(c) ablates each constraint and reports R² for predicting the true instrument from learned Z. However, the ablation is limited to the Linear Mixed Candidate dataset and does not report downstream ATE error under each ablation. Since downstream ATE quality is the paper's primary claim, an ablation demonstrating that each constraint is causally necessary for ATE accuracy (not just instrument recovery) would meaningfully strengthen the argument.

### Trivial

- **Overstated claim in discussion**: Section 7 states "Solutions to the ZNet loss minimization problem will always give a representation that serves as an instrument since IV constraints are explicitly embedded in the loss function." Minimizing a loss term toward zero does not guarantee exact constraint satisfaction, particularly under finite samples. The paper partially qualifies this elsewhere, but the sentence itself is stronger than the evidence.

---

## Nice-to-Haves

- Reporting Figure 4's K-Means clustering result across multiple random seeds would confirm the robustness of the perfect 5-cluster recovery beyond a single initialization.
- Using an IV-based cross-validation criterion (e.g., IV F-statistic on a held-out split) rather than NN-ATE for downstream estimator tuning would remove the confounding-direction bias in the tuning procedure for future work.
- An ablation measuring ATE error (not just instrument-recovery correlations) under removal of each ZNet constraint would make the case for each constraint's contribution to the primary outcome.
- A sensitivity analysis linking test-set F-statistic to ATE estimation error across bootstraps (particularly for the No Candidate settings) would clarify whether ZNet's good ATE performance in weak-instrument regimes is systematic or bootstrap-dependent.

---

## Removed Points

*These points are flagged as removed — treat them with caution.*

- **Reproducibility concern (no anonymized code)**: The paper states "code will be made public upon publication." Removed per the hard rule against nitpicking reproducibility concerns about large artifacts impractical to include in a submission.

- **TrueIV outperformed by ZNet in Linear Latent (TSLS)**: The critic flags that TrueIV(TSLS)=-0.524 while ZNet(TSLS)=-0.125 as suspicious. This is actually explainable: in the Latent Categorical Instrument setting, the true instrument is a discrete categorical grouping. Representing it as a 10-dimensional continuous Z in TSLS may offer strictly more predictive signal for the first stage than a raw categorical encoding, leading to a better-conditioned TSLS estimate. This is not evidence of misconfiguration — it is an expected benefit of learned continuous representations over discrete TrueIV inputs in a linear second stage.

- **ZNet outperforming TrueIV as a general concern**: Removed under the rule that one-off unexpected results visible in the paper's own table are not sufficient to flag a fundamental flaw without specific evidence of misconfiguration.

- **Signed mean error "allows cancellation"**: The use of signed mean error in Table 1 is standard for ATE estimation papers (it tracks directional bias, not magnitude). Using MAE would conflate positive and negative biases. This is not a weakness.

- **Perfect confusion matrix in Figure 4**: Questioning whether this represents cherry-picked cluster initialization was flagged as a concern but is a minor speculation without evidence in the paper. It remains a mild observation worth noting (moved to Nice-to-Haves).

---

## Novel Insights

The harsh critic's most valuable observation is that the step $\mathbb{E}[Z \cdot \mathbb{E}[e_Y|X,T]] = \mathbb{E}[Z] \cdot \mathbb{E}[e_Y|X,T]$ is only valid when $Z \perp (X,T)$, which fails by construction since $Z = g(X)$. This points to a broader challenge: when $X$ is influenced by $U$, any deterministic transformation $g(X)$ inherits that influence, and no finite-sample correlation penalty can guarantee the structural independence $Z \perp e_Y$ in population. This suggests the correct framing for ZNet in the No Candidate confounded setting is as a bias-reducing heuristic rather than a principled IV generator — a framing that is empirically plausible and practically useful, but requires honesty about what the theory does and does not guarantee.

---

## Suggestions

1. **Fix or reframe Lemma 1**: Either (a) provide a corrected proof (which may require additional structural assumptions on $\mathbb{E}[e_Y|X,T]$), or (b) restate Constraint 1 as an empirically motivated regularizer and explicitly acknowledge that ZNet in the confounded-X setting is a heuristic without formal unconfoundedness guarantees. The latter is a more honest framing and would not eliminate the paper's practical contribution.

2. **Address the NN-ATE tuning target**: For settings with $X^{\leftarrow U} \neq \emptyset$, consider using IV F-statistic-based criteria or training-set ATE ground truth (available in synthetic data) for downstream estimator hyperparameter selection, rather than a proxy known to be biased in the confounded regime.

3. **Report ATE-level ablations**: Supplement Figure 5(c) with ATE error as the ablation metric, and include at least one non-linear dataset to test generality of the constraint-necessity finding.

4. **Acknowledge weak instrument issue**: Add a remark in Section 6.2 or the limitations noting the test-set F-statistic for Non-linear No Candidate (F=1.83, p=0.08) falls below the standard weak-instrument threshold, and discuss what this implies for downstream IV estimation variance.

---

## Assessment on Core Axes

- **Originality**: Moderate-to-high. The discriminative SCM-encoding approach distinguishes ZNet from prior VAE-based IV learners. The architecture design is principled, though the theoretical underpinning has a flaw.
- **Importance**: High. Automating instrument construction is a practically significant problem for observational causal inference at scale.
- **Claims supported**: Mixed. Empirical claims in Table 1 are well-supported by comprehensive bootstrapped experiments. The theoretical claim (Lemma 1 as justification for Constraint 1 under confounded X) is not supported by a valid proof.
- **Soundness of experiments**: Largely sound, with the notable caveat of the NN-ATE tuning proxy.
- **Clarity of writing**: Good overall. The method exposition and experimental setup are clearly described.
- **Value to research community**: Real value as a plug-in IV module for settings without known instruments; the evaluation framework itself (8 semi-synthetic settings covering all instrument availability classes) is a useful contribution for future benchmarking.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>