I now have all the evidence I need from the paper. Let me produce the final consolidated review.

## Summary

This paper addresses the ineffectiveness of SVRG for deep neural networks by introducing a simple scalar coefficient $\alpha$ on the variance reduction term, with a linear decay schedule. The authors first demonstrate analytically (via control variates theory) that the optimal coefficient per gradient component is not 1 and decreases with model depth and over training time. They then show that standard SVRG with coefficient 1 can increase gradient variance for multi-layer networks. Their proposed method, alpha-SVRG, applies a linearly decaying scalar coefficient, and the paper reports consistent training loss reductions over both the AdamW baseline and standard SVRG across architectures (ConvNeXt, ViT, Swin, Mixer) on ImageNet-1K and nine smaller datasets.

## Strengths

- **Empirical discovery that optimal SVRG coefficient decreases with depth and over training time**: Section 3, Figure 3 shows analytically computed per-component optimal coefficients for MLPs of varying depth. For logistic regression the optimal coefficient stays near 1, but for MLP-2 and MLP-4 it drops well below 1 and decays as training progresses. This directly motivates why the default coefficient of 1 fails and why a decaying schedule is needed — a concrete, specific finding.

- **Consistent training-loss reduction across architectures on ImageNet-1K**: Table 1 reports that alpha-SVRG achieves lower training loss than both the AdamW baseline and standard SVRG for all six tested models (ConvNeXt-F, ViT-T/16, Swin-F, Mixer-S/32, ViT-B/16, ConvNeXt-B), spanning 5M–89M parameters. This is the paper's primary empirical evidence that the method generalizes to modern, real-world neural networks.

- **Theoretical grounding via control variates**: Equation (5)–(8) derives the optimal coefficient as the covariance ratio between snapshot and current gradients, formally linking it to their correlation. This analysis shows why a coefficient not equal to 1 is required and why it must vary over time, going beyond a purely heuristic modification.

- **Robustness of initial coefficient $\alpha_0$**: Figure 8 (ablation) shows that alpha-SVRG with initial values between 0.2 and 0.9 all yield lower training loss than the baseline on ConvNeXt-F/STL-10, indicating the method does not require precise tuning.

- **Works with AdamW, not only SGD**: Figure 6 demonstrates alpha-SVRG with AdamW reduces gradient variance and training loss for an MLP-4 on CIFAR-10, while standard SVRG with AdamW increases variance. This shows applicability with the optimizer most commonly used in modern deep learning.

- **Demonstration on a modern deep ConvNet**: Figure 7 shows that on ConvNeXt-F with CIFAR-10, alpha-SVRG steadily reduces gradient variance and achieves lower training loss than both standard SVRG and the AdamW baseline, directly addressing the claim that SVRG can be made effective for deep networks.

## Weaknesses

### Fatal

None.

### Major

- **Comparison with standard SVRG lacks clarity on hyperparameter tuning, weakening the headline claim**. The paper consistently claims that alpha-SVRG outperforms "standard SVRG" (coefficient=1), but it does not report whether the learning rate or other hyperparameters were tuned for standard SVRG. SVRG with coefficient=1 modifies the gradient more aggressively than alpha-SVRG and may require a different learning rate to work well. Since the paper does not document any tuning for the SVRG baseline (e.g., learning rate sweep, schedule adjustments), the comparison conflates the effect of the coefficient with potentially suboptimal hyperparameters for the baseline. This does **not** affect the well-controlled alpha-SVRG vs. AdamW-baseline comparison (which is clean), but it weakens the secondary but prominently advertised claim that alpha-SVRG is better than standard SVRG. The paper would be stronger by either tuning the SVRG baseline's learning rate or comparing to SVRG with a fixed optimal constant coefficient found by grid search.

### Minor

- **Single-run results with no reported variance**. Neural network training is stochastic, yet all experiments report single numbers with no indication of variability across runs. For ImageNet-scale experiments single runs are common practice, so this is not a fatal omission, but on smaller datasets (CIFAR-100, STL-10, etc.) reporting results from at least 2–3 seeds would meaningfully strengthen the evidence.

- **The scalar linear decay schedule is a heuristic that is not directly validated for deep networks**. The optimal coefficient is derived per gradient component (Equation 8), and only its *mean* over components is plotted (Figure 3, MLPs up to 4 layers). The variance or distribution of per-component optimal coefficients is never examined, so it is unclear whether a single scalar is a good proxy. Moreover, the linear decay schedule is compared directly to the optimal coefficient only for MLP-4 (Figure 6), not for deeper networks like ConvNeXt-F. The paper is transparent that the linear schedule is a practical heuristic (lines 104–106), but the empirical justification for this particular schedule on modern architectures is thin. Alternative schedules (exponential, step decay) are not compared.

