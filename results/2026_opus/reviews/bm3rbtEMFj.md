Now let me do calibration searches to anchor my score.Initial bracket: 5.0–7.0. Round 2 — narrow.## Summary
ELMUR proposes a transformer architecture for long-horizon RL/IL in which each layer has its own external memory updated through bidirectional cross-attention (mem2tok / tok2mem) and a Least Recently Used (LRU) policy that combines slot replacement with convex blending. The authors provide a theoretical analysis of retention horizons under the blend rule and empirical results on T-Maze (100% success up to 10⁶ steps with L=10, S=3), MIKASA-Robo manipulation (best on 21/23 reported tasks), and POPGym-48 (10.4 aggregate, best on 24/48 tasks).

## Strengths
- **Striking long-horizon retention on T-Maze.** Figure 3 shows 100% success at corridor lengths up to 10⁶ steps with a training context of L=10, S=3 — a dramatic gap over RMT, TrXL, DMamba, BC-LSTM, RATE, DT, BC-MLP, all of which degrade by 10²–10⁴ steps. The result is concrete evidence that the layer-local memory + LRU recipe carries information well beyond the attention window.
- **Strong gains on real manipulation.** Table 1 shows ELMUR reaching 0.78 ± 0.03 on TakeItBack-v0 vs. 0.42 ± 0.24 for the next-best RATE, and 0.89 ± 0.07 vs. 0.65 ± 0.04 on RememberColor3-v0. These are large, consistent gains on sparse-reward visual manipulation with continuous actions.
- **Per-component ablations isolate several design choices.** Table 3 confirms persistent layer-local memory matters: removing LRU drops to 0.43, sharing memory across layers drops to 0.45, and removing both relative bias and LRU drops to 0.22. The "shared vs. layer-local" comparison is a clean causal piece of evidence for the architecture's central framing.
- **Explicit theoretical analysis of retention.** Section 4 provides a closed-form geometric forgetting series (Prop. 1), a half-life corollary, and a boundedness result (Prop. 2). Even though these are mild, they explicitly link λ, M, and L to a retention bound — uncommon for memory-augmented transformers.
- **Compute footprint is competitive.** Section 5.2 reports 2.1M parameters and 6.8 ± 0.5 ms/step, faster than RATE (7.2 ms) and DT (10.7 ms), so the long-horizon gain does not come at a clear efficiency cost.

## Weaknesses

### Fatal
None.

### Major
- **The headline T-Maze "100,000×" claim does not isolate the LRU+convex-blend mechanism.** The T-Maze cue is effectively one bit followed by a deterministic corridor. With L=10, S=3, and the LRU policy starting in pure-replacement mode (α=1 for empty slots), the result cannot distinguish (a) the cue slot genuinely surviving repeated convex blending from (b) subsequent writes degenerating to near-no-ops or repeatedly targeting non-cue slots. Section 4's bound H(ε) = M·L·ln(ε)/ln(1−λ) predicts retention linear in M·L, yet observed retention vastly exceeds this and the paper attributes the gap only to the bound being "conservative" (Section 4, last paragraph). Without slot-content probing, ablation against replacement-only / FIFO / random eviction on a task with actual memory contention, the 100,000× number does not yet support the architectural claim it is used to support.
- **Baseline composition shifts across benchmarks, weakening the cross-domain robustness claim (RQ4).** Figure 3 (T-Maze) includes RMT, TrXL, DMamba, BC-LSTM, RATE, DT, BC-MLP. Table 1 (MIKASA-Robo) drops RMT, TrXL, DMamba, BC-LSTM and adds CQL, DP. Table 2 (POPGym) drops RMT, TrXL, DMamba, CQL, DP and adds Random. RMT and DMamba — the closest contemporary memory-augmented / state-space competitors — appear only on T-Maze, so the "robust across domains" claim cannot be checked against any one fixed strong contender across all three benchmarks.
- **The "No LRU" ablation conflates two distinct effects.** Table 3 shows that "No LRU" drops to 0.43, but as stated this removes the write-management mechanism entirely rather than swapping it for an alternative eviction rule (FIFO, random, learned gating, or replacement-only). Combined with the fact that the ablation runs on RememberColor3-v0 — a 3-distractor visual recall task that does not stress long-horizon eviction — the evidence supports "having layer-local memory with a write path matters" but does not isolate the specific LRU+convex-blend choice that is the paper's novel architectural contribution.

