Now I have good calibration. Let me synthesize my review. 

**Key comparisons:**
- **HOI-Diff (5.25, Reject)**: most directly comparable — text-driven 3D HOI with diffusion, but reviewers identified serious gaps: neglected hand-object interaction, no physical constraints, insufficient comparisons. TOUCH is clearly stronger on all these dimensions.
- **IHDiff (5.50, Reject)**: first diffusion for interacting hands, but limited novelty and weak evaluation. TOUCH has broader contributions.
- **TapMo (6.50, Accept)**: text-driven motion for skeleton-free characters, new problem + method but evaluation limited to one dataset. TOUCH has comparable novelty plus a new dataset; evaluation more comprehensive.
- **CLoSD (7.50, Accept)**: tighter, more polished integration of diffusion + physics, with stronger experimental rigor. TOUCH is weaker on polish but broader in scope.

Our paper sits between TapMo and CLoSD — better than 6.5 given the dataset contribution, but below 7.5 due to evidential gaps. **Final bracket: 6.5–7.0.**

---

## Summary

This paper introduces the Free-Form HOI Generation task, moving beyond grasp-centric hand-object interaction to diverse non-grasping manipulations (pushing, rotating, etc.) controlled by fine-grained text. The authors construct WildO2, a 4.4k-sample 3D HOI dataset built from in-the-wild videos (Something-Something v2) via an automated reconstruction pipeline, and propose TOUCH, a three-stage framework combining contact-map CVAEs, a multi-level conditioned diffusion model, and a physical refinement step. The work makes a genuine contribution by broadening the scope of HOI synthesis and providing a new dataset resource.

## Strengths

- **Novel task definition with clear motivation**: The paper identifies a real gap — existing HOI generation is almost exclusively grasp-centric — and defines Free-Form HOI generation to encompass the broader range of daily interactions (pushing, poking, rotating, etc.). The motivation in Section 1 is well-articulated and the contrast with prior work is fairly drawn.

- **New dataset fills a real resource gap**: WildO2 provides 4,414 3D HOI samples from in-the-wild videos spanning 92 intents and 610 object categories, with multi-level text annotations (SSCs + DSCs) and fine-grained 17-part hand segmentation. The O2HOI frame-pairing strategy (Section 3.1) is a clever, scalable alternative to diffusion-based inpainting. This dataset directly enables the proposed task.

- **Strong quantitative results with comprehensive ablations**: TOUCH significantly outperforms adapted baselines (ContactGen, Text2HOI) across all reported metrics (Table 1), improving contact accuracy (P-IoU 0.776 vs. ≤0.711) and physical plausibility (MPVPE 2.97 vs. ≥4.69). The ablation study (Table 2) convincingly demonstrates that contact guidance ("✗ hoc." drops P-IoU from 0.728 to 0.492), the multi-level design, and the physical refiner are each essential. The ablation also experiments with multiple text encoders (CLIP, BERT, MPNet, Qwen).

- **Physical refinement with cycle-consistency**: The refiner module (Section 4.3) using self-supervised cycle-consistency loss is well-designed and effective. The ablation confirms removing the refiner degrades contact accuracy from 0.728 to 0.513. The paper also correctly notes that penetration metrics alone can be misleading without contact (the refiner-less variant achieves deceptively low penetration because the hand drifts away from the object entirely).

- **Encouraging out-of-domain generalization**: Qualitative results on Objaverse CAD models (Fig. 7) show plausible interactions for novel objects and verbs outside the training distribution, suggesting the learned priors transfer beyond WildO2's specific objects.

- **Force-related semantic nuance emerges naturally**: The model associates "firm" prompts with larger, denser contact areas and "gentle" prompts with sparser contacts (Fig. 9), quantitatively supported by a 22-25% larger average contact area for firm/tight interactions — a genuinely interesting emergent behavior.

## Weaknesses

### Fatal

None.

### Major

- **No independent validation of dataset quality**: All training labels and evaluation metrics are computed against the pipeline's own pseudo-ground-truth. The reconstruction pipeline involves multiple error-prone stages (image-to-3D, hand pose estimation, camera alignment, contact refinement) and has a 55% automated success rate. While the paper mentions "manual inspection and refinement," it provides no details on what was inspected, how many samples, what error rates were found, or any validation metric (e.g., 2D reprojection error, contact accuracy against human annotation on a subset). Without this, the reader cannot assess how much noise the ground truth contains, which directly impacts the credibility of all reported metrics. This is addressable with a modest manual-annotation study on a small subset.

### Minor

