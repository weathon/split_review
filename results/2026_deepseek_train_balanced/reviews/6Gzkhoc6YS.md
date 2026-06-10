## Summary

This paper introduces PerSAM and PerSAM-F, two methods to personalize the Segment Anything Model (SAM) for automatically segmenting user-designated objects using only a single reference image with a mask. PerSAM is training-free and injects target semantics via a location confidence map, target-guided attention, and target-semantic prompting. PerSAM-F adds a scale-aware fine-tuning variant that learns only 2 parameters in 10 seconds to resolve mask-scale ambiguity. The paper also releases a small benchmark dataset (PerSeg, 40 objects) and demonstrates an application to DreamBooth. The core contribution — achieving strong personalized segmentation with near-zero overhead — is simple, well-motivated, and convincingly supported by the primary experiments.

## Strengths

1. **Extreme parameter efficiency with strong empirical results.** PerSAM-F achieves 95.3 mIoU on the PerSeg benchmark using only **2 learnable parameters** fine-tuned in **10 seconds** on a single A100 GPU (Table 1, lines 224–226). The ablation in Table 5 shows it substantially outperforms standard PEFT methods (Prompt Tuning: 76.5, Adapter: 78.3, LoRA: 90.0) while using orders-of-magnitude fewer parameters, demonstrating that the method genuinely avoids one-shot overfitting.

2. **Training-free variant outperforms several foundation models with zero training.** At 0 learnable parameters, PerSAM achieves 89.3 mIoU on PerSeg, surpassing Painter (56.4), Visual Prompting (65.9), and SEEM (87.1) — all of which require full model parameters (Table 1). This validates that the proposed training-free techniques (confidence map, guided attention, semantic prompting) are effective independently.

3. **High robustness to coarse one-shot input.** When the reference mask is replaced with a mere bounding box, PerSAM drops only from 89.3 to 88.1 mIoU and PerSAM-F from 95.3 to 94.9 mIoU, while competitors collapse (SegGPT drops from 94.3 to 36.0, VP from 65.9 to 38.1) (Table 6). This robustness to imprecise user input is a practically meaningful advantage not demonstrated by prior in-context segmentation methods.

4. **Comprehensive ablation isolating each component's contribution.** Table 4 traces a clear path from a positive-prior baseline (69.1 mIoU) to the full PerSAM-F (95.3), with each technique's gain cleanly quantified: negative prior (+3.4), cascaded post-refinement (+11.4), guided attention (+1.9), semantic prompting (+3.5), and scale tuning (+6.0). This provides granular, direct evidence for each design choice.

5. **Competitive video segmentation without any video-specific training.** PerSAM-F achieves 76.1 J&F on DAVIS 2017 val (Table 2), outperforming methods that include in-domain video training (AFB-URR: 74.6, AGSS: 67.4), demonstrating strong temporal generalization from a single reference image.

## Weaknesses

### Fatal
None.

### Major
1. **SegGPT comparison scores are absent from the primary comparison tables despite being the paper's main competitive baseline.** The paper claims PerSAM-F outperforms SegGPT on DAVIS 2017 "by +0.5%" (line 328) and "performs comparably" on one-shot semantic/part segmentation (line 331), yet **SegGPT's scores are not shown in Table 2 (DAVIS) or Table 3 (one-shot segmentation)**. SegGPT *is* present in Table 1 and Table 6, so the omission from Tables 2 and 3 is not a formatting constraint — it is a selective presentation choice that prevents the reader from directly verifying the numerical comparisons the paper relies on for its strongest claims against the primary competitive baseline. This is the most significant evidential gap in the paper and should be corrected.

### Minor
1. **No discussion of per-object variance or outlier influence on PerSeg.** The 1.0 mIoU gap between PerSAM-F (95.3) and SegGPT (94.3) on PerSeg is reported as a single point estimate. The per-object results in Table 1 reveal substantial variation — notably, PerSAM-F scores 97.5 on "Barn" versus SegGPT's 63.8, a difference of 33.7 points that appears to drive a large fraction of the aggregate advantage. On other objects (e.g., "Cat": 92.3 vs. 94.1), PerSAM-F is slightly lower. The paper does not discuss this variation or what makes "Barn" qualitatively different, making it difficult for the reader to assess whether the headline 1.0-point advantage is broadly representative or driven by a single outlier case.

