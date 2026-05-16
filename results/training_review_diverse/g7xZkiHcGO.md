I have verified the paper's claims against the reviewer's statements. The paper uses appropriately bounded language ("through our evaluated domain gap factors," "among our proposed benchmarks," "among our evaluated ones") for the synthetic-to-real claim. Let me now compile the final, consolidated review.

---

## Summary

This paper proposes the first domain adaptation benchmarks for indoor 3D object detection, combining existing real-world datasets (ScanNet, SUN RGB-D) with two newly introduced large-scale synthetic datasets (SimRoom, SimHouse) generated via the ProcTHOR procedural pipeline. It defines four adaptation scenarios (high-to-low quality point clouds, low-to-high quality, synthetic-to-real, single-room-to-multi-room), systematically analyzes which domain gap factors most degrade detection performance, and provides baseline results using several domain adaptation methods adapted from other tasks. The key observation—that synthetic-to-real adaptation is the most challenging gap among those evaluated—is supported by controlled experiments that isolate data scale from domain shift.

## Strengths

1. **First systematic domain adaptation benchmark for indoor 3D object detection.** The paper explicitly proposes "the first domain adaptation series benchmarks for indoor 3D object detection" (contributions, Section 1), combining four datasets across four practically motivated adaptation scenarios (Section 3.3.3). Cross-dataset evaluation in Figure 1(b) reveals drastic mAP drops (e.g., VoteNet from 44.09 within ScanNet to 11.20 when trained on SimRoom), confirming this is a previously unstudied and challenging problem.

