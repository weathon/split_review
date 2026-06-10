## Summary
This paper re-evaluates the claim that programmatic (DSL-based) policies generalize better than neural policies in RL across three benchmarks (TORCS, KAREL, PARKING), arguing that much of the reported gap is due to experimental confounds (reward shaping, observation design) rather than representational differences. It proposes an expressivity/discoverability framework and argues that the genuine advantage of programmatic representations lies in their ability to express solutions with instance-scaling memory, supported by information-theoretic arguments and a FUNSEARCH proof-of-concept.

## Strengths
- **KAREL re-evaluation is clean and convincing (Table 2):** "PPO with a_{t-1}" — a fully connected network with augmented last-action observation — achieves perfect generalization (1.00 return) on 4/5 tasks at 100×100 scale, matching LEAPS and dramatically outperforming both ConvNet and LSTM baselines. This directly demonstrates that the prior generalization gap was a confound of observation design rather than a representational difference.
- **Expressivity/Discoverability framework (Definitions 2–3):** Formalizes OOD generalization into two necessary conditions — whether the policy space contains a generalizing solution and whether the search algorithm can find it — providing useful vocabulary for analyzing confounds in all three benchmarks and making predictions about when programmatic representations provide a genuine advantage.
- **Instance-scaling memory argument with complexity lower bounds (Section 5):** Provides rigorous information-theoretic arguments (Ω(log|V|) bits for vertex indexing, Θ(|V|) working memory for BFS) that formally characterize when fixed-capacity neural architectures fail on expressivity. This goes beyond empirical observation and connects the RL generalization debate to fundamental computational requirements.
- **Transparent and honest reporting:** The paper reports that PARKING results are mixed, that only 13/30 TORCS seeds succeed at training, and that HARVESTER at 100×100 remains unsolved by all methods. This honesty strengthens credibility even when the results are not uniformly favorable.
- **Sparsity-driven insight (Section 4.4):** Identifies that programmatic solutions use sparse conditions (single variables in Boolean expressions, Figure 5) while neural networks use all available features, connecting to the generalization-through-sparsity literature and providing an intuitive mechanism for the observed effects.

## Weaknesses

### Fatal
None.

### Major
- **TORCS re-evaluation is weaker than the headline claim suggests:** Only 13 of 30 (43%) neural seeds successfully learn to complete the G-TRACK-1 training track with β=0.5, and 4 of 15 on AALBORG (Table 1 footnote). The majority of neural models fail on the *training* domain itself — a brittleness NDPS did not exhibit (all 3 seeds succeeded). Combined with the required reward function redesign (β=0.5), the practical message is that making neural policies competitive requires substantial domain-specific effort and yields low training success rates. The abstract's claim that neural policies "can match or exceed" programmatic ones overstates the result; it should more honestly be framed as "among the minority of seeds that succeed at training, most generalize." The distinction between the paper's headline framing and its actual experimental findings is significant.

- **FUNSEARCH proof-of-concept lacks critical details needed to support the strongest claim:** The paper states "Three runs of FUNSEARCH returned a correct implementation of breadth-first search" (line 308) without disclosing total runs attempted. No neural baseline (transformer, memory-augmented model) is tested on SparseMaze, and no scaling study shows the synthesized BFS generalizing across maze sizes. This is the paper's primary evidence for its strongest theoretical claim — that programmatic representations provide an inherent advantage on problems requiring instance-scaling memory — yet it reads as an anecdote rather than a compelling result. Even a few additional data points (run success rate, a neural baseline failure, or a scaling demonstration) would substantially strengthen this section.

### Minor
- **HARVESTER at 100×100 shows no method works well, underemphasized:** PPO with a_{t-1} achieves only 0.04 return and LEAPS achieves 0.00 (Table 2). This suggests the observation-augmentation fix doesn't universally close the generalization gap and should be discussed more prominently rather than buried in the table alongside four tasks where it works perfectly.

- **PARKING results are ambiguous relative to the headline claim:** DQN achieves higher test success rate (0.18 vs 0.16) while PSM has a smaller train-test gap (0.10 vs 0.68) — Table 3. The paper acknowledges this but then uses PARKING to motivate better benchmarks, which partially undercuts the abstract's framing. The abstract should differentiate between benchmarks where the claim holds cleanly (KAREL), partially (TORCS with caveats), and where it doesn't clearly hold (PARKING).

### Trivial
None.

