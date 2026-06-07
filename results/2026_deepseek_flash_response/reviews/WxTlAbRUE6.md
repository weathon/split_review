## Summary

This paper introduces GMD-25, a benchmark for evaluating compositional generalization in machine learning force fields (MLFFs). It consists of four systematically designed tasks—length extrapolation, functional group composition, functional group duplication, and functional group combination—each isolating a specific form of compositional generalization. The paper evaluates five popular MLFF architectures (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) on these tasks and finds that all models struggle with OOD generalization, with errors often 1–2 orders of magnitude higher than in-distribution, and that ID performance does not predict OOD ranking.

## Strengths

- **Well-motivated and systematically designed tasks**: The four tasks cleanly isolate distinct compositional generalization challenges (length extrapolation, composition, duplication, combination) with clear rationales. This goes substantially beyond existing MLFF benchmarks (MD17, WS22, Transition1x, MD22), which test interpolation within the same chemical space. The two-track design (base/augmented variants for Tasks 1–2) is a thoughtful addition.

- **Important empirical finding**: The paper demonstrates that the model ranking on in-distribution performance does not carry over to out-of-distribution performance. For example, EquiFormerV2 achieves the lowest OOD force MAE on Length Extrapolation but its energy MAE becomes the worst in the OOD region (Figure 2). This is concrete evidence that standard ID benchmarks give a misleading picture of model quality.

- **Clean diagnostic signal by excluding foundation models**: Section 4.1 explicitly excludes pre-trained foundation models (e.g., MACE) to avoid conflating memorization with genuine compositional generalization—a principled design choice that keeps the benchmark's diagnostic signal clean.

- **Reproducible pipeline**: The four-step data generation workflow (RDKit → FlashMD → GFN2-xTB recalculation → ASE) is documented with specific parameters (300 K, 16 fs timestep, 200k steps), totaling 296,534 labeled geometries across 118 molecules, making the process extensible.

## Weaknesses

### Major

- **No statistical reproducibility (multiple random seeds / error bars)**. The paper presents results from single runs with no mention of multiple seeds, no standard deviations, and no error bars. For a benchmark paper that makes comparative claims such as "GemNet overall performs best in the OOD region for Functional Group Composition and Functional Group Duplication," the reader cannot assess whether observed differences are reliable or within training noise. This is the single most significant weakness for a benchmark intended as a community reference. *Verification: grep for "seed|standard deviation|error bar|multiple run" across the paper returns zero matches.*

- **Figure label inconsistencies require clarification.** The paper's text (Section 4.1, Abstract, Conclusions) consistently lists five evaluated models: SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2. However, the figure descriptions extracted from the PDF show discrepancies: Figure 2 lists "PBE0" as one of the compared models (not PAINN), and Figure 3 lists "m4s" as a model name that does not appear elsewhere in the paper. Figure 4 correctly lists the five models from the text. These inconsistencies may be PDF extraction artifacts from embedded figures, but given that this is a benchmark paper where readers need to know exactly which models were compared, the authors must clarify this. *Verification: Line 120 (Figure 2 alt text) lists "EquiFormerV2, PBE0, DimeNet++, SchNet, GemNet"; Line 144 (Figure 3 alt text) lists "DimeNet++, m4s, GemNet, EquiFormV2, PAINN, and SchNet." Neither "PBE0" nor "m4s" appear in the paper's model list (Section 4.1).*

- **GFN2-xTB ground truth limits the benchmark's scope, and this is not adequately discussed.** The paper motivates the benchmark by discussing MLFFs that aim to replace DFT, yet the reference labels are computed with GFN2-xTB—a semi-empirical tight-binding method substantially less accurate than DFT for many chemical properties. The paper mentions this only in passing (Section 3, "known for its balance between computational efficiency and accuracy"). For a benchmark intended to drive progress toward physically meaningful MLFFs, good performance on GMD-25 does not necessarily imply good performance on DFT-level data. The paper should either (a) benchmark GFN2-xTB against DFT on a subset of molecules to show that the compositional structure is preserved, or (b) more carefully reposition the claims as being about generalization to semi-empirical approximations. *Verification: Line 56 uses "GNF2-xTB" (typo for GFN2-xTB); Line 94 mentions "GFN2-xTB" for recalculation.*

### Minor