2. **The claim that "our approach can achieve higher scores than HSNet" (line 331) is imprecise.** On FSS-1000, PerSAM-F (86.3) is actually slightly *lower* than HSNet (86.5). On the other three benchmarks (LVIS-92ⁱ, PASCAL-Part, PACO-Part) PerSAM-F is higher, making the claim partially accurate but misleading in its absolute phrasing. The paper should specify which datasets support this comparison.

3. **The balancing factor α in target-guided attention (Eq. 18) is never given a numerical value, ablated, or discussed beyond being called a "balancing factor."** This hyperparameter directly controls how strongly the location confidence map biases attention in every cross-attention layer of SAM's decoder. Its value could substantially affect behavior, and leaving it unspecified impairs reproducibility.

4. **The DreamBooth application is evaluated purely qualitatively.** Section 4.3 provides only visual examples with subjective commentary ("better visual correspondence," "higher fidelity"). No quantitative metrics (CLIP score, FID, user study, or segmentation accuracy) are provided. Since the DreamBooth literature routinely includes quantitative evaluation, and the paper presents this as a contribution (Abstract, Introduction, contribution list), the evidence is disproportionate to the claim. The authors should either add quantitative evaluation or appropriately downgrade this to a qualitative demonstration.

### Trivial
1. The claim that post-refinement "only costs an extra 2% latency" (line 212) is stated without citing a measurement or providing the absolute per-image runtime, making it unverifiable.
2. The paper does not report absolute per-image inference latency for any method, which would help contextualize the efficiency claims.

## Nice-to-Haves
- **Ablate the choice of feature encoder** for the location confidence map. The paper notes the encoder "can be SAM's frozen backbone or other pre-trained vision models" (line 148) but only evaluates SAM's encoder. An ablation comparing SAM encoder vs. DINOv2 vs. CLIP would either validate the design choice or reveal a meaningful sensitivity.
- **Add standard deviations or per-object statistics** on PerSeg (e.g., standard error across objects) to help assess whether the reported gaps are meaningful given the dataset's small size (40 objects).
- **Provide more thorough characterization of the PerSeg dataset** — annotation protocol, diversity of poses and scenes, and a discussion of limitations (objects are drawn from subject-drive diffusion training sets and may be more canonical/centered than real-world unconstrained settings).
- **For the DreamBooth application**, add quantitative evaluation (CLIP score, FID) or reframe as a qualitative demonstration rather than a contribution.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Criticism about SAM's encoder not being optimal for correspondence:** The paper acknowledges the encoder choice explicitly ("can be SAM's frozen backbone or other pre-trained vision models," line 148), so this is not an overlooked issue. Moved to Nice-to-Have as an ablation suggestion.
- **Criticism about three mask scales not being clearly defined:** The paper clearly states it "refers to SAM's original solution to output three-scale masks" (line 220), which is sufficiently specific for readers familiar with SAM. Removed.
- **Criticism about missing appendix or proofs:** The parser strips these sections; they exist in the original submission. Removed per Hard Rules.
- **Generic area-of-concern sweeps** (e.g., "could the metric be measuring a proxy?", "are confounders controlled?") without specific anchors in the paper. Removed per Filtering Discipline.
- **Strength Finder's generic/superficial strengths** (e.g., "addressed an important problem") — dropped as they lack concrete evidence specific to this paper.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective on the method that the paper itself does not provide. The most interesting synthesis from the critique is that the method's primary empirical advantage (the 1.0 mIoU gap on PerSeg) appears to be substantially influenced by a single outlier object ("Barn"), which raises a question the paper does not address but which the community should investigate when building on this work.

## Suggestions
1. **Add SegGPT scores to Tables 2 and 3.** This is the single highest-leverage change — it directly addresses the most significant evidential gap and allows readers to verify claimed comparisons.
2. **Report per-object statistics and discuss the Barn outlier.** A brief discussion of what makes Barn behave differently (is it the scale ambiguity PerSAM-F specifically addresses?) would substantially strengthen confidence in the aggregate results.
3. **Specify the value of α and either ablate it or justify the choice.** This is a simple fix that improves reproducibility.
4. **Either add quantitative metrics to the DreamBooth evaluation or reframe its role** in the paper to match the qualitative evidence provided.
5. **Report absolute per-image inference latency** for all methods to support the efficiency claims.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>