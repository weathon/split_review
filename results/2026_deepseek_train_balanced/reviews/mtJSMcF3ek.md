## Summary

This paper studies LLM self-improvement through a modular framework that decomposes the process into generation, verification, and update components. It introduces the Generation-Verification Gap (GV-Gap) as a metric that isolates the verification signal before the model-update step, and conducts controlled experiments across six model families, multiple verification methods, and several tasks (GSM8K, Natural Questions, Sudoku). The paper claims to "discover a scaling phenomenon" where the relative GV-Gap grows monotonically with pre-training FLOPs, and also presents findings on cross-verification, task-dependent self-improvement success, iterative saturation, diversity degradation, and verification ensemble benefits.

## Strengths

1. **Clean mathematical decomposition of self-improvement into three factors (generation, verification, update).** The framework in Section 2 formalizes the process, defines the GV-Gap (Definition 2.1) as a quantity that isolates verification quality from post-update confounders, and illustrates with concrete examples (KL-regularized RL, rejection sampling). This is a genuine conceptual advance over prior work that reported end-to-end improvement without disentangling verification from format-alignment artifacts — the paper demonstrates this concretely in Section 5 (lines 194-197), showing that post-finetuning accuracy gains on GSM8K can exceed the GV-Gap because of answer-format convergence.

2. **Cross-characterization of verification (Section 4.2, Figure 2) is well-executed.** The cross-verification study — systematically varying generator and verifier capacities across the Llama-2 and Qwen-2 families — cleanly demonstrates that GV-Gap increases with verifier capability and decreases with generator capability. This is one of the paper's strongest empirical contributions and provides practical guidance for teacher-student configuration.

3. **Useful negative results bounding the scope of self-improvement.** Sections 4.3–4.4 show that on factual recall (Natural Questions) the gap is near zero across all models, and on Sudoku only the largest models (72B+) achieve non-trivial gaps. These results serve as important boundary conditions on when "verification is easier than generation" actually holds, and are presented carefully with post-hoc reasoning.

4. **Ensemble verification benefits (Section 6.3, Table 3).** The finding that combining MC and CoT-Score with an AND operation consistently improves GV-Gap across model sizes is practically useful and well-supported by the data.

5. **Diversity degradation observation (Section 5, Figure 3 right).** The finding that pass@k for large k decreases during iterative self-improvement (while small-k improves) is a finer-grained diagnosis than the generic observation that iterative improvement saturates.

## Weaknesses

### Major

1. **The headline scaling claim is substantially overclaimed relative to the evidence.** The abstract states "we discover a scaling phenomenon" where the relative GV-Gap "scales monotonically with the model pre-training flops," and the introduction presents this as a central contribution. However:
   - **Single-task evidence.** The scaling analysis (Section 4.1, Figure 1) is conducted exclusively on GSM8K. The other tasks (Natural Questions, Sudoku) serve different purposes and do not provide scaling data across model families. One math benchmark is insufficient evidence for a claimed scaling phenomenon, especially given the paper's own acknowledgment that slopes differ across model families.
   - **No statistical quantification.** The paper reports no confidence intervals, goodness-of-fit measures, or error bars on any gap measurement for the scaling trend. Figure 1 is presented as a scatter plot of point estimates without any indication of variance, despite the fact that gap estimates are derived from 128 samples per prompt across 1320 questions and thus have sampling variance.
   - **Opaque FLOP estimates.** The paper never specifies how pre-training FLOPs are computed for each model. For a claim framed in the scaling-laws tradition (citing Kaplan et al. 2020, Hernandez et al. 2021), the x-axis of Figure 1 is a black-box quantity whose derivation is not reproducible from the paper as written.
   
   The body hedges somewhat — "we hypothesize that…" (line 152), "our scaling analysis is primarily observational" (line 266) — but the abstract and introduction frame this as a "discovery" without these caveats. This mismatch between framing and evidence is a significant issue. The scaling observation is worth reporting as a suggestive finding warranting further study; presenting it as a discovered phenomenon overstates the evidence.

2. **Mechanical confound in the relative gap is not discussed in interpreting the scaling trend.** Definition 2.2 normalizes by the deficiency (U_max − expected utility). For binary accuracy (U_max=1), the relative gap for a prompt is (filtered_accuracy − base_accuracy) / (1 − base_accuracy). When a larger model has higher base accuracy, the denominator shrinks, mechanically inflating the relative gap even if the absolute verification improvement is identical. For example, a model with 90% accuracy and a 2-point absolute gap yields a 20% relative gap, while a model with 50% accuracy and the same 2-point absolute gap yields a 4% relative gap. Since larger models have higher accuracy on GSM8K, the scaling trend in Figure 1 could partially or fully reflect this mechanical relationship rather than improved verification capability per se. The paper motivates the relative gap on reasonable grounds (lines 96-97) but never discusses this confound in interpreting the scaling result. Figure 15 shows that the absolute gap does **not** exhibit the same trend, which partially mitigates the concern, but the paper does not make this argument or provide any controlled analysis to disentangle the effects.

