Now I have a solid calibration picture. Let me write the full review.

**Round 1 bracket**: The paper clearly sits in the (3.5, 7.5) band. It is far stronger than the weak-band papers (avg 1.0–3.33) which had fundamental flaws (incremental novelty over strong prior art, unclear methodology, missing baselines). It is also clearly not in the 7.5+ band (oral-level papers on RL with world models, foundation models).

**Round 2 narrowing**: I examined anchors at 4.50 (MeSH, Accept), 4.67 (Memory Caching, Reject), 4.80 (Pretraining w/ hierarchical memories, Accept), 5.00 (Smooth Reading, Accept), and 5.50 (MoM, Accept). The TNT paper's technical contribution (periodic resets enabling context parallelism) is more novel than Smooth Reading's multi-round inference and the hierarchical memory pretraining paper. Its parameter-documentation gap is similar to MoM's issue (~17% parameter difference), except MoM at least quantified the difference in the appendix. The speed claims are slightly overstated (17× vs slowest baseline) but the core speedup is real. Overall, TNT sits between Smooth Reading (5.00) and MoM (5.50) — I'd place it at 5.0.

---

## Summary

This paper proposes TNT, a two-stage training framework for deep memory modules (e.g., Titans, TTT) that decouples training throughput from inference accuracy. Stage 1 uses a hierarchical memory architecture: a global memory processes large hardware-friendly chunks for long-range context, while multiple parallel local memories with periodic state resets handle fine-grained details — the resets break sequential dependencies and enable context parallelism. Stage 2 is a brief fine-tuning phase that adapts local memory modules to smaller inference-time chunk sizes. The paper reports up to 17× training speedup over baseline Titans while also improving perplexity and downstream accuracy.

## Strengths

1. **Periodic state resets as a mechanism for context parallelism in non-linear recurrences is genuinely novel.** The key insight — breaking long-range sequential dependencies in non-linear recurrent modules by periodically resetting local memory states to a learned initial state — is clean, well-motivated, and directly addresses a known bottleneck. Equation 6 formalizes this concisely, and the approach is architecturally simple enough to be applicable across deep memory module families (Titans, TTT).

2. **Comprehensive ablation study validates each design choice.** Table 3 systematically isolates the contribution of each component: adding local memories improves perplexity from 23.53 (Baseline Titans) to 20.15 (4 local modules); removing the global memory degrades PPL to 25.60; removing Q-K projection increases PPL from 21.04 to 22.01; Stage 2 fine-tuning further improves PPL to 20.86 and accuracy to 40.9%. This provides clear evidence that every proposed component contributes meaningfully.

3. **Linear runtime scaling with sequence length is convincingly demonstrated.** Figure 4 shows TNT's runtime remaining nearly flat (~400–550ms) as sequence length grows from 2K to 32K, while Titans (C=16) scales from ~400ms to ~4000ms. At 32K, TNT (C_L=128) is faster than even FlashAttention (~550ms vs ~1000ms). This scaling behavior is the core efficiency claim and is well-supported.

4. **Two-stage decoupling of training efficiency from inference quality is practically valuable.** Stage 1 uses large chunks for throughput, then Stage 2 adapts to small chunks with only 5% additional compute. Table 2 shows Stage 2 consistently improves over Stage 1 across all configurations, validating the practical utility of this decoupling.

## Weaknesses

### Major

1. **No explanation of how parameter counts are equated between TNT and baseline Titans.** The paper states "We train 150M parameter models following (Behrouz et al., 2025d)" and labels all models as "150M parameters" in Tables 1–2. However, TNT adds architectural components that the baseline Titans lack: a global memory module with its own fast-weight sub-network, multiple local memory modules (up to 4), Q-K projection matrices, and a learnable reset state W_init. The paper provides no explanation of how the total parameter count stays constant despite these additions — e.g., whether the hidden dimension, number of layers, or slow-weight network sizes were reduced to compensate. This is a documentation gap that prevents the reader from determining whether TNT's quality gains (PPL 23.13 vs 25.07) come from the proposed training paradigm or simply from increased model capacity. The paper should provide a parameter-count breakdown for each variant (as MoM did for its 17% diff) or at minimum state the architectural trade-offs explicitly.

