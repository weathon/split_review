Now I have enough context from calibration. Let me write the consolidated review.

## Summary

The paper introduces TNT, a two-stage training paradigm for deep memory modules (e.g., Titans) that decouples training efficiency from inference performance. Stage 1 uses a hierarchical memory architecture with a global module for long-range context and multiple parallel local modules with periodic state resets, enabling massive context parallelism. A Q‑K projection mechanism addresses the compression–retrieval domain mismatch. Stage 2 fine-tunes only the local modules at smaller chunk sizes for high-resolution inference. Experiments on 150M-parameter models show up to 17× training speedup over Titans baselines and improved perplexity and commonsense reasoning accuracy.

## Strengths

1. **Hierarchical memory with periodic state resets enables context parallelism for non‑linear RNNs.** Eq. 6 defines a local memory that resets to a shared learnable state every S_L tokens, breaking sequential dependencies across shards and allowing independent processing across devices (Figure 1). This is a genuine architectural innovation for parallelizing deep memory modules.

2. **Q‑K Projection resolves the compression–retrieval mismatch.** Eq. 7 projects queries onto the subspace spanned by recent keys before retrieval. The ablation (Table 3) shows removing this projection increases perplexity from 21.04 to 22.01 and drops commonsense reasoning accuracy from 40.6% to 36.4%, confirming its essential role.

