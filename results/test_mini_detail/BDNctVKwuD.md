Now I have a thorough understanding of the paper and its calibration landscape. Let me write the consolidated review.

## Summary

The paper identifies a theoretical limitation of HiResCAM explanations — they admit an arbitrary spurious shift M while preserving the same probability prediction (Theorem 3.2) — and proposes ContrastiveCAMs, which are invariant to this shift and provide granular class-versus-class explanations. Using ContrastiveCAMs, the paper then derives Core-Focused Cross-Entropy (CFCE), a loss that penalizes contributions from non-core image regions, and proves it is classification-calibrated with respect to core-constrained risk minimization (Theorem 4.6). Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC show that CFCE-trained models achieve dramatically higher alignment to core regions (e.g., 93.39% ContrastiveCAM IoU vs. ≤30.27% for baselines) at a moderate accuracy cost.

## Strengths

1. **Formal proof of HiResCAM non-uniqueness (Theorem 3.2).** The paper proves that HiResCAM explanations for a given input are not uniquely determined and admit an arbitrary spurious shift M while corresponding to the same probability prediction. This is a theoretically grounded, previously unrecognized weakness in a widely used interpretability method.

2. **M-invariant ContrastiveCAMs with class-versus-class granularity (Definitions 3.3–3.4, Theorem 3.5).** The proposed ContrastiveCAMs eliminate the spurious shift M and provide pairwise class explanations that reveal hidden reliance on non-core regions — a practical improvement over the CAM family that is directly validated by the paper's theoretical analysis.

3. **Consistency guarantee for CFCE (Theorem 4.6).** CFCE is proven to be classification-calibrated with respect to core-constrained risk minimization, giving a formal bridge between interpretability and alignment that prior empirical alignment methods lack.

4. **Strong empirical alignment gains on Hard-ImageNet (Table 2).** CFCE+KL achieves 93.39% ContrastiveCAM IoU and a positive Relative Foreground Sensitivity of 0.236, while all baselines have negative RFS (e.g., −0.18 for CE) and GradCAM IoU at most 20.43%. The ablation accuracy drops sharply for CFCE models when core regions are removed (Gray Mask: 41.78% vs. 75.94% for CE), confirming that predictions are driven by core regions.

5. **Demonstrated applicability with approximate masks (Section 5.2).** The method works with auto-generated SAM masks and bounding boxes on Oxford Pets (e.g., 83.54% binary IoU with SAM masks), addressing a practical barrier for interpretability-guided training where ground-truth masks are unavailable.

## Weaknesses

### Fatal
None.

### Major

1. **Accuracy–alignment trade-off is acknowledged but not characterized.** On Hard-ImageNet, CFCE+KL drops unablated accuracy from 94.25% (CE) to 90.35%, and on Oxford Pets multiclass from 94.41% to 90.08%. The paper mentions this "at the cost of some un-ablated performance" but does not analyze the Pareto frontier (e.g., by varying λ1), discuss under what conditions the trade-off is favorable, or compare the accuracy cost to other alignment methods. This makes it difficult to judge whether the alignment improvement is worth the accuracy loss in practice.

2. **Missing standard deviations for key baselines on Hard-ImageNet (Table 2).** The non-architecture baselines (CE, CORM, DFR, CORM+DFR) are reported without standard deviations, while the proposed methods and CE w/ Arch include them. This prevents readers from assessing the statistical significance of comparisons between the proposed methods and these baselines.

### Minor

3. **ContrastiveCAM IoU is reported only for a subset of methods on Hard-ImageNet.** The ContrastiveCAM IoU column shows "—" for CE, CORM, DFR, and CORM+DFR. While the paper explains it uses GradCAM "for consistency with baselines," the CE w/ Arch baseline does have a ContrastiveCAM IoU value (30.27%), suggesting the computation is feasible. Having this metric for all baselines would strengthen the claim that ContrastiveCAMs better measure alignment.

4. **The L_core and L_Non-Core metrics in Figure 3 are not defined in the main text.** The qualitative examples show these values for CE vs. CFCE models, but the reader cannot verify how they are computed. This is a clarity gap that should be filled (even with a brief definition).

5. **CE w/ Arch has anomalously low IoU on Oxford Pets (38.58% vs. 78.37% for standard CE in binary setting).** This suggests the architectural modifications alone actively hurt alignment on this dataset. While CFCE then recovers and improves alignment, the paper does not discuss why this occurs or whether it complicates interpretation of the results.

### Trivial
None.

## Nice-to-Haves

- The hyperparameters λ1, λ2, λ3 are not analyzed; a sensitivity study or description of how they were chosen would be helpful.
- A brief description of the "interpretability-motivated modifications" in the main text (even a paragraph) would make the paper more self-contained.
- The PASCAL VOC classification results show comparable AP between CFBCE+KL (87.19%) and CE w/ Arch (88.85%); discussing why alignment gains don't translate to higher AP in this multilabel setting would add useful context.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Uncontrolled baseline comparisons" (Harsh Critic point #1).** The critic claimed that architecture modifications are applied to CE w/ Arch but not to CFCE methods, rendering the comparison unfair. This is incorrect. The paper's experimental section states: "For our experiments, we evaluate the performance of ResNet-50 with a set of interpretability-motivated modifications... For consistency, we include baselines with (denoted by 'w/ Arch') and without these modifications." CFCE and CFCE+KL are trained on the same modified ResNet-50 architecture as CE w/ Arch, making the comparison controlled. The critic's concern about architectural differences is a misunderstanding of the experimental setup. *Removed because it is factually wrong.*