2. **The 17× speedup headline is against the slowest baseline and conflates architectural changes with training improvements.** The claimed 17.37× speedup (Table 1) compares TNT (C_L=64, 1.12 hrs) to Titans (C=8, 19.48 hrs) — the *slowest* Titan configuration. The most natural comparison, TNT vs Titans at matched chunk sizes, shows more modest speedups (e.g., C=16: 1.65 hrs vs 10.79 hrs = 6.5×; C=64: 1.12 hrs vs 4.18 hrs = 3.7×). Additionally, part of TNT's speed advantage comes from the hierarchical architecture itself (parallel local memories + global memory with large chunks), not from a training *technique* that could be applied to a standard single-memory Titan. The paper should separate architectural efficiency gains from training-protocol gains, e.g., by testing whether two-stage training alone (without hierarchical memory) improves baseline Titans.

3. **Stage 2 fine-tuning details are insufficiently documented.** The paper does not specify: (a) how Stage 2 models are initialized from Stage 1 models (e.g., does TNT Stage 2 with C_L={1} start from the Stage 1 model with C_L={8} or from scratch?); (b) which parameters are updated during fine-tuning (all parameters or only local memory sub-networks?); (c) the number of fine-tuning steps and learning rate schedule. Table 4 is referenced for training time but was stripped in parsing (appendix issue). These details are essential for reproducibility.

### Minor

1. **Limited evidence that TNT generalizes beyond Titans.** The paper claims TNT is "model-agnostic" and applicable to "any deep memory module," but all experiments instantiate it only with Titans. TTT and DeltaNet appear only as baselines in Table 2, not as models to which TNT was applied. A single additional instantiation (e.g., TNT applied to TTT) would substantiate the generality claim.

2. **No error bars or statistical significance.** Perplexity and accuracy metrics are reported without variance across runs. Given the modest model scale (150M) and the known variance in downstream task accuracy (the paper itself notes "higher variance" for downstream tasks), confidence intervals or multi-seed results would strengthen the evidence.

3. **"Q-K Projection" terminology is slightly imprecise.** Equation 7 computes Σ(k_t k_t^T / ||k_t||^2) q_t — a Gram-matrix-weighted query, not a projection onto a subspace in the strict linear-algebra sense unless the keys are orthogonal. The mechanism is still reasonable and the ablation confirms its usefulness, but the mathematical framing should be clarified.

### Trivial

- None beyond the points already listed.

## Nice-to-Haves
- A parameter-count breakdown table for all model variants.
- An experiment applying TNT to at least one other deep memory architecture (e.g., TTT).
- Analysis of how W_init is learned, whether it is shared across shards, and whether gradients flow through reset boundaries during training.
- Discussion of the memory overhead of the running-sum Q-K projection (d×d matrix per local memory) for large d.

## Removed Points

The following weaknesses from the harsh critic were removed or demoted after verification against the paper:

- **"The paper does not discuss how W_init is learned"** → The paper states W_init is "learned" (Section 4.1.1, line 158). The precise training mechanics (gradient flow through resets) are implementation details that a conference paper can reasonably omit, though the paper would benefit from a brief clarification. Demoted from critical to nice-to-have.

- **"Q-K projection is not a projection in the linear algebra sense"** → The formula computes a weighted sum of key outer products applied to the query. For normalized keys (which the paper notes is common), this is Σ k_t k_t^T q_t, which is indeed in the span of the keys. The critic's concern about orthogonality is overly pedantic for the intended heuristic use. Kept as Minor #3 in softened form.

- **"The paper does not explain WHY inference performance degrades when chunk size changes"** → The paper identifies this as Challenge 3 with empirical evidence (Figure 2). The mechanism is that the model over-specializes to the training chunk resolution. A deeper analysis would be nice but is not required to motivate the solution (Stage 2 fine-tuning).

- **"Missing Table 4 / appendix content"** → Known parser artifact; the original submission contains these.

- **"Speedup over Transformers is limited"** → The paper acknowledges this explicitly ("our implementation does not yet outperform highly optimized baselines like the Gated Transformer with FlashAttention") and explains it's due to lack of custom kernels. This is a fair limitation, not a weakness in the evaluation.

- **"The paper does not demonstrate context parallelism across devices"** → This is a desirable extension but beyond the stated scope (the paper focuses on single-accelerator throughput via context parallelism within a device).

- **"The 17× number is against a baseline that also lacks custom kernels"** → This is a feature, not a bug: it shows the speedup is algorithmic, not engineering-driven.

## Novel Insights

