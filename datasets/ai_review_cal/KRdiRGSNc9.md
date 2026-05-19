- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 5, 5, 5, 3
Now I have all the information I need to produce the final consolidated review.

---

## Summary

HumanEval-V is a benchmark of 108 entry-level Python coding tasks where visual information is *essential* for solving each problem. The paper constructs tasks by adapting problems from CodeForces/Stack Overflow through a collect-adapt-mutate pipeline, then evaluates 19 proprietary and open-weight LMMs. The results reveal very low performance (GPT-4o achieves only 13% pass@1, open-weight models <4%), and ablation studies show that providing human-annotated image descriptions yields large gains (GPT-4o jumps to 44.4% pass@1), indicating vision is a bottleneck, while open-weight LMMs also exhibit coding performance degradation compared to their LLM decoders.

## Strengths

- **Direct validation that visual context is essential.** The paper confirms that "GPT-4o cannot solve any of the coding tasks without access to the images" (Section 3.3, line 94), which is a concrete sanity check distinguishing this benchmark from prior work where text alone suffices.

- **Ablation study quantifying the vision bottleneck.** Providing human-annotated textual descriptions boosts GPT-4o's pass@1 from 13.0% to 44.4% (Table 2). This large, replicated gain across models directly supports the conclusion that visual perception is a primary limitation of current LMMs.

- **Rigorous test-case quality assurance.** Each task uses an average of 9.8 test cases with full statement and branch coverage on ground-truth solutions, validated through cross-annotation by three experienced programmers (Section 3.2–3.3, Table 1). This ensures evaluations of functional correctness are reliable.

- **Novel finding about coding ability degradation in open-weight LMMs.** Table 3 shows that open-weight LMMs consistently underperform their corresponding LLM decoders on HumanEval+ and MBPP+ (e.g., InternVL-2 40.1B drops 28.1 points). This is a non-trivial empirical finding about multimodal training strategies.

- **Evidence the benchmark captures distinct challenges missed by existing benchmarks.** The correlation analysis (Figure 2) shows many open-weight models with competitive MMMU/MathVista/MMVet scores score near zero on HumanEval-V, confirming the benchmark exposes previously undetected limitations.

- **Lightweight design facilitating adoption.** With 108 tasks, simple assertion-based test cases, and restriction to common Python libraries (Section 3.4), the benchmark mirrors HumanEval/MBPP's simplicity, making it practical for broad community use.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The Q1 (vision limitation) analysis does not fully control for modality confound.** The experiment replaces images with human-written textual descriptions and observes large gains (Table 2). However, the descriptions may be more informative than the images (e.g., providing explicit coordinates vs. requiring the model to read tick marks), and the gain could partly reflect the model's inherent preference for textual over visual input. Without a control that equates information content across modalities (e.g., degraded images vs. machine-generated captions), the conclusion that "visual perception abilities remain inadequate" is reasonable but not definitively isolated to perception failure. The paper's language is measured ("indicating"), but this limitation should be acknowledged more explicitly.

- **No uncertainty quantification for pass@k estimates.** With 108 binary-outcome tasks, pass@1 differences of a few percentage points (e.g., InternVL-2 76.3B at 3.7% vs. Qwen2-VL 73.4B at 3.7%) correspond to only a few task-level differences. The paper's main comparative claims (proprietary vs. open-weight, uniformly low scores) are robust, but finer-grained comparisons between open-weight models would benefit from bootstrapped confidence intervals. This is also a community-standard opportunity rather than a unique flaw.

- **The mutation vs. original-adaptation split is not reported.** The paper states 40 initial tasks are expanded to 108 via mutations (Section 3.2), but does not report how many of the 108 are mutations versus direct adaptations. This is a minor transparency gap that would help assess task diversity.

### Trivial
- **Q2 "degradation" framing.** The comparison of LMMs vs. their LLM decoders on HumanEval+/MBPP+ is informative and uses matched architectures. The critic notes that models differ in training data/objectives (not just the vision encoder), so the drop is correlational. The paper already discusses results in terms of "performance comparison" (Table 3 caption), but adding this caveat would strengthen precision.

## Nice-to-Haves
- **Break down performance by visual element type** (trees, graphs, matrices, maps, etc.). This would increase the diagnostic value of the benchmark by revealing which visual reasoning types are hardest for LMMs.
- **Systematic error categorization** beyond the overfitting/hallucination examples. A taxonomy of common failure modes (misreading axis labels, ignoring grid coordinates, etc.) would strengthen the diagnostic narrative.
- **Provide the human-annotated image descriptions as part of the released dataset** to support reproducibility of the Q1 experiment.

## Removed Points

These are flagged to be removed from consideration; treat them with caution.

1. **Criticism that data-leakage evidence undermines the visual-essentiality claim.** The critic argues that models "tend to generate solutions based on the context of the original problems" (Section 5.1, line 212) is *prima facie* evidence that adaptation failed. **Verification:** The paper explicitly frames this observation as *supporting* the adaptation pipeline — models *fail* (they generate *incorrect* solutions) when they rely on old patterns, showing the adaptation created genuinely new tasks where memorized patterns do not work. The separate validation (GPT-4o cannot solve any task without images, line 94) confirms visual essentiality independently. The criticism misreads the paper's own evidence and is factually incorrect.

2. **Reproducibility concern about missing appendix content** (human-annotated image descriptions not included). Per the hard rules: missing appendix/examples stripped by the parser should not be flagged. The paper states these will be released.

3. **Potential task-ordering bias in pass@10 estimation.** The critic suggests that generating 20 samples in a single batch could inflate pass@10 estimates due to non-independent outputs. **Verification:** The paper uses the standard unbiased pass@k estimator from Chen et al. (2021), which properly accounts for all n samples. This concern is not valid for the standard estimator.

4. **Criticism that the benchmark is too small for meaningful comparisons.** 108 tasks is comparable to HumanEval (164 tasks), which is widely used. The paper's main findings (proprietary vs. open-weight, uniformly low performance) are robust to this size.

5. **Formatting/presentation nitpicks** (wrapfigures, minipages). These are parser artifacts, not paper problems.

## Novel Insights

The most interesting observation that emerges from combining the reviews is that the adaptation pipeline creates a stress test with two complementary failure modes: models fail both when they *ignore* visual information (applying memorized algorithmic patterns from the original problems) and when they *try to use* it (struggling to extract accurate information from images). The first failure mode confirms the adaptation was effective at creating non-memorizable tasks, while the second reveals that even when models engage visually, the information extraction is unreliable. The large gap between image-only and description-augmented performance (Table 2) suggests that the bottleneck is not just in "seeing" but in converting visual percepts into precise symbolic representations suitable for algorithmic reasoning — a challenge distinct from the multiple-choice or VQA formats of existing benchmarks.

## Suggestions

1. **Add bootstrapped confidence intervals** for pass@k scores. This is straightforward to implement and would allow readers to assess the reliability of model rankings, especially for open-weight models near zero.
2. **Explicitly acknowledge the modality confound in the Q1 experiment.** Add a sentence noting that the gain from textual descriptions could partly reflect modality preference, and describe this as an upper-bound estimate of visual limitations rather than a precise diagnostic.
3. **Report the number/percentage of mutation-derived vs. directly adapted tasks** in the dataset statistics.
4. **Add a per-category breakdown** of performance by visual element type (trees, graphs, matrices, etc.) to increase diagnostic value.
