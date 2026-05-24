Now I have everything I need to write the final review. Let me compile my analysis.

## Summary

This paper introduces *Ambig-SWE*, a benchmark of 500 underspecified variants of SWE-Bench Verified GitHub issues, along with an interactive evaluation framework where agents can query a simulated user holding the full specification. The authors evaluate six models across three decomposed capacities — detecting underspecificity, asking targeted questions, and leveraging interaction to improve task resolution — and find that interaction recovers significant performance (up to 74% over non-interactive baselines), but most models default to non-interactive behavior and struggle to distinguish well-specified from underspecified inputs.

## Strengths

- **Systematic construction of paired underspecified issues enabling controlled evaluation.** Section 2.1 describes generating underspecified variants via GPT-4o while preserving the fully-specified ground truth from SWE-Bench Verified. This paired design allows causal measurement of whether interaction resolves genuine underspecification — a capability that prior work using only naturally occurring missing-detail cases lacked. The distributional difference analysis (comparing synthetic against natural underspecified issues) provides transparency about the dataset's characteristics and limitations.

- **Three-capacity decomposition of underspecification resolution with dedicated experiments.** The paper breaks resolution into detection (RQ2, §4), question quality (RQ3, §5), and interactive problem solving (RQ1, §3), each with its own metrics and analysis. This enables targeted diagnosis (e.g., Table 2 reveals Qwen 3 Coder's 100% FNR in detection; Figure 5 shows Llama 3.1's low information gain) that is more granular than prior work evaluating only overall task completion under ambiguity.

- **Fine-grained analysis of navigational vs. informational interaction impact.** Table 1 separates resolve rates for issues where the agent obtained file-location details versus not, yielding counterintuitive findings such as Qwen 3 Coder's performance *worsening* after receiving navigational information (55.43% → 52.38%), revealing rigid protocol-following behavior. This level of behavioral decomposition is not present in prior underspecification studies.

## Weaknesses

### Major

- **Unequal interaction turns confound cross-model comparisons in RQ1.** Claude Sonnet 4 and Qwen 3 Coder are allocated up to 100 turns, while all other models receive only 30. The paper justifies this by appealing to "greater reasoning and planning capacity" (line 110), but this introduces a systematic confound: the higher resolve rates of these models in the Interaction setting could partly reflect longer trajectories (more chances to discover information, iterate on code exploration) rather than superior interactive ability. The finding that Claude Sonnet 4 recovers 89% of full performance, for instance, cannot be cleanly attributed to interaction ability alone. The paper acknowledges this limitation but does not provide a control experiment (e.g., running Sonnet 3.5 or Haiku with 100 turns, or constraining the 100-turn models to 30). Within-model comparisons (Hidden vs. Interaction) remain valid, but cross-model comparisons of interactive gains are weakened.

### Minor

- **Detection evaluation (RQ2) measures interaction behavior as a proxy for detection ability, not detection directly.** The experiment tracks whether models choose to ask questions under different prompts, then computes accuracy, FPR, and FNR based on whether interaction was "appropriate" given the input type. However, the decision to interact is a function of both detection ability and instruction-following/compliance tendencies. A model could detect missing information but still not ask questions because the prompt does not sufficiently encourage it, or could ask questions for reasons other than detection (e.g., prompted to be thorough). The three-prompt design partially addresses this, but the paper would be strengthened by a cleaner direct test (e.g., asking models explicitly "Is this instruction complete?") to validate the behavioral proxy. The paper's core claim that models "struggle to distinguish" is directionally supported (the behavioral data clearly show poor separation), but the precision of the conclusion is reduced.

- **Circularity in using GPT-4o as both user proxy and LLM-as-judge (RQ3).** GPT-4o serves as the simulated user providing ground-truth responses and also as the LLM-as-judge scoring question quality on a 1-5 scale (Section 5.1). This risks overestimating the informativeness of questions, as the evaluator may share preferences with the simulated user. The paper also uses GPT-4o to generate the underspecified variants. While the cosine distance metric provides a complementary signal, the reliance on a single model for multiple evaluation roles could introduce systematic bias.

- **Dataset lacks human validation.** The underspecified variants are generated entirely by GPT-4o, and the validation consists of automated distributional analysis and LLM annotations. Human verification that the underspecified versions (a) genuinely remove information necessary for resolution, (b) are plausibly similar to real user queries, and (c) do not introduce artifacts, would substantially strengthen confidence in the benchmark. This is especially important since the benchmark is positioned as a resource for the community.

- **Cosine distance metric for information gain (RQ3) is unvalidated.** The paper measures information gain as cosine distance between embeddings of task representations before and after interaction (Section 5.1). Changes in embeddings could reflect the model's own reasoning processes or summarization of interaction rather than task-relevant information extracted from the user. The paper acknowledges this in its limitations but does not provide validation (e.g., correlation with human judgment of information gain on a subset).

### Trivial

