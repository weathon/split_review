Now I have all the information I need to write the final consolidated review. Let me produce it.

## Summary

This paper introduces TNT, a two-stage training framework for deep memory modules (e.g., Titans, TTT) — recurrent architectures with non-linear test-time memorization. The key idea is to break the sequential dependency that prevents parallel training of these models by (1) using a hierarchical memory (global + local) where local memories periodically reset to a learned initial state, enabling context parallelism, and (2) a two-stage schedule: efficiency-focused pre-training with large chunks, then a brief fine-tuning with smaller chunks. Evaluated on 150M-parameter Titans models, TNT achieves up to 17.37× training speedup while improving perplexity (23.13 vs. 25.07) and commonsense reasoning accuracy (41.0% vs. 39.0%) over the best Titans baseline.

## Strengths

1. **Periodic reset mechanism enables context parallelism for non-linear deep memories.** The local memory reset to a learned initial state \(W_{\text{init}}\) at segment boundaries (Eq. 6) breaks sequential dependencies across chunks, allowing independent shards to be processed in parallel. Figure 4 shows TNT achieves near-constant runtime (~400–550ms) as sequence length grows from 2K to 32K, while Titans' runtime increases from ~400ms to ~4000ms. This directly addresses a long-standing challenge in parallelizing non-linear recurrences that prior work (Zhang et al., 2025; Guo et al., 2025) either mixed with attention or limited to linear memories.

2. **Q-K Projection empirically resolves the compression–retrieval domain mismatch.** The ablation in Table 3 shows a clear penalty when Q-K projection is removed: perplexity increases from 21.04 to 22.01 and commonsense accuracy drops from 40.6% to 36.4%. This confirms that projecting queries onto the subspace of previously observed keys mitigates the input-space mismatch between memory training (keys) and inference (queries).

3. **Two-stage training demonstrably decouples pre-training speed from inference resolution.** Stage 1 with large chunks achieves the speedup (up to 17.37× in Table 1), and Stage 2 fine-tuning with smaller chunks improves perplexity from 23.13 to 23.09 at only 5% additional compute (Section 5.3, Table 4). This directly resolves the chunksize mismatch identified in Challenge 3 (Figure 2).

4. **Clean ablation study validates each design component.** Table 3 systematically removes global memory, Q-K projection, and Stage 2 fine-tuning, with each removal degrading performance (global memory removal: 25.60 PPL—worse than the Titans baseline; Q-K removal: 22.01 PPL). This provides causal evidence for each proposed mechanism.

5. **Model quality improves beyond the best Titans baseline while also being faster.** In Table 2, TNT Stage 1 achieves average perplexity 23.13 vs. Titans' best 25.07 (chunk size 8) and higher commonsense reasoning accuracy (41.0% vs. 39.0%). The speedup is not at the expense of quality.

## Weaknesses

### Major

