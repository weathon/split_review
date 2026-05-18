Now I have a thorough understanding of the paper and can verify the reviewer's claims against the actual text. Let me compile my consolidated review.

## Summary

This paper proposes Chain-of-Region (CoR), a framework that combines traditional computer vision techniques (connected components, thresholding, contour detection) with VLMs for scientific diagram analysis. The pipeline decomposes diagrams into visual regions using CV-based initialization, VLM-assisted structure recognition, rule-based splitting, and hierarchical merging, then collects shape/semantic metadata from each region to augment the VLM prompt. Evaluated on a 5,210-image scientific subset of the MMMU dataset, CoR shows consistent accuracy improvements over several baselines, and a segmentation analysis reports mIoU gains of 20.8% (individual) and 13.0% (grouped) over SAM2 on a custom 100+ sample set.

## Strengths

1. **Novel, well-motivated integration of traditional CV with VLMs for structured diagrams.** The paper identifies a key property of scientific diagrams (homogeneous colors, structured patterns) and exploits it with cheap, interpretable OpenCV routines (Otsu thresholding, connected components, contour-based shape detection) instead of deep segmentation. This insight is clearly articulated in Section 1 and forms the foundation of the entire CoR pipeline.

2. **Consistent accuracy gains across a broad range of scientific sub-categories.** Table 1 shows CoR (with GPT-4o) outperforming all baselines (raw VLM, zero-shot CoT, few-shot CoT, SAM2, SoM) on every listed sub-category. The text reports that CoR achieves notably large margins on some categories (e.g., Chemistry: CoR 0.73 vs. raw 0.42; SAM2 0.53). This breadth supports the claim that the approach generalizes across different scientific domains rather than working on one specific diagram type.

3. **Qualitatively cleaner segmentation masks for fine-grained diagram elements.** Figure 5 provides a direct visual comparison showing that CoR captures fine lines, annotations, and small objects that SAM2 misses or merges. Table 2 quantifies this with mIoU improvements of 20.8% (individual) and 13.0% (grouped) over SAM2 on a challenging custom subset, supporting the claim that traditional CV-based decomposition is better suited to structured scientific diagrams than deep segmentation.

4. **Cost-effective and plug-and-play design.** The CV pipeline runs on CPU in milliseconds (Section 1), requires no fine-tuning or dataset preparation, and can be appended to any off-the-shelf VLM. These practical advantages over fine-tuning-based approaches are clearly articulated in Sections 1 and 2.

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled VLM query budget confounds the main QA comparison.** CoR uses up to 10 intermediate VLM calls for structure recognition (Section 3.1.2: "pre-defined recognition call limits (ex. 10) per diagram") plus one VLM call per merged region for semantic information (Section 3.2, budget B=5) plus one final answer call — totalling up to ~16 VLM calls. The SAM2 baseline (Section 4.1) uses the same sequential inference strategy and information collection phase but does NOT use the intermediate VLM structure recognition calls. The single-call baselines (Raw, zero-shot CoT, few-shot CoT, SoM) each use exactly 1 VLM call. Because CoR's VLM budget is an order of magnitude larger, it is impossible to tell from the reported results whether CoR's improvements come from better region masks or simply from spending more VLM inference budget. The paper's claim that "CoR outperforms SAM2 by utilizing superior regional masks" (Section 4.1) is unsupported without controlling for this variable.

2. **Segmentation evaluation uses a biased, non-representative sample with a metric that favors the method's granularity.** The custom segmentation dataset is "constructed from instances where the raw predictions of GPT-4V failed" (Section 4.2) — a survivorship-biased sample that deliberately selects the hardest cases for the baseline VLM. This does not provide information about segmentation quality on the broader population of diagrams. Furthermore, the region-matching strategy ("for each ground truth region, select the predicted region with largest overlap") systematically favors methods that produce many small regions (CoR's connected-components-based approach) over methods that produce coarser segments (SAM2), because small predicted regions can match small ground-truth regions with high IoU while SAM2's larger segments spanning multiple ground-truth regions incur penalties. The reported 13–20% mIoU advantage may therefore reflect a difference in granularity rather than in segmentation quality. A representative (random) sample and a measurement that accounts for over-segmentation would be needed to substantiate the claim of "superior regional masks."

### Minor

3. **Key assumption about diagram characteristics is untested.** The method critically depends on diagrams having "homogeneous colors and structured patterns" (Section 1) for Otsu thresholding and connected components to produce meaningful initial regions. The paper provides no analysis of what fraction of the 5,210 MMMU diagrams satisfy this property, nor what happens when they do not (gradients, overlapping semi-transparent elements, anti-aliased text, color diagrams where binarization destroys structure). A failure-case analysis or per-category breakdown by diagram complexity would clarify the method's scope.

4. **Incompletely specified algorithm hinders reproducibility.** The following details are absent: (a) the exact prompt used for VLM-assisted structure recognition (Section 3.1.2 says only "a prompt-based query... which suggests possible structural categories"); (b) the set of structural categories and parameters for shape detectors (e.g., which OpenCV functions are used for rectangle/ellipse/line detection, and with what thresholds); (c) the specific OCR tool (cited as "Contributors, 2024"); (d) the linkage criterion and distance metric for AgglomerativeClustering (Section 3.1.3 specifies only centroid-based distances, which neglect shape and adjacency cues).

