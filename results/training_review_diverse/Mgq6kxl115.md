Now I have a thorough understanding of the paper and the review inputs. Let me write my final consolidated review.

---

## Summary

This paper proposes Diffusion Bridge Network (DBN), a method to reduce the inference cost of deep ensembles by learning a conditional diffusion process that transports the logit distribution of a single ensemble member to the logit distribution of the full ensemble. The method uses a lightweight score network (inspired by MobileNetV2), temperature annealing of the source logit to create a stochastic source distribution, and progressive distillation to reduce sampling to a single step. Evaluated on CIFAR-10, CIFAR-100, and TinyImageNet, DBN achieves accuracy and uncertainty metrics close to a 3-member deep ensemble with ~1.17× the FLOPs of a single model.

## Strengths

- **Novel formulation of ensemble distillation as a conditional diffusion bridge.** The paper reframes ensemble distillation from a one-step prediction problem (as in Bridge Network) into a stochastic transport problem in logit space. This is a principled departure from prior approaches, which either predict ensemble outputs directly (losing diversity) or require quadratic numbers of pairwise bridges.

- **Temperature-annealing trick to avoid trivial solutions.** The paper identifies that a deterministic source logit would allow the bridge to collapse to a copying solution. By randomly annealing the source logit via temperature sampling (Section 3.2, Eq. 5), the source becomes stochastic, forcing the diffusion process to learn a nontrivial path. This design choice is specific, well-motivated, and empirically justified.

- **Empirical superiority over Bridge Network and distillation baselines.** On CIFAR-10, CIFAR-100, and TinyImageNet, DBN achieves accuracy and DEE close to a 3-member deep ensemble with lower FLOPs than Bridge Network, while Bridge Network saturates at DE-2 performance (Table 1, Section 4.1). On TinyImageNet, DBN even outperforms DE-3 at less than half the computation.

- **Lightweight score network and single-step inference.** The score network uses depthwise separable convolutions (MobileNetV2-style), keeping parameter count and FLOPs low (1.166× relative FLOPs vs. 1.411× for Bridge Network). Progressive distillation reduces the multi-step diffusion to a single step, making inference practically cheap.

- **Scalable multi-DBN construction.** Multiple DBNs can share a single source model, so adding more bridges to handle larger ensembles incurs only the cost of the lightweight score networks (Section 3.4). The capacity study (Figure 2) shows a single DBN can effectively distill up to 3 ensemble members.

## Weaknesses

### Fatal
None.

### Major

- **The training loss does not clearly follow from the claimed I2SB (Schrödinger bridge) framework.** The paper derives the I2SB conditional distribution in Eq. 94 as \(q(\mathbf{Z}_t \mid \mathbf{Z}_0,\mathbf{Z}_1) = \mathcal{N}(\mu_t, \Sigma_t)\) with \(\mu_t\) depending on **both** \(\mathbf{Z}_0\) and \(\mathbf{Z}_1\). However, the training loss (Eq. 15) uses \(\|\varepsilon_\phi(\mathbf{h}_1, \mathbf{Z}_t, t) - (\mathbf{Z}_t - \mathbf{Z}_0)/\sigma_t\|^2\) as the target, which depends only on \(\mathbf{Z}_0\) and not on \(\mathbf{Z}_1\). The score of the I2SB conditional distribution is \(-\!(\mathbf{Z}_t - \mu_t)/\Sigma_t\), which involves \(\mathbf{Z}_1\) through \(\mu_t\); this is **not** proportional to \((\mathbf{Z}_t - \mathbf{Z}_0)/\sigma_t\) in general. The loss target \((\mathbf{Z}_t - \mathbf{Z}_0)/\sigma_t\) would be appropriate for a simple Brownian motion forward process \(\mathbf{Z}_t \mid \mathbf{Z}_0 \sim \mathcal{N}(\mathbf{Z}_0, \sigma_t^2 \mathbf{I})\), but the paper states that \(\mathbf{Z}_t\) is sampled from the bridge distribution \(q(\mathbf{Z}_t \mid \mathbf{Z}_0,\mathbf{Z}_1)\) (Eq. 94). This inconsistency between the claimed forward process and the actual training objective is not explained. The reverse SDE in Eq. 10 is correctly derived for a Brownian motion forward process, but the paper's theoretical framing as a Schrödinger bridge (which requires coupling both endpoints) is not supported by the loss as written. **Why this matters:** This undermines the paper's central theoretical justification. The method may still work empirically, but the claim of building a diffusion Schrödinger bridge between the source and target logit distributions is not substantiated by the presented derivation. The authors should clarify the reparameterization (if one exists) or acknowledge the discrepancy.

- **No error bars or statistical significance reported for any experiment.** All tables and figures present point estimates without standard deviations, confidence intervals, or multiple-seed runs. Given that the pipeline involves training ensemble members, a score network, and distillation — all with stochastic elements (random seeds, temperature sampling, diffusion noise) — the reported improvements over baselines cannot be assessed for statistical reliability. **Why this matters:** Without error bars, the reader cannot determine whether the improvements are meaningful or within the noise of a single run. This is a basic expectation for empirical comparisons.

