Now I have a thorough understanding of the paper and the reviews. Let me synthesize the final review, carefully cross-referencing every criticism against the paper text.

## Verification Summary

I verified all claims against the actual paper text. Key findings:

- **Table data is missing** from the parsed text because tables are loaded via `\input{figures/table_DSD.tex}` — a parser limitation, not a paper flaw.
- **Line 112** confirms the paper acknowledges the multi-label confound.
- **Line 152** shows the paper claims the GMM "negates the bias associated with engineering detection scores" — this is somewhat inflated given line 158 admits the approach "still relies on heuristic scores."
- **Line 191** confirms the ensemble "rarely surpasses the best baselines for a specific distribution shift type."
- **Lines 129-131** confirm method modifications are acknowledged.
- **Line 177** confirms AUC-only reporting is a deliberate choice.
- **Line 4** shows the dataset is called "PartialBROAD" without explanation.

Now writing the consolidated review.

---

# Consolidated Review

## Summary

This paper introduces BROAD, a benchmark spanning five types of distribution shifts (novel classes, adversarial perturbations, synthetic images, corruptions, and multi-label images) for OOD detection relative to ImageNet. It evaluates 12+ existing detection methods and finds that every method performs well on some shift types but poorly on others. The paper also proposes a GMM-based ensemble of existing detection scores that improves average AUC across shift types (6.86% on ViT, 4.04% on ResNet-50) but rarely beats the best single method on any individual shift type.

## Strengths

- **Novel multi-label category with a concrete construction methodology.** Section 2.5 introduces multi-label images (images containing ≥2 distinct ImageNet classes occupying substantial area) as a genuinely new distribution shift type for OOD detection. The construction pipeline (filtering COCO 2017 training images, ranking by second-largest-class area, keeping top 2000) is clearly specified and reproducible.

- **Quantified demonstration of inconsistency across shift types.** The paper provides concrete evidence (Figure 1, Section 4) that every evaluated baseline exhibits "subpar performance on at least one distribution shift" and that "almost all of them are Pareto-optimal." This is a clear, evidence-backed diagnosis, not generic criticism.

- **Architecture-dependent method rankings.** The paper reports that MDSl ranks as the best baseline on ViT but the third-worst on ResNet-50 (Section 4). This non-obvious finding shows backbone choice fundamentally changes which detection methods work, reinforcing the call for broader evaluation.

- **Principled score-selection procedure for the ensemble.** Section 3 describes using covariance matrices on a held-out validation set to avoid highly correlated scores, and using in-distribution error detection AUC to break ties — a methodologically sound approach that does not require OOD samples (explicitly bolded in the text).

- **Ens-F (fast variant) retains most of the benefit.** The 5-score fast ensemble "trails only slightly" in DSD and "unexpectedly delivers the best results" in error detection (Section 4), showing the approach can be deployed with minimal overhead.

## Weaknesses

### Major

1. **The GMM ensemble framing is overstated relative to what it actually achieves.** The paper's central diagnosis is strong: existing methods are overspecialized to particular shift types. But the proposed solution — a GMM fitted on the outputs of those same specialized methods — does not genuinely solve the specialization problem. The paper claims (line 152) that generative modeling "negates the bias associated with engineering detection scores against specific distribution shifts," but the GMM operates on those very scores and inherits their biases. The paper itself acknowledges (line 158) that "this approach still relies on heuristic scores" and (line 191) that the ensemble "rarely surpasses the best baselines for a specific distribution shift type" — it merely averages out specializations. The framing as "generative modeling" that overcomes engineered-score bias is misleading; this is fundamentally an ensemble of discriminative scores with a learned weighting scheme. The method is a reasonable baseline but not a conceptual advance that addresses the paper's own diagnosis.

### Minor

2. **Multi-label benchmark has a confound that is acknowledged but not resolved.** The paper states (line 112) that the multi-label benchmark "exhibits other less easily characterized shifts, such as differences in the properties of ImageNet and CoCo images, and the fact that MultiLabel comprises only 17 of the 1000 ImageNet classes." While the paper attempts to mitigate the class-subset issue (line 114: evaluating on the same 17 classes only), the domain/style gap between ImageNet and COCO photography remains uncontrolled. This makes it impossible to attribute detection performance to the "multi-label" property specifically rather than to the dataset style shift.

3. **Missing GMM implementation details.** The paper specifies the score sets (Ens-V, Ens-R, Ens-F) and the training set size (45k samples) but does not report the number of GMM components, covariance parameterization (full/diagonal/tied), initialization strategy, regularization for near-singular covariance, or convergence criteria. Fitting GMMs in 8-dimensional space with tens of thousands of samples can be ill-conditioned if scores exhibit near-deterministic relationships, and these details matter for reproducibility.