- The paper reports point estimates without confidence intervals or error bars for resolve rates and detection metrics. Given 500 instances, bootstrap confidence intervals would help assess reliability.
- The classification of whether a model "asked for navigational information" is not clearly operationalized — the paper does not specify how interaction content was categorized (Section 3.3).

## Nice-to-Haves

- A direct detection experiment where the model is explicitly asked "Is this instruction complete?" would cleanly separate detection ability from behavioral compliance.
- A cost/efficiency analysis (API tokens per resolved issue in Interaction vs. Hidden settings) would help practitioners evaluate the practical trade-offs.
- A baseline of asking generic questions (e.g., "What file? What error?") would calibrate the value of targeted questioning strategies.
- Corroborating the simulated user proxy with a simpler rule-based user would test robustness of the information extraction findings.

## Removed Points

These points were flagged for filtering but may contain useful context:

- **Criticism that RQ2 detection metric uses accuracy which "conflates two different decisions"**: The paper actually reports FPR and FNR separately alongside accuracy, which addresses this concern. Accuracy is provided as a summary metric with full transparency.
- **Criticism about missing related work citations**: Cannot be verified without external sources; the paper's related work section (§6) provides reasonable coverage of ambiguity, underspecificity, interactive ML systems, and code generation benchmarks.
- **Concerns about unspecified interaction protocol details**: The paper describes the OpenHands framework, turn limits, and the user proxy design. While additional detail would help, the description is sufficient for understanding the experimental design.
- **Claims that "strengthening the paper on its own terms" suggestions constitute weaknesses**: These are forward-looking recommendations for improvement, not deficiencies in the submitted work.

## Novel Insights

The reviews surface a tension that the paper itself does not fully resolve: the RQ2 detection experiment is well-motivated and the behavioral findings (models rarely interact unprompted; prompt engineering yields inconsistent results) are practically useful, but the experimental design conflates detection ability with the propensity to follow interaction prompts. This matters because the paper's headline claim — that models "struggle to distinguish" — rests on this experiment, yet the same data could be reinterpreted as showing that models are sensitive to prompt framing rather than fundamentally unable to detect underspecificity. The Qwen 3 Coder result (100% FNR across all prompts) is genuinely informative regardless of this confound, as it reveals a hard refusal to interact that no prompt variation overcomes. The navigational vs. informational analysis in Section 3.3 is the most methodologically clean result in the paper and yields the most surprising findings (Qwen's performance degrading with more information; Claude Sonnet 3.5 succeeding without file locations). The paper's decomposition framework is a genuine contribution, even if individual experiments vary in how cleanly they isolate each capacity.

## Suggestions

1. **Control for turn limits in RQ1.** Either cap all models at 30 turns, or run a subset of the 100-turn models on a 30-turn budget and report whether the comparative interaction gains hold. This is the single highest-leverage improvement for supporting cross-model claims.
2. **Add a direct detection experiment.** Ask models explicitly whether a task description is complete enough to solve, and compare this to the interaction-based proxy. This would cleanly separate detection from the decision to interact.
3. **Validate the dataset with human annotators.** Have at least 2 annotators evaluate whether underspecified variants hide necessary information and whether the full specification contains it.
4. **Break the circularity.** Use a different model (e.g., Claude) as the LLM-as-judge in RQ3 to avoid potential bias from using GPT-4o for both user simulation and evaluation.

## Score and Decision

**Initial bracket (Round 1):** 5.0 – 6.5

**Anchor comparison:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| RefactorBench (NiNIthntx7) | 6.50 | R1 | Stronger on evaluation breadth and benchmark size, comparable on contribution significance; this paper has more methodological confounds |
| Commit0 (MMwaQEVsAg) | 6.67 | R1 | Weaker — this paper has a larger dataset (500 vs. small set) and more models evaluated, but Commit0 has a novel task formulation |
| ScienceAgentBench (6z4YKr0GK6) | 6.00 | R1 | Comparable — both are benchmark papers with some methodological concerns; ScienceAgentBench has human validation this paper lacks |
| AgentBench (zAdUB0aCTQ) | 6.20 | R2 | Slightly stronger on model coverage (27 vs. 6) but this paper has a more specific analytical framework |
| ML-Bench (sf1u3vTRjm) | 5.75 | R2 | Slightly weaker — this paper has more coherent evaluation design and clearer contribution |

**Narrowing:** The paper sits between ScienceAgentBench (6.0) and RefactorBench (6.5). It has a larger, more systematically constructed dataset and more analytical depth than ScienceAgentBench, but lacks its human validation. It has stronger model coverage than RefactorBench but has methodological confounds (turn limits) that RefactorBench does not. The core decomposition framework and empirical findings are genuine contributions that outweigh the fixable weaknesses.

**Final score: 6.0** — The paper makes a worthwhile contribution with a novel benchmark, a well-structured analytical framework, and actionable empirical findings. The turn-limit confound and detection-proxy concerns reduce the precision of some conclusions but do not invalidate the core results. These issues are addressable in revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>