Now I have a thorough understanding of the paper and calibration anchors. Let me synthesize the final review.

---

## Summary

This paper introduces the task of **Free-Form HOI Generation**, which extends hand-object interaction synthesis beyond grasp-centric paradigms to encompass diverse daily manipulations (pushing, poking, rotating, etc.). The authors contribute (1) **WildO2**, a 3D HOI dataset of 4.4k samples with 92 intents and 610 object categories, constructed from in-the-wild videos via an automated O2HOI reconstruction pipeline, and (2) **TOUCH**, a three-stage framework with contact map prediction (via CVAEs), multi-level conditioned diffusion (coarse-to-fine injection of global geometry and fine-grained text), and physical refinement with a cycle-consistency loss. Experiments demonstrate strong performance over adapted baselines, with ablations confirming the importance of each component.

## Strengths

- **Novel task formulation fills a genuine gap**: The paper identifies and formalizes a clear limitation in existing HOI generation — the grasp-centric paradigm — and proposes a broader free-form generation task. This is well-motivated (Sec. 1) and backed by a dataset that includes non-grasping actions absent from prior resources. The task definition opens a new direction for the field.

- **WildO2 dataset and O2HOI pipeline are practical contributions**: The automated pipeline (Sec. 3.1–3.2) that pairs object-only frames with interaction frames and transfers masks via dense matching is a clever, scalable alternative to diffusion-based inpainting. The resulting dataset of 4.4k samples across 610 object categories and 92 intents, with 17-part hand segmentation and multi-level language descriptions (Sec. 3.3), provides a valuable resource for the community.

- **Multi-level conditioned diffusion with coarse-to-fine injection is well-designed and well-ablated**: The hierarchical conditioning strategy (Sec. 4.2) — global geometry and SSC features in early diffusion stages, local DSC and contact features in later stages — is architecturally sound. Table 2 shows that removing multi-level structure ("✗ mul.") drops P-IoU from 0.728 to 0.525 and removing fine-grained DSC text ("✗ T_DSC") drops it to 0.698, providing concrete evidence that the design is essential.

- **Physical refinement with cycle-consistency loss addresses a real problem**: The refiner module (Sec. 4.3) tackles hand-object drift, a critical issue in free-form synthesis where grasping priors are absent. Removing the refiner collapses P-IoU from 0.728 to 0.513 (Table 2), convincingly demonstrating its necessity for establishing contact.

- **Semantic controllability and generalization evidence**: The model produces plausible interactions on out-of-domain Objaverse CAD models (Fig. 7) and captures force-related semantic nuances — "firmly" vs. "gently" yields 22–25% larger contact areas (Fig. 9, Sec. 5.4.3). These results go beyond rote memorization.

## Weaknesses

### Fatal

None.

### Major

- **WildO2 reconstruction accuracy is not quantitatively validated**: The entire training and evaluation pipeline depends on the 3D ground truth produced by the reconstruction pipeline (Sec. 3.2). While the pipeline is described and includes manual inspection, no quantitative validation of reconstruction accuracy is provided — no error metrics against annotations or synthetic ground truth on even a small subset. Errors in object-hand alignment, depth scale, or mesh recovery propagate into the "ground truth" contact maps and poses, which means all metrics relying on this ground truth (P-IoU, P-F1, MPVPE) carry unquantified uncertainty. The 55% success rate (Fig. 3a) is from the pipeline's own filtering, not an external accuracy measure. This does not invalidate the work but weakens confidence in the quantitative results and the dataset's claimed quality as a community resource.

### Minor

- **MPVPE as a primary metric creates tension with generative claims**: The paper claims diverse generation, yet MPVPE (Mean Per-Vertex Position Error) penalizes any deviation from the single ground-truth pose. The paper does mitigate this by also reporting diversity metrics (Entropy, CS) and semantic consistency metrics (P-FID, VLM, user study), so the evaluation is not one-dimensional. However, MPVPE sits prominently in Tables 1–2, and its interpretation for a generative model warrants more explicit discussion. The paper would benefit from clarifying that MPVPE measures pose accuracy given a specific text+object conditioning (for which the ground truth is a valid reference), while diversity is assessed separately.

- **Static snapshots have inherent ambiguity for action semantics**: The task generates static hand-object poses conditioned on action descriptions (e.g., "push," "lift"). Some actions are defined by forces and motion dynamics that a single static pose cannot fully disambiguate — a "push" pose may look similar to "touch." The paper acknowledges this limitation (Sec. 6) and does demonstrate that different intents yield visually distinct poses (Fig. 8), but the semantic faithfulness of generated poses to action verbs is not rigorously evaluated (e.g., no forced-choice perceptual study asking users to identify the action from the pose alone).

- **Out-of-domain generation lacks quantitative evaluation**: Sec. 5.4.2 shows only qualitative examples on Objaverse CAD models. While the visual results are promising, quantitative metrics (e.g., FID on a held-out category, contact plausibility scoring, or user ratings) would substantially strengthen the generalization claim.

### Trivial

- The paper says details about O2HOI pair extraction are in the Appendix, but a brief summary of the main approach in the main text would improve self-contained readability.
- The cycle-consistency loss (Eq. 7) assumes nearest-neighbor bijection between hand and object contact surfaces, which is geometrically approximate for area contacts. The paper does not discuss this assumption or its limitations.