- **"Practical severity of HiResCAM non-uniqueness is overstated" (Harsh Critic).** The critic argues that for a fixed trained model, HiResCAMs are determined by the parameters, and the ambiguity is in the logit space rather than in the CAM computation. However, Theorem 3.2 is correct: the softmax function's shift-invariance means that multiple logit configurations (with correspondingly different HiResCAMs) yield the same probability prediction. This is a genuine property of the model family, not an overstatement. The paper's claim that this may cause misleading interpretations is reasonable and supported by Figure 1. *Removed because this is a matter of interpretation, not an error, and the paper's framing is defensible.*

- **"Bias-free classifier restriction not discussed in main text" (Harsh Critic).** The paper explicitly states in Section 4 (page 5, after Proposition 4.1): "By zero-ing the final bias vector (i.e., b := 0_C for h only)." This is in the main text, not relegated to an appendix. *Removed because it is factually wrong.*

- Various generic or speculative criticisms about missing comparison methods (masking-based baselines, regularization-based methods). *Removed per instructions to not demand methods outside the paper's stated scope.*

- The Strength Finder's generic strengths about "important problem" and superficial praise that are not backed by specific content. *Removed.*

## Novel Insights

The harsh critic's critique inadvertently highlights an interesting gap in the paper: the "CE w/ Arch" baseline on Oxford Pets has dramatically lower IoU (38.58%) than standard CE (78.37%), yet CFCE trained on the same architecture recovers and surpasses standard CE. This suggests that the architecture modifications may have created a vulnerability to alignment loss that CFCE specifically addresses, rather than CFCE being a general alignment improvement. The paper does not discuss this dynamic, but it presents an interesting hypothesis: interpretability-motivated architectural changes may surface misalignment that standard architectures hide, and the CFCE loss then resolves it. This framing could turn a weakness into a strength and merits explicit discussion.

## Suggestions

1. **Characterize the accuracy–alignment trade-off.** Vary λ1 in Definition 4.7 and plot the Pareto frontier (unablated accuracy vs. ContrastiveCAM IoU or RFS). Show the operating point (λ1=0 corresponds to pure CE w/ Arch) and discuss where the trade-off is favorable. This turns an acknowledged weakness into a controlled analysis.

2. **Report standard deviations for all baselines on Hard-ImageNet**, or clearly justify why they are omitted (e.g., single runs from published results). Similarly, compute ContrastiveCAM IoU for at least the strongest non-architecture baselines (CE and CORM) to strengthen the contrast.

3. **Add brief definitions of L_core and L_Non-Core in Section 5.1 or the figure caption** — a single sentence indicating, e.g., "L_core = sum over core regions of CAM, L_Non-Core = sum over non-core regions of CAM" would suffice.

4. **Discuss the CE w/ Arch IoU collapse on Oxford Pets** in the main text. Even a brief note ("the architecture modifications make alignment harder, which CFCE then corrects") clarifies what might otherwise look like an unfair comparison.

## Score and Decision

**Bracketing and Narrowing Details**

*Round 1 (bracketing):* Queried for papers on interpretability, feature alignment, CAM explanations. Low-anchor papers (avg 2.5–3.0) such as WASUP, HyperPg, and Patch Ranking Map were rejected/withdrawn with issues like limited novelty, weak evaluation, or missing baselines — the current paper is clearly stronger than these. High-anchor papers (avg 8.0) such as "Interpreting CLIP's Image Representation via Text-Based Decomposition" are oral-level work with comprehensive analysis — the current paper has evaluation gaps that keep it below this tier. Mid-anchor papers (avg 4.0–7.33) are the relevant comparison.

*Round 2 (narrowing within bracket):* Compared against QPM (6.67, Accept Poster) — a clean global-interpretability paper with strong results but some subjective limitations. The current paper has stronger theoretical foundations (Theorem 3.2, 4.6) and more striking alignment gains, but weaker characterization of the accuracy–alignment trade-off. Compared against AFT for CLIP (6.80, Accept Poster) — had solid theory and experiments but novelty concerns about adversarial training's known connection to interpretability. The current paper has higher theoretical novelty. Compared against "Start Smart" (5.75, Accept Poster) — a practical method for mask-based XAI with less theoretical depth. The current paper is stronger. The paper's genuine theoretical contributions, novel method, and striking empirical results place it above 6.0, while the uncharacterized accuracy trade-off and minor evaluation gaps (missing stds, incomplete metric reporting) prevent it from reaching the 7+ tier.

**Final Score: 6.5**
**Decision: Accept (Poster)**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>