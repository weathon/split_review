Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper introduces WI3D (Weakly Incremental 3D object Detection), a new task where a 3D detector learns to detect novel object classes using only 2D visual prompts (from off-the-shelf 2D detectors) rather than costly 3D annotations. The authors propose a framework with three components: a class-agnostic pseudo-label refinement module (PRF) to denoise 2D-to-3D projected boxes, cross-modal knowledge transfer (CKT) with bipartite matching for representation learning, and reweighted knowledge distillation (RKD) for base-class retention. Experiments on SUN RGB-D and ScanNet show consistent improvements over baselines and an adapted version of SDCoT.

## Strengths

1. **Novel and practically motivated task definition.** WI3D replaces expensive 3D annotations for novel classes with cheap 2D visual prompts, targeting a real deployment bottleneck. The task is clearly distinguished from prior class-incremental 3D detection (which requires 3D labels for novel classes) and open-vocabulary 3D detection.

2. **PRF provides clear, measurable gains on novel-class detection.** The pseudo-label refinement module improves novel-class mAP by +3.25% on SUN RGB-D (Table 3). Ablation studies show that both box coordinates and point-cloud context are necessary (Table 4), and the Binary Classification Head adds a further +0.96%, confirming the module's role in mitigating 2D-to-3D projection noise.

3. **CKT with bipartite matching yields meaningful improvements over alternatives.** CKT improves novel-class mAP by +1.43% compared to no feature-level supervision, while a naive "one-to-many" assignment hurts (-0.35%), demonstrating that the bipartite matching design is critical (Table 6).

4. **RKD outperforms prior distillation strategies for base-class retention.** RKD achieves 51.52 mAP_base and 41.65 mAP_novel on SUN RGB-D, surpassing both KL-divergence-based and L2-distance-based distillation (Table 7).

5. **Robustness to diverse 2D teachers is explicitly validated.** The framework works with Faster R-CNN, Ground Dino, and human-annotated 2D boxes (Table 5), with substantial improvements across all teachers (e.g., +9.49% mAP_novel for Ground Dino), showing the approach is not tied to a specific 2D model.

6. **Comprehensive evaluation across two benchmarks and multiple incremental settings.** Results on SUN RGB-D and ScanNet with varying numbers of novel classes consistently show WI3D outperforming fine-tuning, freeze-and-add, and adapted SDCoT (Tables 1-2).

## Weaknesses

### Fatal
None.

### Major
None. The verified issues below are addressable and do not invalidate the core contribution.

### Minor

1. **SDCoT adaptation is underspecified.** The paper states "we modify the training of SDCoT to fit our weakly incremental learning setting" (Sec. 4.2) without describing what modifications were made. Since SDCoT was designed for class-incremental detection with full 3D annotations, the reader cannot determine whether it received the same coarse pseudo labels as WI3D or whether WI3D's PRF refinement was applied. While the reported gap (+7.57 mAP_novel) is large enough to be convincing, this omission weakens the comparison. The authors should describe the adaptation explicitly.

2. **CKT bipartite matching equation contains a likely sign error.** Equation (2) states:
   ```
   min ∑_i ∑_j m_ij * IoU(Project(B_i^3D), B_j^2D)
   ```
   This minimizes the sum of IoU values, which would push matches toward *low* overlap — the opposite of the intended behavior. The standard formulation should either maximize IoU or minimize (1−IoU). The actual implementation almost certainly uses the correct formulation, but the equation as written is mathematically incorrect and could confuse readers.

3. **PRF training process during base training is ambiguous.** The paper trains PRF on base classes with L_PRF = L_box (Sec. 3.5), but does not specify what the *input* coarse boxes to PRF are during this stage. Are they (a) the 2D teacher's projections on base classes, (b) the base detector's own predictions, or (c) ground-truth boxes with noise? These would produce different error distributions, and it matters whether the refinement pattern learned on base classes matches the 2D-to-3D projection errors encountered for novel classes. The authors should clarify this.

4. **No statistical significance or multi-run results reported.** All experiments appear to be single runs. Several ablation differences are small (e.g., PRF w/o BCH vs. full PRF: +0.96 mAP_novel in Tab. 3; RKD vs. prior KD: +1.51 mAP_novel in Tab. 7). While single-run evaluation is common in this area, the specific claim that these differences are stable would benefit from at least 3 runs with error bars.

