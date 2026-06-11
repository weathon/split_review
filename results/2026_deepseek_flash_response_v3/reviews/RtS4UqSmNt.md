## Summary

This paper introduces a formal model of controlled sequential social learning, where an information-mediating planner (e.g., an LLM) strategically chooses the precision of agents' private signals at a cost while agents also learn from each other's actions. The paper proves convexity of the altruistic planner's value function (Theorem 2) — a non-trivial result because agents' dependence on public belief breaks the linearity that would make convexity automatic — and characterizes optimal policies for both altruistic (three phases) and biased (five phases, including intentional signal obfuscation) planners via Theorems 3–5. LLM-based simulations complement the theory, showing broad structural alignment between LLM planner behavior and the analytically optimal policies, with deviations plausibly linked to measured non-Bayesian biases in LLM agents.

## Strengths

1. **Non-trivial convexity proof (Theorem 2).** The paper proves \(V_A^*(\cdot)\) is convex in public belief, explicitly noting this is "quite involved" because agents' actions depend on the public belief — breaking the standard linearity that would make convexity immediate (line 139). This result is then used to characterize the structure of optimal altruistic policy in Theorem 3, demonstrating it is not a decorative result but a working part of the theory.

2. **Complete policy characterization with a novel obfuscation result (Theorems 4–5).** The five-phase characterization for the biased planner is structurally rich and includes the surprising finding (regime E) that the planner intentionally reduces signal precision below baseline to \(b - \epsilon\) so agents ignore private signals and follow the public belief (line 176, line 200). The paper clearly explains the strategic logic: the risk of a countervailing private signal overturning a favorable public belief outweighs the cost of reducing precision. This is a genuinely non-obvious insight.

3. **Clean differentiation from prior work.** The paper carefully distinguishes its model from Wei & Anastasopoulos (2022) — which requires two-way communication — and Smith et al. (2021) — which directly alters agents' choice rules — noting that neither applies to typical black-box algorithmic mediators (lines 45–46). It also distinguishes from Arieli et al. (2022) and Wu et al. (2025), which fix information structure at onset, whereas this paper allows dynamic per-agent precision choice (line 49). These distinctions are precise and accurate.

4. **Quantified welfare impact under transparency constraints.** The paper reports that biased planners decrease social welfare by 40–50% when misaligned (Figure 2c), even under the harsh transparency constraints of Remark 2 (information parity, no lying/cherry-picking, full observability). This provides concrete quantitative evidence for the potential societal risk of LLM-based information mediators.

5. **Measured non-Bayesian biases in LLM agents (NB1–NB3).** The paper identifies three specific deviations from Bayesian updating (underreaction to aligning signals, overreaction to counter-signals, higher cascade thresholds; lines 232–234) and links them to documented human cognitive biases. These measurements are then used to explain structural differences between LLM and optimal policies, creating internal coherence between the empirical observations.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Interpretive overclaiming on the "adaptation to non-Bayesian agents" claim.** The paper observes structural differences between LLM and optimal policies and interprets these as "the planner's strategic adaptations to the specific non-Bayesian behaviors identified" (line 244). Specifically, it attributes continued investment at low beliefs to the planner "understanding that its agents might overreact (NB2)" and gradual tapering to "a direct response to the agents' resistance to cascades (NB3)." However, the paper runs no control experiment that would distinguish this interpretation from simpler alternatives — e.g., testing whether the LLM planner's policy reverts toward the analytical optimum when paired with Bayesian-simulated agents. The paper's own note that one deviation (avoiding extreme precisions) is "consistent with a known central tendency bias" in the LLM planner itself (line 244, point 1) shows that at least one observed deviation likely comes from the planner's own biases rather than strategic adaptation. Without the control experiment, the "strategic adaptation" interpretation is a plausible but untested post-hoc explanation, yet it features prominently in the paper's strongest claims (abstract line 9: "exhibits emergent strategic behavior"; contributions line 33: "LLMs exhibit sophisticated strategic reasoning").

