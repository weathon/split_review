Now let me search for calibration anchors.**Round 1 Bracket: 5.0 – 6.5.** The paper sits above the weak anchors (~3.0) due to its concrete, well-run experiments and clean Karel result. It falls below the strong anchors (8.0) due to the partial Parking contradiction and thin FunSearch proof-of-concept. Let me narrow within 5–6.5.Now I have enough information to write the final review.

---

## Summary

This paper re-evaluates OOD generalization claims for programmatic policies across three benchmarks (TORCS, Karel, Parking), arguing that much of the reported advantage over neural policies stems from experimental confounds rather than representational differences. The paper introduces a conceptual framework — *expressivity* (whether a policy class can represent a generalizing solution) and *discoverability* (whether the search algorithm can find it) — to structure this analysis. It also identifies a principled boundary: problems requiring working memory that grows with input size (e.g., general pathfinding) cannot be solved by fixed-capacity neural architectures, and offers a proof-of-concept where FUNSEARCH synthesizes BFS to provably generalize in a wall-sparse Karel maze.

---

## Strengths

1. **Clean Karel result.** Table 2 shows that "PPO with a_{t-1}" — a feedforward network augmented only with the agent's last action — achieves perfect generalization to 100×100 grids on STAIRCLIMBER, MAZE, TOPOFF, and FOURCORNER (return 1.00), while both PPO with ConvNet and PPO with LSTM fail entirely on 100×100 problems. This directly and reproducibly demonstrates that the prior generalization advantage attributed to LEAPS arose from input sparsity (local vs. full observability), not the programmatic representation itself. Notably, LEAPS also uses local observations, so the comparison is fair.

2. **TORCS reward-function confound.** Table 1 shows that 76% (13/30 successful models) and 69% of neural models generalize under the cautious reward (β=0.5) to OOD tracks where all β=1.0 neural models crashed. The mechanism is clearly articulated: the original reward incentivizes speed-maximizing behavior that generalizes poorly to sharp turns, while the programmatic policies happened to be less effective at speed optimization. The note that β is an intrinsic reward while evaluation is on lap time/crash is an important and correct clarification.

3. **Expressivity/discoverability framework.** Definitions 2–3 provide a principled vocabulary for analyzing why a representation may fail at OOD generalization, distinguishing the case where a generalizing solution is absent from the representation class from the case where the search merely fails to find it. The paper applies this framework to argue that TORCS and Karel satisfy expressivity for neural networks, while working-memory-requiring tasks like pathfinding do not. The argument via TORCS's if-then-else language approximating ReLU networks (with cite) is informal but plausible and anchored in prior work.

4. **Correct identification of a principled limit.** Section 5's argument that constant-capacity models cannot generalize for pathfinding — because merely indexing a vertex among |V| candidates requires Ω(log|V|) bits — is logically sound. The connection to NetHack nested subproblems is a concrete, actionable extension of this insight.

---

## Weaknesses

### Fatal
None.

### Major

- **The Parking result partially contradicts the headline claim.** The abstract states that neural policies "can match or exceed the OOD generalization of programmatic policies" across the three benchmarks. Yet Table 3 shows PSM has a generalization gap of 0.10 (0.26→0.16) vs. DQN's 0.68 (0.86→0.18), and 2/30 PSM models generalize reliably (Successful-on-100) while 0/15 DQN models do. The paper acknowledges this ("Our results suggest that PSM policies generalize better than DQN policies") in Section 4.3, but then softens it ("PARKING is a challenging domain for both types of representation") without offering any fix or deeper analysis of why the confound-removal strategy fails here. The paper's own framing in Section 4.4 identifies that both representations *could in principle* encode the solution, yet DQN does not generalize, indicating an unresolved discoverability problem that is not adequately reconciled with the main thesis. The conclusion and abstract should be calibrated to reflect this.

