Now I have thoroughly verified every claim against the paper. Let me produce the consolidated final review.

## Summary

This paper identifies "self-attention leakage" as the root cause of multi-character consistency failures in storyboard generation, and proposes StoryBooth—a training-free method that combines LLM-based spatial planning with (1) bounded cross-frame self-attention to limit inter-character attention leakage, (2) a dropout-based relaxation to preserve image quality, and (3) cross-frame token merging/negative unmerging to align fine-grained features while maintaining pose diversity. The method uses no fine-tuning, achieves inference in ~8.7s, and reports improved character consistency (CC) and text-to-image alignment (VQAScore) over both training-based and training-free baselines on established benchmarks.

## Strengths

- **Diagnoses a meaningful and under-explored problem.** Section 3 and Figure 3 provide a clear empirical analysis showing that cross-frame self-attention (used by StoryDiffusion, ConsiStory) *exacerbates* inter-character leakage when generating multiple subjects. This diagnostic insight goes beyond simply applying existing methods and directly motivates the technical approach.

- **Clean, training-free architectural solution.** The bounded self-attention mechanism (Eqs. 3–6) and the dropout-based relaxation are simple, well-motivated modifications. The cross-frame token merging (Eq. 7) and the early negative unmerging heuristic are novel components that demonstrably improve fine-grain consistency and pose diversity, respectively. The ablation study (Fig. 9) verifies that each component contributes empirically.

- **Competitive results across multiple baselines.** Table 1 reports quantitative improvements (StoryBooth CC 0.914 vs. ConsiStory 0.891; VQAScore 0.891 vs. 0.872) against both training-based methods (Dreambooth-LoRA, IP-Adapter, BLIP-Diffusion) and training-free methods (StoryDiffusion, ConsiStory). The user study (Table 2, detailed in App. C) confirms human preference for StoryBooth on both alignment and consistency, providing complementary validation to the automatic metrics.

- **Practical efficiency.** The 8.7s inference time is competitive with training-free baselines (StoryDiffusion: 6.5s) while offering better multi-character consistency, and the 30× speedup claim against optimization-based methods is factually correct (5–7.5 min vs. seconds).

## Weaknesses

### Fatal
None.

### Major

- **No evaluation of the layout predictor's accuracy or robustness.** The entire bounded self-attention mechanism depends on predicted masks $\{m_i^k\}$ from an LLM-based spatial planning step (Sec. 4.1). The paper provides zero analysis of how often these masks are correct: no precision/recall, no IoU against human annotations, no failure cases, and no ablation where layout predictions are corrupted. If the LLM predicts a wrong bounding box (e.g., places the dog where the cat should be, misses a character, or outputs a degenerate mask), the attention mask $\bar{M}$ in Eq. 6 will be semantically wrong, potentially causing the method to either fail to reduce leakage or block valid attention. Because the layout predictor is the upstream bottleneck for the entire pipeline, the paper's reliability claims are incomplete without characterizing when and how often it works. This is the most significant gap in the submission.

- **No sensitivity analysis for key hyperparameters.** The method relies on several parameters with specific numeric values: the dropout probability $\beta_d$, the positive merging weight $\alpha=0.4$, the negative unmerging weight $\alpha=-0.5$, and the timestep ranges $t\in[1000,950]$ for negative unmerging. None of these are ablated. Without understanding how performance changes when these values are varied, the reported results may reflect fragile tuning rather than a robust method.

### Minor

- **Standard deviations / error bars are absent from Table 1.** The quantitative results are presented without variance over multiple seeds or prompts. While single-run evaluation is common in this sub-field for large diffusion models, the lack of error bars makes it impossible to assess whether the reported improvements are statistically significant.

- **The analysis of attention leakage (Sec. 3) is purely qualitative.** Figure 3 shows one example of leakage. No quantitative measure is provided (e.g., attention entropy, inter-subject attention overlap). A quantitative characterization would strengthen the motivation and provide a baseline for measuring improvement.

- **The paper does not ablate the number of characters.** The core claim concerns multi-character consistency, yet Table 1 aggregates results across single and multi-character settings. Showing how performance degrades with 1, 2, 3+ characters for each method would directly validate the claimed advantage.

### Trivial
None.

## Nice-to-Haves

- **Comparison against layout-guided single-image methods (GLIGEN, InstanceDiffusion).** Since the method uses explicit layout prediction, adapting layout-guided methods to the storyboard setting could help isolate the contribution of the bounded attention mechanism from the layout prediction itself, but this goes beyond the paper's stated scope as a training-free storyboard method and is not required.

- **Attention map visualization for the proposed method.** Figure 3 shows leakage for prior methods; showing the attention maps of the proposed bounded self-attention under identical conditions would provide an intuitive demonstration that leakage is reduced.

## Removed Points
These points are flagged to be removed; treat them with caution:

1. **"30× speedup claim is misleading."** — The paper explicitly states "30× faster than prior training-based methods" (abstract, Sec. 5) and provides the comparison numbers (5 min Dreambooth-LoRA, 7.5 min TI vs. 8.7s). The paper also separately compares against training-free methods (StoryDiffusion at 6.5s, ConsiStory). The claim is factually accurate and properly scoped. Removed as factually wrong criticism.

