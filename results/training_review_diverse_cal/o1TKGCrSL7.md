Now I have all the information I need. Let me compile the final review.

## Summary

The paper proposes L-DRO, a method that uses natural language descriptions of confounding sub-population attributes (e.g., "male"/"female") to debias CLIP's image representations via an entropy maximization loss plus a consistency loss, thereby improving worst-case subgroup accuracy without requiring instance-wise group membership labels. The method is evaluated on CelebA and Waterbirds datasets across multiple CLIP architectures, showing consistent worst-case accuracy improvements and superior training stability compared to DRO baselines.

## Strengths

- **Consistent and substantial worst-case accuracy gains across architectures and datasets**: Table 6 (table_worst_case_zero_shot) shows L-DRO achieves the best worst-case accuracy among all methods on both CelebA and Waterbirds with both RN50 and ViT-B/32. For example, on CelebA ViT-B/32, L-DRO achieves 79.2±1.3% vs. the best DRO baseline (χ²-DRO) at 72.0±9.6%.

- **Superior training stability without early stopping**: Figure 1 (fig_stability) demonstrates that L-DRO maintains nearly flat worst-case accuracy across training epochs on both datasets, while χ²-DRO, JTT, and CVaR DRO exhibit large fluctuations. This directly addresses a known practical weakness of DRO methods that typically require a domain-aware validation dataset for model selection via early stopping.

- **Language-based debiasing without instance-wise labels**: The method only requires natural language descriptions of the sub-population attributes—not per-sample group membership—which represents a practically useful trade-off between supervision cost and robustness.

- **Robustness to hyperparameter choice**: Table 3 (table_vary_eta) shows that varying η over two orders of magnitude (512 to 8192) yields nearly identical worst-case accuracy (79.2%–76.3%), demonstrating insensitivity to this hyperparameter.

- **Data efficiency**: Table 9 (table_data_eff) shows that L-DRO reaches or exceeds zero-shot worst-case performance with as few as 2048 training examples on CelebA and 512 on Waterbirds.

- **Informative analysis of correlated and unaligned debiasing**: Table 10 (table_mutual_sig) and Table 11 (table_mutual_h) systematically explore how debiasing on semantically related vs. unrelated attributes affects performance, providing useful practical guidance.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed theoretical grounding**: The paper claims "a principled connection between natural language supervision and robustness to sub-population shift" (line 44), but the derivation in Section 4 (Eq. 4–5, lines 163–173) is heuristic, not principled. The reasoning proceeds from "using ERM with balanced labels yields performance proportional to subgroup proportions" (itself an approximation) to a claimed proportionality `sup_{Q} E[ℓ(θ,Z)] ∝ -ℓ_ent(P(F|x), P(M|x))` without formal justification. The method itself—maximizing entropy of predictions on debiasing prompts—is a reasonable and empirically effective heuristic, but the paper overstates the theoretical foundation. This gap between claimed and actual contribution weakens the paper's framing and creates false expectations.

- **Comparison asymmetry with DRO baselines is insufficiently discussed**: L-DRO receives subgroup attribute descriptions (e.g., "male"/"female") as debiasing prompts, while the primary DRO baselines (CVaR DRO, χ²-DRO, JTT) receive no subgroup information whatsoever—they only see data and labels. This structural asymmetry means the comparison conflates two distinct advantages: the entropy-based debiasing mechanism and the availability of the confounding attribute's identity. A fairer framing would position L-DRO as a language-guided debiasing method that benefits from knowing the attribute, rather than as a general DRO competitor. The paper includes OrthCali (which also uses language) but does not foreground this distinction or isolate the source of L-DRO's gains. This does not invalidate the contribution but significantly changes what is legitimately claimed.

- **No uncertainty estimates for zero-shot baselines**: Throughout all tables, zero-shot results are reported as point estimates without standard deviations, while L-DRO results include ± ranges. This makes it difficult to assess whether improvements are statistically meaningful in cases where gains are modest (e.g., Waterbirds ViT-B/32 with prompt "a {landbird, waterbird}": zero-shot 56.8 vs. L-DRO 56.6±2.6). Given that all L-DRO experiments are run with 10 seeds, the same should be done for zero-shot to enable proper comparison.

### Minor

- **Method requires knowing the confounding attribute**: L-DRO needs the practitioner to (a) know which attribute causes the sub-population shift and (b) be able to describe it verbally. Table 10 shows that debiasing on an unaligned attribute reverts performance to near zero-shot levels. The paper acknowledges this in the limitations (lines 600–603) but uses the term "domain-oblivious" (defined as lacking instance-wise labels, line 41) throughout, which may mislead readers into thinking the method requires less prior knowledge than it actually does.

