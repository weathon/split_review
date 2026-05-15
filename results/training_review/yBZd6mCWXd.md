Now I have all the information I need. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal

### Major

### Minor

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me construct each section carefully.

Here is my analysis of what to keep, remove, weaken:

**REMOVE (hard rules):**
1. RKD "illegible" criticism (Critical Issue 4) — "Keoi eoi" is a PDF parsing artifact. Hard rule says remove criticisms about garbled text.
2. Missing OV-3DET comparison — the paper discusses it as related work and explains difference. Asking for a baseline not in the paper's scope.
3. Missing Appendix/proofs references — hard rule.
4. Formatting nitpicks.

**WEAKEN (soft rules):**
1. mAP@0.25 threshold — The paper follows the established convention in this sub-field (Zhao & Lee 2022, Zhao et al 2022, Liang et al 2023). Not a weakness at all in context.
2. No variance/CI — Not standard for single-run benchmark evaluations in this field.

**KEEP:**
1. **Undisclosed 2D teacher** — The paper never specifies which 2D teacher generated pseudo labels for Tables 1 and 2. If it's Faster R-CNN trained on SUN RGB-D 2D annotations, the "cost-free" claim is misleading. This is a Major weakness.
2. **SDCoT adaptation undocumented** — "We modify the training of SDCoT to fit our weakly incremental learning setting" with zero description of how. Invalidates interpretability of that comparison. Major weakness.
3. **PRF generalization not validated on novel classes** — Minor, since ablation shows +3.25% improvement.
4. **CKT failure mode analysis** — Minor/nice-to-have.

Now let me also check the Strength Finder output:

**Strength Finder claims:**
1. First formalization of WI3D — valid, supported by abstract and intro.
2. Strong quantitative gains over prior methods — valid, supported by Table 1/2 numbers.
3. Pseudolabel noise analysis and PRF — valid, supported by Table 3/4.
4. Robustness to different 2D teachers — valid, supported by Table 5.
5. Cross-modal knowledge transfer via bipartite matching — valid, supported by Table 6.

These all seem reasonable. I'll keep the strengths that are specific and evidence-backed, drop any generic ones.

Let me now write the review.Here is my consolidated meta-review.

---

## Summary

This paper introduces Weakly Incremental 3D Detection (WI3D), a task that extends a 3D detector to novel object classes using only 2D visual prompts (bounding boxes from off-the-shelf 2D detectors) rather than costly 3D annotations. The authors propose a framework with three components: (1) a class-agnostic Pseudo-label Refinement (PRF) module that denoises coarse 3D boxes projected from 2D predictions, (2) Cross-modal Knowledge Transfer (CKT) via bipartite matching for feature-space supervision, and (3) Reweighting Knowledge Distillation (RKD) to mitigate catastrophic forgetting. Experiments on SUN RGB-D and ScanNet under several incremental settings show consistent improvements over baselines.

## Strengths

- **Novel task formulation.** WI3D is a well-motivated and practically relevant problem that combines weakly-supervised 3D detection with class-incremental learning. The paper clearly articulates why this setting matters (eliminating 3D annotations for novel classes) and what the major challenges are (pseudo-label noise, catastrophic forgetting without base-class 3D annotations). The paper correctly positions itself as the first attempt at this specific task formulation.

- **Clear identification and targeted mitigation of pseudo-label noise sources.** Section 3.1 and Figure 2 identify three concrete noise types (Projection Migration, Scale Ambiguity, Overlapped Boxes) arising from projecting 2D boxes into 3D. The PRF module is directly motivated by this analysis, and the ablations (Tables 3, 4) confirm that PRF provides +3.25 mAP on novel classes over coarse pseudo labels—validating that the noise analysis translates into measurable improvement.

- **Robustness across different 2D teachers is explicitly demonstrated.** Table 5 tests the framework with three distinct 2D teachers (Faster R-CNN, Ground Dino, 2D Oracle) and shows consistent gains across all of them, including +9.49% on novel classes with the zero-shot Ground Dino. This supports the claim that the approach is not tied to a specific off-the-shelf model.

- **Bipartite matching for cross-modal alignment is technically sound and ablated.** The paper identifies that naive one-to-many feature assignment actually hurts performance (−0.35% in Table 6) due to occlusion-induced noise, then proposes bipartite matching that yields +1.43% over the no-CKT baseline. This ablation cleanly separates the contribution of the matching strategy from the effect of adding more supervision.

## Weaknesses

### Major

- **The 2D teacher used for the main experiments (Tables 1 and 2) is never disclosed.** The paper tests three different 2D teachers (Faster R-CNN, Ground Dino, 2D Oracle) in Table 5 but never states which one generated the pseudo labels for the headline results in Tables 1 and 2. This omission makes the primary numbers uninterpretable. If the main experiments use Faster R-CNN trained on SUN RGB-D's 2D bounding-box annotations, then the teacher is not "cost-free" as claimed (lines 12, 54)—it requires 2D instance annotations. If Ground Dino (zero-shot) was used, that should be stated explicitly. Without this specification, the reader cannot assess whether the reported 51.52 mAP_base and 41.65 mAP_novel reflect a fair, cost-effective setting.

