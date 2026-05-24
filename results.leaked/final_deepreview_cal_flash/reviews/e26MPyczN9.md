Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper re-evaluates influential claims that programmatic policies generalize better than neural policies in RL, showing across three benchmarks (TORCS, Karel, Parking) that much of the reported gap stems from uncontrolled experimental factors — reward design in TORCS, input featurization in Karel — rather than intrinsic representational advantages. The authors introduce an expressivity/discoverability framework to explain when and why a representation enables out-of-distribution generalization, and argue that programmatic representations provide a genuine advantage only when solutions require working memory that grows with input size, a class that fixed-capacity neural architectures cannot express. A proof-of-concept using FUNSEARCH synthesizes a BFS program for a wall-sparse Karel variant, demonstrating feasibility.

## Strengths

- **TORCS reward confound identified and experimentally confirmed.** The paper shows that reducing the speed coefficient (β=1.0→0.5) in the intrinsic reward allows DDPG-trained neural policies to generalize OOD at rates (76% to G-TRACK-2, 69% to E-ROAD) matching the programmatic NDPS (Table 1). This cleanly isolates the reward function — not representation — as the cause of the previously reported gap.

- **Simple neural baseline matches or exceeds programmatic policies on Karel.** PPO with last-action augmentation (a_{t-1}) achieves perfect 100×100 OOD generalization on 4 of 5 tasks (Stairclimber, Maze, TopOff, FourCorner), while LEAPS, ConvNet, and LSTM baselines all fail on multiple tasks (Table 2). This demonstrates that appropriate input featurization can make neural policies as effective as programmatic ones.

- **Expressivity/Discoverability framework provides a clean conceptual lens.** Definitions 2 and 3 formalize why prior comparisons were confounded: the DSL-induced policy spaces and neural spaces had similar expressivity, but discoverability (search) was inadvertently easier in the programmatic space. The framework gives the field a precise vocabulary for reasoning about representational advantages.

- **Rigorous and honest re-evaluation methodology.** Experiments use 30 seeds for TORCS β=0.5, 30 seeds for Karel a_{t-1}, 30 seeds for PSM, with transparent reporting of success rates, fractions of successful seeds, and confidence intervals. The Parking results are reported without spin — the authors honestly acknowledge that different metrics paint different pictures and that neither approach reliably solves the domain.

- **Theoretical identification of a principled limitation of fixed-capacity neural architectures.** The paper argues convincingly that neural policies with constant-memory design (feedforward, LSTM) cannot express algorithms requiring instance-scaling memory, using the Ω(log|V|) lower bound for vertex indexing and citing relevant theory (Weiss et al. 2018, Delétang et al. 2023, Nowak et al. 2023).

## Weaknesses

### Major

1. **Insufficient empirical support for the memory-scaling constructive claim.** The paper's positive thesis — that programmatic representations offer a decisive advantage when solutions require growing working memory — is supported by only three runs of FUNSEARCH on a wall-sparse Karel variant, with no variance reporting, no success rate across runs, no quantitative comparison to neural baselines on the same task, and no formal definition of the wall-sparse modification. While the theoretical expressivity argument is sound, the experimental evidence does not meet the rigorous standard the paper itself sets in Sections 4.1–4.3 (multiple seeds, confidence intervals, controlled comparisons). The paper labels this a "proof-of-concept," yet the abstract, introduction, and conclusion frame it as a central claim, creating an imbalance between the paper's parts.

### Minor

2. **FUNSEARCH experiment conflates representation with search algorithm.** The proof-of-concept uses Qwen 3-Coder (30B) + evolutionary search — a qualitatively different discovery mechanism from the end-to-end RL training used for neural baselines. The paper's own expressivity/discoverability framework warns that both factors must be accounted for, but this experiment does not isolate whether the success comes from the programmatic representation or the powerful search procedure.

3. **PARKING results are inconclusive.** The paper honestly reports that different evaluation metrics favor different methods (PSM has better generalization gap, DQN has higher absolute test success rate). While this honesty is a strength, it means the domain provides no clear evidence for either the re-evaluation narrative or the memory-scaling narrative, weakening the paper's overall empirical arc.

### Trivial

None.

## Nice-to-Haves

