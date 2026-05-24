Now I have a thorough understanding of the paper and the calibration landscape. Let me synthesize the final review.

**Initial bracketing (Round 1)**: The weak band anchors (avg 2-3) are clearly rejected papers. This paper is much stronger. The middle band anchors (avg 4.75-6.6) include papers like GSM-Symbolic (6.0, accepted), "Let's Verify Step by Step" (5.5, accepted), and "Can LLMs Solve Long Math Word Problems Better?" (4.75, accepted). The strong band (avg 8+) are outstanding benchmark papers (BigCodeBench, MMQA, etc.) that this paper doesn't match. Initial bracket: 5.0–6.5.

**Round 2 narrowing**: Looked at middle-band papers. GSM-Symbolic (avg 6.0) is the closest comparable — also a benchmark construction + degradation analysis paper covering 25 models. The current paper has broader scope (code, agents), more analysis dimensions (error types, effective reasoning length, budget allocation), and RL training results. However, GSM-Symbolic has cleaner experiments. The current paper's RL confound is a notable weakness relative to GSM-Symbolic's clean design. I'd place it slightly below GSM-Symbolic due to this issue but above simpler benchmarks (avg 4.75-5.5). Final score: 6.0.

---

## Summary

2-3 sentence summary of the paper's contribution.

R-HORIZON introduces a simple method for composing existing single-horizon math/code/agent problems into sequential, interdependent multi-step tasks by linking key variables via arithmetic dependencies. Using this method, the authors construct a benchmark spanning 6 datasets and evaluate 26 LRMs, revealing universal performance degradation as the reasoning horizon increases. Additionally, they show that using R-HORIZON composed data for RLVR training improves both multi-horizon and single-horizon reasoning performance on R1-Qwen-7B.

## Strengths

- **Comprehensive evaluation across 26 models and 6 datasets (math, code, agent) reveals a clear and previously unquantified degradation pattern.** Figure 3 and the full table show that even the strongest models (DeepSeek-R1, Qwen3-235B-Thinking, o4-mini) suffer severe accuracy drops as composed queries increase. This is the most systematic documentation I have seen of this phenomenon and constitutes a genuine empirical contribution.

- **Error-type decomposition (Problem Reasoning Error, Dependency Reasoning Error, Early Stop, Output Truncation) provides actionable diagnostic insight.** Figure 5 shows that Problem Reasoning Error dominates and grows with n, while Dependency Reasoning Error remains low — indicating that the bottleneck is maintaining per-problem reasoning quality across a sequence, not the arithmetic dependency itself. This is a non-obvious finding that meaningfully extends what we know from simpler concatenation studies like NEST.

- **Effective reasoning length analysis (Figure 6) identifies model-specific reasoning boundaries.** The observation that 7B models stabilize error positions at 4–6k tokens while 32B models stabilize at 8–10k tokens is a concrete, size-dependent characterization that could inform architecture-level decisions. The gap between actual and expected accuracy grows with n, providing a quantitative measure of how far each model can "really go."

- **Thinking budget allocation analysis (Figure 8) and reflection analysis (Figure 7) reveal specific behavioral limitations.** LRMs allocate disproportionately more tokens to early problems and show highly localized reflection (>50% of problems lack long-range reflection). These are concrete, measurable weaknesses that suggest specific directions for improvement (e.g., horizon-aware token budgeting).

- **RL training with R-HORIZON composed data shows promising improvements.** Table 1 and Figure 4 demonstrate that training R1-Qwen-7B with n=2 composed data yields +7.5 on AIME24 single-problem accuracy and +17.4 on composed AIME24 compared to single-problem training. This suggests that multi-horizon training data can benefit both standard and composed reasoning.

## Weaknesses

### Fatal

None.

### Major

- **The RL training comparison confounds composition with atomic problem exposure.** When comparing n=1 training (single problems) to n=2 training (composed pairs), if batch size and training steps are held constant, the n=2 condition exposes the model to roughly twice as many distinct atomic problems per update. The paper does not discuss this confounding or attempt to control for it (e.g., by halving the batch size for n=2). Without such control, the claim that "training with R-HORIZON data is a highly efficient training approach" and that the improvement arises specifically from the compositional structure is not convincingly supported. The improvements could partially stem from greater data throughput, not composition. This does not invalidate the benchmark contributions, but it substantially weakens the strongest advertised claim about the training method's efficacy.

- **No statistical rigor in RL experiments.** Table 1 and Figure 4 report single runs without error bars or variance estimates. RL training for LLMs is known to be noisy across seeds. The headline improvement of +7.5 on AIME2024 and the differences between reward schemes ($R_{\text{last}}$ vs. $R_{\text{all}}$) could fall within natural variation. Multiple seeds (at least 3) with standard deviations are needed for the main comparisons to assess reliability.

- **The paper's central claim about "long-horizon reasoning" is partially overstated relative to the actual task design.** The dependency mechanism (Algorithm 1) is an arithmetic shift: $f_i(a_i) = a_i + (m_{i+1} - a_i)$. This reduces the inter-problem dependency to a constant offset computation. The benchmark tests context management and basic arithmetic chaining across a problem sequence, not the kind of planning, state tracking, or temporally extended reasoning that the introduction invokes ("sometimes thousands or even millions" of steps). This does not make the work uninteresting — the degradation results are real and important — but the framing should be calibrated to match the actual task complexity.

### Minor

- **Missing independent-concatenation baseline (NEST comparison).** The paper distinguishes from NEST conceptually but provides no quantitative comparison. A simple concatenation of independent problems (no dependencies) at the same length would isolate whether the degradation is driven by sequence length/context management alone or is exacerbated by the dependency structure. This would also strengthen the RL claims by showing whether the training benefit is specific to dependent compositions.

