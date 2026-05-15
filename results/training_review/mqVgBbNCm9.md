Now I have enough information from the paper to verify each reviewer claim. Let me write the consolidated review.

---

## Summary

This paper introduces Skeleton-of-Thought (SoT), a method that reduces end-to-end LLM generation latency by first prompting the model to output a concise skeleton of the answer, then expanding each skeleton point in parallel (via batched decoding for open-source models or parallel API calls for API-based models). The method is evaluated on 12 LLMs (9 open-source, 3 API-based) on two assistant-style datasets, reporting speed-ups up to 2.39×. The paper further extends SoT with a router module (trained RoBERTa or GPT-4 prompting) that adaptively decides when to apply SoT, mitigating quality degradation on step-by-step reasoning tasks.

---

## Strengths

- **Novel segment-level parallelism via content planning, clearly differentiated from prior work.** Unlike token-level parallel methods (speculative decoding, non-autoregressive generation) that require auxiliary models or architectural changes, SoT exploits off-the-shelf LLMs' instruction-following ability to plan content structure and parallelize at the segment level without modifying the model, system, or hardware. The paper explicitly contrasts this with existing approaches (Section 1).

- **Broad evaluation across 12 diverse LLMs and two datasets.** SoT is tested on models ranging from 7B to 33B (open-source) and three API-based models (ChatGPT, Claude, GPT-4), on the Vicuna (80 questions, 9 categories) and WizardLM (218 questions) datasets. This breadth gives reasonable coverage of the model landscape.

- **Practical router extension that addresses SoT's main limitation.** The paper identifies that SoT is unsuitable for step-by-step reasoning questions (math, coding) and designs a router (trained 120M-parameter RoBERTa or GPT-4 prompting) that adaptively falls back to standard generation. Evaluation shows the router improves quality on previously degraded categories while maintaining gains on suitable ones, making the method more deployable.

- **Detailed diagnostic analysis of when SoT works and why.** The paper breaks down speed-ups and quality per model and per category, analyzes factors such as number of points, point-expanding response length, and adherence to the "short" instruction. It identifies specific failure modes (e.g., stablevicuna13B not following length constraints, leading to poor acceleration). This analysis helps readers understand the boundary conditions of the method.

- **Transparent acknowledgment of limitations.** The paper explicitly discusses limitations: potential bias of GPT-4 judges (line 381), the lack of human evaluation, the estimation-based latency for open-source models in the main text, the overhead of SoT in saturated serving scenarios, and increased token costs for API models.

---

## Weaknesses

### Fatal
None.

### Major

1. **Speed-up claims for open-source models in the main text are based on composited profiling-table estimates, not direct wall-clock measurement.** Section 3.1 describes constructing latency profiling tables for Llama architectures (prefilling and decoding latencies at various batch sizes) and then "quickly estimating" SoT latency by looking up and summing table entries. The main speed-up figures (Figs. 2, 3, right panel of Fig. 1) use this estimation method. While the estimation approach is technically sound—the paper explains that decoding is weight-bound so batching adds little per-token cost—and actual measurements are referenced in the appendix (line 134–136), relying on additive lookup numbers as the primary evidence in the main text leaves uncertainty about synchronization overhead, padding inefficiency, and other real-world factors that a direct latency measurement would capture. The paper's central empirical claim is weaker than if measured end-to-end latencies were presented in the main body.

2. **Answer-quality improvements are plausibly confounded by increased length.** The paper reports (line 151) that SoT answers are "on average, 1∼2× longer than the baseline answer." GPT-4 as a judge is known to favor longer, more verbose outputs. The paper acknowledges judge bias generally (line 381) but does not control for length—e.g., by matching token counts, examining correlation between length and win rate, or showing that quality improvements persist when answers of similar length are compared. The claimed "potential to improve answer quality" (abstract) may therefore partly reflect a length artifact rather than a structural benefit from content planning. The paper hedges with "potential" and "maintains" (vs. "improves"), which is appropriate, but without deconfounding, the quality claims remain uncertain.

### Minor

1. **Small evaluation set (80 questions, Vicuna) with no statistical significance reporting.** The core quality evaluation uses 80 questions; per-category analyses split this into groups of roughly 5–10 questions (e.g., math, coding). No confidence intervals, standard errors, or statistical tests are reported for any win/tie/lose or net win rate. When net win rates are modest (~10–20%), it is unclear whether the difference is meaningful. While the Vicuna 80-question set is a standard evaluation prompt set in the chatbot literature, the lack of any significance analysis weakens the quality conclusions, particularly for per-category breakdowns that motivate the router design (Figure 6).

