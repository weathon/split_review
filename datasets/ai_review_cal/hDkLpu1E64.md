- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5
Now I have full verification. Let me write the consolidated review.

## Summary

This paper introduces FEABench, a benchmark for evaluating LLMs and LLM agents on solving physics/engineering problems by operating COMSOL Multiphysics (an FEA software) through its Java API. The benchmark has two components: FEABench Gold (15 human-verified problems with ground-truth target values) and FEABench Large (200 algorithmically parsed tutorial problems). The paper proposes a suite of intermediate evaluation metrics (executability, model tree score, physics recall, etc.) beyond simple pass@k, benchmarks several closed-source and open-weight LLMs, and designs a multi-turn agent that uses execution feedback and retrieval-augmented code generation. The key finding is that no model or agent can solve any problem correctly, though the agent achieves 88% executable API calls (up from 62% without interaction), demonstrating the benchmark's difficulty.

## Strengths

- **First benchmark for LLM+FEA interaction**: The paper addresses a genuinely underexplored domain — using LLMs to drive numerical simulation software. As stated in Section 1, "the application of LLMs to numerical analysis tasks like FEA remains largely unexplored." This is a novel and worthwhile testbed.

- **Thoughtful multi-granularity evaluation metrics**: Section 3 introduces metrics at multiple levels — executability, model tree similarity, physics interface/feature/property recall, feature dimension, and target relative error. These provide signal even when the full solution is incorrect, going beyond binary pass@k. This is well-motivated given that most solutions fail before computing a target value.

- **Transparent and honest reporting of failures**: The paper explicitly states (Section 6.1) that "the LLM was only able to compute a Valid Target that was also within 10% of the correct answer for a single problem" — and then notes that this single success returned a COMSOL default temperature, not a genuine solution. This candor is commendable.

- **Error analysis identifies key bottleneck**: Figure 4 and the results in Section 6 break down executability by code block type, isolating the physics block as the hardest component. Interface factuality scores (0.54–0.85) quantify the hallucination problem, providing a clear target for future work.

- **Broad LLM evaluation across 6 models**: The paper tests three closed-source (Claude 3.5-Sonnet, GPT-4o, Gemini-1.5-Pro) and three open-weights models (CodeGemma-7B, Gemma-2-9B, Gemma-2-27B), establishing a set of baselines.

## Weaknesses

### Fatal
None.

### Major
- **FEABench Gold contains only 15 human-verified problems, which is too small for a benchmark claiming to evaluate general capability**. With n=15, per-problem variance dominates such that reported means and comparisons (especially small metric deltas across models) are fragile. The paper acknowledges this ("adding more human verified problems would be valuable" in Section 7), but as presented, the benchmark does not provide a stable measurement platform. The standard errors on the mean are reported but with 15 samples these bounds are wide, and the paper conducts no statistical significance tests, making cross-model comparisons unreliable. This is the most significant limitation of the paper's central contribution.

- **The multi-turn agent's improvement (executability 0.62→0.88) is not cleanly attributed to the correction mechanism vs. simple oversampling**. The paper states (Section 6.1) that the agent generates 40 solutions: "20 from oversampling the initial prompt, and another 20 from correcting the best of the initial 20" and that "this allows us to include gains obtained both from oversampling as well as from correction." No ablation is provided that isolates the correction loop — e.g., comparing 40 independent samples from the base prompt vs. the 20+20 pipeline. For 5 of 15 problems, the best solution came from the initial population (pre-correction), suggesting that for at least some problems correction was unnecessary. Without an ablation, the conclusion that iterative correction (rather than increased sampling budget) drives the improvement is unsubstantiated.

### Minor
- **The VerifierLLM's analytical-numerical consistency feedback is not evaluated for accuracy**. Section 5 describes that the VerifierLLM "sets an analytical guess at the start of the Multi-Turn experiment" and uses this for consistency checking, but the paper does not report how often the VerifierLLM's guesses are correct or whether its feedback misleads the correction process.

