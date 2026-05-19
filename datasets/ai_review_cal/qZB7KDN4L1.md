- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

Subject-Diffusion proposes a unified zero-shot framework for open-domain personalized text-to-image generation. It requires only a single reference image per subject, supports both single- and two-subject generation without test-time fine-tuning, and is trained on a newly constructed large-scale dataset (SDD: 76M images, 222M entities) built via an automatic pipeline (BLIP-2 → Grounding DINO → SAM). The method integrates coarse location control, fine-grained patch features via an adapter, and a cross-attention map loss to handle multiple subjects.

## Strengths

1. **First framework targeting open-domain two-subject zero-shot personalization.** The paper tackles a problem no existing zero-shot method claims to solve: generating two distinct subjects from one reference image each, without fine-tuning. Table 2 shows Subject-Diffusion (zero-shot) outperforms fine-tuning methods DreamBooth (DINO 0.506 vs. 0.430) and Custom Diffusion (0.506 vs. 0.464) on two-subject DreamBench, a result no prior zero-shot approach reports. (Section 4.2, Table 2)

2. **Large-scale structured dataset (SDD) with automatic construction pipeline.** The SDD dataset (76M images, 222M entities, 162K classes) is substantially larger than OpenImages (1M images) and is built with a replicable pipeline. Ablation (Table 4, rows a vs. b) directly validates its impact: training on SDD improves DINO from 0.664→0.711 (single) and 0.491→0.506 (two-subject) over training on OpenImages. (Section 3.1, Figure 2, Table 4)

3. **Strong single-subject fidelity among zero-shot methods.** On DreamBench, Subject-Diffusion achieves DINO 0.711, outperforming all zero-shot baselines (ELITE 0.621, BLIP-Diffusion 0.594, IP-Adapter 0.667) and even exceeding the fine-tuning method DreamBooth (0.668). (Table 1)

4. **Attention map control loss demonstrably improves two-subject generation.** Ablation (Table 4, rows a vs. f) shows this loss increases two-subject DINO from 0.500→0.506 and CLIP-T from 0.302→0.310, with a well-motivated mechanism: penalizing deviation between cross-attention maps and ground-truth segmentation masks. (Section 3.3, Equation 2, Table 4)

5. **Systematic ablation study.** Table 4 provides a full ablation for both single- and two-subject settings across six components (dataset choice, location control, box coordinates, adapter layer, attention map control, image CLS feature), with each removal producing measurable degradation. (Section 4.3, Table 4)

6. **Human image generation surpasses domain-specific methods in ID preservation.** On FastComposer's human evaluation protocol, Subject-Diffusion achieves ID preservation 0.605, outperforming FastComposer (0.514) and IP-Adapter (0.520) despite not being trained on domain-specific portrait data. (Table 3)

## Weaknesses

### Fatal

None.

### Major

1. **Missing zero-shot baselines for two-subject generation.** The paper claims to be the first zero-shot method for two-subject generation (Section 1, contribution ii) but Table 2 compares only with fine-tuning methods (DreamBooth, Custom Diffusion). It does not compare with or discuss why existing zero-shot approaches capable of accepting multiple image prompts (e.g., IP-Adapter) cannot be applied to the two-subject setting. Without this comparison or a clear justification for its absence, the paper's central uniqueness claim is not convincingly supported. To substantiate or appropriately moderate the "first" claim, the authors should either (a) include zero-shot two-subject baselines or (b) explain in detail why such comparison is infeasible.

### Minor

1. **Quantitative results lack error bars.** All metrics in Tables 1–4 and the ablation are reported as point estimates without variance, confidence intervals, or significance tests. Given the stochasticity of diffusion sampling, the DINO gap between Subject-Diffusion (0.711) and IP-Adapter (0.667) — or the box-coordinate ablation anomaly (row d: DINO improves from 0.711→0.732 for single-subject) — may not be significant. While single-run evaluation is standard in this field, the paper would be strengthened by reporting variance over multiple seeds or sampling runs.

2. **Fidelity–editability trade-off acknowledged but not characterized.** The user study (Table 5) shows Subject-Diffusion has high ID preservation (3.47) but lower prompt consistency (2.27) than IP-Adapter (2.32) and ELITE (2.53). Similarly, in Table 3, prompt consistency (0.228) trails FastComposer (0.243). The paper mentions this trade-off but does not explore how it could be controlled (e.g., by varying λ_attn or the interpolation parameter α). Characterizing a Pareto frontier would turn the observed imbalance from a limitation into a controllable feature. (Sections 4.4, 5)

