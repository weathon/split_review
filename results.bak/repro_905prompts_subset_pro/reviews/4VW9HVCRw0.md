Now I have a thorough understanding of the paper and a clear calibration picture. Let me synthesize the final review.

**Calibration Summary:**

Round 1 anchors:
- HOI-Diff (avg 5.25, Reject): Text-driven 3D HOI generation, weaker methodology and evaluation
- IHDiff (avg 5.50, Reject): 3D interacting hands diffusion, limited novelty
- TANGO (avg 8.50, Accept): Co-speech gesture generation, strong but different domain
- CyberHost (avg 7.60, Accept): Audio-driven talking body, different domain

Round 2 anchors:
- InterDance (avg 5.60, Reject): Duet dance dataset + diffusion, closest analog but weaker
- InterMask (avg 6.00, Accept): 3D human interaction generation, comparable scope but less comprehensive
- TapMo (avg 6.50, Accept): Shape-aware motion generation, accepted with some weaknesses
- HandCLR (avg 6.67, Accept): In-the-wild hand pre-training, accepted

Bracket: Round 1 placed TOUCH clearly above 5.5 and below ~8. Round 2 narrowed to roughly 6.0–7.0. TOUCH is more ambitious than InterMask (6.00) with its dataset contribution, more comprehensive than TapMo (6.50) in evaluation, and comparable to HandCLR (6.67) in contribution depth. The dataset validation concern keeps it from reaching higher. **Final score: 6.5.**

---

## Summary

This paper introduces the task of Free-Form Hand-Object Interaction (HOI) generation, which expands beyond grasp-centric generation to encompass diverse daily interactions like pushing, pressing, and rotating. To support this task, the authors construct WildO2, a dataset of 4.4k 3D HOI samples recovered from in-the-wild videos via a semi-automated pipeline, spanning 92 intents and 610 object categories with multi-level semantic annotations. They propose TOUCH, a three-stage framework combining contact map prediction, multi-level conditioned diffusion with coarse-to-fine control, and a self-supervised cycle-consistency refiner. The paper demonstrates strong quantitative results, diverse controllable generation, and out-of-domain generalization.

## Strengths

- **Compelling task motivation and scope expansion**: The paper identifies and addresses a genuine limitation in the HOI generation literature — the grasp-centric paradigm — and proposes a well-motivated extension toward free-form daily interactions that is both timely and significant for AR/VR, robotics, and embodied AI.

- **Strong quantitative results with wide margins**: Table 1 shows TOUCH substantially outperforms ContactGen and Text2HOI across all four evaluation dimensions — contact accuracy (P-IoU 0.776 vs. 0.711/0.620), physical plausibility (MPVPE 2.97 vs. 4.69/5.46), diversity (Ent 2.93 vs. 2.85), and semantic consistency (P-FID 4.13 vs. 15.72/6.08). These margins are convincing.

- **Well-designed ablation study**: Table 2 cleanly isolates the contribution of each component (contact prediction, refiner, cycle loss, multi-level injection, and text encoders). The large drop when removing contact guidance (P-IoU from 0.728 to 0.492) provides compelling causal evidence for the method's design.

- **Fine-grained semantic controllability**: Figures 8–9 demonstrate that the model captures nuanced semantic distinctions — switching between "push" and "lift up" produces meaningfully different hand poses, and force-related terms ("firmly" vs. "gently") yield a 22–25% difference in contact area backed by quantitative analysis on the dataset.

- **Ambitious dataset construction with a principled pipeline**: The O2HOI pairing strategy for mask transfer (avoiding diffusion-based inpainting artifacts) and the three-stage reconstruction pipeline (initialization → camera alignment via differentiable rendering → hand-object refinement with physical constraints) are sensible technical choices. The dataset fills a genuine gap for non-grasping 3D interaction data.

- **Self-supervised cycle-consistency refinement**: The bidirectional contact-surface consistency loss (Eq. 7) is a novel constraint that improves contact accuracy (P-IoU 0.728 vs. 0.513 with refiner removed in Table 2) without requiring extra supervision.

- **Out-of-domain generalization**: Figure 7 shows plausible interaction poses on unseen Objaverse CAD models and for verbs outside the primary annotated intents, suggesting the model does not overfit to WildO2-specific geometries or labels.

## Weaknesses

### Fatal

None.

### Major

- **Dataset ground-truth reliability is not quantitatively validated**: All training labels (contact maps, hand poses, part-level assignments) and evaluation metrics (P-IoU, P-F1, MPVPE) derive from the automated pipeline's output. The paper reports a 55% success rate with 4,414 samples surviving manual inspection, but provides no quantitative evidence that these reconstructions are accurate — no metric on object mesh fidelity, no hand-object alignment error against a verified reference, no user validation of reconstruction quality. The pipeline uses multiple optimization constraints (mask IoU, 2D joint reprojection, ICP, physical losses) that partially mitigate this concern, and the manual inspection stage provides a quality filter. However, for a paper whose primary contributions include a new dataset intended to enable a new task, some validation — even on a small subset — of reconstruction quality would substantially strengthen the foundation on which all downstream results rest. This is not fatal because the pipeline's multi-constraint design and manual curation make systematic errors unlikely to be entirely unconstrained, but it is the paper's most significant limitation.

### Minor

- **Baseline post-processing module is unspecified**: The paper augments ContactGen and Text2HOI with "an optimization-based post-processing module to correct hand poses" for fairness, but provides no details about what this module does or whether it is comparable to TOUCH's refiner. If the baselines received a weaker optimization, the comparison in Table 1 may be uneven. This can be clarified in rebuttal.

