Now I have all the information I need to write the consolidated review. Let me synthesize everything carefully.

---

## Summary

This paper identifies a theoretical limitation in HiResCAM: its explanations are only determined up to an unknown additive matrix $M$, inherited from softmax's shift-invariance. The authors propose ContrastiveCAM, which cancels this $M$ by differencing class-wise HiResCAMs (yielding class-versus-class explanations provably invariant to the shift), and then leverage ContrastiveCAM to design Core-Focused Cross-Entropy (CFCE) — a training loss that penalizes reliance on non-core image regions via signed suppression in the log-sum-exp. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC show that CFCE dramatically shifts model reliance toward core regions (e.g., Gray BBOX accuracy on Hard-ImageNet drops from 72.49% to 31.66%) while largely preserving classification accuracy, and that the method works with coarse or auto-generated masks.

## Strengths

- **Novel theoretical identification of a structural limitation in HiResCAM.** Theorem 3.2 proves that HiResCAM explanations are not uniquely determined — an arbitrary matrix $M$ can be added to all class CAMs without changing softmax probabilities. This is a clean, previously unremarked observation grounded in the well-known shift-invariance of softmax, and the authors provide a concrete construction (Figure 1, Eqs. 5–6).

- **ContrastiveCAM provably removes the ambiguity and enables fine-grained class-versus-class explanations.** Definitions 3.3–3.4 define a contrastive difference that cancels $M$, and Theorem 3.5 proves invariance. Figure 2 concretely demonstrates that class-versus-class comparisons reveal contributing regions hidden in standard HiResCAM visualizations (e.g., environmental cues for "dog sled" images), providing genuinely more granular interpretability.

- **CFCE yields strong, multi-metric alignment improvements on Hard-ImageNet.** Table 2 shows that CFCE reduces Gray BBOX accuracy from 72.49% → 31.66% (demonstrating reliance has shifted to core regions), raises ContrastiveCAM IoU from 30.27% → 89.22%, and improves RFS from −0.23 → 0.224. The paper also reports GradCAM IoU (a different attribution method) to avoid fully circular evaluation, with CFCE+KL reaching 51.52%.

- **The method is robust to mask quality.** Table 3 on Oxford-IIIT Pets shows that CFCE trained with SAM-generated masks or bounding boxes still achieves competitive core-region IoU (e.g., 85.26% multiclass IoU with SAM masks), demonstrating practical deployability when pixel-accurate masks are unavailable.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Hyperparameters $\lambda_1, \lambda_2, \lambda_3$ in Eq. (18) are not reported in the main text**, nor is the tuning procedure described. These terms control the strength and shape of the KL regularization and directly affect the reported IoU values. Without them, reproducing the CFCE+KL results is not possible from the main text alone. (They may appear in the stripped appendix, but the main text should be self-contained for key experimental parameters.)

- **The IoU binarization procedure is never specified.** IoU between a continuous CAM heatmap and a binary mask requires a thresholding step, but the paper does not state how CAM values are converted to binary masks. This is essential for both reproducibility and for interpreting whether the very high ContrastiveCAM IoU values (93%+) are partly an artifact of favorable threshold choice.

- **The "Core," "Non-Core," and "Core/Total" metrics in Table 1 lack precise formulas.** The caption says "average contributions of core / non-core regions" but the reader must guess whether these are sums of absolute CAM values, squared values, or means over spatial positions. Providing an explicit definition would eliminate ambiguity.

- **CFBCE is used in the PASCAL VOC experiments without formal definition.** Section 5.3 reports results for "CFBCE" and "CFBCE + KL" in a multilabel setting, but the paper never defines how CFCE is adapted for multilabel classification. The reader must infer this from context. (Appendix B is mentioned for "adaptations of core-focused optimization" but is stripped.)

