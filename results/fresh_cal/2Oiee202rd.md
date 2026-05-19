Here is my consolidated review:

## Summary

PerceptionCLIP proposes a training-free two-step zero-shot classification method for CLIP: first infer contextual attributes (e.g., background, orientation) from the image using CLIP itself, then classify conditioning on those inferred attributes. The method is motivated by human visual perception and evaluated on 11 datasets for generalization and on Waterbirds/CelebA for group robustness, showing consistent improvements over standard CLIP templates and 80-template prompt ensembling.

## Strengths

1. **Consistent generalization gains across 11 datasets.** The paper reports that PerceptionCLIP with domain-specific attributes (e.g., *image source* + *condition* for EuroSAT) outperforms both the simple template and 80-template prompt ensembling on every dataset, with a near 5% accuracy improvement on EuroSAT (Section 7.1). The paper further shows that "considering almost any single contextual attribute improves the accuracy" (line 338), demonstrating robustness to attribute choice.

2. **Substantial reduction in worst-group accuracy gap on Waterbirds (19%) and CelebA (7%) with ViT-L/14** (Section 7.2). By conditioning on attributes such as *background* (Waterbirds) or *gender* (CelebA), the method reduces reliance on spurious correlations without any fine-tuning or additional data.

3. **Training-free and principled formulation.** The method requires no fine-tuning or external data, operating entirely through CLIP's existing representations. The probabilistic framing (joint, conditional, and marginal distributions approximated via CLIP scores) and the annotation function that maps discrete attribute values to text distributions provide a systematic foundation that goes beyond ad-hoc prompt engineering (Sections 3–4).

4. **Grad-CAM visualizations support the claimed mechanism.** Figure 3 (Section 5.2) shows that conditioning on correct contextual attributes shifts saliency toward core object features and away from spurious background regions, with quantified core-vs-spurious ratios. This connects the algorithmic steps to the interpretability claim.

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguity in how the "two most effective attributes" were selected (Section 7.1).** The paper states that "using the two most effective attributes" outperforms 80-template ensembling (line 344). It is not fully clear whether these attributes were chosen based on prior knowledge of the data generation process (as described in lines 318–319: "We manually construct essential attributes that may be generative factors") or by peeking at test-set performance. The paper partially mitigates this by showing that (a) *almost any* single attribute improves accuracy (line 338) and (b) accuracy improves monotonically as more attributes are added (line 345). Nevertheless, the phrase "most effective" creates ambiguity about the selection protocol, and this should be explicitly clarified — either by stating that a held-out validation set was used or by reporting results with a fixed, pre-specified attribute set for all datasets.

2. **Group robustness evaluation lacks a controlled ablation that isolates the benefit of the two-step marginalization over simply describing the spurious attribute in the prompt.** On Waterbirds and CelebA, the baselines are standard class-only templates. While the results show that conditioning on attributes reduces the worst-group gap, it is unclear how much of this gain comes from (a) the two-step marginalization over the attribute distribution versus (b) simply appending the inferred attribute value to the prompt in a one-shot manner. Adding a baseline that uses the *inferred* attribute value (not ground-truth) directly in a single prompt — without the marginalization over the distribution — would cleanly isolate the value of the full algorithm.

### Minor

1. **No runtime or computational cost analysis.** The method requires evaluating CLIP for all combinations of classes and attribute values. For datasets with many classes and attributes, this could be substantially more expensive than standard zero-shot CLIP. The paper does not discuss this cost or provide inference time comparisons (Section 6). This should be reported, as it affects practical deployment claims.

2. **The proof-of-concept attribute inference accuracy (~74% on binary synthetic tasks) is modest** (Section 5.3). While above chance (50%), this leaves room for error in the first step. The paper acknowledges this via the temperature intervention, but the practical impact of inference errors on the final classification is not systematically analyzed (e.g., how often does an incorrect attribute inference cause a wrong class prediction?).

3. **Performance gains over 80-template ensembling on standard benchmarks are often modest (1–2%)** (Section 7.1). The paper's framing could more clearly distinguish between the consistent but small improvements on standard benchmarks and the larger gains on domain-specific datasets (EuroSAT) and group robustness. The current framing suggests a larger breakthrough than the numbers on standard benchmarks indicate.

### Trivial
None.

## Nice-to-Haves
- An ablation comparing the two-step marginalization approach against a simpler "append inferred attribute to prompt" baseline would strengthen the group robustness analysis.
- Testing whether attributes can be automatically discovered (e.g., via LLM prompting or CLIP's own zero-shot knowledge) rather than hand-crafted per dataset would improve practical applicability.
- Reporting statistical significance (confidence intervals or variance across runs) would help assess the reliability of the reported gains, though single-run evaluation is the norm in CLIP zero-shot benchmarks.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Attribute underspecification hurts reproducibility"** — The paper names specific attributes for each dataset in the main text (e.g., *background* for Waterbirds, *gender* for CelebA, *image source* and *condition* for EuroSAT, *cuisine* for Food101, *species* for Oxford Pets). Full details would be in the supplementary material, which the parser strips. Also, the reviewer's concern about vague examples like "cuisine" or "species" is inaccurate: these are the actual attribute names used for those datasets, not vague placeholders.
- **"CLIP scores as unnormalized log-probabilities is not justified"** — The paper explicitly cites the energy function connection (line 144) and this is standard practice in the CLIP literature. The paper presents these as approximations, not as generative probabilities.
- **"Wrong/random attribute ablation is too simple"** — The paper's ablations use semantically meaningful "wrong" values (e.g., "upright" for a flipped image) and random strings, which are standard controls. The reviewer's suggestion of "plausible but incorrect" attributes would be a supplementary experiment, not a flaw.
- **"Single-step computational cost not discussed"** — This is retained as a Minor weakness above (it's a real practical concern). The removed version refers to the reviewer's framing that it was an "omission" that invalidates the method, which overstates the issue.
- **"No comparison to existing debiasing methods"** — The paper evaluates a training-free zero-shot method; comparing to training-based approaches like group-DRO or counterfactual prompting would be apples-to-oranges. The retained weakness (Major #2) focuses on the more relevant ablation that falls within the paper's own methodological scope.
- **"Statistical significance not reported"** — Single-run evaluation with point estimates is standard for CLIP zero-shot benchmarks. This is moved to Nice-to-Haves.

## Novel Insights
The harsh critic correctly notes that the two-step inference can be collapsed into a single step (summing exponentiated scores over attributes), which the paper itself identifies as a special case that "coincides with prompt ensembling" (line 306). This is an insightful connection: it provides a principled explanation for why ad-hoc prompt ensembling works — it implicitly marginalizes over contextual attributes — and simultaneously shows why the systematic, structured attribute set of PerceptionCLIP is superior: it covers the actual generative factors rather than random templates. This reframing of prompt ensembling as implicit perception is the paper's most interesting conceptual contribution and deserves more emphasis.

## Suggestions

1. **Clarify the attribute selection protocol.** Explicitly state whether attributes were chosen before or after seeing test accuracy, and whether the "two most effective" selection was based on a validation set or prior knowledge. If attributes were selected post-hoc, re-run the main tables with a fixed, pre-specified attribute set.
2. **Add a controlled ablation for group robustness.** Compare against "direct attribute prompting" — using the single inferred attribute value (not the distribution) directly in the prompt. This isolates the benefit of the two-step marginalization.
3. **Report inference time** alongside accuracy for the main experiments, comparing PerceptionCLIP to standard CLIP and 80-template ensembling.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Reject</decision>