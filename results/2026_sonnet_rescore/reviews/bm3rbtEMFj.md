## Summary

ELMUR is a transformer architecture augmented with structured layer-local external memory, where each layer maintains its own set of M memory embeddings, reads from them via cross-attention (`mem2tok`), writes to them via a symmetric path (`tok2mem`), and manages slot replacement/blending through a Least Recently Used (LRU) policy with a tunable convex blending factor λ. The model uses segment-level recurrence with detached memory between segments and temporally-grounded relative biases for token–memory attention. It is evaluated on synthetic T-Maze retention, the MIKASA-Robo robotic manipulation suite, and the POPGym benchmark of 48 partially observable tasks, showing substantial gains on memory-intensive settings.

---

## Strengths

- **T-Maze 100% success at one million steps (Figure 3):** Training on L=10-context, S=3-segment inputs and evaluating on corridors up to 10^6 steps, ELMUR uniquely maintains 100% success while every tested baseline degrades substantially. No other compared method comes close across the 10^1–10^6 extrapolation range, and Figure 4 further confirms that this generalizes cleanly across all train/test length combinations up to 9600 steps.

- **POPGym puzzle-task improvements on an independent benchmark (Table 2):** On the 33-task memory-intensive puzzle subset, ELMUR scores 1.2 vs. 0.45 for RATE, while DT and BC-LSTM score below zero. This is a genuine, independently-validated gap. The aggregate score across all 48 tasks is 10.4 vs. 9.5 for the next-best method (RATE), driven primarily by these puzzle gains.

- **Thorough ablation study isolating key components (Table 3, Figure 6):** The ablation on RememberColor3-v0 cleanly demonstrates the importance of LRU (removal drops performance from 1.00 ± 0.00 to 0.43 ± 0.22), layer-local memory (shared memory drops to 0.45 ± 0.03), and relative bias. Figure 6 additionally quantifies the M vs. N capacity dependency across blending factor, initialization scale, and segment configuration.

- **Sequence-length generalization (Figure 4):** The heatmap demonstrates perfect 100% success transfer across all 77 (train, validation) length combinations between 9 and 9600 steps, covering both interpolation and extrapolation regimes.

- **Computational efficiency without accuracy penalty:** At 2.1M parameters and 6.8 ± 0.5 ms/step, ELMUR is faster per step than both RATE (7.2 ± 0.3 ms) and DT (10.7 ± 0.1 ms) despite adding a full memory track (Section 5.2, RQ4). Replacing MoE with MLP preserves accuracy (Table 3, MoE→MLP: 1.00 ± 0.00), confirming that the base design is not dependent on MoE for quality.

- **No degradation on fully observable MDPs:** ELMUR achieves 500 ± 0 on CartPole-v1 alongside all baselines, confirming the memory mechanisms do not harm MDP performance.

---

## Weaknesses

### Fatal
None.

### Major

- **In-group evaluation for the headline MIKASA-Robo result.** The MIKASA-Robo benchmark (Cherepanov et al., 2026a) and the primary transformer comparison baseline RATE (Cherepanov et al., 2026c) both originate from the same research group as the ELMUR authors. The paper's largest claimed gain—"70% improvement over the previous best baseline" and "21 out of 23 tasks"—rest entirely on this benchmark-baseline pair, and the paper does not acknowledge or discuss this evaluation design risk anywhere in the text. The strongest result in Table 1, TakeItBack-v0 (ELMUR: 0.78 ± 0.03 vs. RATE: 0.42 ± 0.24), is notable not only for the gap but also for RATE's extremely high variance (±0.24 on a [0,1] scale), which suggests RATE is not reliably converging on this task—i.e., the comparison may be against a method with known training instability on this specific task rather than against a strong converged baseline. The paper does not discuss RATE's instability on TakeItBack-v0. Since POPGym provides an independent validation, the MIKASA-Robo claims should either be framed with this caveat or the authors should explicitly address the independence concern.

