Now I have a clear picture. Let me compare:

- **LV-Eval (6.00, Rejected)**: Long-context QA benchmark, straightforward techniques, narrow task coverage. Our paper is broader and more innovative but has different weaknesses.
- **MathCheck (6.25, Accepted)**: Math reasoning checklist, clean methodology, honest framing. Our paper is comparable — broader domains and adds RL training, but with more significant weaknesses (framing mismatch, missing controls).
- **MAmmoTH (7.20, Accepted)**: Clean, strong empirical results, precise methodology-framing match. Our paper is clearly below this.

**Round 1 Bracket: 5.5 – 7.0**
**Round 2 Narrowing: ~6.0** — above LV-Eval (broader contribution) but below MathCheck (messier execution with two Major weaknesses).

Now let me write the final review.

---

## Summary

This paper proposes R-HORIZON, a method for composing single-horizon reasoning problems into multi-horizon sequences by creating arithmetic dependencies between them (one problem's answer determines a key variable in the next). The authors use this method to (1) build a benchmark spanning math, code, and agentic tasks, evaluating 25+ LRMs, and (2) generate training data for RLVR. Key findings: all LRMs suffer severe degradation as the number of composed problems increases (e.g., DeepSeek-R1 drops from 87.3% to 24.6% on AIME25 going from 1 to 5 composed queries), and training on composed data improves both multi-horizon (+17.4 on AIME24 n=2) and single-problem (+7.5 on AIME24) performance. The paper also provides error-type decomposition, reflection analysis, thinking budget allocation, and rollout efficiency characterization.

## Strengths

- **Comprehensive benchmark evaluation across 25+ LRMs**: The evaluation table (lines 146-202) covers models from DeepSeek-R1, o4-mini, Qwen3-235B-Thinking, Gemini-2.5-Pro, Claude-Sonnet-4, and many distilled/smaller variants across MATH500, AIME24, AIME25, AMC23, LiveCodeBench, and WebShaper at multiple composition counts. The consistent degradation pattern provides strong converging evidence for limited long-horizon reasoning capabilities in current LRMs.

- **Fine-grained error decomposition**: Beyond aggregate accuracy, the paper categorizes failures into Problem Reasoning Error, Dependency Reasoning Error, Early Stop, and Output Truncation (Figure 5, lines 253-260). This reveals that Problem Reasoning Errors dominate and grow rapidly with query count, providing mechanistic insight beyond "models get worse."

- **Rollout efficiency analysis with practical implications**: Figure 10 and the accompanying data table (lines 303-334) quantify that training with n=4 composed queries maintains ~85-90% effective sample ratio versus ~65% for n=1. This provides a concrete mechanistic explanation for why composed training helps — more balanced reward signals yield higher-quality policy gradients.

- **Demonstration that composed training improves both multi-horizon and single-problem performance**: Table 1 (lines 231-242) and Figure 4 show that RLVR with composed data (n=2) improves composed-problem AIME24 accuracy by +17.4 while also boosting single-problem AIME24 by +7.5 over naive single-problem training. This transfer effect is non-obvious and well-quantified.

- **Simple, scalable construction pipeline**: Algorithm 1 (lines 74-96) reduces long-horizon data construction to integer extraction, key-variable verification, and linear dependency substitution. The method reuses existing datasets without new human annotation.

- **Cross-domain coverage**: The benchmark spans mathematics (MATH500/AIME/AMC), code (LiveCodeBench), and web agent tasks (WebShaper), showing degradation generalizes across qualitatively different reasoning domains.

- **Controlled ablation of reward schemes**: Table 1 compares last-only reward (R_last) versus all-correct reward (R_all), showing R_all further improves multi-horizon performance (e.g., +4.7 on AIME24 n=2 over R_last), providing actionable guidance for RL training.

- **Reflection and thinking budget analysis**: Figures 7 and 8 (lines 273-289) show that LRM reflections are highly localized and token allocation is biased toward early problems — characterizing specific behavioral deficiencies that explain the performance gap.

## Weaknesses

### Fatal

None.

### Major

- **The dependency construction tests sustained accuracy with error propagation, not semantically interdependent reasoning.** Algorithm 1 creates dependencies via f_i(x) = x + (m_{i+1} - a_i), which resolves to the original key variable when the previous answer is correct. The problems remain logically independent — solving problem 2 does not require reasoning about problem 1's content, only its numeric answer. The paper's framing (e.g., "interdependent problems," "complex multi-horizon reasoning scenarios") overstates what the construction actually produces. The error analysis (Figure 5) confirms this: Dependency Reasoning Errors are a small fraction while Problem Reasoning Errors dominate. The benchmark is best understood as testing *sustained accuracy under error propagation* rather than *inter-problem reasoning*. This narrows the contribution relative to the framing but does not invalidate it — measuring how models degrade across extended problem sequences with cascading errors is a genuinely useful contribution, just not the one the title and framing promise.

- **The RL training comparison lacks controls for data volume and total problem exposure.** Training with n=2 composed data means each training example contains two math problems and generates longer response sequences than an n=1 example. At the same number of training steps (600), the n=2 model sees roughly twice as many individual problems and processes more tokens. The headline +7.5 AIME24 gain could therefore be explained by exposure to more problems or more compute rather than by anything specific to composition. The paper does not report total problem count or token count across conditions, nor does it include a minimal control such as training n=1 for 2x steps, or concatenating two independent problems without dependencies. Without such controls, the claim that *composition specifically* drives the improvement is not adequately supported.

### Minor

- **All RL experiments use a single base model (R1-Qwen-7B).** Given that the evaluation results show substantially different degradation patterns across model scales and architectures, the finding that composed training is beneficial may not generalize. At minimum, the paper should not claim broad applicability without a second model.

- **Anomalous values in the evaluation table suggest data quality issues.** Qwen3-32B scores 127.6 on MATH500 at n=4 (line 157), which cannot be a percentage. R1-Qwen-7B on AIME25 shows an implausible non-monotonic pattern: 0.0 (n=3) → 20.0 (n=4) → 0.0 (n=5) (line 168). The table also contains two entries labeled "Qwen3-32B" (lines 157 and 162) with different results, which is confusing. These may be parser artifacts or data entry errors, but they raise concern about the reliability of the reported numbers.

- **Seed filtering restricts to integer-answer problems without reporting coverage.** The filtering criterion a ∈ Z (Equation 1, line 54) excludes problems with non-integer answers. The paper does not report what fraction of each source dataset (e.g., MATH500) survives this filter, making it impossible for the reader to assess whether the benchmark is representative of the original datasets.

### Trivial

- **"Effective sample" is used without explicit definition.** Figure 10 and the surrounding discussion (lines 303-307) refer to "Effective samples" as a category alongside "Solve None" and "Solve All," but the term is never formally defined. The meaning can be inferred (some but not all sub-problems correct), but this should be stated explicitly.

- **Error position analysis conflates reasoning length limits with problem difficulty.** Figure 6 interprets the position of the first error as evidence of an "effective reasoning length" boundary (e.g., 4-6k tokens for 7B models). However, error position could reflect where harder problems happen to appear rather than a fundamental reasoning ceiling. This interpretation should be qualified.

## Nice-to-Haves

- Add a no-dependency concatenation baseline (two problems concatenated with a delimiter but solved independently) to the RL training to isolate the effect of composition from the effect of seeing more problems per example.
- Control for total problem exposure across training conditions (e.g., n=1 at 2x steps).
- Verify the RL findings on at least one additional base model (e.g., R1-Qwen-32B).
- Add difficulty-controlled analysis to distinguish position effects from problem difficulty in the error position analysis.
- Report what fraction of each source dataset survives integer filtering.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **HC: "The expected accuracy baseline gap is a mechanical consequence of the evaluation design."** REMOVED. The expected accuracy baseline (Equation 4) is intentionally constructed as an independence-based baseline; the gap between actual and expected accuracy is precisely the phenomenon under study. The paper explicitly uses this gap to quantify degradation. The criticism misunderstands the metric's purpose.

- **HC: "The paper defers critical details to the appendix (key-variable verification model, dataset statistics, training hyperparameters)."** REMOVED per hard rules — the appendix was stripped by the parser; these details exist in the original submission. Cannot penalize the paper for what the parser removed.

- **HC: "The introduction cites real-world scenarios requiring thousands or millions of steps, which overstates what the benchmark tests."** REMOVED. This is a standard motivation-vs-method gap found in most papers. The introduction motivates long-horizon reasoning broadly; the method tests a specific instantiation. Not a genuine weakness.

- **HC: "The dependency function is computationally trivial — this is a fatal/structural flaw."** REMOVED. The substance of the concern is preserved in the first Major weakness above, but the "fatal" characterization is removed. The benchmark remains useful for what it measures (sustained accuracy under error propagation), and the evaluation results are independently valuable. The severity is Major (framing), not Fatal (methodology).

- **HC: "The all-or-nothing scoring (Equation 3) is harsh but defensible."** This was flagged as a note, not a weakness. Not included.

- **SF: Generic strengths about "important problem" or "interesting question."** REMOVED. All kept strengths reference specific evidence from the paper.

## Novel Insights

The most distinctive insight from this paper is the finding that training on composed problem sequences improves *single-problem* performance and reasoning efficiency (shorter responses, better budget allocation), not just multi-problem performance. This transfer from harder composed data back to simpler isolated problems is non-obvious and, if replicated with proper controls, suggests that long-horizon training data may be a generally useful curriculum for reasoning models — not merely a specialized training objective. The rollout efficiency analysis (Figure 10) provides a plausible mechanism: composed data produces more balanced reward signals, yielding higher-quality policy gradients.

## Suggestions

- Reframe the contribution around what the benchmark actually measures: sustained reasoning accuracy under sequential problem-solving with error propagation, rather than "interdependent reasoning." This is a valuable contribution that does not require the overclaim.
- Add the no-dependency concatenation baseline and 2x-steps control to the RL experiments. These are the most important additions for the rebuttal.
- Fix the anomalous table values (127.6, non-monotonic 0.0→20.0→0.0) and clarify why there are two Qwen3-32B entries.
- Explicitly define "Effective sample" in the rollout efficiency section.

## Score and Decision

### Calibration Anchors

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Planning in Strawberry Fields (jOuHjFw71C) | 3.00 | R1 | Our paper is substantially stronger — novel method, broader evaluation, RL training |
| LogicBench (71kocBuhNO) | 5.40 | R1 | Comparable; our paper is broader (cross-domain, RL training) but messier (framing, controls) |
| LV-Eval (WQwy1rW60F) | 6.00 | R2 | Our paper is slightly stronger — more innovative method, broader domains, RL findings |
| MathCheck (nDvgHIBRxQ) | 6.25 | R2 | Comparable scale; MathCheck is cleaner methodologically, our paper adds RL training |
| NovelQA (uMEsKEiB7J) | 6.40 | R2 | Our paper is somewhat below — NovelQA is a cleaner, more focused benchmark |
| MAmmoTH (yLClGs770I) | 7.20 | R2 | Our paper is clearly below — MAmmoTH has stronger, better-controlled empirical results |

**Round 1 Bracket:** 5.5 – 7.0
**Round 2 Narrowing:** The paper sits just above LV-Eval (6.00) and slightly below MathCheck (6.25). The two Major weaknesses (framing overclaim, missing RL controls) pull it down from what would otherwise be a ~6.5 contribution. Final assessment: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>