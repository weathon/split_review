- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 6, 5, 5
Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

The paper proposes "Layout-your-3D," a coarse-to-fine framework for compositional text-to-3D generation guided by a 2D layout (bounding boxes with instance names). The pipeline: (1) generates a reference image from the layout using MIGC, (2) segments/inpaints each instance and reconstructs coarse 3D objects with LGM, (3) arranges them in 3D space via depth information and a DINOv2-based rotation estimation, and (4) performs a two-stage refinement — collision-aware layout refinement (SSDS + feature-level reference loss + tolerant collision loss) followed by instance-wise refinement (adjustable-timestep SDS + smoothness terms). The method claims a 12-minute generation time.

## Strengths

- **Coherent pipeline design with several novel components.** The DINOv2-based rotation estimation (Eq. 3), the tolerant collision loss (Eq. 8, which allows controlled overlap to model natural interactions while penalizing severe intersections), and the adjustable timestep sampling strategy for instance refinement are all technically sound and well-motivated. The ablation in Fig. 6 and Tab. 3 (layout loss) provides empirical evidence that these components contribute: removing the collision loss drops BLIP-VQA from 53.51% to 52.04%.

- **Qualitative results show clear improvement over text-only baselines.** The visual comparisons in Fig. 3 demonstrate that the method produces substantially more reasonable multi-object arrangements than DreamFusion, ProlificDreamer, GaussianDreamer, and LucidDreamer — methods that receive no layout input and predictably fail at compositional generation (blown-out colors, Janus problem, implausible object interactions like a basketball larger than a sofa).

- **Demonstrated downstream flexibility.** The instance customization and object insertion results (Figs. 7–8) show the framework's utility beyond one-shot generation, enabling iterative editing and per-instance stylization with minimal additional effort.

## Weaknesses

### Fatal

None.

### Major

- **Missing comparison against layout-based / compositional methods.** The quantitative and qualitative evaluations compare the method exclusively against text-only, single-object generation methods (DreamFusion, ProlificDreamer, GaussianDreamer, LucidDreamer) that do not have access to layout input. The paper cites COMOGen, GALA3D, GroundedDreamer, and ComboVerse in the related work but never compares final outputs against them. The sole comparison with ComboVerse (Fig. 4 / Sec. 5.3) is limited to the *coarse initialization stage only*, not the final generated scene. Since the paper claims "superior performance compared to the baseline methods" and "advancing the state of the art in compositional generation," the absence of comparisons against methods working on the *same task* (layout-guided or compositional 3D generation) is a significant gap. Without these comparisons, the reader cannot assess whether the pipeline's specific design choices outperform existing layout-based solutions that also use SDS directly.

- **Quantitative evaluation is underspecified and lacks rigor.** The validation set (Compo20) contains only 20 prompts, yet no confidence intervals, variance estimates, or statistical significance tests are reported. The reported metric scores (CLIP-Score, BLIP-VQA, mGPT-CoT) are image-text alignment metrics applied to rendered 3D views, but the paper does not specify which rendered views are evaluated, how many views per scene, whether all objects are visible from the chosen views, or how the metrics are computed for a multi-object 3D scene. More targeted layout-aware metrics (e.g., per-object CLIP on isolated renders, bounding-box IoU, or collision rate) would be more informative for a method whose claim is spatial control.

### Minor

- **Missing implementation details.** (a) The 12-minute generation time is claimed without any breakdown (coarse stage vs. refinement stage, per-scene vs. total) or hardware specification (GPU type). (b) The tolerant collision loss (Eq. 7–8) is described for two instances only; it is not specified how it generalizes to scenes with three or more objects (e.g., summed over all pairs, or computed between each instance and the union of others). (c) The feature-level reference loss (Eq. 5–6) uses "higher layers of DINOv2" but which specific layers is not stated, which matters for reproducibility.

- **Ablation studies are thin.** The ablation on the layout loss (Tab. 3) reports only BLIP-VQA and lacks per-object or spatial metrics. The ablation on timestep sampling (Fig. 6 left) is purely qualitative with no quantitative backup. The ablation on the coarse initialization compares only against ComboVerse and only for the coarse stage, not the final refinement output.

### Trivial

None.

## Nice-to-Haves

- Reporting per-method generation times on the same hardware to substantiate the efficiency claim.
- Including bootstrapped confidence intervals for metric scores given the small (20-prompt) validation set.
- Specifying the rendering protocol used for quantitative evaluation.

## Removed Points

These points were flagged by reviewers but are removed (with justification):

- **"The user study table and metric table are missing from the draft."** — These are included via \input{tables/metric} and \input{tables/user_study} in the original submission and were stripped by the PDF parser. This is not an author error.
- **"The paper compares against methods that are not designed for the task."** — Partially weakened: the comparison against text-only methods is still meaningful as a demonstration of the value of adding layout guidance, and the paper acknowledges (line 272–273) that it uses an additional input. The core issue is the *absence* of comparison against other layout-based methods, which is kept as a Major weakness above.
- **"The evaluation would need to be redesigned from the ground up"** / **"This is a structural flaw that invalidates the central claim."** — Overstated. The paper's contributions (pipeline design, rotation estimation, collision loss, timestep strategy) are independent of the baseline choice. The missing comparisons weaken the evaluation but do not invalidate the core technical contributions. Kept as Major, not Fatal.
- **"The 12-minute timing claim is empty without HW specification."** — Kept as a Minor weakness (missing detail), not a fatal flaw.
- **Strength: "CLIP-Score of 0.328, BLIP-VQA of 53.51%, and mGPT-CoT of 62.62%"** — The 53.51% BLIP-VQA is confirmed from the ablation table; the CLIP-Score and mGPT-CoT numbers come from the stripped \input{tables/metric} and cannot be verified from the extracted text. The qualitative claim of superiority is supported by visual evidence, so this strength is retained without those specific unverifiable numbers.
- **Strength: "Drastic reduction in generation time"** — Kept as stated in the paper's own claims, though the missing hardware breakdown is noted as a minor weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper's approach that the authors themselves have not already articulated. The main insight from the review process is that the paper's evaluation strategy is misaligned with its claims — a gap the authors would need to address — but this is a critical observation about presentation, not a novel technical insight.

## Suggestions

1. **Add quantitative and qualitative comparisons against at least 2–3 layout-guided / compositional methods** (COMOGen, GALA3D, and/or GroundedDreamer) on the Compo20 validation set, using the same metrics. This is the single most impactful improvement.
2. **Report confidence intervals** on the 20-prompt evaluation (e.g., bootstrapped 95% CIs) to establish significance of reported differences.
3. **Specify the rendering protocol used for metric computation** — which views, how many views, whether all objects are visible.
4. **Provide a timing breakdown** (coarse stage vs. layout refinement vs. instance refinement) and specify the GPU hardware used.
5. **Clarify how the collision loss extends to N > 2 objects** (e.g., all-pairwise or per-instance vs. union).
6. **State which DINOv2 layers** are used for the feature-level reference loss.
