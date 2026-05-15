Now I have thoroughly verified all claims against the paper. Here is my consolidated review.

---

## Summary

This paper proposes VideoPrompter, a training-free framework that enhances zero-shot video understanding by augmenting both the visual features (via a video-to-text model, Video-ChatGPT) and the class label representations (via GPT-3.5-generated language attributes, descriptions, and high-level action contexts). The method is evaluated across three zero-shot settings (action recognition, retrieval, time-sensitive tasks) on seven datasets with four different VLMs, showing consistent improvements.

## Strengths

- **Dual-side enhancement (visual + textual) is well-motivated and effective.** Prior LLM-based work (CUPL, etc.) only enriched the text classifier. VideoPrompter goes further by also enriching visual features via video-to-text descriptions. The ablation in Figure 4 confirms both sides contribute and their combination is better than either alone. The gains are substantial: e.g., CLIP on HMDB-51 goes from 37.5 → 50.79 (+13.29%), and on UCF-101 from 61.72 → 72.77 (+11.05%).

- **Consistent improvements across diverse settings with no training.** The method improves 4 different VLMs (CLIP, ViFi-CLIP, AIM, ActionCLIP) on action recognition (Table 2), boosts CLIP on retrieval (Table 3), and improves time-consistency scores (Table 4). All gains are obtained without fine-tuning or task-specific training.

- **Efficient prompt usage.** VideoPrompter uses only 3 language descriptors (attributes, descriptions, high-level context) plus one video-textual description, yet outperforms CUPL which uses 50 descriptors (Table 5). This demonstrates a practically meaningful reduction in complexity.

- **Thorough ablations on design choices.** The paper systematically studies: removing visual vs. textual branches (Figure 3-left), filtering of video descriptions (Figure 3-middle), temperature diversity (Figure 3-right), component removal (Figure 4), and action context integration (Table 6). This gives clear engineering insight.

- **Interpretability.** Figure 2 shows that individual language attributes can be visualized to explain which visual cues drove the model's prediction, a useful byproduct of the approach.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the empirical evidence presented.

### Minor

- **No variance reporting across runs.** All results are reported as single numbers with no standard deviation, confidence intervals, or indication of how many runs were performed. While single-run evaluation is standard practice in zero-shot video benchmarks, some of the reported improvements are small enough (e.g., +0.87% on SSv2 with ViFi-CLIP, +1.8% R@1 on text-to-video retrieval) that variance information would help establish reliability. The authors should at minimum acknowledge this limitation and ideally provide variance estimates.

- **The contribution of the high-level action context is not systematically evaluated.** The paper reports that GPT-3.5 fails on SSv2 (all actions grouped as "manipulating objects"), but provides no quantitative assessment of the quality of the generated hierarchies for other datasets (e.g., agreement with human annotation, impact of misgroupings). The claimed novelty of the "Tree Hierarchy of Categories" would be strengthened by such an evaluation. Without it, the reader cannot tell whether the gains from action context are attributable to good groupings or are simply an artifact of adding more descriptive text.

- **No control experiment isolating video-specific temporal understanding from general descriptive power.** The paper ablates VGPT (video captioner) vs. GPT-3.5 (text generator), showing both contribute. However, replacing VGPT with an image-level captioner (e.g., BLIP on keyframes) would help determine whether the VGPT gains come from video-specific *temporal* reasoning or merely from adding generic descriptive caption cues. The paper's "zero-shot" framing is technically correct (no target-task training), but VGPT itself is a strong video-language model; a cleaner isolation of its role would strengthen the analysis.

- **The weighting parameter β₂ (cosine similarity between video and description) is not analyzed.** The paper states β₂ is computed as cosine similarity, which is data-dependent and ranges in principle from 0 to 1. Showing the distribution of β₂ values across different videos or datasets, or analyzing whether weighting outperforms simple averaging, would improve reproducibility and insight.

### Trivial

- The synthetic dataset (SD) for time-sensitive tasks is not described in the paper beyond its name and citation to Bagad et al. (2023). A brief one-sentence description would aid self-contained reading.
- The Charades improvement (+1.4%, Table 4) is modest; the authors could discuss why the gain is smaller for real-world temporal reasoning compared to the synthetic dataset (+10%).

## Nice-to-Haves

- A control experiment replacing VGPT with an image captioner (e.g., BLIP on sampled frames) to isolate the value of video-specific temporal understanding.
- Statistical significance / variance estimates for key results.
- Human evaluation of the GPT-3.5-generated action hierarchies for at least one dataset (e.g., fraction of classes mis-grouped).
- Analysis of the distribution of β₂ values and their effect on performance.

## Removed Points

- **"No statistical significance invalidates the paper's core empirical contribution"** — Overstated. Single-run reporting is standard in zero-shot video benchmarks; the concern is real but minor, not fatal.
- **"Video-ChatGPT makes zero-shot framing misleading"** — The paper correctly uses "zero-shot" to mean no target-task training. The ablation in Figure 4 already isolates VGPT's contribution. The call for an image-captioner control is valid but the criticism as stated is too harsh.
- **"High-level action context is conceptually indistinguishable from prior work"** — The paper explicitly differentiates from Waffling (single context) and CHILS (fine-grained sub-division), and generates multiple high-level contexts via LLM, which is distinct. Removed as it misreads the paper.
- **"Missing critical baselines (XCLIP, A5 not adapted)"** — The paper's goal is to improve *base* VLMs, not to wrap competing methods. Scope creep.
- **"Synthetic dataset not described"** — The dataset is from Bagad et al. 2023 and cited; a one-line note would help but this is not a weakness.
- **"Retrieval improvements are modest"** — Factual observation but not a weakness; the paper reports them honestly.
- **"CUPL comparison not apples-to-apples"** — Table 5 includes CUPL+VGPT as a baseline; the comparison is properly scoped. Removed.
- Style/formatting nitpicks, missing appendices, grammar comments — all parser artifacts or irrelevant.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already articulate or acknowledge.

## Suggestions

1. Add variance estimates (mean ± std over 3-5 runs) for the main results in Table 2 and Table 3, or at minimum acknowledge the limitation explicitly.
2. Include a control experiment using an image captioner (BLIP on keyframes) instead of VGPT to isolate the benefit of video-specific temporal descriptions.
3. Provide human evaluation or quantitative quality metrics for the LLM-generated action hierarchies (agreement rate with a human-annotated grouping, impact analysis of misgroupings).
4. Analyze the empirical distribution of β₂ across videos/datasets.
5. Briefly describe the synthetic temporal dataset in the main text for self-contained reading.

## Score and Decision

The paper presents a clean, practical, and well-ablated framework for training-free zero-shot video understanding. The dual enhancement of visual and textual representations is sound and yields consistent improvements across multiple settings. While there are minor concerns about variance reporting and the strength of individual component isolation, none of the weaknesses undermine the core claims. The paper makes a substantive empirical contribution to the zero-shot video understanding literature.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>