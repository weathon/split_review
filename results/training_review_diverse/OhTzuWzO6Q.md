Now I have all the verification I need. Let me write the consolidated review.

## Summary

This paper proposes FedBNN, a federated learning framework for heterogeneous settings where clients have varying data resources, compute capacities, and model architectures. The key idea is to enable collaboration through functional-space priors: clients share outputs (logits) on a public alignment dataset (AD) rather than weight-space parameters, allowing clients with non-identical architectures to benefit from peer knowledge. The paper also describes a differentially private variant and provides a theoretical privacy analysis. Experiments on MNIST, CIFAR-10, and CIFAR-100 compare against FedAvg, FedProx, pFedME, pFedGP, pFedBayes, FOLA, and DP-FedAvg under multiple heterogeneity axes.

## Strengths

- **Novel functional-space prior mechanism for heterogeneous FL.** The core idea — using an unlabeled alignment dataset at the server to transfer knowledge via output-space priors rather than weight-space aggregation — is genuinely novel. It directly addresses the system heterogeneity challenge (non-identical architectures across clients) that most personalized FL methods cannot handle. (Section 3.2.1–3.2.2)

- **Non-DP experimental results show promise across multiple realistic heterogeneity axes.** The paper evaluates under compute heterogeneity, data-size heterogeneity, and statistical (non-IID) heterogeneity on three datasets. Reported results suggest that low-capacity clients gain ~10% accuracy through collaboration with higher-capacity clients — a benefit not achievable by homogeneous baselines. The method reportedly outperforms baselines by ~6% on average in small/medium data settings. (Section 5.2, Figure 1)

- **Seven baselines compared across three datasets.** The paper includes a solid set of comparators spanning non-Bayesian FL (FedAvg, FedProx, pFedME), Bayesian FL (pFedGP, pFedBayes, FOLA), and DP (DP-FedAvg), evaluating on MNIST, CIFAR-10, and CIFAR-100 under non-IID settings. (Section 5.1)

## Weaknesses

### Fatal
None. The core non-DP method and its evaluation constitute a legitimate contribution; the flaws described below are severe but do not invalidate the paper entirely.

### Major

- **Privacy analysis is technically unsound and the DP variant is never empirically tested.** This is the most serious weakness. Two specific problems: (1) The sensitivity bound Δ² ≤ 2 (line 126) is not justified. The paper claims this holds because clients output "normalized" logits, but the sensitivity of a neural network's output on a fixed public dataset with respect to a change in one training data point cannot be bounded by any constant without explicit mechanisms (gradient clipping, bounded Lipschitz constant, etc.) — none are described. (2) The composition formula in Theorem 4.2 (ρ = ε²/(4 E K log(1/δ))) does not follow from standard zCDP-to-DP conversion. Standard results give ε = EKρ + 2√(EKρ·log(1/δ)), which does not invert to the paper's formula. Furthermore, **the DP version of the proposed method is never evaluated.** The paper claims "under strict privacy constraints" in the abstract and states ε ≈ 9.98 with δ = 10⁻⁴ (line 128), but reports zero experiments with noise added to their own method. The only privacy baseline (DP-FedAvg) is included but with no matching comparison. The combination of an invalid formal analysis and absent empirical support means the entire privacy contribution is unsubstantiated.

- **Calibration is never measured despite being a core motivation.** The abstract, introduction, and discussion repeatedly emphasize "well-calibrated outputs," "calibrated predictions," and uncertainty quantification as key advantages of the Bayesian framework. However, the experiments report only classification accuracy. No calibration metric (expected calibration error, negative log-likelihood, coverage) is presented anywhere in Section 5. This is not a minor omission — it means a central claimed benefit of the method is asserted rather than demonstrated.

- **No ablation studies are performed.** The method has multiple design choices that directly affect performance: the mixing parameter γ (set to 0.7), the prior optimization procedure (100 steps), the AD size (2000), the number of Monte Carlo samples K (unspecified), and the core question of whether the functional-space prior provides improvement over simply training locally with Bayes-by-Backprop. Without ablations, it is impossible to attribute the reported performance to any specific component or to understand sensitivity to hyperparameters.

### Minor

- **Prior/posterior separation is methodologically unclear.** The paper states that prior parameters ψ are optimized by training the BNN to minimize the distance between Φ_i^corrected and Φ_i(AD; W_i) (Equation 4, line 85). But the BNN's output Φ_i(AD; W_i) depends on the variational parameters θ (via sampled weights W_i ∼ q(W_i|θ)), not on ψ directly. The paper says "the optimization involves training the client's personal BNN Φ_i to only learn the parameters of the prior distribution denoted by ψ" (line 88), but does not explain how updating the BNN's weights can affect ψ without also affecting θ. If the same network parameters are being trained in both phases, the "prior optimization" may constitute double-counting local data (once in the prior-tuning step, once in the variational inference step). This ambiguity undermines the theoretical grounding of the Bayesian framework.

- **The number of Monte Carlo samples K is never specified.** K is introduced in the method (line 59) as the number of weight samples drawn from the posterior to approximate Φ_i(AD), but its value is absent from the experimental details (Section 5.1). This makes the results partially unreproducible.

- **Adaptive aggregation weights (w_j) are set to 1/N and never varied.** The method motivates w_j as representing client "strength" in terms of data or compute resources, but all experiments use uniform weighting. The claimed benefit of resource-aware aggregation is never tested.

