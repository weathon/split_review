## Summary

This paper formalizes memory types in RL using quantitative definitions: agent context length \(K\) and environment correlation horizon \(\xi = t_r - t_e - \Delta t + 1\). It defines short-term memory (STM) as \(\xi \leq K\) and long-term memory (LTM) as \(\xi > K\), proves the existence of a context memory border \(\overline{K} = \min\Xi - 1\) with three validation intervals, and proposes Algorithm 1 for correctly designing experiments to test each memory type. The paper also introduces a taxonomy distinguishing Memory DM (declarative memory within a single episode) from Meta-RL (procedural memory across episodes). Experiments with DTQN, DQN-GPT-2, and SAC-GPT-2 on Passive T-Maze and MiniGrid-Memory illustrate the consequences of violating the proposed methodology.

## Strengths

1. **Formal quantitative definition of LTM vs. STM grounded in agent context length.** Definition 4 (lines 143–161) introduces the correlation horizon \(\xi = t_r - t_e - \Delta t + 1\) and defines STM as \(\xi \leq K\) and LTM as \(\xi > K\). Prior work relied on qualitative temporal scales (e.g., "a few steps" vs. "hundreds of steps"); this definition makes the boundary measurable, agent-specific, and environment-relative in a principled way.

2. **Context memory border theorem and the three validation intervals.** Theorem 1 (lines 307–314) proves \(\overline{K} = \min\Xi - 1\), and the framework derives three crisp intervals (box, lines 337–348): \(K \in [1, \overline{K}]\) validates only LTM, \(K \in (\overline{K}, \max\Xi)\) is ambiguous (validates both), and \(K \in [\max\Xi, \infty)\) validates only STM. This is a clean, actionable result absent from prior benchmark-focused work.

3. **Empirical demonstration that violating the methodology produces misleading conclusions.** The MiniGrid-Memory experiment (lines 449–453) shows that a naive "variable-mode" setup (\(\xi \in [7, L+1]\)) yields ~1.0 success rate for both LTM and STM configurations, incorrectly suggesting SAC-GPT-2 has LTM. Switching to the fixed-mode configuration prescribed by Algorithm 1 reveals the agent lacks LTM. This directly supports the paper's central claim about experimental misconfiguration causing erroneous judgments.

4. **Taxonomy disambiguating Memory DM from Meta-RL.** Table 1 systematically classifies tasks using \(n_{\text{envs}} \times n_{\text{eps}}\) and inner-loop type (POMDP vs. MDP), including the green/blue decoupling that acknowledges POMDP inner-loop tasks in Meta-RL can be classified as Memory DM. This formalizes a distinction that prior work often conflated.

5. **Passive T-Maze worked example with explicit computation.** Section 5.3 (lines 413–424) walks through Algorithm 1 step-by-step, computing \(\overline{K} = T-1\) and showing how varying \(K\) or \(L\) shifts between LTM and STM validation. This demonstrates the methodology is practically actionable, not just a theoretical formalism.

## Weaknesses

### Fatal

None.

### Major

1. **Thin experimental validation lacking basic rigor.** The experiments (Section 6, lines 427–493) are presented without error bars, confidence intervals, multiple seeds, training hyperparameters, network architecture details, or evaluation protocol descriptions. Only two environments (both simple single-corridor tasks) and three agents are tested. For a paper whose fourth claimed contribution is *empirically demonstrating* that methodology violations cause incorrect judgments, the experimental evidence is not commensurate with the claim's strength. The results may be correct, but the presentation does not meet the standard of rigor that a methodology paper about *correct evaluation* ought to exemplify.

2. **Methodology's dependence on known event-recall pairs is not addressed.** Algorithm 1 (lines 377–407) requires enumerating all event-recall pairs in the environment and computing \(\xi = t_r - t_e - \Delta t + 1\) for each. In the Passive T-Maze and MiniGrid-Memory, this is straightforward (one clue, one junction). However, the paper does not discuss how to estimate the set of correlation horizons \(\Xi\) for realistic POMDPs (robotic navigation, dialogue management, StarCraft micro-management) where the causal structure between past observations and future decisions is complex, unknown, and often stochastic. This is a genuine applicability gap that limits the methodology's practical scope, and the paper neither acknowledges it nor proposes mitigation strategies.

### Minor

1. **Declarative vs. procedural memory definition is a coarse operationalization.** Definition 3 (lines 118–131) equates declarative memory with \(n_{\text{envs}} \times n_{\text{eps}} = 1\) and procedural memory with the product > 1. The paper explicitly states (line 26) that it is "not [trying] to replicate the full spectrum of human memory" and focuses on declarative memory (line 84), so the criticism that this does not perfectly track the neuroscience concepts is mitigated. Nevertheless, the counting-rule framing is so simple that it could mislead readers: standard multi-episode training on a single environment (e.g., DQN on one Atari game for 10K episodes) would technically fall under "procedural memory" by this rule, even though nothing about procedural skill transfer is being tested. Clarifying that this definition is strictly a task-taxonomy tool—not a claim about the agent's cognitive mechanisms—would prevent confusion.

