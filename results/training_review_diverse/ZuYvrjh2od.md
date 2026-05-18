Now I have all the information needed. Let me write the consolidated review.

---

## Summary

ReForm-Eval proposes to re-formulate 61 existing task-oriented multi-modal benchmarks into unified multiple-choice and text-generation formats compatible with large vision-language models (LVLMs). The paper evaluates 16 open-source LVLMs across 8 capability dimensions and provides analysis of how model architecture, pre-training data quality, instruction-following ability, and prompt-instability affect performance. The core idea — reusing existing annotations at scale rather than constructing new benchmarks from scratch — is sensible and well-motivated.

## Strengths

- **Large-scale benchmark construction via re-formulation**: By systematically re-formulating 61 existing task-oriented benchmarks covering 8 capability dimensions (coarse/fine-grained perception, scene text, reasoning, spatial, cross-modal inference, description, dialog), ReForm-Eval provides substantially more evaluation data than manually annotated alternatives like MME and MMBench. This directly addresses the data-scarcity limitation of prior LVLM benchmarks.

- **Unified evaluation strategy with dual methods for multiple-choice**: The paper designs both a black-box in-context learning method (guiding models to output format-constrained responses) and a white-box likelihood-based method (Equation 1, directly computing generation probability over options). Table 4 demonstrates that in-context samples raise format hit rates from as low as 62.86% to near 100% for most models, validating the practical effectiveness of the black-box strategy — a concrete improvement over dataset-specific post-processing required by prior work like LVLM-ehub.

- **Instability-aware evaluation with an entropy-based metric**: The paper introduces a formal instability metric (entropy of the prediction distribution across multiple tests) and systematically quantifies sources of instability. Table 5 shows that option-order shuffling causes the largest instability (0.5523 in generation), providing novel quantitative evidence of LVLM sensitivity that goes beyond prior qualitative observations.

- **Extensive model analysis yielding actionable findings**: The paper evaluates 16 models and provides evidence-backed conclusions about architecture choices — e.g., Vicuna-based models outperform LLaMA-based ones (Figure 2), ViT-G visual backbones outperform ViT-L and ImageBind, and the connection module choice matters for different backbones (Table 2). These findings offer practical guidance for LVLM development.

## Weaknesses

### Fatal

None.

### Major

1. **Insufficient transparency of the multiple-choice re-formulation process (Section 3.1).** For a benchmark paper, the construction of the evaluation data is the central contribution. The description of how negative options (distractors) are generated is limited to a single paragraph: for close-vocabulary tasks, "we build relationships between categories based on which hard negative options are selected"; for open-ended tasks, "negative options can be obtained with the help of task-specific strategies or LLMs like ChatGPT." No concrete examples, no systematic rules per task type, no quality checks, and no human validation are reported. The paper does not state the number of options per question, whether all options are drawn from the dataset's own label space or externally generated, or whether any human verification was performed on a sampled subset. The credibility of every multiple-choice accuracy in Table 1 depends on whether the distractors are meaningful — poor distractors inflate scores, overly hard ones suppress them. This opacity is a significant shortcoming for a benchmark paper.

2. **Missing benchmark statistics.** The paper claims "almost 100 times the size of MMBench" (Section 1) but provides no exact numbers for total sample size, per-dataset sample counts, or whether full datasets or subsamples are used. MMBench has ~3k questions; 100× would be ~300k, but the 61 datasets include massive resources like ImageNet-1K (1.2M images) and MSCOCO (~120k images), making the actual total highly dependent on subsampling decisions. Without these basic statistics, the reader cannot assess whether the benchmark is genuinely "large" in a meaningful way or whether it is dominated by a few massive datasets. Per-dataset counts, distribution across dimensions, and average number of options per question are standard expectations for a benchmark release.

3. **Unclear handling of tasks that do not naturally map to multiple-choice (Section 3.2).** Several tasks listed under "Visual Cognition" and "Visual Perception" are intrinsically structured problems. Object grounding (RefCOCO, MSCOCO) typically requires referring expression comprehension or bounding box output; the paper states it is "formulated as multiple-choice questions" without explaining how. Spatial reasoning benchmarks like CLEVR involve compositional reasoning about object attributes — again, no explanation of the conversion. Multi-turn dialog (VisDial) requires dialog-aware options. Without concrete examples of how these conversions were done, the validity of the corresponding evaluation results cannot be assessed.

### Minor

1. **The claim "without the need for manual annotation" is somewhat overstated.** The abstract and conclusion state that ReForm-Eval provides data "without the need for manual annotation" (conclusion) or "reduces the manual effort" (abstract). While the benchmark reuses existing annotations (a valid and valuable approach), constructing high-quality multiple-choice questions still requires human effort: designing negative option generation strategies, crafting prompts for LLM-based option generation (where used), and ensuring the reformulation preserves task intent. The paper should be precise about what is automated and what required human judgment.

2. **Instability analysis limited to one dataset.** The investigation of instability sources (Table 5, Section 4.4) is conducted only on ScienceQA. While the results are illustrative, this is too narrow to support general conclusions about "current LVLMs." Replicating the analysis on at least 2-3 diverse datasets spanning different task types would substantiate the claims.