- **AD size is fixed at 2000 with no sensitivity analysis.** The choice of 2000 is plausible but not justified, and no experiment varies the AD size to understand how the method's performance depends on this auxiliary dataset. Since the AD is a key assumption of the framework, this gap limits practical guidance.

- **Asymmetric local training epochs unexplained.** Clients train for 50 epochs before collaboration but only 20 epochs per round afterward. This difference is not explained.

- **Missing baseline: FedDF.** FedDF (Lin et al., 2020) is discussed in Related Work as a knowledge-distillation approach for heterogeneous FL, which is conceptually similar to the proposed functional matching. Its omission from the experimental comparison weakens the evaluation.

### Trivial

- The claim of being "the first to jointly address" limited data, heterogeneous compute, privacy, and calibration (line 16) is overclaimed — Noble et al. (2022) already targets DP for heterogeneous FL, and pFedBayes already addresses limited data with uncertainty.
- The auxiliary dataset requirement is described as "a very mild requirement," which downplays a practical constraint that many FL deployments may not satisfy.
- No training curves or convergence analysis are provided for the 200-round runs.

## Nice-to-Haves

- A brief experiment varying AD size (e.g., 500, 2000, 5000) would significantly strengthen the evaluation and provide practical guidance.
- Reporting the computational overhead of the 100-step prior optimization and Monte Carlo sampling relative to standard FL training would help assess practicality.
- Including training/test accuracy curves would allow readers to assess convergence behavior.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Table 1 is unreadable / no numerical evidence the reader can inspect"** — Parser artifact. The table was an embedded image in the original submission; only the DP-FedAvg row survived text extraction. The original PDF contained a proper table. (Per hard rules: remove formatting/parser artifacts.)
- **Strength: "Formal differential privacy guarantee that is general and algorithm-agnostic"** — Conflicts with verified weaknesses (the analysis is incorrect, and no DP experiments exist). (Per rules: when a strength and weakness disagree, the weakness wins.)
- **Strength: "Privacy analysis provides actionable knobs for real deployment"** — Conflicts with verified weaknesses. Same reasoning as above.
- **Strength: "Mild assumption of a small public dataset for alignment"** — Generic/superficial; the paper's own self-characterization, not an independent strength. (Per rules: drop strengths that are generic or lack specific content.)
- **"Related work would benefit from distinguishing methods that require a public dataset from those that do not"** — This is a presentation suggestion, not a weakness of the paper's own contribution. (Scope creep.)
- **"Proof is missing / appendix references absent"** — The parser strips appendix sections from all papers; these exist in the original submission. (Per hard rules.)

## Novel Insights

The reviews surface a tension that the paper itself does not fully address: the functional-space prior mechanism is the paper's genuinely novel contribution, but the authors weighed it down by overclaiming on privacy and calibration — two dimensions where the evidence is either absent or technically flawed. The most interesting observation from the critic is that the Bayesian framing ("prior optimization") may not be doing what the paper claims: if the "prior" parameters ψ are optimized by training the BNN to match a target output, but the BNN's output depends on the variational parameters θ, then the distinction between prior-tuning and posterior-inference collapses. This suggests that the method might work well for reasons other than its stated Bayesian interpretation — perhaps as a form of output-regularized training. The paper would be stronger if it acknowledged this ambiguity and presented the mechanism in more neutral terms.

## Suggestions

1. **Fix or remove the privacy analysis.** The sensitivity argument and composition formula need a complete rework. If a correct DP analysis cannot be provided, remove the DP claim and present the method as a non-private approach to heterogeneous FL — the core contribution does not depend on privacy.
2. **Run the DP experiments or remove the privacy claims from the abstract/introduction.** Showing the proposed method's accuracy-privacy trade-off (or acknowledging it cannot be run) is non-negotiable if privacy remains a claimed contribution.
3. **Measure calibration.** Report at minimum expected calibration error (ECE) on test sets. This directly addresses the uncertainty quantification motivation.
4. **Provide ablations.** At minimum: performance without prior optimization (i.e., local-only Bayes-by-Backprop), sensitivity to γ, and sensitivity to AD size. This would clarify which components drive performance.
5. **Clarify the prior/posterior separation.** Provide explicit pseudocode showing which parameters (ψ vs. θ) are updated in each phase, and explain how training the BNN's output affects ψ without double-counting data.
6. **Specify K.** The number of Monte Carlo samples must be reported for reproducibility.

## Score and Decision

The paper's core idea — functional-space priors via an alignment dataset for heterogeneous FL — is novel and addresses a genuine gap in the literature. The non-DP experimental results suggest practical promise. However, the paper attempts to claim contributions in privacy and uncertainty quantification that are not supported (invalid theoretical analysis, absent DP experiments, no calibration metrics). Combined with methodological ambiguity in the Bayesian framing and missing experimental rigor (no ablations, unspecified K, no sensitivity analysis), the paper is not ready for acceptance in its current form.

**Originality:** 7/10 — The functional-space prior mechanism is genuinely new in the FL context.

**Importance of research question:** 8/10 — Heterogeneous FL with varying architectures is a practically important problem.

**Whether claims are well supported:** 3/10 — Core accuracy claims are plausible but unablated; privacy and calibration claims are unsupported.

**Soundness of experiments:** 4/10 — Reasonable breadth of baselines and datasets, but missing ablations, calibration metrics, DP experiments, and key details (K).

**Clarity of writing:** 5/10 — The method section is readable but the prior/posterior ambiguity creates confusion about what is actually being optimized.

**Value to the research community:** 6/10 — The core idea could inspire follow-up work if clarified and properly evaluated.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>