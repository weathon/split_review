Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes Skeleton-of-Thought (SoT), a prompting strategy that reduces LLM generation latency by first extracting a skeleton outline of the answer, then expanding each skeleton point in parallel via batched decoding (for open-source models) or parallel API calls (for API-based models). The method requires no model modifications, system changes, or hardware alterations. Evaluated across 12 LLMs, SoT reports speed-ups of up to 2.39× on several models while maintaining or improving answer quality on certain question categories (generic, knowledge, common-sense, roleplay, counterfactual). The paper also introduces SoTr, a router-based extension that selectively applies SoT only when beneficial.

## Strengths

1. **Novel data-level paradigm for inference efficiency**: Instead of modifying models (quantization, pruning) or systems (batching, scheduling), SoT reduces latency by guiding the LLM to plan and parallelize its output content. The paper explicitly distinguishes this from model- and system-level techniques (Section 5, Section 6) and makes a compelling case for "content co-organization for efficiency" as a new research direction.

2. **Consistent speed-ups across 12 diverse LLMs without architectural changes**: SoT achieves >2× speed-up on 8 out of 12 models spanning 7B–33B open-source models and API-based models (ChatGPT, Claude, GPT-4). The speed-up is achieved purely through prompting—no model retraining, quantization, or system-level optimization is required. This is demonstrated in Figures 1 (right) and the per-model breakdown in Section 3.1.

3. **Answer quality can be maintained or improved on suitable question types**: On generic, knowledge, common-sense, roleplay, and counterfactual categories, SoT yields positive net win rates against baseline sequential decoding (Figure 6). The analysis in Section 3.2.3 attributes improvements to increased diversity and relevance, supported by detailed metrics from LLMZoo. The paper honestly identifies categories where SoT underperforms (math, coding, writing).

4. **Adaptive routing (SoTr) makes the method practical**: The router extension (prompting-based using GPT-4, or a trained 120M RoBERTa) selectively applies SoT only for suitable questions. SoTr preserves speed-ups (>1× for most models, Figure 7) while significantly improving quality on categories where SoT alone hurts (coding, math, writing, fermi; Figure 8). The trained router performs comparably to human annotations on Vicuna-80 and better on WizardLM.

5. **In-depth analysis of when and why SoT works**: The paper identifies key factors affecting SoT's success—model instruction-following ability, point count, length balance between points, and question type. It shows that SoT succeeds when answer points can be expanded independently, but fundamentally struggles on step-by-step reasoning tasks. This provides actionable insights for future work.

## Weaknesses

### Fatal
None.

### Major

1. **Primary efficiency results for open-source models rely on estimated rather than measured latencies.** Section 3.1 (lines 132–136) describes that for open-source models, SoT latency is estimated by looking up entries in a pre-built profiling table. The headline speed-up numbers in Figure 2 and the speed-up axis of Figure 1 (right) are based on this estimation for these models. While the paper mentions that actual latency comparisons exist in the appendix and the estimation methodology is transparent, the central claim of the paper is about efficiency, and the primary evidence for that claim is estimated rather than directly measured for the majority of evaluated models. The paper would be stronger by presenting actual measured latencies as the primary results, or at minimum including a validation of the estimation against real runs in the main text rather than deferring it to the appendix. *(Note: actual latency comparisons do exist in the appendix, which was stripped by the parser—this criticism concerns their absence from the main presentation, not their absence from the paper.)*

### Minor

2. **Answer quality evaluation lacks human validation and is entirely automated with GPT-4 as judge.** The paper acknowledges this limitation (Section 6), noting that human evaluation is avoided because SoT answers have a distinctive pattern that could bias raters. However, prior work has documented systematic preferences in LLM-as-judge evaluations (e.g., favoring longer answers, list-like structures) that align with SoT's artifacts. The discrepancy between FastChat and LLMZoo metrics (45.8% vs. 29.5% win rates in Figure 3) further suggests that evaluation prompt design heavily influences results. A small human evaluation on a focused subset (e.g., 20–30 questions per category) would substantially strengthen the quality claims. Without it, the quality results should be treated as suggestive rather than conclusive. The paper's main contribution is efficiency, which limits the severity of this concern, but the quality claims are part of the paper's narrative.

3. **Router overhead is mentioned but not concretely quantified.** The paper states the router induces "a small latency overhead" (line 322) but does not provide concrete latency or cost numbers for either the prompting-based router (which requires a separate GPT-4 call—more expensive and slower than the models being accelerated) or the trained RoBERTa router. Since the speed-up comparison between SoT and SoTr in Figure 7 is a key result, the lack of explicit overhead quantification makes it difficult for readers to assess the net benefit in practical deployment.

