Now I have thoroughly examined the paper and all reviewer inputs. Let me write the final consolidated review.

## Summary

This paper identifies a theoretical non-uniqueness in HiResCAM explanations due to softmax shift-invariance, proposes ContrastiveCAMs (class-vs-class difference maps) that are invariant to this shift, and introduces Core-Focused Cross-Entropy (CFCE) — a training loss that uses ContrastiveCAMs to penalize contributions from non-core image regions during training. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC show large improvements in feature alignment (measured by CAM-to-mask IoU) and downstream segmentation, albeit with modest accuracy trade-offs.

## Strengths

1. **Principled integration of interpretability into training.** Using ContrastiveCAMs (which are derived from HiResCAMs) directly inside the training loss to penalize non-core contributions is novel and practically relevant. The CFCE loss (Definition 4.5) is derived from an explicit decomposition of cross-entropy into core and non-core CAM terms (Proposition 4.2), giving the approach a clean theoretical grounding beyond ad-hoc regularization.

2. **Elegant decomposition of cross-entropy (Proposition 4.2).** Showing that standard cross-entropy can be expressed as a function of ContrastiveCAMs separated by core/non-core masks is the paper's strongest theoretical contribution. It cleanly reveals why CE does not inherently favor core-region features — non-core contributions that aid classification are equally rewarded — and directly motivates the CFCE modification.

3. **Large quantitative gains in feature alignment.** On Hard-ImageNet, CFCE raises ContrastiveCAM IoU from 30.27% (CE baseline) to 89.22%, and CFCE+KL achieves 93.39%. Accuracy under core-region ablation drops sharply (Gray Mask from 76.53% to 41.78%), demonstrating substantially reduced reliance on spurious features. These are large, convincing effects.

4. **Robustness to imperfect core masks.** CFCE with automatically generated SAM masks achieves IoU of 83.95% (binary) and 85.26% (multiclass) on Oxford-IIIT Pets, and even bounding-box supervision yields competitive results (84.61% multiclass). This demonstrates practical applicability when exact segmentation masks are unavailable.

5. **Downstream segmentation improvements.** Core-focused backbones (trained with CFCE+KL) improve per-class IoU on PASCAL VOC Semantic Boundaries compared to CE-trained backbones. This transfer suggests the learned feature alignment has genuine utility beyond the training objective.

## Weaknesses

### Major

1. **Overclaimed motivation regarding HiResCAM non-uniqueness.** The paper frames the non-uniqueness of HiResCAM as a practical flaw requiring a fix (e.g., "fail to guarantee a faithful interpretation," "explanations are accurate only up to an unknown summand M"). In reality, for a **fixed, trained model**, HiResCAMs are uniquely determined by the model weights. Theorem 3.2 is mathematically correct — given only softmax probabilities, many CAM patterns are consistent — but this is a well-known consequence of softmax shift-invariance, not a limitation specific to HiResCAMs. Every logit-based explanation method inherits this property. The contrastive subtraction in ContrastiveCAM is a legitimate way to remove this redundancy, but the severity of the "problem" being solved is overstated. This weakens the paper's narrative, though the core technical contributions (ContrastiveCAM for class-vs-class explanations, CFCE for training) do not actually depend on this being a practical issue.

2. **Missing comparisons with saliency-guided training baselines.** The paper compares CFCE only with CORM, DFR, and unregularized cross-entropy — none of which use saliency during training. Relevant methods like Right for the Right Reasons (Ross et al., 2017), HINT (Selvaraju et al., 2019), or attention-based masking (e.g., Aniraj et al., 2023, which is cited in the paper) are not included. Without such comparisons, it is difficult to assess whether CFCE's benefits are unique to its formulation or shared by any approach that regularizes using attribution maps.

3. **Unexplained large IoU jump on PASCAL VOC (multilabel).** The IoU jumps from 44.50% (CE) to 82.07% (CFBCE) — an improvement of ~38 percentage points. This is an order of magnitude larger than improvements on other datasets. The paper does not define how IoU is computed for the multilabel setting (per-class averaging? per-image with multiple positive labels?), does not provide per-class breakdowns, and offers no ablation to verify this is not driven by threshold effects, metric artifacts, or some other trivial explanation. This result is suspicious and needs significant clarification.

### Minor

1. **ContrastiveCAM IoU not computed for all baselines in Table 2.** The paper computes ContrastiveCAM IoU only for CFCE and the "CE w/ Arch" baseline, but not for standard CE, CORM, or DFR. The justification ("GradCAM used for consistency with baselines") is weak; without these numbers, the reader cannot fully separate the effect of the CFCE loss from the effect of switching from GradCAM to ContrastiveCAM as the evaluation metric.

2. **Accuracy-alignment trade-off not thoroughly discussed.** On Hard-ImageNet, CFCE reduces un-ablated accuracy from ~94% to ~90% while dramatically improving IoU. The paper acknowledges this cost but does not discuss when it is acceptable or how practitioners should weigh the trade-off. Given that CFCE+KL also shows accuracy in the ~90% range, it is not clear whether the alignment gains always justify the accuracy loss, or whether there are failure modes where CFCE harms classification disproportionately.

3. **No explicit analysis of computational overhead.** Computing ContrastiveCAM gradients during training requires computing HiResCAMs for multiple classes per iteration, which multiplies the backward pass cost. The paper does not report training time comparisons or FLOPs, making it difficult for practitioners to assess the method's cost.

4. **Segmentation results reported as a bar chart without numerical values or error bars.** Figure 4 shows IoU improvements for downstream segmentation, but only as a grouped bar chart. Without exact values and error bars, the reader cannot evaluate the statistical significance or magnitude of the observed improvements.

