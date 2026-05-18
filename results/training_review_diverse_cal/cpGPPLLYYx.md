Now I have a thorough understanding of the paper and all reviewer claims. Let me compile the final review.

---

## Summary

This paper introduces VL-ICL Bench, the first comprehensive multimodal benchmark specifically designed to evaluate in-context learning (ICL) in vision-language models (VLLMs). The paper first demonstrates that existing VQA and captioning benchmarks are inadequate for ICL evaluation (few-shot gains largely reflect answer-format learning rather than true task learning), then proposes a suite of ten tasks spanning image-to-text and text-to-image generation, fast concept binding, perception, induction, reasoning, interleaving, and long-context challenges. Evaluations of 15+ VLLMs reveal that even the best models (LLaVA-OneVision-72B, GPT4V) struggle on several tasks, and that many models show non-monotonic shot scaling, negative ICL efficiency, and significant headroom for improvement.

## Strengths

- **Identifies and empirically validates the inadequacy of VQA/captioning for ICL evaluation.** Section 2.2 (Figure 1) cleanly demonstrates that few-shot gains on MathVista, VizWiz, and COCO Captioning nearly vanish when using LLM-based evaluation instead of exact match, confirming that existing benchmarks primarily measure answer-format adaptation rather than genuine multimodal ICL. This directly motivates the need for a dedicated benchmark.

- **Introduces a diverse, comprehensive benchmark spanning genuinely challenging ICL scenarios.** Table 1 describes ten tasks covering both image-to-text and text-to-image generation, fast concept binding (synthetic names), fine-grained perception (TextOCR), rule induction (Operator Induction, CoBSAT), reasoning, interleaved images, and long-context challenges. The benchmark is compact (1.82 GB total) yet covers a broader range of ICL-relevant capabilities than any prior multimodal evaluation suite.

- **Rigorous evaluation of 15+ VLLMs reveals non-trivial ICL and concrete failure modes.** Tables 2 and 3 show that, unlike in VQA/captioning, every task in VL-ICL Bench has low zero-shot performance and meaningful ICL improvement for at least one model. Results also surface non-monotonic scaling (e.g., GPT4V on CLEVR Count Induction, performance dropping with more shots), negative ICL efficiency in many models, and the finding that zero-shot strength does not predict ICL ability (e.g., LLaVA-Next-7B).

- **Additional analyses disentangle key factors limiting multimodal ICL.** Section 4.3 provides controlled experiments isolating specific challenges: fast vs. real-world concept binding (Table 4), text-only vs. multimodal input (Figure 3), context-extension via SelfExtend (Table 5, showing context length is not the sole bottleneck), and emergent ICL with model scale (Figure 4, showing the 72B model improves with shots while 0.5B/7B models fail within the same LLaVA-OneVision family).

- **Systematic comparison of text-to-image models** (Table 3) fills a gap largely ignored by prior work, which focused almost exclusively on image-to-text. The benchmark reveals that text-to-image models exhibit more consistent shot scaling, and provides a standardized evaluation framework for this less mature area.

## Weaknesses

### Fatal
None.

### Major

- **The `[Task Description]` field in the prompt template (Section 4.1) is never specified.** The paper presents a prompt template containing the bracketed placeholder `[Task Description]` but never states what (if anything) was placed there for each task. The paper's task descriptions consistently emphasize that models must induce the task *from examples* (e.g., CLEVR: "models must learn to solve tasks... from examples rather than explicit prompts"; TextOCR: "we focus on evaluating whether the task can be induced by way of example through ICL"), and the zero-shot results are 0% for many tasks, which together strongly imply the task description was generic or empty. However, this is never stated explicitly. If the `[Task Description]` contained task-specific instructions (e.g., "Count the number of red objects"), the benchmark would conflate zero-shot instruction-following with ICL, undermining its core claim. This is a documentation gap that must be closed for the benchmark's validity to be fully assessable. The authors should disclose the exact content of this field for every task and ideally provide the full prompts used.

- **Absence of variability/error metrics across seeds.** Results are reported as averages over three random seeds (line 160), but no standard deviations, confidence intervals, or per-episode ranges are provided. Several tasks have very small test sets (Operator Induction: 60 test examples; Fast Counting: 40 test examples), where three-seed variance could be substantial. The paper makes comparative claims (e.g., "LLaVA-OneVision 72B is the best overall model", "negative ICL efficiency") without error characterization. For a benchmark whose primary contribution is measurement, readers need to know whether observed differences are reliable.

### Minor

- **Limited validation of the text-to-image judge.** The evaluation of text-to-image tasks relies solely on LLaVA-Next-7B as an automated judge (Section 4.1) to determine whether generated images contain the correct attributes, counts, etc. No human agreement study, comparison to ground-truth labels, or consensus with an alternative judge (e.g., GPT-4V) is reported. A single VLLM judge may introduce systematic biases (e.g., better at recognizing some attributes than others) that could confound model rankings.

