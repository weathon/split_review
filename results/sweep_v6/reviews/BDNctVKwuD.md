Now I have everything I need. Let me write the consolidated review.

## Summary

This paper identifies that HiResCAM explanations admit a spurious shift (adding the same matrix M to all class-level CAMs does not change softmax output), proposes ContrastiveCAMs (pairwise differences of HiResCAMs) that are invariant to this shift, and introduces Core-Focused Cross-Entropy (CFCE), a loss that penalizes non-core region contributions by integrating ContrastiveCAMs into training. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC show that CFCE improves core-region alignment (e.g., Hard-ImageNet GradCAM IoU from 16.25% to 51.52%, ContrastiveCAM IoU from 30.27% to 93.39%) and transfers to downstream segmentation.

## Strengths

1. **Strong empirical gains on Hard-ImageNet with multiple evaluation axes.** CFCE+KL raises GradCAM IoU from 16.25% to 51.52% (Table 2), improves RFS from negative to positive (+0.236), and dramatically reduces accuracy under core-region ablation (Gray Mask: 76.53%→45.49%). These improvements are reported across ablation metrics, saliency alignment, and relative foreground sensitivity — not just a single measure — and the GradCAM metric provides evaluation independent of the proposed ContrastiveCAM.

2. **Effectiveness with approximate and weak masks (SAM, bounding boxes).** On Oxford-IIIT Pets, CFCE with SAM or bounding-box masks achieves IoU scores comparable to ground-truth masks (e.g., 83.95% SAM vs. 82.92% GT in binary validation, Table 3). This demonstrates practical applicability when precise core masks are unavailable — a genuine strength for real-world deployment.

3. **Downstream segmentation transfer.** CFCE+KL-trained backbones yield consistently higher per-class IoU on PASCAL VOC segmentation compared to CE-trained backbones in both fine-tuned and end-to-end settings (Figure 4). This shows the alignment benefit transfers beyond classification.

4. **Principled motivation connecting interpretability and training.** Proposition 4.2 formally decomposes cross-entropy into core and non-core ContrastiveCAM contributions, showing theoretically why standard CE does not penalize non-core region use. Theorem 4.6 establishes classification-calibration of CFCE, connecting the loss to core-constrained risk minimization.

5. **Qualitative demonstration of non-core suppression.** Figure 3 shows concrete examples where CFCE reduces non-core contributions (e.g., core/total ratio improving from 0.032 to 0.848 for "Seahorse"), providing visual evidence corroborating the quantitative metrics.

## Weaknesses

### Major

1. **The optimization procedure for CFCE is underspecified.** The CFCE loss (Definition 4.5) involves `CAM_{(c_t,c)}^{Cntrst}`, which depends on gradients of logits with respect to feature maps. Differentiating this loss with respect to model parameters requires second-order gradients (through the gradient computation). The paper provides no description of how this is implemented — whether via `create_graph=True` in autograd, stop-gradient on CAM values, or alternating updates. This is not a minor implementation detail: it determines the method's feasibility, computational cost, and convergence behavior. The paper reports no training time, stability analysis, or hyperparameter sensitivity for this aspect. This gap must be addressed for the contribution to be reproducible.

2. **Partial evaluation conflation despite mitigation.** The primary evaluation metric (ContrastiveCAM IoU) partially overlaps with the CFCE training objective (which explicitly penalizes non-core ContrastiveCAM contributions). While the paper partially mitigates this by also reporting GradCAM IoU (where CFCE+KL achieves 51.52% vs. 16.25%), the headline result of 93.39% ContrastiveCAM IoU should be treated as expected optimization behavior, not independent evidence of alignment quality. The baselines lack ContrastiveCAM IoU values (marked "—"), making it impossible to compare the gap on this metric across all methods. Additionally, the ablation accuracy drops (Gray Mask: 76.53%→41.78%) could partly reflect the model's overall accuracy decline (93.69%→90.35%) and its inability to use any features outside the penalized non-core regions, rather than a genuine shift to core-only reliance. The paper would benefit from a causal evaluation (e.g., replacing non-core patches with noise and measuring accuracy change) that is independent of the training loss.

3. **Accuracy drop on some datasets not adequately justified.** On Oxford-IIIT Pets multiclass, CFCE reduces validation accuracy from 94.41% (CE) to 92.96% (CFCE) and 90.08% (CFCE+KL). On Hard-ImageNet, unablated accuracy drops from 93.69% to 90.35%. The paper presents this as an expected trade-off but does not establish whether the IoU gains justify the accuracy cost for any practical setting. Given that core regions constitute only 13.96% of Hard-ImageNet images on average, the model is forced to rely on limited signal — the paper should analyze whether this accuracy drop is necessary or could be reduced with better regularization.

### Minor

1. **The HiResCAM spurious-shift observation (Theorem 3.2) is modest as a theoretical contribution.** The invariance is a straightforward algebraic consequence of softmax shift-invariance combined with the fact that HiResCAMs sum to logits. The paper frames this as a significant limitation, but any attribution method whose per-class outputs sum to logits shares this property, and the actual computed HiResCAM for a given model and input is still uniquely determined. The resulting ContrastiveCAM fix (differences of HiResCAMs) is the clean and useful part, but the theoretical critique is thinner than claimed.

2. **Absolute value penalization of non-core regions (Definition 4.5) may be overly restrictive.** Using `|CAM|` for non-core regions penalizes both positive and negative contributions. Negative CAM values can represent evidence *against* the target class — suppressing these could remove useful negative signal. The paper does not discuss this design choice or explore alternatives (e.g., asymmetric penalties or ReLU-based masking).

