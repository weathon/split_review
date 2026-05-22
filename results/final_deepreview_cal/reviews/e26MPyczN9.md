Now I have sufficient anchors. Let me synthesize the final review.

**Calibration summary:**

Round 1 bracket: [5.0, 7.0]

Round 2 anchors read in full:
- "The Generalization Gap in Offline RL" (6.50) — similar benchmarking/re-evaluation study, more thorough experiments but weaker conceptual framework. Current paper is comparable but slightly weaker on experimental breadth.
- "On Generalization Within MORL" (5.75) — framework + benchmark paper with mixed reviews. Current paper has cleaner experiments and more impactful central claim.
- "How the Level Sampling Process..." (5.67) — rejected with evidence gaps. Current paper is stronger on clarity and evidence.
- "InnateCoder" (5.75) — programmatic policies + LLMs, rejected. Current paper is conceptually stronger.
- "On Provable Length and Compositional Generalization" (5.25) — rejected, strong assumptions limit relevance.
- "Towards Bridging Generalization and Expressivity of GNNs" (6.75) — theoretical paper on expressivity/generalization trade-off, stronger theory but different domain.

The current paper sits between the Offline RL paper (6.50) and the MORL paper (5.75). The TORCS and Karel confound experiments are clean and well-presented, the framework is useful, but the proof-of-concept disconnect and some experimental gaps prevent it from reaching the 6.5+ tier. Final score: 6.0.

---

## Summary

This paper re-evaluates three influential claims (TORCS, Karel, Parking) that programmatic policies generalize better OOD than neural policies in RL. It identifies experimental confounds — reward shaping in TORCS, full observability in Karel — that explain most of the reported gap. After controlling these factors, neural policies match programmatic ones. The paper then proposes an expressivity/discoverability framework and argues that programmatic representations have a genuine advantage only for problems requiring instance-scaling working memory (e.g., BFS pathfinding), which fixed-capacity neural networks cannot express. A proof-of-concept using FunSearch to synthesize a BFS implementation supports the expressivity claim.

## Strengths

- **TORCS confound is cleanly identified and experimentally demonstrated (Section 4.1, Table 1).** The paper shows that changing β from 1.0 to 0.5 in the intrinsic reward function allows DDPG to generalize from G-TRACK-1 to OOD tracks at rates comparable to NDPS (76–100%), directly attributing the previously reported gap to speed optimization rather than representation. This is a controlled, persuasive experiment.

- **Karel last-action augmentation enables neural OOD generalization where prior methods failed (Section 4.2, Table 2).** PPO with a feedforward network + last action generalizes perfectly (1.00 return) to 100×100 grids on four of five Karel tasks, while LSTM and ConvNet baselines (from Trivedi et al. 2021) collapse. This cleanly identifies partial observability with spurious feature removal, not representation type, as the key factor.

- **Expressivity/discoverability framework is useful and well-motivated (Section 5, Definitions 2–3).** The framework separates two necessary conditions for OOD generalization and provides conceptual clarity for understanding why prior comparisons were confounded (both representations satisfied expressivity, but discoverability was unevenly controlled). The theoretical argument about Ω(log |V|) memory for vertex indexing is sound.

- **Honest characterization of Parking results (Section 4.3, Table 3).** The paper acknowledges that neither PSM nor DQN reliably solves OOD Parking (test success rates 0.16 vs 0.18) and that the evidence is mixed — a candid assessment that strengthens rather than weakens the paper's credibility.

## Weaknesses

### Major

- **The FunSearch proof-of-concept is disconnected from the paper's RL core (Section 5, final paragraphs).** The paper synthesizes BFS using FunSearch + Qwen 3-Coder (30B) — a large LLM-based program synthesis system operating in Python, not an RL algorithm searching a DSL-defined policy space. The paper's central claim about programmatic representations in RL is not demonstrated by this experiment, which belongs to a fundamentally different paradigm (LLM-as-oracle program synthesis). No evidence or argument is provided that existing programmatic RL methods (NDPS, LEAPS, PSM) or their DSLs could express BFS-like solutions. This creates a gap between the re-evaluation (which is thorough and well-connected to prior work) and the constructive claim. The paper should either (a) show that an existing programmatic RL approach can synthesize memory-scaling solutions, or (b) explicitly acknowledge that this advantage remains theoretical / requires richer representations than current programmatic RL methods use, and reframe the experiment as an illustration of possibility rather than evidence.

- **FunSearch details are too sparse to assess (Section 5).** The paper reports only "Three runs of FUNSEARCH returned a correct implementation of breadth-first search." Missing: number of total attempts, success rate, the prompt used, the evaluation/specification function, the number of candidate programs generated and evaluated, computational cost. Without this information, the reader cannot gauge the reliability or practical significance of the result.

### Minor

- **Parking results are presented with a framing that overstates the case for PSM (Section 4.3).** The paper writes "our results suggest that the PSM policies generalize better than the DQN policies" primarily because the train-to-test gap is smaller (0.10 vs 0.68). However, a model that performs poorly on both train and test naturally has a smaller gap. On the absolute test success rate, DQN (0.18) slightly exceeds PSM (0.16), and the 95% CIs overlap substantially. The Successful-on-100 metric favors PSM (0.06 vs 0.00) but this reflects 2/30 PSM seeds vs 0/15 DQN seeds — the asymmetry (30 vs 15 seeds) weakens this comparison. The paper's claim that Parking "points in the direction of benchmarks that could distinguish the generalization power" overstates what the evidence supports.