2. **"Evaluation metrics are non-standard and don't measure what they claim."** — VQAScore and Dreamsim are the same metrics used by the prior work ConsiStory (Tewel et al., 2024), which is the most directly comparable baseline. The paper also includes a human user study (Table 2, App. C) providing direct validation. Removed as factually wrong (metrics follow prior work) and partially addressed (user study included).

3. **"User study lacks preference rates, confidence intervals, number of users."** — The paper states "refer App. C for details." The appendix was stripped by the parser; these details exist in the original submission. Removed per rule about missing appendix content.

4. **"Critical implementation details missing (mask conversion, timestep alignment, LLM exemplar construction)."** — The paper explains mask conversion: "$\bar{\bar{m}}_{l}^{k}\in\mathbb{R}^{N\times1}$ refers to the object level mask $m_{l}^{k}\in\mathbb{R}^{H\times W}$, which is flattened and reshaped to the number of tokens $N$ for the corresponding self-attention layer" (line 102). The timestep ranges for token merging are specified ($t\in[1000,950]$ negative, $t\in[950,600]$ positive, lines 138). Further details are in the supplementary material (which was stripped). Partially removed as addressed in paper / deferred to appendix.

5. **"Table 1 is an image, cannot read numbers."** — This is a parser artifact from PDF extraction. The original PDF renders the table visibly. Table 1 is presented as a table image in the PDF, which is a common formatting choice. Removed as a parser artifact / formatting nitpick.

6. **"Abstract claims 'surpasses prior state-of-the-art' without defining metric or dataset."** — The abstract language is standard for a research paper; the specifics are provided in Section 5 (VQAScore, Dreamsim, ConsiStory dataset). Removed as a style nitpick.

7. **"Negative unmerging timestep range is a heuristic without principled justification."** — Heuristics grounded in the known behavior of diffusion models (early steps determine layout/location, later steps fill in details) are standard in the diffusion literature. The paper provides this rationale. Removed as unreasonable demand for theoretical proof in an empirical systems paper.

## Novel Insights

The most interesting finding that emerges from the reviews—beyond the paper's own contributions—is the tension between the paper's strongest asset and its biggest blind spot: StoryBooth's bounded self-attention mechanism is a genuinely elegant and well-motivated solution to an important problem, but its dependence on an unvalidated upstream component (the LLM layout planner) creates a structural uncertainty. The paper implicitly assumes perfect layout prediction by treating it as a black box (citing Yang et al., 2024a), yet the bounded attention cannot work correctly if the masks are wrong. This is exactly the kind of "last-mile" reliability gap that papers proposing pipeline-based methods routinely need to address but often overlook. The community would benefit from understanding whether layout prediction accuracy is a bottleneck in practice—if the LLM planner is already highly reliable on storyboard-style prompts, then this concern is minor; if it frequently errs, the method's utility is sharply curtailed.

## Suggestions

1. **Evaluate the layout predictor.** Report the accuracy of LLM-predicted bounding boxes against human-annotated layouts for a sample of the benchmark prompts. Show at least 2–3 failure cases of the planner and illustrate how the method degrades (or recovers) when masks are incorrect.

2. **Add standard deviations to Table 1.** Run each method with 3–5 different random seeds and report mean ± std for both VQAScore and Dreamsim. This is essential for the reader to assess whether improvements are reliable.

3. **Ablate the key hyperparameters.** Vary $\beta_d$ (e.g., {0.1, 0.3, 0.5, 0.7}), the positive/negative $\alpha$ values, and the timestep cutoff for negative unmerging, reporting VQAScore/CC for each setting. Show that the chosen values are near-optimal and that performance does not collapse under reasonable variation.

4. **Show performance broken down by number of characters.** Plot character consistency as a function of the number of subjects (1, 2, 3+) to directly validate the paper's central claim about multi-character improvement.

## Score and Decision

**Originality:** 7/10 — The self-attention leakage diagnosis and the bounded attention + token merging solution are novel contributions.

**Importance of research question:** 8/10 — Multi-character consistency is a real and growing bottleneck as storyboard generation gains adoption.

**Claims supported:** 6/10 — The core claims are directionally supported but the unevaluated layout predictor creates a significant gap, and the lack of error bars weakens statistical confidence.

**Soundness of experiments:** 6/10 — Good breadth of baselines and ablation, but missing layout predictor evaluation, sensitivity analysis, and variance reporting.

**Clarity of writing:** 7/10 — The method is clearly described with equations and figures; the analysis and experimental sections are clean.

**Value to community:** 7/10 — The diagnostic insight and training-free approach are useful; the identified weaknesses are addressable.

The paper makes a genuine contribution: it identifies a meaningful problem (self-attention leakage in multi-character generation), proposes a clean training-free solution with ablated components, and demonstrates competitive results. The main weaknesses—unvalidated layout predictor, no hyperparameter sensitivity analysis, lack of error bars—are significant but addressable and do not invalidate the core contribution. The paper should be accepted with a request to address these gaps in the final version or in supplementary materials.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>