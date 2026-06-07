Here is the final consolidated review.

## Summary

ARPO proposes an RL algorithm for training multi-turn LLM agents that use external tools. The core idea is to monitor token-level entropy after tool-call steps and adaptively branch sampling when entropy rises above a threshold, combined with an advantage attribution mechanism that distinguishes shared and individual token segments. Evaluated across 13 benchmarks and two model families, ARPO consistently outperforms trajectory-level RL methods (GRPO, DAPO, REINFORCE++) while using fewer tool calls during training.

## Strengths

1. **Entropy-based branching is grounded in an empirically measured phenomenon specific to multi-turn tool-use agents.** The pilot experiment (Section 2, Figure 2) directly quantifies token entropy after tool-call steps and establishes that entropy spikes in the first 10–50 tokens after each tool call, that search feedback induces more uncertainty than Python feedback, and that tool-induced entropy exceeds initial-reasoning entropy. This provides a measurement-driven motivation for why trajectory-level methods are insufficient for agentic RL — a claim that prior entropy studies on single-turn reasoning do not address for the multi-turn tool-use setting.

2. **Tool-call efficiency is directly measured during training.** Figure 7a shows ARPO maintaining roughly 250–300 tool calls during training while GRPO hovers around 400–450, yet ARPO achieves higher accuracy. This provides quantitative evidence for the "half the tool-use budget" claim rather than relying on speculative reasoning about efficiency.

3. **Rollout diversity improvement is demonstrated through clustering analysis.** Figure 7b uses PCA dimensionality reduction and DBSCAN clustering on 7.6k trajectories to show that ARPO produces 54 distinct clusters versus GRPO's 48, with greater intra-cluster compactness and inter-cluster separation. This offers a non-trivial quantitative demonstration that the branching mechanism actually changes the distribution of sampled behaviors.

4. **Empirical comparison of hard vs. soft advantage attribution.** Figure 5 directly compares two design choices for advantage estimation under the same ARPO framework, showing that the soft variant yields more stable and higher reward scores throughout training. This ablation goes beyond stating architectural preferences and provides a principled reason for the default design choice.