3. **Instruction templates not shown.** The paper mentions "multiple (more than five) instruction templates manually designed" for each task (Section 3.3.2) and provides one in-context example. The exact set of templates is not provided in the main text. While these may appear in supplementary materials, the evaluation's reproducibility depends on their availability and the templates being reasonable and diverse.

4. **Interpretation of the generation vs. likelihood gap.** The paper attributes the performance gap between generation and likelihood evaluation primarily to "limited instruction-following capability" (Section 4.3). This interpretation is plausible but not rigorously isolated — other factors such as model calibration, different sensitivity to option marking formats, or decoding strategy could contribute. The paper should discuss these alternative explanations.

5. **Limited positioning against other LVLM benchmarks.** The paper compares against MMBench (for scale) and LVLM-ehub (for evaluation methodology). While MME is cited in related work, there is no positioning table or comparison against other recent comprehensive LVLM benchmarks like SEED-Bench or MM-Vet, making it harder for readers to understand where ReForm-Eval fits in the ecosystem.

### Trivial

None.

## Nice-to-Haves

- A human validation study on a random subset of re-formulated questions to measure whether the correct answer is unambiguous and whether negatives are plausible would substantially strengthen confidence in the benchmark.
- Extending the instability analysis (Section 4.4) to 3-4 diverse datasets spanning different capability dimensions.
- A table positioning ReForm-Eval against existing LVLM benchmarks (MME, MMBench, SEED-Bench, MM-Vet, LVLM-ehub) along axes like: total samples, number of datasets, capability dimensions covered, evaluation formats, manual annotation required.

## Removed Points

These points were flagged by reviewers but are removed or downgraded per the filtering rules:

- **Criticism about object grounding not being multiple-choice compatible**: Kept in Major but note that object grounding can be re-formulated as selecting the correct referring expression among options — the paper's failure is not explaining this, not that the task is impossible to convert.
- **"No manual annotation" as a fatal overstatement**: Downgraded to Minor. The paper's core claim — reusing existing annotations rather than creating new ones — is valid and valuable.
- **Criticism about missing appendix content (instruction templates, per-dataset details)**: The parser strips appendix sections from all papers. The main-text description is still too vague, which is the valid core of the criticism.
- **Strength about "large-scale, comprehensive benchmark"**: Kept but qualified — the scale claim lacks precision (no exact numbers), which is captured as Weakness #2.
- **Weakness about CLEVR being compositional reasoning**: Kept as part of Major point #3 — the paper doesn't explain how any of these tasks are converted, not just CLEVR.

## Novel Insights

The paper's most striking finding — that option-order shuffling causes substantially larger instability (0.5523) than instruction variation (0.1607) or option-mark changes (0.3295) — goes beyond the usual observation that LVLMs are "prompt-sensitive." It specifically points to a misunderstanding of option content rather than instruction ambiguity. The analysis of likelihood vs. generation evaluation (Figure 5) also provides an interesting diagnostic: models based on FlanT5 and LLaMA2-Chat show the smallest gap between the two methods, suggesting that backbone instruction-following strength is a bottleneck for fair evaluation. These insights are genuinely useful for the community.

## Suggestions

1. **Open the black box of re-formulation.** Provide a concrete taxonomy of re-formulation strategies across the 61 datasets. For each major task type (classification, VQA, grounding, spatial reasoning, dialog), show: (a) how negative options are generated, (b) how many options per question, (c) what quality checks were applied. Include at least one worked example per capability dimension showing the original annotation and the re-formulated input.

2. **Report basic benchmark statistics.** Total number of multiple-choice questions, total number of text-generation samples, distribution across the 8 dimensions, per-dataset sample counts, and whether datasets are used in full or subsampled. State the average number of options per multiple-choice question.

3. **Release instruction templates.** Make all instruction templates publicly available alongside the benchmark to ensure reproducibility of the instability-aware evaluation.

4. **Add a small human validation study.** Sample ~100-200 re-formulated questions across task types and have human annotators judge whether the correct answer is unambiguous and whether the distractors are plausible but incorrect.

## Score and Decision

This paper tackles an important problem — enabling large-scale automated evaluation of LVLMs by reusing existing benchmarks — and provides extensive model analysis with several useful findings (architecture effects, data quality insights, instability characterization). The evaluation methodology (dual black-box/white-box, instability-aware metrics) is well-designed and represents real value.

However, for a paper whose core contribution is a benchmark, the construction process is documented at far too high a level. The re-formulation of 61 datasets into multiple-choice questions is described in a single vague paragraph, basic statistics (total sample size, per-dataset counts) are absent, and the conversion of tasks that are not naturally multiple-choice (object grounding, CLEVR, VisDial) is not explained. These gaps undermine confidence in every numerical result derived from the benchmark. The issues are fixable with substantial supplementary documentation, but in its current form, the paper does not provide sufficient evidence that the benchmark is well-constructed and trustworthy.

**MY FINAL SCORE: <pineapple>5.0</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**