Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper proposes TNT (Two-stage Non-linear Training), a training framework for deep memory modules (e.g., Titans, TTT) that decouples training efficiency from inference performance. The key ideas are: (1) a hierarchical memory architecture where a global memory processes large chunks for long-range context while multiple parallel local memories handle fine-grained details with periodic state resets to enable context parallelism; (2) a Q-K projection mechanism to address the compression–retrieval domain mismatch; and (3) a two-stage process where Stage 1 maximizes throughput and Stage 2 fine-tunes with smaller chunk sizes for inference-quality. Experiments on 150M-parameter Titans models show up to 17.37× training speedup with improved accuracy over Titans baselines, and linear runtime scaling that outperforms FlashAttention at 32K context.

## Strengths

- **Up to 17.37× training speedup with simultaneous accuracy improvements (Table 1, Table 2):** TNT (C_L=64) reaches the target loss 17.37× faster than the best Titans baseline (C=8), while also achieving lower perplexity (23.13 vs. 25.07) and higher commonsense reasoning accuracy (41.0% vs. 39.0%) on 150M-parameter models trained on 10B tokens. This directly validates the central claim of decoupling efficiency from performance.

- **Periodic state reset mechanism enabling context parallelism for non-linear recurrences (Eq. 6, Section 4.1.1):** The paper introduces a learned initial state W_init with periodic resets every S_L tokens, breaking the long-standing sequential dependency in non-linear RNNs. This is a genuine algorithmic innovation: prior chunkwise methods (e.g., Titans' chunkwise training) still carry state between chunks, whereas TNT allows fully independent processing of sequence shards. The linear runtime scaling in Figure 4 confirms this parallelism is practically realized.

- **Q-K projection resolving compression–retrieval mismatch (Section 4.1.2, Eq. 7, Table 3):** The paper identifies a real issue: during compression the memory function f(W, ·) maps keys → values, but during retrieval it is queried with q_t. The proposed projection onto the subspace of observed keys is a theoretically motivated fix, and the ablation (Table 3) shows removal increases perplexity from 21.04 to 22.01, confirming its practical importance.

- **Thorough ablation study (Table 3):** Each component (hierarchical memory, global memory, Q-K projection, Stage 2 fine-tuning) is individually tested. The ~21.7% PPL degradation when removing the global memory convincingly demonstrates that the global module is essential for long-range context, not just a capacity increase.

- **Linear runtime scaling at long contexts (Figure 4):** TNT (C_L=128) runs in ~550ms at 32K sequence length, compared to ~1000ms for FlashAttention and ~4000ms for Titans (C=16). This demonstrates that the hierarchical design yields more than theoretical linearity — it produces better wall-clock time than highly engineered attention kernels at scale.

## Weaknesses

### Fatal
None.

### Major

- **The claim of being a "general training paradigm" is unsubstantiated; TNT is evaluated on only one architecture.** The paper claims TNT is "a general training paradigm applicable to any deep memory module rather than a specific architecture" (Section 1, p.1) and the abstract states "Evaluated on Titans and TTT models." However, Section 5.1 reveals TTT is only used as a baseline, not as a TNT instantiation: "While TNT is model-agnostic, we instantiate it with a strong deep memory model, Titans" (line 209). The hierarchical memory design (global + local modules, periodic resets, Q-K projection) involves specific architectural components that may not transfer trivially to other deep memory architectures like TTT or Atlas without significant modification. **This is the paper's most significant weakness** — the core claim of generality is asserted but not demonstrated. The contribution is best framed as a new architecture for Titans, not a general paradigm.

- **No control for model capacity in comparisons.** TNT introduces additional parameters (a global memory module V, multiple local memory modules, and the learnable W_init state) compared to the baseline Titans, which uses a single memory module. The paper does not control for parameter count, hidden dimension, or FLOPs. As noted in Table 2, TNT Stage 1 with C_L={4,8,16,32} achieves 23.13 PPL vs. Titans C=8 at 25.07 PPL, but the TNT model has strictly more components. The reported accuracy improvements could partly reflect increased capacity rather than the efficacy of the two-stage training paradigm. A controlled comparison (e.g., increasing Titans' hidden dimension to match TNT's parameter count) is needed to isolate the contribution of the training approach itself.

- **Stage 2 fine-tuning procedure is underspecified.** The paper describes Stage 2 as adapting "only the local memory modules to a smaller, high-resolution chunksize" (Section 4.2). However, comparing Stage 1 and Stage 2 configurations in Table 2 reveals different numbers of local modules and different chunk-size sets (e.g., Stage 1: {4,8,16,32}, Stage 2: {2,4,8,16}). It is unclear whether the Stage 2 models are derived by fine-tuning a specific Stage 1 checkpoint, whether local modules are re-initialized, or whether the hierarchical configuration is changed and then re-trained. The paper states "an additional 5% of the original pre-training compute" but does not specify the exact procedure (learning rates, number of steps, which parameters are frozen/thawed). This makes the Stage 2 results difficult to reproduce or attribute.

### Minor

- **Runtime breakdown is missing.** Figure 4 shows impressive scaling but does not decompose wall-clock time into global memory, local memory, and Q-K projection contributions. Since the global memory requires sequential updates across its large chunks (C_G=2048), a detailed breakdown would clarify where the parallelism advantage actually comes from. Without this, it is difficult to assess whether the speedup is driven by local memory parallelism, the larger global chunk size, or both.

- **Experiments are conducted at only one model scale (150M parameters).** While this is standard for proof-of-concept, the scalability claims would be stronger with evidence at larger sizes (e.g., 1B+). The linear runtime scaling advantage is most relevant at large model scales and long sequences.

### Trivial
- The 1.3× speedup claim over FlashAttention in the text (Section 5.2) is actually conservative relative to the ~1.82× suggested by Figure 4's table values (1000ms / 550ms). This is the opposite of an error — the paper undersells itself — but the discrepancy should be reconciled.

## Nice-to-Haves
- Applying TNT to a second deep memory architecture (e.g., TTT or Atlas) to substantiate the "general paradigm" claim.
- A diagram or explanation showing how TNT distributes work across devices versus standard chunkwise training.
- Qualitative analysis showing that the global memory captures long-range dependencies and local memories capture fine-grained patterns (e.g., via attention/retrieval visualizations).
- Ablation on the segment length S_L — the reset period is a critical hyperparameter that controls the parallelism vs. context coherence trade-off, but it is never varied.

## Removed Points
*These points were flagged for removal but are included here in case they are useful.*

- **"Architecture not training paradigm" (from Harsh Critic #1):** The paper's framing as a "training paradigm" is indeed an overclaim given only one architecture is demonstrated. This is retained as the first Major weakness above, but the sharp distinction between "architecture change" and "training paradigm" is itself somewhat artificial — many training innovations (dropout, batch normalization, layer-wise adaptive learning rates) also alter model structure. The substantive concern (generality unproven) is what matters.
- **Runtime scaling claims unsupported (Harsh Critic #2, about 1.3× vs 1.82×):** The paper claims TNT is "1.3× faster than FlashAttention" while Figure 4 suggests ~1.82×. This is the paper being conservative, not erroneous — the claimed speedup is *less* than what the data shows. This does not undermine any claim; it undersells the result. Retained only as a Trivial note for internal consistency.
- **Q-K Projection is a heuristic with no theoretical justification (Harsh Critic #4):** The paper provides clear theoretical motivation (Challenge 2, Eqs. 1-2) that during compression f(W, k_t) is trained on keys, but retrieval uses q_t, which may lie outside the learned key domain. The ablation confirms its importance. The critic's alternative explanation ("increased model capacity") is speculative and unsupported. **Removed.**
- **Criticism about missing related work, appendix content, unreleased code, or formatting/typo issues:** These were filtered per instructions.

## Novel Insights

The periodic reset mechanism (Eq. 6) is the paper's most interesting innovation. By resetting local memory states to a shared learned initial state W_init at segment boundaries, TNT breaks the sequential dependency that has historically prevented parallelization of non-linear RNNs. This is conceptually different from prior parallelization approaches: chunkwise methods (used in Titans, TTT) still carry state between chunks, while linear RNNs (Mamba, Mamba-2) rely on the associative property of linear recurrences. TNT's approach is to accept that local context is lost at reset boundaries and compensate with a separate global memory — a clean architectural division of labor. The resulting ability to process sequence shards as independent batch items is what produces the observed linear scaling. This design choice means the trade-off between parallelism (large S_L) and local context coherence (small S_L) is now an explicit, tunable knob rather than a fixed architectural constraint.

## Suggestions

1. Reframe the contribution: position TNT as a *hierarchical memory architecture for deep memory modules* rather than a "general training paradigm." This is more accurate and avoids overclaiming.
2. Add a parameter/FLOPs-matched comparison: increase the baseline Titans' hidden dimension to match TNT's parameter count and compare performance.
3. Clarify the Stage 2 fine-tuning protocol: specify which Stage 1 checkpoint each Stage 2 model starts from, whether modules are re-initialized, learning rates, and exact number of steps.
4. Provide a runtime breakdown showing wall-clock time contributions of global memory, local memory (parallel + overhead), and Q-K projection separately.
5. Reconcile the 1.3× speedup claim with the plotted data for internal consistency, even if the paper is being conservative.

## Score and Decision

**Calibration anchors (from corpus search):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `E34AlVLN0v.md` (Parallelizing non-linear sequential models) | 6.00 | Similar scope — both tackle parallelism for non-linear RNNs. TNT has stronger empirical evaluation (accuracy + speed vs. just speed) but less theoretical rigor. Comparable quality. |
| `GrmFFxGnOR.md` (Were RNNs All We Needed?) | 5.00 | TNT has more extensive experiments and clearer novelty than this paper, which was criticized for limited dataset scope and prior-art overlap. TNT is stronger. |
| `AL1fq05o7H.md` (Mamba) | 6.25 | Mamba had a cleaner story and larger-scale experiments. TNT is narrower in architecture focus but has similarly clean empirical validation. Slightly lower than Mamba's avg. |
| `s1kyHkdTmi.md` (Evolved Universal Transformer Memory) | 7.00 | Stronger paper with cleaner experiments and broader validation across modalities. TNT is below this anchor. |
| `TvGPP8i18S.md` (MELODI) | 6.25 | Similar hierarchical memory architecture paper. Comparable evaluation depth. TNT has similar quality. |
| `cZWCjan02B.md` (Flash Inference) | 6.83 | Strong algorithm paper with rigorous analysis. TNT has stronger end-to-end results but weaker theoretical framing. |
| `JOBokGDcX0.md` (Overlapped Chunks) | 2.50 | Much weaker paper. TNT is clearly well above this. |

Comparing across these anchors: TNT sits in the 5.5–6.5 band. It has genuine contributions (periodic reset mechanism, hierarchical design for deep memory), solid empirical support (up to 17× speedup with quality improvements), and thorough ablations. Its main limitations are framing overclaims (generality unsubstantiated, no parameter-controlled comparison) that are addressable but non-trivial. This places it around the level of the DEER paper (6.00) and below Mamba (6.25) and Flash Inference (6.83).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>