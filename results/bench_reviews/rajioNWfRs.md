Now I have enough information to write the final consolidated review. Let me synthesize everything.

---

## Summary

This paper introduces TNT (Two-stage Non-linear Training), a framework that decouples training efficiency from inference quality in deep memory modules (e.g., Titans, TTT). TNT's Stage 1 uses a hierarchical memory design where a global module processes large, hardware-friendly chunks while multiple parallel local modules with periodic state resets enable context parallelism. Stage 2 adapts the local modules to smaller chunk sizes via lightweight fine-tuning. A Q-K Projection mechanism addresses the domain mismatch between key-based compression and query-based retrieval. Evaluated on a 150M-parameter Titans instantiation, TNT achieves up to 17.4× faster training to reach a target loss than the most accurate Titans baseline, while simultaneously improving perplexity.

## Strengths

- **Periodic resets + hierarchical memory is a genuinely clever solution to parallelizing non-linear recurrences.** Breaking sequential dependencies by resetting local memory states while compensating with a global memory is a principled and practical approach. The ablation (Table 3) confirms both components are necessary: removing global memory increases PPL from 21.04 to 25.60 (Section 5.4).

- **The Q-K Projection mechanism is well-motivated and empirically validated.** The paper identifies a real issue (key-based compression vs. query-based retrieval) and provides a clean solution whose removal in the ablation increases PPL from 21.04 to 22.01 and drops accuracy from 40.6% to 36.4% (Table 3, Section 5.4).

- **Clear identification and framing of the chunk-size trade-off.** The paper correctly identifies (Section 3, Challenge 3) that deep memory modules become over-specialized to their training chunk size, and that small-chunk inference cannot be freely substituted without performance degradation. Figure 2 illustrates this sensitivity clearly.

- **Comprehensive ablation isolating each component.** Table 3 separately evaluates hierarchical memory depth, global memory necessity, Q-K projection, and Stage 2 fine-tuning, providing clear evidence for each design choice.

- **Stage 2 is efficiently designed.** The fine-tuning phase requires only ~5% of pre-training compute (Table 4: 0.15–0.46 hours vs. 3–6 hours for Stage 1) while providing consistent improvements.

## Weaknesses

### Fatal
None.

### Major

- **Ablation baseline perplexity is inconsistent with main experiments, and the setup is underspecified.** The ablation study (Table 3) reports a Base Model (Titans) PPL of 23.53, but the main results (Section 5.3, line 542) state the best-performing Titans model achieves 25.07 PPL — a gap of ~1.5 PPL. The paper does not explain whether the ablation uses a different training budget, data mix, sequence length, or chunk configuration. This inconsistency undermines confidence in the ablation's quantitative comparisons, though the qualitative trends (each component helps) are likely robust.

- **Evaluation is limited to a single architecture (Titans) at a single scale (150M parameters / 10B tokens).** The paper claims TNT is "a general training paradigm applicable to any deep memory module" (Section 4, line 105) and "model-agnostic" (Section 5, line 452), yet the only instantiation tested is Titans. Applying TNT to TTT or Atlas would substantially strengthen the generality claim. Moreover, experiments at 150M parameters leave open the question of whether the efficiency gains hold at scales where practitioners would deploy these models (1B+ parameters, 100B+ tokens). Table 1 of the companion ParaRNN paper (accepted ICLR 2026 Oral), which tackles a similar problem, demonstrates training up to 7B parameters — a higher bar.

- **No comparison against modern efficient linear RNNs/SSMs (Mamba2, RWKV-7, GLA, DeltaNet).** The paper acknowledges these as "linear memory modules" in the related work but does not benchmark against them. Even though the paper's scope is deep memory modules, the headline claim of "remov[ing] a critical scalability barrier" and the speedup numbers (e.g., beating FlashAttention) invite comparison against the broader efficient sequence modeling landscape. Including even one or two representative linear RNN baselines under matched training conditions would greatly strengthen the paper by showing whether TNT's approach yields a favorable quality–speed trade-off relative to the fastest available alternatives. Without this, it is difficult to assess the practical significance of the contribution.

