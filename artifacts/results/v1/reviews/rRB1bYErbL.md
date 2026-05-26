Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

The paper proposes R-HORIZON, a method for composing existing single-step reasoning problems into sequential, interdependent multi-step chains. It constructs a benchmark spanning 6 datasets (math, code, agent tasks), evaluates 26 LRMs, and finds severe degradation as reasoning horizon increases. The paper also provides analysis of failure modes (limited effective reasoning length, constrained reflection scope, overthinking) and uses R-HORIZON data for GRPO-based RL training on R1-Qwen-7B, showing improvements on both composed and single-problem tasks.

## Strengths

1. **Comprehensive evaluation across 26 LRMs reveals systematic degradation.** Figure 3 reports accuracy across MATH500, AIME24/25, AMC23, LiveCodeBench, and WebShaper with increasing query counts, showing that even top models like DeepSeek-R1 drop from 87.3% to 24.6% on AIME25 (n=1→n=5). The breadth of models (multiple families, sizes from 1.5B to 235B) makes this one of the most extensive studies of long-horizon LRM behavior.

2. **Identification of limited effective reasoning length with quantitative boundaries.** Figure 6 shows error positions stabilize at 4–6k tokens for R1-Qwen-7B and 8–10k tokens for R1-Qwen-32B on MATH500. The gap between actual and expected accuracy systematically widens with query count, providing direct evidence for a finite reasoning horizon beyond which performance collapses.

3. **Error type decomposition isolates dominant failure modes.** Figure 5 categorizes errors into Problem Reasoning Error, Dependency Reasoning Error, Early Stop, and Output Truncation across query counts, showing that problem reasoning errors dominate and that early stopping grows with horizon. This goes beyond surface-level accuracy reporting to diagnose why models fail.

4. **Reflection and thinking budget analyses provide empirical grounding for known phenomena.** Figure 7 shows long-range reflection rates stay below 50%, empirically confirming that self-correction is highly localized. Figure 8 shows front-loaded token allocation across models, including DeepSeek-R1, which provides concrete evidence for the overthinking claim in multi-horizon settings.

5. **RL training with R-HORIZON composed data improves performance on both multi-step and single-step tasks on R1-Qwen-7B.** Table 1 shows composed training (n=2) raises AIME24 from 57.9 to 65.4 (origin) and from 16.4 to 34.1 (n=2) compared to n=1 training. The rollout efficiency analysis (Figure 10) provides a plausible mechanism: composed data yields more balanced reward signals.

## Weaknesses

### Fatal
None.

### Major

1. **Training experiments are limited to a single small model (R1-Qwen-7B).** The paper claims that "R-HORIZON mitigates the current limitations of long-horizon reasoning in training and evaluation paradigms" and that the approach is a "scalable, controllable, and low-cost path to improve" LRMs — but the RL evidence comes from only one 7B model. No results are shown for larger models (e.g., R1-Qwen-32B), different base architectures, or other model families. The benchmark evaluation (Section 4.2) convincingly shows that scale matters: larger models degrade less. Therefore, whether training with composed data helps at larger scales is an open question. The training claims in the abstract and conclusion are overgeneralized relative to the evidence presented. This does not invalidate the evaluation contribution, but it means the training component is preliminary rather than conclusive.

2. **Potential overlap between training and evaluation data is not addressed.** The training data pool is drawn from "Skywork-OR1-RL training data" (Section 4.3), while evaluation uses standard benchmarks including AIME24/25, MATH500, and AMC23. The paper does not state whether these evaluation sets are disjoint from the training pool. Given that Skywork-OR1 was trained on standard math reasoning data, there is a real risk that AIME/MATH problems (or distributionally similar ones) appear in both the training pool and the evaluation sets, which could inflate the reported improvements. The paper must clarify this. Even if the relative comparison (n=1 vs. n=2 training) is unaffected by contamination, the absolute numbers and the claim of generalization to "standard reasoning tasks" require clean evaluation.

3. **Anomalous WebShaper result for o4-mini is unexplained.** In Figure 3, o4-mini on WebShaper scores 43.7% at n=1 but jumps to 87.6% at n=2 — a massive improvement that contradicts the general degradation trend and is not seen with any other model. This suggests a problem with the composition, evaluation metric, or answer extraction for this specific model-task combination. The paper does not mention or attempt to explain this anomaly. If the WebShaper sub-benchmark is unreliable for certain models, it weakens the claim that R-HORIZON generalizes to agentic tasks. The authors should either correct, explain, or retract this result.

### Minor

4. **The expected accuracy metric conflates composition overhead with chain difficulty.** Equation (4) computes expected accuracy as the product of pass rates on unmodified atomic problems. Since the composed problems have modified statements (dependency text prepended), their difficulty is not identical even when the previous answer is correct. Thus the gap between actual and expected accuracy partly reflects the overhead of processing dependency specifications, not purely the effect of longer reasoning chains. The paper's error-type analysis (Figure 5) partially mitigates this by separately tracking dependency reasoning errors, but the presentation of expected accuracy as a precise baseline (Figure 1) overstates its rigor.

5. **No confidence intervals or multiple seeds for training results.** Table 1 and Figure 4 report single curves with no indication of variance. The improvements of +7.5 on AIME24 (origin) and +17.4 on AIME24 (n=2) are large, but without multiple seeds or error bars, it is impossible to assess whether the differences are statistically significant or how stable the results are across runs.