5. **Internal contradiction about hyperparameter sensitivity.** Section 4 states "Given their minor impact on the final algorithm, we do not engage in an extensive discussion on these parameters" — yet the sensitivity analysis in the same section reports that the cluster number "significantly impacts performance" with an inverted-U trend spanning ~8% accuracy variation. The paper acknowledges the cluster number's importance for future work on dynamic selection, so the contradiction is in the framing rather than the evidence, but it should be resolved.

6. **No inter-annotator agreement reported for the segmentation ground truth.** The custom segmentation dataset used in Table 2 relies on human annotators generating "individual" and "grouped" masks with "up to five cohesive semantic regions" (Section 4.2). Without inter-annotator agreement statistics, the reliability of this ground-truth data is unknown, which weakens the segmentation evaluation.

### Trivial

7. **White-box claim is partially overstated.** The paper lists "White-box Algorithm" as an advantage (Section 1), but the VLM calls (both structure recognition and semantic extraction) are black-box. The paper specifically qualifies this as being about "region separation methods" (Section 1), so this is a framing nuance rather than an error, but the overall system is hybrid and the interpretability of the CV component does not extend to the VLM reasoning.

8. **No confidence intervals or statistical tests on main results.** Table 1 reports only point estimates. While single-run evaluation is common in large-scale VLM benchmarks, the absence of any variance estimate makes it unclear whether smaller margins (e.g., 0.3–2.8% on some sub-categories) are meaningful.

## Nice-to-Haves

- An ablation that limits CoR's intermediate VLM calls to zero (using only the CV-based decomposition without VLM-assisted structure recognition) would isolate the contribution of the region masks from the extra VLM processing budget.
- Reporting per-region IoU broken down by region size (large background elements vs. small annotations) would clarify whether CoR's granularity is always beneficial or sometimes harmful.
- A computational cost comparison (total VLM API cost + CV runtime per diagram) would help practitioners assess the practical trade-off.
- The exact prompts for VLM-assisted structure recognition and semantic information extraction should be included in an appendix for reproducibility.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The paper does not specify whether SAM2 also uses intermediate VLM calls"** — The paper does specify this (Section 4.1, method 4). SAM2 applies the same sequential inference strategy and the same information collection phase but using SAM2's initial segments instead of CV-based regions. The paper is clear that the structure recognition step is CoR-specific, so the reviewer's own analysis of the SAM2 baseline being controlled at the information-collection level is actually correct; the issue is about the *structure recognition* calls. Kept the controlled substance in Major #1 above.

- **"The paper generates ground-truth segmentation masks... but does not report how the 'up to five cohesive semantic regions' instruction was operationalized"** — The paper describes this as "grouped segmentation masks... aggregate the visual elements into up to five cohesive semantic regions per image" (Section 4.2). The instruction is described, albeit briefly. Kept as Minor #6 (inter-annotator agreement missing) but the quote about the instruction itself is in the paper.

## Novel Insights

The most interesting tension in the reviews is that the Strength Finder and Harsh Critic essentially agree on the paper's core claim (CV-based decomposition helps VLMs on diagrams) but disagree on whether the main experiment (Table 1) actually supports it, because the comparison is confounded by VLM query budget. This reveals a common blind spot in VLM-augmented prompting papers: comparing a multi-step prompting method against single-call baselines conflates inference compute with prompt quality. The true test is whether the method helps *given the same total VLM budget* — and that test is absent here. This insight is worth flagging because it applies broadly to the "augmented prompting" literature.

## Suggestions

1. The most impactful improvement would be to control VLM query budget in the main QA experiments. Run the SAM2 baseline with the same number of intermediate structure-recognition calls as CoR (even if the calls are structure-irrelevant), or run CoR with zero intermediate calls to isolate the mask quality contribution.

2. For the segmentation evaluation, construct a random sample from the full MMMU scientific subset (not just GPT-4V failures) and report mIoU on that representative set. Also report a metric that penalizes over-segmentation (e.g., covering-based IoU or boundary F1) alongside the current matching-based mIoU.

3. Resolve the internal contradiction about the cluster number's impact and include explicit reproducibility details (prompts, detection parameters, clustering linkage) in an appendix or the camera-ready version.

## Score and Decision

The paper presents a genuinely novel and well-motivated idea — using cheap, interpretable CV operators for diagram decomposition before VLM analysis. The qualitative segmentation improvements are convincing, and the concept is clearly superior to SAM2 for structured diagrams on visual inspection. However, two structural weaknesses significantly undermine the quantitative evidence: (1) the main QA comparison does not control for VLM query budget (CoR uses up to ~16× more VLM calls than single-call baselines), making it unclear whether the gains come from better masks or simply more inference; (2) the segmentation evaluation uses a biased sample with a metric that favors the method's granularity. These are addressable in revision but require real experimental work. The paper has genuine merit and a clear contribution, but in its current form the evidence does not fully support its strongest claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>