- **Unexplained mechanistic gap for the T-Maze result.** ELMUR uses stop-gradient between segments (`sg(m^{i-1})`, explicitly stated in Section 3), meaning no gradient flows through the memory recurrence—the model can only learn to write something in segment i that benefits segment i+1, not segment i+N. With M=3 slots, L=10, and corridors of 10^6 steps, the LRU policy must overwrite all three slots thousands of times over. Yet the cue written at step 1 survives to inform the decision at step 10^6. The paper provides no explanation of how the model accomplishes this. Possible mechanisms include the model learning to periodically re-write cue content back to itself from its own memory readout (rehearsal), or distributing cue information across slots via blending such that no single overwrite destroys it. Neither is discussed. Given that the T-Maze result is the paper's most striking empirical claim, the absence of a mechanistic account—especially given the theoretical analysis's assumption that each slot is updated uniformly once per M segments—is a substantive gap. The result is impressive but currently uninterpretable.

### Minor

- **MIKASA-Robo subset selection criterion not stated.** The main paper shows results on 23 of the 32 MIKASA-Robo tasks (Table 1 note: "See results for all 32 MIKASA-Robo tasks in Appendix, Table 8"), but the criterion for selecting these 23 tasks for the main text is not stated. The abstract's "21 out of 23 tasks" claim rests on this unnamed subset.

- **POPGym abstract framing overstates the aggregate story.** On reactive tasks (15/48 tasks), ELMUR (9.2) is functionally tied with RATE (9.1), DT (9.3), and BC-LSTM (9.1) — Table 2 makes this clear. The genuine contribution is on the puzzle subset. The abstract statement "outperforms baselines on more than half of the tasks" is technically accurate but obscures the fact that the improvement is concentrated in one task regime. RQ4 in the paper does discuss puzzle vs. reactive separately, which is appropriate, but the abstract should reflect this more precisely.

- **M ≥ N hyperparameter dependency is unresolved.** Figure 6 and the ablation section correctly identify that performance is highly sensitive when M < N (where N is the number of segments needed to solve a task). However, N is not generally knowable in advance on new tasks, and the paper provides no heuristic or guidance for setting M in unseen settings. This is acknowledged but left open.

### Trivial

- **Proposition 1 and Proposition 2 are elementary observations.** Proposition 1 is a direct expansion of a geometric series; Proposition 2 is a one-line convex combination argument. Both are correct and useful for formal presentation, but labeling them as propositions slightly overstates their technical contribution. Reframing as "Observations" would be more appropriate and more honest.

---

## Nice-to-Haves

- **Visualize memory slot write patterns on T-Maze.** Showing which slots are written at which time steps (e.g., whether slot 0 is refreshed periodically, whether cue information is blended across multiple slots) would transform the T-Maze result from "impressive but opaque" to "impressive and mechanistically understood." Even a single visualization for a corridor of 1000 steps would substantially strengthen the paper's core claim.

- **Stress-test LRU with competing cues.** T-Maze measures single-item retention under maximally sparse context. Constructing a condition where two or more important cues must both survive in M≤2×(number of cues) slots would directly probe whether the LRU policy makes intelligent eviction decisions, rather than simply whether any persistent-slot system can survive a sparse corridor.

- **Report inference time for MLP ablation.** Table 3 shows MoE→MLP preserves accuracy, and the paper claims MoE contributes to efficiency (Section 5.2, RQ4). Reporting the MLP variant's inference time would quantify this claim and clarify whether MoE is earning its architectural complexity.

- **Frame POPGym contribution as puzzle-specific.** Separating the abstract claim into puzzle (where ELMUR clearly leads) and reactive (where all methods are equivalent) would make the paper's contribution sharper and more defensible to readers familiar with the benchmark.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"RMT missing from Tables 1 and 2."** RMT appears in Figure 3 (T-Maze comparison). The paper's Section 5.1 defines the comparison set clearly and notes why certain baselines are excluded (online RL, real-robot). RMT's absence from MIKASA-Robo and POPGym tables is not explained, but per the hard rules, missing baselines are not penalized when the excluded method is not directly cited as a required comparison. REMOVED per the rule against missing-related-works and unfair-comparison-criticism.

