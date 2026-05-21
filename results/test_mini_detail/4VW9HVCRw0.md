Now I have enough information for calibration. Let me write the consolidated review.

## Summary

This paper introduces the task of **Free-Form HOI Generation** — going beyond the well-studied grasping-only paradigm to produce diverse, semantically controllable hand-object interactions (pushing, tipping, pressing, etc.). The authors construct **WildO2**, a dataset of 4.4k 3D HOI samples across 92 intents and 610 object categories, built through an automated pipeline using O2HOI frame pairing and three-stage reconstruction from Something-Something v2 videos. They propose **TOUCH**, a three-stage framework consisting of: (1) contact map prediction via CVAEs, (2) multi-level conditioned diffusion with coarse-to-fine semantic injection, and (3) physical refinement with a cycle-consistency loss. Experiments show TOUCH outperforms adapted grasping baselines, and ablation studies cleanly validate each component.

## Strengths

1. **Novel task and well-motivated paradigm shift.** The paper convincingly argues that existing HOI generation is trapped in a "grasp-centric" paradigm and provides a concrete path toward free-form, semantically controllable interactions. This reframing is timely and opens a meaningful research direction.

2. **Large-scale 3D HOI dataset covering non-grasping interactions.** WildO2 is the first dataset of its kind at this scale (4.4k unique interactions, 92 intents, 610 object categories) with non-grasping actions and 17-part hand segmentation. The automated O2HOI frame pairing and reconstruction pipeline (mask transfer via dense matching, avoiding geometric inconsistencies of inpainting) is a pragmatic technical contribution that makes the dataset feasible to scale.

3. **Comprehensive ablation study.** Table 2 systematically ablates every component: removing contact prediction (hoc.) drops P-IoU from 0.728 to 0.492, removing the refiner drops it to 0.513, removing multi-level conditioning (mul.) drops it to 0.525, and each text level (SSC/DSC) contributes. This is the strongest evidence for the method's design — stronger than the baseline comparisons, and presented with an insightful caveat about penetration metrics being misleading when contact is not established.

4. **Multi-level semantic control is convincingly demonstrated.** The coarse-to-fine injection of global SSCs and local DSCs (Eq. 4–5) is validated both quantitatively (ablation rows showing both text levels matter) and qualitatively (Fig. 8 shows push vs. lift for the same object; Fig. 9 shows force-related semantics reflected in contact area with a 22–25% difference).

5. **Cycle-consistency loss for refinement is well-motivated and effective.** The bidirectional mapping loss (Eq. 7) for enforcing contact consistency is a novel contribution that the ablation confirms as important: removing the refiner degrades P-IoU from 0.728 to 0.513.

## Weaknesses

### Fatal

None.

### Major

1. **"In-the-wild" framing is overstated for Something-Something v2 provenance.** The paper repeatedly describes WildO2 as an "in-the-wild 3D HOI dataset derived from internet videos" (abstract, introduction, Section 3). However, Section 3.1 explicitly states the source is **Something-Something v2**, which is a dataset of *scripted, goal-directed actions* recorded by crowdworkers in relatively controlled settings. This is not equivalent to truly in-the-wild egocentric video like EPIC-Kitchens or Ego4D. While the paper does disclose the source (it is not hiding anything), the "in-the-wild" label misrepresents the nature of the data and sets an expectation the dataset does not meet. This is a framing problem that should be corrected in revision — the dataset's contribution stands on its own merits without this overstatement. The paper should use a more accurate descriptor (e.g., "crowd-sourced daily interactions").

