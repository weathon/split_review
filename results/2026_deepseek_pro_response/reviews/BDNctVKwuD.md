Now I have a good read on the anchors. Let me finalize.

**Round 1 bracket:** 5.5–6.5 based on comparison with Shortcut Learning Foundations (6.80, stronger theory), SEBRA (5.75, weaker empirical validation), and How to Probe (6.25, similar contribution level).

**Round 2 narrowing:** The paper is comparable to INTR (6.00, similar contribution level with clearer idea but weaker evaluation) and slightly below EvA (6.50, cleaner method with stronger benchmarks). This narrows to **5.5–6.0**.

**Final score: 6.0.** The paper has genuine empirical contributions (dramatic core-region ablation results, approximate mask practicality, downstream transfer benefits) and a coherent method. The theoretical motivation has weaknesses (M-shift practical significance not established) and presentation gaps exist (accuracy trade-off undiscussed, missing standard faithfulness metrics), but these don't invalidate the core contribution. This places it at the INTR level — clear idea, real results, some limitations — which is solid accept territory.

---

## Summary
This paper identifies a theoretical limitation of HiResCAM explanations — they are not uniquely determined due to softmax invariance, admitting arbitrary additive spatial shifts — and proposes ContrastiveCAMs (pairwise class differences) that are provably invariant to this shift. The authors then leverage ContrastiveCAMs to decompose cross-entropy into core and non-core region contributions and design Core-Focused Cross-Entropy (CFCE), which penalizes reliance on non-core regions. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC demonstrate that CFCE-trained ResNet-50 models shift predictive reliance dramatically toward core image regions, with strong performance even when using approximate masks (SAM, bounding boxes).

## Strengths
- **Convincing empirical demonstration of core-region reliance shift (Table 2):** On Hard-ImageNet, CFCE-trained models drop to 31.7–41.8% accuracy under core-region ablation (gray mask, bounding box, tile), compared to 63–76% for all baselines. Relative Foreground Sensitivity improves from −0.18 to +0.224. ContrastiveCAM IoU against core masks reaches 89–93%. These metrics collectively provide strong, multi-faceted evidence that CFCE genuinely shifts model dependence to core regions.
- **Practicality with approximate masks (Section 5.2):** CFCE trained with auto-generated SAM masks or bounding-box supervision achieves competitive IoU (79–85%) versus ground-truth masks (83–93%) on Oxford-IIIT Pets. This substantially lowers the barrier to adoption by showing that expensive pixel-level annotations are not required.
- **Clean logical chain from interpretability to training objective:** The paper builds a coherent progression: (a) identify HiResCAM non-uniqueness → (b) propose M-invariant ContrastiveCAMs → (c) use them to decompose cross-entropy into core/non-core regions (Proposition 4.2) → (d) modify the loss to penalize non-core contributions (CFCE). Each step is theoretically motivated.
- **Downstream segmentation transfer (Section 5.3, Figure 4):** CFCE-trained backbones consistently outperform CE-trained backbones when fine-tuned or trained end-to-end for segmentation on PASCAL VOC. This demonstrates that the feature alignment induced by CFCE produces better representations that transfer beyond classification, not merely a classification artifact.
- **Class-versus-class explanations reveal hidden spurious reliance (Figure 2):** The pairwise ContrastiveCAM visualizations expose that different class comparisons attend to different image regions, and that HiResCAMs can conceal non-core contributions. This empirically motivates why per-class explanations are insufficient.

## Weaknesses

### Fatal
None.

### Major
- **The M-shift argument's practical significance is not directly established, yet it serves as the paper's central motivation.** Theorem 3.2 proves that HiResCAMs admit an arbitrary additive matrix M shared across all classes. But the paper never demonstrates that this M-shift actually corrupts HiResCAM explanations in trained models. Figure 1 is a constructed schematic, not an empirical observation. The redundancy ratio γ in Table 1 measures ‖−mean(CAM_c)‖ / ‖CAM_{c_t}‖, which quantifies how far the mean CAM deviates from zero — this is a specific computed quantity, not a measurement of the arbitrary M from Theorem 3.2. The paper treats γ as if it estimates the problematic M, which is unjustified. This weakens the narrative coherence, though it does not invalidate the method (ContrastiveCAMs and CFCE would work regardless of this motivation).