### Minor
- **MoE-FFN ablation shows no measurable effect on the chosen task.** Table 3 reports "MoE → MLP" at 1.00 ± 0.00, identical to the baseline, despite the MoE being introduced as a deliberate design choice in Section 3 ("This design enables expressive updates while keeping inference efficient"). The paper acknowledges this in Section 5.2 ("replacing MoE-FFN with MLP-FFN preserves accuracy while improving computational efficiency"), but the architectural framing should be tempered accordingly.
- **Regime-dependence in Figure 6 is reported but not reconciled with the framing.** Figure 6 (a–d) shows that performance is robust to λ, σ, and segmentation when M ≥ N but collapses sharply when M < N. The motivation for LRU + convex blending was precisely the bounded-capacity regime. The paper does not explicitly engage with the fact that ELMUR succeeds when memory acts essentially as a hard cache (M ≥ N), versus the bounded regime where the blending mechanism is supposed to matter.
- **"21 of 23 tasks" vs. "32 MIKASA-Robo tasks".** The abstract and Section 1 cite "21 of 23 tasks" but Table 1's caption references "all 32 MIKASA-Robo tasks in Appendix, Table 8." The framing should be precise about what subset the 21/23 covers and what subset the "~70% aggregate improvement" is over.
- **POPGym aggregates in Table 2 lack error bars.** The 10.4 / 9.5 / 9.0 ordering among ELMUR, RATE, BC-LSTM is reported without SEM at the aggregate level, while Tables 1 and 3 do include SEM. Given the small gap, error bars would clarify the size of the win on the 48-task aggregate.
- **Training corridor length in RQ1 is under-specified.** Section 5.1 says "training with short contexts (L=10, S=3) and evaluating on corridors up to 10⁶ steps", but it is not crisp whether the training corridor length equals L·S=30 or is longer (with segment recurrence stretching over more segments). The "100,000×" extrapolation factor depends on this detail.