- **The 17× speedup headline is against an extreme operating point.** The claimed "up to 17.4× speedup" (Table 1) compares TNT CL={64} against Titans C=8 (19.48 hrs), which is the most accurate but also the slowest configuration. Against more practical Titans configurations (C=64, 4.18 hrs), the speedup drops to 4.67×, and against TTT (1.69 hrs) or the Gated Transformer with FlashAttention (0.96 hrs), TNT is slower on the time-to-quality metric in Table 1. Similarly, Table 4 shows that TNT Stage 1 (3.06 hrs for CL={8}) is slower than TTT (1.69 hrs) and Titans C=256 (1.99 hrs) for full training on 10B tokens. The abstract and conclusion should contextualize these numbers more honestly.

### Minor

- **Stage 2 fine-tuning provides only marginal improvements.** In Table 2, Stage 2 improves average PPL from 23.13 to 23.09 (Δ = 0.04). In the ablation (Table 3), from 21.04 to 20.86 (Δ = 0.18). While consistent, the gains are small enough to question whether the additional complexity and hyperparameter choices (chunk sizes, shard lengths) are justified, especially given the paper claims to "resolve" Challenge 3. A direct comparison against the simpler alternative — fine-tuning a standard (non-hierarchical) Titans model with smaller chunks — would help establish that the hierarchical architecture is the source of the benefit.

- **Q-K Projection overhead is not analyzed.** The projection matrix is d×d (d=768 for the 150M model, ~0.5M parameters). The paper claims it is "efficient" and describes a chunkwise implementation (Appendix C), but reports no wall-clock or memory overhead numbers. Since this matrix requires O(d²) storage per shard and a running sum of outer products, its cost at larger scales (e.g., d=4096 for a 1B model) could be non-trivial.

- **The FlashAttention comparison on TPUs is circumstantial.** The paper reports TNT (CL=128) is 1.3× faster than "FlashAttention (Pallas)" at sequence length 32K (Figure 4). This is a comparison of JAX/Pallas kernel implementations on TPUv4, not a fundamental architecture speed comparison. The paper appropriately labels the implementation but should more clearly caveat that optimized CUDA-based FlashAttention on GPUs would likely show different results. The linear scaling claim of TNT is valid in principle, but the empirical advantage over FlashAttention is specific to this hardware/software stack.

### Trivial
- The paper does not explicitly describe how the learnable initial state W_init is initialized or optimized. This is a detail that would help reproducibility.
- The evaluation does not report standard errors or confidence intervals for downstream task accuracy, which is known to be noisy at 150M scale across four commonsense reasoning benchmarks.

## Nice-to-Haves
- Apply TNT to a second deep memory architecture (e.g., TTT or Atlas) to demonstrate generality beyond Titans.
- Report training time to reach a fixed perplexity (e.g., 24.0 PPL) rather than a fixed loss, as loss-landing points may not correspond to equal model quality across architectures.
- Provide a synthetic analysis of TNT's effective memory horizon (how far back can the model retrieve information given the global chunk size and local shard length?).
- Include per-token latency and memory profiling for the Q-K projection at multiple scales.

## Removed Points