2. **"Percentage policy deviation" metric undefined.** The paper presents a histogram of "Percentage Policy Deviation" (Figure 2b) and states that "the deviation is less than 10% for the majority of belief states" (line 242), but never defines how this metric is computed (e.g., percentage of what — integrated absolute difference over belief space, average absolute difference at sampled points, normalized by the range of precision?). Without this definition, the quantitative claim is difficult to interpret precisely.

3. **Cost function parameter values not specified in main text.** The paper states it varies \(k\), baseline precision \(p\), and discount factor \(\delta\) with \(C=1\) fixed (line 212), but does not report the specific values or ranges in the main text. The welfare impact numbers (40-50% decrease) and the policy plots depend on these parameters, so the reader cannot assess sensitivity.

### Trivial

None.

## Nice-to-Haves

- **Control experiment for the adaptation claim:** Running the LLM planner with Bayesian-simulated agents (rather than LLM agents) and comparing whether the policy shifts toward the analytical optimum would directly test whether the observed deviations are truly "adaptations" to non-Bayesian agents or artifacts of the LLM planner's own biases or imprecision.
- **Brief discussion of the deterministic policy restriction:** The paper restricts to deterministic Markov policies (line 115) and handles the biased planner's non-existence regions via \(\epsilon\)-optimality (lines 166, 176). A brief note on whether stochastic policies could resolve these discontinuity issues would strengthen the theoretical framing.

## Removed Points

The following points from the Harsh Critic were removed per the filtering rules. These should be treated with caution as they may reflect the reviewer's knowledge gaps or the parser stripping the appendix.

1. "No LLM model is named" — Experimental details including the specific LLM are in Appendix E (stripped by the parser). Per hard rules: remove criticisms about missing appendix content.
2. "No number of trials, seeds, or statistical measures" — Same reasoning; experimental methodology details are in the appendix sections stripped by the parser.
3. "Oracle validation not shown" — The paper states "In Appendix E.3, we validate both the beliefs and the performance of the oracle" (line 213). This is appendix content.
4. "Figure descriptions duplicated" — These are parser-induced formatting artifacts (lines 190–198), not author errors.
5. "Connection between model abstraction and LLM behavior underspecified" regarding how the LLM generates signals of exact precision — The oracle mechanism is described at line 212 and validated in the (stripped) appendix.
6. "Markov policy restriction" as a serious weakness — The paper already handles non-existence via \(\epsilon\)-optimality; this is a standard assumption in MDP theory.
7. "First formal model" overstated — The paper's claim (line 31) is specifically "the first formal model that integrates a dynamic control problem for a centralized information planner with the mechanism of sequential social learning," and the related work section (lines 45–49) provides concrete distinctions from the closest works. This is a reasonable, carefully qualified claim, not an overstatement.

## Novel Insights

The Harsh Critic's concern about the experiments needing more rigor is valid but focuses on details that likely reside in the stripped appendix. The more interesting observation — and one that survives filtering — is that the paper's strongest advertised claim ("emergent strategic behavior" / "sophisticated strategic reasoning") rests on a post-hoc interpretation of policy deviations that could alternatively be explained by the LLM planner's own imprecision or central tendency bias. The paper itself provides one such alternative explanation (point 1 at line 244) for one of the three deviations, but does not address whether the other two could also be artifacts. This tension between the strength of the claim and the conclusiveness of the evidence is the paper's most substantive unresolved issue.

## Suggestions