- **No quantitative results table.** The paper presents all results through figures with logarithmic scales (Figures 2–4). A benchmark paper should include a summary table with actual MAE values (energy and forces) for each model-task combination to facilitate comparison by future work. The current presentation makes it difficult to read precise values.

- **16 fs timestep in FlashMD trajectories is unusually large and not validated.** Standard atomistic MD uses timesteps of 0.5–2 fs. While FlashMD is designed for long-stride simulations (Bigi et al., 2025), the paper does not validate that the generated trajectories are physically realistic (e.g., by comparing energy distributions or RDFs with standard MD). If trajectories contain unphysical configurations, the GFN2-xTB recalibration step provides accurate energies for those geometries, but it does not fix the geometry quality. *Verification: Line 92 states "16 femtosecond timestep."*

- **Limited training data sizes may conflate data scarcity with compositional generalization failure.** For Length Extrapolation base, models see only ~10,000 snapshots from 5 molecules (C2–C6 alkanes). The paper attributes poor OOD performance to compositional generalization failure, but an alternative explanation is simply undertraining. A data-ablation experiment (training on progressively larger ID subsets and checking whether OOD error decreases) would help separate these explanations.

### Trivial

- "GNF2-xTB" appears to be a typo for "GFN2-xTB" (line 56; correct spelling at line 94).

## Nice-to-Haves

- A data-ablation control for at least one task (e.g., Length Extrapolation base) training on progressively larger ID subsets to distinguish data scarcity from genuine compositional generalization failure.
- A quantitative comparison of GFN2-xTB vs. DFT on a subset of the molecules to validate that the compositional structure the benchmark aims to test is preserved at the semi-empirical level.
- Including MACE as a baseline—it is a prominent equivariant MLFF that is not a foundation model—would strengthen the claim of covering "state-of-the-art" MLFFs.

## Removed Points

These points from the input reviews were filtered:

- *"Related work missing MACE"* — Removed. The paper explicitly justifies excluding foundation models; MACE-o (Batatia et al., 2023) is a foundation model variant. MACE (Batatia et al., 2022) could reasonably be included, but this is a nice-to-have, not a weakness.
- *"Hyperparameter tuning on ID only may hurt OOD"* — Removed. This is a speculative concern without specific evidence that it affected results. Tuning on ID is standard practice in OOD benchmarks.
- *"GFN2-xTB compared to DFT limitation should be explored"* — Kept as a major weakness above (repositioned from the harsh critic's framing).
- *"Toolkit to be released upon acceptance"* — Removed per hard rules (do not question release status).
- *"Missing appendix details"* — Removed per hard rules (parser strips appendix).
- *"Benchmark does not control for data scarcity vs compositionality"* — Kept as minor weakness above.
- *"16 fs timestep concern"* — Kept as minor weakness above, but tempered from the harsh critic's framing (the paper cites FlashMD which is designed for this).
- *"No discussion of what compositional means for force fields"* — Removed. The paper does provide reasonable motivation in Section 3.1 for each task.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add multiple random seeds.** Run each model-task combination with at least 3 seeds and report mean ± std. This is the single most impactful improvement.
2. **Clarify figure labels.** Resolve whether "PBE0" and "m4s" in the figures are artifacts, mislabeled baselines, or additional methods. Align all figure legends with the model list in Section 4.1.
3. **Add a quantitative results table.** Include a table with numerical MAE values for each model on each task (ID and OOD) so the community can reference the numbers.
4. **Add a limitations paragraph** discussing the GFN2-xTB ground truth and the 16 fs timestep, with evidence or validation where possible.
5. **Add a data-ablation experiment** for at least one task to help distinguish data scarcity from compositional generalization failure.

## Score and Decision

The paper addresses a genuine gap—systematic evaluation of compositional generalization in MLFFs—with four well-motivated tasks and a finding (ID performance does not predict OOD performance) that is likely to be influential. However, in its current form the paper has two significant shortcomings: (a) no statistical reproducibility (single runs, no error bars) for comparative claims, and (b) figure-label inconsistencies that undermine reader confidence in the evaluation. For a benchmark paper that aims to serve as a community reference, these issues are too significant to overlook. With revisions addressing these concerns, the paper could be acceptable.

**Score: 5.5 — Borderline reject. The benchmark design is solid and the contribution is real, but the evaluation reporting lacks the rigor expected of a benchmark paper, and the figure inconsistencies need clarification.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>