## Nice-to-Haves

- A quantitative validation of the reconstruction pipeline (e.g., reconstruction error on a manually annotated subset) would substantially increase confidence in WildO2.
- A forced-choice perceptual study or physics-simulation check for action-semantic accuracy would strengthen the "semantic controllability" claim.
- Ablating the cycle-consistency loss against simpler alternatives (e.g., one-way contact distance) would clarify whether the bijective assumption is beneficial or merely harmless.
- Extending to temporal keyframe sequences would address the acknowledged static limitation.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"MPVPE is fundamentally unsuited to the generative task" (Harsh Critic #1, full severity)**: The claim that MPVPE is structurally inappropriate is overstated. The paper uses MPVPE under "Physical Plausibility," not "Diversity," and separately reports Entropy and CS for diversity plus P-FID and user study for semantic consistency. MPVPE measures whether the generated pose matches the ground truth for a given conditioning — which is a legitimate, though imperfect, evaluation axis. Weakened to a minor concern about metric interpretation.

- **"The baselines ContactGen and Text2HOI are not designed for fine-grained text control; their poor performance is therefore expected"**: The paper explicitly acknowledges that existing methods have not explored fine-grained control (Sec. 5.2) and adapts them with optimization-based post-processing for fair comparison. Using available baselines is standard practice when introducing a new task. This is not a weakness of the paper.

- **"Camera-alignment optimisation uses scale-invariant depth... which introduces an unknown scale factor; this is not discussed"**: Scale-invariant depth loss is specifically designed to handle unknown scale — this is a feature, not a bug. The reviewer misunderstood the technique.

- **"The ablation does not test the method's actual generative versatility"**: The ablation tests component contributions, which is its purpose. Generative versatility is separately assessed in Sec. 5.4.2–5.4.3.

- **"The distinction between grasp-centric and free-form interactions is drawn mainly by the absence of force-closure priors, yet the proposed method itself is heavily contact-driven"**: The paper uses contact as a spatial constraint, which is different from the force-closure grasp prior. Contact modeling for diverse interactions is reasonable and well-motivated in Sec. 1.

- **Strength Finder "Comprehensive evaluation and User Study" kept but weakened**: The evaluation is multi-faceted and reasonably comprehensive for this task, though the user study (10 users) is modest.

## Novel Insights

The paper's most genuinely novel observation is that contact relationships — when predicted explicitly via CVAEs and injected hierarchically into a diffusion process — can serve as a powerful substitute for the grasp priors that dominate prior HOI generation. The ablation results (Table 2) demonstrate this quantitatively: removing contact guidance ("✗ hoc.") causes the largest single-component drop in P-IoU (from 0.728 to 0.492). This suggests that explicit contact modeling, rather than implicit grasp heuristics, is a viable and generalizable path toward free-form interaction synthesis. The finding that LLM-based text encoders (Qwen-7B) substantially outperform CLIP/BERT/MPNet for fine-grained contact-region disambiguation (Table 2, bottom) is also a useful empirical signal for the HOI generation community.

## Suggestions

- Add a small-scale quantitative validation of the WildO2 reconstruction pipeline (e.g., report vertex error on 50–100 manually annotated samples). This would significantly strengthen the paper's central resource contribution.
- Reframe MPVPE in the text as "pose reconstruction accuracy given conditioning" rather than "physical plausibility," and add a sentence clarifying the complementary roles of MPVPE vs. diversity metrics.
- Add a brief discussion of the cycle-consistency bijection assumption and why it is reasonable despite area contacts (or show empirically that it does not hurt).
- For the OOD generation section, report at least one quantitative metric (e.g., contact IoU after manual annotation, or user preference rate) to support the qualitative results.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Comparison to TOUCH |
|---|---|---|
| HOI-Diff (ZYwLfi50GI) | 5.25 | Similar topic (text-driven HOI generation via diffusion), but HOI-Diff neglects hand-object contact modeling, lacks physical constraints, and has weaker evaluation. TOUCH is stronger on all these axes. |
| IHDiff (nTNElfN4O5) | 5.50 | First diffusion model for 3D interacting hands. Criticized for limited novelty and unsatisfactory evaluation. TOUCH has more architectural novelty (three-stage, multi-level conditioning) and more comprehensive evaluation, but shares concerns about dataset dependency. |
| Interactive-Action Image Gen (OWIk5E4lJs) | 5.20 | Different modality (2D image generation) but similar goal of physical priors for interactions. TOUCH is more focused and has stronger task-specific contributions. |
| TF-HOT (gVWEq7LITG) | 3.50 | Hand-object pose tracking from video. Criticized for lack of novelty and unrealistic assumptions. TOUCH is substantially stronger in contribution, evaluation, and clarity. |
| TCIG (RFJGFrMvYj) | 1.50 | Two-stage image generation. Severely lacking in novelty, evaluation, and presentation. TOUCH is incomparably stronger. |

TOUCH sits above the HOI-Diff/IHDiff cluster (~5.25–5.50) due to stronger architectural contributions, a new dataset resource, more comprehensive evaluation, and better ablation evidence. However, the unvalidated dataset reconstruction pipeline and the metric tension between MPVPE and generative claims prevent it from reaching the 7+ range. The paper is a solid contribution with clear novelty and practical value, but has addressable weaknesses that weaken confidence in the quantitative results.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>