3. **KL regularization formulation (Definition 4.7) is unclearly specified.** The term `σ(λ₂H)` applies softmax to a binary mask, producing a 2D probability distribution. While mathematically valid, this is an unconventional target distribution for a spatial KL penalty, and the paper does not justify why softmax-normalized binary masks are an appropriate target for ContrastiveCAM values. The ambiguity in the notation (softmax of a 2D matrix) makes this hard to reproduce without the appendix.

4. **Accuracy-IoU trade-off not systematically explored.** For Pets multiclass, CFCE+KL achieves 93.12% IoU but at 90.08% accuracy vs. 94.41% for CE. The paper does not study whether tuning λ₁, λ₂, λ₃ can recover accuracy while maintaining IoU gains, or whether the trade-off is inherent.

### Trivial

- None beyond the issues already listed.

## Nice-to-Haves

- A causal evaluation protocol (e.g., swapping or inserting patches from other classes into non-core regions) would strengthen the claim that CFCE genuinely shifts reliance to core features, rather than simply suppressing all non-core signals.
- An analysis of how mask errors (underestimated or overestimated core regions) affect accuracy and IoU would be practically valuable, given the method's reliance on mask quality.
- Comparison with simpler baselines such as feature-map masking (multiplying feature maps by core mask before GAP) or direct attention regularization with GradCAM/HiResCAM penalties would help isolate the benefit of the ContrastiveCAM formulation.

## Removed Points

The following points from the reviewer inputs are removed with justification:

- **"GradCAM is used for baselines while ContrastiveCAM is used for CFCE models"** — The paper reports GradCAM IoU for ALL methods (Table 2, column "GradCAM IoU"). ContrastiveCAM IoU is reported as supplementary for CE w/ Arch and CFCE models. The claim misrepresents what the paper actually reports.

- **"The paper should include standard ResNet with cross-entropy as a baseline"** — This baseline is already present: "Cross-Entropy" row in Table 2 (94.25% accuracy, 18.44% GradCAM IoU).

- **"Theorem 4.6 proof is deferred to the appendix... claim should be treated with caution"** — The appendix exists in the original submission; it was stripped by the parser. Per review policy, missing appendix content is not a valid criticism.

- **"No mention of learning rate, optimizer, batch size, or number of epochs"** — The paper explicitly states training details are in Appendix C (line 289). These are deferred to the appendix as standard practice.

- **"Hard-ImageNet accuracy of 94.25% is questioned"** — Hard-ImageNet is a subset of ImageNet with specific classes, not the full 1000-class set. 94.25% top-1 on a subset is entirely plausible for a fine-tuned ResNet-50.

- **Formatting nitpicks and rewriting suggestions** — Removed per policy.

## Novel Insights

None beyond the paper's own contributions. The key observations (HiResCAM admits spurious shifts, CE does not inherently penalize non-core use, ContrastiveCAM differences remove the M-invariance) are all stated within the paper. The reviews did not surface a novel synthesis beyond what the authors already provide.

## Suggestions

1. **Clarify the optimization procedure for CFCE.** Specify whether the CAM computation is differentiated through (with `create_graph=True` or equivalent), treated as constant (stop-gradient), or optimized via alternating updates. Report training time overhead and any stability issues observed.

2. **Report ContrastiveCAM IoU for all baselines** (including vanilla CE, CORM, DFR) to enable complete comparison and address evaluability concerns.

3. **Provide a controlled study of the accuracy-IoU trade-off** by varying the strength of the non-core penalty (e.g., λ scaling) and plotting the Pareto frontier.

4. **Add a causal manipulation experiment** (e.g., replacing non-core patches with random noise or out-of-distribution content) to independently verify that CFCE models rely on core regions rather than simply being unable to use non-core regions.

5. **Justify or relax the absolute value penalty** on non-core ContrastiveCAM contributions — consider asymmetric penalties or different handling of negative values.

## Score and Decision

**Calibration anchors used (selected from batch):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `PBjCTeDL6o.md` (Unlearning-based Neural Interpretations) | 8.00 | Stronger — cleaner theoretical framing, more rigorous evaluation. Paper under review has underspecified optimization and weaker theory. |
| `Bk13Qfu8Ru.md` (Severing Spurious Correlations) | 7.00 | Stronger — thorough empirical analysis with principled approach. Paper under review has comparable ambition but less clean evaluation. |
| `Tj3xLVuE9f.md` (On the Foundations of Shortcut Learning) | 6.80 | Stronger in theoretical depth. Paper under review has more applied contribution but weaker foundations. |
| `57NfyYxh5f.md` (How to Probe) | 6.25 | Comparable — both have interesting empirical findings but significant concerns. How to Probe's concerns were about limited architectures; this paper's concerns are about optimization specification and evaluation. |
| `T7q5LBGISH.md` (Saliency map smoothing) | 5.25 | Comparable — both have a reasonable idea but limitations in execution. The smoothing paper was rejected; this paper has larger empirical scope but also more significant methodological ambiguity. |
| `yeEWZ8qvlS.md` (Signal Vectors) | 5.00 | Weaker — limited experimentation. Paper under review has stronger empirical evidence. |
| `FTSUDBM6lu.md` (Patch Ranking Map) | 2.50 | Much weaker. Paper under review is substantially more rigorous. |

**Score rationale:** The paper has genuine contributions — ContrastiveCAM is a clean fix to a real issue with HiResCAM, and CFCE produces convincing alignment improvements especially on Hard-ImageNet. However, the optimization procedure for the core loss (CFCE) is critically underspecified, and the evaluation partially conflates training target with evaluation metric. The theoretical contribution is modest, and the accuracy drop on some datasets is not adequately justified. Against the calibration anchors, this paper sits between the 5.25 (rejected) and 6.25 (accepted) papers — it has more empirical breadth than the former but more significant methodological gaps than the latter.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>