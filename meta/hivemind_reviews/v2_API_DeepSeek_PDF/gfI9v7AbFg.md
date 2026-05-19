## Summary
# Final Review Report

## Summary

This paper presents STRATEGIST, a bi-level framework that combines LLM-driven high-level strategy search with low-level Monte Carlo Tree Search (MCTS) for decision-making in multi-agent adversarial games. The high-level strategies are represented as interpretable Python-coded value heuristics or chain-of-thought dialogue guides, iteratively refined through population-based self-play without external training data. The framework is evaluated on two games: Game of Pure Strategy (GOPS) and The Resistance: Avalon.

**Strengths:** The bi-level architecture is well-motivated and addresses a genuine limitation of existing LLM agents — their difficulty with complex planning in adversarial multi-agent settings. The idea queue mechanism for modular strategy improvement is a novel design choice that enables incremental refinement and transfer of improvement ideas. The application to social deduction games (Avalon) with both action and dialogue components demonstrates versatility. The strategic randomization analysis in human evaluations is a revealing finding.

**Core Weaknesses:** (1) The comparison against RL methods is conducted in an extremely low-data regime (320 episodes) that heavily disadvantages RL, making "superiority" claims over RL questionable. (2) Human evaluation is underpowered (30 games, 10 participants), and claims of human-competitive performance are not statistically supported. (3) Several key claims about generalizability go beyond the tested settings (only two games). (4) The PUCT/MCTS formulation has technical gaps (singularity in the value interpolation, circular belief estimation). (5) High variance in key experimental results (GOPS standard deviations exceed means) weakens the reliability of reported improvements. (6) Novelty claims cannot be verified without external literature comparison (Retrieval-Disabled Mode).

## Strengths
1. **Well-motivated bi-level architecture.** The paper identifies a genuine limitation of existing LLM agents — their inability to handle complex strategic reasoning in adversarial multi-agent environments — and proposes a principled solution that separates high-level strategy abstraction (LLM-driven) from low-level policy execution (MCTS-driven). This division of labor is conceptually sound and addresses a real gap.

2. **Novel idea queue mechanism.** The modular improvement process using an idea queue with UCB-based selection is a thoughtful design. By separating "idea generation" from "strategy implementation," the framework enables incremental, interpretable improvements and allows successful ideas to transfer across strategies. This is a genuine methodological contribution over simpler line search or BFS approaches.

3. **Versatile across game types.** The framework handles both non-dialogue action domains (GOPS, a card game with numeric bidding) and dialogue-driven social deduction (Avalon, with natural language discussion). This demonstrates meaningful versatility beyond single-domain LLM agent systems.

4. **Interesting empirical finding about strategic randomization.** The action analysis in Figure 3 revealing that STRATEGIST employs more uniform voting patterns than humans (concealing role identity) is a non-trivial and insightful result. This finding is well-supported by the data and represents genuine emergent strategic behavior.

