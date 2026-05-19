- Decision: Reject
- Avg Score: 4.40
- Scores: 8, 3, 3, 5, 3
Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper proposes AVUA (Adaptive Video Understanding Agent), an LLM-based agent for video understanding that combines query-adaptive frame sampling with self-reflective feedback (evaluator + refiner) and long-term memory. The method uses an LLM to dynamically decide which frames to process based on the question and prior observations, rather than pre-sampling frames uniformly. Evaluated on EgoSchema, Ego4D NLQ, MovieChat, and NextQA, the method shows strong accuracy improvements and large reductions in frame access relative to baselines, with ablation experiments confirming each component's contribution.

## Strengths

- **Strong ablation evidence for the proposed components**: The paper systematically ablates the evaluator, refiner, sampler, and memory across multiple datasets (Table 5, "ablation1"). The plain ReAct baseline (same LLM, same tools) achieves 42.02% on EgoSchema, while the full framework reaches 66.98%. Removing any single component causes a substantial drop (e.g., evaluator removal → 50.1%, refiner removal → 53.2%, memory removal → 55.1%). This is the cleanest evidence that the proposed feedback and memory mechanisms are driving the gains, and it properly controls for the underlying LLM.

- **Demonstrated query-adaptive behavior via textual cue analysis**: Section 5.2 and Figure 4 show that on NextQA, questions with temporal cues (e.g., "at the end", "at the beginning") cause the agent to concentrate frame sampling on the corresponding video segment, while questions without cues sample more uniformly. This provides direct behavioral evidence for the paper's central claim of query-adaptive sampling.

- **Generalization across diverse video understanding benchmarks**: The method is evaluated on four benchmarks spanning long-form egocentric video (EgoSchema, Ego4D NLQ, ~3-9 min), movie understanding (MovieChat, ~9.4 min), and short-form temporal/causal reasoning (NextQA, ~44 sec). The method consistently outperforms or matches the best baseline on each while using fewer frames, demonstrating broad applicability.

- **Comprehensive component-level ablation across multiple datasets**: The ablation study (Table 5) isolates each component's contribution, showing that their relative importance varies by task (e.g., evaluator is most critical for EgoSchema, sampler for Ego4D). This provides nuanced empirical support for the framework's modular design.

## Weaknesses

### Fatal
None.

### Major

- **MovieChat evaluation protocol invalidates the reported comparison**: The paper evaluates its method on MovieChat using a custom LLM evaluator (Claude-3.5-Sonnet with a confidence threshold of 80/100, line 156) but compares against baseline numbers (MovieChat 62.3%, VideoChat 57.8%, etc.) that were reported in their original papers using different evaluation protocols (presumably human evaluation, captioning metrics, or GPT-based evaluation with different settings). The resulting 84.8% accuracy and the claimed "22% increase" are uninterpretable because the scoring function differs between the author's method and the baselines. This is a direct comparison of incomparable numbers. The authors must either (a) re-evaluate all baselines under the same protocol, or (b) clearly state that the MovieChat result uses a non-standard evaluation and remove claims of superiority on this benchmark. As presented, this comparison cannot be accepted as evidence.

- **Frame count metric systematically undercounts true processing cost**: The paper reports "frames accessed" as the number of frame indices the agent selects (e.g., 14.27 on EgoSchema). However, the paper states (line 127): "To accommodate the model's requirement for frame sequences, we sample 3 additional frames (for a total of 4) for information extraction" — and this applies to both LaViLa and Video-LlaVa. So each reported "frame access" triggers processing of 4 frames by the vision model. The baselines' frame counts (e.g., 180 for LLoVi) represent frames individually processed by their models. The claim of "93% reduction in frames" (line 205) is inflated because it uses a different counting convention. The authors should report effective frame processing cost (number of frames actually processed by vision models) and clarify the counting methodology. Additionally, the total computational cost should account for LLM API calls (policy generation, each ReAct step, evaluator, refiner, memory retrieval), which are non-trivial.

