Now I have thorough evidence. Let me produce the final consolidated review.

## Summary

ReForm-Eval proposes a large-scale LVLM benchmark by re-formulating 61 existing task-oriented multimodal datasets into unified multiple-choice or text-generation formats, spanning 8 capability dimensions. The paper introduces both black-box (generation with in-context learning) and white-box (likelihood-based) evaluation, along with an instability-aware protocol to measure prompt sensitivity. Experiments on 16 LVLMs analyze how architecture, pretraining data, and instruction-tuning diversity affect performance.

## Strengths

- **Large-scale benchmark via systematic re-formulation of 61 datasets:** ReForm-Eval re-uses existing resources to construct a benchmark roughly 100× the size of MMBench without manual annotation, spanning 8 capability dimensions from coarse-grained perception to multi-turn dialogue (Section 3.2, Introduction). This directly delivers on the paper's central contribution of providing substantial evaluation data.

- **Dual evaluation strategy (generation + likelihood) with instability awareness:** The paper provides both black-box (in-context guided generation) and white-box (likelihood-based) evaluation methods for multiple-choice problems, complemented by an entropy-based instability metric across multiple instruction templates and option orders (Section 3.3). The in-context samples raise format adherence to nearly 100% (Table 4), demonstrating the effectiveness of the black-box approach.

- **Quantitative characterization of LVLM instability:** The paper isolates and measures three sources of instability (instruction variation, option order shuffling, option mark randomization) and reports that option-order shuffling causes the largest instability (0.55 on average, Table 5). This provides a concrete analytical tool that goes beyond accuracy-only evaluations.

- **Comprehensive model analysis identifying actionable factors:** Using ReForm-Eval, the paper evaluates 16 LVLMs and conducts analyses isolating the influence of visual/language backbones, connection modules, pretraining data quality, and instruction-tuning diversity (Figures 2-5, Tables 2-3), providing specific recommendations such as preferring ViT-G visual backbones and carefully selecting compatible connection modules.

## Weaknesses

### Fatal

None.

### Major

- **Distractor quality for multiple-choice questions is unvalidated (structural):** The most critical shortcoming. The paper states that for open-ended tasks, negative options are obtained "with the help of task-specific strategies or LLMs like ChatGPT" (line 72-73), but provides no concrete examples, no manual verification, no analysis of distractor plausibility, and no ablation. If distractors are trivial (obviously wrong), accuracy will be inflated and fail to reflect real capability differences. This is not a minor ablative detail — it is the foundational validity of the multiple-choice reformulation. Compare this to MMBench, which documents distractor sources per dataset. Without validation, the accuracy numbers reported in Table 1 are ungrounded for open-ended tasks.

- **Claimed "zero-shot" evaluation ignores extensive training data leakage:** The paper frames its evaluation as measuring "zero-shot capabilities" (line 18), yet many of the 61 reformulated datasets — including MSCOCO, VQA v2, GQA, and ScienceQA — are commonly used during the pretraining or instruction-tuning of the evaluated models. For instance, BLIP-2 and InstructBLIP are explicitly pretrained on MSCOCO, yet MSCOCO appears in the fine-grained perception, cross-modal inference, and visual description dimensions. The paper itself discusses MSCOCO's impact in Section 4.3.2 but does not flag which evaluations are genuinely zero-shot vs. confounded by training overlap. The commented-out notation in Section 4.1 ("% Star marks are utilized to indicate non-zero-shot results") suggests the authors considered this issue but did not implement it. This undermines the paper's comparative analyses (backbone, data quality, etc.) and the conclusion that certain models are "top-2."

- **Architecture and data analyses are confounded by multiple uncontrolled variables:** The analyses in Sections 4.3.1-4.3.2 group models by visual backbone (ViT-G vs. ViT-L), connection module, or pretraining data exposure (e.g., "with vs. without MSCOCO"), but these groups differ simultaneously in language backbone, total parameter count, training recipe, and data composition. For example, ViT-G models (BLIP-2, InstructBLIP) also use Q-Former and FlanT5/Vicuna, while ViT-L models use diverse connection modules and language backbones. Similarly, Figure 3(a)'s comparison of "with MSCOCO" vs. "without MSCOCO" groups models that differ in architecture and data scale. The paper presents these as causal findings, but they are at best correlational.

### Minor