### Minor
- **IoU evaluation is partly circular for the KL-regularized variant.** The RCFCE loss (Definition 4.7) includes a KL divergence term that explicitly encourages ContrastiveCAMs to match the shape of the core mask H. Consequently, the high ContrastiveCAM IoU scores (93.39%) for CFCE+KL are partly an artifact of the training objective. The paper does report CFCE without KL achieving 89.22% IoU, which mitigates this concern, but the conflation of circular and independent evidence somewhat overstates the case.
- **Substantial accuracy cost on Hard-ImageNet is not analyzed.** CFCE drops un-ablated accuracy from 94.25% (CE) to 90.53%, a loss of nearly 4 percentage points. The paper acknowledges this only briefly as "at the cost of some un-ablated performance" without discussing when this trade-off is acceptable, whether it can be tuned via λ₁, or what it implies for practical deployment.
- **The absolute value operation in CFCE is not justified.** Equation (15) penalizes non-core contributions via +Σ(1−H)⊙|CAM^{Cntrst}|, which means negative non-core contributions — which could help suppress competing class probabilities — are also penalized. This is a non-obvious design choice that the paper never discusses or ablates.
- **Terminology conflation: "faithfulness" vs. alignment with human annotations.** The abstract claims ContrastiveCAM provides "more faithful attention maps," but the primary evaluation metric is IoU against human-annotated core masks, which measures alignment with human expectations rather than standard faithfulness (deletion curves, insertion curves, pointing game). The core-region ablation tests and RFS do provide indirect evidence about model reliance, but the paper should distinguish these concepts.
- **CE w/ Arch baseline shows puzzling IoU degradation on Pets that goes unremarked.** On Oxford-IIIT Pets, vanilla CE achieves 78.37% train IoU while CE w/ Arch drops to 38.58%. This severe degradation from architectural modifications alone is never discussed, yet it affects interpretation of subsequent CFCE improvements.
- **Pareto improvement claim is ambiguous.** On PASCAL VOC, CFBCE achieves higher IoU but slightly lower AP than CE w/ Arch (88.39% vs. 88.85%). The paper should specify which baseline the Pareto claim references.
- **Discussion section lacks limitations.** The discussion is a single paragraph restating contributions without addressing the accuracy trade-off, computational cost of computing ContrastiveCAMs during training, reliance on mask annotations, or any failure modes.

### Trivial
- Table 1 reports single values without error bars, while Tables 2–4 report ± intervals. This inconsistency should be addressed.
- The theoretical framing of HiResCAM non-uniqueness, while mathematically correct, derives from the elementary softmax property σ(x) = σ(x + a·1). The extension to spatial matrices is a valid observation about HiResCAM specifically, but the paper's presentation could be more measured about the depth of this finding.

## Nice-to-Haves
- Standard faithfulness metrics (deletion/insertion curves) comparing ContrastiveCAMs against HiResCAMs and GradCAMs on CE-trained models would strengthen the claim that ContrastiveCAMs are better explanations, independent of CFCE training.
- An ablation study varying λ₁ to characterize the accuracy-alignment trade-off curve would help practitioners decide when to adopt CFCE.
- The multilabel adaptation CFBCE should be briefly described in the main text rather than solely deferred to Appendix B.
- A brief description of the "CE w/ Arch" modifications in the main text would improve self-containedness.

## Removed Points
These points are flagged as removed. Treat them with caution.

- **"Key methodological content absent from main text" (Harsh Critic):** The paper explicitly states that architectural modifications are in Appendix C, multilabel adaptations in Appendix B, and proofs in Appendix A. These appendices exist in the original submission; their absence is a parser artifact, not an author error.
- **"Equation (44) not present" (Harsh Critic):** Equation (44) is in Appendix A (stripped by parser). Not an author error.
- **"ContrastiveCAMs are a trivial derivation and the paper overstates their contribution" (Harsh Critic):** The pairwise difference formulation is mathematically simple, but simplicity is not a weakness. The value is in the insight that pairwise differences are M-invariant and provide granular class-vs-class explanations.
- **"The HiResCAM non-uniqueness follows directly from the softmax property taught in introductory ML courses" (Harsh Critic):** While the scalar invariance is elementary, the extension to a spatial matrix M that affects HiResCAM explanations is a non-trivial observation about CAM methods specifically. The paper identifies a previously undiscussed practical consequence, not claiming to discover softmax invariance.
- **"CE baseline does not report ContrastiveCAM IoU" (Harsh Critic):** The paper explains that IoU was computed using GradCAMs for consistency with baselines, as GradCAMs have known limitations. This is a reasonable methodological choice.
- **"CE w/ Arch sometimes performs worse than vanilla CE" (Harsh Critic, framed as a weakness about unfair comparison):** The asymmetry favors the baseline, not the authors' method. This is intentionally conservative experimental design.
- **"Any explanation method that explains logits rather than probabilities would face the same underdetermination" (Harsh Critic):** True but the paper is specifically about HiResCAM. The paper doesn't claim uniqueness of this limitation.
- **"Theoretical analysis using NTK is problematic" / various speculative claims about missing content:** These are not verifiable from the paper and represent speculation, not identified problems.