- **"Propositions inflate significance — they are trivial."** This is retained as a Trivial weakness (reframing suggestion), not removed entirely, but it does not weigh on the accept/reject decision.

- **"The 21/23 MIKASA-Robo claim depends on a stripped appendix."** Per hard rules, appendices are assumed to exist. The main paper explicitly points to Appendix Table 8. REMOVED as a fatal/major concern; retained as Minor only for the subset-selection question.

- **"The effective horizon formula assumes uniform LRU updates."** The critic speculates this may not hold if the model learns to preferentially refresh important slots. This is a speculative-fatal claim that depends on unverified assumptions about learned behavior. DEMOTED to informing the "unexplained mechanism" Major weakness rather than standing as an independent fatal flaw.

- **Strength: "MIKASA-Robo nearly doubles baseline performance."** This strength conflicts with the Major weakness about in-group evaluation. Per the hard rule, when a strength and weakness disagree, the weakness wins. The raw numbers in Table 1 are real but the in-group context limits how strongly this can be claimed as independent evidence. DEMOTED from strength.

---

## Novel Insights

The most conceptually interesting observation emerging from the synthesis is the tension between the stop-gradient architecture and the 10^6-step T-Maze result: ELMUR provably cannot learn cross-segment credit assignment through backpropagation, yet it achieves perfect retention across 10^5 gradient-free memory rewrites. This implies that either the blending dynamics alone create a sufficiently stable attractor for the cue (small-λ regime creating near-perfect retention even under overwrite pressure), or the model learns an emergent rehearsal behavior—periodically re-reading and re-writing important memory content to refresh its LRU anchor—that is invisible in the current experimental analysis. Understanding which mechanism operates, and whether it generalizes beyond single-cue retention, would constitute a meaningful scientific finding beyond this paper's current claims.

---

## Suggestions

1. Add a mechanistic analysis of T-Maze slot dynamics: log which slot is written per segment and what content it carries, to determine whether retention is achieved by small-λ stability, slot refreshing/rehearsal, or content distribution across slots.

2. State explicitly in the main text that MIKASA-Robo and the primary baseline RATE share a research group with the authors, and discuss why results should nevertheless be considered reliable (e.g., open benchmark, shared code, other independent results corroborate the pattern).

3. Clarify the 23/32 MIKASA-Robo subset selection: state the inclusion criterion in the main text.

4. Revise the abstract to distinguish puzzle-subset gains (where ELMUR has a clear, specific advantage) from aggregate aggregate POPGym performance (where reactive tasks flatten the delta).

5. For the M < N ablation: provide a practical heuristic for estimating N on new tasks, even a rough one (e.g., estimate horizon length / segment length as an upper bound on N).

---

## Evaluation on Key Axes

**Originality:** Moderate. The individual components—segment recurrence (Transformer-XL, RMT), external memory with cross-attention (Memformer, NTM), LRU policy—are established. The specific combination of layer-local memory with bidirectional cross-attention, LRU management, and IL training for POMDP control is novel and sensibly engineered. Not a conceptual breakthrough, but a well-motivated synthesis.

**Importance:** High. Long-horizon partially observable decision-making is a fundamental challenge in robotics and RL, and ELMUR addresses it with a method that scales without quadratic cost and generalizes across modalities.

**Claims supported:** Partially. The T-Maze and POPGym puzzle claims are well-supported by independent evidence. The MIKASA-Robo "70% improvement" headline claim is supported by numbers but weakened by the in-group evaluation concern. The mechanistic story behind the T-Maze extrapolation is absent.

**Soundness:** Moderate-high. The architecture is clean and well-specified. The theoretical analysis is elementary but correct. The ablations are thorough. The in-group evaluation and unexplained T-Maze mechanism are the main soundness concerns.

**Clarity:** High. Algorithm 1, Figure 2, and the method section are precise and reproducible. The experiment section is well-organized and the RQ structure helps readability.

**Community value:** High. Broad evaluation across three benchmarks, code released, addresses a real problem with a deployable method. The POPGym and T-Maze results in particular provide usable reference points for future work.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>