- **TORCS: asymmetric training success base rates weaken the generalization fractions.** Table 1 notes that 13/30 G-TRACK-1 models and 4/15 AALBORG models successfully learned the training task; generalization fractions (76%, 69%, 100%, 100%) are computed only over these subsets. The NDPS comparison is over 3/3 seeds that all completed training. This creates an asymmetry: the neural fractions condition on a selected subset of "lucky" seeds (~43–27% training success rates), while NDPS is evaluated on all trained models. The paper is transparent about this but does not compute an equivalent "fraction of all trained seeds that generalize" for both approaches, which would yield a more comparable summary statistic.

### Minor

- **LSTM failure is empirically observed but unexplained.** Section 4.2 notes that "PPO with LSTM often also fails to learn how to solve even the smaller problems" without investigating why. This is the paper's one case of a representation that is expressive (in principle, LSTMs can approximate finite-state machines) but empirically non-discoverable. Given that the discoverability framing is central to the paper's argument, some analysis of the LSTM failure — optimization instability, overfitting to small grids, credit assignment, or sensitivity to hidden state size — would meaningfully strengthen the framework.

- **FunSearch proof-of-concept is thin.** Section 5 reports that "three runs of FUNSEARCH returned a correct implementation of BFS" on a single wall-sparse maze variant. The paper reports no failure rate, number of total FUNSEARCH runs attempted, or comparison of neural performance on this exact task. The point that a correct BFS provably generalizes is logically true, but the synthesis process itself is not characterized. As written this is a proof-of-concept that the approach is possible, not a demonstration that it is reliable or general.

### Trivial
None — formatting issues throughout are parser artifacts from PDF extraction.

---

## Nice-to-Haves

- A control experiment for TORCS: does NDPS with β=0.5 still generalize, or does the reduced speed incentive actually hurt NDPS? If NDPS generalizes equally well under both reward functions, it would sharpen the claim that the reward change addressed a discoverability confound specific to neural optimization.

- For Parking: a systematic search for modifications (sparse observations, last-action augmentation, different reward structure) that might close the DQN–PSM gap, or a more explicit statement that no modification worked, would be informative. The current presentation leaves this question open without acknowledgment.

- The FunSearch proof-of-concept would be significantly more convincing with a report on total runs, failure rate, and a brief characterization of what non-BFS programs were synthesized, to distinguish whether FUNSEARCH reliably discovers BFS or merely happened to do so three times.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "Karel fix changes the task from full to partial observability."** The critic states "the 'fix' involves switching from the fully observable setting (where LEAPS and ConvNet baselines use the full grid)." This is factually incorrect about LEAPS. LEAPS's domain-specific language (Figure 2a) uses local perception functions (frontIsClear, leftIsClear, rightIsClear, markersPresent) — it operates in the *same* partially observable setting as "PPO with a_{t-1}." The ConvNet baseline (PPO with ConvNet) is the one that uses the full grid. The paper's comparison is fair: it aligns the neural baseline's observability with LEAPS rather than the poorly designed ConvNet baseline. **Removed as factually incorrect criticism.**

- **Harsh critic: "The β change changes the problem, not just training."** The critic argues that "β changes the objective the agent optimizes during training, which determines which policies are found," and disputes the paper's claim that "we are not changing the problem, but only how the agent learns." The paper explicitly and correctly notes (Section 4.1) that β is an *intrinsic* reward used only during training while evaluation is performed on the actual problem metrics (lap time, crash). The critic conflates intrinsic training reward with problem definition. **Removed as contradicted by the paper's explicit clarification.**

- **Strength finder: "DQN achieves a higher average test success rate (0.18 vs. 0.16), indicating the generalization advantage is not unilaterally in favor of programmatic policies."** While numerically true, this framing ignores the generalization gap analysis (0.10 vs. 0.68) and the Successful-on-100 metric (2/30 vs. 0/15). The strength overstates what is a nuanced and contested finding in favor of the authors. **Removed as potentially misleading.**

---

## Novel Insights

