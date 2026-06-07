Now I have a complete calibration picture. Let me finalize the review.

**Calibration summary:**

| Anchor | Score | Round | Comparison to ELMUR |
|--------|-------|-------|---------------------|
| RATE (c4w7WVs1z7) | 4.75 | R1 | ELMUR explicitly outperforms this baseline; stronger architecture, better results |
| DT-Mem (FhbZ1PQCaG) | 5.75 | R1/R2 | ELMUR has more architectural novelty, better ablations, broader evaluation |
| LRAM (T1pUS4GZZq) | 5.75 | R2 | Different focus; ELMUR has comparable empirical breadth with more original design |
| LaMo (AY6aM13gGF) | 6.25 | R2 | Different approach (pre-training); ELMUR has more original architecture |
| MELODI (TvGPP8i18S) | 6.25 | R2 | NLP domain; ELMUR comparable in quality but different field |
| Stable Hadamard Memory (We5z3UEnUY) | 6.50 | R1/R2 | Closest comparator. SHM has deeper theory; ELMUR has stronger empirical results (T-Maze 1M, 3 benchmark domains). Comparable overall. |

**Round 1 bracket:** 5.75–7.50  
**Round 2 narrowing:** ELMUR sits at approximately 6.5 — comparable to SHM (6.50), clearly above DT-Mem/LRAM (5.75), and clearly above RATE (4.75).

---

## Summary
ELMUR is a transformer architecture in which each layer maintains an external memory of M slots. Tokens read from and write to memory via bidirectional cross-attention (mem2tok / tok2mem), and memory is managed by an LRU policy: empty slots are filled by full replacement, then the least recently used slot is refreshed via convex blending with parameter λ. The paper evaluates ELMUR on T-Maze (up to 1M steps), 48 POPGym tasks, and the MIKASA-Robo robotic manipulation suite, demonstrating 100% T-Maze success at all corridor lengths and best aggregate performance across benchmarks.

## Strengths
- **Exceptional T-Maze extrapolation (Figure 3):** ELMUR achieves 100% success rate on T-Maze at corridor lengths up to one million steps, using a context window of only L=10 with S=3 segments — a retention factor of 100,000× beyond the native attention window. All baselines (RMT, DT, BC-LSTM, RATE, TrXL, DMamba, BC-MLP) degrade sharply as corridor length increases.
- **Causal ablation evidence (Table 3):** Removing the LRU update mechanism drops success from 1.00 to 0.43 ± 0.22; removing both LRU and relative bias collapses performance to 0.22 ± 0.11; switching from per-layer to shared memory reduces success to 0.45 ± 0.03. These controlled ablations provide strong evidence that LRU-based management and layer-local memory are the primary drivers of performance.
- **Length generalization (Figure 4):** ELMUR trained on short T-Maze sequences (9–300 steps) maintains 100% success when evaluated on sequences up to 9,600 steps, and also generalizes downward to shorter sequences. The uniformly green heatmap demonstrates a length-agnostic memory mechanism.
- **Strong MIKASA-Robo performance (Table 1):** On TakeItBack-v0 ELMUR achieves 0.78 ± 0.03 vs. RATE's 0.42 ± 0.24, and on RememberColor3-v0 it scores 0.89 ± 0.07 vs. RATE's 0.65 ± 0.04 — clear improvements on pixel-input, continuous-action tasks.
- **Cross-domain consistency:** ELMUR achieves the best aggregate score on POPGym (10.4 vs. 9.5 for RATE across 48 tasks), perfect T-Maze performance, and top MIKASA-Robo results, spanning discrete puzzles, continuous control, and visual robotic manipulation.
- **Computational efficiency:** ELMUR (2.1M parameters) runs at 6.8 ± 0.5 ms per step — faster than RATE (7.2 ± 0.3 ms) and DT (10.7 ± 0.1 ms) — by keeping self-attention windows short while handling long-term context through bounded external memory.

## Weaknesses

### Fatal
None.

### Major
- **Theoretical analysis is elementary and disconnected from experiments (Section 4).** Proposition 1 ("Exponential Forgetting") is an algebraic expansion of the convex recurrence — it states that after k overwrites the original content is weighted by (1−λ)^k, which follows directly from the definition of the LRU update rule. Proposition 2 ("Memory Boundedness") observes that a convex combination of bounded vectors remains bounded. The half-life and effective-horizon derivations are straightforward consequences of the recurrence formula. These results are correct, but presenting them as a contribution on par with the architecture and empirical evaluation (line 33: "We provide a theoretical analysis... establishing formal bounds on forgetting, retention horizons, and stability") overstates their depth. More importantly, the bounds are never tested against observed behavior — the predicted half-lives are not compared to empirical forgetting rates, and the theoretical framework does not inform hyperparameter selection or predict when the model will succeed or fail. The theory section functions as a formal restatement of the update rule's properties rather than as a tool for understanding or prediction.

