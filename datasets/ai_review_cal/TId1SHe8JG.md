- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6
Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper introduces higher-order calibration, a generalization of ordinary calibration to higher-order predictors that predict mixtures over label distributions. The key theoretical contribution is showing that under higher-order calibration, the mutual information decomposition of uncertainty (aleatoric/epistemic) has rigorous real-world semantics: the predicted aleatoric uncertainty equals the average true aleatoric uncertainty over points in the same level set, with no distributional assumptions. The paper proposes k-th-order calibration as a tractable relaxation, proves convergence rates, gives sample complexity bounds for post-hoc calibration, and demonstrates the approach on CIFAR-10H using human annotation snapshots.

## Strengths

- **First distribution-free guarantee for uncertainty decomposition (Theorem 1.2, Lemma 3.2):** The paper proves that under higher-order calibration, the estimated aleatoric uncertainty equals the *average true aleatoric uncertainty* over the predictor's level set, and the epistemic uncertainty equals the average divergence of the Bayes distributions to their mean. This holds without any assumptions on the data distribution — a genuine advance over Bayesian methods whose semantics rely on well-specified models and asymptotic consistency (Section 1.1). The necessity direction (Theorem E.1) further strengthens this result.

- **Principled hierarchy and convergence rates (Lemma 2.5, Theorem 2.6):** The paper establishes that k-th-order calibration converges to higher-order calibration at rate |𝒴|/(2√k) in Wasserstein distance, and proves that ε-k-th-order calibration implies (ε+|𝒴|/(2√k))-higher-order calibration. This generalizes the k=2 case of Johnson et al. (2024) with rigorous error bounds and clarifies the conceptual hierarchy from first-order to full higher-order calibration.

- **Post-hoc calibration with finite-sample guarantee (Theorem 2.8):** The paper provides a concrete post-hoc procedure for achieving k-th-order calibration with sample complexity N ≥ (2(|𝒴⁽ᵏ⁾|log 2 + log(1/δ)))/ε², purely by learning the k-th-order projection of the Bayes mixture within each partition cell. For binary prediction this simplifies to k+1, and the approach parallels standard first-order calibration procedures like Platt scaling.

- **Small k suffices for common entropy functions (Theorem 3.3):** The paper shows that Brier entropy (k=2) and Shannon entropy (polylogarithmic k in 1/ε) can be accurately estimated with modest k, establishing practical feasibility.

## Weaknesses

### Fatal

None.

### Major

- **No baselines in experiments.** The paper claims to "demonstrate through experiments that our method produces meaningful uncertainty decompositions in tasks such as image classification," yet presents zero comparisons to any existing uncertainty decomposition method — no Bayesian neural networks, deep ensembles, Monte Carlo dropout, or even the k=2 method of Johnson et al. (2024) that the paper directly builds on. Without baselines, the reader cannot assess whether the proposed method yields better, worse, or comparable aleatoric/epistemic estimates relative to the substantial body of prior work the paper cites (Section 1.1). This is the most significant weakness of the experimental section.

- **Partition mismatch between theory and experiments.** The theory defines higher-order calibration with respect to the predictor's *own level sets*. The experiments (Section 4) use a coarser partition defined by the maximum class and confidence slice of the *marginal* first-order predictor, producing 100 bins. The paper acknowledges this ("it is infeasible to compute the true level set partition of g") but does not analyze or bound the approximation error this introduces. Since the theoretical guarantees (Theorem 1.2, Lemma 3.2) depend on the partition being the higher-order predictor's level sets, the direct applicability of the theory to the experimental results is unclear.

- **Limited statistical rigor.** The experiments run on a single dataset (CIFAR-10H) with a single architecture (ResNet). No error bars, confidence intervals, or reproducibility checks are reported. With 5000 calibration points spread across 100 bins, many bins likely contain few snapshots, yet the paper does not report bin sizes, analyze per-bin variance, or discuss the reliability of the empirical mixture estimates in low-data bins.

### Minor

- **Evaluation metric is a proxy.** The paper measures aleatoric estimation error (Eq. 4.1) rather than directly measuring higher-order or k-th-order calibration error (e.g., Wasserstein distance between the predicted mixture and the empirical Bayes mixture within each bin). The theoretical guarantees flow from calibration; showing that the predictor is actually calibrated would more directly validate the framework.

- **The k-snapshot assumption is a genuine limitation.** The paper acknowledges this honestly in the conclusion and discusses settings where it holds (crowdsourcing, model distillation). However, for many practically important domains (medical diagnosis where outcomes occur once per patient, credit scoring, etc.) the assumption fails, and the paper provides no analysis of robustness to violations (e.g., correlated annotators, biased labels). Since the entire method hinges on this assumption, the absence of any sensitivity analysis is a gap.

### Trivial

None.

## Nice-to-Haves

- An analysis of bin sizes in the experimental partition and how the sample complexity bound (Theorem 2.8) relates to the actual calibration set size per bin.
- A sensitivity study showing how the method degrades under violations of the independent-snapshot assumption (e.g., correlated annotators).

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The informal statement of Theorem 3.3 is too vague"* — The paper explicitly labels it "informal" and states the formal version is in the appendix. With the parser stripping the appendix, this is not a verifiable weakness.
- *"No evaluation on downstream tasks (active learning, OOD detection)"* — Scope creep. The paper's contribution is uncertainty decomposition with rigorous semantics, not a full application suite.
- *"The theoretical rate for Shannon entropy (exp(Θ(k))) is worrisome"* — The paper reports this rate honestly; it is a property of the problem, not a flaw in the analysis. The same theorem also shows Brier entropy works at k=2.
- *"Sample complexity bound not followed in practice"* — The experiments use the available snapshots with a standard plug-in estimator, which is consistent with the post-hoc algorithm described. The bound is a worst-case guarantee; not exceeding it in a specific run is not a weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Add baselines.** At minimum, compare the proposed method's aleatoric/epistemic decomposition to the mutual information decomposition from a deep ensemble (Lakshminarayanan et al., 2017) and from MC Dropout on the same CIFAR-10H data. Show that the proposed k-th-order calibration approach yields decomposition quality comparable to or better than these existing methods.
- **Measure calibration error directly.** Compute the Wasserstein distance between the predicted mixture and the empirical Bayes mixture within each bin, and show that it decreases as k increases. This would directly validate the core theoretical notion.
- **Quantify the partition mismatch.** Either (a) design a method that actually computes level sets based on the predicted mixtures, or (b) provide a bound on the additional error introduced by using a coarser partition based on the marginal predictor.
- **Add statistical rigor.** Report standard deviations or confidence intervals (e.g., via bootstrap over the test set), and ideally add a second dataset with multiple annotations (e.g., CIFAR-10H alone is limited).
- **Acknowledge experimental scope honestly.** The current framing ("demonstrates through experiments that our method produces meaningful uncertainty decompositions") overstates what is shown. A more measured claim — e.g., "we provide a proof-of-concept on CIFAR-10H showing that aleatoric estimation error decreases with k" — would better match the evidence.