1. Add a definition of the "Percentage Policy Deviation" metric (Figure 2b) directly in the main text.
2. Report the specific parameter ranges (values of \(k\), \(p\), \(\delta\)) used in the experiments in the main text, not only in the appendix.
3. Consider adding a control condition (LLM planner with Bayesian agents) to strengthen or qualify the "strategic adaptation to non-Bayesian agents" claim, or alternatively temper the interpretive language (e.g., replace "the planner learns that" with "the policy is consistent with").
4. Tone down the most assertive claims about "sophisticated strategic reasoning" in the abstract and contribution list to better match what the experimental design can distinguish from alternative explanations.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing (all queries on "social learning model information design control"):**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| "Emergence of Grounded Spatial Language" | 2.33 | R1 (<2.5) | Much weaker — vague modeling with minimal theory vs. this paper's clean MDP formulation and proofs |
| "Steer a Crowd: Learning to Persuade" | 4.00 | R1 (2.5-4.5) | Weaker — incremental algorithmic results; this paper has richer theoretical characterization |
| "Social Learning: Collaborative Learning with LLMs" | 4.00 | R1 (2.5-4.5) | Weaker — applied LLM knowledge transfer, no theory comparable to this paper's convexity and policy characterization |
| "Convex is back: Solving Belief MDPs via Convexity-Informed DRL" | 5.50 | R1 (4.5-6.1) | Somewhat weaker — exploits known convexity; this paper proves convexity in a new, non-trivial setting |
| "Near-Optimal Policy Identification in RCMDP" | 5.80 | R1 (4.5-6.1) | Comparable — both have solid theory with empirical validation; this paper's theoretical characterization is more complete |
| "Learning to Steer Markovian Agents" | 6.33 | R1 (6.0-7.5) | Comparable but stronger experiments; this paper has cleaner theoretical results |
| "Generalized Principal-Agent Problem" | 7.25 | R1 (6.0-7.5) | Stronger — cleaner, more general theoretical results with broader implications |
| "Hidden Cost of Waiting for Accurate Predictions" | 8.00 | R1 (>7.5) | Stronger — elegant model with complete analysis and clear practical implications |

**Round 2 — Narrowing (queries on "social learning theory MDP optimal policy convexity characterization"):**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| "Convex is back: Solving Belief MDPs via Convexity-Informed DRL" | 5.50 | R2 (4.5-6.0) | Weaker — exploits known convexity property; this paper proves convexity in a novel setting with a genuinely involved proof |
| "Near-Optimal Policy Identification in RCMDP" | 5.80 | R2 (4.5-6.0) | Comparable — both accepted-quality work with solid theory; this paper's policy characterization is richer |
| "Global Convergence of Policy Gradient in Average Reward MDPs" | 6.50 | R2 (6.0-7.0) | Stronger — tight convergence analysis for fundamental problem; this paper is a modeling contribution rather than an algorithmic one |
| "Learning Decentralized Partially Observable MFC" | 6.33 | R2 (6.0-7.0) | Comparable — both have theory + experiments; different domains |
| "Optimal Sample Complexity for Average Reward MDPs" | 6.50 | R2 (6.0-7.0) | Stronger — resolves an open question with tight bounds |

**Round 1 bracket:** I initially bracketed the paper between approximately 4.5 and 7.0 based on the topical similarity searches.

**Narrowing in Round 2:** Within the (4.5, 6.0) band, the paper compares favorably to "Convex is back" (5.50, Reject) — the convexity result here is novel rather than exploiting known properties — and is comparable to "Near-Optimal Policy Identification in RCMDP" (5.80, Accept). In the (6.0, 7.0) band, the paper is somewhat weaker than the strong theoretical papers (policy gradient convergence, sample complexity) because those solve fundamental open problems, whereas this paper provides a modeling framework and characterization rather than a tight bound or algorithmic breakthrough. However, the paper's theoretical contribution is genuine and non-trivial.

The paper is clearly stronger than the 4.00-level papers (Steer a Crowd, Social Learning with LLMs) due to its cleaner theoretical results. It is not as strong as the 7.25+ papers that solve fundamental open problems or provide elegant, general frameworks. The paper sits between the upper end of the 4.5–6.0 band and the lower end of the 6.0–7.0 band — a solid contribution with genuine theoretical novelty but weaker empirical support for its strongest claims.

**Final score:** 6.0

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>