### Minor
- **Unexplained discrepancy between main and ablation results.** Table 1 reports ELMUR's RememberColor3-v0 success as 0.89 ± 0.07 (100 evaluation episodes, 3 runs), while Table 3 reports "Baseline ELMUR" on the same task as 1.00 ± 0.00 (20 evaluation episodes, 3 runs). The 11-point gap with zero-variance at 1.00 is not reconciled. While the protocols differ in evaluation budget (100 vs. 20 episodes), the paper should explain the gap or explicitly state configuration differences between main evaluation and ablation runs.
- **RMT and TrXL baselines are never introduced or described.** These appear in Figure 3 and are mentioned in passing at line 274, but unlike DT, RATE, DMamba, BC-MLP, CQL, and DP — which are described in Section 5.1 — RMT and TrXL receive no architectural description or implementation details.
- **MIKASA-Robo aggregate claims rely on stripped appendix content.** The abstract claims ELMUR achieves "the best success rate on 21 out of 23 tasks" and "improving the aggregate success rate across all tasks by about 70% over the previous best baseline." However, the main text shows results for only 4 of 23 tasks (Table 1). The strength of the aggregate claim is not verifiable from the main text alone.
- **MoE FFN presented as core but shown non-essential.** The MoE FFN is described as a design choice in the method section (lines 92–94, 110), yet the ablation (Table 3) shows that replacing it with a standard MLP yields identical performance (1.00 ± 0.00). While the ablation itself acknowledges this, the method section could more clearly distinguish essential from incidental components.
- **All ablations are on a single task.** The component ablations and sensitivity analysis (Table 3, Figure 6) are conducted exclusively on RememberColor3-v0. While informative, this limits confidence that findings about λ sensitivity, the M ≥ N condition, and component importance generalize across tasks and domains.

### Trivial
- **POPGym gains are modest on reactive tasks.** The aggregate improvement over RATE is 10.4 vs. 9.5, and on reactive tasks the methods are statistically tied (9.2 vs. 9.1). The framing that ELMUR "consistently outperforms baselines" (line 259) is directionally true but slightly overstates the magnitude on reactive subsets.

## Nice-to-Haves
- **Active memory turnover stress test.** The T-Maze benchmark stores a single unchanging cue. A variant where the agent must remember *which* of several cues was seen, or where cues change mid-trajectory, would demonstrate that the LRU mechanism works when memory requires active management — not just when a single slot can be frozen.
- **Ground the theory in experiments.** Derive concrete predictions from the half-life formula — e.g., for given M, L, λ, at what corridor length should performance degrade? Testing those predictions would connect the theoretical section to the empirical results meaningfully.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Baseline selection stacks the deck" (Harsh Critic):** The claim that including CQL and Diffusion Policy is unfair because they are MDP methods. Including MDP baselines to demonstrate that POMDP tasks require memory is standard practice; the paper also includes proper POMDP baselines (RATE, BC-LSTM, DMamba). REMOVED.
- **"RATE and BC-MLP at 0.7 undercuts the struggle claim" (Harsh Critic):** The claim that RATE/BC-MLP maintaining ~0.7 at 1M steps undercuts the paper's characterization. A 30-point gap to ELMUR's 1.0 is meaningful, and "struggle" is a fair characterization. REMOVED as nitpicking.
- **"Algorithm 1 computes M candidate updates but only one is used" (Harsh Critic):** This misreads the architecture. The cross-attention in tok2mem naturally produces M candidates (one per memory slot attending to all tokens), and the LRU then selects one slot to update. The cross-attention computation itself involves all M slots and affects gradients. REMOVED as a misunderstanding.
- **"DT adaptation details are missing" (Harsh Critic):** The paper states that all models use "the same data budgets and preprocessing" (line 208). Specific adaptation details are in the stripped appendix, which exists in the original submission. REMOVED.
- **"Formal theoretical analysis with exponential forgetting bounds and stability guarantees" (Strength Finder):** This strength overstates the theoretical contribution. The derivations are correct but elementary — algebraic consequences of the convex update definition. The paper does provide theoretical grounding, but not at the level this strength claims. DEMOTED; the theoretical content is appropriately characterized as a weakness at the Major level.

## Novel Insights
The review process highlights an important tension in this work: the most impressive result (T-Maze at 1M steps) demonstrates a special case where a single piece of information is stored once and retrieved at the end, with no active memory turnover. Meanwhile, the LRU mechanism — the paper's core contribution for memory management — is most interesting precisely when memory must be actively managed (overwriting stale information while retaining relevant cues). The ablation on RememberColor3-v0 partially addresses this (showing LRU removal causes large drops), but the paper would be strengthened by a benchmark that requires discriminating which of multiple stored memories is relevant at decision time, rather than simply recalling the only stored cue. This observation does not invalidate the results but clarifies the gap between what is demonstrated and what is claimed.

## Suggestions
- Reconcile the Table 1 / Table 3 discrepancy on RememberColor3-v0, or explicitly note the configuration differences between main evaluation and ablation runs.
- Add a brief description of RMT and TrXL in Section 5.1, or remove them from Figure 3 if they are not part of the intended baseline set.
- Move the MoE FFN description in Section 3 to note that it is an optional efficiency improvement rather than a core component, consistent with the ablation finding.
- Either ground the theoretical analysis in the experiments (e.g., test whether predicted half-lives match observed forgetting) or reduce the prominence of the theory section in the contribution claims.

## Score and Decision

**Calibration:** ELMUR is clearly stronger than RATE (4.75), DT-Mem (5.75), and LRAM (5.75), and is comparable to Stable Hadamard Memory (6.50) — the closest anchor. ELMUR brings stronger empirical results (100% T-Maze at 1M steps, 3 diverse benchmarks) but weaker theoretical grounding. It sits above MELODI (6.25) in its domain due to broader evaluation and more striking headline results. The paper's strengths (spectacular T-Maze result, clean architecture, strong ablations, cross-domain consistency) are sufficient for acceptance, while the weaknesses (elementary theory, minor unexplained discrepancies, single-task ablations) are addressable but collectively nontrivial.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>