2. **Baseline comparisons are informative but structurally favorable to TOUCH.** ContactGen and Text2HOI were designed for grasping-only settings. The paper adapts them by removing temporal axes and adding an optimization-based post-processing module, but their architectures are fundamentally mismatched to free-form HOI (e.g., ContactGen's coarse part labels do not include dorsal contacts). The large gaps in Table 1 may partly reflect architectural incompatibility rather than pure superiority. The paper's own ablation study (Table 2) is actually the stronger evidence. A simple additional baseline — e.g., nearest-neighbor retrieval from the training set — would help establish a lower bound and demonstrate that TOUCH genuinely generalizes rather than merely interpolating.

3. **Missing analysis of reconstruction success bias (55% yield).** Figure 3a shows only 55% of reconstruction attempts succeed; 31% fail due to "poor estimation." The paper does not analyze whether the successful 55% are systematically different from the failures (e.g., less occlusion, simpler geometries, more stereotypical grasps). If so, WildO2 training and evaluation would overrepresent easier interactions. Since the method is trained and evaluated exclusively on this subset, performance on genuinely hard, occlusion-heavy interactions is unknown. This should be discussed as a limitation.

### Minor

1. **Out-of-domain evaluation on Objaverse is only qualitative.** Figure 7 shows promising results on novel CAD models with unseen verbs, but no quantitative evaluation. Even a small-scale human evaluation (e.g., "does the pose look physically plausible for this object?") on 20–30 samples would significantly strengthen the generalization claim.

2. **VLM and perceptual score (PS) evaluation details are underspecified.** Section 5.1 mentions "VLM assisted evaluation" and a "perceptual score (PS) from 10 users" but does not describe: what questions were posed to the VLM, what rubric users were given, or inter-rater reliability. These metrics are reported in Table 1 alongside objective metrics, making their provenance important for interpretation.

3. **User study size is small (10 participants).** While not invalid, this is worth noting for the PS metric in Table 1.

4. **No analysis of dataset distribution by interaction type.** The Sankey diagram (Fig. 3b) is useful but does not report counts. It would be informative to know what fraction of interactions are non-grasping (e.g., pushing, tapping) vs. grasp-like, and how many samples per intent exist, to understand the dataset's coverage.

### Trivial

None.

## Nice-to-Haves

- **Joint end-to-end training of contact prediction + diffusion.** The current pipeline feeds predicted contact maps into the diffusion model; a joint training objective might improve robustness to contact prediction errors.
- **Failure case analysis in generation.** The paper discusses reconstruction failures but not generation failures (e.g., does the model struggle with small objects? highly articulated actions?). A figure showing failure cases would strengthen the paper's transparency.
- **Clarify how the network handles missing cross-attention inputs** when local features are absent (Eq. 4, where $\mathbf{y}_{\text{loc}}^i = \emptyset$).

## Removed Points

These were identified in the reviewing process but are excluded from the main review for the reasons stated:

1. **"Paper neglects hand-object contact" (implied concern)** — This was raised as a weakness in HOI-Diff's review, not a criticism of this paper. The paper explicitly models hand-object contact with 17-part hand segmentation, so this criticism does not apply.

2. **Missing related works / lack of citations** — As per instructions, I do not mention missing related works as I lack external sources to confirm existence. This is removed from consideration.

3. **Formatting/style nitpicks** — Parser artifacts, not author errors.

4. **Reproducibility concerns about trivial details** (e.g., undisclosed hyperparameters, training log availability) — Removed as these are not substantive.

5. **Criticism that ContactGen/Text2HOI baselines are "set up to fail"** — Weakened and downgraded from a critical issue to a major weakness above. The paper discloses its adaptation and the ablation study provides stronger evidence. The framing as "set up to fail" is too harsh given that the paper does make a good-faith effort at comparison.

6. **Generic speculation about confounders/potential biases** (from the harsh critic's area-based sweep) — Removed when not anchored to specific paper content.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Recalibrate dataset framing.** Replace "in-the-wild" with a more accurate descriptor such as "crowd-sourced daily interactions" or "semi-in-the-wild." The dataset's contribution (scale, diversity of non-grasping interactions, 17-part annotations) is valuable without overstating the "wildness" of its source.

2. **Add a retrieval baseline.** A simple nearest-neighbor approach that retrieves the most similar training interaction given the object mesh and text would establish a lower bound and strengthen the claim that TOUCH genuinely generalizes.

3. **Provide quantitative OOD evaluation.** Even a small human evaluation on Objaverse samples (10–20 per category, rating physical plausibility) would significantly strengthen the generalization claim beyond qualitative examples alone.

4. **Discuss the 55% reconstruction success rate bias.** Acknowledge and analyze whether successful reconstructions are systematically different from failures, and discuss implications for training/evaluation.

5. **Specify VLM and user study evaluation protocols.** Add details about what questions/instructions were used, how scores were computed, and inter-rater agreement for the PS metric.

## Score and Decision

**Calibration protocol:**

**Round 1 (Bracketing):**
- Weak band (<3.5): Retrieved papers scoring 1.5–3.0 on unrelated/weak submissions — clearly inferior to the current paper.
- Mid band (3.5, 7.5): Most relevant anchor is **HOI-Diff** (avg 5.25, Reject) — the closest paper in topic (text-driven 3D HOI generation with modular diffusion design). HOI-Diff was rejected for neglecting hand-object contact (only 8 body joints), missing comparisons, and limited metrics. The current paper is substantially stronger: it specifically models hand-object contact with 17-part segmentation, provides thorough ablations, constructs a new dataset, and produces cleaner results. Also in this band: **Human Motion Diffusion as a Generative Prior** (avg 6.0, Accept Poster) and **EgoExo-Gen** (avg 6.67, Accept Poster).
- Strong band (>7.5): Papers like DreamGaussian (8.5, Oral), DMV3D (8.0, Spotlight) — clearly stronger with larger impact.

**Round 1 bracket: [5.0, 7.0].**

**Round 2 (Narrowing, scores within 4.5–7.5):**
- Lower mid (4.5, 6.0): HOI-Diff (5.25, Reject), Arti-PG (4.75, Withdrawn), Build-A-Scene (5.75, Accept). TOUCH is clearly stronger than HOI-Diff and Arti-PG. Compared to Build-A-Scene (5.75, Accept), TOUCH has a larger scope of contribution (task definition + dataset + framework).
- Upper mid (6.0, 7.5): Think Then React (6.5, Accept Poster), 3DTrajMaster (6.75, Accept Poster), DartControl (6.6, Accept Spotlight), EgoExo-Gen (6.67, Accept Poster). TOUCH offers a stronger novel contribution (new task definition + dataset + framework) than EgoExo-Gen, but its framing issues (overclaimed "in-the-wild," no OOD quantification) prevent it from reaching the 6.5+ tier where papers have cleaner narratives and more complete evaluations.

**Final position:** TOUCH is clearly above HOI-Diff (5.25) but below the clean 6.5+ papers due to addressable framing and evaluation gaps. It sits at **6.0** — comparable to Human Motion Diffusion as a Generative Prior (6.0, Accept Poster) — a solid Accept that makes a genuine contribution with some weaknesses that can be resolved in revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>