Now I have enough calibration data. Let me write the consolidated review.

**Calibration Summary:**

**Round 1 — Bracketing:** The paper clearly sits above the weak band (papers scoring 2–3) — those have fundamental methodological flaws or are withdrawn. It sits well below the strong band (8+) which are broad-impact papers with clean evaluations on established benchmarks. The plausible range is 3.5–7.5.

**Round 2 — Narrowing:** Within this band, the most directly comparable paper is **CLUTCH** (avg 5.0, Accept Poster). CLUTCH also introduces an in-the-wild hand dataset with a method evaluated primarily on its own data, and was flagged by reviewers for the same type of concern (dataset quality, no external validation, no human verification). Yet CLUTCH was accepted at 5.0. TOUCH has stronger task novelty (free-form HOI beyond grasping, vs. hand-motion-only in CLUTCH) but has additional underspecification issues in evaluation metrics. **Text2Interact** (avg 5.5, Accept Poster) has cleaner evaluation on established benchmarks but less task novelty. **SynHLMA** (5.5, Reject) was rejected despite strong methodology due to limited novelty and presentation issues — TOUCH has stronger novelty. **HOI-PAGE** (4.5, Reject) is weaker than TOUCH in both methodology and evaluation breadth. I place TOUCH around the same level as CLUTCH — solid contributions with evaluation concerns that are typical for this type of data-creation paper, but with specific underspecification issues that should be addressed. Score: **5.0**.

---

## Summary

This paper introduces the task of **free-form hand-object interaction (HOI) generation** — moving beyond the standard grasp-centric paradigm to diverse interactions like pushing, tipping, and pressing. The authors contribute (1) **WildO2**, a 3D HOI dataset of 4.4k samples derived from in-the-wild video with 92 intents and 610 object categories, built via a semi-automated reconstruction pipeline, (2) **TOUCH**, a three-stage framework with contact map prediction, multi-level conditioned diffusion, and physical refinement, and (3) a multi-level annotation system including fine-grained 17-part hand segmentation and descriptive synthetic captions. Experiments show TOUCH outperforms adapted baselines on contact accuracy, physical plausibility, and diversity metrics.

## Strengths

- **New task formulation (free-form HOI beyond grasping) is well-motivated and timely.** The paper clearly identifies that existing methods are constrained by grasp-centric priors and inductive biases. The argument that contact relationships can serve as a spatial prior for non-grasping interactions (Section 4.1) is technically sound. This reframing opens a meaningful direction for the community.

- **WildO2 dataset fills a genuine gap.** While the dataset is moderate in size (4.4k samples), it covers non-grasping interactions that no existing 3D HOI dataset (GRAB, HOI4D, ARCTIC) captures. The O2HOI frame-pairing strategy (Section 3.1) — using SAM2 segmentation on an object-only frame with dense matching to transfer masks — is clever and more scalable than inpainting-based alternatives. The 17-part hand segmentation including dorsal regions is a practical improvement over the inner-hand-only schemes in prior grasp datasets.

- **Multi-level conditioned diffusion with coarse-to-fine injection is validated by clean ablations.** Table 2 shows consistent degradation when removing components: removing both contact maps (✗ hoc.) drops P-IoU from 0.728→0.492, removing the refiner drops it to 0.513, and removing either text level (✗ T_DSC or ✗ T_SSC) produces measurable drops. The ablation confirms that the coarse-to-fine conditioning design (Eq. 4–5) and the cycle-consistency refinement (Eq. 7) each contribute meaningfully.

- **Clear quantitative advantage over adapted baselines.** Table 1 shows TOUCH substantially outperforms both ContactGen and Text2HOI across contact, penetration, diversity, and semantic consistency metrics, with P-IoU 0.776 vs. 0.620/0.711 and MPVPE 2.97 vs. 5.46/4.69. The advantage is consistent across all metrics.

- **Qualitative evidence of semantic controllability is compelling.** Figures 8–9 demonstrate the model can produce distinct poses for "firm" vs. "gentle" prompts with 22–25% larger contact area for firm prompts (Section 5.4.3), and Figure 7 shows plausible OOD generalization to Objaverse objects.

## Weaknesses

### Major

- **Semantic consistency evaluation (VLM metric) is completely underspecified.** The paper reports "VLM assisted evaluation" (VLM↑ in Table 1) with a score of 7.1, but provides zero details about which VLM was used, the prompting protocol, the rating scale, or how the evaluation was conducted (Section 5.1, line 169). This makes the metric impossible to interpret, reproduce, or compare against. For a paper whose core claim is fine-grained semantic controllability, this is a significant gap. The perceptual score from only 10 users (PS↑) is also too small to establish statistical significance for a task as nuanced as HOI plausibility.

- **Baseline post-processing is not described, casting doubt on comparison fairness.** The paper states baselines are augmented with "an optimization-based post-processing module to correct hand poses" (Section 5.2, line 194) but gives no details about what this module is, its complexity, or whether its hyperparameters were tuned separately for each baseline. Without this information, it is unclear whether the comparison reflects architectural differences or engineering budget.

- **No evaluation against independently captured 3D ground truth.** All quantitative metrics are computed on the WildO2 test set, which comes from the same reconstruction pipeline used to create the training data. While this is standard practice in dataset-driven work, the situation is more acute here because (a) the reconstruction pipeline has a 55% success rate (Figure 3a), meaning 45% of attempts were discarded — introducing potential selection bias toward easier interactions, and (b) the reconstruction quality itself is a bottleneck (using single-image-to-3D from Xu et al. 2024). The paper does not validate against any independently captured HOI data (e.g., a small subset of GRAB or HO3D) to verify that its metrics reflect real physical plausibility rather than fit to reconstruction artifacts.

