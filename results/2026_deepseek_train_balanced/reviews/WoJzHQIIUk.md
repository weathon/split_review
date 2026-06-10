## Summary

This paper proposes a "MinMax Bayesian Neural Network" that formulates robustness as a two-player game between a deterministic network \(f\) and a stochastic perturbed network \(f + r \cdot \xi\), where \(r\) is a learnable radius parameter. The experiments study how this radius behaves under different architectural choices (bias, batch normalization, embedding dimension) and use it for out-of-distribution detection. The paper's two claimed contributions are: (1) verifying that sufficient embedding dimension is needed for uncorrelated representation learning from a robustness perspective, and (2) using the learned radius for OOD detection.

## Strengths

- **Systematic dimension-scaling study.** The paper trains CNNs at 11, 32, 64, and 128 embedding dimensions (Figure 3 a–d) and shows that the sampling radius distribution narrows and stabilizes at 128 dimensions for CNNs without bias or batch normalization, while remaining wide at 11 dimensions. This provides clear empirical evidence for the claim that sufficient embedding dimension is needed for isotropic perturbation behavior.

- **Empirical comparison of architectural effects on stability.** The paper documents that batch normalization disrupts isotropic perturbation behavior far more than bias terms (Figure 3 e–f; Figure 2). CNN with BN produces many large-radius samples, indicating sensitivity to specific perturbation directions, while adding only bias has a milder effect. This is a specific, documented architectural finding.

- **Noise corruption experiments with non-monotonic behavior.** Section 3.3 evaluates corruption ratios from 0 to 0.9 and finds the minimal radius occurs at moderate corruption (~0.4 for MNIST, ~0.3 for FMNIST) rather than zero corruption, with a Taylor-expansion argument offered as explanation. The additional comparison showing Cauchy (heavy-tail) noise always increases \(r\) while Gaussian noise does not provides a useful distinction between light-tail and heavy-tail perturbation behaviors.

## Weaknesses

### Fatal

- **The paper does not describe a Bayesian neural network in any recognizable sense, making the title and framing fundamentally misleading.** The stochasticity is at the **representation level** (\(g = f + r \cdot \xi\)), not at the weight level. The only Bayesian element is a variance network updated via Bayes by Backpropagation, but the paper explicitly states: *"Note that the way to update the variance NetV is by Bayes by Backpropagation Blundell et al. (2015) though **we do not care much about NetV here**"* (line 53). If the Bayesian component is not cared about, and the stochastic perturbation is on the representation rather than the weights, the method is not a Bayesian neural network. The title "MinMax Bayesian Neural Networks" sets an expectation the paper does not meet, and this mismatch is not fixable by additional experiments — it would require re-framing the entire contribution.

### Major

- **The core method is not coherently defined, so the reader cannot determine what was actually trained.** (a) The constraint in Equation (1) uses \(|\text{pre}(f(X,\mu)) - \text{pre}(h(X,\mu,\rho,r))| \geq c\), where the function \(\text{pre}(\cdot)\) appears from nowhere and is **never defined** anywhere in the paper. (b) Equation (2) is \(\min_{\rho,r} \max_\mu [\dots]\) where the inner maximization is over \(\mu\) — the **weights of the deterministic encoder**. Maximizing over the encoder's own weights would push it to produce poor representations; the paper provides no rationale, no algorithmic description, and no explanation of why this is beneficial. (c) The notation is inconsistent: Equation (1) uses both \(g\) and \(h\) for the sampling network without clarifying their relationship. The text says \(g = f + r \cdot \xi\) but also says "Combine \(\mu,\rho\) and \(r\), we can get the sampling neural network \(h(X,\mu,\rho)\)." It is unclear whether \(g\) and \(h\) refer to the same function or different ones.

- **Robustness — the paper's central claimed property — is never directly measured.** The introduction motivates the work through robustness to adversarial attack and uncertainty quantification, and the contribution claims a "robustness perspective." Yet: no adversarial attack (FGSM, PGD) is performed; no calibration metric (ECE, reliability diagram) is reported; no comparison to standard BNN methods (Bayes by Backprop, MC Dropout, SWAG) is provided. The radius \(r\) is a **property of the method**, not an evaluation of robustness. The paper asserts that a stable \(r\) implies robustness without argument or evidence. For a paper whose thesis is about robustness, this is a fundamental gap.

- **The OOD detection experiment lacks standard metrics, baselines, and sufficient detail to support its claims.** The OOD experiment uses a fixed radius threshold of 0.7, determined from an image-only table. Performance is described only qualitatively: *"the performance of OOD will not be so good if introducing the BN or bias term"* and *"this will not have accept the wrong data if having suitable radius level"* (line 82). No AUROC, no FPR@95TPR, no comparison to any OOD detection baseline (Mahalanobis distance, ODIN, energy-based OOD, etc.) is reported. The key claim — that the method can detect OOD data — is supported entirely by qualitative assertion.