- **The emergent threshold analysis (Figure 4) is based on a single model family.** The conclusion about "emergent ICL abilities at 72B" is drawn solely from the LLaVA-OneVision series (0.5B, 7B, 72B). While this is a clean controlled comparison, the observation is suggestive rather than generalizable. The authors should explicitly acknowledge this limitation rather than presenting it as a general finding about model scale.

- **The motivation analysis (Figure 1) covers only three benchmarks (MathVista, VizWiz, COCO Captioning).** While these are representative and widely used, the paper argues broadly that "VQA and captioning benchmarks are poor for ICL evaluation." The claim's strength would benefit from a larger or more diverse set of examples (e.g., OK-VQA, GQA), or at minimum an explicit acknowledgment of this scope limitation.

### Trivial
None.

## Nice-to-Haves

- Provide detailed full-prompt examples for at least one task from each category, including the exact `[Task Description]` content and a full support-set + query example.
- Include a "zero-shot with good prompt" baseline — i.e., what happens if the model is given the optimal task description without any support examples. This would validate that the benchmark is genuinely testing ICL rather than instruction following.
- Expand the text-only ICL comparisons (Figure 3) to systematically show which tasks benefit most from image inputs versus text inputs, better isolating the role of perception difficulty.
- Discuss how the benchmark's synthetic/simplified images (MiniImageNet, CLEVR, generated operator images) relate to potential real-world multimodal ICL applications (e.g., adapting to a new visual domain from a few examples).

## Removed Points

- *"The image-to-text and text-to-image dichotomy is not strictly maintained"* — The critic acknowledges "The classification is clear enough." The paper correctly classifies all tasks. Not a weakness.
- *"The motivation analysis is based on only three benchmarks"* (escalated from Removed) — Downgraded from the critic's framing to Minor above; the core point (three benchmarks is limited but still sufficient to make the point) is retained in Minor with softened severity.
- *Criticisms about missing appendix content* — The parser strips appendices; they exist in the original submission.
- *"Negative ICL efficiency" claim not being reliable without error bars* — Already covered in Major weakness about variability metrics.

## Novel Insights

The paper's most interesting finding beyond its own benchmark contributions is that zero-shot performance is *not* predictive of ICL ability in VLLMs — LLaVA-Next-7B is strong on zero-shot benchmarks but among the worst on VL-ICL Bench, while models like Phi3-Vision show relatively good ICL efficiency despite modest zero-shot performance. This suggests that VLLM training protocols (single-image vs. multi-image training, token allocation per image) may have a larger impact on ICL than on zero-shot inference, which has design implications for future VLLM development. The observation that text-to-image models show more consistent shot scaling than image-to-text models — attributed to training on more diverse interleaved datasets — is also a practically useful insight for model developers.

## Suggestions

- **Disclose the exact prompt format for every task.** State explicitly what the `[Task Description]` field contained for each of the ten tasks (e.g., "empty string," "Answer the question," or the exact phrasing used). Provide full prompt examples in the appendix. This is the single most important clarification needed.
- **Report variability.** Add standard deviations or interquartile ranges across seeds to all tables, or at minimum provide per-episode individual results in the appendix. This is especially important for tasks with fewer than 100 test examples.
- **Validate the T2I judge.** Report agreement rates between LLaVA-Next-7B and either human annotators or a second VLLM judge (e.g., GPT-4V) on a sampled subset of generated images. This does not need to be large-scale — even 50–100 images per task would substantially increase confidence in the evaluation.
- **Acknowledge the single-family limitation** of the emergent threshold analysis more explicitly in the main text.
- **Add a "zero-shot with informative prompt" baseline** for at least CLEVR Count Induction and TextOCR to directly demonstrate that the benchmark measures ICL rather than instruction-following.

## Score and Decision

The paper addresses a genuine gap — current VLLM ICL evaluation being dominated by VQA/captioning tasks that primarily measure format adaptation — and proposes a well-designed, diverse benchmark suite that genuinely requires and measures multimodal ICL. The benchmark tasks are well-motivated, the evaluation covers an impressive range of models, and the additional analyses (SelfExtend, text-vs-image, fast-vs-real binding, emergent scale) provide useful scientific insights beyond a simple leaderboard.

The weaknesses are real but primarily concern documentation/analysis gaps rather than fundamental methodological flaws. The prompt template ambiguity is the most consequential issue but is straightforward to resolve through disclosure. The missing error bars and T2I judge validation are standard rigor improvements that would strengthen the paper.

On originality, the paper makes a clear contribution — it is the first comprehensive multimodal ICL benchmark. The importance of the research question is high (properly evaluating ICL is critical as VLLMs proliferate). The claims are mostly well-supported, though the prompt template and error-bar gaps create some uncertainty. The experiments are sound in design but would benefit from better uncertainty characterization. The clarity is good overall, with the prompt template being the main opaque point. The value to the community is potentially high as a standardized evaluation resource.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>