### Minor

2. **No variance estimates on gap measurements throughout the paper.** Beyond the scaling claim, the paper reports gap means without any indication of variability (standard deviations, confidence intervals, or even min/max ranges) for most experiments. Figure 6 reports σ for two specific gap distributions, but this is not the norm. For an empirical study making quantitative comparative claims, readers cannot assess whether observed differences between models or verification methods are meaningful relative to sampling noise.

3. **FLOP estimation methodology unspecified.** Related to Weakness 1, but worth calling out separately: even if the scaling claim were better supported, the paper does not document how each model's pre-training FLOPs were computed. This is a reproducibility gap for the paper's quantitative scaling analysis.

4. **Diversity degradation analysis limited to one model.** The pass@k analysis (Section 5, Figure 3 right) is shown only for Qwen-1.5 7B. Given that this finding is highlighted in the conclusion as a "significant obstacle" and "exciting future direction," demonstrating it across at least one more model size or family would substantially strengthen the claim.

5. **"Scaling" terminology oversells the evidence.** The paper invokes the scaling laws literature (Kaplan et al., Hernandez et al.) but provides ~3–4 data points per model family on a single task, with no fitted functions, no goodness-of-fit measures, and acknowledged slope differences across families. A monotonic trend in a handful of points is an observation, not a scaling law on the standard of the cited literature. The paper's own hedging ("observational," "conjecture," "hypothesize") conflicts with the stronger language in the abstract and introduction.

### Trivial

None.

## Nice-to-Haves

- The deliberate choice to use only base models (line 132) is methodologically sound but limits the applicability of the main claims, since virtually all practical self-improvement deployments use instruction-tuned models. Stating this scope limitation more prominently early in the paper (rather than in the experimental setup) would better calibrate reader expectations.
- Adding one additional math benchmark (e.g., MATH) to the scaling analysis would substantially increase confidence that the trend is not GSM8K-specific.
- An ablation on the number of samples (128) used for GV-Gap estimation would ground the methodology.

## Removed Points

- **"No discussion of limitations"** (from Harsh Critic): The paper does not have a dedicated limitations section, but the conclusion acknowledges key caveats (line 266: "While our scaling analysis is primarily observational"). The absence of a formal limitations section is a minor presentation choice, not a substantive weakness. Removed as overly strict.

- **"Base models limit applicability more than acknowledged"** (from Harsh Critic): The paper states this choice explicitly (line 132) and the scope is defensible. The applicability concern is real but is a scope constraint, not a flaw in the experiments. Moved to Nice-to-Haves.

- **"Sudoku only shows Qwen-2 models"** (from Harsh Critic): The text references broader families (Qwen-1.5/2 72B, Llama 3.1 70B at line 182) even if Table 2 shows only Qwen-2. The broader families are mentioned. Removed as partially addressed.

- **Strength about cross-family scaling being a core strength** (from Strength Finder): Tempered because the scaling finding itself is under-supported. The cross-family breadth is retained as part of the strength description but the finding is qualified by the weaknesses above.

## Novel Insights

The most interesting tension that emerges from synthesizing the reviewers' assessments is this: the paper's core methodological contribution — the modular framework and GV-Gap metric — is actually *more* valuable than the paper itself seems to realize, because it provides a clean way to detect and control for the very confounders (format-artifact improvements, accuracy-driven denominator effects) that the current scaling analysis fails to address. The paper would be substantially stronger if it leveraged its own framework to rigorously test whether the scaling trend holds after controlling for the mechanical accuracy-relative-gap relationship, rather than presenting the trend as a standalone discovery. Conversely, the detailed verification analysis (Sections 6.1–6.3) is the paper's strongest empirical contribution but appears later in the paper and receives less emphasis than the weaker scaling claim. The paper's overall impact would increase by demoting the scaling claim and promoting the better-supported modular/verification contributions.

## Suggestions

1. **Reframe the scaling result.** Replace "discovery" and "scaling phenomenon" (abstract, introduction) with measured language like "suggestive monotonic trend" or "positive correlation with model scale." Acknowledge the limitations (single task, no error bars, FLOP opacity) explicitly. This is the single most impactful change the paper can make.

2. **Address the mechanical confound in the relative gap.** Either: (a) show that the scaling trend holds for the absolute gap on a subset where accuracy is not near-ceiling, (b) provide a decomposition separating the accuracy-driven component from the verification-driven component of the relative gap, or (c) explicitly discuss why the confound does not fully explain the observed trend (e.g., using Figure 15's null result for the absolute gap as partial evidence).

3. **Add error bars or variance estimates.** At minimum, provide confidence intervals for the gap measurements in the scaling plot (Figure 1) and document the variability across prompts.

4. **Specify FLOP estimation methodology.** Document the source and assumptions behind each model's pre-training FLOP estimate.

5. **Expand the diversity degradation analysis to at least one additional model size or family** to substantiate the claim that this is a general phenomenon.

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>