Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper makes two contributions: (1) it theoretically identifies a non-uniqueness issue in HiResCAM—the explanations are not uniquely determined because adding any common matrix M to all class CAMs leaves softmax predictions unchanged—and proposes ContrastiveCAMs (pairwise differences of HiResCAMs) that are invariant to this redundancy; (2) it leverages ContrastiveCAMs during training via a new loss, Core-Focused Cross-Entropy (CFCE), that penalizes contributions from non-core image regions, and evaluates the approach on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC with improved alignment metrics, core-ablation drops, and downstream segmentation gains.

## Strengths

1. **Theoretical identification of HiResCAM non-uniqueness (Theorem 3.2)**: The paper proves that HiResCAMs admit a spurious shift by an arbitrary matrix M while the probability prediction remains unchanged. This is a concrete, formal limitation of a widely-used interpretability method, and it directly motivates the proposed ContrastiveCAMs. The proof is clean and the observation is genuinely novel.

2. **ContrastiveCAMs are provably M-invariant (Theorem 3.5)**: A formal proof that both ContrastiveCAM and the class-reconstructed variant are invariant to the spurious shift M. This establishes a clear theoretical advantage over HiResCAM and is more than a trivial extension of the softmax invariance.

3. **Strong independent evidence from core-region ablation (Table 2)**: Under core-region ablation (Gray Mask), the accuracy drop goes from 75.94% (CE) to 41.78% (CFCE). This is an independent metric that does not rely on ContrastiveCAMs, directly demonstrating that the proposed loss genuinely shifts the model's reliance toward core regions.

4. **GradCAM IoU improvements (Table 2)**: GradCAM IoU (an explanation method *not* used in the loss) improves from 18.44% (CE) to 51.52% (CFCE+KL). This provides independent validation that the alignment gains generalize beyond ContrastiveCAMs.

5. **Practicality with approximate masks (Table 3, Section 5.2)**: CFCE with auto-generated SAM masks or bounding boxes achieves competitive alignment (e.g., 83.95% binary IoU with SAM, 79.13% with BBOX), demonstrating the method works without expensive ground-truth masks.

6. **Downstream segmentation transfer (Figure 5)**: Backbones pre-trained with CFCE+KL yield higher per-class IoU on PASCAL VOC segmentation, particularly in the end-to-end setting, providing a useful downstream validation.

7. **Theoretical analysis of cross-entropy misalignment (Proposition 4.2)**: The paper dissociates core and non-core contributions in the cross-entropy loss, formally showing that CE does not inherently penalize non-core usage—providing a principled motivation for CFCE.

## Weaknesses

### Fatal

None.

### Major

1. **Partial circularity in the ContrastiveCAM IoU metric**: The CFCE loss is explicitly defined in terms of ContrastiveCAMs and penalizes mismatch with the core mask. Therefore, the high ContrastiveCAM IoU scores (89–93% in Table 2, 85–93% in Table 3) are in significant part a direct consequence of the optimization objective—they do not independently validate that the model has *generically* learned to attend to core regions. The paper partially mitigates this by including GradCAM IoU (independent metric) and core-region ablation accuracy, and it acknowledges "IoU for this benchmark was computed using GradCAMs only for consistency with baselines." Still, the headline ContrastiveCAM IoU numbers are over-interpreted as evidence of general alignment. The paper would benefit from evaluating alignment with a third, unrelated explanation method (e.g., input perturbation or LIME) to fully break this circularity.

### Minor

1. **Limited baseline comparisons**: The paper compares against only CORM (Singla et al., 2022), DFR (Kirichenko et al., 2022), and generic cross-entropy. While these are the standard baselines for the Hard-ImageNet suite, several conceptually related alignment techniques—such as saliency map regularization (Ismail et al., 2021) and masking-based approaches (Aniraj et al., 2023)—are mentioned in the related work but not compared empirically. Adding even one representative baseline (e.g., simple feature-map masking) would increase confidence. This is an evidential limitation, not a fatal one.

2. **Accuracy–alignment trade-off acknowledged but not systematically explored**: Raw accuracy drops from 94.25% (CE) to 90.35% (CFCE+KL) on Hard-ImageNet, and from 94.41% to 90.08% on Oxford Pets multiclass. The paper mentions "at the cost of some un-ablated performance" but does not systematically analyze the Pareto frontier (e.g., by varying λ₁ and reporting both accuracy and IoU), nor does it explore whether accuracy can be recovered. This makes it difficult for readers to assess the practical cost of the alignment improvement.

3. **Hyperparameter values absent from main text**: The loss has three tunable parameters (λ₁, λ₂, λ₃ in Eq. 18), but their values are not reported—they are deferred to Appendix C (stripped by the PDF parser, a known artifact). While the original submission likely contains this information, the main text is missing a brief statement of the chosen values or the selection procedure.

4. **Theorem 4.6 proof deferred to appendix**: The proof that CFCE is classification-calibrated with respect to core-constrained risk is relegated to the appendix (stripped). Without seeing the proof, the claim is under-validated in the main text. An intuitive explanation of why the absolute-value term enforces the constraint would strengthen the presentation.

5. **Table 1 underspecified**: The "Core" and "Non-Core" contributions in Table 1 are not explicitly defined—it is unclear whether these are sums of absolute values, signed sums, or some other aggregation. This should be clarified.