- **TTA contribution not isolated from the core model in main results**: Table 1 includes TTA for the full model, while Table 2 (ablation) disables TTA. This is transparent but makes it difficult to assess how much of the gain in Table 1 comes from the generative model versus the test-time optimization. Reporting a "Ours (w/o TTA)" row in Table 1 alongside the baselines would give a clearer picture.

- **Limited user study and under-specified VLM evaluation**: The perceptual score uses 10 participants, which is small but acceptable for initial work. The VLM-assisted evaluation is mentioned but not described in the main text (presumably detailed in the appendix, which was stripped), making it hard to assess its independence.

- **Out-of-domain evaluation is purely qualitative**: Figure 7 shows encouraging generalization but no quantitative metric (even a simple physics-based or user-preference measure) is provided. This limits the strength of the generalization claim.

### Trivial

- Computational cost of the TTA optimization loop (number of iterations, runtime per sample) is not reported, which matters for practical deployment.
- The manual inspection and refinement protocol after the automated pipeline is mentioned but not described; readers cannot gauge the nature or extent of human intervention required.
- The limitations section acknowledges only the static-snapshot nature of the interactions; the dataset reliability concern should also be recognized.

## Nice-to-Haves

- Reporting a version of the main results without TTA alongside the baselines in Table 1 would strengthen the case for the core generative model.
- A small-scale quantitative validation of the dataset (e.g., comparing reconstructed object silhouettes against masked frames, or a human rating study on reconstruction fidelity for ~50 samples) would significantly strengthen the contribution.
- More detail on how the baseline post-processing module was implemented would ensure a fair comparison.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Circular dependence between contact prediction and evaluation" (Harsh Critic Issue 3)**: This is essentially a restatement of the dataset reliability concern. Training and evaluating on the same dataset is standard supervised learning practice; the real issue is whether the labels are accurate, which is already captured under the Major weakness. Removed as duplicate.

2. **"Force-expression analysis is anecdotal"**: The paper provides quantitative analysis (22–25% larger contact area for "firm/tight" interactions on the WildO2 dataset). This is a concrete, numerically-supported finding, not merely anecdotal. Removed as factually incorrect.

3. **"VLM-assisted evaluation not described in enough detail to judge independence"**: The VLM evaluation is described in the paper (Sec. 5.1 "Semantic Consistency, evaluated using... VLM assisted evaluation"). The details are presumably in the stripped appendix. Removed as likely addressed in the full submission.

4. **"The camera alignment loss does not report convergence frequency or hyperparameter sensitivity"**: This is a level of implementation detail that is appropriate for an appendix, not the main paper. Removed as excessive nitpicking.

5. **"Pore Estimation Failure is not explained"**: This is likely detailed in the appendix. Even if not, it's a minor presentation issue about a failure mode label in a pie chart. Removed as formatting nitpick.

6. **"The harsh critic asserts this is a structural/fatal weakness"**: The dataset validation concern is real but not fatal. The pipeline uses multiple orthogonal constraints, includes manual inspection, and the paper is transparent about success rates. The concern is retained as Major rather than Fatal.

## Novel Insights

The paper's contact-map-prediction-as-intermediate-representation design is a genuinely useful insight for free-form HOI: by predicting where contact occurs before generating the pose, the model decomposes the high-dimensional interaction space into a lower-dimensional contact space that is easier to learn. The cycle-consistency refinement (Eq. 7) applying bidirectional nearest-neighbor mapping between hand and object contact surfaces is a simple but effective self-supervised regularizer that could generalize to other contact-rich generation tasks.

## Suggestions

- The highest-impact improvement would be to add a small quantitative validation of WildO2 reconstruction quality — even 50–100 manually verified samples with silhouette IoU or user-rated fidelity would substantially address the dataset reliability concern and could be done within a rebuttal period.
- Report the full model's performance without TTA in Table 1 alongside the baselines so readers can assess the generative model's intrinsic capability.
- Describe the baseline post-processing module in sufficient detail for reproducibility and fairness assessment.

## Score and Decision

**Originality**: High. The free-form HOI generation task is genuinely new, breaking from the grasp-centric paradigm. The O2HOI pairing strategy and three-stage pipeline for in-the-wild dataset construction are novel technical contributions.

**Importance**: High. Expanding HOI generation to diverse daily interactions has clear implications for AR/VR, robotics, and embodied AI. The dataset fills a real gap.

**Claim support**: Good but not fully rigorous. The method's superiority is well-supported by quantitative results and ablations, but the dataset ground-truth reliability — the foundation for all training and evaluation — lacks quantitative validation.

**Soundness**: Generally sound. The method is well-designed with clear motivations for each component. The ablation study is thorough. The main concern is the unvalidated dataset labels.

**Clarity**: Good. The paper is well-organized and the figures effectively communicate the pipeline, dataset statistics, and results.

**Value to community**: High. The dataset, task formulation, and method each represent meaningful contributions. Even with the validation limitation, WildO2 would be a useful resource, and the TOUCH framework demonstrates effective techniques for free-form HOI generation.

**Anchor comparison**: TOUCH is clearly above HOI-Diff (5.25) and InterDance (5.60) in contribution scope, evaluation thoroughness, and result quality. It is stronger than InterMask (6.00) due to its dataset contribution and more comprehensive evaluation. It is comparable to TapMo (6.50) and HandCLR (6.67) — the dataset validation concern keeps it from exceeding these, but the task novelty and methodological contributions are at least equivalent.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>