- Decision: Accept
- Avg Score: 6.25
- Scores: 3, 6, 8, 8
Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

This paper proposes Robust Representation Consistency Model (rRCM), a method for certified robustness via randomized smoothing. The key idea is to pre-train a classifier with a contrastive objective that aligns representations of temporally adjacent points along diffusion trajectories, then fine-tune with supervised consistency regularization. This enables implicit denoising-and-classification in a single forward pass at inference time, avoiding the separate purification stage and classifier of prior diffusion-based methods. Experiments on ImageNet and CIFAR-10 show improved certified accuracy over baselines, particularly at larger perturbation radii, with reported inference speedups.

---

## Strengths

**1. Unified one-step denoising-and-classification with measured latency reduction.**  
The paper reformulates the generative denoising objective into a discriminative task, enabling the model to predict class labels from noisy inputs in a single forward pass. Table 1 shows rRCM-B-Deep achieves per-sample certification latency of 53 s (100k noises), while diffusion-based DensePure requires up to 52 min 20 s for comparable radii — a substantial reduction. The raw latency numbers are provided for reader verification.

**2. Controlled comparison on ImageNet shows clear gains over diffusion-based methods.**  
On ImageNet, the paper reimplements DDS (Carlini et al., 2022), DensePure, and DiffSmooth all using the same ViT-based classifier (81.35% ImageNet validation accuracy), controlling for architecture. Table 1 shows rRCM-B-Deep reaching 61.9% at r=0.5 and 24.0% at r=1.5, compared to DDS at 48.1% and 12.0% respectively — a 5.3% average improvement and up to 11.6% at larger radii claimed. This controlled setup gives credibility to the ImageNet results.

**3. Strong scalability with model size and training budget.**  
Section 4.3 demonstrates that certified accuracy improves monotonically when scaling from rRCM-S to rRCM-B to rRCM-B-Deep (Figure 3) and when increasing batch size (Figure 4). This scalability suggests the method can further benefit from additional compute — a property not demonstrated for most competing diffusion-based smoothing approaches.

---

## Weaknesses

### Fatal
None.

### Major

**1. Architecture confound on CIFAR-10 comparisons.**  
On CIFAR-10 (Table 2), the paper compares rRCM-B (ViT backbone) against DDS (Carlini et al., 2022) without reimplementing DDS to use ViT. The paper explicitly describes reimplementing DDS with ViT for ImageNet (line 164: "we reimplement DDS... with a ViT-based classifier") but no such controlled reimplementation is mentioned for CIFAR-10 — the CIFAR-10 DDS results are taken from the original paper (likely using ResNet). The up-to-6.4% improvement over DDS on CIFAR-10 may be partially or fully driven by the stronger ViT architecture rather than the proposed training method. This undermines the claim that the method generalizes across datasets.

**2. No ablation of the pre-training components.**  
The method has a two-stage pipeline: (a) contrastive pre-training along diffusion trajectories, followed by (b) supervised fine-tuning with consistency regularization. The paper provides no ablation isolating the contribution of each component:
- How much gain comes from the specific trajectory-alignment pre-training versus just supervised fine-tuning of a strong self-supervised ViT (e.g., DINO, MoCo-v3)?
- What is the effect of the consistency loss term versus the contrastive loss term during pre-training?
- The paper mentions (line 133) that "training a ViT model from scratch with this objective proved challenging" but provides no quantitative evidence.  

Without ablation, it is unclear whether the pre-training objective is actually responsible for the gains or whether any strong ViT pre-training would suffice.

### Minor

**1. Imprecise inference cost claim.**  
The abstract states "reducing inference costs by 85x on average," but this figure is not clearly defined. Against the fastest diffusion baseline (DDS, 2 min 40 s), the speedup is ~3× (160 s → 53 s). The 85× figure appears to be driven by comparing against the most expensive variants (DensePure at 52+ min yields ~59×). While the raw numbers are provided in Table 1 for independent assessment, the abstract claim lacks transparency about which baselines are being averaged and should be qualified.