- **Small batch-size failure mode is identified but not deeply analyzed**. Figure 9 shows alpha-SVRG underperforms the baseline for small batch sizes (below the default 128). The paper correctly flags this as a limitation (line 150: "a sufficiently large batch size is essential"), but does not investigate why the correlation between snapshot and model gradients breaks down at small batch sizes, nor does it propose mitigations. This limits the method's applicability to the common setting of training with small batches on limited GPU memory.

- **Optimal coefficient behavior is only analyzed on tiny models (MLPs up to 4 layers)**. The two key observations (coefficient decreases with depth and over training time) are empirically validated only on Logistic Regression, MLP-2, and MLP-4 using CIFAR-10. For the deeper ConvNeXt-F, the paper only shows that alpha-SVRG *works* (Figures 7–10), not that the optimal coefficient actually follows the hypothesized trend. Computing the full optimal coefficient for deep networks may be impractical, but an approximate analysis (e.g., on a subset of parameters or data) would substantially strengthen the theoretical motivation.

### Trivial

- None.

## Nice-to-Haves

- **Wall-clock time comparison**: alpha-SVRG requires periodic full-gradient computation for the snapshot. The paper mentions the trade-off in the snapshot interval ablation (Figure 10) but provides no timing data. A plot of training loss vs. wall-clock time would help practitioners evaluate the computational overhead.

- **Comparison with a constant-coefficient SVRG baseline**: To isolate the benefit of the *decay schedule* from the benefit of simply using a smaller coefficient, a natural baseline is SVRG with a constant coefficient (e.g., $\alpha=0.5$ found by grid search). This would clarify whether the decay matters or a fixed small coefficient suffices.

- **Direct analysis of optimal coefficient (approximate) for a deeper network**: Using an approximation (e.g., a subset of parameters or a smaller data sample to estimate covariances) for a small ResNet on CIFAR-10 would provide direct evidence that the optimal coefficient decreases over time for deeper networks, beyond just MLPs.

## Removed Points

- **"Only training loss reported for ImageNet"**: The paper explicitly states "We report both the training loss and the validation accuracy" (line 130) and discusses validation generalization for ImageNet models (lines 140–141). The critic's claim is contradicted by the paper's own description. — REMOVED (factually incorrect)
- **"Missing discussion of AdaSVRG or related adaptive SVRG variants"**: Per policy, I cannot penalize for missing related works. — REMOVED (policy restriction)
- **"Generalization to non-vision domains"**: The paper's scope is clearly image classification; criticizing it for not testing NLP or other domains is scope creep. Moved to Nice-to-Haves. — REMOVED (scope creep)
- **"Gradient variance metrics not defined in main text"**: The paper references Table 1 (metric table) and states it employs three existing metrics. The table likely exists in the submission; the parser strips such content. — REMOVED (parser artifact)
- **"Theoretical motivation is weaker than presented" framing as a fatal issue**: The paper is transparent that the scalar linear schedule is a practical heuristic following from the observed trend. This is a minor limitation, not a methodological gap. — DEMOTED to Minor.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the per-component optimal coefficient derivation and the scalar approximation. The paper itself correctly identifies that the optimal coefficient is per gradient component, but the scalar schedule works surprisingly well in practice. This suggests that gradient components may share similar temporal dynamics in their correlation with the snapshot — an implicit finding that the reviews did not articulate but that the paper's MLP-4 comparison (Figure 6) partially supports. Whether this pattern holds for deeper, structured networks like ConvNeXt or ViT remains an open empirical question that neither the paper nor the reviews fully resolve.

## Suggestions

- Document the learning rate and any hyperparameter tuning used for the standard SVRG baseline. Ideally, perform a small LR sweep for standard SVRG on at least one setting (e.g., ConvNeXt-F on STL-10) to demonstrate that alpha-SVRG's advantage is not simply due to mistuned baselines.
- Add a constant-coefficient SVRG baseline (e.g., $\alpha=0.5$ fixed) to separate the benefit of the decay schedule from the benefit of a smaller coefficient.
- Report results from 2–3 seeds for the smaller-dataset experiments (CIFAR-100, STL-10, etc.) to quantify variance.
- Add an approximate analysis of the optimal coefficient for a deeper network (e.g., a small ResNet on CIFAR-10, using a parameter subset) to validate the decreasing-trend assumption beyond MLPs.
- Include a brief discussion or ablation on alternative decay schedules (exponential, step) to justify the linear choice.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>