The most genuinely novel observation in the paper is not the main thesis (training confounds explain the gap) but the theoretical argument in Section 5 about *constant-capacity expressivity*: the reason pathfinding and nested-subproblem benchmarks are hard for neural policies is not optimization failure but representational impossibility, because even just indexing vertices requires Ω(log|V|) bits of growing memory. This reframes the programmatic-vs-neural question from a discoverability problem (which is domain-specific and hard to control) to an expressivity problem (which is characterizable in terms of computational complexity). The connection to NetHack nested subproblems as a practical benchmark that falls into this category is a useful, underexplored direction that the field should pursue.

---

## Suggestions

1. **Recalibrate the abstract and conclusion** to accurately reflect that Parking is a case where PSM does generalize better by generalization-gap metrics. Either add a control that closes the gap, or reframe Parking explicitly as a case where the confound explanation is *insufficient* and working-memory analysis is needed.

2. **Report TORCS results using "fraction of all trained seeds that generalize"** (i.e., 13/30 = 43% for G-TRACK-1, not 76% of successful models) alongside the current presentation, to enable fair comparison with NDPS's 3/3.

3. **Add at least a brief empirical or theoretical analysis of why LSTM fails** on small Karel problems. Even a one-paragraph discussion or a simple ablation (hidden state size, number of layers, gradient clipping) would significantly strengthen the discoverability framing.

4. **Expand the FunSearch experiment** by reporting total runs, failure rate, and what non-BFS programs were generated, to characterize the synthesis process's reliability rather than just its possibility.

---

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Foundation Policies with Memory | It4KL6XnPq.md | 3.00 | R1 | Weaker: incremental memory integration with limited insight |
| Non-Parameterized Randomization | fvTaoyH96Z.md | 2.33 | R1 | Weaker: thin theoretical justification, narrow contribution |
| Bad Habits (policy confounding) | ehSQZa4vuk.md | 5.25 | R1/R2 | Similar: also identifies confounds in RL, slightly less concrete experiments, better theoretical formalism |
| Extensive Analysis on DRL premises | R6klub5OXr.md | 5.25 | R1 | Similar: re-evaluation paper, but overclaims about distributional RL; weaker |
| State Combinatorial Generalization | PH7ja3T0vN.md | 4.50 | R1 | Weaker: no principled framework |
| On Generalization in MORL | tuEP424UQ5.md | 5.75 | R2 | Comparable: also formalizes generalization in RL, similar scope, accepted; similar issues with headline claims vs. empirical support |
| CodeIt: Abstract Reasoning | JlSyXwCEIQ.md | 5.75 | R2 | Comparable: program synthesis applied to challenging benchmark, has novelty and soundness concerns, rejected |
| How Level Sampling Impacts ZSG | X1p0eNzTGH.md | 5.67 | R2 | Slightly weaker: empirical analysis of one training factor, less principled framework |
| Data Scaling Laws in Imitation Learning | pISLZG7ktL.md | 8.00 | R1 | Much stronger: comprehensive, clean experiments with clear takeaways |
| Interpreting Emergent Planning | DzGe40glxs.md | 8.00 | R1 | Much stronger: novel mechanistic evidence with rigorous methodology |

**Round 1 bracket: 5.0–6.5.** Paper is clearly above weak anchors (~3.0) and well below strong anchors (~8.0).

**Round 2 narrowing:** The most comparable papers are "Bad Habits" (5.25, Reject) and "On Generalization in MORL" (5.75, Accept) / "CodeIt" (5.75, Reject). The paper under review has a cleaner Karel result than "Bad Habits" and a more directly testable conceptual framework, arguing for placement above 5.25. But the Parking contradiction with the headline claim and the asymmetric TORCS sampling are real weaknesses that prevent it from being a clean accept at 5.75+. The paper sits between these anchors, closer to 5.5.

**Final score: 5.5 | Reject**

The paper contains a genuinely strong finding (Karel) and a useful conceptual contribution (expressivity/discoverability), but the main thesis as stated in the abstract and conclusion is overclaimed relative to the Parking evidence. These issues require revision to either close the Parking gap or recalibrate the claims to reflect what the evidence actually shows.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>