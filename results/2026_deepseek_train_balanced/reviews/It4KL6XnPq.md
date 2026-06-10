## Summary

This paper integrates memory models (GRU, S4, Transformer) into Foundation Policies (FPs) to enable generalization to both unseen tasks and unseen environment dynamics — a capability neither approach achieves alone. The method feeds trajectory histories through a memory model and conditions the FP's actor and critic on the resulting hidden state. Evaluated on POPGym and ExORL benchmarks, the central finding is that FB-GRU approximately matches the aggregate test performance of a supervised single-task baseline (TD3-GRU) on zero-shot dynamics generalization, despite being trained without reward supervision.

## Strengths

1. **FB-GRU matches a supervised baseline on zero-shot dynamics generalization (Section 4.3, line 121):** Aggregate test performance of FB-GRU "approximately matches TD3-GRU aggregate test performance despite not seeing rewards during training." This is the paper's strongest result — the method simultaneously generalizes to unseen tasks AND unseen dynamics (both interpolation at 1.0× and extrapolation at 2.0×) without reward supervision, approaching a single-task supervised method that has full reward access.

2. **FB-S4 and FB-GRU match TD3-GRU on POPGym state inference (Section 4.2, line 111):** Frame-stacking FB reaches only 30% of TD3-GRU's aggregate score, while FB-S4 and FB-GRU match TD3-GRU's performance. This cleanly demonstrates that the memory-model integration solves the partial observability problem that naive frame-stacking cannot.

3. **Controlled experimental design isolating three distinct capabilities (Sections 4.2–4.4):** The paper separates state inference (Q1), dynamics+task generalization (Q2), and environment generalization (Q3). Each experiment targets a specific capability, making the empirical picture interpretable rather than a single black-box result.

4. **Practical architectural insight — separate actor/critic memory models (Section 3.2, line 81):** The paper reports that a shared memory model led to model collapse, so separate models are used. This corroborates [73] and is a concrete design decision practitioners can adopt directly.

5. **Honest treatment of limitations (Sections 4.4, 5):** The paper transparently reports that Q3 absolute returns are low (max of 33/1000), discusses the context-length limitation (L=64 vs. episodes of 200–1000 timesteps), and acknowledges uncertainty about whether dynamics can be inferred from such short windows.

## Weaknesses

### Major

1. **Memory model comparison confounded by controlling for hidden-state size rather than parameter count (Section 4.1, line 104).** The paper follows [68] and fixes hidden state size to 1024 dimensions for all models. A GRU with 1024 hidden dimensions has substantially fewer parameters than a Transformer or S4 of the same hidden dimension. The paper's conclusion that "GRUs achieve the best generalization" may be partly an artifact of capacity differences rather than architectural superiority. The paper acknowledges the choice and provides a functional justification, but includes no parameter-controlled ablation. Without this, the reader cannot determine whether the GRU's advantage stems from its architecture or from being a differently-sized model that happens to generalize better with fewer parameters.

2. **Abstract overclaims on environment generalization relative to the evidence (Abstract, line 4; Section 4.4).** The abstract states "our approach improves FP performance on entirely new environments not encountered during training." While technically true (FB-S4 improves ~4× over FB), the absolute returns top out at 33 out of 1000 — the paper itself says "there is significant room for improvement." Moreover, FB-GRU (the best method on the paper's primary Q2 experiment) performs *worst* on Q3 among the memory-augmented methods, which the paper reports but does not explain. The conclusion (Section 7) wisely omits this claim entirely. The abstract should be recalibrated to distinguish the (well-supported) dynamics generalization result from the (weak) environment generalization result.

3. **Missing hyperparameter and training-detail documentation.** The paper does not state how hyperparameters were selected, whether they were tuned separately per memory model, or whether the same values were used across all FB-based methods. For an empirical RL paper whose central comparison is across three different memory architectures, this is a noticeable gap.

### Minor

1. **Failure of all memory models on RepeatPreviousHard (Section 4.2, line 111).** The paper honestly reports that all methods fail on a benchmark designed to test long-range memory recall, where other in-context RL agents succeed. The attributed cause — "memory models are not accurately recalling information from the start of their context" — cuts against the paper's assumption that memory models can effectively encode trajectory-level dynamics information. The paper flags this but does not discuss its implications for the broader approach. This is not fatal (the strong Q2 results provide empirical counter-evidence that the models are doing something useful for dynamics generalization), but it deserves more than a single sentence.

2. **No ablation of context length L.** The paper's own Limitations section (Section 5) identifies L=64 as a significant constraint and raises the possibility that this window may be insufficient to infer the dynamics context. An ablation over L ∈ {16, 32, 64} would directly address the paper's most serious acknowledged uncertainty. This is particularly important because the POPGym experiments use re-conditioning (which the paper describes as disentangling state inference from hidden-state propagation), while the ExORL experiments do not, so the same memory models operate under different conditions across experiments.

### Trivial

None.

## Nice-to-Haves

- **Add a probing analysis of the memory hidden state.** The paper claims the memory model "infers the dynamics context" from trajectories but provides no direct evidence. A linear probe to predict dynamics parameters (mass, damping) from the hidden state would directly validate the claimed mechanism.
- **Add a parameter-count ablation for the memory model comparison.** Even a single data point (a GRU with hidden size matched to give comparable parameter count to the S4 variant) would resolve the confound.
- **Report per-environment breakdown in text.** The aggregate IQM figures are helpful, but per-environment results for the ExORL experiments would help readers understand where the method works and where it struggles.

## Removed Points

These points were flagged by reviewers but are removed or demoted after cross-checking against the paper:

- **Critic's claim that Q3 results "undermine the paper's headline claims" and are "internally inconsistent."** The paper's primary claim (from both abstract and conclusion) is about dynamics generalization (Q2), which is well-supported. Q3 is presented as an additional finding, and the paper is honest about its weakness. The characterization as a fatal contradiction is overblown. Merged into the abstract-overclaiming point (Major weakness 2).
- **Critic's claim that RepeatPreviousHard is "a direct challenge to the paper's core assumption."** The strong Q2 results provide direct empirical evidence that the memory models are effective for dynamics generalization despite this failure. The paper already flags the limitation. Demoted from proposed fatal/major to Minor.
- **Critic's claim about POPGym re-conditioning design — "the paper should be more explicit about this difference."** The paper already explicitly describes the re-conditioning setup and its purpose (line 92). This is a reading issue, not a paper flaw. Removed.
- **Strength Finder item 3 ("systematic comparison rules out alternatives")** — Caveated in the strength text with the confound issue. Not removed, but the reader should interpret it in light of Major weakness 1.

## Novel Insights

None beyond the paper's own contributions. The key empirical finding — that GRU-augmented FPs match a supervised single-task baseline on zero-shot dynamics generalization — is the paper's own novel result.

## Suggestions

1. Recalibrate the abstract to separate the strong dynamics generalization claim (Q2) from the weak environment generalization claim (Q3), or remove the Q3 claim from the abstract entirely.
2. Add a parameter-count ablation for the memory model comparison (e.g., a GRU with matched parameter count to the S4 variant).
3. Add a context-length ablation (L ∈ {16, 32, 64}) to directly address the paper's own most serious acknowledged limitation.
4. Include a probing experiment to verify that the hidden state actually encodes dynamics parameters.
5. Document hyperparameter selection methodology.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>