- **Likelihood evaluation specification for encoder-decoder models is incomplete:** The paper states the likelihood formula "is parameterized by the causal-LLM-based LVLMs" (line 144), yet several evaluated models — BLIP-2_F and InstructBLIP_F — use FlanT5, an encoder-decoder architecture. While the likelihood computation can conceptually be adapted (using the decoder to score each option), the paper does not specify how this is done, leaving the results for these models in Table 1 under-specified compared to the causal-based models.

- **Per-dataset results are not reported; aggregation masks important variance:** Table 1 aggregates many heterogeneous datasets into 8 single scores per evaluation mode (e.g., VGR includes VQA v2, GQA, Whoops, OK-VQA, ScienceQA, VizWiz, etc.). These datasets differ substantially in difficulty and format (ScienceQA already has human-curated multiple-choice, while VQA v2 is open-ended). Averaging them obscures which specific capabilities drive the rankings, making it difficult to assess whether conclusions (e.g., "BLIP-2 and InstructBLIP hold top-2 positions") are robust across individual datasets.

- **Option-order instability (0.55) is noted but its implications for benchmark validity are underexplored:** The paper reports that shuffling option order causes an average instability of 0.55 (Table 5) — meaning models change their answers more than half the time when options are reordered. The paper attributes this to "option preference" but does not investigate whether it is systematic (e.g., a left-option bias) or task-dependent, nor whether it renders the multiple-choice format unreliable for certain models or tasks.

### Trivial

None.

## Nice-to-Haves

- A small-scale validation experiment comparing accuracy on reformulated vs. original open-ended datasets (e.g., VQA v2) to demonstrate that distractors are non-trivial.
- A per-model audit of which of the 61 datasets were seen during training, with appropriate flags or filtering.
- Concrete examples of the ChatGPT prompts used for distractor generation, with examples of easy vs. hard distractors.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"In-context example 'Can you see the image?' sets answer-preference bias"** — The paper explicitly states (line 136) that the in-context sample "provides no information about the image." The example teaches output format, not content. This is a standard approach and not a bias concern. (Misunderstanding of the paper.)

- **"Shuffling option order masks systematic failure"** — The paper deliberately studies option-order sensitivity as part of the instability analysis (Section 4.3.5) and transparently reports it as a finding. Averaging across orders to obtain a robust score is a principled methodological choice, not a flaw. (Misunderstanding of the methodology.)

- **"Prompts for text-generation problems are undescribed"** — The paper describes these prompts in lines 124-125, including the use of CIDEr for description and word-level accuracy for STP with "well-designed" input prompts. (Contradicted by the paper.)

- **"Average rank is not a principled aggregation"** — Average rank is a standard aggregation method used across many benchmark papers. This is a subjective formatting nitpick rather than a substantive criticism. (Nitpick.)

- **"No total sample count for the 100× MMBench claim"** — The paper provides the relative comparison; exact sample counts are a minor presentational detail. Not a substantive weakness. (Nitpick.)

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any insight about the paper that the paper itself does not already state or imply.

## Suggestions

1. **Validate distractor quality** — Add a human evaluation or automated analysis showing that distractors are non-trivial (e.g., that a random baseline or弱 model does not achieve near-chance accuracy). Provide examples of ChatGPT prompts and sample distractors in an appendix.

2. **Document training data overlap** — For each model in Table 1, report which of the 61 datasets were seen during pretraining or instruction-tuning. Flag non-zero-shot evaluations explicitly, and re-run the architecture/data analyses controlling for training overlap where possible.

3. **Clarify likelihood computation for encoder-decoder models** — Specify whether the encoder-decoder likelihood is computed via the decoder's conditional likelihood (which works for T5-family models equivalently to the causal formulation) or whether a different approach is used.

4. **Provide per-dataset results** — Include a supplementary table (appendix or linked resource) with per-dataset accuracy scores alongside the dimension-level aggregates, so readers can assess whether rankings are consistent across datasets within a dimension.

5. **Investigate option-order instability** — Analyze whether the 0.55 option-order instability reflects a systematic left-option bias, whether it is concentrated in particular models or tasks, and whether the instability metric correlates with model quality or is orthogonal to it.

## Score and Decision

This paper makes a notable contribution in scale (61 reformulated datasets) and methodology (dual evaluation + instability awareness). However, the lack of distractor validation and the unaddressed training-data leakage substantially weaken confidence in the reported numbers and the conclusions drawn from them. The confounded architecture/data analyses further limit the reliability of the paper's causal claims. These weaknesses are significant but addressable; they do not invalidate the benchmark as a resource.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>