The periodic reset mechanism for enabling context parallelism in non-linear recurrent modules is the paper's most striking idea. Most prior work on parallelizing recurrences has focused on linear RNNs (where parallel scans apply) or on architectural approximations; the direct approach of simply resetting the state and using a global memory to retain context has been overlooked. The empirical finding that this reset-based local memory, combined with a global memory for long-range context, produces a net *improvement* in quality despite losing cross-shard memory is interesting — it suggests that for deep memory modules, fine-grained local modeling may matter more than continuous state propagation for next-token prediction. The Q-K projection addresses a subtle but real distribution mismatch (training the memory to compress key→value but querying with q_t), and the ablation confirms this effect is non-trivial (~1 PPL point). The two-stage decoupling is practically valuable: it shows that brief fine-tuning at smaller chunk sizes (C'_L = {1} or {2,4}) can recover and even surpass performance lost from training at larger chunks, with only 5% additional compute.

## Suggestions

1. **Provide a parameter-count breakdown.** Add a table or paragraph showing how the 150M parameter count is distributed across components in each TNT variant compared to baseline Titans. If the hidden dimension or number of layers was reduced to accommodate added memory modules, state this explicitly. If the fast-weight sub-networks are shared or parameter-efficient, describe how.

2. **Add a two-stage baseline without hierarchical memory.** Run an experiment where a standard single-memory Titan is pre-trained with large chunks and fine-tuned with small chunks (without adding global memory or Q-K projection). This would isolate the contribution of the training schedule from the architectural changes.

3. **Report TNT applied to at least one additional deep memory architecture** (e.g., TTT) to substantiate the model-agnostic claim.

4. **Add error bars or multi-seed results** for at least the main perplexity and accuracy metrics.

5. **Clarify Stage 2 fine-tuning protocol** — which parameters are updated, how models are initialized, number of steps, and learning rate schedule.

6. **Frame the 17× speedup more carefully** in the abstract and introduction (e.g., "up to 17× faster than the slowest, most-accurate baseline configuration; 4.7× faster than the same-chunk-size baseline").

## Score and Decision

**Calibration Anchors (all rounds):**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| Coupling Attention and Memory (d1KbcYaWaE) | 2.67 | 1 | Much weaker — unclear theoretical grounding, asymmetric evaluation settings. TNT's contribution is far clearer. |
| Artificial Hippocampus Networks (UUW0DHqs4f) | 2.50 | 1 | Weaker — incremental over prior hybrid attention-RNN work, missing key comparisons. TNT has stronger novelty. |
| MeSH (IhTrFvY7p3) | 4.50 | 1,2 | Comparable contribution level. MeSH had a 0-score reviewer outlier but was accepted. TNT has cleaner experimental design but similar documentation gaps. |
| Memory Caching (R3EJ2IjgOI) | 4.67 | 2 | Rejected — GRM variant had worst-case quadratic complexity that undermined the core efficiency claim. TNT does not have a comparable fatal flaw. |
| Pretraining w/ hierarchical memories (XOu5z16cbY) | 4.80 | 1,2 | Similar in contribution level. That paper was accepted despite a static retriever and weak RAG baseline. TNT has clearer technical novelty. |
| Smooth Reading (GoaWSQWtOE) | 5.00 | 2 | Comparable. Smooth Reading was seen as incremental over existing compression methods but had solid experiments. TNT has stronger architectural novelty. |
| MoM (3PdOq8Rgue) | 5.50 | 1,2 | Slightly stronger. MoM had a similar parameter-count concern (~17% diff) but quantified it and provided equal-parameter ablations in the appendix. TNT should follow this example. |

**Round-1 bracket**: 3.5–7.5 (clearly above weak-band papers, clearly below oral-level papers).  
**Round-2 narrowing**: Compared against anchors at 4.50–5.50. TNT sits between Smooth Reading (5.00) and MoM (5.50) — the technical contribution is more novel than Smooth Reading, but the documentation gaps (parameter count, fine-tuning details, lack of second architecture instantiation) prevent it from reaching MoM's level of empirical rigor.

**Final score**: 5.0.

The paper introduces a genuinely clever idea (periodic resets for context parallelism in non-linear recurrences) and supports it with a well-designed ablation study and convincing runtime scaling results. The main weaknesses are documentation gaps (parameter-count equality, Stage 2 fine-tuning protocol) and a slightly overstated speedup headline — all addressable in a revision. The core contribution is solid enough to warrant acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>