5. **Consistent results across 13 benchmarks and two model families.** Tables 1 and 2 cover mathematical reasoning, knowledge-intensive QA, and deep search using both Llama-3.1-8B and Qwen2.5-7B / Qwen3 backbones. ARPO achieves the highest average accuracy in both table settings (55.3% on Llama vs GRPO's 51.1%; 58.3% on Qwen vs GRPO's 56.5% for math/knowledge tasks, and substantial gains on deep search benchmarks such as GAIA: 43.7% vs GRPO's 36.9% on Qwen3-14B).

## Weaknesses

### Major

1. **Missing the critical ablation: entropy-guided vs. random branching at the same branching frequency.** The paper's central claim is that *entropy-guided* adaptive branching drives ARPO's improvement. The obvious control experiment is to branch at tool-call steps with equal probability (or randomly) instead of using the entropy threshold, holding everything else (number of branches, overall budget, advantage attribution) constant. Without this ablation, it is impossible to know whether the gains come from (a) the entropy signal, (b) simply doing *any* branching at tool-call steps (which trajectory-level methods do not do), or (c) the overall increase in trajectories sampled per question. The paper references "Appendix A.2" for additional analyses, but the appendix is not available for verification. This is the single most important experiment the paper does not include. **Why it matters**: The paper attributes improvement to a specific mechanism (entropy-guided branching), but the evidence does not isolate that mechanism — the improvement could come from generic branching at tool-call steps.

2. **Rollout budget fairness between ARPO and baselines is not clearly established.** The paper claims "In a fair setting" (Section 5.1) and "Under identical conditions" (Section 5.1) but never specifies what these mean numerically. ARPO uses *M* total trajectory budgets, with *N* for global sampling and *M−N* for branched partial sampling. The critical question is: do the baseline methods (GRPO, DAPO, REINFORCE++) use *M* rollouts per question (matching ARPO's total budget) or *N* (matching only the global sampling component)? If baselines use *N* trajectories while ARPO effectively uses up to *M* trajectory segments, then ARPO's advantage could partly reflect a larger effective sample size rather than the branching mechanism itself. The values of *M* and *N* are never disclosed. **Why it matters**: A confound in the comparison could undermine the conclusion that ARPO is superior to trajectory-level methods — the advantage might simply reflect more sampling.

3. **No statistical significance or variance reporting.** Results are reported as single pass@1 point estimates without standard deviations, confidence intervals, or multiple-run statistics. For a claimed ~4% average gain (Table 1), variance on the order of the claimed improvement would change the interpretation substantially. This makes it impossible to assess the robustness of the reported gains. **Why it matters**: The magnitude of the claimed improvement is modest enough that variance could erase it.

### Minor

1. **The "theoretical foundation" (GPG Theorem) is a notational reparameterization that does not specifically justify ARPO's design.** Section 3.3 introduces the Generalized Policy Gradient Theorem, which states that policy gradients can be computed over macro-actions (grouped token segments) rather than individual tokens. This follows directly from the standard policy gradient theorem by re-indexing grouped tokens as actions — it is not a new theorem. More importantly, the GPG Theorem has no substantive connection to ARPO's entropy-based branching or advantage attribution mechanisms. It simply states that gradient-based optimization works with grouped token segments, which is true of *any* rollout strategy. The paper's claim that ARPO "as an advanced implementation of the GPG Theorem, provides a robust theoretical foundation" (line 170) overstates what the theorem actually contributes.

2. **The entropy observation is qualitative and the "pioneering" claim is overstated.** The entropy calculation follows prior work (Wang et al., 2025b;c; Cheng et al., 2025; Zheng et al., 2025b), and the visualization (Figures 1–2) consists of qualitative line plots without confidence intervals, effect sizes, or comparisons across models. The claim "pioneeringly quantify the token entropy variation" (line 47) overstates the novelty given several cited works already study entropy in LLM reasoning. Furthermore, the paper implicitly assumes that higher entropy after tool calls is *beneficial for exploration* and that branching at these points improves outcomes — but high entropy could equally indicate confusion or insufficient knowledge. The paper provides no analysis of whether branched trajectories at high-entropy points are actually *better* than the original trajectory.

3. **The tool-call efficiency claim ("only half the tool-call budget") is supported by only one comparison.** Figure 7a shows the efficiency analysis for only one model (Qwen2.5-7B) vs. one baseline (GRPO). Extending this analysis to the other model families (Llama3.1-8B, Qwen3-8B/14B) and other baselines (DAPO, REINFORCE++) would substantiate the headline efficiency claim.

4. **Key hyperparameter values (α, β, τ, Z, k) are not specified in the main text.** These parameters control the core adaptive branching mechanism. While they may appear in the appendix, their absence from the main body makes the method under-specified for the reader evaluating the paper's credibility.

5. **The hierarchical reward includes a multi-tool bonus (r_M = 0.1 for using both search and python)** that could incentivize unnecessary multi-tool usage (Equation 5). This runs somewhat counter to the efficiency claim and could introduce reward-hacking behavior. The paper does not discuss this trade-off.

6. **The complexity claim of O(n log n) to O(n²) for rollout is stated without derivation** (line 116) and appears to rely on assumptions about branching reducing effective trajectory length that are not clearly connected to the algorithm's mechanics.

7. **LLM-as-Judge evaluation (Qwen2.5-72B-instruct) could introduce bias** since the judge is from the same model family as some of the trained models (Qwen2.5-7B). A held-out judge or human verification on a subset would increase confidence.

### Trivial

None.

## Nice-to-Haves

- Sensitivity analysis of hyperparameters α, β, τ, Z to assess robustness.
- Analysis of whether branched trajectories at high-entropy points actually discover better solutions compared to the original trajectory.
- Extend the tool-call efficiency analysis to all model×baseline pairs.
- Test whether the improvements persist at larger training scales (e.g., 10k+ RL samples) for deep search tasks.

## Removed Points

The following points from the inputs were removed for the reasons stated:

1. **Harsh Critic: "The comparison may be confounded by unequal rollout budgets"** — *Partly kept as Major Weakness #2 but the speculation about which direction the bias runs is removed. The core concern (values not disclosed) is valid; the assumption about direction is not.*
2. **Harsh Critic: "The 'pioneering' entropy observation is qualitative and unclearly connected to the method's benefit"** — *Kept as Minor Weakness #2 but the "unclearly connected" framing is weakened: the paper's logical connection (high entropy → exploration opportunity) is clear even if unproven.*
3. **Strength Finder: "This paper addressed an important problem" and similar generic framing** — *Removed as generic/superficial. The strengths kept are those with specific, concrete content (measured efficiency, clustering analysis, etc.).*
4. **Harsh Critic: Various "Strengthening the Paper on Its Own Terms" suggestions** — *These are suggestions, not weaknesses of the paper as submitted. Moved to Nice-to-Haves where appropriate.*
5. **Harsh Critic: "The '1k RL samples' regime for deep search is unusually small"** — *This is noted in the paper itself. The paper treats it as a feature (sample efficiency), and it's not a flaw per se — moved to Nice-to-Haves.*

## Novel Insights

None beyond the paper's own contributions. The entropy-guided adaptive branching for agentic RL is the paper's own novel insight. The reviewer comments do not surface additional observations beyond what the paper already articulates.

## Suggestions

1. **Add the random-branching ablation**: Compare entropy-guided branching vs. random branching at the same branching frequency, holding budget and advantage attribution constant. This single experiment would directly validate the paper's core claim.
2. **Disclose rollout budget settings**: Report the values of *M* and *N* used in experiments and clarify whether baselines use *M* or *N* rollouts per question.
3. **Add variance reporting**: Report standard deviations or confidence intervals for all main results, ideally from multiple runs.
4. **Temper the theoretical claims**: Calibrate the framing of the GPG Theorem — it is a straightforward generalization of the standard policy gradient theorem and does not specifically justify ARPO's entropy-based mechanisms.
5. **Specify hyperparameters (α, β, τ, Z, k) in the main text** for all reported experiments.

## Score and Decision

The paper tackles a genuine problem, proposes a novel mechanism with clear intuition, and backs it with the broadest evaluation (13 benchmarks) in this sub-area. These are real strengths that set it apart from related work like StepTool (5.50) and MetaTool (5.00).

However, the paper has two significant evidential gaps that prevent full confidence in its central claim: (1) the missing ablation that would isolate the entropy signal from generic branching, and (2) the unclear rollout budget fairness. The overstated theoretical framing and absent variance reporting are additional concerns.

Relative to the calibration anchors: ARPO is clearly stronger than StepTool (5.50) — more novel mechanism, broader evaluation, efficiency analysis — but slightly weaker than REFUEL (6.50) — less rigorous theory, missing key ablation. It is comparable to Rational Decision-Making Agent (6.25, Reject) in that both have promising mechanisms but miss critical ablations.

**Score: 6.0** — The paper has genuine contributions and thorough evaluation, but the evidential gaps are significant enough that the core claim is not fully supported. The missing random-branching ablation is the single most impactful improvement that could be made.

**Decision: Weak Accept** — The entropy-guided branching idea is novel and practically motivated, and the empirical results are consistently positive. However, the paper would be substantially strengthened by the random-branching ablation and clarified rollout budgets.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>