4. **No ablation on the number of skeleton points.** The paper instructs 3–10 skeleton points and reports average point counts per model (Figure statistics) but does not analyze how speed-up or quality varies with the number of points. Since the speed-up is directly tied to B (the number of parallel-decoded points), understanding this relationship would provide practical guidance and deepen the analysis.

### Trivial

5. **The "data-centric" framing is somewhat imprecise.** The paper describes SoT as "data-centric optimization for inference efficiency," but SoT is really a prompting/planning strategy rather than data selection or augmentation. The term does not add much analytical value to the contribution. This is a minor issue of framing rather than substance.

6. **Answers generated by SoT are 1–2× longer than baseline answers** (acknowledged in the paper, line 151). While speed-ups still hold because generation is parallelized, the comparison with baseline sequential generation is not token-matched. A reader may wonder how the baseline would compare if allowed to generate longer answers. The paper acknowledges this but does not discuss its implications for the fairness of quality comparisons.

## Nice-to-Haves

- **Validate latency estimation against actual runs**: Taking a representative subset of model–question pairs (e.g., one model per architecture, 10 questions per category) and comparing estimated speed-up against actual wall-clock latency would turn the efficiency results from plausible into convincing.
- **Small human evaluation of answer quality**: A focused human evaluation on the five categories where SoT claims improvement and the two where it clearly loses would provide a sanity check on the GPT-4 judgments.
- **Comparison with a simple speculative decoding baseline** would help benchmark SoT's practical value, though the two approaches target different mechanisms (parallel token verification vs. parallel content planning).
- **Analysis of how speed-up varies with skeleton point count (B)** would provide practical guidance for users.

## Removed Points

These points were raised by reviewers but do not hold up under verification against the paper:

- **"No comparison with speculative decoding in the main evaluation"**: Speculative decoding requires a draft model and operates at the token level, making it a fundamentally different approach. The paper discusses it in the related work (Section 5). A direct comparison would require a substantial expansion of scope. Not a weakness.

- **"Speed-ups are unverifiable without real runs"**: The paper explicitly provides actual latency comparisons in the appendix (line 135: "we also compare the actual latency... in \cref{sec:app-actual-eff-test}"). The appendix exists in the original submission but was stripped by the parser. The estimation is a methodology for fast analysis, not the only evidence available.

- **"The paper should also cover additional domains/tasks"**: The paper evaluates on two datasets (Vicuna-80, WizardLM) spanning nine categories with 12 models. This is a thorough evaluation within a reasonable scope.

- **"Missing token-level parallel decoding comparisons"**: Addressed above under speculative decoding.

- **Formatting/style nitpicks** and concerns about appendix sections being "missing" (stripped by parser): Removed per hard rules.

## Novel Insights

The reviews surface an important tension not fully explored in the paper: the profiling-based latency estimation for open-source models is a methodological shortcut that, while reasonable for rapid iteration, sits uncomfortably alongside the paper's central efficiency claim. This tension is amplified by the fact that the actual latency comparisons exist only in the appendix. A second insight is that the quality evaluation's reliance on GPT-4 as judge is particularly problematic for this method because SoT produces exactly the kind of structured, list-like outputs that GPT-4 evaluators are known to favor systematically—meaning the evaluation bias may not be evenly distributed but instead tilted in SoT's favor in ways that are hard to disentangle without human judgment.

## Suggestions

1. **Promote actual latency measurements to the main text** for open-source models, at least for a representative subset, and present the estimation as a methodological tool for analysis rather than the primary evidence.
2. **Quantify router overhead explicitly**—report the average latency added by the prompting-based router (GPT-4 call) and the trained RoBERTa router separately.
3. **Add a small human evaluation** of answer quality on a focused subset (e.g., 20 questions × 3 categories) to validate the GPT-4 judgments, or at minimum temper the quality claims further given the known biases.
4. **Include a scatter plot or analysis of speed-up vs. number of skeleton points (B)** to understand how the method's efficiency scales with its main free parameter.
5. **Clarify in the "data-centric" framing** what specifically makes SoT data-level rather than prompt-level, or reduce emphasis on this terminology.

## Score and Decision

The paper presents a clever, intuitive idea with a reasonably broad evaluation across 12 models. The core insight—that LLMs can be prompted to plan and parallelize their output structure—is sound and likely useful. The main weaknesses are (1) the efficiency results for open-source models rely on estimated rather than directly measured latencies in the main text, which undermines the primary claim, and (2) the quality evaluation relies entirely on LLM-as-judge without human validation. Neither weakness invalidates the paper's contribution, but both prevent the empirical claims from being fully established. The contribution is promising and the direction is compelling, but the current presentation of evidence leaves enough uncertainty that the paper would benefit from strengthening before publication.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>