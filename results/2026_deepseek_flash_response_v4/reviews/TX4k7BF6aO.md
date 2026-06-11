## Summary

ARPO proposes an RL algorithm for training multi-turn LLM agents that use external tools. The method builds on the observation that token entropy spikes after tool-call steps, and uses an entropy-based adaptive rollout mechanism (branching at high-entropy decision points) plus advantage attribution estimation. Evaluated across 13 benchmarks spanning math reasoning, knowledge QA, and deep search tasks against GRPO, DAPO, and REINFORCE++, the paper reports consistent gains and a tool-use efficiency advantage.

## Strengths

- **Empirically-motivated algorithm design**: The paper demonstrates (Section 2, Figure 2) that token entropy spikes sharply in the first 10–50 tokens after each tool call, and designs the branching mechanism around this observed phenomenon. This is more principled than generic exploration heuristics.

- **Consistent gains across diverse benchmarks**: Tables 1 and 2 show ARPO outperforming GRPO, DAPO, and REINFORCE++ on all 10 math/knowledge benchmarks and on deep search benchmarks, with average gains of ~4% over the best trajectory-level baseline. The evaluation covers two backbone families (Qwen and Llama) and multiple task types.

- **Tool-call efficiency**: Figure 7a shows ARPO using ~250–300 tool calls during training versus GRPO's ~400–450 while achieving better accuracy. This is a practically important result since tool-call costs are a primary bottleneck in agentic RL training.

- **Hard vs. soft advantage ablation**: Section 3.2 and Figure 5 systematically compare two design choices for advantage attribution in the branched rollout setting, with empirical support for the soft setting.

## Weaknesses

### Fatal

None.

### Major

1. **Entropy guidance not causally validated.** The paper's core claim is that branching at *high-entropy* decision points is beneficial. However, there is no ablation comparing against branching at random decision points or fixed intervals. The critical control — "entropy-guided branching vs. any branching at tool-use boundaries" — is missing. Without this, the observed gains could come from increased rollout diversity at tool-use boundaries generally, not specifically from the entropy signal. The signature mechanism of the paper is unablated. (Section 3.1, Equation 2; compare against the trajectory-level baselines in Table 1, none of which branch at all.)

2. **No uncertainty quantification.** All results in Tables 1 and 2 are point estimates (Pass@1) without confidence intervals, standard errors, or significance tests. Several gains are small (e.g., Qwen2.5-7B average: ARPO 58.3% vs GRPO 56.5%; individual benchmarks like MATH500: ARPO 78.8% vs DAPO 80.4% — ARPO is actually *lower*). Without error bars, the reader cannot assess whether reported differences reflect signal or noise.

### Minor

3. **GPG theorem provides generic framing, not specific validation.** The Generalized Policy Gradient theorem (Section 3.3, Equation 6) states that policy gradient can be applied over macro actions (token segments) rather than individual tokens. This is a known result from hierarchical RL / options frameworks and is consistent with ARPO, but it does not explain *why* segmentation should occur at high-entropy points or *why* adaptive branching is beneficial. The paper claims this provides a "robust theoretical foundation," but the theorem would apply equally to random or fixed-interval segmentation.

4. **Multi-tool reward bonus (r_M = 0.1) potential confound.** Equation (5) awards a bonus when the model uses both search and Python tools. Since ARPO's branching mechanism inherently produces more diverse tool-use trajectories, it may mechanically receive this bonus more often than baselines, independent of reasoning quality. The paper does not report how often this bonus is awarded across methods or ablate its contribution to the reported gains.

5. **Iso-budget comparison would strengthen efficiency claim.** Figure 7a shows ARPO uses fewer tool calls than GRPO, but the "half the tool-call budget" claim is not supported by a controlled comparison at equal tool-call budgets (e.g., GRPO restricted to ARPO's budget, or ARPO expanded to GRPO's budget). The efficiency claim conflates the method's innate consumption with a controlled efficiency advantage.

6. **Pilot experiment lacks statistical detail.** Section 2 presents the entropy observation qualitatively. The paper does not report how many examples were analyzed, whether the pattern is statistically robust, or how representative the shown examples are.

7. **Entropy computation overhead not quantified.** Footnote 1 acknowledges the overhead of token-level entropy computations but calls it "minor" without measurement.

### Trivial

None.

## Nice-to-Haves