2. **Effective context \(K_{\text{eff}}\) is defined but not operationalized.** Definition 5 (lines 355–361) introduces \(\mu(K) = K_{\text{eff}} \geq K\) as the function characterizing memory mechanisms, and Condition (3) of the algorithm (line 371) requires verifying that \(\xi \leq K_{\text{eff}}\). However, the paper provides no method for empirically measuring \(K_{\text{eff}}\) for a given agent. For an RNN, \(K_{\text{eff}}\) depends on task difficulty, gradient dynamics, and training procedure; treating it as a single known number without offering an estimation protocol weakens the otherwise clear methodology.

3. **Section 6.2 demonstration is largely a tautological verification of the definitions.** The observation that agents achieve return 1.0 when \(K = \xi = 15\) and drop to 0.5 when \(K = 5, \xi = 15\) confirms the expected behavior that reducing context length below the correlation horizon impairs performance. While this serves as a sanity check that the framework's predictions hold, presenting it as an independent empirical "finding" about "the relative nature of an agent's memory" (line 484) overstates its novelty—it follows directly from the definitions already established in Section 5.

### Trivial

None.

## Nice-to-Haves

- Reporting results with multiple random seeds and error bars would significantly strengthen the empirical section.
- Adding a discussion of how practitioners might estimate event-recall pairs in environments without known structure (e.g., using attention maps, probing classifiers, or saliency methods) would broaden the methodology's applicability.
- Dropping or repositioning the declarative vs. procedural definitions as a purely task-taxonomy tool (rather than a cognitive-science claim) would preempt confusion without losing the useful Memory DM / Meta-RL distinction in Table 1.

## Removed Points

These points were flagged by reviewers but removed after verification against the paper:

- **Criticism that the declarative/procedural definition is "not fit for purpose" / "structural" / "fatal":** The paper explicitly states (line 26) its goal is not to replicate human memory, and (line 84) its focus is declarative memory. The definition is a task-taxonomy tool for RL, not a neuroscience claim. Removed as overblown relative to the paper's stated scope.
- **Criticism about lines 20–23 regarding prior definitions:** Subjective opinion about framing, not a verifiable weakness. Removed.
- **Criticism about Section 4.2 "eliding" Meta-RL declarative memory:** The paper addresses this directly with the green/blue decoupling in Table 1 (lines 176–178). Strawman removed.
- **Criticism about missing limitations section:** The paper has no explicit limitations section, but this is a presentation preference, not a technical weakness. The substantive concern about event-recall pairs is retained in Major Weakness 2.
- **Criticism about missing reproducibility details (hyperparameters, architectures):** The harsh critic flagged this; it is subsumed by Major Weakness 1 (experimental rigor) and does not need separate listing.
- **Generic area-of-concern sweeps ("could the metric be measuring a proxy?"):** Not anchored to a specific sentence or problem in the paper. Removed.
- **Strength Finder's generic/superficial strengths removed:** The generic "this paper addresses an important problem" framing dropped as it is not a concrete attribute of the work.

## Novel Insights

The most informative observation that emerges from synthesizing the reviews is the **tension between the paper's methodological ambition and its own experimental execution**. The paper argues that researchers must be precise and rigorous about evaluating memory in RL—yet its own experiments lack basic statistical reporting (error bars, multiple seeds) and test only trivially simple environments where the event-recall structure is known by construction. This tension is not a fatal contradiction (the core conceptual contribution stands independently), but it reveals that the paper is best understood as a **conceptual framework paper** with illustrative demonstrations, rather than an empirical paper that validates the framework's necessity through strong evidence. The community would benefit most from the formal definitions and methodology; the experiments serve mainly as proof-of-concept. The second novel insight is that the methodology's reliance on known \(\Xi\) is not merely a practical limitation—it reflects a deeper epistemic issue: if you already know the event-recall structure, you don't need the methodology to discover it; if you don't, the methodology cannot be applied without additional inference tools. This circularity is worth acknowledging explicitly.

## Suggestions

1. Add error bars and multi-seed reporting to all experiments.
2. Include a discussion of strategies for estimating or bounding \(\Xi\) in environments without known event-recall structure (or clearly characterize the class of environments for which the methodology is directly applicable).
3. Reposition Definition 3 (declarative/procedural) as a task-taxonomy rule and explicitly disclaim any claim about agent-internal cognitive mechanisms.
4. Provide an operational protocol for empirically estimating \(K_{\text{eff}}\) for agents with recurrent or external memory architectures.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>