- **The SDCoT baseline adaptation is completely undocumented.** The paper states (line 161): "Additionally, we modify the training of SDCoT (Zhao & Lee, 2022) to fit our weakly incremental learning setting." No further details are provided about how SDCoT was modified—which components were kept, how pseudo labels replaced 3D annotations, whether the co-teaching structure was preserved, etc. SDCoT is a fully-supervised method requiring 3D annotations for novel classes. Its behavior when fed coarse or refined pseudo labels is unpredictable without specifying the adaptation. The numbers in Tables 1 and 2 ostensibly show that the proposed method surpasses SDCoT, but without understanding how SDCoT was adapted, this comparison carries no scientific weight. The paper's strongest quantitative claim ("surpass prior arts") rests partly on this opaque comparison.

### Minor

- **PRF generalization to novel classes is not directly validated.** The PRF module is trained on base classes and applied to novel classes without explicit analysis of whether the learned refinement actually transfers across object shapes (e.g., small vs. large, cubic vs. elongated objects). Table 3 shows a +3.25% aggregate improvement on novel classes, but a per-class breakdown or an analysis of IoU improvement (coarse vs. refined) on held-out novel-class ground truth would substantially strengthen the class-agnostic transfer claim.

- **CKT matching coverage is not analyzed.** The CKT module relies on bipartite matching between 3D proposals and 2D detections. If the 2D teacher misses an object (due to occlusion, small size, or class not in its vocabulary), that object receives no feature-level supervision. The paper does not report what fraction of novel-class objects are successfully matched, nor how matching failures affect downstream detection. This would help the reader understand the limits of the approach.

- **The "cost-free" claim is inconsistently scoped.** The paper calls the 2D teacher "cost-free" (lines 12, 54), but the robustness experiments (Table 5) include Faster R-CNN trained on SUN RGB-D 2D annotations—which requires supervised 2D bounding-box annotations. Only Ground Dino is truly zero-shot. The paper should clarify what "cost-free" means in context and state clearly which setting was used for main results.

### Trivial

- None beyond the points already listed.

## Nice-to-Haves

- **Additional IoU thresholds.** The paper uses mAP@0.25 following the convention of prior work in this sub-field (Zhao & Lee 2022; Zhao et al. 2022; Liang et al. 2023). While this is standard, reporting mAP@0.5 or at least showing recall/precision curves would address concerns that the refinement produces tight boxes rather than loose approximations that happen to score well at 0.25 IoU.

- **Comparison with an incrementally-adapted version of OV-3DET.** OV-3DET (Lu et al., 2023) is the closest weakly-supervised 3D detection method that also uses 2D-generated pseudo labels, though for open-vocabulary rather than incremental detection. Adapting it to the incremental setting (e.g., by adding knowledge distillation on base classes) would further isolate the paper's contribution.

- **Variance or confidence intervals.** Given the relatively small validation sets (312 samples for ScanNet), reporting run-to-run variance would help assess the reliability of the reported improvements.

## Removed Points

These points were flagged by the harsh critic but are removed per the meta-review guidelines:

- **"RKD formulation is illegible / Keoi eoi garbled"** — The garbled text "Keoi eoi" (line 117) is a PDF parsing artifact, not an author error. The hard rules mandate removing criticisms about broken characters or garbled text. The general idea (α_i depends on proposal objectness) is conveyed.
- **"No justification for mAP@0.25 threshold"** — The paper explicitly follows the established convention in the class-incremental 3D detection sub-field (Zhao & Lee 2022; Zhao et al. 2022; Liang et al. 2023). Criticizing a field-standard metric is not a valid weakness.
- **"Missing comparison with OV-3DET"** — This asks for an experimental scope extension into a different task setting (open-vocabulary → incremental) that the paper does not claim to address. The paper discusses OV-3DET as related work and explains the difference.
- **"Formatting/style nitpicks"** — Removed per hard rules.
- **"Typos, grammar, whitespace issues"** — These are parser artifacts, not author errors.

## Novel Insights

The key takeaway that emerges from the reviews beyond the paper's own claims is that the paper's experimental framing suffers from a transparency gap: two critical pieces of information needed to interpret the main results are missing (which 2D teacher was used, and how SDCoT was modified). This is unusual because the paper is otherwise thorough in its ablations (PRF, CKT, RKD are each ablated cleanly) and the framework components are well-motivated. The disconnect is between the careful component-level analysis and the opaque setup for the headline comparisons. This suggests that the paper's contributions are likely real but presented in a way that prevents the reader from fully crediting them.

## Suggestions

1. **Explicitly state the 2D teacher used in each table.** Add a footnote or column to Tables 1 and 2 specifying which 2D detector generated the pseudo labels. If it varies across settings, state why. This is the single most important clarification.

2. **Describe the SDCoT adaptation in detail.** Provide a paragraph in the experimental section explaining how SDCoT was modified to accept pseudo labels instead of ground-truth 3D annotations. If the adaptation is nontrivial, consider adding an appendix with the modified training procedure.

3. **Add a per-class performance breakdown for novel classes.** This would directly validate the class-agnostic transfer claim of PRF and reveal whether certain shapes or sizes benefit less from refinement.

4. **Report the fraction of novel objects successfully matched by CKT.** A simple coverage statistic (e.g., percentage of ground-truth novel objects that are matched with a 2D detection) would help the reader understand the method's limitations.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>