4. **No variance or confidence intervals reported.** Results are reported as point estimates of AUC without error bars, standard deviations, or confidence intervals. Given that some benchmarks are small (e.g., multi-label at 2000 images) and that the paper's main empirical finding (inconsistency) depends on relative rankings, variance could affect the conclusions.

5. **AUC-only reporting reduces comparability with the OOD detection literature.** The paper states (line 177) that FPR@95 and AUPR are "redundant with AUC," but FPR@95 is a standard metric in OOD detection that captures behavior at low false-positive rates — a practically relevant operating point. Omitting it makes direct comparison with many existing results difficult.

6. **Several baseline methods are used in modified forms that may disadvantage them.** CADet uses only the intra-similarity score (line 129), DOCTOR uses only $D_\alpha$ (line 130), and Odin uses default parameters tuned for novel-class detection (line 131). While the paper acknowledges these modifications, it does not assess whether the full formulations would perform differently on the proposed shift types.

7. **"PartialBROAD" naming is unexplained.** The HuggingFace dataset is called "PartialBROAD" (abstract), but the paper never clarifies what is partial about the release or what is omitted.

### Trivial

8. **Single perturbation budget for adversarial attacks.** Using $\epsilon=0.05$ for $L_\infty$ is a single setting; results may not generalize to other perturbation magnitudes. (The paper does not justify this specific choice.)

9. **Stable Diffusion prompt template is narrow.** Using only `"High quality image of a {class_name}"` generates a limited style of synthetic images, while current generative models produce much wider variety.

## Nice-to-Haves

- Provide per-dataset results (not just per-category averages) to reveal variation within shift types.
- Ablate the GMM against simpler ensembles (e.g., simple average of normalized scores, logistic regression) to verify that the generative modeling aspect provides benefit beyond discriminative combination.
- Include FPR@95 alongside AUC to improve comparability with existing literature.
- Analyze *why* methods fail on specific shift types (mechanistic analysis) rather than just reporting inconsistency — e.g., do norm-based methods systematically fail on adversarial attacks?
- Consider milder corruption levels (not just max intensity) for more practical relevance.
- Study mixtures of shift types, as real-world deployments do not present cleanly categorized shifts.

## Removed Points

The following points from the harsh critic were removed per the filtering guidelines:

- **"Quantitative results cannot be verified from parsed text"**: The tables are loaded via `\input{figures/table_DSD.tex}` — this is a parser limitation, not a paper flaw. The tables exist in the original submission.
- **"Inference time cut off"**: Parser artifact (line 193 truncation).
- **"Corruptions at max level only"** and **"mixture of shift types not discussed"**: These are scope choices or nice-to-haves, not weaknesses. The paper deliberately tests challenging scenarios.

## Novel Insights

The most interesting observation that emerges across the reviews is the **architecture-dependent reversal of method rankings** (MDSl best on ViT, third-worst on ResNet-50). This suggests that the feature geometry of the backbone fundamentally shapes which OOD detection heuristics are informative — an insight that points toward the need for architecture-aware detection method design rather than one-size-fits-all approaches. The finding that the fast ensemble (Ens-F) unexpectedly performs best on error detection is also a non-obvious result worth deeper investigation.

## Suggestions

1. **Reframe the GMM ensemble as a strong baseline, not a conceptual solution to specialization.** The paper's diagnostic contribution (methods are inconsistent) is strong enough to stand on its own. Presenting the ensemble as "a first step" (as the paper already does in the abstract) is appropriate, but claims about "negating bias" should be toned down to match what is actually achieved: averaging across specialized detectors.

2. **Either resolve the multi-label confound (e.g., using a controlled multi-label generation pipeline with fixed style) or rename the benchmark to reflect what it actually measures** (e.g., "multi-label + domain-shifted images").

3. **Report GMM hyperparameters and variance** in a revision or appendix.

4. **Clarify the "Partial" in PartialBROAD** — what is withheld and why?

5. **Include per-dataset results and FPR@95** in supplementary materials or a revision.

## Score and Decision

This paper makes a genuine contribution with the BROAD benchmark and the empirical finding of inconsistency across shift types. The multi-label category is a genuinely novel addition. However, the method framing is overstated, the multi-label benchmark has an acknowledged but unresolved confound, and several implementation details are missing. The benchmark contribution is solid and would be useful to the community with revisions to clarify scope and limitations.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>