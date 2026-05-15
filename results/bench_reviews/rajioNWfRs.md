Now I have all the information I need. Let me write the consolidated review.

---

## Summary

TNT proposes a two-stage training paradigm for deep memory RNNs (e.g., Titans, TTT) that aims to decouple training efficiency from inference performance. Stage 1 introduces a hierarchical memory with a global module (large chunks, captures long-range context) and multiple local modules with periodic state resets that enable context parallelism; a Q-K projection mechanism addresses the domain mismatch between memory compression and retrieval. Stage 2 is a brief fine-tuning phase that adapts local memories to smaller chunk sizes for high-resolution inference. Evaluated on Titans at 150M parameters, TNT achieves up to 17× training speedup over the most accurate Titans baseline while improving perplexity and downstream accuracy.

## Strengths

- **Clear problem framing with three well-articulated challenges** (Section 3): domain mismatch between compression and retrieval, the chunk-size tradeoff between expressiveness and efficiency, and the train-test chunk-size mismatch. Each architectural contribution is positioned as a direct countermeasure, creating a coherent narrative.

- **Q-K Projection is a clean, efficient solution to Challenge 2.** By projecting queries onto the key subspace via a running second-moment matrix, the mechanism resolves the retrieval domain mismatch with constant-size state overhead. The ablation (Table 3) confirms its importance: removing it raises perplexity from 21.04 to 22.01.

- **The hierarchical memory design is flexible and cumulative.** Table 3 shows consistent perplexity reduction as local memory modules are added (23.53 → 21.04 → 20.74 → 20.47 → 20.15), confirming that multi-resolution processing captures richer temporal patterns than a single chunk size.

- **TNT demonstrates genuine improvements over its base architecture.** Table 2 shows TNT Stage 1 (23.13 avg PPL) substantially outperforming the best Titans configuration (25.07), and matching or exceeding the vanilla Transformer (23.58). The gains are clear relative to the architecture TNT is built upon.

- **The ablation study (Table 3) is well-designed**, cleanly isolating the contributions of global memory, Q-K projection, and Stage 2 fine-tuning against the Titans baseline.

## Weaknesses

### Major

- **The core decoupling claim is not tested with a controlled experiment.** The paper's central narrative is that Stage 2 resolves the train-test chunk-size mismatch (Challenge 3): a model trained with large chunks should degrade when evaluated at small chunks, and Stage 2 should recover. The mismatch problem is demonstrated on vanilla Titans (Figure 2), but no analogous experiment is performed for TNT. Table 2 shows Stage 2 models with smaller chunks achieving better perplexity than Stage 1 models, but it never shows a *single* TNT Stage 1 model evaluated at a mismatched (smaller) inference chunk size, followed by Stage 2 recovery. Without this controlled comparison, the improvements from Stage 2 could be attributed to extra training compute rather than specifically resolving the chunk-size mismatch. The paper notes Stage 2 requires ~5% extra compute (via Table 4, reported in text), but no compute-matched control (continued training at the original chunk size) is provided. This leaves the paper's headline contribution—decoupling training from inference—with incomplete empirical support.

- **Speedup metrics use training loss, not validation quality.** The 17× speedup reported in Table 1 measures time to reach a training loss of 3.20. The model quality the paper ultimately evaluates is validation perplexity and downstream accuracy (Table 2). While training loss and validation perplexity are correlated in this regime, the paper provides no calibration showing what validation perplexity corresponds to training loss 3.20 across configurations, and no time-to-validation-perplexity comparison. The 17× figure is also computed against Titans C=8 (the slowest Titans variant, though also the most accurate among Titans). Against Titans C=128 (3.71 hrs), TNT {64} (1.12 hrs) provides a more modest 3.3× speedup. The paper does transparently report all configurations in Table 1, but the abstract's "up to 17×" framing requires careful qualification.

### Minor

- **Context parallelism via periodic reset is demonstrated only on a single device.** Figure 4 shows TNT maintaining constant runtime as sequence length increases (with fixed total tokens), which demonstrates effective intra-device parallelization. However, the paper's claim that resets enable "massive context parallelization" by distributing independent segments across multiple devices is never tested with a multi-device experiment or throughput-scaling measurement. The observed flat runtime could arise from better chunk-level batching rather than the reset mechanism specifically. A comparison against a non-reset baseline or a multi-device scaling plot would strengthen this claim considerably.

- **Experiments are limited to 150M parameters trained on 10B tokens.** This is a reasonable scale for an efficiency-focused methods paper, but it limits how strongly the paper can claim to have "removed a critical scalability barrier." The path from 150M to larger scales is plausible but unverified.

- **The mapping from Stage 1 to Stage 2 models is ambiguous.** Table 2 lists Stage 1 models (e.g., C_L = {8}, {8,16}, {4,8,16,32}) and Stage 2 models (e.g., {1}, {2,4}, {2,4,8,16}) but does not specify which Stage 1 checkpoint each Stage 2 model was fine-tuned from. This makes it difficult to assess the exact improvement attributable to Stage 2 for a given starting point.

