- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 5, 6, 5, 5
Now I have thoroughly verified all claims against the actual paper. Let me construct the final review.

---

## Summary

This paper introduces PhyGenBench, a benchmark of 160 prompts spanning 27 physical laws across 4 domains (Mechanics, Optics, Thermal, Material Properties), and PhyGenEval, an automated three-stage hierarchical evaluation framework (key phenomena detection → order verification → overall naturalness) that uses VLMs to assess physical commonsense in text-to-video generation. Evaluating 8 T2V models, the paper finds that even the best model (Gen-3) scores only 0.51, providing quantitative evidence that current models are far from being "world simulators."

## Strengths

- **Comprehensive physical-commonsense benchmark covering diverse laws.** PhyGenBench includes 160 prompts across 27 distinct physical laws organized into four fundamental domains (Section 3, Figure 2). This breadth goes well beyond prior work like VideoPhy, which focuses narrowly on motion naturalness, enabling systematic assessment of whether T2V models capture intuitive physics.

- **Automated evaluation framework with strong human correlation.** PhyGenEval achieves a Spearman correlation of 0.81 with human judgments, far surpassing existing generic metrics (best competitor VideoScore: 0.19; Table 1). This provides direct evidence that the proposed hierarchical strategy effectively addresses the limitations of general-purpose video evaluation metrics for physics assessment.

- **Empirical demonstration that current T2V models remain far from world simulators.** Even the best-performing model, Gen-3, scores only 0.51 on the physical-commonsense alignment metric (Table 2). This result, derived from controlled prompts targeting simple everyday phenomena, quantitatively establishes a major gap.

- **Novel three-tier hierarchical evaluation design.** The decomposition of physical commonsense evaluation into Key Physical Phenomena Detection (single-frame), Physics Order Verification (multi-frame), and Overall Naturalness Evaluation (full-video) is a structured approach with clear motivation, compared to prior work that applies a single VLM judgment without exploiting temporal causality.

- **Qualitative evidence that existing metrics miss clear physical violations.** Case studies (Figure 6) show VideoScore and DEVIL misclassifying videos where an egg bounces like rubber or a rock floats on water, while PhyGenEval correctly identifies these failures. This concretely illustrates the benchmark's diagnostic value.

- **Rigorous prompt construction methodology.** The five-step pipeline (conceptualization → prompt engineering → augmentation → diversity enhancement → quality control) ensures one-to-one correspondence between each prompt and a single physical law, reducing confounding factors in evaluation (Section 3).

## Weaknesses

### Fatal
None.

### Major

- **Missing inter-annotator agreement.** Three annotators scored 512 videos, but the paper does not report any measure of inter-annotator agreement (e.g., Krippendorff's alpha, Fleiss' kappa, pairwise Spearman). For a benchmark that uses human judgments as the gold standard for correlation analysis, this is a standard requirement. Without it, the reliability of the human ground truth — and by extension the strength of the claimed ρ=0.81 correlation — cannot be fully assessed. This should be added.

- **Ablation study mentioned but no data presented.** Section 5 states: "Experimental results show that the key designs of PhyGenEval are essential" (line 286) with no table, figure, or quantitative comparison in the main paper. Given that the three-stage hierarchical design and the use of specific VLMs are central contributions, the ablation evidence must appear in the main text, not merely be asserted. The reader cannot evaluate the necessity of each stage without the data.

### Minor

- **Scoring scale description inconsistent with reported values.** The paper states that S_key, S_order, and S_natural are discretized into a four-point scale (0–3), averaged, and floor-rounded to produce the final score (line 194); similarly, human scores are described as "the average of the three scores and rounded up" (line 210). However, Table 2 reports values like 0.39, 0.45, 0.51, and 0.31 — clearly decimals, not integers. These appear to be normalized to [0,1] (likely divided by 3), but the text does not specify this normalization. The discrepancy is confusing and should be resolved. (Note: this does not affect the rank-based correlation results in Table 1, since Spearman and Kendall are invariant to linear scaling.)

- **Unclear how VideoPhy was adapted as a comparison metric.** The paper lists VideoPhy as a baseline in Table 1 and reports correlation values, but does not explain how VideoPhy — which is a benchmark with its own prompts and human annotations, not a general evaluation metric — was applied to score PhyGenBench videos. Was a classifier trained? Were human annotations from VideoPhy used directly? The methodology is uninterpretable without this clarification. (DEVIL is less of a concern since it provides an evaluation methodology applicable to arbitrary videos, as acknowledged indirectly via its use in the naturalness stage.)