6. **Composition method for math is limited to integer-answer problems with verifiable key variables.** While the paper acknowledges this (Section 3.1), it means a substantial fraction of problems from the original datasets are discarded during filtering. The generalizability of R-HORIZON to non-integer reasoning tasks (e.g., proof-based math, open-ended generation) is unclear. The appendix covers code and agent tasks, but the construction for those domains is not described in the main paper.

### Trivial
None.

## Nice-to-Haves

- A discussion of the computational cost of the model-based key-variable verification step (Equation 2) would aid reproducibility.
- Reporting training hyperparameters (G, epsilon, beta, learning rate) in the main text rather than deferring to Appendix F would improve self-containedness.

## Removed Points

These points are flagged to be removed per the filtering rules. Treat them with caution.

- **Speculation about prompt standardization across models**: The harsh critic raised "the paper might not standardize prompts across models." This is speculative; the paper uses model-based extraction (Appendix E.2) to handle diverse formats. No concrete evidence of a problem was provided. → **Removed** (speculative, no specific anchor in the paper).
- **Missing appendix content**: Criticisms about details being "only in the appendix" (code/agent composition, training hyperparameters, full cost analysis). The paper clearly references Appendix A, F, H for these details, and the parser strips appendices from all papers. → **Removed** (parser artifact).
- **Computational cost of generating composed problems**: The harsh critic noted the paper does not discuss computational cost. This is a minor omission, not a weakness that undermines any claim. → **Moved to Nice-to-Haves**.
- **"Limited scope reduces applicability" framing**: The harsh critic noted the integer-answer restriction as limiting broad applicability. This is a legitimate limitation but is explicitly acknowledged in the paper's method description. → **Kept as Minor #6** (re-framed from a sweeping concern to a specific known limitation). The original framing was overly broad; the specific limitation is clear from the paper.

## Novel Insights

The reviewers collectively surface one genuinely novel observation beyond the paper's own contributions: the finding that *effective reasoning length* has a sharp token-level boundary that scales with model size (4–6k for 7B vs. 8–10k for 32B) is notable and could serve as a diagnostic for comparing reasoning architectures. The combination of this finding with the error type decomposition provides a concrete failure profile that goes beyond "models get worse on longer tasks." The training result that composed data reduces overthinking while improving accuracy is also an interesting tension that invites further investigation.

## Suggestions

1. **Expand training experiments** to at least one additional model size (e.g., R1-Qwen-32B) or explicitly limit the training-related claims to small models. Without this, the claim that R-HORIZON "mitigates the current limitations of long-horizon reasoning in training" is only supported for 7B-scale models.
2. **Clarify data contamination status** by stating whether the evaluation benchmarks (AIME24/25, MATH500, AMC23) are fully disjoint from the Skywork-OR1 training data pool. If they are not, contamination analysis or mitigations should be reported.
3. **Investigate and explain the WebShaper o4-mini anomaly** (43.7% → 87.6% at n=2). If the result is valid, explain why this specific combination defies the degradation trend. If it is an artifact of answer extraction or composition design, correct it or remove the result.
4. **Add uncertainty quantification** (multiple training seeds, error bars) to the RL results in Table 1 and Figure 4.
5. **Qualify the expected accuracy metric** as an optimistic bound that does not account for dependency overhead, and avoid presenting it as a precise baseline in Figure 1.

## Calibration Anchors

I compared the paper under review against the following anchors from the calibration search:

- **jOuHjFw71C** (avg 3.00, topic-low): "Planning in Strawberry Fields" — evaluated 2 LRMs on planning benchmarks, no new method or dataset. The current paper is much stronger: it introduces a novel method, evaluates 26 models across 6 datasets, provides fine-grained analysis, and shows training improvements.
- **MK6E6IgROl** (avg 3.75, topic-low): "ProcBench" — multi-step instruction-following benchmark with synthetic tasks. The current paper has broader scope, more realistic tasks, and a method contribution beyond benchmarking.
- **71kocBuhNO** (avg 5.40, topic-mid): "LogicBench" — systematic logical reasoning benchmark with evaluation across many LLMs. Comparable in evaluation breadth, but the current paper additionally contributes a method with practical training utility.
- **NUD03NBDOE** (avg 6.75, topic-high): "ActionReasoningBench" — clean benchmark design with clear conceptual contribution (ramification constraints). Stronger on methodological rigor than the current paper, which has unresolved concerns (data contamination, WebShaper anomaly).
- **Nsms7NeU2x** (avg 6.75, weakness-data-contamination): "How much can we Forget about Data Contamination?" — directly addresses data contamination in LLM evaluation. The current paper does not address this concern, which is a gap relative to this standard.
- **1WceuzWff5** (avg 3.50, weakness-training-on-one-model): "Understanding the Transfer of High-Level RL Skills" — similar limitation of single-model experiments, scored low partly for that reason.

The low-band topic anchors (3.00–3.75) failed primarily because they offered limited novelty beyond evaluating existing models on existing benchmarks. The current paper does not share that failure — it has a clear method contribution. However, the weakness-anchored queries show that papers with unresolved data contamination concerns or single-model training evidence tend to score lower (3.50–4.25 range). The current paper partially shares those failure modes (training on one model, contamination not addressed), which prevents it from reaching the 6+ range.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>