- **"TNT is an architecture not a training paradigm"** — Removed as overly semantic. The paper is transparent that its training paradigm involves architectural co-design (hierarchical memory, periodic resets). Many training paradigms in the literature involve specific architectural innovations, and the paper discusses applicability to other deep memory modules (Appendix D).
- **"Paper doesn't analyze effective memory horizon"** — Removed. The paper provides empirical validation through ablation studies that show both global and local components contribute. A formal analysis would be nice but is not required for the core contribution.
- **"Linear-runtime claim is invalid"** — Removed. TNT's runtime is theoretically linear (independent shards processed in parallel) and empirically demonstrated in Figure 4. The claim is sound.
- **"The comparison against FlashAttention is invalid on TPU"** — Removed. The paper labels "FlashAttention (Pallas)" transparently and compares implementations on the same hardware. The limitation is acknowledged by weakening this point in the Minor section above.
- **"Challenge 1 is not a technical problem"** — Removed. Identifying a practical bottleneck is a legitimate way to motivate a technical contribution.
- **"Paper doesn't compare against simpler baseline of fine-tuning standard Titans"** — Weakened from a standalone criticism to a suggestion in Stage 2 discussion above. The paper does compare against standard Titans with various chunk sizes; the specific "fine-tune standard Titans with small chunks" ablation would be a nice addition but its absence is not a fatal flaw.
- **"No discussion of limitations"** — Moved from a standalone weakness to implicit in the existing weaknesses. Many papers at this venue do not include explicit limitations sections.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any perspective not already present in the paper's framing and results.

## Suggestions

1. **Resolve the ablation inconsistency.** Explain why the Base Model (Titans) in Table 3 achieves 23.53 PPL while the main experiment (Table 2) reports 25.07 PPL. This is the most fixable and most important clarification for the next version.

2. **Add at least one modern linear RNN baseline** (e.g., Mamba2 or GLA) under matched training conditions. Even a single comparison would significantly strengthen the paper's claims about advancing the efficiency frontier.

3. **Scale to at least one larger model size** (e.g., 1B parameters) to demonstrate that the efficiency gains are not specific to small models. This is standard practice for papers targeting this venue's audience.

4. **Report wall-clock overhead for the Q-K Projection** at the current model scale, and discuss the O(d²) scaling concern for future larger models.

5. **Reconsider the headline speedup claim.** The "up to 17×" is technically accurate but gives a misleading impression when the speedup over practical Titans configurations is ~5× and TNT is slower than TTT and Gated Transformers. Qualify the claim more carefully in the abstract and conclusion.

6. **Apply TNT to at least one other deep memory module** (TTT would be the most natural choice given it is already used as a baseline) to support the "general paradigm" claim.

## Score and Decision

**Calibration Anchors** (all from ICLR 2026 human reviews):

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| **ParaRNN** (mX8b64iUaa, Accept Oral) | 6.50 | Trains 7B nonlinear RNNs with strong baselines (Mamba2) and open-source code. TNT is weaker on scale and baseline coverage. |
| **MesaNet** (xa3OnTb6c3, Accept Poster) | 6.50 | Thorough experiments up to 1B, compares against many RNN baselines. TNT has similar technical depth but narrower evaluation. |
| **Smooth Reading** (GoaWSQWtOE, Accept Poster) | 5.00 | Also missing SSM baselines, accepted despite this. TNT has a stronger technical contribution but similar evaluation gaps. |
| **Lattice** (12jdbVQ7t0, Reject) | 5.20 | Strong results but rejected due to limited novelty/evaluation. TNT is more novel but has comparable evaluation shortcomings. |
| **Hierarchical Memories** (XOu5z16cbY, Accept Poster) | 4.80 | Accepted despite being somewhat incremental. TNT has a similar evaluation profile. |
| **Weak Expert Ensemble** (YGZdVl454O, Reject) | 3.00 | Fundamentally flawed methodology. TNT is significantly stronger than this. |

**Judgment**: Relative to the anchors, TNT has a genuine technical contribution that is stronger than Lattice (rejected) and roughly on par with Hierarchical Memories (accepted) and Smooth Reading (accepted). However, the unexplained ablation inconsistency (23.53 vs 25.07 PPL for the same baseline), the complete absence of any linear RNN baseline, and evaluation at only 150M parameters are between them more concerning than the gaps in those accepted papers. The core ideas are solid, but the experimental validation has material weaknesses that prevent acceptance in the current form.

**Score**: 4.5

**Decision**: Reject

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>