1. **The claimed "training paradigm" is inseparably tied to architectural changes, and the framing is overclaimed.** The paper repeatedly states TNT is "a general training paradigm applicable to any deep memory module rather than a specific architecture" (Section 1). Yet the contribution list includes "a novel hierarchical memory architecture" (Section 4.1), and the ablation in Table 3 confirms that the architectural components are essential: removing the global memory causes perplexity to jump to 25.60, *worse* than the original Titans baseline (23.53). The speedup and quality gains reported in Tables 1–2 compare TNT's global+local architecture against Titans' single-memory architecture, so the comparison conflates architecture and training method. A within-architecture comparison (TNT's hierarchical architecture trained without the two-stage schedule) is missing and would be needed to isolate what the training paradigm itself contributes. *This does not invalidate the paper's contributions, but it means the contribution is more accurately described as an architecture+training co-design rather than a general training paradigm.*

2. **No evaluation on tasks that require long-range dependencies, despite long-context efficiency being the central motivation.** The paper opens with "The demand for modeling long sequences" and consistently motivates TNT through the need to "apply these models to truly long sequences" (Section 1). However, the quality evaluation (Table 2) uses only standard perplexity datasets (C4, FineWeb, PG19) and short-context reasoning benchmarks. PG19 contains long documents, but perplexity is not reported as a function of position or sequence length, so it is impossible to tell whether the model actually uses long-range information. The hierarchical design deliberately resets local memory every 2048/4096 tokens, discarding fine-grained cross-segment information. Without demonstrating that quality holds on tasks requiring long-context reasoning (e.g., multi-hop QA over long documents, in-context retrieval at >16K), the practical significance of the runtime gains for long sequences remains unverified.

3. **The claim of generality is unsubstantiated.** The paper states TNT is "a general training paradigm applicable to any deep memory module" (Section 1) and the abstract says "Evaluated on Titans and TTT models." However, TNT is only ever applied to Titans. TTT appears only as a baseline trained with its original method (Table 2, PPL 27.62), not as a TNT-instantiated model. Other deep memory modules (Atlas, etc.) are mentioned but never tested. The hierarchical memory design (global vs. local, periodic resets) may not transfer straightforwardly to architectures with different recurrence structures. The generality claim is a major selling point of the paper and needs at least one additional instantiation to be credible, or the claim should be scaled back.

### Minor

1. **Stage 2 fine-tuning shows very marginal improvement.** The best Stage 1 perplexity is 23.13 and Stage 2 improves it to 23.09 — a 0.04 PPL reduction at 5% additional compute. The paper frames this as important, but the gain is negligible. The authors should either show a more substantial benefit (e.g., on the \(C'_L=1\) configuration for autoregressive decoding) or temper the claim about Stage 2's importance.

2. **No sensitivity analysis for the local window size \(S_L\).** The paper uses \(S_L=2048\) or \(4096\) throughout. This hyperparameter controls how often local memory resets (and thus the degree of parallelism vs. context preservation). An ablation varying \(S_L\) would help readers understand the trade-off.

3. **Theoretical justification for Q-K Projection is thin.** The paper motivates it as projecting queries onto the subspace of past keys, but does not analyze why a linear projection should suffice when keys may lie on a non-linear manifold (the paper notes keys are often L2-normalized). The ablation confirms it works empirically, so this is not a fatal flaw, but the framing as a "principled solution" (Section 4.1.2) overstates what is essentially a heuristic validated only by ablation.

### Trivial

None.

## Nice-to-Haves

- **Confidence intervals or multiple seeds.** Standard practice in large-scale LM training is single-run evaluation, so this is not a flaw, but reporting variance would strengthen the claims, especially for the small commonsense accuracy differences (e.g., 41.0% vs. 39.7%).
- **Position-wise perplexity on PG19** to demonstrate that long-range dependency capture is preserved despite the local memory reset mechanism.

## Removed Points

These points were raised by reviewers but excluded or downgraded from the main weaknesses after verification against the paper:

1. *"The speedup comparison varies (17× vs Titans C=8, 3.2× vs C=128)."* — Removed because the paper explicitly cites the comparison as "up to 17.37×" against the "most accurate baseline configuration" (Titans C=8), which is standard reporting practice. The paper does not claim uniform 17× against all configurations.

2. *"Missing confidence intervals."* — Moved to Nice-to-Haves. Single-run large-scale LM training is standard in this community; the absence is not a flaw but would strengthen the paper if included.

3. *"Q-K Projection may not work for normalized keys."* — Demoted to Minor. The paper acknowledges that keys are often normalized and notes the simplification this enables (Section 4.1.2: "denominator... can simplify"). The ablation confirms it works. The reviewer's concern is speculative.

4. *"Parameter budget not controlled between global and local memories."* — Removed. The paper states all models are 150M parameters (Section 5.1). Without evidence that parameter allocation is unfair, this is speculation.

5. *"Strength: framework is model-agnostic."* — Removed from strengths because it conflicts with verified Weakness #3 (generality unsubstantiated). The paper's claim of model-agnosticism is not backed by experiments beyond Titans.

6. *"Missing comparison to concurrent work (Zhang et al., 2025; Guo et al., 2025)."* — Removed. The paper discusses these works in Section 1 ("Recent work attempts to mitigate this issue...") and positions TNT relative to them conceptually. Quantitative comparison would strengthen the paper but is not standard for concurrent work.

## Novel Insights

None beyond the paper's own contributions. The reviewer reviews surface a genuine tension in how to classify TNT (architecture vs. training paradigm) and identify a clear gap between the paper's long-context motivation and its evaluation suite, but these are gaps in the paper's framing and evaluation rather than novel observations about the method.

## Suggestions

1. **Add a within-architecture ablation.** Train the TNT hierarchical architecture using standard chunkwise training (no periodic resets, no two-stage schedule) and compare wall-clock time to quality. This would isolate the training paradigm's contribution from the architecture's.

2. **Add long-context quality evaluation.** Evaluate on at least one benchmark that requires fine-grained long-range dependencies (e.g., BABILong, RULER, or language modeling perplexity as a function of context position on PG19). Without this, the paper's central motivation is unvalidated.

3. **Demonstrate generality on at least one other architecture** (e.g., TTT or a simple deep memory RNN), or moderate the claim from "any deep memory module" to "applicable to architectures like Titans."

4. **Provide a sensitivity analysis of the local window size \(S_L\)** to show how the parallelism/quality trade-off behaves.

5. **Report Stage 2 results with per-step curves** rather than just the endpoint, to clarify whether the small improvement (0.04 PPL) is meaningful or near saturation.

## Score and Decision

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| MoM: Mixture-of-Memories | 3PdOq8Rgue.md | 5.50 | 1 (middle) | More comprehensive evaluation at larger scales (380M, 1.3B); TNT has more novel method but less evaluation breadth |
| Smooth Reading | GoaWSQWtOE.md | 5.00 | 1 (middle) | Comparable evaluation thoroughness and clarity; TNT's training efficiency contribution is more fundamental |
| Memory Caching | R3EJ2IjgOI.md | 4.67 | 1 (middle) | Simpler method with computational complexity questions; TNT has cleaner method and stronger results |
| Hierarchical Memories Pretraining | XOu5z16cbY.md | 4.80 | 2 | Larger-scale experiments (trillion tokens) but more incremental method; TNT is more novel but smaller scale |
| Tuning Burn-in Phase RNN | jwkdKpioHJ.md | 5.33 | 2 | Theoretical+empirical on a related problem; TNT has more practical impact but lacks theoretical analysis |

Round-1 bracket: between 3.5 and 7.5 → narrowed by round-2 to ~4.5–5.5.

The paper's core idea is novel and the speedup results are impressive. However, three significant gaps (architecture/training conflation, missing long-context quality evaluation, unsubstantiated generality claim) prevent it from reaching the 5.5+ tier. It is comparable to Smooth Reading (5.00, accepted) in overall quality — a methodologically sound paper with clear contributions but evaluation gaps that should be addressed. The paper is above the rejected Memory Caching paper (4.67) because its method is more novel and the evidence of its central claim (training speedup) is stronger.

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**