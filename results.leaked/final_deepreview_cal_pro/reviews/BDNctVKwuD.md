Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper identifies a theoretical limitation of HiResCAM: because softmax is invariant to uniform logit shifts, HiResCAM explanations are only determined up to an arbitrary class-common matrix \(M\). The authors propose ContrastiveCAM, a pairwise-difference explanation that is invariant to \(M\) and provides class-versus-class granularity. Using ContrastiveCAM, they observe that standard cross-entropy training produces reliance on spurious non-core regions. To address this, they derive Core-Focused Cross-Entropy (CFCE), a loss that penalizes non-core contributions while preserving classification calibration. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC demonstrate improved feature alignment, including dramatic core-ablation improvements on Hard-ImageNet.

## Strengths

- **Rigorous theoretical foundation for the proposed method.** Theorem 3.2 proves the \(M\)-invariance of HiResCAM under softmax; Theorem 3.5 proves ContrastiveCAM is invariant to \(M\); Proposition 4.1 expresses softmax probabilities directly via ContrastiveCAM; and Theorem 4.6 establishes that CFCE is classification-calibrated for the core-constrained risk minimization objective. This chain of theoretical results cleanly motivates and justifies the method.

- **Compelling independent evidence from core-ablation on Hard-ImageNet.** The core-ablation results (Table 2) are the strongest evidence in the paper: CFCE drops gray-mask accuracy from 75.94% (standard CE) to 41.78%, and CFCE+KL drops it to 45.49%, while RFS flips from negative (−0.18) to strongly positive (+0.224–0.236). These metrics do not train on the mask signal that the KL term uses, so they provide an independent, non-circular validation that the model genuinely shifts its reliance to core regions.

- **Practical robustness to imperfect masks.** Table 3 shows that CFCE trained with SAM-generated masks or bounding-box annotations achieves competitive IoU (e.g., 83.46%/83.54% for SAM on binary Oxford Pets), demonstrating that the method does not require costly pixel-perfect ground-truth annotations.

- **Downstream transfer benefit.** Figure 4 shows that backbones initialized from CFCE+KL-trained models consistently outperform CE-trained backbones on PASCAL VOC semantic segmentation, indicating the learned representations are better aligned with object structure beyond the classification task.

## Weaknesses

### Fatal

None.

### Major

- **IoU evaluation is partially circular for the KL-regularized variant.** Equation 18 includes a KL-divergence term that explicitly encourages the ContrastiveCAM to match the shape of the core mask \(H\). Reporting IoU between the resulting CAM and \(H\) as evidence of improved alignment is therefore confounded — the model is directly rewarded for producing attention maps that resemble the mask. This concern is mitigated on Hard-ImageNet, where independent core-ablation metrics (gray-mask accuracy, RFS) corroborate the IoU gains. For Oxford Pets (Table 3) and PASCAL VOC (Table 4), however, IoU is the sole alignment metric reported, leaving the claim that the model genuinely relies on core features less fully substantiated for those datasets. The non-KL variant (CFCE without regularization) does show improvements over standard CE on these datasets (e.g., Oxford Pets binary IoU 82.92% vs. CE 78.37%), partially addressing this concern.

- **Architectural modifications are not isolated, complicating attribution of gains.** The paper uses interpretability-motivated architectural modifications for CFCE variants and provides a "CE w/ Arch" baseline. On Oxford Pets, CE w/ Arch dramatically degrades IoU relative to standard CE (39.07% vs. 78.37%), indicating these architectural changes have a large effect. While CFCE (82.92%) still outperforms standard CE (78.37%), the paper does not ablate whether the gains come from the loss, the architecture, or their interaction. Including CFCE results on the standard (unmodified) architecture, or a clear ablation isolating the architecture's effect, would strengthen confidence in the loss function's contribution.

### Minor

- **Accuracy trade-off is acknowledged but not analyzed.** CFCE drops clean accuracy by ~3–4% on Hard-ImageNet and ~1.5% on Oxford Pets multiclass. The paper notes this cost but provides no analysis of *why* accuracy degrades — e.g., whether ground-truth core masks are imperfect for some examples, or whether non-core context genuinely carries class-relevant information in certain cases. This analysis would help practitioners assess when the method can be safely applied.

- **The theoretical framing of HiResCAM's limitation is somewhat overstated.** Theorem 3.2 shows that HiResCAMs shifted by a class-common \(M\) yield identical softmax probabilities. The paper describes this as HiResCAM "failing to guarantee a faithful interpretation." HiResCAM was designed to explain logits, which are uniquely determined by the model's weights and input; the \(M\)-shift represents a non-discriminative baseline removed by softmax. The mathematical observation is correct, but framing it as an inherent unreliability of HiResCAM rather than as the removal of a non-discriminative component weakens the paper's rhetorical precision.

- **No ablation of CFCE against simpler alternatives.** The paper does not compare CFCE against simpler regularization strategies (e.g., directly penalizing non-core activations from HiResCAM without the pairwise contrastive structure, or standard attention-mask regularization). Such comparisons would clarify what the ContrastiveCAM formulation specifically adds beyond a generic mask-guided penalty.