### Minor

- **Dataset scale limits the strength of conclusions.** With 4.4k samples across 92 intents (~7 per intent on average), the dataset is sparse. The authors acknowledge this in the limitations ("the current dataset scale also presents an area for future growth"), but the concern about memorization vs. generalization for rare intents is real. The OOD generalization demonstration (Figure 7) is only qualitative across 4 samples.

- **OOD evaluation is purely qualitative.** Figure 7 shows plausible OOD results on Objaverse for 4 examples, but no quantitative metric (e.g., contact accuracy, or human-rated plausibility on a larger set of OOD samples) is reported. This limits the strength of the generalization claim.

- **P-FID as a "semantic consistency" metric is questionable.** FID measures distributional distance between generated and ground truth sample sets, not direct text-to-pose alignment. While P-FID is reasonable as a quality/diversity indicator, its placement under "Semantic Consistency" in Table 1 is misleading. The paper could clarify this or rename the metric.

### Trivial

- Figure 3a: "Pore Estimation Failure" is clearly a parser artifact for "Pose Estimation Failure." This should be corrected.
- The 10% random drop rate for global condition components (Section 4.2) is mentioned but its effect is not ablated.

## Nice-to-Haves

- A small-scale human preference study (e.g., 50+ raters) comparing generations from TOUCH vs. baselines on semantic alignment would substantially strengthen the controllability claim.
- Variance/confidence intervals on Table 1 would help assess significance given the 677-sample test set.
- Analysis of failure modes: what kinds of interactions does TOUCH systematically struggle with?

## Removed Points

- **"Evaluation is circular" claim** — removed as overstated. Evaluating against reconstructed ground truth is standard practice for dataset-driven generation. The real concern (no independent validation) is preserved in the Major weaknesses. The framing as "circular" misrepresents standard supervised evaluation.
- **Speculative overfitting concern about 1000 epochs** — removed. Without evidence of overfitting (e.g., training/validation loss divergence), this is speculation.
- **Contact map prediction question ("ambitious to infer contact without seeing the hand")** — removed. The ablation (Table 2, ✗ hoc. row) validates this design choice, showing a clear drop in performance when contact maps are removed.
- **Split into 4 early/4 later blocks is arbitrary** — weakened to nice-to-have. An ablation on this split would be informative but the current choice is reasonable.
- **Missing related works and missing appendix content** — removed per hard rules (parser strips appendices; you cannot confirm missing related works are actually missing).
- **"No code or data release commitment"** — removed per hard rule (cannot question existence/release status of cited entities).
- **Strength Finder items that are generic or conflict with verified weaknesses** — removed: generic strengths like "addressed important problem" are dropped. Strength about P-FID for semantic consistency is weakened since P-FID measures distribution similarity, not text-pose alignment.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface known concerns about evaluation methodology for in-the-wild reconstructed datasets rather than revealing fundamentally new observations about the work.

## Suggestions

1. **Specify the VLM evaluation protocol in full** — which model, exact prompt template, rating scale, number of queries, and whether ratings were per-sample or aggregate. Without this, the VLM↑ metric is not actionable.
2. **Document the baseline post-processing** — what optimization is run, how many steps, what loss terms, and whether hyperparameters were tuned per baseline.
3. **Add a small independent validation experiment** — e.g., reconstruct 50–100 GRAB samples through the same pipeline and evaluate TOUCH on them, or annotate a small set of held-out OOD samples with human plausibility ratings.
4. **Increase the perceptual study size** to at least 30 raters with bootstrapped confidence intervals, or replace it with a more rigorous protocol.
5. **Clarify what P-FID measures** — rename it or add a sentence explaining its role as a distributional quality metric rather than a direct semantic consistency measure.

## Score and Decision

**Calibration Anchors (all rounds):**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| SIGHT (ff3gboFkss) | 3.00 | R1 (weak) | Below TOUCH — less developed method, lower novelty |
| MoCtrl4D (JT6hR0sNXZ) | 2.50 | R1 (weak) | Below TOUCH — motion control for 4D, unrelated domain |
| SesaHand (sKMgGQQy7g) | 5.00 | R1 (middle) | Comparable — both have good method with evaluation gaps, TOUCH has stronger task novelty |
| InfBaGel (TeyHNq4WlI) | 6.00 | R1 (middle) | Above TOUCH — cleaner evaluation, clearer contributions |
| SynHLMA (EzJowEZ1UJ) | 5.50 | R1 (middle) | Above in avg score but REJECTED — TOUCH has stronger novelty |
| CLUTCH (W7YRskO47j) | 5.00 | R2 (narrow) | Most comparable anchor — same type of evaluation concerns (own dataset only, no external validation), accepted. TOUCH has stronger task novelty but weaker VLM metric documentation |
| Text2Interact (cthzUgBUn7) | 5.50 | R2 (narrow) | Above TOUCH — cleaner evaluation on established benchmarks, less task novelty |
| HOI-PAGE (qZhk7prB7v) | 4.50 | R2 (narrow) | Below TOUCH — cascade of pre-trained models, limited methodology |
| EgoHandICL (nwjy9BeorI) | 6.00 | R2 (narrow) | Above TOUCH — in-context learning for reconstruction, stronger evaluation |

**Round 1 bracket:** 3.5–7.5  
**Round 2 narrowing:** Compared against CLUTCH (5.0, Accept) as the most similar paper — same type of contribution (in-the-wild dataset + model), same type of evaluation concern (no external validation). TOUCH has stronger task novelty but weaker metric documentation.  
**Final score:** 5.0 — a paper with genuine contributions (new task, new dataset, solid method) whose evaluation has real but addressable weaknesses. Comparable to CLUTCH which was accepted at this score level.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>