### Trivial
None retained (the harsh reviewer's remaining items were either presentation-style sweeps or duplicates of the points above).

## Nice-to-Haves
- Probe the contents of memory slots across a trajectory (e.g., decode the cue from a specific slot at long horizons on T-Maze and on a multi-cue MIKASA-Robo task). This would turn the 100,000× number into an architectural insight rather than a benchmark headline.
- Run a T-Maze variant with multiple sequential cues whose joint retention exceeds M·L, where Section 4's bound predicts failure. The result either delineates the operating regime honestly or provides an interesting puzzle for the theory to explain.
- An ablation that swaps the LRU policy for FIFO / random eviction / learned gating on a task with real memory contention would directly isolate the LRU+blending contribution.
- Add RMT and DMamba comparisons on MIKASA-Robo and POPGym for symmetric cross-benchmark evidence.

## Removed Points
These points are flagged to be removed, treat them with caution.
- *Harsh critic's "Simple and scalable is a stretch"* — opinion about abstract tone; not a substantive flaw.
- *Harsh critic's "Related work undersells how close ELMUR sits to prior architectures"* — the paper does discuss RATE, Memformer, and Block-Recurrent Transformer in Section 6 and frames LRU + convex blending as the novel piece. The framing is reasonable and the criticism amounts to disagreement about novelty calibration rather than a verifiable misrepresentation. Hard rule against speculative "missing related work" critiques also applies.
- *Harsh critic's "Section 4 theory is descriptive rather than predictive"* — Propositions 1 and 2 are honest, useful, and consistent with what the paper claims. Asking for a stronger theorem connecting LRU slot choice to information content is a nice-to-have, not a structural flaw.
- *Strength Finder's "computational efficiency" and "cross-domain consistency"* — kept partially; the efficiency claim is concrete (numbers in Section 5.2), but the cross-domain consistency strength is weakened by the baseline-composition concern in Major, so it is downweighted rather than treated as a top-line strength.

## Novel Insights
None beyond the paper's own contributions. The most interesting unexpected finding — Figure 6's M ≥ N vs. M < N regime split, where the bounded-capacity regime the LRU rule was designed for is also where ELMUR is most fragile — is in the paper but underexploited; it would be a genuinely interesting story if the authors engaged with it directly.

## Suggestions
- In RQ1, state the training corridor length explicitly and probe memory-slot contents to demonstrate that the cue actually survives in a specific slot under LRU+blending.
- Add a "policy ablation" that swaps LRU for FIFO, random, learned gating, and replacement-only (no blending), on a multi-cue T-Maze variant — i.e., a task where blending vs. replacement actually matters.
- Reconcile the 23 vs. 32 task counts in the abstract, introduction, and Table 1; state clearly which subset the 21/23 claim and the ~70% aggregate improvement refer to.
- Add RMT and DMamba to Table 1 and Table 2; if compute or training-budget constraints preclude this, state them explicitly.
- Add SEM to the POPGym aggregates in Table 2.
- Soften the "simple" framing in the abstract, or qualify it as "simple to integrate into a standard transformer decoder."

## Calibration

Anchors retrieved:

Round 1 (bracketing):
- `N581Nje6fH.md` (1.50, R1, weak) — much weaker, vague long-horizon-RL story with no quantitative wins; ELMUR is far stronger.
- `It4KL6XnPq.md` (3.00, R1, weak) — Foundation Policies w/ Memory on POPGym; weaker contribution and weaker results; ELMUR clearly above.
- `N18Z2MkMEa.md` (3.00, R1, weak) — unrelated LLM coding memory paper; not comparable.
- `7ZyFjPUeJp.md` (3.00, R1, weak) — Mamba MARL; weaker positioning.
- `FhbZ1PQCaG.md` (5.75, R1, middle) — DT with internal memory; similar concept but with much weaker empirical wins than ELMUR.
- `c4w7WVs1z7.md` (4.75, R1, middle) — RATE (cited baseline in ELMUR); methodologically related but with weaker results; ELMUR is stronger.
- `9DrPvYCETp.md` (5.33, R1, middle) — Shared Recurrent Memory Transformer (multi-agent); related architecture, weaker uptake.
- `We5z3UEnUY.md` (6.50, R1, middle/strong) — Stable Hadamard Memory; very close peer (POPGym, theoretical analysis of memory update); ELMUR's empirical wins are at least as strong, but its mechanism-isolation is weaker.
- `9pW2J49flQ.md` (8.00, R1, strong) — DeepLTL; different research area (LTL satisfaction), much more polished contribution; ELMUR is below.
- `Tzh6xAJSll.md` (7.60, R1, strong) — Scaling laws for associative memory; cleaner theory; ELMUR is below.
- `PdaPky8MUn.md` (8.00, R1, strong) — Fair long-sequence comparison; broader and more rigorous; ELMUR is below.
- `agPpmEgf8C.md` (8.00, R1, strong) — Predictive auxiliary objectives in RL; well-controlled empirical study; ELMUR is below.

Round 1 bracket: **5.0–7.0**.

Round 2 (narrowing):
- `B5kAfAC7hO.md` (5.33, R2) — Provable rep for POMDPs; theory-heavy, weaker empirics than ELMUR; ELMUR sits above.
- `IaKxCsJSOO.md` (6.00, R2) — Tractable inference for offline RL; different angle, comparable rigor; ELMUR is similar-or-slightly-above.
- `o3pJU5QCtv.md` (6.25, R2, accept) — EC-Diffuser manipulation; cleaner empirical paper with smaller scope; ELMUR is comparable.
- `s1kyHkdTmi.md` (7.00, R2, accept) — Evolved Universal Transformer Memory; broader and more thoroughly analyzed memory contribution; ELMUR somewhat below.
- `TvGPP8i18S.md` (6.25, R2, accept) — MELODI hierarchical memory compression; ELMUR is comparable, with stronger RL-specific wins but weaker analytical depth.
- `q2Lnyegkr8.md` (6.75, R2, accept) — Forgetting Transformer; strong analysis + long-context experiments; ELMUR is slightly below.
- `vBo7544jZx.md` (6.67, R2, accept) — PMI inference framework; comparable.
- `5iWim8KqBR.md` (5.50, R2) — Memory-efficient algorithm distillation; ELMUR is above on empirical breadth.
- `zjeHLSiNv1.md` (6.00, R2, accept) — Ultra-Sparse Memory Network; comparable.

Round 2 narrows the bracket to **5.5–6.5**. ELMUR sits closest to Stable Hadamard Memory (6.5, Accept), MELODI (6.25), and Ultra-Sparse Memory (6.0): a clear, well-motivated memory architecture with theoretical analysis and concrete benchmark wins, but with mechanism-isolation gaps and a headline claim that is striking but evidentially under-supported. I place ELMUR slightly below Stable Hadamard Memory because its ablation does not isolate the novel piece (LRU+blending) as cleanly, and above the 5.5–5.75 cluster because the MIKASA-Robo wins are large and concrete.

## Score and Decision

Final score: 6.0. Originality is moderate (LRU+convex-blend is the novel piece; layer-local cross-attention memory is established). The research question is important. Claims are well-supported on MIKASA-Robo and POPGym, less so on T-Maze where the mechanism is not isolated. Soundness is good with limitations noted above. Clarity is good. The contribution should be useful to the memory-RL community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>