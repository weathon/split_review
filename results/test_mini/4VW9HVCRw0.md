## Summary

This paper introduces **Free-Form HOI Generation**, extending hand-object interaction synthesis beyond grasp-centric patterns to diverse non-grasping actions like pushing, poking, and rotating. The contributions are three-fold: **(1)** a new task formulation that breaks the grasp paradigm; **(2)** the WildO2 dataset — 4,414 3D HOI samples reconstructed from internet videos spanning 92 intents and 610 object categories, with multi-level language annotations and 17-part hand segmentation; and **(3)** the TOUCH framework comprising CVAE-based contact prediction, a multi-level conditioned diffusion model with coarse-to-fine feature injection, and a cycle-consistency refinement module. Experiments on WildO2 report improvements over adapted baselines across contact accuracy, physical plausibility, diversity, and semantic consistency.

## Strengths

- **New task and dataset expand the HOI generation frontier.** The paper correctly identifies that existing methods are overly grasp-centric, and the push toward free-form, non-grasping interactions is a timely and valuable direction. WildO2 is the first dataset to provide in-the-wild 3D HOI with this breadth of intents and object categories (92 intents, 610 categories), and the multi-level annotation system (SSCs + DSCs + 17-part hand segmentation) enables finer-grained semantic control than existing alternatives.

- **The multi-level conditioned diffusion design is technically well-motivated and ablated thoroughly.** The coarse-to-fine conditioning — global SSC/geometry in early stages, local DSC/contact features in later stages — is clearly justified and validated by ablation (Table 2: removing multi-level structure drops P-IoU from 0.728 to 0.525). The ablation is comprehensive, covering contact maps, refinement, cycle loss, multi-level structure, text levels, and text encoders.

- **Quantitative improvements over adapted baselines are consistent across multiple metric families.** TOUCH outperforms ContactGen and Text2HOI on contact accuracy (P-IoU 0.776 vs. 0.620/0.711), physical plausibility (MPVPE 2.97 vs. 5.46/4.69), diversity (Entropy 2.93 vs. 2.85), and semantic consistency (P-FID 4.13 vs. 6.08/15.72). The margins are substantial on MPVPE and P-FID.

- **Out-of-domain generalization is demonstrated qualitatively.** Figure 7 shows plausible hand poses on Objaverse CAD models with verbs outside the training set (e.g., "roll," "pinch," "press"), suggesting the model has learned interaction priors beyond dataset-specific patterns.

- **The automated O2HOI frame-pairing pipeline is practical and scalable.** The strategy of transferring masks from object-only frames via dense matching avoids the geometric inconsistencies of diffusion inpainting and is more scalable than manual completion — a genuine engineering contribution.

## Weaknesses

### Major

- **The evaluation is conducted entirely against a reconstructed ground truth whose quality is unverified against any external 3D reference.** The WildO2 ground truth is produced by the same pipeline (image-to-3D object reconstruction + monocular hand reconstruction + hand-object refinement) that has a 55% success rate and uses known-approximate methods. Every quantitative metric in Tables 1 and 2 (P-IoU, P-F1, MPVPE, PD, PV, P-FID) measures agreement with this pipeline's output, not with ground-truth 3D scans or independently captured data. This means the numbers reflect how well TOUCH reproduces the pipeline's reconstruction *style* — not necessarily real-world physical plausibility. The claim of "physically plausible" interactions is therefore less substantiated than the paper asserts. A cross-dataset evaluation on a lab dataset like GRAB (even a subset of non-grasping interactions) or a user study that compares generated poses against real video frames would significantly strengthen the claims. This is the most serious weakness.

