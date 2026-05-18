Now I have a thorough understanding of the paper and the review inputs. Let me synthesize the final consolidated review.

---

## Summary

This paper identifies and systematically studies *scale shift* — differences in head scale distributions between training and test domains — as a distinct and under-explored challenge in domain generalization for crowd localization. The authors build ScaleBench (17,138 images, 1.5M bounding box annotations across 4 scale-controlled domains), benchmark 20 existing DG algorithms showing many fail on scale shift, provide a theoretical characterization of scale shift as a mixed diversity+correlation shift, and propose Semantic Hook as a case-study mitigation method. The paper's core value lies in formalizing and quantifying the problem; the contributions are a resource (ScaleBench), an empirical finding (existing DG algorithms underperform), a theoretical framing, and a proof-of-concept method.

## Strengths

1. **First dedicated benchmark and systematic study of scale shift in DG for crowd localization.** ScaleBench is built via a principled domain partition pipeline (2D Gaussian mixture model → image-to-patch splitting → scale-distribution manipulation) that produces four domains with controlled inter-domain scale shifts (Sec. 2.2). This moves beyond prior cross-dataset evaluations that confound scale with other factors. The benchmark is a genuine resource that enables future controlled study.

2. **Comprehensive failure analysis of 20 DG algorithms.** The paper reproduces 20 SOTA domain generalization methods on ScaleBench across three backbones (ResNet18, HRNetW-48, ViTBase), and shows that many perform worse than a simple ERM baseline (Table 2). This empirical evidence directly supports the claim that scale shift is under-explored and that existing DG approaches do not address it.

3. **Formal characterization of scale shift as a mixed shift (diversity + correlation).** Theorem 1 connects scale shift to established OOD concepts (Ye et al., 2022), explaining why single-shift-targeting algorithms fail. Even if the formalism has imprecisions (see below), the conceptual framing is useful and provides a principled basis for future algorithm design.

4. **Actionable empirical analysis via four well-defined research questions (Q1–Q4).** The controlled experiments in Sec. 4.3 — multi-source ablation (Table 3), IID-by-scale "less is more" (Figure 4), interpolation study (Table 4), and Semantic Hook ablation (Table 5) — provide concrete evidence about the nature of scale shift that future work can build on. The ablation showing scale perturbation harms performance (61.34% vs. 73.88% InD in Table 5) directly corroborates the spurious-correlation hypothesis.

## Weaknesses

### Fatal
None.

### Major

1. **ScaleBench lacks confound analysis.** The four scale-defined domains are constructed by partitioning patches from multiple original datasets (SHHA, SHHB, SHRGBD, QNRF, JHU, NWPU) that differ in scene type, density, camera perspective, and resolution. The paper filters patches only by scale standard deviation but does **not** check whether the resulting domains are balanced on these other attributes. If, for instance, the Tiny domain contains disproportionately more patches from indoor surveillance views while the Big domain contains more close-up street scenes, then observed performance differences could be driven by confounds, not scale alone. This weakens every conclusion drawn from benchmark evaluations. The paper should at minimum analyze domain similarity on non-scale features or explicitly discuss this limitation and its implications.

2. **The theoretical analysis (Theorem 1) has mathematical imprecision that weakens its claimed rigor.** Two specific issues: (i) The theorem premise states "p₁(c|z) ≠ p₂(c|z)" (conditional scale distributions given objects), but the formulas use *marginal* distributions p₁(c) and p₂(c) — these are different quantities and the logical link between premise and formulas is not established. (ii) The correlation shift formula uses the Bhattacharyya coefficient √(p₁(c)·p₂(c)), which equals 0 when the supports of p₁ and p₂ are disjoint, making the claimed "> 0" false in that edge case. The paper presents Theorem 1 as a proof ("we prove that scale shift embodies a combination of both") but provides no derivation — just states the equations. This matters because the mixed-shift claim is used to motivate both the failure of existing DG algorithms and the design of Semantic Hook. The core intuition is plausible and likely correct, but the formalism needs tightening to support the weight placed on it.

### Minor

3. **Semantic Hook's design intuition is under-explained and reproducibility details are missing.** The paper's claim that the residual f_E(x+ε) − γ f_E(x) "tends to contain less task-specific information" but that minimizing its prediction loss can "hook" task-relevant features is not self-evident and needs clearer mathematical or empirical justification (e.g., feature visualization, probing analysis). Additionally, the γ annealing schedule and noise variance λ are not specified, making the method not fully reproducible as described. While Semantic Hook is presented as a case study rather than a SOTA method, these gaps limit its utility for future work.