- **Several implementation details are unspecified.** The identity of model $M$ used for key variable verification (Equation 2) is not disclosed. The filtering statistics (proportion of problems retained after Equations 1–2, characteristics of discarded problems) are not reported. These omissions affect reproducibility and make it harder to assess the benchmark's representativeness.

- **The 127.6% value in Table 1 (Qwen3-32B, MATH500 n=4) is clearly an error.** While this is likely a formatting artifact, such numerical inconsistencies undermine trust in the reported results.

### Trivial

- None beyond the 127.6% table error noted above.

## Nice-to-Haves

- A controlled RL experiment that equalizes atomic problem exposure (e.g., halving batch size for n=2) would solidify the claim that composition, not data quantity, drives the improvement.
- Reporting the frequency of output truncation errors across n and models would help interpret results for longer sequences.
- Applying the training approach to at least one non-math domain (code or agent) would better support the paper's broader framing.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The composition method reduces multi-step challenge to adding a constant" (Harsh Critic Point 1, partially).** The dependency mechanism is indeed a linear shift, but the paper never claims the *dependencies* are complex — it claims the *sequential composition* creates multi-horizon tasks. The difficulty shown in results (Problem Reasoning Error increasing with n) goes beyond simple arithmetic chaining. However, I have retained the essence of this criticism (overstated framing) in the Major section, tempered to reflect what the paper actually shows.

- **"The paper should include RL results for code and agent tasks" (Harsh Critic).** This demands experiments outside the paper's stated scope. The paper explicitly focuses RL experiments on math, and code/agent evaluations are presented as benchmark results. This is a scope-expansion request, not a weakness of the existing work.

- **"Statistical significance and reproducibility" specific demands about releasing prompts.** The paper already provides code on GitHub and the pipeline is described. Demanding exact prompts is overly granular for a conference submission.

- **"Coverage of the original datasets" — demanding exact proportions from filtering.** While useful, this is a minor presentational omission, not a structural weakness. I've demoted it to a minor point.

- **Strength Finder's claim about "Rollout efficiency analysis demonstrates that composed data increases effective training samples by ~20%."** This is supported by Figure 10 but the interpretation is not entirely clean — the "effective" definition needs scrutiny. I have not included this as a separate strength since the RL confound issue complicates any efficiency claim.

## Novel Insights

**The finding that models' effective reasoning length stabilizes at a model-size-dependent plateau (4–6k tokens for 7B, 8–10k for 32B) and that accuracy degrades even while the per-problem expected accuracy remains flat suggests that the bottleneck is not per-problem capability but sequential reasoning management.** This aligns with and extends the "overthinking" literature by showing that models not only over-allocate tokens to early problems (Figure 8) but fail to reflect across problem boundaries (Figure 7). Combined, these paint a picture where LRMs operate with a fixed-duration "attention budget" that they spend mostly on the first problem, then run out of capacity for subsequent ones. The RL results showing that composed training reduces response length while improving accuracy suggest this budget can be reshaped through training. This is the paper's most valuable conceptual contribution.

## Suggestions

- **Disentangle the composition benefit from data quantity.** Run the RL comparison with matched atomic problem exposure (n=1 batch size 512, n=2 batch size 256) and report results with 3+ seeds. If the improvement persists, the composition claim is strongly supported. If it shrinks, the paper should honestly report this.
- **Add an independent-concatenation baseline** (same problems, no dependencies, tested at the same sequence lengths) to both the evaluation and the RL training comparison. This will clarify whether the observed effects are driven by sequence length or dependency structure.
- **Reduce the rhetorical gap between the task design and the framing.** The benchmark tests sequential context management with simple arithmetic dependencies, not open-ended planning. Framing it as evaluating "long-horizon reasoning in breadth and depth" is defensible but should be accompanied by an explicit discussion of what the design does and does not capture.
- **Specify model M** and report filtering retention rates.
- **Correct the 127.6% table entry** and verify all numerical values.

## Score and Decision

**Calibration anchors used (across all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| koza5fePTs (Planning benchmark) | 2.0 | R1 | Much weaker than this paper |
| JQbqaQjV7D (Traffic benchmark) | 3.0 | R1 | Much weaker than this paper |
| pXIbcRPxWR (Supervised CoT) | 2.5 | R1 | Much weaker than this paper |
| Tn5B6Udq3E (Grade-school math reasoning) | 6.0 | R1 | Comparable — similar empirical depth but narrower scope |
| Ze4aPP0tIn (TSMC for math) | 6.6 | R1 | Stronger — cleaner method paper with theoretical grounding |
| GtpubstM1D (Math reasoning training study) | 5.71 | R1 | Comparable — similar mixed review pattern, split opinions |
| C9ju8QQSCv (Long math word problems) | 4.75 | R1 | Weaker — narrower evaluation, less analysis depth |
| AjXkRZIvjB (GSM-Symbolic) | 6.0 | R2 | **Best comparison** — similar benchmark+degradation paper, 25 models. Current paper has broader scope but weaker experimental controls on RL portion |
| WrBqgoseGL (Putnam-AXIOM) | 5.8 | R2 | Comparable — both are math reasoning benchmarks with degradation findings |
| v8L0pN6EOi (Let's Verify Step by Step) | 5.5 | R2 | Comparable — both have strong empirical contributions with some methodological concerns |

**Round 1 bracket:** [5.0, 6.5]
**Round 2 narrowing:** Compared against GSM-Symbolic (6.0) and Putman-AXIOM (5.8). The paper's benchmark and evaluation contributions are on par with these, but the RL confound issue pulls it slightly below GSM-Symbolic's cleaner experimental design. I position it between these anchors — comparable to GSM-Symbolic in value but with a more mixed methodological profile.
**Final score:** 6.0

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>