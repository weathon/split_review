Now I have enough calibration. Let me compose the final review.

**Round 1 bracket:** Based on the initial search, weak anchors averaged ~2.9 (2.5, 2.33, 3.0, 3.4), middle anchors averaged ~4.95 (5.0, 5.8, 4.33, 4.67), and strong anchors averaged ~7.94 (8.0, 7.75, 8.0, 8.0). The paper is clearly stronger than the weak anchors and weaker than the ~8.0 strong anchors. **Initial bracket: 5.0–7.0.**

**Round 2 narrowing:** I retrieved 8 additional anchors with scores 5.0, 5.8, 4.67, 6.0, 5.8, 6.33, 7.0, 6.5. Reading the full reviews of the most relevant ones (3D-GRAND avg 5.0, Coarse Correspondences avg 4.67, 3D-AffordanceLLM avg 5.8, Matryoshka avg 6.0, MLLMs Know Where to Look avg 7.0), CUBE-LLM is clearly stronger than 3D-GRAND (which was withdrawn because no models were trained on its dataset), similar to or slightly stronger than 3D-AffordanceLLM (5.8) and Matryoshka (6.0), and less polished than MLLMs Know Where to Look (7.0) which had a tightly focused finding. **Final score: 6.0.**

## Summary

This paper introduces CUBE-LLM, a multimodal large language model (MLLM) that learns metric 3D grounding from images by scaling data rather than adding 3D-specific architectural components. The authors curate LV3D, a large pretraining dataset (9.6M images, 40.9M QA pairs) combining existing 2D and 3D recognition datasets under a multi-turn QA formulation, and design a task decomposition strategy (decomposing 3D boxes into easier sub-tasks) plus a visual chain-of-thought (V-CoT) training scheme. CUBE-LLM achieves state-of-the-art scores on refCOCO (87.0 average), competitive performance on standard VQA benchmarks (VQAv2, GQA, SQA), and strong 3D grounding results on Talk2Car (71.4 BEV AP with LiDAR prompting, outperforming the prior SOTA camera+LiDAR method by 21.3 points) and DriveLM.

## Strengths

- **Data scaling drives 3D understanding without 3D-specific architecture.** Figure 5 (top) shows a clear monotonic improvement in zero-shot BEV and 3D AP on Talk2Car as LV3D data increases from 10% to 100%. This directly supports the paper's central claim that scaling diverse 2D+3D data induces 3D capability in a standard MLLM architecture.

- **Large and well-structured pretraining dataset (LV3D).** Combining 14 datasets across indoor/outdoor, 2D/3D into 40.9M QA pairs under a standardized coordinate format is a substantial engineering contribution. The task decomposition (Section 3.2) that crafts up to 30 QA pairs per sample from a single 3D label is a concrete, scalable data-engineering strategy.

- **State-of-the-art 2D grounding across refCOCO/+g.** Table 4 shows CUBE-LLM (7B) achieving 87.0 average, outperforming all generalist models (Qwen-VL 85.7, Ferret 83.9) and matching/exceeding several specialist models. This result is clean and verifiable.

- **3D capability does not degrade general MLLM performance.** Table 5 confirms that CUBE-LLM (13B) scores 79.9 on VQAv2, 64.1 on GQA, and 72.2 on SQA_I, closely matching LLaVA-1.5-13B, validating that 3D reasoning is an "expansion, not a trade-off."

- **Visual chain-of-thought and specialist prompting are both empirically beneficial.** Figure 5 (bottom) shows V-CoT training improves zero-shot 3D AP, and the LiDAR-prompted variant (CUBE-LLM†) more than doubles camera-only BEV AP (from 30.1 to 61.2). Both are demonstrated with measurable results.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by evidence; the issues below are addressable with revisions.

### Minor

- **Abstract presents the headline 21.3 AP_BEV result ambiguously.** The abstract states "CUBE-LLM significantly outperforms existing baselines by 21.3 points of AP_BEV on Talk2Car" without clarifying that this result uses LiDAR prompting (CUBE-LLM† with CenterPoint proposals). The camera-only variant achieves 30.1 BEV AP_A, which trails the camera+LiDAR baseline MSSG (35.7). While the experiments section clearly separates the two settings, the abstract and introduction (line 43: "71.4 vs 50.1") should explicitly note that the 21.3-point gain comes from the LiDAR-prompted version. This is fixable by adding a brief qualifier.

- **Indoor 3D grounding evaluation (Table 3) lacks external baselines.** Table 3 only compares CUBE-LLM trained on LV3D-small vs. full LV3D. Without comparisons to existing indoor 3D grounding methods (e.g., prior detection-based 3D approaches or other MLLMs), the reader cannot assess whether the absolute numbers are meaningful. The paper frames this as an ablation showing that outdoor data transfers to indoor scenes, which is a valid analysis, but the section would be strengthened by even one simple external baseline.

- **Risk of data leakage between LV3D pretraining and DriveLM evaluation not discussed.** LV3D includes nuScenes (Table 1), which is the sensor data underlying DriveLM. While the paper describes a separate evaluation split (line 186: "We sample 600 scenes for training and 96 scenes for validation"), there is no discussion of whether any LV3D pretraining images overlap with DriveLM validation scenes. A sentence addressing this would strengthen confidence in the DriveLM results.