### Minor

- **The "Brownian Motion" analogy is invoked repeatedly (abstract, lines 41, 64, 170) but never formally developed or used.** The paper says the stochastic network "can be seen as a Brownian Motion of \(f\)" but provides no technical connection — no stochastic process formalism, no connection to the Wiener process, no practical insight derived from the analogy. It remains a rhetorical flourish.

- **The novelty claim is overstated.** The paper says *"this is the first time to applied the minimax method in BNN"* (line 16), but earlier cites fault-tolerant neural networks (Neti et al., 1992; Deodhare et al., 1998; Duddu et al., 2019) that already used minimax games with dropout/perturbation. The differences claimed (perturbation vs. fault nodes, representation-level concern) are incremental, not first-of-its-kind.

- **The paper does not report which training case (case 1 or case 2) was used for which experiment.** The paper describes two training variants: updating \(r\) in both max and min processes (case 1) vs. only in the min process (case 2), but never specifies which was used for the reported results.

- **The network architecture is referenced only as "the same network structure as Dai et al. (2023)"** (line 51) without description. The \(k\) in kNN is not reported. Golden search bounds for \(r\) are unspecified. No experiment reports variance across random seeds or noise samples — essential for a stochastic method.

### Trivial

- Template text for author contributions and acknowledgments sections was left in the submission verbatim (lines 174–180: *"If you'd like to, you may include a section for author contributions as is done in many journals…"*). This is unprofessional for a conference submission.

- The phrase *"This loss is one kind of principle component analysis and should be isotropic to the Brownian Motion"* (line 41) is not a coherent technical claim.

## Nice-to-Haves

- Clarify the optimization: provide a self-contained description of the training objective and algorithm for both supervised and representation learning variants. Explain why \(\max_\mu\) over encoder weights makes sense, or replace it with a standard adversarial perturbation.
- Report accuracy results with standard deviations in the prose (not only in tables). Compare to deterministic baselines with the same architecture in addition to LDR.
- Benchmark OOD detection with standard metrics (AUROC, FPR@95TPR) against at least one standard OOD baseline.
- Ablate the minimax formulation: what happens if the constraint in Eq 1 is removed or the max in Eq 2 is replaced with a standard representation learning loss?

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that tables are embedded images and unverifiable** — Removed as a parser artifact. In the original PDF submission, the table images would be readable. The substantive remaining concern (lack of statistical rigor, no standard deviations) is retained under Major/Minor.
- **Criticism that "loss(f(X,μ)) minimizes over μ which is standard training"** — This particular framing is not a weakness (minimizing over weights is normal). The genuine issue (max over μ in Eq 2) is retained.
- **Generic areas-of-concern framing** — Some phrasing by the harsh critic ("could the metric be measuring a proxy?", "are confounders controlled?") was removed as speculative concern-sweeping without concrete anchor in the paper.
- **Complaint that no comparison to LDR is given** — The paper does compare to LDR (line 60), so this specific sub-point was removed as factually incorrect.
- **Strength Finder: generic strengths about "addressing an important problem"** — Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The dimension-scaling and BN-vs-bias stability findings are genuine empirical observations, but the severe issues with method definition, evaluation validity, and framing prevent any novel synthesis beyond what the paper itself reports.

## Suggestions

1. **Re-frame the paper honestly.** Drop the "Bayesian Neural Network" label from the title if the stochasticity is at the representation level and the Bayesian component is not actually used. "Minimax Feature Perturbation" or "Stability via Adversarial Noise Injection" would be more accurate.
2. **Define every symbol and function used in the equations.** The function \(\text{pre}(\cdot)\) must be defined. Clarify whether \(g\) and \(h\) are the same or different.
3. **Measure robustness directly.** Run at least one standard adversarial attack (e.g., PGD) and report accuracy under attack. Report calibration error. Compare to at least one standard BNN baseline.
4. **Evaluate OOD detection with standard metrics** (AUROC, FPR@95TPR) against a standard baseline (e.g., Mahalanobis distance or energy score).
5. **Report all experimental details**: which training case was used, the \(k\) in kNN, validation splits, number of random seeds, and standard deviations.

## Score and Decision

This paper has a fatal framing issue (it is not a Bayesian neural network as described, making the title and core framing misleading) combined with major methodological and evaluation gaps (method not coherently defined, robustness never measured, OOD evaluation lacks rigor, no proper baselines). The empirical observations about dimension-scaling and architectural effects are interesting but do not salvage the fundamental problems. The paper is not ready for publication at a top-tier venue.

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>