- **HARVESTER failure is not analyzed (Table 2).** PPO with a_{t-1} fails catastrophically on HARVESTER (0.04 on 100×100 vs 0.59 on small), while programmatic methods also perform poorly. This is the most interesting case study in the Karel suite — unlike Maze and Stairclimber (constant-memory heuristics suffice), HARVESTER may require different capabilities. The paper does not discuss why the simple trick fails here, which would strengthen the argument about what kinds of problems do and do not benefit from different representations.

- **NDPS ablation for the cautious reward is missing (Section 4.1).** The paper shows that DDPG with β=0.5 matches NDPS (originally trained with β=1.0). It does not test whether NDPS also benefits from β=0.5, or whether DDPG with β=1.0 could generalize with different hyperparameters or architectures. The comparison is asymmetrical: one specific neural method with a modified reward vs. one specific programmatic method with the original reward. While the main insight (speed optimization is the confound) remains well-supported, the incomplete factorial design leaves minor ambiguity about whether the confound is fully isolated.

- **LSTM failure in Karel is vaguely attributed to "complexity" (Section 4.2).** The paper states LSTMs "tend to be more complex to train than fully connected networks" but does not explore why they fail — whether it is a training difficulty (reward shaping, hyperparameter sensitivity, optimization landscape) or a fundamental representational limitation. This matters because the paper later argues LSTMs could in principle solve these tasks, implying the failure is in discoverability not expressivity, but the evidence for this is circumstantial.

### Trivial

- The paper states neural policies "match or exceed" programmatic OOD generalization in the abstract. "Exceed" is justified for Karel (PPO with a_{t-1} gets 1.00 vs LEAPS's 0.21–0.45 on TOPOFF and FOURCORNER) but the phrasing could be clearer.

## Nice-to-Haves

- A discussion of why HARVESTER resists the last-action trick would strengthen the Karel analysis and provide insight into what makes a problem genuinely hard for constant-memory strategies.
- A brief investigation into whether LEAPS's programs on Maze/Stairclimber encode the same wall-following heuristics as the neural policies would make the expressivity-equivalence argument more concrete.
- Reporting computational cost for the FunSearch run (number of candidates evaluated, wall time, API cost) would help readers gauge practicality.
- Testing the DDPG+β=0.5 vs NDPS+β=0.5 comparison would complete the TORCS ablation.

## Removed Points

- The harsh critic's claim that the paper's "exceed" claim is unsupported: the abstract is justified by Karel results (PPO with a_{t-1} achieves 1.00 on TOPOFF and FOURCORNER where LEAPS achieves 0.21 and 0.45 respectively).
- The critic's claim that "our modifications help the gradient search find generalizing solutions" is "retroactive": the paper explicitly distinguishes intrinsic (training) reward from evaluation metrics (lap time, crashes), so modifying β does not change the task; it changes the training signal, which is exactly the mechanism being tested.
- The critic's claim that the Karel a_{t-1} result is not adequately contextualized because the paper doesn't discuss LEAPS programs: the paper already makes the expressivity/discoverability argument that both representations can encode the same heuristics, and the point is about discoverability — this is addressed on pages 7–8 and in Section 5.
- The critic's claim about the TORCS confound being "undersold" due to missing NDPS+β=0.5 comparison: this is a secondary ablation; the primary claim (speed optimization confound) is well-supported by the existing experiment.
- The critic's point about "match or exceed" in the abstract being unsupported: already addressed above.
- Pure formatting/style nitpicks about presentation.

## Novel Insights

The paper's key insight is that the reported generalization gap between programmatic and neural policies in three influential prior studies can be attributed to specific experimental confounds (reward shaping, observation design) rather than representational differences. The framework distinguishing expressivity from discoverability is a clarifying lens for the field — it explains why controlling for discoverability is difficult when expressivity is already satisfied, and identifies that the genuine advantage of programmatic representations lies not in the commonly studied benchmarks but in problems requiring memory that scales with input size. This reframes the research agenda from "which representation is better" to "which representation is better for which class of problems."

## Score and Decision

**Score:** 6.0

**Decision:** Accept

**Calibration details:**
- Round 1 bracket: [5.0, 7.0]
- Round 2 anchors: (a) "The Generalization Gap in Offline RL" (6.50, Accept) — similar re-evaluation/benchmarking study, more thorough experiments but weaker conceptual framework. The current paper matches this on conceptual contribution and quality of core experiments, but falls slightly short on experimental breadth and has a weaker positive result. (b) "On Generalization Within MORL" (5.75, Accept) — framework + benchmark with mixed reviews. Current paper has stronger experimental evidence. (c) "InnateCoder" (5.75, Reject) — programmatic policies + LLMs. Current paper is more impactful. (d) "How the Level Sampling Process..." (5.67, Reject) — had evidence/presentation issues. Current paper is stronger. (e) "Towards Bridging Generalization and Expressivity of GNNs" (6.75, Accept) — stronger formal theory but different domain. Current paper's re-evaluation experiments and conceptual framework place it slightly below this anchor. (f) "On Provable Length and Compositional Generalization" (5.25, Reject) — too idealized. Current paper is more empirically grounded and impactful. The paper sits at 6.0 — above the 5.5–5.75 tier (e.g., InnateCoder, Level Sampling) due to cleaner experiments and a more useful framework, but below the 6.5+ tier due to the proof-of-concept disconnect from the RL setting and incomplete experimental details.

<score>6.0</score>
<decision>Accept</decision>