- **Comparisons to prior alignment methods (CORM, DFR) are limited to Hard-ImageNet.** On Oxford-IIIT Pets and PASCAL VOC, the only baselines are standard CE and CE with architectural modifications. While CORM and DFR were introduced in the Hard-ImageNet context, demonstrating how CFCE fares against them on additional datasets would strengthen the generality claim.

- **Theorem 4.6 (classification calibration of CFCE) is stated without proof in the main text.** The proof is deferred to the stripped appendix. The calibration guarantee is an important theoretical selling point of CFCE, so the reader of the main text cannot fully assess its validity without trusting the appendix.

- **Computational cost of CFCE for many classes is not discussed.** Eq. (15) sums over all $C$ classes, requiring computation of $\text{CAM}_{(c_t,c)}^{\text{Cntrst}}$ for each $c$. On Hard-ImageNet ($C \approx 200$) this is non-trivial. The paper does not mention how this is handled in practice (e.g., whether all classes are used or a sampling strategy is employed). Adaptations may be in the stripped Appendix B, but the main text should at minimum acknowledge the scaling concern.

- **The ContrastiveCAM IoU metric is partially circular when KL regularization is used.** The KL term in Eq. (18) explicitly encourages ContrastiveCAMs to match the shape of the mask $H$, so the high ContrastiveCAM IoU for CFCE+KL (93.39%) is partly a direct consequence of the regularization rather than purely evidence of shifted model reliance. The paper mitigates this by also reporting GradCAM IoU, but a brief discussion of this circularity and its limits would improve transparency. (CFCE *without* KL still achieves 89.22% ContrastiveCAM IoU, so the effect is not solely due to the KL term.)

### Trivial

- The framing of HiResCAM's limitation could be more precise: the $M$-shift means that *different model parameterizations* can produce the same predictions with different CAMs, which is an identifiability concern rather than evidence that the CAM of any *single trained model* is misleading. The current wording ("fail to guarantee a faithful interpretation") is slightly overstated.

## Nice-to-Haves

- An ablation isolating the effect of the KL divergence term on downstream metrics beyond what is already shown (CFCE vs. CFCE+KL rows in the tables) — e.g., whether KL purely boosts IoU or also improves causal reliance as measured by the ablation suite.
- A brief discussion of the trade-off between clean (unablated) accuracy and alignment on Hard-ImageNet (CFCE loses ~4 points of unablated accuracy) and whether mixing with standard CE can recover some of that gap.
- Adding CORM and DFR comparisons on Oxford-IIIT Pets and PASCAL VOC to demonstrate general superiority over prior feature-alignment methods.

## Removed Points

These points were flagged for removal; treat them with caution.

- **Harsh Critic claim that comparisons to CORM/DFR are missing on all secondary datasets and that this "limits the generality of the claimed superiority."** Kept in weakened form as Minor: the absence is real but CORM and DFR are Hard-ImageNet-specific methods; their absence on other datasets is a limitation but not a fatal gap.

- **Harsh Critic claim that error bars are missing for CORM, DFR, and CORM+DFR baselines.** The paper states those baseline numbers come from prior work (Singla et al. 2022, Krichenko et al. 2022), and re-running them may not be feasible. This is standard practice. Removed.

- **Harsh Critic claim that the drop in GradCAM IoU for "CE w/ Arch" vs. vanilla CE (16.25 vs. 18.44) "could indicate an interaction between architectural changes and interpretability methods that deserves discussion."** This is a tiny numerical difference within error bars and does not warrant discussion. Removed.

- **Harsh Critic claim that "the severity of the original [HiResCAM] limitation should be discussed more precisely."** Kept as Trivial (wording refinement), not a substantive weakness.

- **Harsh Critic claim that the paper "relies on self-consistent metrics for alignment" and that the circularity is not discussed.** The paper *does* report GradCAM IoU (a different method) and the ablation suite (a causal measure), partially mitigating circularity. Kept as Minor with this nuance added.

- **Harsh Critic claim about non-differentiability of absolute values in Eq. (15).** Modern autodiff frameworks handle subgradients at zero without issue; this is not a practical concern. Removed.

