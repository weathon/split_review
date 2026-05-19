- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6
Now I have a thorough understanding of the paper and can verify the claims. Let me produce the final consolidated review.

## Summary

This paper addresses limitations in Randomized Smoothed Conformal Prediction (RSCP). It identifies that RSCP's robustness guarantee is flawed in practice because it relies on an intractable expectation but does not bound Monte Carlo estimation error. The paper proposes **AlgName**, which uses the Monte Carlo estimator directly as the conformity score and derives a concentration-based continuity bound, providing a _provable_ robustness guarantee. However, AlgName alone produces trivial (full label set) predictions. To improve efficiency, the paper introduces **PTT** (a training-free post-hoc score transformation) and **RCT** (a differentiable robust conformal training pipeline), achieving up to 16.9× reduction in prediction set size on ImageNet.

## Strengths

- **Identifies and fixes a genuine flaw in RSCP.** Section 3 correctly pinpoints that RSCP's guarantee is invalid in practice because it uses a Monte Carlo estimate of the expectation without a finite-sample error bound. AlgName resolves this by using the Monte Carlo estimator $\hat{S}_{\text{RS}}$ directly as the base score and deriving a continuity bound using concentration inequalities, yielding a _provable_ robustness guarantee. This is a principled and clean fix.

- **Substantial and well-documented efficiency gains.** Tables (referenced as `tab:RSCPplusSplitCifar` and `tab:RSCPplusSplitInet`) show that the baseline (AlgName without PTT/RCT) produces trivial full-label-set predictions across all three datasets, while PTT and RCT yield meaningful, small prediction sets. The reported improvements — up to 4.36× on CIFAR-10, 5.46× on CIFAR-100, and 16.9× on ImageNet — directly support the paper's central claim of improved efficiency under a provable guarantee.

- **Principled theoretical motivation for PTT.** Equation (11) provides a clean linear approximation linking threshold inflation $M_\epsilon$ to the coverage gap via the slope of the smoothed score CDF. This motivates reducing the slope near the threshold, which the paper then operationalizes through ranking + sigmoid transformations on the base score. The paper is transparent about the heuristic nature of the approximation and acknowledges a failure mode in the appendix.

- **Novel end-to-end differentiable training pipeline (RCT).** Section 4.2 extends conformal training (Stutz et al.) to the robust setting by incorporating randomized smoothing and threshold adjustment into the training loop, making the entire pipeline differentiable via Monte Carlo gradient approximation. This is a non-trivial adaptation that moves beyond training for standard conformal prediction.

## Weaknesses

### Fatal

None.

### Major

- **No empirical coverage verification on adversarially perturbed test data.** The experiments report only prediction set size, relying entirely on the theoretical guarantee for coverage. Given the multiple approximations involved (Monte Carlo concentration bound, union bounds over classes, confidence parameter $\beta$), the reader cannot empirically assess whether coverage actually stays at or above $1-\alpha$ when PTT/RCT are applied. The paper states (line 268) that coverage "is guaranteed by our theoretical results," but an empirical check — e.g., coverage on a held-out test set under adversarial noise at the specified $\epsilon$ — would substantially strengthen confidence that the efficiency gains do not come at the cost of violating the nominal coverage. This is the single most important gap in the experimental validation.

### Minor

- **Only one perturbation magnitude $\epsilon$ per dataset.** The paper uses $\epsilon=0.125$ for CIFAR-10/100 and $\epsilon=0.25$ for ImageNet. Results at multiple $\epsilon$ values (e.g., 0.1, 0.25, 0.5 on CIFAR-10) would better demonstrate how prediction set size and the effectiveness of PTT/RCT vary with perturbation severity.

- **No comparison to vanilla (non-robust) conformal prediction.** The baseline is AlgName without PTT/RCT (which produces full label sets). Adding vanilla CP prediction set sizes would help contextualize the cost of robustness and calibrate the reported improvement factors (e.g., "16.9× over what baseline, and how far from non-robust efficiency?").

- **No ablation study for PTT components.** The paper combines ranking transformation and sigmoid transformation without isolating their individual contributions. Ablations (ranking-only, sigmoid-only, full PTT) and sensitivity analysis for hyperparameters $b$ and $T$ would clarify which component drives the efficiency gains.

### Trivial

None.

## Nice-to-Haves

- **Multi-$\epsilon$ experiments** across a wider range would strengthen the empirical profile.
- **Ablation of PTT components** (ranking-only vs. sigmoid-only vs. full PTT) would clarify design choices.
- **Vanilla CP comparison** to quantify the cost of robustness.
- **Reporting training overhead** for RCT relative to standard conformal training.

## Removed Points

These points raised by reviewers are excluded from the main weaknesses with brief justification:

1. **"PTT motivation uses base score CDF instead of smoothed score CDF."** — Factually incorrect. The paper's linear approximation (Eq. 11, line 176) explicitly uses $\Phi_{\smoothscorebs}^{\prime}(\tau)$, the CDF of the **smoothed** score. The paper then transparently states it approximates by working on the base score (line 187–188) and provides justification in the appendix. The critic misread the derivation.

2. **"Main theorem is not stated in the main text."** — The theorem is included via `\input{Tab/theorem_proof_Hoef}` in the original submission. The PDF parser strips appendix content from all papers; the theorem exists in the original. Per policy, criticisms about missing appendix/proof content are removed.

3. **"The guarantee form (1−α vs. 1−α−β) is unclear."** — The paper states $\beta=0.001$ (line 274) and the guarantee is stated in the theorem in the appendix. This detail is present in the original submission.

4. **"Theoretical analysis of PTT is not rigorous for the smoothed score."** — The paper is transparent about the heuristic nature, acknowledges a failure mode in the appendix (line 215), and provides synthetic/empirical validation in the appendix. The paper does not overclaim rigor.

5. **Generic reproducibility complaints about hyperparameters.** — The paper reports key hyperparameters ($N_{\text{MC}}=256$, $\beta=0.001$, $b=0.9$, $T=1/400$, $|D_{\text{holdout}}|=500$) and references the appendix for further details.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already articulate.

## Suggestions

1. **Add an empirical coverage table:** For each dataset, method (Baseline, PTT, RCT), and perturbation magnitude, report empirical coverage on adversarially perturbed test inputs alongside prediction set size. Show that coverage stays at or above $1-\alpha$ (or $1-\alpha-\beta$) across all configurations. This is the highest-priority revision.

2. **Add a PTT ablation** separating ranking-only and sigmoid-only contributions to prediction set size.

3. **Include a vanilla CP baseline** to contextualize the efficiency numbers.

4. **Report results at multiple $\epsilon$ values** (e.g., 0.1, 0.25, 0.5 on CIFAR-10) to show sensitivity.