### Trivial

- The paper would benefit from more qualitative examples of failure cases where CFCE degrades performance or misses core regions, beyond the successful cases shown in Figure 3.
- The notation overload (CAM\textsuperscript{HiRes}, CAM\textsuperscript{Cntrst}, CAM\textsuperscript{Recon}) is sometimes hard to follow across sections.

## Nice-to-Haves

- An ablation of the CFCE loss separating the core term (-∑ H⊙CAM) and the non-core term (+∑ (1-H)⊙|CAM|) would help verify each component's contribution.
- A per-class breakdown of the PASCAL VOC IoU results would clarify the surprisingly large improvements.
- Reporting ContrastiveCAM IoU for all Table 2 baselines would strengthen the comparison.
- A comparison of CFCE with the gradient of the KL regularization term visualized could provide insight into how the divergence term affects learning.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"CFCE loss is ad-hoc without derivation."** Removed because the loss is directly derived from the CE decomposition in Proposition 4.2, with the non-core term modified to use an absolute value — a natural encoding of the Core-Constrained Risk constraint (Definition 4.4). The formulation is motivated and the consistency claim (Theorem 4.6) is stated, though the proof is in the appendix (parser-removed, not missing from submission).

- **"Theorem 4.6 proof is not available."** Removed because the appendix was stripped by the PDF parser; the proof exists in the original submission.

- **"Missing comparison with contrastive Grad-CAM or guided backprop variants."** Removed as it requires knowledge of specific prior work that may or may not be directly comparable, and the paper does cite related work in the CAM family (Section 1.1).

- **"CE w/ Arch and CE use architecture modifications not described."** Removed because the paper explicitly says these modifications are in Appendix C (parser-removed), and the notation "w/ Arch" transparently indicates architecture changes are applied.

- **"HiResCAM non-uniqueness is a 'trivial' consequence of softmax."** Removed as overstatement — the observation is mathematically valid even if practically less severe than claimed. This is already addressed in the Major weaknesses section with appropriate calibration.

## Novel Insights

The most interesting observation from the reviews is the tension between the paper's theoretical motivation and its practical contribution. The non-uniqueness observation (Theorem 3.2) is mathematically correct but practically benign for fixed models — it describes ambiguity in the inverse mapping from probabilities to explanations, not an actual flaw in the explanations produced by a given model. Yet the CFCE training framework that builds on ContrastiveCAMs appears genuinely effective regardless of whether the motivating "problem" is practically severe. This suggests the review process should evaluate the CFCE contribution on its own empirical merits rather than penalizing it for having an imperfect motivational framing. A stronger version of this paper would acknowledge that the class-vs-class granularity of ContrastiveCAMs is an independent contribution (useful for debugging spurious features) and de-emphasize the "fixing a broken method" narrative.

## Suggestions

1. Reframe the motivation: Acknowledge that HiResCAM non-uniqueness is a theoretical property of the inverse mapping (probabilities → explanations) rather than a practical failure of the method for fixed models. Position ContrastiveCAM primarily as providing class-vs-class granularity, which is its genuine strength.

2. Add saliency-guided training baselines (at minimum a simple version of attention masking or gradient-based input regularization) to position CFCE against existing approaches.

3. Clarify the PASCAL VOC IoU metric definition for multilabel classification and provide per-class breakdowns. Explain why the improvement is so much larger than on other datasets — a control experiment with simple masking at test time would help.

4. Report ContrastiveCAM IoU for all baselines in Table 2 so the reader can separate the effect of the loss from the effect of the evaluation metric.

5. Include a brief discussion of the accuracy-alignment trade-off: under what conditions should a practitioner prefer CFCE over CE, and when might the accuracy loss be unacceptable?

6. Report training time overhead so practitioners can assess computational cost.

## Score and Decision

**Anchor comparisons:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| ClusCAM (MYGtEADPUs) | 4.67 | Similar CAM-based method; this paper has stronger theoretical grounding (Proposition 4.2, consistency theorem) and extends to training, but ClusCAM was more thoroughly evaluated across architectures. Slightly better. |
| VAR / "Now you see me" (FVU4vd6WoN) | 4.50 | Similar contrastive/multi-class attribution idea; that paper had higher variance (8,2,4,4). This paper is more complete with training integration. Comparable. |
| Subset Selection Attribution Regularization (3bstHHCWhD) | 4.00 | Similar goal of attribution-guided training; this paper has cleaner theoretical motivation but also missing baselines. Slightly better. |
| MICLIP (28Hfz8RLcD) | 4.50 | Accepted poster on interpretability. MICLIP has stronger evaluation breadth; this paper has a more direct training-interpretability loop. Comparable quality. |
| MI-Grad-CAM (C5Dgtmk7ho) | 3.00 | Another CAM variant with overclaimed causality; this paper is more rigorous both theoretically and experimentally. Clearly stronger. |
| Controlled Structured Explanations (3zOZXcn4YR) | 5.00 | Shapley-based regularization; rejected despite higher scores due to limited novelty. This paper has clearer novelty. Comparable quality. |
| AGR (evNfQ1sqoQ) | 2.50 | Regularization approach with weak baselines; this paper is significantly stronger both in theory and experiments. Clearly stronger. |

The paper has genuine contributions — the CFCE training framework, Proposition 4.2's decomposition, and strong empirical alignment results — along with three significant weaknesses: an overclaimed motivation, missing saliency-guided baselines, and an unexplained large result on PASCAL VOC. These issues are addressable in revision but not fatal. Positioned relative to the anchors, the paper falls below the strong accepted papers (6.5-7) but above the clearly weak papers (2-3). It is comparable to mid-range papers (4.5-5.0).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>