Now I have a thorough understanding of the paper. Let me synthesize my final review.

Key findings from my verification:

1. **Conflated contributions in baseline comparison**: The harsh critic raises this as a critical issue. The paper does partially address this for *dataset distillation* baselines (Table 2, FRePo VI, RCIG VI, AVBPC), but NOT for the *BPC baselines* in Table 1. This is a real concern but needs to be placed in context. BPC baselines use SGMCMC, which is fundamentally their inference method; VBPC uses last-layer VI. The paper's contribution IS the combined method (pseudo-coreset + VI). The comparison in Table 1 is fair in the sense that it compares complete methods. However, the claim that VBPC learns *better pseudo-coresets* is not fully supported without isolating the inference factor. This is a legitimate concern but more moderate than the critic suggests — it's a major concern, not fatal.

2. **No calibration metrics**: The paper claims VBPC "effectively captures epistemic uncertainty" (line 290) but only reports ACC and NLL. For Bayesian methods, NLL is a proper scoring rule that captures both accuracy and calibration. However, ECE/Brier score would provide more direct evidence of calibration quality. This is a real concern but moderate — NLL is a standard and principled metric for evaluating predictive distributions.

3. **Unvalidated mean-field Gaussian-softmax approximation**: Eq. 25 relies on a mean-field approximation from Lu et al. (2020). The paper does cite this. The approximation quality is not experimentally validated in the paper. This is a real and valid concern, particularly since it underpins both training and inference.

4. **Gaussian/softmax likelihood mismatch**: The paper acknowledges this as a "detour" and provides justification (infinitely-wide NN literature). The impact is not analyzed. This is a valid concern.

5. **Model pool and fixed φ assumption**: The critic claims the model pool changes φ during training, contradicting the closed-form solution's assumption about φ. However, the paper describes the model pool procedure clearly: at each step, one θ is sampled, S is trained for one step with that φ, then θ is updated. The closed-form solution for the inner problem is computed with φ fixed for that step. This is standard bilevel optimization with alternating updates — not a contradiction.

6. **Table 2 confusion**: The paper states "↓ indicates performance drop compare to original method," which means that when applying VI to FRePo/RCIG coresets or FRePo's method to VBPC coresets, the drop is measured. This is consistent — no real confusion.

7. **Scaling beyond 3-layer ConvNets**: Table 4 already includes AlexNet, ResNet18, VGG11 — so the critic's claim that "all tested architectures are still relatively small" is partially incorrect; they do test larger architectures.

8. **BN statistics and OOD**: This is a minor concern specific to the experimental setup.

## Summary

The paper proposes Variational Bayesian Pseudo-Coreset (VBPC), reformulating Bayesian pseudo-coreset learning by using last-layer variational inference with Gaussian likelihood in the inner optimization and softmax likelihood in the outer optimization. This enables a closed-form solution for the coreset VI problem (eliminating stop-gradients), a mean-field approximation for single-forward-pass BMA (eliminating SGMCMC), and Woodbury-identity-based memory-efficient computation (reducing space from O(h²) to O(n̂²)).

## Strengths

- The closed-form solution for the last-layer variational posterior with Gaussian likelihood (Eqs. 20-21) is a clean technical contribution that genuinely enables gradient-based bilevel optimization without stop-gradients or computation graph unrolling. This directly resolves problem #2 from prior BPC work (stop-gradient suboptimality).

- The memory-efficient computation via Woodbury/Weinstein-Aronszajn identities (Eqs. 28-31) reducing training memory from O(h²) to O(n̂²) and inference memory to O(n̂h + n̂²) is a practical engineering contribution with empirical validation in Table 5 showing nearly halved memory and <20% training time.

- Strong empirical performance across all five benchmark datasets and all ipc settings in both ACC and NLL (Table 1), with particularly large improvements on NLL, plus OOD robustness results on CIFAR10-C (Table 3) and architecture generalization to AlexNet/ResNet18/VGG11 (Table 4).

- The paper partially addresses the concern about conflated contributions by applying VI to FRePo/RCIG pseudo-coresets and evaluating VBPC pseudo-coresets with FRePo's method (Table 2), showing VBPC's performance advantage is not solely due to the inference method.

## Weaknesses

### Fatal
None.

### Major

- **The main BPC comparison (Table 1) conflates pseudo-coreset quality with inference method differences.** Table 1 compares VBPC (last-layer VI + pseudo-coreset) against BPC baselines (SGMCMC + pseudo-coreset). While the paper provides a partial isolation experiment for dataset distillation baselines (Table 2: FRePo VI, RCIG VI, AVBPC), it does NOT perform this isolation for the BPC baselines. Applying last-layer VI to BPC-learned pseudo-coresets or applying SGMCMC sampling to VBPC pseudo-coresets would reveal whether VBPC's advantages in Table 1 come from better pseudo-coresets or from the inference paradigm shift. Without this, the paper's claim that VBPC "effectively learns the variational distribution" for the BPC setting cannot be fully disentangled from the inherent differences between VI and SGMCMC inference. This matters because the paper's central positioning is about improving pseudo-coreset learning, not just replacing SGMCMC with VI.