3. **Box-coordinate ablation anomaly under-explored.** In Table 4 row (d), removing box coordinates *improves* single-subject DINO from 0.711→0.732 and CLIP-I from 0.787→0.810. The paper offers a plausible post-hoc explanation ("information becomes overly redundant") but does not explore whether an adaptive scheme (using box coordinates only when subjects > 1) would improve results or whether this regression is within noise range (see Minor 1). (Section 4.3, Table 4)

4. **BLIP-Diffusion excluded from human generation experiments without explanation.** Table 3 (human generation) includes FastComposer, IP-Adapter, and fine-tuning methods but omits BLIP-Diffusion, which is a zero-shot method cited elsewhere in the paper. The omission is not justified. (Table 3)

### Trivial

- Table 1 caption states "Boldface indicates the best results of zero shot approaches evaluated in Dreambench." IP-Adapter's CLIP-I (0.813) is correctly bolded as the best zero-shot CLIP-I, but this formatting is slightly inconsistent — a reader might expect Subject-Diffusion's CLIP-I to also be bolded since it's the authors' method. The caption could be clarified.
- The paper references "sophisticated filtering strategies" (Section 3.1) for the SDD dataset but provides no specifics on their nature (e.g., resolution thresholds, mask quality criteria, class coverage).

## Nice-to-Haves

- Investigate adaptive application of box coordinates (conditional on number of subjects > 1) based on the observed single-subject regression in the ablation.
- Explore the Pareto frontier of the fidelity–editability trade-off by reporting metrics across a sweep of λ_attn or α values.

## Removed Points

These points were flagged in the input reviews but are removed for the following reasons:

- **IP-Adapter "explicitly demonstrates multi-concept generation" (Harsh Critic):** This is an assertion about IP-Adapter's capabilities that cannot be verified from the paper under review. The paper does not discuss whether IP-Adapter supports two-subject generation from separate reference images. The underlying concern (missing two-subject zero-shot baselines) is retained as Major weakness #1, but the specific claim about IP-Adapter's multi-concept capability is removed as unverifiable.
- **Reproducibility: dataset/model release (Harsh Critic):** Per the rules, criticisms questioning the release status of cited datasets or models are removed.
- **Inference hyperparameters not reported (Harsh Critic):** Per rules, undisclosed hyperparameters are considered a reproducibility nitpick and removed.
- **Table 1 bolding confusion (Harsh Critic):** IP-Adapter's CLIP-I (0.813) *is* bolded in Table 1, consistent with the caption. The criticism is factually incorrect.
- **"The 'first' claim is invalid because IP-Adapter satisfies the four conditions" (Harsh Critic):** This presumes facts about IP-Adapter's capabilities that are not established in the paper. The underlying concern about missing zero-shot two-subject baselines is retained, but the specific invalidation claim is removed.
- **"Not even a paper" / structural fatal issue framing (implied from Harsh Critic tone):** The paper is a complete, coherent submission with a well-described method, experiments, and analysis. No fatal structural issue exists.
- **Generic strengths from Strength Finder:** No generic strengths were present — all listed strengths are specific and evidence-backed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the need for better two-subject evaluation methodology in the zero-shot personalization space but do not independently generate novel observations about the problem.

## Suggestions

1. **Add zero-shot two-subject baselines** to Table 2. If existing methods cannot be directly applied, explain why clearly and systematically. This is the single most important improvement.
2. **Report confidence intervals or standard deviations** for all quantitative metrics over multiple sampling runs (or multiple seeds) to enable readers to assess the significance of reported improvements.
3. **Characterize the fidelity–editability trade-off** by sweeping λ_attn (Eq. 6) or the interpolation parameter α and reporting DINO/CLIP-T or user-study scores across the range.
4. **Consider adaptive use of box coordinates:** since they hurt single-subject DINO but help two-subject DINO, applying them conditionally based on the number of subjects could improve overall results.
5. **Clarify the "sophisticated filtering strategies"** used for SDD construction to strengthen the dataset contribution.