- **The Feature Dimension metric (a nested physics metric) can only be computed for a small subset of problems**. As noted in Section 3 and 4, this metric is masked when there is no overlap between GT and LLM code. For open-weight models, the paper reports (Section 6) that "the feature dimension metric can only be evaluated for fewer than 5 problems." With a 15-problem total, this means the metric yields almost no signal for many experiments.

- **The Annotated Library (768 LLM-generated code→NL pairs) is not validated for accuracy**. Section 2 describes generating these annotations via Gemini-1.5-Flash, but no human verification or quality check is reported. Since this library is used by the agent's retriever tool, annotation errors could propagate.

- **No per-problem breakdown or error taxonomy is provided for why solutions fail**. The paper identifies the physics block as the hardest component but does not provide a detailed error analysis (e.g., what specific physics errors persist despite feedback, how often geometry construction vs. solver configuration causes failure). With only 15 problems, a per-problem outcome table would be feasible and informative.

### Trivial
None.

## Nice-to-Haves

- Adding a controlled ablation comparing 40 independent samples vs. the 20+20 correction pipeline would substantially strengthen the agent evaluation.
- Expanding FEABench Gold to at least 50 human-verified problems would make the benchmark a more definitive evaluation tool.
- Reporting bootstrap confidence intervals or significance tests for cross-model comparisons would be helpful given the small sample size.
- A per-problem table showing each Gold problem's outcome across models/agents would improve transparency.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Harsh Critic Point 2: "FEABench Large is not evaluated in a way that supports the paper's central claims. Model Tree Score inherently requires execution."** — The paper explicitly states (line 135) that FEABench Large is evaluated "only against metrics that don't require execution." Whether Model Tree Score requires execution depends on whether it is computed from the code structure statically or from execution output; the paper text does not make this unambiguous and the critic's assertion is not verifiable from the readable portion of the paper (Table 1 is an image). The paper is clear about its evaluation protocol. This criticism is insufficiently grounded.

2. **"No statistical significance tests are applied"** framed as a major weakness (from the critic's Section-by-Section Notes). — This is a valid observation but it's a minor concern, not a major one, since the paper does report standard errors on the mean and explicitly warns about small n. I've moved this concern into the relevant Major weakness about the 15-problem set size rather than treating it as an independent point.

3. **Harsh Critic's "Strengthening the Paper on Its Own Terms" section items** — These are constructive suggestions, not weaknesses. They have been folded into Nice-to-Haves above where appropriate.

4. **Generic criticism about "related works" and reproducibility** — The critic mentions "reproducibility: COMSOL is proprietary." The paper acknowledges this and proposes open-source alternatives as future work. This is a known limitation of the chosen platform, not a weakness.

5. **"Section 2: The paper does not report whether a human verified that the LLM-generated annotations are accurate"** — This is a valid point but belongs in Minor weaknesses, which I've included.

## Novel Insights

The two reviewers do not surface any genuinely novel observation beyond what the paper itself contributes. The most useful framing that emerges from synthesis is that the paper's value lies less in the specific numbers it produces (which are inherently unstable with n=15) and more in establishing a concrete, reproducible task definition and metric suite for a previously unevaluated capability — LLM-driven numerical simulation. The finding that every evaluated model/system achieves 0% correct solutions, coupled with the interface hallucination bottleneck (factuality 0.54–0.85), suggests that the core difficulty is not code syntax but physics knowledge grounding, a hypothesis that future work can directly build on.

## Suggestions

1. **Add an ablation for the agent**: Compare 40 independent samples from the base prompt (without correction) against the 20+20 correction pipeline. This is essential to support the claim that iterative feedback helps beyond increased sampling.
2. **Expand the Gold set**: Even 30–50 human-verified problems would significantly improve the benchmark's reliability and the conclusions that can be drawn from it.
3. **Provide a per-problem outcome table**: For 15 problems, a table showing which models solved which metrics on which problems would be highly informative.
4. **Evaluate VerifierLLM accuracy**: Report how often the analytical-numerical consistency check is correct and whether it improves or degrades agent performance.