- **Strengthen the memory-scaling experiment.** Formally define the wall-sparse Karel variant, run the same neural baselines used in Section 4.2 (PPO+a_{t-1}, PPO+LSTM) on it, show that they fail OOD, and report FUNSEARCH synthesis success rate over many runs. This would bring the constructive claim to the same evidentiary standard as the re-evaluation.
- **Test whether neural architecture search or a different search procedure could also yield a BFS-like solution in a neural space.** This would isolate the role of the representation from the search algorithm.

## Removed Points

These points were raised by the reviewers but are excluded or downgraded for the reasons below:
- *"The paper claims to focus on expressivity but the proof-of-concept is about discoverability"* — The FUNSEARCH experiment demonstrates both existence (expressivity) and findability; the paper's theoretical expressivity argument is the primary support, making this criticism partially misaligned with the paper's structure. Kept as a related Minor weakness instead.
- *"No formal definition of the wall-sparse Karel variant"* — This may be described in Figure 7 (stripped by the parser); insufficient basis to include as a standalone weakness.
- *Several generic "could be" concerns from the harsh critic* (e.g., "the advantage might stem from the search algorithm") — These are incorporated into the Minor weakness above; standalone speculative concerns are removed.
- *Strength Finder strength #3 ("proof-of-concept that programmatic representations can provide OOD guarantees")* conflicts with verified Weakness #1; the weakness prevails, so this strength is listed as context-dependent rather than a standalone strong point.
- *Formatting/style nitpicks and comments about missing appendix content* — These are parser artifacts or outside the paper's intended scope.

## Novel Insights

The paper's framework — separating expressivity from discoverability — provides a precise diagnostic tool for the programmatic-policy literature. The most striking insight is that the TORCS advantage was entirely a reward artifact: programmatic policies were not better at generalizing, they were simply worse at speeding, and that slowness happened to transfer. The conceptual pivot to memory scaling as the axis where representational differences are *forced* (not just confounded) gives the field a concrete research direction beyond "programs are good, neural nets are bad."

## Suggestions

- Reframe the paper to more clearly separate the completed re-evaluation contribution from the forward-looking memory-scaling hypothesis. Consider either substantially strengthening the constructive experiment or explicitly demoting it to a "hypothesis with preliminary illustration" rather than a co-equal contribution.
- Add a formal description of the wall-sparse Karel variant and run the same neural baselines from Section 4.2 on it to demonstrate that they do fail OOD.
- Report FUNSEARCH synthesis statistics across many runs (success rate, variance, program length distribution).

## Score and Decision

**Calibration Anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| It4KL6XnPq — Foundation Policies with Memory | 3.00 | R1 | Much weaker; less rigorous, narrower scope |
| fvTaoyH96Z — Non-Param. Randomization | 2.33 | R1 | Weak paper; not directly comparable |
| NGVljI6HkR — Reclaiming Source of Prog. Policies | 3.67 | R1 | Same topic, much less comprehensive; current paper clearly stronger |
| PH7ja3T0vN — State Combinatorial Generalization | 4.50 | R1 | Different topic; less directly relevant |
| UfczlMudN6 — GRAM | 6.00 | R1 | Similar rigor, narrower scope; comparable |
| tuEP424UQ5 — Generalization in MORL | 5.75 | R1,R2 | Similar structure (formalization+experiments); current paper slightly stronger |
| 3w6xuXDOdY — Generalization Gap in Offline RL | 6.50 | R1 | Systematic empirical study; comparable quality |
| agPpmEgf8C — Predictive Auxiliary Objectives | 8.00 | R1 | Top-tier; current paper not at this level |
| X1p0eNzTGH — How Level Sampling | 5.67 | R2 | Generalization investigation; current paper more comprehensive |
| ljwoQ3cvQh — DNNs Extrapolate Predictably | 7.00 | R2 | Strong empirical study; better executed but different topic |
| 2uQBSa2X4R — Robust Gymnasium | 6.50 | R2 | Benchmark paper; comparable contribution |

**Round 1 bracket:** The paper sits between weak anchors (~2–3) and strong anchors (8.0), with the most topically similar anchors scoring 3.67–6.50. Initial bracket: 4.0–7.0.

**Round 2 narrowing:** Compared directly against anchors at 5.75 (MORL generalization, accepted), 6.00 (GRAM, rejected), and 6.50 (Offline RL generalization gap, accepted), the current paper is slightly stronger than the 5.75 anchor due to more extensive experiments, comparable to the 6.00 anchor but with broader scope, and comparable to the 6.50 anchor but slightly held back by the imbalance between the rigorous re-evaluation and the thin constructive evidence. This places the paper at 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>