Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper proposes Storybooth, a training-free approach for multi-subject consistency in visual storytelling. It diagnoses "self-attention leakage" as the root cause of inter-character feature mixing when scaling cross-frame self-attention to multiple characters. The method combines (1) LLM-based spatial planning with chain-of-thought reasoning to localize characters across storyboard frames, (2) bounded cross-frame self-attention with dropout to limit each character's tokens to attending only to the same character's tokens intra-frame and inter-frame, and (3) cross-frame token merging (with a negative unmerging phase for pose diversity) to align fine-grain details. The paper reports improved character consistency and T2I alignment over prior training-free and training-based baselines, with ~8.7s inference time (×30 faster than optimization-based methods).

## Strengths

- **Clear problem diagnosis and well-motivated method design.** Section 3 and Figure 3 convincingly visualize the self-attention leakage problem — tokens of one character (e.g., dog) attending to tokens of another (e.g., cat) when cross-frame self-attention is naively shared. The proposed bounded self-attention (Eqs. 3–6) directly targets this diagnosed issue, and the dropout mechanism (β_d) is a pragmatic fix to preserve image quality while reducing leakage. The connection between diagnosis and solution is one of the paper's strongest aspects.

- **Training-free with substantial speed advantage.** The paper's claim of ×30 faster inference than optimization-based methods (8.7s vs. ~5–7.5 min for Dreambooth-LoRA / Textual Inversion) is directly supported by the reported numbers on the same hardware (single H100, SDXL base). This is a practically meaningful advantage — the method requires no per-subject fine-tuning, which is the paper's stated goal.

- **Novel adaptation of token merging with negative unmerging for pose diversity.** The idea of using the bounded self-attention map to guide cross-frame token merging (Eq. 7) is a clean extension of prior token merging work to the consistency setting. The negative α for early diffusion steps (α=−0.5, t∈[1000,950]) to increase pose variance, followed by positive α for fine-grain alignment, is a novel and well-motivated contribution that addresses a real limitation of aggressive merging.

- **Qualitative results show visible improvements over prior methods.** Figures 7 and 8 demonstrate that Storybooth substantially reduces inter-character leakage compared to StoryDiffusion and ConsiStory (e.g., mouse/hedgehog features not mixing, monkey/human features staying separate). These qualitative gains are visually apparent and consistent with the paper's stated goal.

## Weaknesses

### Major

- **Multi-subject evaluation dataset is completely undescribed.** The paper states that "the storyboard prompt dataset from Tewel et al. (2024) is used for evaluating single-subject generation" but provides no information about the multi-subject evaluation — not the number of prompts, how many characters per prompt, how character types were selected, whether prompts are balanced, or how many seeds/runs were used. Without these details, the reader cannot assess the breadth or fairness of the quantitative evaluation. This is the single most significant evidential gap, as the paper's core claim is improved *multi-character* consistency.

- **No variance or confidence intervals reported for any quantitative metric.** Table 1 reports point estimates for CC (Dreamsim) and T2I alignment (VQAScore), but no standard deviations, confidence intervals, or statistical significance tests are provided. Given that diffusion models exhibit high variance across random seeds, it is unclear whether the reported improvements over StoryDiffusion and ConsiStory are statistically meaningful or fall within the noise. This weakens the quantitative evidence substantially.

### Minor

- **Ablation study is qualitative and limited to one example.** The ablation (Fig. 9, described in line 167) examines one storyboard (bear/lion) and discusses effects qualitatively (self-attention bounding prevents leakage, token merging aligns fine details, negative unmerging increases pose variance). While the conclusions are plausible and consistent with the method's design, the absence of any quantitative ablation (e.g., measuring CC/VQAScore with each component removed across multiple prompts) means the contribution of each component is asserted rather than demonstrated. For a method with multiple moving parts (LLM planning, bounded self-attention with β_d, token merging with α schedules), this is a notable gap.

- **β_d hyperparameter value not disclosed.** The dropout parameter β_d (Eq. 4) is introduced as "a small dropout-probability" but its actual value is not stated in the main text. This is a key hyperparameter — too low and image quality suffers, too high and inter-character leakage returns — and its omission makes the method harder to reproduce and the sensitivity analysis impossible.

