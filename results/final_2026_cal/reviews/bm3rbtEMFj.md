Now I have all the information needed to write a thorough, calibrated review.

---

## Summary

ELMUR augments each transformer layer with a dedicated external memory track, using bidirectional cross-attention for reading/writing and an LRU-based update policy that fills empty slots and then blends new content into the least recently used slot. The method is clean, well-motivated, and tested on three benchmarks: T-Maze (synthetic retention), MIKASA-Robo (robot manipulation with visual observations), and POPGym (48 diverse puzzle/control tasks). The headline result — 100% success on T-Maze corridors up to one million steps using only a 10-token context window — is striking and clean. The paper also provides formal bounds on forgetting (exponential decay under convex blending), half-life, and effective retention horizon, connecting hyperparameters M, λ, and L to retention behavior.

## Strengths

- **Extreme retention on T-Maze (Figure 3):** ELMUR achieves 100% success on corridors up to 10⁶ steps with L=10 context, S=3 segments. This is 100,000× the attention window and far beyond what any baseline achieves (next best ≈ 70% at 10⁶ steps). The result is clean, reproducible from the main-text description, and directly supports the paper's central claim.

- **Dominant performance on robotic manipulation (Table 1):** On the 4 MIKASA-Robo tasks shown, ELMUR beats all baselines by large margins — e.g., 0.78 vs. 0.42 (RATE) on TakeItBack-v0 and 0.89 vs. 0.65 (RATE) on RememberColor3-v0. The strong performance under visual observations and sparse rewards is the paper's most practically significant result.

- **Formal theoretical analysis (Section 4):** Proposition 1 derives exponential forgetting under repeated LRU overwrites; the Corollary gives a simple half-life formula; the effective horizon H(ε) = M·L·ln(ε)/ln(1−λ) connects design choices directly to retention. Proposition 2 proves memory norm-boundedness under convex updates. These are not deep theorems, but they are correct, clearly stated, and give practitioners quantitative guidance — more than most memory-augmented transformer papers provide.

- **Well-designed ablation study (Figure 6, Table 3):** The ablations on RememberColor3-v0 cleanly isolate the contributions of per-layer vs. shared memory, LRU, relative bias, memory capacity M, blending factor λ, and initialization σ. Component removal drops success from 1.0 to 0.22–0.45, confirming that each design element matters. Figure 6's systematic variation of λ, σ, M, and segmentation is thorough and informative.

- **Computational efficiency:** ELMUR has 2.1M parameters and runs at 6.8±0.5 ms/step — faster than RATE (7.2 ms) and DT (10.7 ms) on T-Maze — despite its more complex architecture. The paper correctly attributes this to short attention windows and MoE feed-forward layers, making the explicit-memory approach practically appealing.

## Weaknesses

### Major
None.

### Minor
- **MIKASA-Robo headline claim not fully verifiable from main text.** The abstract claims ELMUR is "best on 21 of 23 tasks" and shows "~70% aggregate improvement," but Table 1 only reports 4 tasks. The supporting data is in the appendix (Table 8). The main text should include a summary statistic (e.g., aggregate success rate ± SEM or a per-task bar chart) to substantiate these claims without requiring the appendix. The inconsistency between "23 tasks" (abstract) and "32 tasks" (Table 1 caption) is also confusing and should be corrected.

- **T-Maze hyperparameters M and λ not reported in the main text.** The paper's flagship result depends on memory capacity M and blending factor λ, yet neither value appears in the main body (the appendix, Table 7, is the intended location). Given the centrality of this experiment, including M and λ in the main text would substantially improve self-containedness and reader confidence.

- **Aggregate POPGym scores reported without confidence intervals (Table 2).** The improvement over RATE (10.4 vs. 9.5) is modest, and without standard errors or confidence bounds it is unclear whether this difference is statistically significant. The per-task results are reported with error bars in Figure 5, but the aggregate table should include SEM or a similar uncertainty measure.

- **The effective horizon formula H(ε) is not empirically validated.** The theoretical analysis derives H(ε) = M·L·ln(ε)/ln(1−λ), which predicts retention given M, L, λ. A simple validation — e.g., "with M=X, λ=Y, L=Z, predicted half-life is W, and observed retention at W steps is Q%" — would tie theory to experiment but is absent.

### Trivial
- The "100,000×" framing in the abstract (ratio of total steps to context length) could be misinterpreted as a measure of memory horizon rather than a comparison between total trajectory length and context size. The paper clarifies this claim in context, but the phrasing may confuse readers.
- Minor inconsistency: abstract says "23 MIKASA-Robo tasks" while Table 1 caption says "32 tasks" — this should be reconciled.

## Nice-to-Haves
- A validation of the theoretical horizon formula against empirical retention (e.g., a plot of predicted vs. observed success rate for varying λ or M).
- Comparison with other explicit-memory architectures such as Memformer or Memory Transformer, which are mentioned in related work but not evaluated.

## Removed Points

