I have verified all reviewer claims against the paper content. Let me now write the final consolidated review.

---

## Summary

GDrag proposes a training-free, task-aware framework for interactive point-based image editing that addresses two ambiguity problems: **intention ambiguity** (unclear editing goals) and **content ambiguity** (distortion of target regions). The paper defines three atomic editing tasks (relocation, rotation, non-rigid transformation), each with closed-form dense trajectory equations (ADT), and introduces a self-adaptive motion supervision method (SMS) that jointly optimizes latent feature biases and point-wise LoRA scaling maps. GDrag achieves state-of-the-art results on DragBench (LPIPS 0.0915, mean distance 26.49) with 60.33% human preference over four strong baselines.

## Strengths

- **Explicit task taxonomy with formalized trajectory equations.** The paper defines three atomic manipulations (relocation, rotation, non-rigid transformation) and provides closed-form dense trajectory equations (Eqs. 1–3) for each. This is the first optimization-based interactive editing framework to explicitly model editing intentions, directly targeting the stated problem of intention ambiguity. The trajectories are derived from the segmentation mask and handle points via principled geometric reasoning.

- **Self-adaptive motion supervision (SMS) with optimizable scaling maps.** Instead of a single global LoRA trade-off scalar used in prior methods, SMS jointly optimizes latent biases **b** and point-wise scaling maps **s** (Eq. 8). The paper reports task-specific ρ values and shows SMS enables fine-grained feature transformations. This is a concrete methodological improvement over single-scale approaches.

- **State-of-the-art quantitative and human-evaluated results.** GDrag achieves the lowest LPIPS (0.0915) and mean distance (26.49) on DragBench against DragDiffusion, DragonDiffusion, FreeDrag, and DragNoise (Table 2). A human preference study with 20 volunteers and 30 questions shows 60.33% prefer GDrag — a large margin over the best competitor (~20%). These results provide direct evidence for the claimed improvements.

- **Principled task-aware point tracking that avoids drift.** GDrag moves dense points only along precomputed task-aware trajectories (end of Section 3.3), rather than searching neighboring areas for handle-point positions as in prior methods. This clean design leverages the reliability of ADT trajectories and is explicitly contrasted with the drifting problem in prior work.

## Weaknesses

### Fatal

None.

### Major

- **Rotation trajectory estimation is underspecified for reproducibility.** The ADT method for rotation (Section 3.2, Eq. 2) describes fitting an ellipsoid ℰ to the target: "we first place ℰ near the center of the target, of which the axis lengths and angles can be adjusted to coarsely cover the target." No algorithm is provided for how the ellipsoid's axis lengths, orientation angles, or placement are determined automatically from the segmentation mask and handle points. The phrase "can be adjusted" leaves ambiguity about whether this step is manual or automated. Since rotation is one of only three atomic tasks and the paper specifically claims ADT addresses the ill-posedness of 2D lines for 3D deformations, the absence of a concrete, implementable procedure is a reproducibility gap. The paper should clarify whether this is automatic (and if so, provide the algorithm) or describe the interactive procedure if manual.

### Minor

- **Loss weight β is not reported.** The loss function (Eq. 9) contains a task-specific weighting factor β balancing ℒ_align and ℒ_smooth, described as "another task-specific parameter" (line 142). Unlike ρ and λ, β values are never reported for any task. This omission hinders exact reproducibility, though the qualitative trends are unlikely to change given the paper's strong overall results.

- **τ is listed but not defined.** Line 172 lists τ = 35 alongside L and N, but τ is never defined in the method section. It likely corresponds to the maximum denoising step T (line 94), but this is not explicitly stated.

- **No discussion of failure cases or limitations.** The paper does not include a limitations section or discuss failure cases (e.g., when the SAM segmentation mask is inaccurate, when the ellipsoid fitting for rotation fails, or when user task specification is ambiguous). Including such discussion would strengthen the paper's rigor and help users understand the method's boundaries.

### Trivial

- Several parameters use calligraphic font in the implementation section (ℒ, 𝒩) that differs from the notation in the method section (L, N), causing minor confusion on first reading.

## Nice-to-Haves

- An ablation study comparing the random time-step sampling strategy (N random steps per movement) against alternatives (e.g., uniform coverage of the diffusion range, fixed schedule of steps, adaptive selection) would strengthen the claim that random sampling best exploits latent features at different granularities. The current ablation studies (Section 4.3, results in an embedded figure) isolate ADT and SMS as components but do not specifically test this design choice.

- A parameter sensitivity analysis for key hyperparameters (ρ, β, λ) on a subset of DragBench would increase confidence in the method's robustness, given the number of introduced parameters.

## Removed Points

The following points from the reviewers were identified as invalid or inapplicable and are surfaced here for transparency but not included in the final assessment:

- **"Ablation studies are absent from the provided text."** The paper's Section 4.3 clearly states "We conduct ablation studies on the two key components of our framework, i.e., ADT and SMS" and the results are embedded as a figure. The apparent absence is a PDF text-extraction artifact, not a missing section. **Removed per rule:** parser artifacts should not be treated as paper weaknesses.

- **"No ablation or comparison to alternative sampling strategies for random time-step selection."** This concern cannot be verified from the text alone since the ablation studies are in an embedded figure; it is listed in Nice-to-Haves as a suggestion rather than a confirmed weakness.

- **Strength Finder's "Detailed implementation and parameter specification."** This strength conflicts with the verified weakness that β is not reported and τ is not defined. Per the rule that "when a strength and weakness disagree, the weakness wins," this strength is moved here. The paper does report many parameter values (L, N, learning rates, λ, r, k, task-specific ρ), but the omissions of β and the definition of τ prevent the claim of full implementation detail.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify the ellipsoid fitting algorithm.** Provide a concrete, reproducible procedure for automatically fitting the ellipsoid from the segmentation mask and handle points (e.g., fit an ellipse to the mask, interpret as the orthographic projection of an ellipsoid, and set the third axis proportionally). If the fitting involves manual adjustment, state this explicitly and describe the user interaction.
2. **Report β values for each task** in the implementation details.
3. **Define τ explicitly** (e.g., clarify that τ = T, the maximum denoising step).
4. **Add a limitations paragraph** covering failure cases: inaccurate SAM segmentation, ambiguous task specification by the user, and scenarios where ellipsoid-based rotation approximation may break down.
5. **Consider adding an ablation** comparing random time-step sampling with alternative strategies (e.g., uniform or fixed schedules) to further validate the SMS design choice.

## Score and Decision

The paper presents a well-motivated framework with clear methodological novelty (task-aware trajectories, optimizable scaling maps) and strong empirical validation on DragBench including a human study. The main issues are reproducible — the underspecified rotation trajectory estimation and missing β values — but these are addressable and do not undermine the core contribution. The paper is a solid contribution to interactive point-based image editing.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>