- **Penetration metrics (PD, PV) are reported in the main comparison (Table 1) without conditioning on contact, despite the paper acknowledging they can be misleading when contact rates differ.** The paper explicitly states in Sec. 5.3: "penetration metrics, PD and PV are meaningful only after hand-object contact is established; otherwise, they can be misleading." Since baselines have substantially lower contact accuracy (P-IoU: 0.620/0.711 vs. 0.776), the penetration advantage claimed for TOUCH (PD 0.932 vs. 1.239/1.296, PV 2.67 vs. 4.93/7.37) is difficult to interpret — it could partially reflect the baselines' lower contact rates rather than genuinely superior physics. Reporting these metrics conditioned on contact regions (e.g., only for hands within a threshold of the object) would resolve this ambiguity.

### Minor

- **The dataset size (4.4k samples) is modest for training a multi-level generative model, and the sparsity across categories is a real concern.** With ~48 samples per intent and ~7 per object category on average, data-hungry diffusion models risk overfitting to reconstruction artifacts. While the authors use resampling to address long-tail distributions, there is no analysis of whether model performance degrades for rare object categories or whether generated diversity reflects real-world variation versus memorization of reconstruction patterns.

- **Several implementation details are underspecified, making reproduction difficult.** These include: how the hand-part mask is "initialized from the fine-grained text" T_DSC (Sec. 4.1) — i.e., the mapping from natural language to 17-part hand labels; how ContactGen's coarse hand-part labels were mapped to WildO2's 17-part segmentation; the specifics of the optimization-based post-processing added to baselines; and the convergence/sensitivity of test-time optimization (N_tta iterations). These gaps are addressable but hinder reproducibility.

- **The "firm vs. gentle" contact area comparison (22-25% larger) lacks error bars or statistical significance testing.** Given the small dataset and the qualitative nature of the VLM-generated annotations, standard deviations across multiple runs or per-condition samples would help establish reliability.

- **The out-of-domain generalization (Fig. 7) is shown only qualitatively.** Quantitative metrics (e.g., contact accuracy or penetration on Objaverse samples with human-judged plausibility) would make this claim more concrete.

### Trivial

- Table 2's "✗ L_cyc." label appears to have a typo (missing "c" in "cyc.").

- Some figure captions are figure-descriptions rather than meaningful summaries (e.g., the lengthy captions that describe the figure layout rather than the scientific content).

## Nice-to-Haves

- Validate reconstruction quality and generation against at least one existing lab dataset (e.g., GRAB, OakInk) to ground the "physically plausible" claim in real 3D data.
- Report penetration metrics conditioned on hand vertices that are within a contact threshold of the object, or normalize by contact region size.
- Provide error bars (confidence intervals) across multiple runs for all quantitative metrics, especially VLM scores and user study results.
- Include a breakdown of reconstruction pipeline failures by object/action type and analyze how these affect downstream generation.

## Removed Points

- **Criticism about the ✗ refiner variant having "PV 2.98 — less than even Ours Full (2.67 from Table 1)":** Factually incorrect — 2.98 > 2.67. The numerical comparison is wrong. The broader point that penetration metrics are sensitive to contact rates is valid and is already acknowledged by the paper in Sec. 5.3; this specific erroneous comparison is removed.

- **Criticism that Qwen-7B is not included in the text encoder ablation:** Misreading of the table. The baseline row "Ours(✗ TTA)" uses Qwen-7B; the CLIP/BERT/MPNet rows are ablation variants. Qwen-7B is the comparator, not omitted.

- **"The paper provides no evaluation against real 3D scans, no human study":** The paper does include a perceptual score (PS) from 10 users (Table 1). The concern about evaluation against lab datasets is kept as a major weakness; the claim that no user study exists is false.

- **"The framing of 'grasp-centric' vs 'free-form' is overblown. Prior works like ContactGen explicitly handle non-grasping interactions":** ContactGen generates hand poses conditioned on object geometry and coarse part labels, but its training data (GRAB, InterHand2.6M) is predominantly grasping. The paper's characterization of prior work as predominantly grasp-centric is accurate.

- **"Something-Something V2 dataset... recorded in controlled environments (tables, plain backgrounds)... The claim of 'in-the-wild' is therefore only partially true":** Something-Something V2 contains richly varied daily actions on diverse tabletops. By the standards of the HOI generation community, this constitutes "in-the-wild" relative to lab mocap datasets. The criticism is scope-creep.