### Minor

- **LLM/tool confound in cross-paper comparisons**: The method uses Claude-3-Sonnet as its agent LLM, while baselines like VideoAgent and LifelongMemory originally used GPT-4 or other models with different tool sets. This confound makes it impossible to attribute performance differences solely to the proposed method components when comparing against published numbers. The ablation study (Table 5) properly controls for this by comparing ReAct (same LLM, same tools) against the full method, and this is the strongest evidence. However, the headline claims of "state-of-the-art performance" against published baselines would be strengthened by stating which LLM each baseline used and discussing the potential confound.

- **No statistical variance reported**: All results are point estimates without confidence intervals, standard deviations, or significance tests. On NextQA, the overall gain over VideoAgent is only 1.4% (72.7 vs 71.3), which could be within noise for a single run. Reporting variability would substantially strengthen the claims.

- **The ReAct ablation baseline is underspecified**: The ablation (Table 5) lists "ReAct" as a baseline, but the paper does not fully specify what it includes — does it have access to the same tools? The same policy generation step? The same sampler? The same initial system prompt? Clarifying this is important for interpreting the ablation results.

### Trivial
- **Typo**: "Cluade-3.5-sonnet" (line 156) → "Claude-3.5-Sonnet."
- **Typo**: "daynamic" (line 312) → "dynamic."

## Nice-to-Haves
- Providing the prompt templates used for policy generation, evaluator, refiner, and memory retrieval (if they exist in the stripped appendix, this is already addressed).
- Clarifying whether the evaluator/refiner LLM is the same instance as the agent LLM or separate calls.
- Specifying how semantic similarity is computed for long-term memory retrieval (embedding model used).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Refinement is always generated regardless of evaluation result"**: The critic questioned why refinement happens when the answer is judged correct. The paper explicitly addresses this (line 86): refinement is stored in memory to enhance future trials even when the current answer is correct. This is clearly explained — removed.
- **"Characterization of baselines as non-adaptive is inaccurate"**: The critic claimed VideoAgent and LifelongMemory also retrieve based on queries. The paper's Table 1 correctly marks them as not having "query adaptive sampling" (they pre-extract captions at uniform intervals, then retrieve from the pre-extracted set — this is fundamentally different from dynamically deciding which frames to access based on the query). The criticism misreads the distinction — removed.
- **"Missing prompts / memory indexing details hinder reproducibility"**: If the appendix (stripped by the parser) contains these details, the criticism is invalid. Since the parser strips appendices, this is removed per instructions.
- **"Related work characterization could be sharper"**: Vague, non-actionable — removed.
- **"The description is high-level and lacks prompt templates"**: Addressed by the appendix-stripping rule; removed.
- **"Overall assessment: fundamental weaknesses prevent acceptance"**: The critic's summary judgment is not a per-weakness point; the specific weaknesses are retained above individually.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Fix the MovieChat evaluation**: Either re-evaluate all MovieChat baselines under the same LLM-evaluator protocol (ideally with the same confidence threshold and evaluator model) or remove the MovieChat comparison and associated claims. If the evaluation protocol differs fundamentally from the baselines', this benchmark cannot be used for comparison.

2. **Report effective frame processing cost**: Re-compute the number of frames actually consumed by vision models (accounting for the internal 4× sampling in LaViLa and Video-LlaVa). Also report approximate total LLM token consumption so readers can assess the full computational trade-off.

3. **Add confidence intervals or standard deviations**: At minimum, report standard errors for the main results and ablation experiments, especially for the small-margin results on NextQA (+1.4%).

4. **Clarify the ReAct baseline**: State explicitly whether the ReAct ablation uses the same LLM, tools, and system prompt as the full method (minus the evaluator/refiner/memory components).

5. **Discuss the LLM confound**: Acknowledge which LLMs the baselines use and discuss how this might affect the comparison. Even a brief statement would strengthen the evaluation's credibility.