- **Large gap between PhyGenEval and baselines (0.81 vs. 0.19) deserves discussion.** While the gap is plausible given that PhyGenEval is designed specifically for PhyGenBench, the paper does not discuss the extent to which this gap reflects genuine diagnostic superiority vs. benchmark-specific tailoring. A brief discussion of this point would strengthen the claims.

- **Agreement between the two VLMs used for naturalness evaluation not reported.** Both InternVideo2 and GPT-4o are used to compute S_natural, and their outputs are ensembled. Reporting their agreement (or per-model performance against humans) would provide insight into whether ensembling is necessary and which model is more reliable.

- **Keyframe localization with CLIPScore not explicitly validated.** The key physical events (e.g., the moment an egg first cracks) are assumed to align with the frame that maximizes CLIPScore against a retrieval prompt. The paper mitigates this by considering adjacent frames (i±2), but does not validate that the selected frames actually correspond to the intended physical moments. A small-scale human verification would strengthen this core component.

### Trivial

- A complete enumerated list of all 27 physical laws with representative prompts (beyond the 4 examples in Section 3) would improve transparency and reusability.
- The number of prompts filtered or modified during the quality control step is not reported.

## Nice-to-Haves

- Validate keyframe selection with human judgments on a small sample to confirm CLIPScore locates the correct physical moments.
- Report statistical significance (confidence intervals or tests) for model-level differences in Table 2.
- Report per-component ablation (how much each stage contributes to the overall correlation with humans) to justify the three-tier hierarchy.
- A cross-benchmark generalization study (e.g., applying PhyGenEval to videos from another physics-related benchmark) would clarify whether the metric's strength is tied to PhyGenBench's specific prompt design.

## Removed Points

These points from the source reviews were filtered:

- **"VLM(I_j, p_r) appears twice in the summation, double-counting the retrieval prompt match"** — The term appears once per question in the sum over Q, which is a deliberate design choice (using the retrieval prompt match as a frame-relevance filter). The critic provides no evidence this actually harms scores. Speculative; removed.
- **"The paper should report how many prompts were filtered or modified at quality control"** — Trivial and already subsumed under the trivial weakness about reporting QC counts.
- **"The naturalness metric is highly dependent on the VLM's understanding"** — This is true of any VLM-based evaluation and not specific to this paper; already addressed by reporting agreement between two VLMs as a minor weakness.
- **"CLIPScore weakness is a potential problem"** — Kept in weakened form; the stronger version claiming it's a clear flaw without acknowledging the i±2 mitigation is removed.
- **"A small-scale human validation of keyframe selection would strengthen"** — Moved to Nice-to-Haves.
- **"Discussion section appears truncated"** — The Discussion section heading exists (line 295) but content is absent in the extracted text, consistent with a PDF parsing artifact, not an author error.
- **"Per-model correlation would help ensure consistency"** — With only 8 data points, per-model rank correlation would be statistically unreliable. Moved to Nice-to-Haves.
- **"The claim that scaling doesn't 'fully' address challenges is true but vague"** — The paper provides supporting evidence (2B→5B improvement from 0.39→0.45, yet still only 0.45) which substantiates the "does not fully address" claim. This is a reasonable interpretation of the data, not a weakness.
- **Strength Finder: generic/superficial strengths about "important problem"** — No such generic strengths appeared in the Strength Finder output; all listed strengths are concrete and paper-specific. None removed.

## Novel Insights

None beyond the paper's own contributions. The reviews do surface a useful framing point: the paper's key result (ρ=0.81 vs. 0.19) is simultaneously its strongest piece of evidence and a potential overclaim — the metric is purpose-built for this benchmark, so some gap is expected. The paper would benefit from acknowledging this explicitly and discussing where PhyGenEval might fail on prompts outside its design scope.

## Suggestions

1. **Add inter-annotator agreement metrics** (Krippendorff's alpha or pairwise Spearman) for the human evaluation. This is essential for any benchmark paper using human judgments as ground truth.
2. **Move the ablation study into the main paper** with a table showing the contribution of each stage and each VLM choice to overall correlation.
3. **Clarify the scoring normalization**: explicitly state that per-prompt scores in the 0–3 range are averaged across prompts and normalized to [0,1] when reporting model-level scores in Table 2.
4. **Explain how VideoPhy was operationalized** as an evaluation metric on PhyGenBench videos.
5. **Validate a subset of keyframe selections** via human inspection to confirm CLIPScore locates the correct physical moments.
6. **Add a brief discussion** of why the gap between PhyGenEval and baselines is so large and whether the metric's benchmark-specific design is a factor.