5. **PRF and BCH generalization to novel classes is supported only indirectly.** The paper claims PRF is "class agnostic" (Sec. 3.3) and applies it to novel classes without direct validation of pseudo-label quality on novel categories. The ablation results (Tab. 3) show that PRF and BCH improve novel-class *detection* mAP, which is indirect but reasonable evidence. More direct analysis (e.g., comparing refined pseudo labels against available ground truth on novel classes) would strengthen the claim, but the current evidence is not negligible.

### Trivial

- Computational cost of the pseudo-label generation pipeline is not reported.
- No discussion of failure cases (e.g., heavily occluded objects producing degenerate pseudo labels).

## Nice-to-Haves

- If the authors' key claim is class-agnostic refinement, a direct evaluation of PRF's output quality on novel classes (e.g., refined-box IoU vs. ground truth on a held-out split) would tighten the argument.
- A version of SDCoT using ground-truth 3D labels for novel classes would provide an oracle upper bound to calibrate the absolute gap to fully-supervised performance.
- Reporting mAP at IoU=0.5 in addition to 0.25 would strengthen the localization evaluation.

## Removed Points

The following points from the reviews are flagged to be removed; treat them with caution:

- **"Garbled text in the CKT projection chain (paragraph beginning '3iDn top ...')":** This is a parser artifact (OCR corruption from the PDF extraction), not an author error. The original submission's text is not available in this format.
- **"BCH precision/recall on novel classes should be reported, or BCH decisions compared against simple heuristics":** While this would be informative, the paper already provides indirect evidence (Tab. 3 shows BCH improves novel-class mAP by +0.96%). The demand for a full precision/recall breakdown is a wishlist item that does not affect the believability of the central claim.
- **"Missing joint-training oracle (3D annotations for all classes) in Table 1":** The paper acknowledges this gap as a limitation in Sec. 5 ("there is still a gap between our results and those obtained using 3D annotations for novel classes"). The oracle is acknowledged rather than missing.
- **"PRF/BCH generalization concern should have been listed as a limitation in Sec. 5":** The paper lists two limitations; the reviewer's suggestion of a third is a presentation preference, not a flaw in the work.
- **"The sign error (minimizing IoU) is likely a writing artifact":** This is retained as Minor #2 above since it is a real mathematical error in the equation as presented, not a parser issue. The reviewer's speculation that it's "likely a writing artifact" does not remove the concern.

## Novel Insights

The reviews converge on a clear picture: this paper defines a genuinely new and useful task (WI3D), proposes a sensible three-component framework, and provides thorough experimental validation. The single most novel observation is that a class-agnostic refinement module trained on base-class 3D annotations can improve 2D-to-3D projected pseudo labels for *novel* classes enough to make weakly incremental 3D detection viable (+3.25% mAP_novel via PRF alone). This suggests that the structural patterns of bounding-box noise from 2D-to-3D projection (migration, scale ambiguity) are sufficiently general across object categories to be learnable from base classes alone — a finding with implications beyond the specific WI3D setting.

## Suggestions

1. **Specify the SDCoT adaptation** — describe what changes were made to fit the WI3D setting (e.g., did it receive the same coarse pseudo labels? Was PRF applied to its training data?). If feasible, add an ablation where SDCoT and WI3D use identical pseudo labels.
2. **Fix the CKT bipartite matching equation** — change "min ... IoU" to "max ... IoU" or "min ... (1−IoU)".
3. **Clarify PRF training inputs during base training** — specify whether the coarse boxes come from the 2D teacher, the base detector, or ground truth with noise.
4. **Add error bars** for main results and key ablations (at least 3 random seeds).
5. **Report the computational cost** of the pseudo-label generation pipeline.

## Score and Decision

The paper tackles a well-motivated and novel problem, proposes a sensible framework with clearly ablated components, and demonstrates consistent gains across two benchmarks. The weaknesses are real but minor — they concern underspecified details, a likely typo in one equation, and the absence of multi-run statistics — none of which threaten the core contribution. This is a solid paper with addressable issues.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>