2. **Introduction of large-scale synthetic datasets (SimRoom, SimHouse) with precise annotations.** Table 1 shows SimRoom has 7,202 scenes (~176k objects) and SimHouse has 7,306 scenes (~686k objects), compared to ScanNet's 1,513 scenes (37k objects) and SUN RGB-D's 10,335 scenes (37k objects). The generative framework (ProcTHOR) enables scalability and controllable experiments (e.g., Table 4's object-replacement study isolating the semantic gap).

3. **Rigorous controlled analysis identifying synthetic-to-real as the most challenging domain gap.** Table 5 aligns training scene counts across datasets to exclude data-scale confounds, showing that even with 3,000 SimRoom scenes, mAP on ScanNet reaches only 5.25, versus 22.54 from 230 ScanNet++ scenes and 44.09 from the full in-domain ScanNet training set. Table 4 further isolates the semantic gap by integrating real objects, showing improvement that still falls far short of the target oracle.

4. **Thoughtful design of controlled experiments.** The data-scale-controlled analysis (Table 5) is a strong methodological choice that correctly separates domain shift from data quantity effects. The object-size prior experiment (Section 4.3.1) and few-shot fine-tuning curves (Figure 4(b)) are useful ablations that deepen the analysis.

5. **Implementation of multiple domain adaptation baselines adapted for indoor 3D detection.** The paper implements and evaluates MT, VSS, PPFA, RV, and OHDA methods (Section 4.3.2, Table 3), establishing a first reference point for future work. The discussion of each method's behavior (e.g., why VSS helps in some settings but harms in others) provides useful diagnostic signal.

6. **Careful label-space unification.** The paper merges fine-grained categories (529 in ScanNet, 620 in SUN RGB-D) into 15 common categories with sufficient instances (≥150) per dataset (Section 3.3.2), enabling meaningful cross-dataset comparison while avoiding the long-tail problem.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions—the benchmarks, datasets, and empirical findings—are supported by the evidence presented. None of the issues raised threaten the central claims.

### Minor
1. **The synthetic-to-real claim, while appropriately bounded, relies on a single procedural generator (ProcTHOR) without discussion of its representativeness.** The paper consistently uses bounded language ("among our evaluated domain gap factors," "among our proposed benchmarks"), but it does not discuss the extent to which SimRoom captures the diversity of synthetic indoor data more broadly, nor does it compare against other synthetic datasets (e.g., Structured3D, 3D-Front). The finding is valid for ProcTHOR-based data, and a brief caveat making this explicit would strengthen the paper's scientific rigor.

2. **Domain adaptation baselines lack sufficient implementation detail for reproducibility.** The paper states that methods were "re-implement[ed]" with "some adjustments" for the detection task (Section 4.3.2), but it provides no specifics on how each method (VSS, PPFA, RV, OHDA) was adapted from its original task (classification, segmentation) to indoor 3D object detection, nor on hyperparameter choices. For a benchmark intended as a reference, this limits the baselines' utility as reliable anchors.

3. **Results are reported without variance or error bars.** Training involves stochasticity (random sampling, weight initialization, data augmentation), yet all tables report single-point estimates. For a benchmark paper that will be used as a reference, reporting mean ± std over multiple runs (e.g., 3 seeds) would significantly increase credibility, especially for DA baselines where some gains are modest.

4. **The label-space merging process (fine-grained → 15 categories) is described but not tabulated.** The paper gives one example ("dining table" and "office table" → "table") but does not provide the complete mapping, which is needed for exact reproducibility. A supplementary table listing the merged categories would be straightforward and valuable.

5. **Table 4 (object semantic analysis) lacks detail.** The paper states that objects from ScanNet were integrated into synthetic scenes, but does not specify: (a) which object categories were replaced, (b) how many scenes were used, (c) whether the replacement was one-to-one or many-to-many. More detail would make this clever ablation reproducible and more informative.

6. **Hard to assess generality across detectors.** The main experiments use only VoteNet. The paper mentions transformer-based detectors (Pointformer, V-DETR) "can be seen in supplementary materials" (Section 4.1), but the parser strips these. Including at least a summary comparison in the main paper would strengthen the claim that the observed gaps are characteristic of indoor detection generally, not specific to VoteNet.

### Trivial
- The paper would benefit from a dedicated limitations section (e.g., discussing ProcTHOR data diversity, the 15-category limitation, and that DA baselines are preliminary).

## Nice-to-Haves
- Commitment to release of SimRoom/SimHouse and evaluation code, which would maximize community impact.
- A table listing per-category object frequency in each dataset, helping future work avoid categories dominating mAP.
- More granular probes of the layout gap (e.g., varying room count in SimHouse to quantify how layout complexity affects transfer).

## Removed Points
No points from the Harsh Critic triggered hard-rule removal requirements. All criticisms are grounded in the paper content and do not involve questioning the existence of cited entities, parser artifacts, formatting nitpicks, missing appendix content, or strawman arguments. Some points were weakened (e.g., the synthetic-to-real "overgeneralization" claim is softened by the paper's own bounded language) and re-tired accordingly.

## Novel Insights
Beyond the paper's own contributions, one genuinely novel insight emerges from the reviews: the fact that VSS (a high-to-low quality augmentation) is effective only when the source has higher point cloud quality than the target, but counterproductive in the reverse direction, suggests that domain adaptation strategies for indoor 3D detection need to be asymmetric—matching the direction of the quality gap matters. This point is latent in the paper's Table 3 but not explicitly articulated as a design principle. The size-prior experiment also suggests a practical finding: knowing even coarse target-domain statistics (category-level mean sizes) provides a reliable performance gain, which is surprising given how simple the prior is.

## Suggestions
1. Explicitly caveat the synthetic-to-real finding: state that it is based on ProcTHOR-generated data and that generalizability to other synthetic pipelines is an open question.
2. Release a table with the complete fine-grained→15-category label mapping, per-category object counts per dataset, and a table of the detailed implementation adaptations for each DA baseline.
3. Add error bars (mean ± std over 3 seeds) for the main comparison tables, especially the DA baselines.
4. Include a brief summary of transformer-based detector results in the main paper (or make the supplementary material accessible).
5. Add a short limitations paragraph.

## Score and Decision

This is a solid benchmark contribution addressing an important and under-explored problem. The synthetic datasets are large-scale and precisely annotated. The controlled experiments are well-designed and the data-scale analysis (Table 5) is a methodological strength. The weaknesses are minor—centered on documentation detail and reproducibility polish rather than any threat to the paper's core claims. The paper should be accepted.

**Originality:** High for task formulation (first indoor 3OD DA benchmark).  
**Importance:** High—domain adaptation is a practical bottleneck for deploying indoor detectors.  
**Claims supported:** Yes, with appropriate bounded language.  
**Soundness:** Good; controlled experiments, isolated confounds.  
**Clarity:** Above average; motivations and scenarios are clearly laid out.  
**Value to community:** High—datasets + benchmarks + baselines will be used.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>