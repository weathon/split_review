Now I have a thorough understanding of the paper and the reviews. Let me produce the final consolidated review.

## Summary

This paper re-evaluates three influential benchmarks (TORCS, Karel, Parking) where programmatic policies were reported to generalize better than neural policies. The authors show that simple modifications—a cautious reward function in TORCS and last-action-augmented partial observability in Karel—allow neural policies to match or exceed the OOD generalization of programmatic policies. They introduce an expressivity/discoverability framework to separate whether a policy class can represent a generalizing solution from whether the search algorithm can find it. They then identify tasks requiring instance-scaling working memory (e.g., general pathfinding) as cases where fixed-capacity neural architectures fail expressivity, and provide a proof-of-concept using FUNSEARCH to synthesize a BFS program.

## Strengths

1. **Controlled reward-function change in TORCS eliminates the reported gap.** Table 1 shows that DRL with β=0.5 (cautious reward) generalizes to OOD tracks (76% of seeds from G-TRACK-1 to G-TRACK-2, 69% to E-ROAD), while β=1.0 crashes on all OOD tracks. NDPS generalizes under the original protocol. This controlled comparison—changing only the intrinsic reward weight—provides direct evidence that the prior gap was driven by speed over-optimization, not representation.

2. **Simple feedforward network with last-action augmentation matches programmatic generalization in Karel.** Table 2 reports that "PPO with a_{t-1}" achieves perfect generalization (return 1.00 on 100×100 grids) on four of five Karel tasks, while prior work showed LEAPS generalizing but standard PPO (ConvNet, LSTM) failing. The paper identifies a specific, plausible confound (full observability creating spurious correlations) and demonstrates that removing it suffices to close the gap.

3. **The expressivity/discoverability framework (Definitions 2 and 3) is a clear conceptual tool.** It isolates two necessary conditions for OOD generalization and explains why prior work's uncontrolled factors (e.g., reward shaping in TORCS, observation design in Karel) produced misleading conclusions—they affected discoverability while both representations satisfied expressivity.

4. **Honest assessment of the Parking domain.** Table 3 shows both PSM and DQN struggle, with DQN achieving higher absolute test success (0.18 vs. 0.16) but PSM having a smaller train-test gap. The paper does not overclaim, instead noting that Parking points toward benchmarks that could distinguish representations. This nuance contrasts with prior work presenting only programmatic successes.

5. **The memory-scaling argument identifies a plausible region where programmatic representations have a genuine advantage.** The theoretical reasoning (Ω(log|V|) bits to index vertices, fixed capacity of feedforward/LSTM architectures) is sound, and the proof-of-concept with FUNSEARCH synthesizing BFS demonstrates feasibility, even if empirical neural baselines are not provided.

## Weaknesses

### Fatal

None.

### Major

1. **Missing control: programmatic policies are not evaluated under the modified conditions.** The paper changes the reward function in TORCS (β=0.5) and observation design in Karel (adding a_{t-1}) and shows neural policies generalize. However, it never tests whether the programmatic policies (NDPS/PROPEL in TORCS, LEAPS in Karel) would also benefit from these same modifications, potentially preserving or changing the gap. The paper's central claim—that the gap arose from uncontrolled experimental factors rather than representation—would be stronger with this control. Without it, the evidence shows that neural policies *can* match programmatic ones under certain conditions, but does not fully isolate representation as the non-factor. The paper acknowledges this implicitly in Section 4.4 ("We conjecture that NDPS and PROPEL would not generalize... if they could find better optimized policies") but does not test this.

2. **The memory-scaling advantage claim lacks a neural failure experiment.** The paper argues theoretically that fixed-capacity neural architectures cannot represent solutions requiring instance-scaling memory (e.g., BFS on arbitrary mazes), then shows FUNSEARCH can synthesize BFS. However, no neural baseline (e.g., PPO-LSTM, feedforward with a_{t-1}, or even a Transformer) is actually trained on the modified wall-sparse Karel maze to demonstrate that it cannot generalize OOD. The proof-of-concept demonstrates programmatic success but not neural failure. The paper frames this as a "proof-of-concept" and the theoretical argument is rigorous, but the empirical side remains incomplete for a claim presented as a firm finding in the abstract and conclusion.

### Minor

1. **Disconnect between the re-evaluated DSLs and the proof-of-concept.** The proof-of-concept uses FUNSEARCH with Python (Turing-complete) to synthesize BFS. The Karel DSL in Figure 2 cannot express BFS (no arrays, no arbitrary recursion, no dynamic memory). The paper's positive demonstration therefore does not apply to the same class of *DSL-based programmatic representations* studied in the re-evaluation. The argument about "programmatic representations in general" is valid, but the narrative arc from the negative results (DSL programs don't help) to the positive results (programs help for memory-scaling tasks) would be stronger if connected through the same or an augmented DSL.