### Minor

- **Poor Expected Calibration Error (ECE) is acknowledged but not analyzed.** The paper notes (Section 4.1) that "interestingly DBN also shows poor ECE scores even with high performance in the other uncertainty metrics." Since a key motivation for deep ensembles is improved calibration, this is a significant limitation. The paper offers no analysis of why the diffusion bridge produces miscalibrated outputs, whether post-hoc temperature scaling could fix it, or whether this is inherent to the method. This deserves at least a discussion or an attempted remedy.

- **No validation of distillation quality.** The paper trains the diffusion bridge with 5 steps but reports only the distilled single-step results. There is no ablation comparing the 5-step (pre-distillation) performance against the 1-step (post-distillation) performance on any metric. **Why this matters:** Without this comparison, the reader cannot assess how much performance the distillation step sacrifices relative to the full multi-step process. The claim that distillation "retains" performance is not quantitatively supported.

- **Temperature distribution \(p_{\text{temp}}\) is underspecified.** The paper defines \(\mathbf{Z}_1 = \mathbf{z}_1/T\) with \(T \sim p_{\text{temp}}\) (Section 3.2) and states this distribution is crucial for avoiding trivial solutions, but does not specify its form (uniform, log-uniform, Gaussian? what hyperparameters?) in the main text. Details are relegated to the appendix, which is stripped from the review version. **Why this matters:** The sensitivity of results to this distributional choice is unknown, and reproducibility requires this information front and center.

- **No comparison of DBN's training cost.** The paper focuses heavily on inference FLOPs but does not report training GPU-hours or comparable cost for the diffusion bridge training relative to Bridge Network or ensemble distillation. The conclusion acknowledges that "multiple diffusion bridges leads to a proportional training time," but a quantitative comparison is missing. **Why this matters:** A practitioner choosing between DBN and BN needs to know the training cost tradeoff, not just inference.

### Trivial
None.

## Nice-to-Haves

- A table or plot showing how performance scales with the number of DBN bridges \(L = 1, 2, 3\) on the same dataset (accuracy, FLOPs, ECE) would strengthen practical guidance.
- An ablation on the temperature distribution (e.g., fixed temperature vs. uniform vs. log-uniform) would validate the claim that temperature randomization is essential.
- Explaining why ECE degrades relative to the ensemble — is it the temperature sampling, the single-step distillation, or the score network capacity? A diagnostic experiment would be informative.

## Removed Points

- **Criticism that the loss never involves \(\mathbf{Z}_1\):** While the loss target \((\mathbf{Z}_t - \mathbf{Z}_0)/\sigma_t\) does not explicitly involve \(\mathbf{Z}_1\), the score network \(\varepsilon_\phi\) does take \(\mathbf{h}_1\) as input, which encodes logit-level information about the source model (and thus \(\mathbf{Z}_1\) indirectly). The concern is retained (in Major) but the framing is adjusted: the issue is the *mathematical inconsistency* between the claimed forward process and the loss target, not that \(\mathbf{Z}_1\) is "never used."
- **"Bridge Network's training cost is not trivially lower":** This is a valid observation but belongs in Nice-to-Haves rather than a weakness — the paper's focus is inference cost.
- **Figure/table references that are missing in the parsed version:** These are parser artifacts, not author errors.
- **"The paper should also discuss low-loss subspace cost in more depth":** Scope-creep; the paper explicitly argues its approach avoids this cost.
- **Missing algorithm reference:** The parsing stripped `\input{algorithm/dbn}`; this is a parser artifact.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a truly novel perspective on the work that was not already present in the paper itself.

## Suggestions

1. **Clarify the loss derivation.** Provide a step-by-step derivation showing how \(\|\varepsilon_\phi - (\mathbf{Z}_t - \mathbf{Z}_0)/\sigma_t\|^2\) follows from the I2SB framework given the conditional distribution \(q(\mathbf{Z}_t \mid \mathbf{Z}_0, \mathbf{Z}_1)\) in Eq. 94. If a different reparameterization or approximation is used, state it explicitly. If the forward process is actually a simple Brownian motion (not the I2SB bridge), revise the Background section to match and temper the Schrödinger bridge claims accordingly.

2. **Add error bars.** Report means and standard deviations over at least 3 independent runs of the full pipeline for all main metrics (ACC, NLL, BS, ECE, DEE) on at least one dataset.

3. **Analyze the ECE gap.** Apply temperature scaling to DBN outputs and report the resulting ECE. If this does not fix the issue, provide a plausible explanation or acknowledge it as a limitation.

4. **Report pre-distillation vs. post-distillation metrics.** Show a table comparing 5-step DBN (before distillation) vs. 1-step DBN (after distillation) on all metrics to validate that distillation does not significantly degrade performance.

5. **Specify \(p_{\text{temp}}\) in the main paper.** At minimum, state whether it is uniform, log-uniform, or Gaussian, and provide its support or parameters.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>