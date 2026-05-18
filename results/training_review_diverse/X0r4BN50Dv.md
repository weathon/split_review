Now I have all the information needed to write the consolidated review.

## Summary

The paper introduces F-Fidelity (FFid), a framework for evaluating the faithfulness of XAI explanations. FFid addresses two core problems in removal-based faithfulness metrics: (1) out-of-distribution (OOD) inputs caused by large removals, which it mitigates via an upper-bounded removal (controlled by a β parameter), and (2) classifier unreliability on perturbed inputs, which it addresses via explanation-agnostic fine-tuning using random stochastic masks. The paper evaluates FFid on image (CIFAR, Tiny ImageNet) and time series (PAM, Boiler) tasks using a systematic degradation framework to create known ground-truth rankings of explainer quality. It additionally provides a theoretical result (Theorem 1) connecting the FFid⁺ metric to explanation size recovery, validated on a synthetic colored-MNIST dataset.

## Strengths

1. **Explanation-agnostic fine-tuning elegantly sidesteps information leakage.** Unlike ROAR, which retrains on explainer-specific masks and can leak information about which explainer produced the mask, FFid fine-tunes with random stochastic masks that are independent of any explainer output (Section 3, Eq. 4). This design choice cleanly separates robustness adaptation from explanation evaluation.

2. **Systematic degradation framework provides a principled ground-truth for comparison.** Rather than relying on human annotations or synthetic datasets with potentially questionable ground truth, the paper degrades a known-good explainer (Integrated Gradients) with controlled noise to create a provably correct ranking of explainer quality (Section 4). This methodological choice raises the bar for how faithfulness metrics should be compared.

3. **Consistent empirical superiority across two modalities and both macro/micro metrics.** The results in Sections 4.1 and 4.2 show FFid achieving perfect or near-perfect macro Spearman correlations on Tiny ImageNet (-1.00 across all metrics for both SG-SQ and GradCAM) and consistently outperforming Fidelity, ROAR, and RFid on time series datasets. The comprehensive sparsity range (5–95% at 5% intervals) rules out the concern that results are artifacts of a particular sparsity level.

4. **Theoretical insight connecting faithfulness metrics to explanation sparsity is novel.** Theorem 1 provides a formal link between the FFid⁺ metric's monotonicity and the size of the most influential feature tier, under Shapley-value-based explainers and a tiered influence structure. While the assumptions are idealized, this is a genuinely novel theoretical contribution that goes beyond the standard "propose a metric and evaluate it" paradigm.

## Weaknesses

### Fatal
None.

### Major

1. **The β hyperparameter is never specified for the main evaluation experiments (Sections 4.1, 4.2).** β is a critical parameter in the framework: it simultaneously controls (a) the fraction of input removed during evaluation via Eq. 3 (the truncation), and (b) the mask size used in the fine-tuning loss via Eq. 4. Yet the reader is told only that "For RFid and FFid, we set α⁺ = α⁻ = 0.5" for the time series experiments (line 144), with no mention of β for either time series or image experiments. Without this information, the experiments cannot be reproduced, and it is unclear whether β was tuned per domain, held fixed, or set to a default value. This is a basic methodological reporting gap that must be addressed.

2. **No ablation study isolates the contributions of the two proposed components.** FFid incorporates two modifications relative to the RFid baseline: (i) explanation-agnostic fine-tuning and (ii) upper-bounded removal (β-truncation). The paper compares FFid against RFid (which uses neither) and reports large improvements. However, it never tests the intermediate conditions: RFid + bounded removal alone (no fine-tuning), or FFid without β-truncation but with fine-tuning. Without an ablation, the reader cannot tell whether both components are necessary or whether one alone drives the gains. Given that the paper frames both as contributions, this gap weakens the empirical claims about the method's design.

### Minor