- **Visual chain-of-thought inference procedure is underspecified.** Equation (8) shows a factored distribution p(A_box2D | Q) · p(A_box3D | Q, A_box2D), and Figure 4 (left) depicts two separate turns. It is unclear whether the 2D and 3D boxes are generated in a single autoregressive pass or in two separate forward passes. The paper should specify the inference protocol precisely.

- **"Any specialist model" claim is unsupported.** Section 3.3 states that CUBE-LLM can be prompted with "any specialist models" but only tests with CenterPoint (a LiDAR-based 3D detector). The claim about generalization to arbitrary specialists is speculative without even one additional experiment (e.g., a monocular 3D detector or an RGB-D method).

### Trivial

- No error bars or variance estimates are reported for any main result. While single-run evaluation is common in large-scale MLLM papers, the reported improvements would be more credible with even 2–3 seed runs.

## Nice-to-Haves

- An ablation comparing DINOv2 vs. CLIP directly on the core 3D benchmarks (e.g., Talk2Car zero-shot) would cleanly separate the contribution of the vision encoder swap from data scaling.
- The DriveLM-Grounding ablation in Table 2b shows a "CLIP → DINOv2" step that improves BEV AP_A from 33.2 to 39.6. The paper claims "pure data scaling," but this 6.4-point gain from DINOv2 alone is not attributed to data. Acknowledging this explicitly and ablating DINOv2 separately would strengthen the paper.
- Reporting results with a larger LLM backbone (e.g., 70B) would be informative about scaling laws for 3D reasoning, but is not required.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Pure data scaling" narrative vs. architectural changes (DINOv2, two-stage training) as a tension.** The paper's claim is "without 3D-specific architectural design or training objectives" — using DINOv2 (a general vision encoder, not 3D-specific) and two-stage training (a common MLLM procedure, not a 3D-specific objective) does not contradict this. The paper acknowledges these changes in Section 3.4. This criticism overstates a genuine but minor nuance into an apparent contradiction.

- **Missing related works on 3D reasoning from images.** Per guidelines, I cannot verify whether prior work exists on MLLM-based 3D reasoning from images, and the instruction forbids mentioning missing related works.

- **Formatting/style nitpicks and grammar complaints.** These are parser artifacts or standard presentation preferences, not substantive weaknesses.

- **Missing appendix references.** The paper explicitly states that appendices are removed by the parsing process.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify in the abstract and introduction** that the 21.3 AP_BEV improvement comes from the LiDAR-prompted variant (CUBE-LLM†), and report the camera-only numbers as well. This would not weaken the paper — the LiDAR-prompted setup is a genuine contribution — but would improve transparency.

2. **Add at least one external baseline to Table 3** (indoor 3D grounding), even a simple one like projecting ground-truth 3D boxes into 2D and back. This would anchor the absolute numbers.

3. **Add a data leakage discussion** for DriveLM/nuScenes overlap, even briefly stating that steps were taken to ensure no validation scene leakage.

4. **Specify the V-CoT inference procedure** — whether 2D and 3D boxes are generated in a single autoregressive pass or in two separate calls.

5. **Add an ablation** comparing DINOv2 vs. CLIP directly on a core 3D benchmark to separate the encoder choice from data scaling.

## Score and Decision

Score relative to anchors (all from the middle/upper-middle band):

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 3D-GRAND (i7hXOqzUcK) | 5.0 | 1 | Weaker: dataset-only contribution with no models trained on it; CUBE-LLM is a complete system with stronger experiments |
| 3D-AffordanceLLM (GThTiuXgDC) | 5.8 | 1 | Similar: both introduce LLM-based 3D systems with solid experiments; CUBE-LLM has broader scope (3D grounding from images vs. affordance segmentation from point clouds) |
| Coarse Correspondences (8ibaVk4mU8) | 4.67 | 1 | Weaker: simpler training-free method; CUBE-LLM requires substantial training/data curation effort |
| Spatial 3D-LLM (JzLcKWtGnl) | 4.33 | 1 | Weaker |
| Matryoshka MM (Uhj5OxAz7I) | 6.0 | 2 | Similar: both are solid accepted papers with clear contributions and minor weaknesses |
| MLLMs Know Where to Look (DgaY5mDdmT) | 7.0 | 2 | Stronger: tightly focused, clean findings; CUBE-LLM has broader engineering scope but less precision |
| CoVLM (PHGxChm1l5) | 6.33 | 2 | Similar |
| 3D-Spatial MM (XYdstv3ySl) | 6.5 | 2 | Similar |

**Round 1 bracket:** 5.0–7.0. **Round 2 narrowed** to 5.8–6.5. The paper is comparable to 3D-AffordanceLLM (5.8) and Matryoshka MM (6.0), slightly below MLLMs Know Where to Look (7.0). The core contribution is real and the experiments are broad, but the framing issues (abstract ambiguity, missing baselines for indoor eval) keep it from the top of the bracket.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>