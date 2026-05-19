## Summary
# Final Review Report

## Summary
This paper introduces STRATEGIST, a bi-level framework for LLM decision-making in adversarial multi-agent environments. The approach abstracts complex policies into high-level, interpretable text-based strategies (value heuristics or dialogue guides) that are iteratively improved via an LLM-driven evolutionary process with an idea queue. These high-level strategies are then refined into executable low-level policies using Monte Carlo Tree Search (MCTS) or Chain-of-Thought prompting. The framework is evaluated on two challenging games: the Game of Pure Strategy (GOPS) and The Resistance: Avalon. Results indicate that STRATEGIST outperforms traditional RL methods (AlphaGo, DeepRole) and other LLM-based self-improvement techniques, while achieving performance comparable to human players in Avalon. The paper demonstrates the potential of combining LLM reasoning with structured search for efficient skill acquisition without parameter updates.

## Strengths
1. **Innovative Bi-Level Abstraction:** The core idea of abstracting policies into high-level, LLM-editable value heuristics (Python code) or dialogue guides is highly creative. It effectively bridges the gap between the reasoning capabilities of LLMs and the precise planning requirements of game-playing agents.
2. **Modular Idea Queue Mechanism:** The introduction of an idea queue with UCB sampling for modular strategy improvement is a strong methodological contribution. It allows for incremental, interpretable updates and helps the search process escape local maxima, as evidenced by the evolutionary path visualizations.
3. **Comprehensive Experimental Evaluation:** The paper evaluates the framework on two distinct and challenging environments (GOPS and Avalon), covering both non-dialogue and dialogue-based actions. The comparisons against traditional RL methods, other LLM self-improvement techniques, and human players provide a robust validation of the approach.
4. **Sample Efficiency:** The demonstration that STRATEGIST outperforms deep RL methods while utilizing significantly fewer training transition steps highlights its exceptional sample efficiency, a critical advantage for LLM-based agents where compute costs are high.

## Weaknesses
1. **Inconsistent Claim-Evidence Alignment:** The third contribution bullet claims STRATEGIST achieves "higher win rates than both existing agents and human players." However, Table 1 shows STRATEGIST's win rate (0.333) is slightly lower than that of humans (0.367) in the 6-player Avalon setting. This factual inconsistency undermines the credibility of the contribution statements.
2. **Notation Ambiguity in Formalism:** Section 2.1 introduces a notation collision where `A` is used for both the global action space and the state-dependent legal action function (`A : S → N , P(A)`). This creates ambiguity and reduces reproducibility.
3. **Unsupported Extrapolation in Limitations:** The limitations section extrapolates that "similar performance will be observed in single agent, non-adversarial settings" without empirical basis. The mechanisms driving success in adversarial settings (e.g., opponent modeling) may not translate directly to single-agent tasks.
4. **Incomplete Variance Reporting:** While the paper acknowledges high variance and environmental noise, standard deviations or confidence intervals are not consistently reported across all comparative tables, making it difficult to assess the statistical reliability of small performance margins.
5. **Generic Gap Statement:** The introduction's gap statement regarding LLMs in adversarial environments is somewhat high-level. It could more explicitly connect the challenge to the computational cost of per-step LLM querying and the lack of structured strategic abstraction to better motivate the bi-level approach.

## Key Issues
1. **Factual Contradiction in Contributions:** The claim of outperforming humans in win rate directly contradicts Table 1. This must be corrected to "comparable to" or "competitive with" human players to maintain scientific integrity.
2. **Notation Collision in Problem Definition:** The reuse of symbol `A` for both action space and legal action function creates ambiguity. Renaming the legal action function (e.g., to `L`) is necessary for formal clarity.
3. **Unbounded Generalization Claims:** The extrapolation to single-agent, non-adversarial settings in the limitations section lacks empirical support and should be bounded or removed to avoid overclaiming.
4. **Inconsistent Statistical Reporting:** Given the acknowledged high variance in multi-agent feedback, consistent reporting of mean ± standard deviation across all key comparative tables is essential for assessing result reliability.

## Actionable Suggestions
1. **Correct Contribution Claims:** Update the third contribution bullet to state that STRATEGIST achieves "performance comparable to human players" rather than "higher win rates," aligning with Table 1 data.
2. **Clarify Formal Notation:** Rename the legal action function in Section 2.1 from `A` to `L` (or `A_s`) and explicitly define its codomain as `2^A` to resolve notation collision and improve reproducibility.
3. **Bound Generalization Claims:** Revise the limitations section to remove the unsupported extrapolation to single-agent settings. Instead, frame it as an open question for future empirical validation.
4. **Enhance Statistical Reporting:** Ensure all key comparative tables (e.g., Table 2, Table 3) consistently report mean ± standard deviation or confidence intervals to address the acknowledged high variance in multi-agent feedback.
5. **Tighten Introduction Gap Statement:** Explicitly connect the adversarial multi-agent challenge to the computational cost of per-step LLM querying and the lack of structured strategic abstraction, creating a stronger narrative bridge to the bi-level framework.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Traditional RL requires vast data, while LLMs struggle with complex, long-horizon planning in adversarial multi-agent environments due to per-step querying costs and lack of strategic structure.
- **S2 (Significance/Challenge):** Effective decision-making in these settings requires balancing high-level strategic reasoning with precise low-level action execution, a gap current LLM agents fail to address efficiently.
- **S3 (Prior Gap):** Existing methods either rely on expensive gradient updates (RL) or unstructured per-step prompting (LLM agents), lacking a mechanism for data-efficient, interpretable strategy abstraction.
- **S4 (Proposed Method):** We introduce STRATEGIST, a bi-level framework that uses LLMs to learn and iteratively improve high-level strategy abstractions (value heuristics/dialogue guides), which are refined into executable policies via MCTS or CoT.
- **S5 (Key Result & Bounded Implication):** STRATEGIST outperforms RL and LLM baselines on GOPS and Avalon with superior sample efficiency, achieving win rates comparable to human players in Avalon.

