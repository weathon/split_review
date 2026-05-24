Here is the final consolidated review.

---

## Summary

This paper proposes Predictive Differential Training (PDT), a method that applies Koopman/DMD-based predictions to selectively accelerate a subset of neural network parameters during training. The key innovation is a per-parameter masking strategy (quantity and direction criteria) that identifies which predicted weight updates are reliable, combined with an acceleration scheduler that rolls back to SGD when predictions are poor. Experiments on FCN, AlexNet, ResNet-50, and ViT-Base across CIFAR-10 and ImageNet show consistent wall-clock time reductions to reach the baseline best loss (10–39%).

## Strengths

- **Consistent wall-clock speedups across diverse architectures**: Table 1 reports concrete time-to-best-loss reductions: 39.7% (FCN), 37.1% (AlexNet), 19.4% (ResNet-50), and 10.2% (ViT-Base), with per-epoch overheads clearly documented. These measurements support the claim that PDT accelerates training without sacrificing final accuracy.

- **Ablation validates that masking is crucial**: Figures 6 and 7 show that (a) randomly selecting a subset of parameters and increasing their learning rates and (b) randomly selecting among predicted weights both lead to training instability or NaN values, while PDT's quantity-direction masking converges stably. This demonstrates that the selective application of predictions is necessary for robust performance on complex networks.

- **PDT improves over a prior Koopman-based scheduling baseline**: Section 4.3 (Figure 8) compares against a validation-loss-based switching strategy inspired by Tano et al. (2020). The baseline causes a catastrophic loss spike from which the model never recovers, while PDT's per-parameter masking maintains stable convergence. This provides direct evidence that PDT's approach improves upon existing Koopman training frameworks.

- **Hyperparameter sensitivity study**: Figure 9 systematically examines prediction steps, interval, starting epoch, and snapshot counts, identifying operating ranges where PDT succeeds (e.g., prediction steps 1–7) and degrades beyond (9+ steps). This empirical characterization aids deployment.

## Weaknesses

### Major

- **The contribution of the Koopman operator is not isolated from simpler selective-acceleration mechanisms.** The two masking criteria (Eqs. 8–9) effectively select parameters whose predicted update is larger than the one-step SGD update and directionally aligned. This is operationally similar to applying a per-parameter adaptive learning rate that accelerates parameters with consistent update directions. The paper compares PDT against random selection of accelerated subsets (Fig. 6) and random selection among predicted weights (Fig. 7), but **never against a simple non-predictive heuristic** — e.g., selecting parameters based on gradient magnitude, momentum buffer consistency, or the agreement of recent gradient directions — that applies a larger update without Koopman prediction. Without this comparison, it is unclear whether the DMD-based linear operator provides any benefit over cheaper alternatives for estimating which parameters benefit from acceleration. This gap weakens the paper's central claim that Koopman-based prediction is the source of improvement.

### Minor

- **No error bars, confidence intervals, or variance shading on any plot, despite claiming 5 random seeds.** The paper states "All experiments were repeated with five random seeds (0, 100, 200, 300, 400) to ensure reliability" but all figures (5, 6, 7, 8, 9) show single curves. Visual differences between methods cannot be assessed for statistical significance. This is a significant reporting weakness.

- **Figure 1's comparison is misleadingly framed.** The caption shows Adam at Epoch 10 (loss 2.08) vs. PDT at Epoch 29 (loss 1.16) and labels this "more efficient descent." Since the two methods run for different numbers of epochs and reach different loss values, this does not demonstrate faster convergence. Both methods should be compared at the same epoch count (e.g., both at Epoch 10), or the figure should be removed/reframed as a qualitative illustration.

- **The quantity criterion (Eq. 8) has an unexamined bias.** Equation 8 compares a *multi-step* predicted change ($\|w_{i+\tau}^{pred} - w_i^{pred}\|$) to a *single-step* SGD change ($\|w_{i+1}^{opt} - w_i^{opt}\|$). A τ-step trajectory will naturally tend to have larger magnitude than a single step for any consistently moving parameter, which could bias the criterion to accept many parameters regardless of prediction quality. This issue is not discussed in the paper.

- **"Prediction error" in the acceleration scheduler is never defined.** The paper lists "design a scheduler to keep track of the prediction error" as a contribution, but the actual scheduler simply checks whether any parameter satisfies Eqs. 8–9. The concept of prediction error is invoked but never operationalized. The description "If no element in the mask is qualified as 'good' prediction, then standard SGD-based optimization takes place" also conflates per-parameter masking with a global decision about whether to run prediction at all.

- **The toy example (Sec. 3.2) motivates differential learning rates, not prediction.** The example optimizes a 6-variable function by tripling the learning rate for a subset and shows 60% fewer steps. This cleanly illustrates the value of selective acceleration, but it does not involve Koopman prediction at all. The framing risks conflating the general idea of differential learning rates with the paper's specific claim that Koopman-based prediction is the mechanism. The connection should be made explicit or the example repositioned.

### Trivial

- **Cross-condition comparison in the hyperparameter study is limited.** Figure 9 varies one parameter per subplot while holding others fixed, but the fixed values differ across subplots (e.g., lr=0.01 in (a) vs. lr=0.05 in (b)). This makes it harder to compare results across conditions.

## Nice-to-Haves