- **Reproducibility nitpicks** about undisclosed hyperparameters, trivial implementation details, or artifacts impractical to include: removed per hard rules.

- **Pure formatting/style nitpicks, missing related works, missing appendix content:** removed per hard rules.

## Novel Insights

The most interesting observation to emerge from the reviews is that the paper's core tension — evaluating free-form HOI without a ground-truth 3D reference — is both its main vulnerability and the very reason the dataset is valuable. No existing lab dataset captures the diversity of non-grasping interactions at scale, which forced the authors into an automated reconstruction pipeline. This means the ground truth used for evaluation is the best available proxy, but the metrics may measure fidelity to the reconstruction pipeline's biases rather than to real-world physics. A productive path forward would be to treat the evaluation as a calibration problem: use a small set of high-quality 3D scans (e.g., from GRAB) to measure the pipeline's own reconstruction error, then adjust conclusions about relative method quality accordingly. The ablation study's internal consistency (each component removal causes degradation in contact metrics) partially mitigates the circularity concern, since these relative comparisons are less sensitive to absolute ground-truth quality than the absolute numbers might suggest.

## Suggestions

1. **Validate against external 3D data.** Even a small-scale experiment — e.g., selecting 20-30 interaction types from GRAB that qualify as non-grasping, running the WildO2 pipeline on those, and comparing TOUCH's output against the true mocap data — would transform the evaluation from internally consistent to externally convincing.

2. **Report contact-conditioned penetration metrics in Table 1.** Compute PD and PV only on hand vertices within a distance threshold of the object surface, or report the ratio of penetration volume to contact area. This directly addresses the acknowledged ambiguity.

3. **Clarify the text-to-hand-part-label mapping.** The hand-part mask "initialized from the fine-grained text T_DSC" is the bridge between language and spatial contact prediction. A paragraph describing how this parsing works (rule-based, LLM-extracted, or learned) would substantially improve reproducibility.

4. **Add error bars to the "firm vs. gentle" quantitative claim.** Report per-condition standard deviations across samples to establish whether the 22-25% difference is statistically significant.

5. **Provide a failure-case analysis for the reconstruction pipeline.** The 45% failure rate is never analyzed by object category, action type, or error mode. Understanding which interactions resist reconstruction would inform users about WildO2's coverage gaps and help guide data collection for future versions.

## Score and Decision

**Calibration anchors considered** (from the human review corpus):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| SIGHT (ff3gboFkss) — HOI trajectory generation | 3.00 | Weaker method, no dataset contribution, rejected. TOUCH is clearly stronger on all dimensions. |
| HOIDiNi (mHgaCF2qI5) — Text-driven HOI diffusion | 3.60 | Similar task space but full-body; TOUCH has a more thorough method and dataset contribution, but both share evaluation limitations. TOUCH is stronger. |
| UniHand (upUl6hMYwy) — Unified hand motion model | 5.33 | Accepted poster. Both have strong method contributions but evaluation concerns. Comparable overall quality. |
| SpatialHand (VpsqfCac2B) — 3D object insertion | 6.00 | Accepted poster. Cleaner evaluation pipeline. TOUCH has a more complex task and dataset contribution but weaker evaluation validation. Slightly below. |
| InfBaGel (TeyHNq4WlI) — HOSI generation | 6.00 | Accepted poster. Solid evaluation with scene generalization. TOUCH has comparable methodology quality but less cross-validation. |

The paper makes a genuine contribution — task expansion, dataset construction, and a well-designed method with thorough ablation — but the evaluation is fundamentally limited by reliance on reconstructed ground truth without external validation. This places it below the cleanest papers in the corpus but above clearly rejected ones. The relative comparisons in the ablation are internally trustworthy, but the absolute claims about "physical plausibility" are not fully supported.

**MY FINAL SCORE:** <score>5.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>