## Nice-to-Haves

- A compute-matched control for Stage 2: fine-tune a Stage 1 model at its original chunk size for the same number of steps and compare against fine-tuning at a smaller chunk size. This would isolate the effect of chunk-size adaptation from that of additional training.
- Multi-device scaling experiments to validate the context parallelism claim.
- A diagnostic on Q-K projection behavior: e.g., cosine similarity between projected queries and training keys before/after projection, correlating with the degree of domain mismatch.

## Removed Points

These points were flagged for removal. Treat them with caution.

- **"No evidence that Stage 2 resolves the train-test chunk mismatch"** — Partially incorporated into the Major weakness above, but the original framing as a *fatal* evidential gap was softened. The paper does provide indirect evidence (Stage 2 models with smaller chunks outperform Stage 1), and the problem itself is demonstrated on the base architecture (Figure 2). The gap is a missing controlled experiment, not an absence of all evidence.

- **"Efficiency claims are not linked to the final model quality"** — Retained as a Major weakness but weakened from the harsh critic's original severity. The training loss proxy is imperfect but not arbitrary; the independent quality results in Table 2 provide corroborating evidence that TNT achieves better quality with less training time.

- **"Context parallelism via periodic reset is claimed but not validated"** — Retained as Minor. The single-device evidence in Figure 4 does demonstrate parallelism; the gap is in multi-device scaling specifically.

- **Strength Finder claim: "TNT achieves up to 17× speedup... directly shown by TNT's linear runtime scaling"** — Weakened. The 17× figure requires careful qualification (measured against the slowest Titans variant, using training loss not validation perplexity).

- **Strength Finder claim: "Two-stage design decouples training efficiency from inference resolution, a novel solution"** — Kept but qualified. The decoupling is the paper's core claim and has partial support, but the controlled experiment isolating this effect is missing.

- **Criticism about missing multi-device experiments for context parallelism** — The harsh critic demanded multi-device scaling; this is a fair observation but does not invalidate the single-device evidence. Kept as Minor.

## Novel Insights

None beyond the paper's own contributions. The three-challenge framing (Section 3) is a useful synthesis of problems faced by deep memory modules, and the Q-K projection mechanism is a genuinely neat idea worth wider adoption, but the reviews did not surface insights the paper itself doesn't already articulate.

## Suggestions

- Add the controlled chunk-mismatch experiment: evaluate a Stage 1 TNT model at its training chunk size and at C_L=1, report the perplexity gap, then apply Stage 2 and show recovery. This would directly validate the paper's central claim with minimal additional compute.
- Report time to reach a target validation perplexity (e.g., 23.13) for both TNT and the best Titans configuration, including Stage 2 overhead. This would ground the speedup claims in the quality metric readers care about.
- Clarify in Table 2 which Stage 1 checkpoint each Stage 2 model was fine-tuned from.
- Consider reporting speedup against Titans C=128 in the abstract alongside the 17× figure to give a more balanced picture of the efficiency gains.

## Anchor Comparison and Score Justification

**Anchors retrieved:**
| Path | Avg Score | Comparison to TNT |
|------|-----------|-------------------|
| `mX8b64iUaa` (ParaRNN) | 6.50 | ParaRNN has stronger empirical validation at scale (7B), custom CUDA kernels, and released code. TNT has broader conceptual scope but less rigorous evaluation of its central claims. |
| `xa3OnTb6c3` (MesaNet) | 6.50 | MesaNet offers more thorough experiments (up to 1B, many baselines) and stronger theoretical grounding. TNT's architectural innovations are comparably interesting but less well-validated. |
| `GoaWSQWtOE` (Smooth Reading) | 5.00 | TNT is stronger: it addresses training efficiency (not just inference), has architectural innovations, and shows concrete speedup results. Smooth Reading has a narrower scope. |
| `R3EJ2IjgOI` (Memory Caching) | 4.67 | TNT is clearly stronger: better problem framing, more architectural novelty, stronger ablations, and competitive quality results. |
| `YgvIjdzR4C` (Memora) | 4.50 | TNT is stronger in both contribution clarity and empirical results. |
| `ddf7XdLtNO` (Data Scheduling) | 4.00 | TNT is substantially stronger: architectural contribution vs. data scheduling heuristic. |
| `bjo26ERkai` (It Depends) | 2.00 | TNT is far stronger across all dimensions. |
| `LPqjfqw2OI` (Factorization Memory) | 2.00 | TNT is far stronger: clearer novelty, better ablations, more competitive baselines. |

TNT sits between the 5.0–6.0 band. It has genuine architectural contributions, a clear problem framing, and shows improvements over its base architecture. However, the core decoupling claim has incomplete empirical support (no controlled chunk-mismatch experiment for TNT), the speedup methodology uses training loss rather than validation quality, and experiments are at modest scale (150M). These gaps place it below ParaRNN/MesaNet (6.50) but above Smooth Reading (5.00) and Memory Caching (4.67). The paper makes a real contribution to an important problem but would benefit from stronger validation of its central claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>