- **Baseline configuration details missing.** The paper states that all methods use SDXL on an H100 GPU, but does not specify: whether baselines (StoryDiffusion, ConsiStory, IP-Adapter, BLIP-Diffusion) were run using their original code, whether any adaptation was needed for the multi-character setting, or how reference images were selected for encoder-based methods (IP-Adapter, BLIP-Diffusion). The choice of reference images can drastically affect the comparison, and this information is needed to evaluate fairness.

### Trivial

- None of the remaining points rise to the level of a meaningful weakness. The reliance on supplementary material for LLM prompt details, the qualitative nature of the attention analysis, and the timestep interval choices for negative unmerging are all within standard practice for this type of paper.

## Nice-to-Haves

- A small-scale validation of LLM layout accuracy (e.g., IoU between predicted masks and human-annotated masks on a handful of prompts) would strengthen confidence in the planning step.
- A discussion of failure cases (e.g., when character masks overlap, when the LLM produces inconsistent layouts across frames) would set realistic expectations for practitioners.

## Removed Points

These points were raised in the reviews but are excluded from the main weaknesses for the following reasons:

- **"Table 1 appears to be an image and is not legible"** — This is a PDF parsing artifact; the original submission has a legible table. Removed as a formatting artifact.
- **"User study details not disclosed"** — The paper references Appendix C for user study details. While the appendix is stripped in this parsed version, pointing to supplementary material for implementation details of a user study is standard practice. Removed as an appendix-stripping artifact.
- **"Comparison fairness is questionable" framing that baselines may have been disadvantaged** — Concerns about unfair advantage favoring the proposed method vs. baselines are not supported by evidence; the paper describes using the same base model and hardware. If there is any asymmetry, it is not demonstrated to favor the proposed method. Removed as speculative.
- **"The LLM planning step is not validated" / "Failure cases not analyzed"** — These are nice-to-haves that go beyond what is standard to expect in a main conference paper. Deferred to Nice-to-Haves.
- **Strength about "ablation experiments validate each component's contribution"** — Conflicts with the verified weakness that the ablation is qualitative on one example. Removed per the rule that weakness wins when strength and weakness disagree.
- **Strength about "67–74% preference in user study"** — The specific percentages are in an image table (Table 2) and cannot be verified from the text. The paper's text only claims "majority preference." Removed as unverifiable from text; the qualitative claim of majority preference is retained.
- **Strengths about "important problem" / "important research question"** — Generic and superficial. Removed per filtering instructions.
- **Requests for "statistical significance tests" framed as fatal** — The absence of significance tests is a real weakness but not fatal; the qualitative and user study evidence provide corroboration. Retained as a Major weakness but reframed from fatal to major.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the evaluation gaps but do not contribute any new technical insight or alternative framing that the paper itself does not already provide.

## Suggestions

1. **Describe the multi-subject evaluation dataset explicitly** in the main text: number of prompts, number of characters per prompt, source, diversity of settings. This is the single highest-leverage fix.
2. **Report standard deviations or confidence intervals** for all quantitative metrics in Table 1, ideally over multiple seeds. A paired bootstrap comparing Storybooth against each baseline would substantially strengthen the evidence.
3. **Add a quantitative ablation** over at least 10–20 prompts, measuring CC and T2I alignment with each component removed (no bounding, no token merging, no negative unmerging). This would directly support the claim that all three components matter.
4. **Disclose the β_d value** used in all experiments, and ideally include a sensitivity analysis showing how varying it affects the consistency-quality trade-off.

## Score and Decision

The paper makes a clear and well-motivated contribution: diagnosing self-attention leakage for multi-character consistency and proposing a practical, training-free solution with visible qualitative improvements and a meaningful speed advantage. The methodology is sound and clearly presented. However, the evaluation has meaningful gaps — the multi-subject test set is undescribed, no variance is reported for any metric, and the ablation is qualitative on a single example. These weaken the quantitative evidence but do not invalidate the core contribution, which is supported by strong qualitative results and a user study. The paper would benefit from a revision addressing these evaluation gaps, but in its current state it presents a sufficiently clear contribution and compelling qualitative evidence.

**Score: 6.5**

**Decision: Accept**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>