5. **Sample efficiency argument is valid.** While the RL comparison is flawed (see Weaknesses), the observation that STRATEGIST achieves reasonable performance with only 100-300 training transition steps (vs RL's ~3,840-24,000) is noteworthy. The use of an LLM prior to bootstrap strategic knowledge is a legitimate advantage in low-data regimes.

6. **Comprehensive appendix.** The paper provides detailed pseudocode (Algorithm 1), prompt templates (Appendices H, J), and worked examples of strategy improvement. This significantly aids reproducibility despite the complexity of the framework.

## Weaknesses
1. **Unfair RL comparison (P0 - Critical).** The comparison against AlphaGo-style and DeepRole-style RL methods uses only 320 episodes (GOPS) and 160 episodes (Avalon). Standard deep RL for games requires orders of magnitude more data (AlphaGo Zero used ~4.9 million games). At 320 episodes, the neural network has barely seen any transitions. The paper's claim of "superior performance" is misleading because it compares LLM-guided search (which leverages extensive prior knowledge) against RL from random initialization in a regime that systematically handicaps RL. The proper claim should be: "STRATEGIST outperforms RL baselines under extremely limited simulation budgets."

2. **Underpowered human evaluation (P0 - Major).** Only 30 games with 10 participants were collected. Win rates (0.333 vs 0.367) have overlapping standard errors and no statistical significance testing is reported. The survey evaluation uses asymmetric methodology — experimenter-rated human performance vs self/team-rated AI performance. Subjective 1-6 scales without validated anchors have limited reliability. The sample is too small to support the "comparable to human players" claim.

3. **Overclaimed generalizability (P1 - Major).** The abstract and conclusion claim STRATEGIST is a "generalizable framework" and "paves the way for autonomous systems." The paper only tests on two carefully curated games with predefined rules, small state spaces, and clear reward structures. The Limitations section (Appendix C) acknowledges this gap, but this disclaimer does not appear in the abstract or conclusion, creating a disconnect.

4. **High experimental variance (P1 - Major).** Key results show standard deviations that often exceed or rival mean effects. In Table 4 (GOPS), population-based self-play achieves 0.87 ± 1.5 (SD > mean). In Table 2 (GOPS), BFS with thought achieves -0.48 ± 0.375, while STRATEGIST achieves 1.5 ± 0.99. The large error bars suggest the ranking could change substantially with more data.

5. **Technical gaps in MCTS/PUCT formulation (P2 - Major).** The PUCT formula (Eq. 1) has a singularity at N(s,a) = 0 that is not addressed. The belief distribution π_B in Eq. 2 is circularly defined (rollout counts define the belief, but the belief defines the rollout selection). Metropolis-Hastings sampling for hidden states is mentioned without convergence criteria or acceptance rate reporting. These gaps reduce reproducibility.

6. **Reliance on LLM stability (P2 - Minor).** The entire framework depends on the LLM generating valid, high-quality Python code for value heuristics and coherent dialogue guides. Small perturbations in LLM output could lead to broken code or degenerate strategies. While the paper uses GPT-3.5 consistently and seeds strategies, the sensitivity of the approach to LLM version/model/hyperparameters is not analyzed.

7. **Confounded feedback comparison (P2 - Minor).** Table 4 compares feedback methods but confounds the feedback type with the number of opponents (0, 1, or 4). Population-based self-play uses 4 opponents while fixed opponent uses 1. The improvement could come simply from opponent diversity rather than the population mechanism. A control with 4 fixed opponents is missing.

8. **Novelty claims deferred.** Due to Retrieval-Disabled Mode in this review, novelty and literature positioning claims cannot be independently verified. The paper's related work discussion (Section 4) and Table 6 provide a feature comparison matrix but do not include head-to-head empirical comparisons against the cited systems (e.g., Cicero, Agent-Pro, ReCon).

## Key Issues
### Issue 1: RL comparison fairness (Critical)
The most serious concern. The paper frames STRATEGIST as outperforming RL methods (AlphaGo, DeepRole/MuZero-style) but evaluates all methods at an extremely low number of self-play episodes (320 for GOPS, 160 for Avalon). These numbers are 4-5 orders of magnitude less than what typical deep RL methods require (AlphaGo Zero: ~4.9M games, MuZero: ~100K-5M games depending on domain). The comparison is therefore not a test of algorithmic superiority but a test of which method makes better use of a small simulation budget. The paper should:
- Rename the section to "Sample Efficiency Comparison" rather than "LLM-Improvement vs RL"
- Explicitly state the simulation budget limitation in all claims
- Include a scaling curve showing whether STRATEGIST's advantage persists with more episodes (Appendix L partially addresses this but needs more emphasis in the main text)

### Issue 2: Human evaluation validity (Major)
The human evaluation has multiple validity threats:
- N = 30 games, N = 10 participants — insufficient statistical power
- Asymmetric evaluation: experimenter-rated human performance vs player-rated AI
- Subjective 1-6 Likert scales without validated anchors
- Missing random baseline for "correct vote" metric (base rate ~60%)
The paper should commit to a larger-scale human study and pre-register evaluation metrics.

### Issue 3: Overclaiming (Major)
Several claims in abstract/intro/conclusion go beyond evidence:
- "Generalizable framework" — tested on 2 games only
- "Outperforms traditional RL methods" — underpowered comparison
- "Comparable to human players" — statistically equivalent (not the same as comparable) with high variance
- "Paves the way for autonomous systems" — speculative
Needed: bounded claim language throughout, explicit acknowledgment of limitations in the abstract and conclusion.

### Issue 4: Technical reproducibility gaps (Major)
- PUCT formula has undefined behavior at N=0 (singularity)
- π_B belief distribution is circularly defined
- Metropolis-Hastings parameters (proposal, acceptance criteria, burn-in) unspecified
- UCB formula missing factor of 2 and non-stationarity handling
- No seed/randomness management protocol reported

### Issue 5: Statistical reliability (Major)
Multiple results have standard deviations exceeding or rivaling mean effects. The paper does not report:
- Statistical significance tests for any comparison
- Confidence intervals beyond standard error
- Effect sizes
- Multi-seed results for the LLM improvement runs (LLM output is stochastic)

## Actionable Suggestions
### S1. Reframe the RL comparison (Must, P0)
Current claim: "STRATEGIST consistently outperforms both AlphaGo and DeepRole."
Recommended revision: "Under limited simulation budgets (320 episodes for GOPS, 160 for Avalon), strategies discovered by STRATEGIST achieve higher win rates than value networks trained from scratch with the same episode budget. This suggests LLM-guided strategy search offers sample efficiency advantages in low-data regimes, though the gap may narrow given sufficient training data (see Appendix L)."

### S2. Expand the human evaluation (Must, P0)
- Collect at least 150+ games with 30+ participants
- Use symmetric evaluation: have both humans and AI rated by the same method
- Pre-register the evaluation protocol (metrics, sample size, stopping rule)
- Report statistical tests (e.g., bootstrap confidence intervals for win rate differences)
- Add a random-voting baseline for the "correct vote" metric

### S3. Add scaling experiments for RL (Nice-to-have, P1)
Run the RL baselines at multiple episode budgets (320, 1K, 5K, 20K, 100K) to show where STRATEGIST's sample efficiency advantage diminishes and whether the LLM-guided approach remains competitive with more data. This would strengthen the paper by providing a more complete picture.

### S4. Fix the PUCT formula (Must, P2)
- Add explicit handling for N(s,a) = 0 in Eq. 1: Q(s,a) = Q̂(s,a) when N(s,a) = 0
- Discuss the circularity in the belief estimation π_B(s|I) and propose a fix (e.g., use a uniform prior over information states for the first K rollouts)
- Report Metropolis-Hastings parameters: proposal distribution, acceptance rate, burn-in length, number of chains
- Add the missing factor of 2 to the UCB formula, or explain why it is omitted

### S5. Add variance reduction techniques (Nice-to-have, P1)
Given high variance across results: increase the number of Monte Carlo rollouts per strategy evaluation, use common random numbers for pairwise comparisons, and report 95% confidence intervals with bootstrap or t-test for all main comparisons.

### S6. Rephrase the conclusion (Must, P1)
Replace the speculative "paves the way for autonomous systems" paragraph with a concise summary of 3-4 validated findings, 2-3 specific limitations, and 2-3 concrete future research directions that follow directly from the paper's results.

### S7. Add ablation: effect of LLM model (Nice-to-have, P2)
Run the full STRATEGIST pipeline with at least one additional LLM (e.g., GPT-4, Llama-3) to test whether the framework's effectiveness depends on the specific LLM used. The paper currently uses only GPT-3.5.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows a reasonable structure but has several weaknesses:
- Paragraph 1 is too generic, lacking a concrete, falsifiable gap statement
- The two "critical questions" are too broad to drive a clear narrative
- Paragraph 2 introduces the method before establishing what specifically is missing in prior work
- Paragraph 3 makes overclaims (RL superiority, human-competitive) before presenting evidence
- The contribution list is functional (mechanism, method, demonstration) but does not foreground the research insight

### Recommended Storyline: "Bi-Level Abstraction for LLM Strategy Learning"

The core insight should be: *LLMs can generate and iteratively improve strategy abstractions that make multi-agent planning tractable, and these abstractions can be refined into policies by low-level search.*

**Abstract Outline (5 sentences):**
- S1 (Problem): "LLMs exhibit strong generalization but struggle with detailed planning in multi-agent games where policy spaces are combinatorial and opponents actively adapt."
- S2 (Prior gap): "Existing LLM agents rely on direct action prediction or self-reflection, which are inefficient in adversarial settings with large state/action spaces."
- S3 (Proposal): "We introduce STRATEGIST, a bi-level framework where an LLM generates and iteratively improves high-level strategy abstractions (as value heuristics or dialogue guides), which are then refined into action policies by low-level Monte Carlo Tree Search."
- S4 (Key mechanism): "Strategies are evaluated through population-based self-play; a priority queue with bandit sampling selects promising improvement ideas; MCTS provides fine-grained value estimates."
- S5 (Results): "On GOPS and Avalon, STRATEGIST achieves higher win rates than selected LLM self-improvement methods and RL baselines under limited simulation budgets, and demonstrates human-competitive strategic concealment behaviors in human-AI experiments."

**Introduction Outline (4 paragraphs):**
- P1 (Big Picture + Gap): State that LLMs show promise for decision-making but fail in adversarial multi-agent settings. Specifically diagnose three failure modes: combinatorial policy spaces, active opponent adaptation, and lack of theory-of-mind reasoning. End with: "This raises two questions: (1) can LLMs learn high-level strategic abstractions that simplify multi-agent policy search, and (2) can these abstractions be improved through self-play?"
- P2 (Solution intuition): Introduce STRATEGIST conceptually. The key idea: separate "what to do" (strategy, represented as text/code) from "how to execute it" (policy, via MCTS). This division allows the LLM to focus on high-level reasoning while MCTS handles tactical precision. Mention the idea queue for modular improvement.
- P3 (Evidence preview): Briefly state that STRATEGIST outperforms LLM improvement baselines and RL methods under limited budgets, demonstrates strategic randomization against humans, and scales well with MCTS budget. Keep wording bounded and specific.
- P4 (Contributions): List 3 contributions, each with a clear scope qualifier.

**Three Alignment Checks:**
- Problem alignment ✓: Adversarial multi-agent planning -> bi-level abstraction is a natural fit
- Variable alignment ✓: High-level strategy (σ), idea queue (Q), MCTS budget all appear in method section
- Contribution-evidence alignment: Partially ✓ (RL comparison needs reframing; human eval needs stronger evidence)

## Priority Revision Plan
### P0 (Critical — must fix before resubmission)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P0.1 | Unfair RL comparison | Reframe claims: "outperforms under limited budgets" not "outperforms RL" | Prevents validity rejection | 1 day (wording) |
| P0.2 | Underpowered human eval | Expand to 150+ games, symmetric evaluation, statistical tests | Prevents accept/reject uncertainty | 2-4 weeks |
| P0.3 | Overclaiming in abstract/conclusion | Rephrase bounded statements; add limitations upfront | Prevents reviewer backlash | 2-3 days |

### P1 (Major — strongly recommended)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P1.1 | Generalizability overclaimed | Add explicit scope: "on two adversarial games"; test one more domain | Strengthens positioning | 2-4 weeks |
| P1.2 | High experimental variance | Increase rollouts, report CIs, add significance tests | Strengthens credibility | 1-2 weeks |
| P1.3 | Confounded feedback comparison | Add 4-fixed-opponent control for Table 4 | Clarifies mechanism | 1 week |
| P1.4 | RL scaling experiments | Run baselines at 320/1K/5K/20K episodes | Provides complete picture | 1-2 weeks |

### P2 (Nice-to-have — improves quality)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P2.1 | PUCT formula gaps | Fix N=0 case, discuss circular belief, report MH parameters | Enables reproducibility | 1 day |
| P2.2 | UCB formula | Add factor of 2, discuss non-stationarity | Improves correctness | 0.5 day |
| P2.3 | LLM sensitivity | Test with GPT-4 or Llama-3 | Strengthens robustness | 1-2 weeks |
| P2.4 | Dialogue evaluation | Add separate dialogue quality metrics (coherence, persuasiveness) | Strengthens Avalon analysis | 1-2 weeks |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------------|---------|-------------|-----------------|-------------------|
| E1 | STRATEGIST vs Human (Avalon) | 6-player Avalon, 10 participants, 30 games | Win rate, 7 survey metrics (1-6 scale) | STRATEGIST 0.333 vs Human 0.367 | "Comparable to human players" | Underpowered (N=30), asymmetric eval |
| E2 | Different LLM improvement methods | GOPS (40 func), Avalon (24 func), 4 baselines (Line, Greedy, BFS, BFS+thought) | Point difference (GOPS), Winrate (Avalon) | STRATEGIST best on all metrics | "Superior LLM skill learning" | High variance for GOPS (SD 0.99 vs mean 1.5) |
| E3 | RL vs STRATEGIST | GOPS (320 eps), Avalon (160 eps), vs AlphaGo/DeepRole adaptations | Point diff, winrate, transition steps | STRATEGIST higher in all comparisons | "Outperforms RL" | Extremely low episode budget for RL; unfair comparison |
| E4 | Feedback quality comparison | Population self-play vs LLM-critic vs Fixed opponent | Point diff (GOPS), Winrate (Avalon) | Population self-play best | "Evolutionary self-play effective" | Confounded by opponent count (4 vs 1 vs 0) |
| E5 | STRATEGIST vs LLM agents | vs ReAct, ReCon on game metrics | Winrate, tokens/round | STRATEGIST wins both | "Better than other LLM agents" | ReCon adaptation may not be faithful |
| E6 | MCTS scaling | Vary MCTS budget for initial vs improved VH | Winrate scaling curve | Improved VH scales better | "Bi-level scaling effective" | Only tested on GOPS |

### Research-Theme Gap Diagnosis

1. **New Knowledge**: The bi-level architecture and idea queue are novel, but the magnitude of the advance is unclear without fair RL comparisons and proper human evaluation.

2. **Reproducibility**: PUCT formula gaps, missing Metropolis-Hastings parameters, and LLM output variance reduce reproducibility.

3. **Impact on Practice/Understanding**: The strategic randomization finding is genuinely insightful but is a secondary behavioral observation, not the primary contribution.

### Proposed Research Experiments (P0/P1/P2)

**P0 Experiment: RL Scaling Analysis**
- Target Claim: "STRATEGIST outperforms RL"
- Hypothesis: STRATEGIST's advantage diminishes with more RL training data
- Minimal Design: Run AlphaGo-style RL at 320, 1K, 5K, 20K, 100K episodes on GOPS
- Controls: Same evaluation protocol as Table 3
- Metrics: Point difference, win rate
- Success Criterion: Identify the crossover point (if any) where RL catches up
- Estimated Cost: ~1-2 weeks compute
- Expected Gain: Fair and credible RL comparison

**P1 Experiment: Expanded Human Evaluation**
- Target Claim: "Human-competitive performance"
- Hypothesis: STRATEGIST achieves statistically equivalent win rates to humans
- Minimal Design: 150+ games, 30+ participants, pre-registered protocol
- Controls: Random voting baseline for correct-vote metric
- Metrics: Win rate with 95% CI, correct vote proportion by role, survey with validated scales
- Success Criterion: Non-inferiority test (margin δ = 0.1)
- Estimated Cost: 2-4 weeks
- Expected Gain: Statistically valid human comparison

**P2 Experiment: Single-Agent Transfer**
- Target Claim: "Generalizable framework"
- Hypothesis: STRATEGIST transfers to single-agent non-adversarial tasks
- Minimal Design: Apply to one text-based game (e.g., ALFWorld, ScienceWorld) without dialogue
- Controls: ReAct baseline
- Metrics: Success rate, improvement iterations needed
- Success Criterion: Positive improvement over initial strategy
- Estimated Cost: 2-3 weeks
- Expected Gain: Support for generalizability claim

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

The paper has a well-motivated architecture and interesting empirical findings (particularly the strategic randomization analysis). However, three major concerns prevent a higher score: (1) the RL comparison is conducted in an unfair regime that systematically disadvantages the baselines, undermining the central "superiority over RL" claim; (2) the human evaluation is underpowered and methodologically asymmetric, making the "human-competitive" claim unsubstantiated; and (3) key generalizability claims go beyond the evidence. The idea queue mechanism and bi-level design are legitimate contributions but their empirical support needs strengthening.

**Post-Revision Target: [6.5, 7.5] / 10**

If the authors (P0) reframe all comparative claims to reflect the limited-budget regime, (P0) expand the human evaluation with adequate statistical power, (P1) add RL scaling experiments, and (P1) address the technical gaps in the PUCT formulation, the paper would present a solid contribution to LLM-based decision-making. The bi-level architecture and idea queue are genuinely novel mechanisms that advance the state of the art in LLM strategy learning, but the current empirical package does not yet demonstrate their value convincingly enough relative to the strength of the claims made.