## Nice-to-Haves
- A scaling study for the FUNSEARCH BFS solution (testing on mazes of varying sizes) would transform the proof-of-concept from an anecdote into a compelling result.
- Discussion of why 17/30 TORCS seeds fail on training with β=0.5 would be informative and bear on whether "confound" is the right framing versus "neural policies require significant engineering effort to match programmatic ones."

## Removed Points
These points are flagged to be removed, treat them with caution.
- Harsh critic's concern about "modifications being domain-specific and non-trivial" — the paper explicitly frames its contribution as identifying what confounds were present in each benchmark, not as providing a universal fix. Varying confounds across domains is the expected finding.
- Strength finder's "rigorous experimental protocol for KAREL" as a standalone strength — reporting 30 seeds with standard deviations is standard practice, not a distinguishing contribution.

## Novel Insights
The paper's most novel contribution is connecting the programmatic vs. neural generalization debate to the concept of instance-scaling memory with formal information-theoretic lower bounds. By showing that indexing a vertex among |V| candidates requires Ω(log|V|) bits — exceeding the fixed capacity of standard architectures — the paper reframes the debate from "which representation empirically performs better" to "what computational requirements does the problem impose on the representation." This is a more principled and actionable framing that yields concrete predictions about when each representation class should be preferred.

## Suggestions
- Revise the abstract to accurately reflect that TORCS required reward redesign with only 43% training success rate, and that PARKING results are ambiguous. Differentiate between benchmarks where the claim holds cleanly (KAREL) and where it requires caveats.
- For FUNSEARCH: report total number of runs attempted, test at least one neural baseline on SparseMaze, and ideally show a small scaling study across maze sizes.
- Expand discussion of HARVESTER's poor results at 100×100 for all methods as evidence that the problem remains open in some domains.

## Calibration Report

**Round 1 (bracketing):**
- fvTaoyH96Z (2.33): Non-Parameterized Randomization — rejected, much weaker empirical study
- It4KL6XnPq (3.00): Foundation Policies with Memory — rejected, limited contribution
- 473sH8qki8 (2.00): Reward as Observation — rejected, much weaker
- 5f0n5yi8qK (3.40): Training Open-ended Policies — rejected, weaker
- tuEP424UQ5 (5.75): MORL Generalization — accepted benchmark paper; this paper has stronger conceptual contribution
- 3w6xuXDOdY (6.50): Generalization Gap in Offline RL — accepted evaluation paper; comparable ambition, this paper has stronger conceptual framework
- NGVljI6HkR (3.67): Reclaiming the Source of Programmatic Policies — accepted, same research group; this paper is substantially stronger in scope and depth
- X1p0eNzTGH (5.67): Level Sampling and Zero-Shot Generalisation — rejected; this paper is stronger
- OI3RoHoWAN (8.00): GenSim — accepted, much stronger
- DzGe40glxs (8.00): Interpreting Emergent Planning — accepted, much stronger
- 9pW2J49flQ (8.00): DeepLTL — accepted, much stronger
- agPpmEgf8C (8.00): Predictive auxiliary objectives — accepted, much stronger

**Round 2 (narrowing):**
- ehSQZa4vuk (5.25): Bad Habits: Policy Confounding — rejected, similar topic but only toy experiments; this paper is clearly stronger
- eY5JNJE56i (6.75): Offline RL with Smooth OOD Generalization — accepted, novel method + theory; comparable strength, different profile
- 3mnWvUZIXt (7.25): Principled Representation Learning from Videos for RL — accepted, theoretical + empirical; this paper is slightly weaker
- s9SVlWOcLt (6.75): Proto Successor Measure — rejected despite high average; strong theoretical contribution

**Bracket:** Initial 5.5–7.5, narrowed to 6.0–7.0 after round 2. The paper is clearly better than the 5.25 anchor ("Bad Habits"), comparable to the 6.50–6.75 anchors, and slightly below the 7.25 anchor. The conceptual contribution (expressivity/discoverability framework, instance-scaling memory argument) pushes it toward the upper end, but TORCS caveats and FUNSEARCH underspecification prevent it from reaching 7+.

**Final score: 6.5.** A solid paper making a genuine conceptual contribution by reframing the programmatic vs. neural generalization debate, supported by strong KAREL experiments and well-reasoned theoretical arguments. The TORCS and FUNSEARCH weaknesses are real but addressable.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>