**2. No confidence intervals or variance estimates.**  
Certified accuracy is reported on only 500 images without any uncertainty quantification (confidence intervals, standard errors, or variance across seeds). For a comparison involving point estimates on a small sample, this weakens the statistical support for the claimed improvements.

**3. Gap between PF ODE theoretical framing and implementation.**  
The method is motivated throughout Sections 1 and 3.1 by aligning points along "deterministic PF ODE trajectories." However, the actual training pairs are constructed using the forward SDE with shared noise, approximated via Tweedie's formula (line 111). The paper acknowledges this approximation but does not reconcile the theoretical framing with the implementation. The forward SDE pairs and PF ODE steps differ unless the score is known exactly. This leaves a disconnect between the conceptual motivation and what is actually optimized.

### Trivial
None.

---

## Nice-to-Haves

- **Controlled CIFAR-10 baseline:** Reimplement DDS with ViT on CIFAR-10, or train rRCM with a ResNet backbone, to isolate the method's contribution from architecture effects.
- **Ablation study:** Compare full rRCM against (a) fine-tuning from scratch with consistency loss, (b) pre-training with only the contrastive loss, (c) standard self-supervised pre-training (e.g., MoCo-v3) + same fine-tuning.
- **Confidence intervals:** Report 95% binomial confidence intervals or standard errors on certified accuracy.
- **Clarify whether separate models are trained per noise level σ**, or if a single σ-conditional model is used, and the practical implications for deployment.

---

## Removed Points

*These points were flagged for removal by the filtering rules. Treat them with caution.*

- **Harsh Critic Issue 4 (full framing):** "Motivation misaligned with implementation" — The paper explicitly acknowledges the score is unknown (line 111) and describes the Tweedie approximation. This is a standard practice in consistency models (Song et al., 2023). The remaining gap (forward SDE vs. PF ODE) is kept as a Minor weakness above, but the harsh critic's framing as a critical/fatal issue is removed as overblown.

- **Harsh Critic Issue 5 sub-point:** "On ImageNet, only DDS is controlled" — Factually incorrect. The paper states (line 164–166) that DDS, DensePure, and DiffSmooth are ALL reimplemented with the same ViT-based classifier on ImageNet. This sub-point is removed.

- **Harsh Critic Issue 5 sub-point:** "Classical methods use different backbones" — The paper does not claim architecture-controlled comparison against classical methods (SmoothAdv, MACER). The classical methods results are taken from their respective papers (standard ResNet-based), and the comparison is informative but not architecture-controlled. This is neither a flaw nor a surprise; removed.

- **"Strengthening the Paper on Its Own Terms" items:** These are constructive suggestions, not weaknesses. Moved to Nice-to-Haves above.

- **Strength Finder general framing** about "structured noise schedule for robustness" conflicting with Harsh Critic's novelty calibration — The noise schedule novelty is a legitimate claim supported by the paper's method; the calibration is noted but does not invalidate the strength.

---

## Novel Insights

The reviewers' main genuine insight beyond the paper's own claims is that the two-dataset evaluation strategy is inconsistent: the ImageNet experiments use a carefully controlled comparison (same ViT backbone for all diffusion baselines), which is rigorous, while the CIFAR-10 experiments do not, making it impossible to tell whether the method or the architecture drives the reported gains. A secondary insight is that the 85× inference reduction claim, while attention-grabbing, is an average that masks a more modest 3× improvement against the most relevant baseline (DDS), and the paper would benefit from more transparent reporting.

---

## Suggestions

1. **Replicate the controlled comparison on CIFAR-10** — either reimplement DDS with ViT on CIFAR-10 or train rRCM with a ResNet backbone.
2. **Add an ablation study** isolating the pre-training stage, e.g., comparing full rRCM against (i) no pre-training, (ii) standard contrastive pre-training (MoCo-v3), (iii) pre-training with only the consistency or only the contrastive loss.
3. **Clarify the "85×" computation** in the abstract, or replace it with a range (e.g., "3–60× depending on the baseline") and explicitly state which variants are being compared.
4. **Add confidence intervals** to the certified accuracy results on the 500-image subset.

---
