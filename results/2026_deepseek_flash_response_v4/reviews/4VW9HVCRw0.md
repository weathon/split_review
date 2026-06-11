Here is my final consolidated review.

## Summary

This paper introduces the task of **Free-Form HOI Generation** — generating hand-object interactions beyond conventional grasping, including non-grasping actions like pushing, poking, and rotating. The authors contribute: (1) **WildO2**, a 3D HOI dataset of 4.4k samples reconstructed from internet videos with fine-grained annotations; (2) **TOUCH**, a three-stage framework combining contact map prediction via conditional VAEs, multi-level conditioned diffusion with coarse-to-fine injection, and physical refinement with a cycle-consistency loss. Experiments on WildO2 show TOUCH outperforms adapted baselines (ContactGen, Text2HOI) across contact accuracy, physical plausibility, diversity, and semantic consistency metrics.

## Strengths

1. **O2HOI mask-transfer strategy enables scalable dataset construction (lines 70-71).** Transferring object masks from unoccluded reference frames via dense matching avoids the geometric inconsistencies of diffusion-based inpainting while being far more scalable than manual cleanup. This design decision is what makes the WildO2 pipeline automated rather than requiring per-sample manual intervention.

2. **Quantitative superiority across all metrics in Table 1.** TOUCH outperforms both adapted baselines on every reported metric — Contact P-IoU (0.776 vs 0.711/0.620), P-F1 (0.844 vs 0.795/0.730), MPVPE (2.97 vs 4.69/5.46), PD (0.932 vs 1.239/1.296), PV (2.67 vs 4.93/7.37), P-FID (4.13 vs 15.72/6.08), VLM score (7.1 vs 6.5/4.8), and perceptual score (8.8 vs 7.5/6.3). This uniform advantage provides direct evidence for the method's effectiveness.

3. **Cycle-consistency loss for disambiguating contact mappings (Eq. 7).** The self-supervised loss enforcing bidirectional consistency between hand-to-object and object-to-hand nearest-neighbor mappings is a principled solution to contact correspondence ambiguity. The ablation (Table 2, "✗ refiner" dropping from 0.728 to 0.513 P-IoU) confirms the refiner module's importance.

4. **Demonstrated semantic nuance in force expression (Section 5.4.3).** The model produces 22-25% larger contact area for "firm/tight" prompts compared to "gentle" ones without explicit force modeling — a genuinely fine-grained capability beyond simple verb-noun matching that prior grasp-centric methods do not address.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation conducted on reconstructed data without external ground-truth validation.** WildO2's "ground truth" is the output of an automated reconstruction pipeline (line 96). The paper provides no validation of reconstruction accuracy against known ground truth — no held-out synthetic data with known geometry, no lab-captured validation set. Only 55% of attempted reconstructions succeed (Fig. 3a); the other 45% are discarded without analysis of systematic bias. All quantitative metrics (contact accuracy, physical plausibility, etc.) measure agreement with these reconstructed targets, not absolute ground truth. While relative comparisons with baselines on the same data remain valid, the core claim of generating "physically plausible" interactions is weakened without external validation of the reconstruction quality.

### Minor

1. **No uncertainty quantification across any experimental result.** Tables 1 and 2 report single scalar values without standard deviations or confidence intervals. Given the stochastic nature of the CVAE (z ~ N(0,I)) and the diffusion process, some metric gaps (e.g., Entropy 2.93 vs 2.85, Cluster Size 5.40 vs 5.20) could be within noise. Reporting mean±std over multiple seeds is standard practice for generative models.

2. **VLM-assisted evaluation is a black box.** The "VLM↑" column in Table 1 reports a score out of 10 without specifying which VLM was used, what prompt was employed, or the scoring criteria. Similarly, the perceptual score from 10 users lacks details on recruitment, rating methodology, blinding, and inter-rater reliability.

3. **Out-of-domain generalization evidence is purely qualitative (Fig. 7).** The Objaverse experiments show four examples with no quantitative metrics, yet the paper claims "strong generalization capability" (line 235). Quantitative metrics (e.g., penetration depth, diversity) could be computed on Objaverse samples even without ground contact maps.

4. **Baseline post-processing not described.** The paper states baselines are "augmented... with an optimization-based post-processing module to correct hand poses" (line 187) but does not specify what this module does, leaving the comparison partially opaque.

5. **Force semantics claim lacks statistical backup.** The 22-25% larger contact area figure (Section 5.4.3) is stated only in prose with no supporting table, statistical test, or per-example breakdown.

6. **55% reconstruction success rate not analyzed for systematic bias.** The paper does not discuss what kinds of interactions, object geometries, or occlusion levels fail reconstruction — potential sources of dataset bias.

### Trivial

- The refiner training targets are not clearly specified (line 152 says it "inherits the Transformer architecture" but not what data or targets it trains on).
- The paper could clarify whether the Qwen-7B encoder weights are shared or separate between the contact predictor and the diffusion module.

## Nice-to-Haves

- Validate WildO2 reconstruction quality against known ground truth (even a small synthetic or lab-captured set) and report reconstruction error.
- Report mean±std over multiple seeds for all quantitative results.
- Describe the VLM evaluation protocol and provide inter-rater statistics for the user study.
- Provide quantitative OOD metrics on Objaverse.
- Analyze/report characteristics of failed reconstructions.