- **Improvement over zero-shot is prompt-dependent**: While many prompt choices show substantial improvements, some do not (e.g., Waterbirds ViT-B/32 with prompt "a {landbird, waterbird}" plus "{water, land}": 56.8→56.6±2.6; Waterbirds ViT-B/32 with "a photo of a bird on {water, land} background": 45.5→43.9±4.2). The paper's emphasis on prompt sensitivity (Table 2, Table 3) is appropriate, but the claim of "consistent improvement" (line 45) should be qualified.

- **Combination with DRO methods (Table 8) shows mixed results**: The sequential adapter approach ($I \triangleright A^1 \triangleright A^2 \triangleright T$) yields modest improvements on CelebA (e.g., χ²-DRO worst-case from 72.0±9.6 to 73.8±6.8) and no improvement on Waterbirds. The authors acknowledge this, but the experiment as presented does not clearly strengthen the contribution.

### Trivial
None.

## Nice-to-Haves

- Include additional language-guided debiasing baselines beyond OrthCali (e.g., FairCLIP, Zhang et al. 2023) to better situate L-DRO within its natural sub-area.
- Add a t-SNE visualization or subgroup-accuracy analysis on the debiasing prompt itself to validate that the entropy objective produces the intended effect (uniform predictions across subgroups).
- Test with three or more subgroup partitions simultaneously to probe the method's limits with multiple confounding attributes.
- Report zero-shot results with standard deviations (10 seeds, consistent with L-DRO reporting) to enable proper statistical comparison.

## Removed Points

- **"Principled connection is hand-wavy" as a fatal weakness**: While the theoretical derivation is indeed heuristic, the paper's core empirical contribution remains valid. The overclaim affects framing but does not invalidate results. Moved to Major weakness.
- **"Domain-oblivious contradicts requiring the attribute"**: The paper clearly defines "domain-oblivious" as lacking instance-wise labels (line 41). The critic's interpretation differs from the paper's own definition. The substance (method requires attribute knowledge) is kept as a Minor weakness; the terminology contradiction claim is removed as it reflects a mismatch between the critic's and the paper's definitions.
- **"Table 8 notation is confusing"**: The notation $I \triangleright A^1 \triangleright A^2 \triangleright T$ is explained in the table footnote. The criticism is a clarity nitpick rather than a substantive issue. Removed.
- **"Should include more baselines like FairCLIP"**: This is a suggestion for strengthening, not a core weakness. Moved to Nice-to-Haves.
- **Strength Finder's generic strengths**: All claimed strengths had specific supporting evidence, so none were filtered.

## Novel Insights

The reviews collectively highlight a tension that the paper itself does not fully resolve: L-DRO's practical value comes from its simplicity and stability, not from a new theoretical advance. The strongest argument for the method is not the dubious DRO connection but the empirical demonstration that a single entropy-consistency objective on known subgroup descriptions yields training-stable improvements across diverse prompts and data regimes. This suggests the paper's natural audience is practitioners deploying CLIP who can identify a confounding attribute—not researchers seeking new DRO theory. The reviews also converge on the observation that the training stability result (Figure 1) is under-discussed relative to its practical importance; it is arguably the paper's most novel empirical finding.

## Suggestions

1. **Reframe the contribution away from DRO theory and toward prompt-based debiasing.** Position L-DRO as a lightweight, language-guided debiasing method for CLIP that improves worst-case accuracy when the practitioner knows and can describe the confounding attribute. The DRO comparisons can remain as baselines but should be accompanied by a clear statement of the information asymmetry.

2. **Replace the heuristic derivation (Eq. 4–5) with an empirical motivation.** For example, show that CLIP's zero-shot predictions on the debiasing prompt correlate with worst-case errors, and that making these predictions more uniform via the adapter improves worst-case accuracy. This would provide an intuitive, empirically grounded rationale without overclaiming theoretical rigor.

3. **Add uncertainty estimates for all zero-shot baselines** by running the zero-shot evaluation with the same 10 random seeds (or, since zero-shot is deterministic w.r.t. seeds, provide confidence intervals via bootstrapping on the test set).

4. **Explicitly state the assumption cost:** "L-DRO assumes the practitioner knows the attribute causing the sub-population shift and can write a text prompt that describes it. This is a form of domain knowledge, distinct from instance-wise subgroup labels." This would clarify the method's applicability conditions.

## Score and Decision

The paper presents a practically useful method with solid empirical support, including consistent worst-case accuracy gains and a striking training stability advantage over DRO baselines. However, its framing overclaims theoretical grounding (the "principled connection" is heuristic) and understates the information advantage L-DRO enjoys over the DRO methods it is compared against. These are framing issues, not fatal methodological flaws. The core empirical contribution is real, reproducible, and valuable. With honest reframing and additional uncertainty reporting, the paper would be a solid contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>