- Add a controlled ablation: entropy-guided branching vs. random/fixed-interval branching (this directly addresses weakness #1)
- Report standard deviations or confidence intervals for all main results, ideally over multiple training seeds
- Ablate the multi-tool bonus r_M to assess its contribution to reported gains
- Provide an iso-budget comparison where GRPO and ARPO use equal tool-call budgets
- Quantify the overhead of entropy computation during rollout
- Report key hyperparameters (α, β, τ from Equation 2) in the main text

## Removed Points

These points were removed from the harsh critic's analysis with brief justification:

1. **"Hyperparameters not reported in main paper"** — Removed per rule: hyperparameters are likely in the appendix (stripped by parser). The critic's call for sensitivity analysis is retained in Nice-to-Haves.
2. **"Missing code link"** — Removed per rule: the link is absent due to parser artifact; "Our codes are released at" exists in the original submission.
3. **"Missing related works / claim overgeneralized"** — Removed per rule: we cannot verify related works from memory, and the paper's Related Work section (Section 6) does cite segment-level RL work.
4. **"Formatting/style nitpicks"** — Removed per hard rules.
5. **"The paper's framing is overgeneralized"** — Removed because the paper's own Related Work section already acknowledges existing step-level/segment-level RL work; the framing difference is a stylistic choice.
6. **Strength Finder's claim that GPG "provides a robust theoretical foundation"** — Partially conflicts with weakness #3; kept in Strengths but the paper's overclaim is reflected in the weakness. The strength (that the theorem provides formal grounding connecting to policy gradient theory) is retained, but the weakness clarifies its limits.

## Novel Insights

None beyond the paper's own contributions. The observation that token entropy spikes after tool calls is genuinely interesting and well-demonstrated. However, the reviewer inputs do not surface any additional novel perspective that the paper itself does not articulate.

## Suggestions

1. **Add the entropy guidance ablation** — compare ARPO against a version that branches at random decision points (or fixed intervals) with the same topology. If entropy-guided branching outperforms random branching, the core claim is supported. This is the single highest-leverage improvement.

2. **Add uncertainty quantification** — report standard deviations over multiple training seeds, or at minimum compute confidence intervals from bootstrap sampling of the evaluation data. This is critical for assessing whether the reported improvements (especially the 1–2 point gains) are meaningful.

3. **Report the multi-tool bonus ablation** — show training curves or final results with and without r_M to disentangle whether the bonus drives the observed improvements.

4. **Provide an iso-budget comparison** — run GRPO with a restricted tool-call budget matching ARPO's consumption, and ARPO with an expanded budget matching GRPO's. This isolates the efficiency claim from the accuracy claim.

5. **Report hyperparameters α, β, τ** — even briefly in the main text or by explicitly citing the appendix equation numbers where they appear, to help readers understand the method's sensitivity.

## Score and Decision

### Calibration Anchors

All anchors retrieved across rounds:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| PNHjoWcQje (StepTool) | 5.50 | R1+R2 | Most directly comparable — step-level RL for tool learning. ARPO has more novel mechanism (entropy-guided rollout vs. standard step-level RL), broader evaluation (13 benchmarks), and efficiency claims. ARPO is stronger. |
| GBIUbwW9D8 (R-MCTS) | 5.75 | R1 | MCTS-based agent with self-learning. Accepted despite concerns. ARPO has broader evaluation and comparably novel algorithm. Roughly equal quality. |
| cVyELMpMRS (REFUEL) | 6.50 | R1+R2 | Multi-turn RLHF with theory. Stronger theoretical grounding but different domain (dialogue, not tool use). ARPO is weaker overall. |
| l1pNNQSzZv (RaDAgent) | 6.25 | R1+R2 | LLM decision-making with Elo scores. Despite high score, rejected. ARPO has more thorough empirical evaluation. |
| Dpqw0namg3 (LAM Sim) | 6.00 | R2 | Framework for online agent exploration. Different approach. Rejected despite 6.00. ARPO is comparably positioned. |
| YCu7H0kFS3 (EAST) | 4.75 | R2 | Entropy-based activation steering. Evaluation limited to simple bandit tasks. ARPO is much stronger. |
| DWLlTNhig1 | 4.75 | R1 | Sparse rewards for dialogue agents. Weaker evaluation. ARPO is stronger. |
| Glcsog6zOe (Tree-Planner) | 5.25 | R2 | Task planning with LLMs. Accepted at lower score. Different domain. |
| 5COCYDObes | 5.00 | R2 | RL for decision-making with LLMs. Weaker than ARPO. |
| 6AUzsrsNUx (MetaTool) | 5.00 | R2 | Tool learning via meta-task augmentation. Different approach. |
| qHpfxfnIq3 (ToolComp) | 5.40 | R2 | Benchmark for multi-tool reasoning. Different contribution type. |
| jpypMKAsO6 | 5.67 | R2 | Grid-based benchmark for MLLMs. Different domain. |
| eI3hEAWe8W | 6.40 | R2 | Multi-turn planner for dialogue. Different domain. |
| owP2mymrTD | 6.50 | R2 | Multi-turn function calling via instruction tuning. Different methodology (not RL). |

**Round 1 bracket**: [4.5, 6.5] — clearly above low-quality papers (EAST at 4.75 on the same entropy theme) and well below top papers (REFUEL at 6.50).

**Round 2 narrowing**: The most directly comparable anchor is StepTool (5.50). ARPO is stronger in novelty (entropy-guided adaptive rollout vs. standard step-level RL with reward shaping) and evaluation breadth (13 benchmarks). ARPO shares similar structural weaknesses: core mechanism not fully validated (entropy ablation missing in ARPO; reward design concerns in StepTool), no uncertainty quantification. ARPO is also comparable to R-MCTS (5.75), which was accepted despite concerns.

**Final score**: 5.75 — above StepTool (5.50), comparable to R-MCTS (5.75). The entropy observation and adaptive rollout are genuinely novel, and the empirical evaluation is broad and shows consistent gains. However, the missing causal validation of the core entropy-guidance mechanism and the lack of uncertainty quantification are significant weaknesses that prevent this from being a clearly strong paper.

**Round-1 bracket explicitly stated**: The narrowest plausible range after reading the paper and harsh critic was [4.5, 6.5]. Round 2 narrowed this to [5.5, 6.0] by comparing against StepTool (5.50, weaker) and LAM Simulator (6.00, comparable quality but rejected). The paper is closest to R-MCTS (5.75, accepted).

MY FINAL SCORE: <score>5.75</score>
MY FINAL DECISION: <decision>Borderline (between Accept and Reject)</decision>