2. **Router overhead is not quantified in the main text.** The paper notes that "the router induces a small latency overhead" (line 322) but does not report its magnitude (e.g., inference time of the 120M-parameter RoBERTa classifier vs. GPT-4 prompting), nor is it factored into the speed-up numbers shown in Figure 7. For the GPT-4 prompting router, the latency and cost of an additional API call could be non-trivial. Quantification would help readers assess the practical deployment trade-off.

3. **The prompt-based router uses GPT-4, whose cost and latency are not accounted for in comparisons.** The prompting router (Section 4.1) relies on an additional GPT-4 call to decide whether to trigger SoT. Since GPT-4 is the most expensive and slowest API model tested, this adds non-trivial overhead. The paper compares router-triggered speed-ups without clearly separating this cost. While the trained RoBERTa router addresses this for the extension, the GPT-4 prompt router is presented as a baseline option without overhead accounting.

### Trivial

- The paper's use of "net win rate" ((wins − loses) / total) discards ties, which are informative. The paper does report raw win/tie/lose rates in separate figures, so the information is available, but the net rate alone can be misleading when ties are common.
- The illustrative latency examples in the introduction (22s for Claude, 43s for Vicuna-33B) are single-question anecdotes that do not constitute a benchmark, though they serve a legitimate motivational purpose.

---

## Nice-to-Haves

- A direct comparison of estimated vs. measured latency for open-source models to validate the profiling-table methodology, ideally presented in the main text.
- A length-controlled quality analysis (e.g., truncating longer answers to match lengths, or reporting correlation between length delta and win rate) to disentangle length effects from structural quality improvements.
- Reporting confidence intervals or bootstrapped error bars for net win rates, especially for per-category results.
- Concrete side-by-side examples (SoT vs. baseline) for categories where SoT excels (e.g., knowledge) and where it fails (e.g., math), to illustrate the qualitative difference.

---

## Removed Points

- **Criticism about "data-centric" framing being undefined.** The paper clearly defines this: "in contrast to existing model- and system-level efforts for inference efficiency, SoT takes a novel 'data-level' pathway by letting the LLM organize its output content" (lines 61–62). This is well-motivated.
- **Criticism about 22s/43s latency numbers being "anecdotal."** These are illustrative motivating examples in the introduction, not benchmark claims. Every paper uses concrete examples to motivate the problem.
- **Criticism about skeleton prompt length constraints not being followed by some models (stablevicuna13B).** The paper already acknowledges and analyzes this in detail (lines 146–148), noting that it explains the model's poor acceleration.
- **Criticism about net win rate "discarding ties."** The paper reports raw win/tie/lose rates in Figure 4 alongside net win rates, so the information is preserved.
- **Criticism calling the framing "just prompt engineering."** The paper's positioning as "data-centric" is a legitimate research framing that draws a clear distinction from model/system-level techniques, and the paper explicitly discusses this.
- **Criticism about "missing actual latency measurements in the main text" presented as if the paper has no such data.** The paper explicitly references actual latency tests in the appendix (line 134–136). The criticism is retained in weakened form: the issue is that the *main text* relies on estimates, not that measurements are absent.
- **Any formatting/style nitpicks removed per hard rules.**

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Promote actual latency measurements to the main text.** Present a direct comparison between estimated and measured latency for open-source models to validate the profiling-table approach. If the error is small (e.g., <5–10%), this would significantly strengthen confidence in the speed-up claims.
2. **Add a length-controlled quality analysis.** At minimum, report the correlation between answer length difference and win rate. Better yet, show that SoT's quality improvements hold when answers are truncated to similar lengths, or use a statistical model that controls for length as a covariate.
3. **Add confidence intervals or bootstrapped error bars to net win rates**, particularly for per-category breakdowns. This would help readers assess whether observed differences are meaningful given the small sample sizes.
4. **Quantify router overhead explicitly** in the main text—RoBERTa inference time, GPT-4 prompting latency, and how these affect the speed-up numbers in Figure 7.

---

## Score and Decision

This is a solid paper with a clever, well-motivated idea, broad evaluation across many models, a practical router extension that addresses the method's main limitation, and transparent disclosure of limitations. The weaknesses—estimation-based speed-up evidence in the main text, length-confounded quality analysis, and small evaluation set without statistical tests—are real concerns but not fatal: the estimation methodology is sound and well-justified, the paper acknowledges its evaluation limitations, and the core contribution (segment-level parallelism via prompting) is novel and clearly demonstrated. With the presentation improvements suggested above, this work makes a valuable contribution to efficient LLM inference.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>