3. **Two-stage design effectively decouples pre‑training efficiency from inference performance.** Stage 1 uses large chunks (C_G=2048) for throughput; Stage 2 fine-tunes only the local modules at small chunks (C'_L as low as 1). Table 2 shows Stage 2 consistently improves perplexity (e.g., from 23.13→23.09) and reasoning accuracy (e.g., 40.6%→40.9%) with only 5% additional compute.

4. **Substantial training speedup.** Table 1 reports time-to-quality (target loss 3.20): TNT with C_L=64 completes in 1.12 hours vs. 19.48 hours for Titans C=8 (17.37× speedup) and 3.71 hours for Titans C=128 (3.2× speedup). Even at identical chunk sizes (C_L=8 vs. C=8), TNT is 7.68× faster due to context parallelism.

5. **Consistent quality improvements over Titans baselines.** Table 2 shows TNT Stage 1 (C_L={4,8,16,32}) achieves average perplexity 23.13 vs. the best Titans model at 25.07, and average commonsense reasoning accuracy 40.6% vs. 39.0% (Titans) and 39.7% (gated Transformer).

## Weaknesses

### Fatal
None.

### Major

1. **Missing ablation of the local memory reset interval (S_L).** The local memory reset mechanism is the key enabler of context parallelism, yet the paper provides no analysis of how S_L affects training speed or final quality. The experiments use S_L=2048 and S_L=4096 without justification, and there is no study of sensitivity to this parameter. If S_L is too small, local memory loses fine-grained context; if too large, parallelism benefits shrink. An ablation varying S_L (e.g., 512, 1024, 2048, 4096) is needed to demonstrate robustness and guide practitioners. This is the most significant empirical gap.

### Minor

2. **Stage 2 improvement confounded with additional training.** The ablation (Table 3) shows Stage 2 fine-tuning improves perplexity from 21.04 to 20.86 (single local memory). But this improvement could partly reflect additional training steps rather than the chunk‑size adaptation itself. A control experiment—fine-tuning Stage 1 for the same number of steps *with the original chunk size* (C'_L = C_L)—would isolate the effect. Without it, the claim that Stage 2 specifically resolves chunk‑size mismatch is only partially supported.

3. **Generality claim supported on only one architecture.** The paper states TNT is “a general training paradigm applicable to any deep memory module” but instantiates it only on Titans. TTT appears as a baseline in Table 2, not as a TNT‑enhanced model. While the paper makes a reasonable case for generality, validating on at least one additional deep‑memory architecture would substantially strengthen this claim.

4. **Accuracy gains on commonsense reasoning are modest and within variance.** The paper correctly notes that perplexity is a more stable metric at 150M scale, but the downstream accuracy improvements (1–2 points over Titans) are well within typical run‑to‑run variance for models of this size. The claim “improves model accuracy” should be read as applying primarily to perplexity, with the reasoning results being suggestive rather than conclusive.

5. **Limited model scale.** Experiments use 150M‑parameter models trained on 10B tokens. Scaling to larger models (e.g., 1B+) is left to future work, and it is unclear whether new bottlenecks (e.g., inter‑device communication for context parallelism, memory for the Q‑K projection running sum) would emerge at scale.

### Trivial
None.

## Nice-to-Haves

- An explicit limitations section discussing scale‑up, potential numerical considerations for the Q‑K projection running sum over very long contexts, and the scope of generality claims would improve the paper.
- The runtime curve in Figure 4 (near‑flat with fixed token‑per‑batch) follows from the experimental design, but a brief explanation of *why* this occurs (batch size scales inversely with sequence length) would preempt confusion.

## Removed Points

- **Missing optimal‑chunk Titans baseline (C=64, Figure 2):** The critic misunderstands Figure 2, which evaluates *inference* perplexity of a 550M model pre‑trained with C=64; Table 2 uses 150M models. The 13.78 PPL in Figure 2 is from a model 3.7× larger and is not comparable. The paper’s comparison is fair as presented.
- **Suspiciously flat runtime scaling:** The fixed‑token‑per‑batch design (0.5M tokens) means batch size decreases linearly with sequence length, making the flat runtime entirely expected. TNT C_L=128 does increase from 400→550 ms (37.5%), which is not “nearly constant” in an absolute sense.
- **Q‑K projection numerical stability:** The sum in Eq. 7 is bounded by the local chunk size C_L (at most 32 in the experiments), not the full sequence length. The critic’s concern about unbounded growth over tens of thousands of tokens misreads the equation bounds.
- **Missing Table 4 / appendix content:** Stripped by PDF parsing; present in original submission.
- **Missing related works / formatting nitpicks / typos:** Parser artifacts or outside scope.
- **General‑applicability strength (from Strength Finder):** The paper’s claim of generality is aspirational and only validated on Titans; this strength is overstated.
- **Generic strengths** about the importance of the problem were removed per filtering guidelines.
- **Missing references / reproduction details** that conflict with instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add an S_L ablation study** varying the local memory window size (e.g., 512, 1024, 2048, 4096) and report both speed and perplexity. This is the most important missing experiment.
2. **Add a Stage 2 control** by fine-tuning the Stage 1 model for the same number of steps with the original chunk size C'_L = C_L to separate adaptation effects from additional training.
3. **Consider validating on at least one additional deep‑memory architecture** (e.g., TTT) to support the generality claim, or alternatively moderate the claim to reflect the single‑architecture validation.
4. **Include a brief explanation** in the Figure 4 caption of why runtime is near‑flat under fixed token‑per‑batch design.

## Score and Decision

**Round‑1 bracket:** I first anchored in three bands: weak papers (score ~2.5–3.0); mid‑range (~4.67–6.50); strong papers (~8.0). The paper clearly sits above the weak band. The most topically relevant anchors in the mid band were *MoM* (5.50), *UltraMemV2* (6.50), *ParaRNN* (6.50, Oral), and *MesaNet* (6.50). The paper is stronger than *MoM* (which had parametric confounds) but weaker than *ParaRNN* (which trains 7B models with custom CUDA kernels and has far larger speedups).

**Round‑2 narrowing:** I retrieved anchors inside 5.5–7.0, finding *ParaRNN* (6.50), *MesaNet* (6.50), *Log‑Linear Attention* (6.67), and *MoM* (5.50). Comparing directly: TNT addresses a less‑explored problem (parallelizing *deep* memory modules specifically) and has a novel multi‑component solution, but its empirical coverage is narrower than any of these (one architecture, 150M scale, missing S_L ablation). It does not reach the scale or speedup magnitude of ParaRNN (6.50), but its contributions are arguably more novel than MoM (5.50). The best comparison is the *OOMB* paper (6.00), which also combined multiple known techniques into a coherent system with solid but not comprehensive evaluation. TNT has clearer novelty than OOMB.

**Final score:** 6.0. The paper makes a genuine contribution to an important problem, with well‑motivated architecture and convincing speedup results. However, the missing S_L ablation, single‑architecture validation, and lack of a Stage 2 control prevent the evaluation from being fully compelling. These gaps are addressable and do not threaten the core claims.

**Anchor listing:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| d1KbcYaWaE.md | 2.67 | 1 | Much weaker — unrelated DynMem memory module paper |
| HHsD970kdE.md | 3.00 | 1 | Much weaker — DreamState paper on RNN state editing |
| iiZy6xyVVE.md | 2.50 | 1 | Much weaker — Sleep/Memory Consolidation paper |
| cEyj6ewRFZ.md | 3.00 | 1 | Much weaker — ReNT nonparametric teaching paper |
| XOu5z16cbY.md | 4.80 | 1 | Weaker — Hierarchical memories for long‑tail knowledge, less innovation |
| 3PdOq8Rgue.md | 5.50 | 1,2 | Slightly weaker — MoM has thorough experiments but parametric confounds; TNT addresses a more fundamental bottleneck |
| QjyLNKm9mx.md | 4.67 | 1 | Weaker — Hierarchical Router for sparse attention, different problem |
| QWuXU0qNX0.md | 6.50 | 1 | Comparable but different — UltraMemV2 has massive scale but incremental novelty over prior memory layers |
| 248ysaRatx.md | 8.00 | 1 | Much stronger — Quantum RNN universality, different subfield |
| yRtgZ1K8hO.md | 8.00 | 1 | Much stronger — Polar Express optimization |
| oBXfPyi47m.md | 8.00 | 1 | Much stronger — RL paper with full‑scale experiments |
| VKGTGGcwl6.md | 8.00 | 1 | Much stronger — LLM conversation analysis, comprehensive evaluation |
| ZbfLR9NbNF.md | 6.50 | 2 | Stronger — Dynamic Chunking has full‑scale experiments up to 1.3B and thorough ablations |
| iHqdSQk6qc.md | 5.50 | 2 | Similar quality — Hierarchical sparse attention analysis, different focus |
| hxwV5EubAw.md | 5.00 | 2 | Slightly weaker — Hippoformer, less comprehensive evaluation |
| dSa3ImCQr7.md | 6.00 | 2 | Similar — OOMB training system, comparable completeness of evaluation |
| mX8b64iUaa.md | 6.50 | 2 | Stronger — ParaRNN parallelizes *any* non‑linear RNN, trains 7B models, 665× speedup, custom kernels |
| xa3OnTb6c3.md | 6.50 | 2 | Stronger — MesaNet has thorough theory, experiments up to 1B, comprehensive ablations |
| mOJgZWkXKW.md | 6.67 | 2 | Stronger — Log‑Linear Attention, thorough evaluation |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>