2. **No analysis of why PPO with a_{t-1} fails on Harvester.** Table 2 shows PPO with a_{t-1} achieves 0.04 (100×100) on Harvester—the only task where it fails to generalize. Harvester may require counting or more complex memory (e.g., tracking how many markers have been picked), which would align with the paper's memory-scaling argument. A brief failure analysis would strengthen the paper's narrative and potentially provide a bridge between the re-evaluation and the memory-scaling claim.

3. **Proof-of-concept details are thin.** Three runs of FUNSEARCH returned BFS—no confidence intervals, no discussion of LLM stochasticity, no ablation (e.g., does FUNSEARCH without the LLM find BFS?). The maze structure (Figure 7, presumably in the appendix) is referenced but not described in the main text. These are standard ablations for an LLM-based pipeline.

4. **Statistical comparison in TORCS is asymmetric.** NDPS results are from 3 seeds (original paper); DRL β=0.5 results are from 13/30 seeds that learned the training track. The paper reports the fraction of successful seeds but does not run NDPS with more seeds or provide a direct statistical test comparing the two methods under the new conditions.

### Trivial

None.

## Nice-to-Haves

- Test programmatic policies (NDPS/PROPEL) under the β=0.5 reward in TORCS to complete the control.
- Train a neural baseline (e.g., PPO-LSTM or small Transformer) on the wall-sparse Karel maze and report OOD generalization results.
- Augment the Karel DSL with arrays or recursion to show that the programmatic methods from the re-evaluation (e.g., LEAPS) can be extended to solve memory-scaling tasks.
- Analyze Harvester failure: does it require counting, and would a memory-augmented model help?

## Removed Points

- Criticism that "the re-evaluation does not refute the original claims because conditions changed" — the paper's claim is that the gap *can be explained by confounds*, not that programmatic policies are equivalent under all conditions. The missing control is a genuine weakness (kept as Major #1) but the framing as "not establishing the central negative result" overstates what's required. The paper shows neural can match programmatic when confounds are removed, which is meaningful evidence for its claim even without the full control.

- "Speculative claims about other works (Related Work) are unsupported" — the paper frames these as conjectures ("could be," "may also be attributed to") in a discussion section. Speculating about other works is appropriate for that context.

- "Paper does not show that feedforward/LSTM/Transformer actually fails to solve the modified maze" — this is kept as Major #2 (the claim lacks a neural failure experiment) but the criticism that the paper "cites only older work on LSTMs" is inaccurate; the paper cites Nowak et al. (2023), Delétang et al. (2023), and acknowledges memory-augmented models (stack-RNNs, NTMs, LLMs) can approximate the needed structures.

- Criticisms about missing appendix content (Figure 7, proofs) — these are parser artifacts; the original submission contains them.

- Formatting nitpicks and style complaints — removed per policy.

## Novel Insights

Beyond the paper's own contributions, a cross-reading of the two reviews surfaces an underexplored tension: the paper argues that programmatic representations are useful for memory-scaling tasks, yet the proof-of-concept uses FUNSEARCH (a neuro-symbolic system with an LLM) rather than the DSL-based program synthesis methods (LEAPS, NDPS) that were the subject of the re-evaluation. This suggests that the genuine advantage of "programmatic" representations may lie not in DSLs as studied in prior work, but in richer representations (full programming languages, or neuro-symbolic hybrids with LLMs) that support dynamic data structures. The paper's own framework (expressivity/discoverability) could be used productively to characterize this: the DSLs satisfy expressivity for constant-memory tasks but not for instance-scaling tasks, while Turing-complete programmatic representations satisfy expressivity for both.

## Suggestions

1. **(Critical for revision)** Add a control experiment testing NDPS/PROPEL under β=0.5 in TORCS and, if feasible, LEAPS with last-action augmentation in Karel. This directly addresses whether programmatic representations would also benefit from the modifications and helps isolate the role of representation from optimization.

2. **(Important for revision)** Train a neural baseline (e.g., PPO with LSTM or a small Transformer) on the wall-sparse Karel maze where wall-following fails. Show that it cannot generalize OOD, providing empirical support for the memory-scaling claim. Alternatively, scale down the claim and explicitly acknowledge it as a theoretical argument with a feasibility demonstration.

3. Discuss why Harvester fails for PPO with a_{t-1}—this could be a bridge case that requires more memory, connecting the re-evaluation to the memory-scaling argument.

4. Report confidence intervals or seed-level variation for the FUNSEARCH proof-of-concept, and clarify whether the LLM is essential or random search would suffice.

## Score and Decision

This paper makes a genuine and important contribution by identifying concrete experimental confounds in influential prior work, re-evaluating those claims with careful experiments, and providing a conceptual framework for thinking about OOD generalization in policy classes. The two major weaknesses—the missing control for programmatic policies under modified conditions and the lack of a neural failure experiment for the memory-scaling claim—are real but do not undermine the core contribution of the re-evaluation experiments. The paper is honest about its limitations and the proof-of-concept nature of the positive claim. The expressivity/discoverability framework and the empirical results on TORCS and Karel alone constitute a valuable contribution to the community's understanding of generalization in programmatic RL.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>