- *"The T-Maze 100% success result is likely impossible under the stated LRU update rule with bounded memory because…"* — **REMOVED: misunderstands the mechanism.** With small λ (e.g., λ → 0), the convex blend equation m'_j = λ·ũ + (1−λ)·m_j reduces to m'_j ≈ m_j, meaning the memory content is preserved nearly unchanged after the initial fill phase. The paper explicitly says λ is a tunable hyperparameter balancing plasticity and stability (Section 3, Algorithm 2). The LRU selects one slot per segment; non-selected slots are untouched. Furthermore, the ablation's M≥N finding (Figure 6) applies to RememberColor3, a task with qualitatively different memory requirements than T-Maze, where only a single bit of info (the cue) needs retention. The critic's extrapolation from M≥N to a requirement of M ≥ 100,000 for T-Maze is unsupported.

- *"Theoretical analysis is not a significant contribution"* — **REMOVED: correctly labeled as analysis, not a claimed contribution.** The paper describes it as "theoretical analysis" (Section 4), not as a primary contribution. The bounds are useful for connecting hyperparameters to retention behavior, which is more than most comparable papers provide.

- *"Missing comparison to Memformer / Memory Transformer"* — **REMOVED: the baseline zoo already includes RATE, DT, DMamba, CQL, DP, BC-MLP, BC-LSTM, TrXL, RMT.** The paper covers the major relevant baselines. Adding every memory architecture is scope creep.

- *"The 100,000× framing is dramatic but not directly meaningful"* — **REMOVED: the paper defines this as total trajectory length / context window length, which is a clear, factual ratio.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Report M and λ for the T-Maze experiment directly in the main text (near Figure 3).
2. Add a summary statistic (aggregate success rate across all MIKASA-Robo tasks ± SEM) to Table 1, or include a small bar chart in the main body, so the "21 of 23" / "~70% improvement" claims are verifiable without the appendix.
3. Add standard errors to the aggregate POPGym scores in Table 2.
4. Include a simple empirical check of the theoretical horizon formula, e.g., a short table or paragraph comparing predicted vs. observed retention for a few (M, λ, L) configurations.
5. Reconcile the "23 tasks" vs. "32 tasks" inconsistency in MIKASA-Robo.

---

## Score and Decision

**Calibration report:**

*Round 1 (bracketing)* — Three queries on "transformer external memory layer long-horizon RL":

| Anchor | Avg Score | Round | Comparison to ELMUR |
|--------|-----------|-------|---------------------|
| oIjxs733Kp | 3.33 | R1 | In-context RL in transformers, different focus; ELMUR clearly stronger |
| dtQxzXILzW | 1.67 | R1 | Reward-driven exploration; not comparable |
| ws9ZjMthvi | 3.33 | R1 | Memory-use quantification metric; ELMUR has stronger empirical results |
| jus1arazi7 | 3.00 | R1 | Continual RL with world models; less directly comparable |
| **kByN4v0M3e (RATE)** | **4.50** | **R1** | **Most directly comparable baseline paper; ELMUR has clearer architecture, more extreme retention, cleaner ablations, and formal analysis — ELMUR is stronger** |
| rb5eTktqbc | 5.00 | R1 | Transformer-based SAC critic; different contribution, comparable quality |
| Iskm1kYo70 | 4.50 | R1 | Elastic Memory for long-context language; different domain, comparable quality |
| OiwMgMjeRz | 5.00 | R1 | Multi-agent memory; less relevant |
| oBXfPyi47m | 8.00 | R1 | World model RL with offline data; different subarea, higher tier |
| kkBOIsrCXh | 8.00 | R1 | Embodied navigation; not comparable |
| qOyF214xmg | 8.00 | R1 | Language model transduction; not comparable |
| VKGTGGcwl6 | 8.00 | R1 | Multi-turn LLM evaluation; not comparable |

*Round 1 bracket:* The most relevant anchors (RATE at 4.5, Chunking the Critic at 5.0, Elastic Memory at 4.5, Hippoformer at 5.0) suggest ELMUR sits in the **5.0–6.5** range. It is clearly stronger than RATE (4.5) and at least as strong as the 5.0 anchors.

*Round 2 (narrowing):*

| Anchor | Avg Score | Round | Comparison to ELMUR |
|--------|-----------|-------|---------------------|
| rb5eTktqbc | 5.00 | R2 | Already examined; ELMUR has more extreme empirical claim |
| OiwMgMjeRz | 5.00 | R2 | Multi-agent memory; different scope |
| VSNmchfjgB | 5.00 | R2 | LLM agent policy gradients; not comparable |
| hxwV5EubAw (Hippoformer) | 5.00 | R2 | Spatial memory; had substantial methodological critiques (confounded baselines, missing citations) that ELMUR does not share |
| QWuXU0qNX0 (UltraMemV2) | 6.50 | R2 | Memory networks at 120B scale for language; different domain, but represents strong work in memory architectures |
| eZ5jtFuk3e | 5.60 | R2 | Meta-tokens for language modeling; different domain |
| vI56m4Iu4e (MemGen) | 7.00 | R2 | Generative memory for LLM agents; different domain |
| xa3OnTb6c3 (MesaNet) | 6.50 | R2 | Linear RNNs for sequence modeling; different domain |

*Final score:* ELMUR is consistently stronger than the most comparable anchor paper (RATE, 4.5), comparable to or stronger than the mid-range anchors (5.0–5.6), and its evaluation breadth (T-Maze + MIKASA-Robo + POPGym) plus formal analysis lift it above the typical 5.0. The main weaknesses are presentation issues (appendix-dependent claims, missing main-text hyperparameters), not fundamental flaws. **Score: 6.0.**

<score>6.0</score>
<decision>Accept</decision>