- **No calibration metrics despite making strong uncertainty quantification claims.** The paper claims VBPC "effectively captures epistemic uncertainty" (Section 5.1, line 290) and "improves robustness to distributional shifts" (Section 5.2, line 299). While NLL is a proper scoring rule that partially reflects calibration quality, for Bayesian methods claiming superior uncertainty quantification, dedicated calibration metrics such as Expected Calibration Error (ECE) or Brier score would provide more direct and interpretable evidence. This is particularly important given that the mean-field softmax approximation (Eq. 25) divides logits by √(1+αΣ*), which could sharpen the predictive distribution and produce overconfidence — a pattern that NLL alone may not reveal.

### Minor

- **The mean-field Gaussian-softmax approximation (Eq. 25) is unvalidated experimentally.** This approximation, derived from Lu et al. (2020), underpins both the training objective and inference. If it is poor when predictive variances Σ* are large (i.e., for high-uncertainty predictions), the coreset is trained against a distorted objective and predictions may be miscalibrated precisely where uncertainty quantification matters most. A comparison of Eq. 25 against Monte Carlo estimation of the true integral (Eq. 23) would strengthen confidence in the method. The paper cites the source but provides no experimental validation of approximation quality.

- **The Gaussian/softmax likelihood mismatch in the bilevel formulation is acknowledged but unanalyzed.** Section 3.3 explicitly uses Gaussian likelihood for the coreset VI problem (p_S) and softmax for the dataset VI problem (p_D). The paper acknowledges this is a "detour" motivated by closed-form tractability and cites the infinitely-wide neural network literature for justification. However, the divergence between the Gaussian-likelihood posterior and the softmax-likelihood posterior is never analyzed. A sensitivity analysis over the Gaussian likelihood precision γ would help establish how robust the method is to this design choice.

### Trivial

- None.

## Nice-to-Haves

- Apply last-layer VI to BPC baselines' pseudo-coresets (or SGMCMC to VBPC pseudo-coresets) in Table 1 to isolate the inference method from pseudo-coreset quality.
- Report ECE/Brier score on CIFAR10-C and the main benchmarks.
- Validate the mean-field softmax approximation quality experimentally by comparing Eq. 25 against Monte Carlo estimates.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Table 2 presentation is confusing"** — The table format (↓ for performance drop) is consistently described in the caption and text; the critic may have misread the table direction. The paper clarifies the meaning.

- **"Model pool contradicts closed-form solution's fixed-φ assumption"** — The model pool uses alternating updates: at each training step, φ is fixed while the inner problem is solved, then φ is updated. This is standard practice in bilevel optimization and does not contradict the per-step closed-form solution which assumes φ fixed for that step.

- **"Scaling beyond 3-layer ConvNets untested"** — Table 4 already tests AlexNet, ResNet18, and VGG11, contradicting the critic's claim that only shallow architectures are tested.

- **"BN statistics affect OOD calibration and this is not discussed"** — While potentially true, this is a very minor experimental detail common to all methods in the comparison, not specific to VBPC.

- **"Number of SGMCMC samples not reported, potentially artificially inflating VBPC's advantage"** — This is speculative. BPC baseline implementations follow their published settings, and there is no evidence they use inadequate sample counts.

- **"h for the 3-layer ConvNet is not stated"** — Minor presentation detail; the memory savings claim is validated empirically in Table 5 regardless.

- **"Influence function interpretation is not deeply exploited"** — This is a nice theoretical observation the paper provides, not a required contribution. Criticizing it for not being exploited further is scope creep.

## Novel Insights

The paper's key insight — that using Gaussian likelihood for the inner coreset VI problem (while keeping softmax for the outer dataset VI problem) enables a fully closed-form bilevel gradient — is genuinely creative. The resulting reformulation of the bilevel gradient as an influence function (Eq. 22) provides a principled theoretical grounding but is presented more as an observation than a tool that is leveraged for deeper analysis or design choices. The most interesting unexplored question raised by this work is whether the Gaussian/softmax likelihood mismatch acts as an implicit regularizer or introduces systematic bias in the learned coreset.

## Suggestions

- Add an ablation experiment isolating the inference method from pseudo-coreset quality: train BPC baselines' pseudo-coresets, then apply last-layer VI to them for BMA, and compare with VBPC's own coreset evaluated under last-layer VI. This single experiment would substantially strengthen the paper's central claim.

- Add ECE results on at least CIFAR10-C to directly support the uncertainty quantification claims, since the paper frames VBPC as a Bayesian method.

## Score and Decision

The paper makes a genuine technical contribution: deriving a closed-form solution for last-layer VI with Gaussian likelihood that enables gradient-based bilevel optimization of Bayesian pseudo-coresets without stop-gradients, combined with practical memory-efficient computation. The experimental results are comprehensive (5 benchmarks, OOD, architecture generalization, efficiency). The two major weaknesses — conflated contributions in the main BPC comparison and missing calibration metrics for uncertainty claims — are significant but do not invalidate the contributions. The method works well empirically and the technical framework is sound. The paper would be notably stronger with the proposed isolation experiment and calibration metrics, but the contributions stand as meaningful.

Originality: Good — the combination of last-layer VI with Gaussian likelihood for BPC is novel and well-motivated.
Importance: Moderate — addresses real computational problems in BPC but in a specific niche.
Claims support: Moderate — main empirical claims partially supported but lack critical isolation experiments.
Soundness of experiments: Moderate — broad evaluation but missing calibration metrics and isolation ablation.
Clarity: Good — well-structured derivation, though the Gaussian/softmax mismatch could be discussed more.
Value: Moderate — meaningful contribution to the BPC literature with practical efficiency gains.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>