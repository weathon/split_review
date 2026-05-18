Now I have thoroughly verified all claims against the paper. Let me compose the final consolidated review.

---

## Summary

This paper proposes PAST (Privacy-Aware Sparsity Tuning), a method that adaptively penalizes model parameters based on their "privacy sensitivity" — defined as the gradient of the loss gap between members and non-members with respect to each parameter. The key empirical finding motivating the method is that only ~20% of parameters account for ~89% of the total privacy sensitivity. PAST applies stronger ℓ₁ regularization to these sensitive parameters while sparing the rest, and is applied as a post-convergence tuning phase. Experiments across five datasets (Texas100, Purchase100, CIFAR-10/100, ImageNet), eight baselines, and multiple attack types show improved privacy-utility trade-offs.

## Strengths

1. **Novel empirical finding about privacy sensitivity concentration**: The paper directly demonstrates (Figure 1b) that privacy sensitivity is highly concentrated — 97% of parameters have sensitivity below 0.1, and the top 20% account for 89.27% of total sensitivity. This concrete measurement motivates the adaptive regularization approach and is itself a useful observation for the field.

2. **Consistent and broad empirical improvement across settings**: PAST shows better privacy-utility trade-offs than eight baselines across five datasets spanning tabular data (Texas100, Purchase100) and image data (CIFAR-10/100, ImageNet), under multiple attack types (NN-based, metric-based, augmentation-based). The privacy-utility curves (Figures 2-3) consistently lie below those of baselines in the region where utility exceeds the undefended model. On CIFAR-10, PAST reduces loss-based attack advantage from 14.8% to 5.2% while maintaining accuracy.

3. **Ablation study cleanly isolates the benefit of adaptive weighting**: Figure 5a compares ℓ₁, ℓ₂, ℓ₁+adaptive weights (PAST), and ℓ₂+adaptive weights under the *same* post-convergence tuning protocol. PAST (ℓ₁+Ours) outperforms uniform ℓ₁ and ℓ₂, confirming the adaptive weights — not just tuning schedule or choice of norm — drive the improvement. The paper explicitly states all four combinations are applied "during tuning" (line 256), so protocol is controlled.

4. **Compatibility with existing defenses**: Table 3 shows that applying PAST on top of models already defended by AdvReg, CCL, Label Smoothing, MixupMMD, or RelaxLoss further improves P1 scores (e.g., AdvReg: 0.720 → 0.784), demonstrating PAST is complementary rather than a replacement.

5. **Low computational overhead**: Figure 6c reports PAST adds only 10.4% time overhead over standard training (1374s vs 1245s for DenseNet121 on CIFAR-100), making it practical for deployment.

## Weaknesses

### Fatal
None.

### Major

1. **No error bars or variance reporting for any experimental result.** Every quantitative result in the paper — Tables 1-2, Figures 2-6 — is reported as a single point without standard deviations, confidence intervals, or indication of run-to-run variability. Given the stochasticity from training (random seeds), dataset splitting (six subsets), subsampling for loss-gap computation (Sₘ, Sₙ), and hyperparameter choices, single-point numbers make it impossible to assess whether the reported improvements (e.g., P1 score 0.784 vs. 0.638 on CIFAR-10) are statistically reliable or within noise range. This is the most significant weakness because it undermines the evaluability of the core empirical contribution. **The paper would benefit from at least 3-5 seeds with standard deviations for the key results.**

2. **Unclear training protocol for baselines in the main comparison (Figures 2-3).** PAST uses a specific two-phase protocol: 100 epochs standard training (λ=0), then 20-50 epochs tuning with regularization. The paper states that baselines' hyperparameters "align with protocols established by previous work" but does not specify whether the baselines in Figures 2-3 were (a) trained from scratch with their regularizations applied throughout, or (b) applied post-convergence like PAST. If the former, then the comparison confounds the effect of the adaptive weights with the effect of the two-phase training schedule. This concern is mitigated by the ablation study (Figure 5a), where all methods share the same tuning protocol and PAST still wins, so the core claim survives. But for the main results, the paper should clarify the baseline training protocol or re-run baselines under matched conditions.

### Minor

3. **Ambiguous notation in the adaptive weight formula (γᵢ, Equation after line 149).** The formula writes: γᵢ = |ℳ(θᵢ)| ∇_{θᵢ} **G̃**\textsubscript{θ} / Σ_{θⱼ∈ℳ(θᵢ)} ∇_{θⱼ} **G̃**\textsubscript{θ}. Two issues: (a) The tilde on **G̃**\textsubscript{θ} is never defined — the paper defines **G**\textsubscript{θ} (without tilde, line 147) but then uses **G̃**\textsubscript{θ} in the γᵢ formula with no explanation of what the tilde denotes (e.g., stop-gradient? absolute value? something else?). (b) Since gradients of the loss gap can be negative, the denominator could theoretically be near zero or negative, leading to undefined or negative weights. The formula as written does not include absolute values. Clarifying this is necessary for exact reproducibility.

4. **Motivation analysis (Figure 1b) limited to one dataset/architecture.** The discovery that "top 20% of parameters account for 89.27% of total sensitivity" is demonstrated only for ResNet-18 on CIFAR-10. The paper does not show whether this concentration pattern holds for other architectures (e.g., DenseNet, MLPs used for tabular data) or datasets. While the method's effectiveness across those settings indirectly suggests the phenomenon generalizes, direct evidence would strengthen the claim.