- **Strength Finder claim about "practical effectiveness with coarse or auto-generated masks" being a supporting strength.** Kept as a strength — the evidence in Table 3 is concrete.

- **Strength Finder generic claim about the paper "establishing a connection between interpretability and feature alignment."** This is too generic to be a standalone strength; merged into the summary.

## Novel Insights

Beyond the paper's own contributions, the reviews converge on an interesting observation: the paper demonstrates that an interpretability tool (ContrastiveCAM) derived for *post-hoc* explanation can be repurposed as a training signal that meaningfully changes *what the model learns*, not just how we inspect it. The CFCE loss is unusual in directly injecting a CAM-derived quantity into the optimization objective, and the calibration theorem (4.6) provides a formal bridge between the interpretability guarantee and training consistency. This two-way connection — interpretability informing training, not just the reverse — is underexplored and could motivate future work on loss functions grounded in explanation correctness.

## Suggestions

- Report $\lambda_1, \lambda_2, \lambda_3$ values and their selection procedure (grid search ranges, tuning criterion) in the main text or a prominent table.
- Specify the IoU binarization method (e.g., "CAM values thresholded at the mean plus one standard deviation," or percentile-based thresholding).
- Define the "Core" and "Non-Core" metrics in Table 1 with explicit formulas (e.g., $\sum H \odot |\text{CAM}^{\text{Cntrst}}|$ and $\sum (1-H) \odot |\text{CAM}^{\text{Cntrst}}|$).
- Formally define CFBCE (the multilabel adaptation) in the main text or explicitly reference the relevant appendix section.
- Add a brief sentence acknowledging the partial circularity of ContrastiveCAM IoU under KL regularization and noting that GradCAM IoU and the ablation suite provide independent verification.

## Score and Decision

**Bracket determination.** Round-1 bracketing placed the paper between ~5.5 and ~7.0: above weak anchors like "Patch Ranking Map" (2.50) and "COMiX" (3.25), and below strong anchors like "Unlearning-based Neural Interpretations" (8.00). Round-2 narrowing retrieved "Model guidance via explanations" (5.50, Rejected), "Boosting CLIP interpretability via AFT" (6.80, Accepted), and "How to Probe" (6.25, Accepted). The paper is clearly stronger than the 5.50 anchor (which suffered from poor presentation and limited comparison) and comparable to "How to Probe" (6.25), which shares the pattern of a solid methodological finding with some evaluation gaps. It sits slightly below "Boosting CLIP via AFT" (6.80), which had broader evaluation coverage and cleaner theoretical exposition in the main text.

**Anchor comparison:**
- `3b8cCgMO5ix` ("Model guidance via explanations", 5.50, Round 2): Our paper has stronger theory, better presentation, and more rigorous benchmarks. Clearly better.
- `khuIvzxPRp` ("Boosting CLIP via AFT", 6.80, Round 2): Broader evaluation, cleaner theoretical framing, slightly higher presentation quality. Our paper is slightly weaker.
- `57NfyYxh5f` ("How to Probe", 6.25, Round 2): Comparable quality — both have solid findings with some evaluation limitations. Our paper has a stronger theoretical component.
- `g6Qc3p7JH5` ("Feature Monosemanticity", 5.80, Round 1): Our paper has more direct measurement of its claims. Comparable or slightly better.
- `Tj3xLVuE9f` ("Shortcut Learning Foundations", 6.80, Round 1): Stronger theoretical foundations and cleaner experimental design. Our paper is slightly weaker but addresses a more applied problem.

**Final score:** 6.0. The paper makes genuine theoretical and empirical contributions with strong primary results. The weaknesses are all minor and addressable in rebuttal (missing hyperparameters, metric definitions, a few missing details). The score reflects the paper being clearly above the middle but not at the level of the strongest interpretability papers at the venue due to incomplete experimental reporting.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>