3. **The explanation-size recovery claim is broader than the evidence supports.** The abstract and conclusion state that FFid "can be used to compute the sparsity of influential input components, i.e., to extract the true explanation size" (line 14). However, Theorem 1 operates under strong idealized assumptions: a Shapley-value-based explainer, a fixed tier structure with known sizes, and a monotonic function g. The empirical validation (Section 6) is limited to a single synthetic dataset (colored-MNIST) with two tiers. The paper itself acknowledges that good explainers often produce continuous scores without distinct clustering (lines 155-156), yet the claimed capability is not tested in those realistic scenarios. The theoretical insight is valuable and the synthetic validation is appropriate for a first step, but the practical claim should be scoped to match the evidence.

4. **"Micro rank" is referenced in tables but never formally defined.** The text (lines 127-129) defines macro and micro *correlations*, stating it reports "the average rank of each method," but tables include a "micro rank" column with values (e.g., ~2.00) whose computation is not explicitly specified. This is a small presentation gap but affects interpretability of the results.

### Trivial

5. **The paper does not discuss the gap between random masks used in fine-tuning and structured masks used in evaluation.** The fine-tuning step uses random stochastic masks (randomly dropping pixels/patches), while evaluation removal masks are driven by explainer outputs and may be highly non-random (e.g., removing contiguous regions for images). The empirical results suggest this transfer works, but a brief discussion acknowledging this potential gap would strengthen the paper's analysis.

## Nice-to-Haves

- A β-sensitivity analysis (e.g., varying β from 0.3 to 0.7) to help practitioners understand how to set this parameter in new domains.
- An additional experiment on a real-world dataset where ground-truth explanation size is known (e.g., a graph dataset like BA-Shapes) to strengthen the cross-domain validity of the explanation-size recovery claim.
- A more precise statement about explanation-size recovery in the abstract/conclusion that acknowledges the idealized conditions under which the result holds.

## Removed Points

- **NLP experiments absent from main text:** The reviewer claimed the main paper claims NLP as an evaluated modality but only shows images and time series. The appendix (which contained NLP results) was stripped by the parser. Per hard rules, criticisms about missing appendix content are removed — the content exists in the original submission.
- **Random vs. structured mask discussion gap kept as trivial** (see Weakness Minor #5 above — retained but downgraded to trivial).

## Novel Insights

The most interesting signal emerging from the reviews is a tension that the paper itself does not fully explore: the method's success hinges on the *mismatch* between training-time masks (random, unstructured) and evaluation-time masks (explainer-driven, potentially structured). Most prior work assumes these distributions should match; FFid deliberately uses disjoint distributions and shows it works anyway. This suggests a deeper principle — that what matters for faithful evaluation is not distributional *identity* between training and evaluation masks, but a weaker property (perhaps coverage of the mask space or the model's learned invariance to masking patterns). Exploring why this transfer succeeds could lead to a more fundamental understanding of what makes a faithfulness metric reliable.

## Suggestions

1. Report the β value(s) used in the image (CIFAR, Tiny ImageNet) and time series (PAM, Boiler) main experiments. Also clarify whether β was held fixed across domains or tuned per dataset.
2. Add an ablation study comparing at least four conditions: (a) FFid (full method), (b) RFid + bounded removal (no fine-tuning), (c) RFid + fine-tuning (no bounded removal), and (d) original RFid.
3. Temper the abstract/conclusion claims about explanation-size recovery to reflect the idealized assumptions required. A phrasing such as "Under the assumption that the explainer approximates a Shapley-optimal explainer and features have a discrete tier structure, FFid⁺ can recover the most influential tier's size" would be more precise.
4. Formally define "micro rank" in Section 4 and explain why it is informative beyond the micro correlation.
5. Add a brief discussion (1–2 sentences in Section 3 or 4) acknowledging the distribution gap between random fine-tuning masks and structured evaluation masks.

## Score and Decision

Based on my assessment: the core methodological contribution (explanation-agnostic fine-tuning + bounded removal) is well-motivated and the experimental evidence for its effectiveness is strong across two modalities. The two major weaknesses — the missing β specification and the absent ablation study — are significant but addressable. The paper's contribution is believable and represents a genuine advance over prior removal-based metrics.

A score of 6 reflects a solid paper with correctable gaps that should not prevent acceptance but require attention.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>