5. **No discussion of whether γᵢ or the subsets Sₘ, Sₙ are updated during tuning.** The paper states γᵢ is "detached from the computational graph" and computed once (implied), but does not explicitly state whether Sₘ and Sₙ are refreshed or fixed throughout the 20-50 tuning epochs, nor whether γᵢ could benefit from periodic recomputation as the model changes.

### Trivial

6. **Time comparison (Figure 6c) reported without variance or repetition count.** The caption states time was "recorded for DenseNet121 on CIFAR-100 using a single RTX 4090 GPU" but does not specify how many runs were averaged or whether the 10.4% figure is stable.

7. **P1 score uses "highest attack advantage among all attack methods" but does not specify which attack gave the highest value for each dataset** (Table 1 caption). This is a minor reporting clarity issue.

## Nice-to-Haves

- A sensitivity/bootstrapping analysis of how the choice of Sₘ and Sₙ affects the γᵢ weights and final performance would increase confidence in the method's stability.
- An ablation of the module normalization factor |ℳ(θᵢ)| (i.e., what happens without per-module normalization) would clarify whether this design choice is important.
- Experimenting with dynamic γᵢ recomputation during tuning (e.g., every N epochs) could potentially improve results and is a natural extension.

## Removed Points

The following points from the harsh review are removed with justification:

1. **"Unfair baseline comparison due to differing access to non-member data"** — The paper explicitly states (line 199) that the inference set is used by "our method and adversarial training algorithms that incorporate adversary loss—such as Mixup+MMD and adversarial regularization." The baselines that do not use non-member data (ℓ₁, ℓ₂, Dropout, etc.) are compared against PAST in their original forms, which is standard practice. A method's use of additional information is inherent to its design, not an unfair comparison, and the paper is transparent about this. The key baselines that also use non-member data (Mixup+MMD, AdvReg) are fairly compared and PAST still wins.

2. **"Ablation study confounds protocol (ℓ₁/ℓ₂ likely trained from scratch vs PAST post-convergence)"** — This is factually incorrect. The paper states (line 256): "Specifically, we used four combinations **during tuning**: ℓ₁ regularization (L1), ℓ₁ regularization + adaptive weight (L1+Ours), ℓ₂ regularization (L2), and ℓ₂ regularization + adaptive weight (L2+Ours)." All four are applied under the **same post-convergence tuning protocol**, so the comparison is fair and does isolate the adaptive weights.

3. **"The paper does not include analysis of how |ℳ(θᵢ)| factor affects results"** — This is a minor wishlist item, not a genuine weakness. The normalization is a standard design choice for per-module weighting.

4. **"Variance of loss-gap gradient due to random subsamples Sₘ and Sₙ is not discussed"** — This is speculation about variance that may or may not exist, not an observed flaw. Moved to Nice-to-Haves.

5. **"Whether the same Sₘ and Sₙ are used throughout tuning or refreshed"** — This is a fair question but belongs in clarifications/Nice-to-Haves, not as a weakness.

## Novel Insights

The reviewer combination surfaces an important tension not explicitly discussed in the paper: PAST's key advantage comes from identifying *which* parameters to regularize, but the method's reliance on a static one-shot computation of γᵢ raises the question of whether the privacy sensitivity landscape shifts during tuning. If sensitivity patterns change as parameters are driven to zero, the initial γᵢ weights may become stale. Whether dynamic recomputation would improve results is an open question worth exploring. Additionally, the concentration of privacy sensitivity in ~20% of parameters is reminiscent of the "lottery ticket hypothesis" and deep learning's intrinsic sparsity — PAST essentially finds and prunes a "privacy-critical subnet," which connects to broader literature on sparse subnetworks and information bottleneck principles.

## Suggestions

1. **Most important**: Add at least 3-5 random seeds with standard deviations for all core results (Tables 1-2, key comparisons in Figures 2-3). This is the single change that would most strengthen the paper.
2. Clarify the γᵢ formula: define **G̃** explicitly and address the sign issue (absolute values or implicit assumption).
3. Specify the training protocol for baselines in Figures 2-3 (from scratch or post-convergence) to rule out the protocol confound. The ablation already addresses this for the ℓ₁/ℓ₂ comparison, but the main figure should be clear.
4. State explicitly whether Sₘ, Sₙ, and γᵢ are fixed or updated during tuning.
5. Add a brief discussion of whether the privacy sensitivity concentration pattern (Figure 1b) generalizes to other datasets/architectures (even a qualitative statement based on the experimental results would help).

## Score and Decision

This paper makes a genuine contribution: it identifies a meaningful empirical phenomenon (concentrated privacy sensitivity) and leverages it into a simple, effective, computationally cheap defense that consistently improves over eight baselines across five datasets. The writing is clear and the experimental scope is broad.

The weaknesses are real but addressable. The lack of error bars is the most significant concern, but the consistency of the improvement across datasets, attacks, and ablations provides enough convergent evidence that the result is not likely noise. The baseline protocol concern is partially mitigated by the controlled ablation study. The formula ambiguity is a minor fix.

I rate this paper as a **borderline accept** that would be a **clear accept** after addressing the error bars and protocol clarity issues.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>