- **Information asymmetry in baseline comparisons**: In Table 1, TOUCH receives both SSCs and fine-grained DSCs as input, while baselines (ContactGen, Text2HOI) receive only SSCs and object meshes. The ablation "✗ T_DSC" partially addresses this (TOUCH without DSCs achieves P-IoU 0.698 vs. Text2HOI's 0.711 — close but slightly behind on contact accuracy, though these numbers are from different tables with TTA disabled in the ablation). The architectural contribution is real and demonstrated by ablation, but the main comparison table conflates method design with input richness. The paper should acknowledge this explicitly rather than leaving it implicit.

- **No quantitative metric for part-level semantic adherence**: A core claim is that TOUCH respects fine-grained part specifications (e.g., "apply [index pad] to exert gentle force on the [handle]"). However, P-IoU and P-F1 measure overall contact overlap with the dataset ground truth, not whether the *specified* hand parts actually make contact. The VLM-assisted score and 10-person user study provide some signal, but the protocol is insufficiently described and neither directly measures part-level adherence. A straightforward metric (e.g., fraction of specified hand-part vertices within contact distance of the object) would directly support the controllability claim.

- **Diversity and VLM metrics insufficiently described**: The diversity metrics "Ent" (entropy) and "CS" (cluster size), and the VLM-assisted evaluation, are mentioned by name only (Section 5.1). No definition, implementation detail, or justification is provided in the main text, making those columns in Table 1 uninterpretable without external knowledge.

- **Limited scale and no quantitative generalization metric**: With 4.4k samples across 610 object categories (avg ~7 per category), the model may overfit to WildO2's reconstruction artifacts. Out-of-domain results on Objaverse (Fig. 7) are qualitative only. The paper acknowledges dataset scale as a limitation, but quantitative generalization metrics (e.g., performance drop on held-out object categories) would strengthen confidence.

### Trivial

- The manual inspection procedure and coverage (Section 3.2) are mentioned only in a single sentence; expanding this in the appendix would improve transparency.
- The 10% condition-dropping strategy (Section 4.2) is stated without ablation, though this is a negligible concern.

## Nice-to-Haves

- Validate the dataset on even 50-100 manually curated samples (e.g., 2D reprojection error, contact-part accuracy vs. human judgment) to establish a concrete quality floor.
- Add a direct part-level adherence metric (fraction of specified hand-part vertices within contact distance) to quantitatively support the controllability claim.
- Report a TOUCH variant conditioned only on SSCs in the main comparison table to cleanly isolate the architectural contribution, or add an explicit caveat about input asymmetry.
- Expand the user study beyond 10 participants with clearer protocol and inter-rater reliability reporting.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Harsh critic: "The baseline comparison is not conditioned on the same information"** — Partially retained as a Minor weakness, but the harsh critic's framing as a fatal confound is too strong. The ablation study shows TOUCH's architecture matters independently of DSCs, and the paper legitimately claims the full framework (including DSC processing) as its contribution. A paper proposing a richer conditioning scheme is not required to retrofit baselines with that scheme to prove its architecture works.

- **Harsh critic: "Scale and overfitting risk"** — Retained as Minor, but the harsh critic's implication that 4.4k samples is inherently insufficient is weakened by the fact that many HOI datasets (GRAB, HOI4D, etc.) operate at similar scales. The concern is reasonable but not disqualifying.

- **Harsh critic: "The global condition dropping (10%) is a minor detail; its effect is not ablated"** — Removed entirely. Ablating every hyperparameter choice is not a standard expectation.

- **Harsh critic: "the refiner's output supervised toward the diffusion denoised pose, or only by the physical loss?"** — Removed. The paper states the refiner is trained with self-supervised cycle-consistency and physical losses (Eq. 7), and the diffusion model is frozen during refiner training (Section 5.1). The relationship is clear enough.

- **Strength finder: "Scalable reconstruction pipeline"** — Retained within the dataset construction strength, but the claim of "high-fidelity" is qualified by the lack of independent validation.

## Novel Insights

The paper's most interesting finding is that a model trained only on static HOI snapshots, without explicit force modeling, naturally learns to associate force-related textual semantics ("firmly," "gently") with contact geometry — producing larger, denser contacts for "firm" prompts and sparser ones for "gentle" prompts, with quantitatively measurable differences (~22-25% contact area variation). This emergent semantic grounding of physical concepts in contact geometry is a genuinely novel observation that could inform future work on language-guided physical interaction modeling.

## Suggestions

- The most impactful single improvement would be a small manual-validation study on ~50-100 WildO2 samples, directly measuring reconstruction error (e.g., 2D projection IoU against the original video frame, or contact-part labeling accuracy). This would transform the dataset from "asserted quality" to "measured quality" at modest annotation cost.
- The O2HOI frame-pairing strategy is independently useful beyond this paper and could be highlighted more prominently as a contribution for the broader community doing in-the-wild 3D reconstruction.
- Consider reporting per-category or per-intent breakdowns of metrics to reveal where the method excels and where it struggles, which would be more informative than aggregate numbers alone.

## Score and Decision

**Calibration anchors used:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| HOI-Diff (ZYwLfi50GI) | 5.25 | R1 | TOUCH is clearly stronger — explicit hand-object modeling, physical refinement, comprehensive metrics, new dataset |
| IHDiff (nTNElfN4O5) | 5.50 | R1 | TOUCH has broader contributions and more thorough evaluation |
| InterDance (KfkmwYQXWh) | 5.60 | R2 | Similar in having dataset + method contributions; TOUCH more directly addresses its task |
| OmniPhysGS (9HZtP6I5lv) | 6.40 | R2 | Different domain; TOUCH comparable in contribution breadth |
| TapMo (OeH6Fdhv7q) | 6.50 | R2 | Closest anchor — new problem + dataset + method, some evidential gaps. TOUCH has slightly broader scope (dataset is a contribution itself) and more comprehensive evaluation |
| Ready-to-React (mm0cqJ2O3f) | 7.00 | R2 | Stronger experimental rigor than TOUCH |
| CLoSD (pZISppZSTv) | 7.50 | R2 | Clearly stronger — tighter integration, more polished, more rigorous experiments |

**Round 1 bracket:** 5.5–7.5. **Round 2 narrowed:** 6.5–7.0. The paper is comparable to TapMo (6.50) in contribution profile — both introduce a new problem formulation, a new dataset, and a new method with reasonable but not flawless experimental support. TOUCH has the edge in evaluation comprehensiveness and dataset scale/novelty, but shares similar evidential gaps (dataset quality validation, some under-described metrics). It does not reach CLoSD (7.50) in experimental rigor. Score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>