### Trivial

- The paper does not specify the number of training runs for experiments that lack standard deviations (e.g., the standard CE, CORM, DFR baselines in Table 2), though this is a minor clarity issue.

## Nice-to-Haves

- Replace IoU with core-ablation metrics on Oxford Pets and PASCAL VOC to provide an independent, non-circular measure of core reliance for those datasets.
- Analyze the accuracy drop by categorizing examples where CFCE degrades performance, to characterize when the trade-off is acceptable.
- Clarify the computational implementation of the loss (e.g., whether stop-gradient or second-order derivatives are needed for CAM-based terms) to aid reproducibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Harsh Critic claim: "Baseline configuration hides the true effect" / CFCE only recovers from self-inflicted degradation.** REMOVED as overstated. CFCE outperforms standard CE on most metrics: Hard-ImageNet core-ablation drops from 75.94% (CE) to 41.78% (CFCE); Oxford Pets binary IoU rises from 78.37% (CE) to 82.92% (CFCE). The improvement over standard CE is genuine and visible in the tables. The architectural-isolation issue is retained as a Major weakness in more measured form.

2. **Harsh Critic claim: "CE w/ Arch baseline is not as prone to spurious reliance as original CE."** REMOVED as factually incorrect. Table 2 shows CE w/Arch has *higher* gray-mask accuracy (76.53%) than standard CE (75.94%), meaning it relies *slightly more* — not less — on non-core features. The difference is negligible in either direction.

3. **Harsh Critic claim: "Missing Parts — second-order derivatives / stop-gradient implementation."** Moved to Nice-to-Haves. This is a reproducibility detail, not a weakness that affects the paper's contribution claims.

4. **Harsh Critic claim about statistical significance not being established.** DEMOTED to Trivial. Standard deviations are reported for the authors' methods; formal hypothesis tests are not standard practice for this type of benchmark evaluation.

5. **Strength Finder claim: "Convincing experimental validation that CFCE improves feature alignment" with emphasis on CFCE+KL IoU numbers.** MODIFIED. The KL IoU gains are partially circular; the review emphasizes the independent core-ablation evidence instead.

## Novel Insights

The paper's most genuinely novel contribution is the algebraic connection between CAM explanations and softmax probabilities formalized in Proposition 4.1, which expresses class probabilities as a direct function of pairwise ContrastiveCAMs. This identity enables the precise dissection of cross-entropy into core and non-core components (Proposition 4.2) and directly motivates the CFCE loss. The observation that cross-entropy does not inherently favor core over non-core regions — and that this creates a theoretical basis for feature misalignment in convnets — is a crisp and useful formalization beyond the paper's own method.

## Suggestions

- For Oxford Pets and PASCAL VOC, run core-ablation experiments (analogous to Hard-ImageNet Table 2) to provide independent validation of core reliance, circumventing the circularity concern with the KL variant's IoU.
- Add an ablation that trains CFCE on the standard (unmodified) ResNet-50 architecture, or at minimum, ablate the individual architectural modifications to isolate their contribution from the loss function's effect.
- Reframe the HiResCAM limitation discussion to emphasize that ContrastiveCAM removes a class-common, non-discriminative baseline, rather than claiming HiResCAM is inherently unfaithful. This aligns the narrative with the actual mathematical operation and avoids a distracting debate.

## Score and Decision

**Round 1 bracket:** The paper sits above the low band (2.5–3.25, all rejected) and above the middle-low anchors (4.0–5.25). It is comparable to the 6.0 anchor (INTR, mainly qualitative) and falls in the 6.0–7.5 range.

**Round 2 narrowing:** Closest anchors are khuIvzxPRp (6.80, CLIP interpretability via AFT) and Tj3xLVuE9f (6.80, Foundations of Shortcut Learning). The paper under review has comparable or stronger theoretical content and broader experimental validation, but shares similar-level weaknesses (evaluation confounds, missing ablations). The circular-evaluation concern on two datasets and the un-isolated architectural modifications pull it slightly below the 6.80 anchors.

**Anchor comparison summary:**
| Anchor | Score | Comparison |
|---|---|---|
| BwQUo5RVun | 3.00 (R1) | Far weaker — weakly supervised grounding with Grad-CAM, limited novelty |
| GjfIZan5jN | 7.33 (R1) | Stronger — more extensive experiments across architectures, cleaner evaluation |
| bkdWThqE6q | 6.00 (R1,R2) | Weaker — mostly qualitative evaluation, less theoretical rigor |
| khuIvzxPRp | 6.80 (R2) | Comparable — similar theoretical+empirical mix, similar-level weaknesses |
| Tj3xLVuE9f | 6.80 (R2) | Comparable — strong theory but synthetic focus, this paper more applied |
| ONhLaNbxVV | 5.75 (R2) | Weaker — incremental ProtoPNet improvement, narrower scope |

**Final score: 6.5.** The paper makes a real contribution with theoretical rigor and strong independent evidence on Hard-ImageNet, but the circular evaluation for the KL variant on two datasets and the un-isolated architectural modifications prevent a higher score.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>