- Compare against a non-Koopman adaptive selection heuristic (e.g., gradient-norm-based or momentum-based selection) to isolate whether the "prediction quality" signal adds value over simple statistics.
- Compare against other training acceleration techniques (e.g., layer-wise adaptive rate scaling, schedule-free optimization) to contextualize PDT's speedups relative to alternatives, not just vanilla optimizers.
- Report prediction quality metrics (e.g., cosine similarity between predicted and actual weight changes) for masked vs. non-masked parameters, ideally as a function of training time.

## Removed Points

These points were flagged by reviewers but are removed from the main assessment for the indicated reasons:

- **"Deterministic dynamical system assumption is unexamined."** This criticism misunderstands the standard application of DMD: DMD performs least-squares fitting on observed trajectory snapshots and is routinely applied to stochastic systems in the existing literature. The paper does not claim the system is deterministic; it treats observed weight snapshots as data. No special justification is required beyond what prior work (Dogra & Redman 2020, Tano et al. 2020) already establishes.
- **"Validation-loss scheduling experiment is a strawman."** The paper explicitly attributes this scheduling strategy to Tano et al. (2020). Whether or not the implementation exactly matches that prior work, the experiment tests a reasonable baseline derived from the literature. This is not a strawman.
- **"No comparison to SOTA training acceleration methods."** The paper compares PDT against the *same base optimizers* with identical hyperparameters (SGD, SGD+Momentum, AdamW), demonstrating that PDT-as-plug-in accelerates those optimizers. Comparing against external acceleration methods is scope-expansion beyond the paper's stated contribution.
- Missing appendix content, reference formatting, and typographical issues — these reflect PDF parsing artifacts or are explicitly outside the scope of evaluation.

## Novel Insights

None beyond the paper's own contributions. The reviewers' critiques converge on a specific methodological gap (Koopman vs. heuristic selection) rather than revealing any new scientific insight not already present in the paper.

## Suggestions

1. **Ablate the Koopman prediction explicitly.** Replace the DMD-predicted weights with a simple linear extrapolation from the same number of past snapshots and apply the same masking criteria. If PDT outperforms this, DMD adds genuine value.
2. **Add error bars to all figures.** With 5 seeds reported, every plot should show variance (shaded region or error bars).
3. **Fix Figure 1.** Show both Adam and PDT at the same epoch count, or reframe the figure as a qualitative loss-landscape illustration without the "faster convergence" claim.
4. **Acknowledge the bias in Eq. 8** and discuss whether it inflates the mask acceptance rate.
5. **Clarify the accelerator scheduler.** Define what "prediction error" means operationally, and describe how per-parameter mask quality is aggregated into a decision to run or skip prediction.
6. **Reframe the toy example** to explicitly state that it motivates *selective acceleration* in general, not Koopman prediction specifically, and clarify how PDT differs from a simple differential learning rate scheme.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| SQl6T4dfs8 (KUNDO) | 3.25 | R1 | Much weaker — Koopman theory paper that was withdrawn; substantially worse experiments than PDT |
| nu1H4MdxcB (Sparse ST reconstruction) | 2.33 | R1 | Much weaker — different domain, rejected |
| Kqm8jxOC4a (SReNet) | 2.50 | R1 | Much weaker — eigenvalue problem, withdrawn |
| OPSpdc25IZ (DS-LLM) | 6.00 | R1 | Somewhat stronger — accepted poster; more ambitious claims but evaluated on LLMs with hardware assumptions |
| twSnZwiOIm (Invariant representations) | 6.00 | R1 | Somewhat stronger — accepted poster; solid theory but different problem setting |
| c9xsaASm9L (CMD) | 6.50 | R1 | Stronger — accepted poster; more thorough analysis and stronger novelty |
| i1BTP8wFYM (Generalizing dynamics) | 5.25 | R1 | Similar — rejected; comparable level of methodological contribution but different domain |
| xGvPKAiOhq (Over-parameterization) | 8.00 | R1 | Much stronger — spotlight; rigorous theory |
| P1aobHnjjj (Implicit bias) | 7.75 | R1 | Much stronger — spotlight; rigorous theory |

**Round 2 — Narrowing:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| cUFIil6hEG (NiNo) | 5.75 | R2 | Somewhat stronger — accepted poster; weight-prediction acceleration with cleaner baselines and clearer isolation of contributions |
| fkrYDQaHOJ (Koopman for RL) | 5.50 | R2 | Similar quality — accepted poster with split reviews; Koopman in ML with similar rigor level |
| 60TXv9Xif5 (Metamizer) | 5.25 | R2 | Similar — accepted poster; different domain (physics sim) |
| NmaXXAiJJC (VQ compression) | 4.67 | R2 | Weaker — rejected; compression rather than training acceleration |
| LXlTdn9hY9 (HESSO) | 4.50 | R2 | Weaker — withdrawn; pruning-focused |
| 72yPbvSx0c (KEEC) | 4.50 | R2 | Weaker — withdrawn; Koopman control |

**Final score**: 5.0. The paper sits below NiNo (5.75) due to weaker evaluation rigor (no error bars, insufficient isolation of the Koopman contribution) but above the rejected/withdrawn papers in the 4–5 range. The core idea is interesting and the results are encouraging, but the central claim — that Koopman-based prediction specifically drives the improvement — is not adequately supported given the absence of a simple heuristic baseline. This places the paper marginally below the acceptance threshold.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>