### Introduction Outline (Complete)
- **P1 (Big Picture & Gap):** Establish LLM potential in interactive environments, then identify the specific bottleneck in adversarial multi-agent settings: computational prohibitive per-step querying and absence of structured strategic abstraction.
- **P2 (Research Questions & Solution):** Pose refined questions on abstracting high-level strategies and refining them efficiently. Introduce STRATEGIST as the bi-level solution bridging LLM reasoning and precise search.
- **P3 (Method Overview):** Briefly explain the high-level evolutionary idea queue and low-level MCTS/CoT executor, emphasizing the non-parametric, self-play-driven nature.
- **P4 (Evidence Preview):** Preview results on GOPS and Avalon, highlighting sample efficiency over RL and human-comparable performance in Avalon.
- **P5 (Contributions):** List three explicit, bounded contributions: (1) bi-level framework, (2) modular idea queue improvement method, (3) empirical validation on dialogue/non-dialogue games with sample efficiency gains.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0 (Critical)** | Correct contribution claim regarding human win rates to match Table 1 data. | Restores scientific credibility and claim-evidence alignment. | Low |
| **P0 (Critical)** | Resolve notation collision in Section 2.1 (`A` vs legal action function). | Improves formal clarity and reproducibility. | Low |
| **P1 (High)** | Add mean ± std or confidence intervals to all key comparative tables. | Addresses acknowledged variance and strengthens statistical reliability. | Medium |
| **P1 (High)** | Bound or remove unsupported extrapolation to single-agent settings in Limitations. | Prevents overclaiming and maintains rigorous scope. | Low |
| **P2 (Medium)** | Tighten introduction gap statement to explicitly link to computational cost and abstraction needs. | Strengthens narrative motivation and bridge to method. | Low |
| **P2 (Medium)** | Clarify UCB formula notation (square root, exploration constant, denominator definition). | Improves theoretical grounding and reproducibility. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | STRATEGIST vs Humans | 6-player Avalon, 30 games | Win Rate, Survey Metrics | Comparable win rate (0.333 vs 0.367), better concealment | Human-comparable performance | Small sample size (30 games) |
| E2 | STRATEGIST vs LLM Improvement Methods | GOPS & Avalon, 40/24 strategies | Points/Winrate | STRATEGIST outperforms Line/Greedy/BFS search | Idea queue effectiveness | Limited to GPT-3.5 |
| E3 | MCTS Scaling | GOPS, varying search budgets | Performance score | Improved heuristics scale better with MCTS | Bi-level synergy | Single game evaluation |
| E4 | STRATEGIST vs RL (AlphaGo/DeepRole) | GOPS & Avalon, matched episodes | Winrate/Points | STRATEGIST wins with fewer training steps | Sample efficiency | RL adapted to setting, not full SOTA |
| E5 | Feedback Quality Comparison | GOPS & Avalon | Points/Winrate | Population self-play > LLM-critic/Fixed opponent | Self-play feedback value | Fixed opponent baseline weak |

### Research-Theme Gap Diagnosis
The core research value lies in demonstrating that LLMs can efficiently learn high-level strategic abstractions without parameter updates. However, the generalizability of this approach to other partial-information games and the robustness of the learned strategies against distribution shifts remain weakly supported.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Sample Efficiency | STRATEGIST maintains advantage with even fewer episodes. | Reduce episodes to 50% of current budget. | AlphaGo, DeepRole | Winrate | STRATEGIST still wins | Low | Strengthens efficiency claim |
| Robustness to Noise | Learned strategies generalize across different LLM seeds. | Evaluate top strategies across 5 different LLM seeds. | Baseline LLM agents | Winrate variance | Lower variance than baselines | Medium | Addresses acknowledged noise |
| Generalizability | STRATEGIST transfers to another social deduction game (e.g., Werewolf). | Apply STRATEGIST to Werewolf benchmark. | ReCon, Agent-Pro | Winrate | Competitive performance | High | Validates framework generality |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
Final Score: 6.5/10
Post-Revision Target: [7.5, 8.5]/10

**Scoring Rationale:**
The paper presents a highly creative and well-motivated bi-level framework that effectively bridges LLM reasoning with structured search. The sample efficiency gains over traditional RL and the strong performance in complex games like Avalon are significant contributions. However, the score is moderated by factual inconsistencies in the contribution claims (specifically regarding human win rates), notation ambiguities in the formalism, and incomplete variance reporting given the acknowledged environmental noise. Addressing these key issues and tightening the claim-evidence alignment would substantially improve the paper's scientific rigor and credibility.