4. **The "less is more" experiment (Q2) does not show that scale is uniquely important.** The paper IID-samples by scale and shows 30% of data suffices. But this result is expected: if training and test are matched on scale distribution, data reduction should work. To demonstrate that scale is a *major* attribute (not just *an* attribute), the paper should compare with IID sampling by other attributes (density, scene type) and show that scale-distribution matching gives superior data efficiency. Without this, Q2 is a consistency check rather than a novel insight.

5. **Potential data leakage from patch-based LOO evaluation.** The four domains are constructed from patches of the same original datasets. In the Leave-One-Out evaluation, source domains contain patches from the same original datasets as the target domain (just from different scale buckets). The paper does not discuss whether this creates leakage or whether validation on source-domain patches meaningfully generalizes to target-domain patches from the same original images.

6. **No comparison with scale-aware crowd localization methods.** The paper compares 20 generic DG algorithms but does not include scale-aware architectures or multi-scale training techniques from the crowd localization literature (e.g., multi-column networks, scale-adaptive modules). Since the problem is specifically about scale, such comparisons would better contextualize whether DG algorithms are insufficient or simply not designed for this task.

7. **Annotation quality for the 1.5M bounding boxes is not reported.** The paper provides no inter-annotator agreement statistics, no quality checks, and no comparison with the original point annotations for consistency. While annotation details may reside in a stripped appendix, the lack of even a brief quality statement in the main text undermines confidence in the core empirical instrument.

### Trivial
- Equation (6) and the surrounding derivation (§3.1) blend notation for abstract objects, attributes, and distributions in a way that is hard to follow. A cleaner causal graph or direct statement of the spurious-correlation claim would serve better.

## Nice-to-Haves
- Compare IID sampling by other attributes (density, scene type) alongside scale to demonstrate that scale is uniquely important (addresses Weakness #4).
- Include one or two scale-aware crowd localization baselines for reference.
- Provide the γ annealing schedule and λ value in a short table or pseudocode.
- Add a brief limitations paragraph acknowledging the potential confound issue and the need for further validation of the domain partition.

## Removed Points
These points from the reviewers are flagged to be removed — treat them with caution:
- **"Semantic Hook's design is self-contradictory"** — The reviewer claims that using a residual with "less task-specific information" to minimize prediction loss is contradictory. This misreads the paper: the method is a standard robustness technique where forcing a perturbed representation to still predict well encourages the model to rely on stable (semantic) features. The paper's intuitive explanation, while not fully rigorous, is coherent.
- **"Empirical insights (Q1, Q3) are standard DG observations"** — While these insights confirm intuitions, their value lies in being *empirically demonstrated* in the specific underexplored context of scale shift in crowd localization. The paper does not claim discovery of universal principles, and the experiments are well-designed.
- **"The paper does not achieve SOTA"** — The paper explicitly states Semantic Hook is a case study/analysis tool, not a SOTA method. Criticizing it for marginal improvement ignores the paper's own framing.

## Novel Insights
Beyond the paper's own contributions, the most noteworthy finding is the joint review: the paper's central empirical claim — that scale shift is a distinct and under-addressed DG problem — is convincingly demonstrated by the systematic failure of 20 DG algorithms, many of which fall below a simple ERM baseline. The ablation showing scale perturbation harming performance (Table 5) cleanly isolates the spurious-correlation mechanism. However, the strength of this empirical contribution is tempered by the confound-control gap in ScaleBench and the mathematical imprecision in the theoretical framing, which together prevent the paper from fully delivering on its ambition.

## Suggestions
1. **Validate ScaleBench.** Provide inter-annotator agreement for the 1.5M new bounding boxes, show consistency with original point annotations, and critically, analyze whether the four domains differ systematically on non-scale attributes (scene type, density, camera angle) — or explicitly discuss why such confounds are unlikely.
2. **Tighten Theorem 1.** Use consistent notation (marginals throughout, not mixing conditionals and marginals). Clarify the assumptions under which correlation shift > 0 holds, or reframe it as a plausible hypothesis supported by experiments rather than a proven theorem.
3. **Clarify and document Semantic Hook.** Provide the γ annealing schedule and λ value. Add a brief analysis (e.g., feature probing or visualization) showing that Semantic Hook actually reduces scale-feature dependence.
4. **Strengthen Q2.** Add a control experiment: IID sample by another attribute (e.g., density) and show scale yields superior data efficiency.
5. **Discuss the patch-origin leakage concern** in the evaluation section explicitly.

## Score and Decision

This paper tackles a genuinely important and under-explored problem. The benchmark, if properly validated, would be a useful community resource. The empirical documentation that 20 DG algorithms fail on scale shift is valuable. However, the confound-control gap in ScaleBench and the mathematical imprecision in Theorem 1 are significant enough that the paper's central claims cannot be fully trusted in this version. A major revision addressing these issues could make this a strong contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>