## Novel Insights
The paper's most genuinely novel contribution is the decomposition of cross-entropy loss into core and non-core region contributions via ContrastiveCAMs (Proposition 4.2), which provides a clean theoretical basis for why standard CE training can lead to feature misalignment. This connects interpretability formalism directly to training objective design in a way that is more principled than prior ad-hoc regularization approaches. The demonstration that CFCE-trained backbones transfer better to downstream segmentation suggests that the alignment benefits reflect genuinely improved feature representations rather than a mere classification artifact.

## Suggestions
- Reframe the motivation around Proposition 4.2 (the core/non-core decomposition of CE) rather than the M-shift argument. This would strengthen the paper by making the theoretical contribution — the decomposition — the central motivation rather than a fix to an unverified problem.
- Add an analysis of the accuracy-alignment trade-off as a function of λ₁ on at least one dataset, to help practitioners understand the operating envelope.
- Distinguish clearly between "alignment with core regions" (IoU-based) and "faithfulness" (standard XAI metrics), and either add deletion/insertion curves or soften the faithfulness claims.
- Discuss the absolute value choice in Eq. (15) and ideally include an ablation comparing absolute value vs. alternative penalization schemes.

## Calibration Anchor Comparisons

| Anchor Paper | Score | Round | Comparison |
|---|---|---|---|
| Conceptualize Any Network (CAN) | 3.00 | R1 | Our paper has dramatically stronger empirical validation and a clearer contribution. |
| Counterfactual Image Generation | 2.50 | R1 | Not directly comparable; our paper is substantially more rigorous. |
| Patch Ranking Map | 2.50 | R1 | Our paper has a more principled method and stronger results. |
| COMiX | 3.25 | R1 | Our paper has better quantitative evaluation and practical impact. |
| Shortcut Learning Foundations | 6.80 | R1 | Stronger paper with deeper theoretical analysis (NTK framework) and more systematic study. Our paper is more applied with a specific training method. |
| ContraLSP | 5.75 | R1 | Different domain (time series); our paper has comparable contribution level. |
| SEBRA | 5.75 | R1 | Our paper has stronger empirical validation (more datasets, more dramatic results) and a more principled theoretical framework. |
| How to Probe | 6.25 | R1/R2 | Similar in spirit (connecting training details to interpretability). How to Probe has a simpler, cleaner finding with broader validation. Our paper has a more elaborate method but comparable impact. |
| Spawrious | 5.75 | R2 | Benchmark paper; our paper is a method paper with stronger contribution. |
| Prototypical Part Networks + RLHF | 5.75 | R2 | Similar score range; our paper has stronger and more systematic results. |
| INTR (Interpretable Transformer) | 6.00 | R2 | Comparable: INTR has a novel architecture with mostly qualitative results; our paper has a novel training objective with stronger quantitative evaluation. Roughly equal contribution level. |
| EvA | 6.50 | R2 | Stronger paper with a cleaner method (post-hoc erasure), better benchmarks, and more practical appeal. Our paper's results are more dramatic on core-region reliance but the method is less clean. |
| Mitigating Spurious Correlations in VLMs | 6.50 | R2 | Different setting (zero-shot multimodal); our paper has comparable quality but narrower scope. |

**Round 1 bracket:** 5.5–6.5
**Round 2 narrowing:** 5.5–6.0, anchored by INTR (6.00) as the closest comparable and EvA (6.50) as clearly stronger.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>