6. **No dedicated limitations or failure case discussion**: The Discussion section (Section 6) is very brief and does not address when CFCE might harm performance (e.g., with inaccurate masks, tiny core regions, multi-object images). Adding a limitations paragraph would improve the paper.

### Trivial

None that warrant mention beyond what's covered above.

## Nice-to-Haves

- A Pareto curve varying λ₁ and plotting accuracy vs. ContrastiveCAM/GradCAM IoU would let readers directly assess the cost of alignment.
- An ablation comparing CFCE with different non-core penalties (absolute value vs. quadratic vs. hinge-like) would sharpen the claim that the specific design in Eq. 15 is optimal.
- Applying CFCE to a task where the natural explanation method is *not* ContrastiveCAMs (e.g., a different backbone or domain-shift robustness) would break the circularity concern more thoroughly.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic: "The main evaluation metric (ContrastiveCAM IoU) is partially circular"** — *Kept at Major tier above, but the critic overstated severity. Circularity is acknowledged by the paper (GradCAM IoU used for baselines, ContrastiveCAM IoU is supplemental). GradCAM IoU and core-ablation are genuinely independent metrics that already show strong gains.*
- **Harsh critic: "Theoretical consistency of loss function / proof in appendix"** — *Demoted from "Critical Issue" to Minor. The proof being in the appendix is a parser artifact; the theorem statement is in the main text, and empirical results support the claim. The concern about whether the absolute-value term is principled is reasonable but the paper provides empirical validation.*
- **Harsh critic: "Strengthening the Paper on Its Own Terms" suggestions** — *Moved to Nice-to-Haves. These are constructive suggestions, not weaknesses.*
- **Strength Finder: Generic/superficial strengths** — *Removed. All remaining strengths are concrete and evidence-based.*
- **Strength Finder: "Consistency of CFCE with core-constrained risk (Theorem 4.6)"** — *Kept as qualified strength. The theorem is stated and is important, though the proof is deferred.*
- **Harsh critic: "No comparison with masking features during training"** — *Moved to Nice-to-Haves. This is a reasonable suggestion but not a standard baseline for this evaluation setup.*
- **Harsh critic: "Scale-sensitivity argument not formally proven" (from Section 4.1 review)** — *Removed. The paper presents this as an empirical observation, which is appropriate for the scope.*

## Novel Insights

None beyond the paper's own contributions. The one genuinely novel observation that emerges from synthesizing the reviews is that the paper's strongest contribution (the theoretical analysis of HiResCAM non-uniqueness) is somewhat separable from its more application-oriented contribution (CFCE training). The HiResCAM non-uniqueness result could stand on its own as a methodological contribution to interpretability, while the CFCE training component addresses a different goal (feature alignment) but introduces evaluation circularity. Connecting the two—using the improved explanation method to supervise training—is a natural idea, but the evaluation would be stronger if the two contributions were validated more independently.

## Suggestions

1. Include an explicit limitations paragraph acknowledging scenarios where CFCE might underperform (inaccurate masks, tiny core regions, multi-object images).
2. Report hyperparameter values (λ₁, λ₂, λ₃) in the main text, not just the appendix.
3. Add at least one more baseline (e.g., simple feature masking or saliency regularization) to broaden the comparison.
4. Clarify the computation of "Core" and "Non-Core" contributions in Table 1.
5. Present a Pareto analysis (accuracy vs. alignment across λ₁ settings) to help readers evaluate the practical trade-off.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:**
- Weak band (score 0–3): MI-Grad-CAM (3.00, Reject), Minimalist Explanation Generation (1.50, Withdrawn), Keypoint Counting Classifiers (2.50, Withdrawn). The current paper is clearly stronger than all of these.
- Middle band (score 4–7): ClusCAM (4.67, Reject), "Now you see me!" (4.50, Withdrawn), HiCEM (6.00, Accept), "A margin-based replacement for CE" (5.00, Reject).
- Strong band (score 8+): Papers on unrelated topics (language models, rotation estimation, RL). Not comparable.

**Round 1 bracket:** [4.5, 6.5]

**Round 2 — Narrowing:**
- ClusCAM (4.67, Reject): Purely post-hoc CAM explanation method with no training component. Current paper is substantially better due to theoretical contribution + training framework + downstream validation.
- "Now you see me!" (4.50, Withdrawn): Contrastive attribution post-processing. Similar conceptual insight about softmax but purely post-hoc. Current paper is stronger due to theoretical proof and training component.
- Controlling Structured Explanations (5.00, Reject): Shapley-based regularization during training. Similar in spirit (using explanations during training), but current paper has stronger theoretical novelty (original non-uniqueness observation vs. applying known Shapley methods).
- HiCEM (6.00, Accept): Concept-based interpretability with user studies and new dataset. Stronger empirical validation than the current paper.

**Final score:** 5.5 — The paper has a genuinely novel theoretical contribution (HiResCAM non-uniqueness) and a practical training framework with decent but not exhaustive empirical validation. The evaluation has some gaps (partial circularity, limited baselines, unexplored accuracy trade-off) that prevent it from reaching the 6+ tier, but the core ideas are solid and well-motivated.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>