## Removed Points

These points are flagged to be removed; treat them with caution if referenced.

1. **"Method's advantage is unsurprising because baselines weren't designed for DSC conditioning"** — REMOVED: When introducing a new task, adapting existing methods as baselines is standard practice. The comparison fairly reflects the current state of the art, and the asymmetry (TOUCH is designed for this task, baselines are adapted) is a natural consequence of the research direction, not a flaw.

2. **"A method that simply reproduces the biases of the reconstruction pipeline would score well"** — REMOVED: Speculative concern without evidence. Baselines are evaluated on the same data and TOUCH outperforms them across all 10 metrics, which would not be explained by bias fitting alone.

3. **"Train/test split is unclear"** — REMOVED: The paper clearly states "For each hand part contact category, we perform a random 4:1 split" (line 162). This is sufficiently clear.

4. **"In-the-wild is overstated"** — REMOVED: Something-Something V2 is captured in uncontrolled recording conditions, which matches standard usage of "in-the-wild" relative to lab mocap datasets.

5. **Missing related works** — REMOVED per instructions (no external sources to confirm existence).

6. **Reproducibility concerns about undisclosed hyperparameters** — REMOVED: The paper provides learning rate, batch size, optimizer, epochs, and training regimen (1000 epochs, Adam, lr=1e-4). This is adequate.

7. **Formatting/style nitpicks / typos / parser artifacts** — REMOVED per instructions.

## Novel Insights

The most insightful tension exposed by the reviews is the inherent **closed-loop evaluation problem** in the paper's core contribution. The paper's strength — building a large-scale in-the-wild dataset via automated reconstruction — is also the source of its main evaluation weakness: the reconstructed data serves as both the training target and the evaluation ground truth, with no external reference to validate the reconstruction quality. This creates a situation where the method could, in principle, be rewarded for fitting the reconstruction pipeline's biases rather than producing genuinely accurate geometry. The ablation study provides internal validation (components are tested relative to each other), but the absolute claim of "physical plausibility" needs an external anchor. A synthetic-data validation study or a small lab-captured validation set would resolve this tension cleanly. This specific pattern — dataset contribution as both strength and evaluation constraint — is worth noting for the broader field of in-the-wild 3D reconstruction from video.

## Suggestions

1. **Validate reconstruction quality externally.** Run a small-scale study (even 20-30 samples) comparing WildO2 reconstructions against ground truth from synthetic data or a calibrated multi-camera capture. Report Chamfer distance or similar error to establish a baseline for reconstruction accuracy.

2. **Add uncertainty quantification.** Re-run all experiments with 3-5 random seeds and report mean±std in Tables 1 and 2. This is especially important for the smaller metric gaps (Entropy, Cluster Size).

3. **Document all black-box evaluation protocols.** Specify which VLM was used, the prompt, and the scoring criteria for the VLM metric. For the perceptual study, report rater count, recruitment method, rating scale, blinding procedure, and inter-rater agreement.

4. **Provide quantitative OOD metrics.** Compute penetration depth, diversity, and (if possible) VLM-based plausibility scores on Objaverse samples to support the generalization claim quantitatively.

5. **Analyze the 45% failure rate.** Characterize which interactions/objects/occlusion levels systematically fail reconstruction to inform users about the dataset's coverage and potential biases.

## Score and Decision

**MY FINAL SCORE: 6.0**
**MY FINAL DECISION: Accept**

**Calibration anchors used:**

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| HOI-Diff | ZYwLfi50GI.md | 5.25 | R1, R2 | Most topically relevant anchor. TOUCH is stronger: fine-grained hand-part contact vs body-level joints, more comprehensive metrics, dataset contribution, proper ablations. HOI-Diff was rejected for neglecting hand contact — TOUCH directly addresses this. |
| IHDiff (Interacting Hands DM) | nTNElfN4O5.md | 5.50 | R1, R2 | Two-hand interaction prior. TOUCH has broader scope (hand-object, diverse interactions) and more methodological components. |
| InterMask | ZAyuwJYN8N.md | 6.00 | R2 | Human interaction generation, accepted. Comparable in comprehensiveness. TOUCH has more methodological novelty but carries a reconstructed-data evaluation concern. |
| DICE | rfrtFwnF62.md | 6.00 | R2 | Hand-face interaction capture, accepted. Comparable score — both address under-explored interaction tasks with convincing evaluations despite some methodological limitations. |
| HandCLR | 96jZFqM5E0.md | 6.67 | R1 | Pre-training for 3D hand pose estimation, accepted. Stronger than TOUCH in experimental thoroughness but tackles a different task. |
| Interactive-Action Image Gen | OWIk5E4lJs.md | 5.20 | R2 | Interactive action image generation. Weaker than TOUCH — less comprehensive evaluation. |

**Round 1 bracket**: (4.5, 7.5). Clearly above weak 2.5-3.0 anchors; clearly below strong 8.0 anchors.

**Round 2 narrowing**: The paper sits between HOI-Diff (5.25, Reject) and InterMask/DICE (6.00, Accept). TOUCH is a clear improvement over HOI-Diff — it addresses precisely the weaknesses that got HOI-Diff rejected (coarse body-level contact, lack of hand-specific metrics, missing physical constraints). It is comparable to accepted papers at 6.00 in comprehensiveness. The reconstructed-data weakness prevents scoring higher.