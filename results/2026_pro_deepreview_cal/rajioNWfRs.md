Now I have enough context to write the final review. Let me synthesize everything.

---

## Summary

TNT introduces a two-stage training framework for deep memory modules (e.g., Titans, TTT) that decouples training efficiency from inference performance. Stage 1 uses a hierarchical memory architecture — a global memory on large chunks paired with multiple local memories using periodic state resets — to enable massive context parallelism during pre-training. Stage 2 is a brief fine-tuning phase adapting local memories to smaller chunk sizes for high-quality inference. Evaluated on Titans at 150M parameters, TNT achieves up to 17× training speedup over the most accurate baseline while improving language modeling perplexity and downstream reasoning accuracy.

## Strengths

- **Novel hierarchical parallelization for non-linear RNNs**: The periodic state reset mechanism (Eq. 6) breaks sequential dependencies in local memories, enabling context parallelism for non-linear recurrences — a genuinely hard problem that prior work (chunkwise training, parallel scans) could not fully solve for deep memory modules. This is the paper's core technical innovation and is clearly motivated.

- **Convincing runtime scaling results**: Figure 4 demonstrates that TNT runtime remains nearly constant as sequence length grows from 2K to 32K, while Titans (C=16) exhibits quadratic growth. At 32K, TNT (C_L=128) is faster than FlashAttention — a strong empirical result for a JAX-native implementation without custom kernels.

- **Comprehensive ablation validates each design choice** (Table 3): Removing the global memory degrades PPL from 21.04 to 25.60; removing Q-K projection degrades to 22.01; adding Stage 2 fine-tuning improves to 20.86. Each component demonstrably matters.

- **Strong empirical performance against relevant baselines**: TNT Stage 2 {2,4,8,16} achieves 23.09 avg PPL vs. Titans' 25.07 (C=8) and outperforms Transformers without gating (23.58). The paper compares against a diverse set of baselines (Titans, TTT, DeltaNet, GatedDeltaNet, Transformers with/without gating, FlashAttention) — a stronger evaluation suite than typical for this sub-area.

- **Clear, well-structured problem formulation**: Section 3 identifies three concrete challenges, and Figure 2 provides direct empirical evidence of the chunksize sensitivity problem (PPL degrades from 13.78 to 36.45 when inference chunk size mismatches training). This gives the reader a crisp understanding of what the paper aims to solve.

## Weaknesses

### Fatal

None.

### Major

- **Multi-resolution local memory gains are not controlled for parameter count**. Table 2 shows consistent PPL improvement when scaling from 1 to 4 local memory modules (23.53 → 21.04 → 20.74 → 20.47 → 20.15 in Table 3), and the paper attributes this to multi-scale dynamics. However, each local memory module adds a fast-weight sub-network with its own parameters. The paper states models are "150M parameter" but never reports per-configuration counts or isolates the architectural benefit from the capacity increase. The diminishing returns (gaps of 0.30, 0.27, 0.32 PPL) suggest it is not purely capacity-driven, but the evidence would be substantially stronger with a capacity-controlled baseline (e.g., a single local memory with proportionally larger hidden dimensions).

- **Stage 2 fine-tuning lacks a vanilla Titans baseline**. The paper presents Stage 2 as the solution to Challenge 3 (chunksize mismatch), but only applies it to TNT models. It is not shown whether a standard Titans model pre-trained with a large chunk size could similarly benefit from fine-tuning at a smaller chunk size. If this works for vanilla Titans too, then Challenge 3 is solved by a general fine-tuning recipe rather than being specific to TNT. The two-stage framework remains valuable for training efficiency, but the claim that TNT *uniquely* resolves the train-test chunksize mismatch would need qualification.

- **Speedup-to-quality comparison uses training loss, not validation metrics**. Table 1 reports time to reach a fixed *training* loss of 3.20. The 17× speedup configuration (C_L={64}) is absent from Table 2's quality evaluation. While the speedup claim is credible and speedups at overlapping configurations ({8}: 7.68× with better PPL) do show simultaneous efficiency and quality gains, the headline 17× number is not directly tied to a validation-quality endpoint. Reporting time to reach a target validation perplexity would make the central claim more directly substantiated.

### Minor

- **Q-K projection overhead is not quantified**. Eq. 7 requires maintaining a d×d projection matrix and computing a matrix-vector product per retrieval. The paper states this is efficient (running sum, constant-size state), but provides no empirical measurement of the added cost relative to the baseline retrieval. For a 150M model with typical hidden dimensions (d ≈ 1024), a 1024×1024 outer product and matrix-vector multiply per token is non-trivial. A brief cost analysis or measurement would help assess practical scalability.

- **No sensitivity analysis for the reset period S_L**. The local memory reset period (S_L) controls the parallelism-accuracy trade-off: larger S_L gives more context but less parallelism. The paper uses S_L = 2048 or 4096 without exploring how this choice affects the trade-off or providing guidance for practitioners.

- **The "5% extra compute" for Stage 2 is stated without precise breakdown**. The paper says Stage 2 requires "only 5% of the original pre-training compute" and references Table 4, but Table 4 was stripped in the parser output. Clarifying what fraction of training tokens/steps this represents and whether it is genuinely cheaper than simply using smaller chunks in the final phase of Stage 1 would strengthen the presentation.

### Trivial

- The paper acknowledges that TNT does not match the Gated Transformer on perplexity (23.09 vs. 22.39) but dismisses the gap by arguing perplexity is "more stable" than downstream accuracy. This rhetorical move is slightly evasive; a straightforward acknowledgement of the remaining gap would read better.

## Nice-to-Haves

- Tie the speedup claims in Table 1 to a validation metric (e.g., time to reach a target validation perplexity) rather than training loss, and include the same TNT configurations that appear in Table 2.
- Add a capacity-controlled baseline for the multi-local-memory experiment to cleanly isolate the architectural benefit.
- Add a fine-tuning baseline for vanilla Titans (large chunk → small chunk) to determine whether Stage 2's benefit is TNT-specific.
- Explore sensitivity to the reset period S_L and provide practical guidance for setting it.
- Quantify the computational overhead of Q-K projection as model dimension scales.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "The speedup claims are decoupled from validation performance"** — Partially valid (see Major weakness), but the harsh critic's framing as a fatal "evidential gap that undercuts the paper's main message" overstates the issue. The {8} configuration appears in both Table 1 (7.68×) and Table 2 (PPL 24.10 vs. 25.07), so simultaneous speed+quality improvement IS demonstrated, just not at the maximal speedup point. Demoted from fatal to major.

- **Harsh Critic: "The training-speedup claims… the models used in the speedup table are not the same configurations whose end-task quality is reported in Table 2"** — Partially true but the overlap at C_L={8} exists. The paper could be clearer about which configurations overlap.

- **Strength Finder: "Model-agnostic design"** — The paper claims TNT is model-agnostic but only evaluates on Titans. This strength is partially aspirational; retained in a qualified form.

- **Harsh Critic: "the paper presents [Stage 2] as a conceptual contribution without a rigorous benchmark"** — The paper does benchmark Stage 2 in Table 2 (Stage 2 rows) and Table 3 ("w Stage 2"), so this criticism is factually incorrect. Removed.

- **Harsh Critic: cost analysis of Q-K projection as a critical issue** — Demoted to minor. The paper does describe the constant-size state property; the missing piece is empirical measurement, not conceptual gap.

- **Strength Finder: "Simultaneous gains in training speed and model quality… 17.37× speedup… while also delivering better perplexity (23.09 vs. 25.07)"** — These numbers come from different configurations. Kept the strength but qualified to note the configurations differ; removed the conflation.

- **Harsh Critic: Section 5.3 "perplexity is a more stable metric" is a "hand-wave"** — This is a stylistic critique, not a substantive error. Moved to Trivial.

## Novel Insights

The hierarchical memory with periodic state resets, combined with the observation that a brief fine-tuning stage can recover from the chunksize mismatch, represents a genuinely novel approach to the long-standing problem of parallelizing non-linear recurrences. The key insight — that you don't need to maintain sequential state across the entire sequence during training if you can recover fine-grained performance with minimal fine-tuning — could generalize beyond the Titans architecture studied here. It reframes the problem from "how do we parallelize non-linear recurrence" to "how much sequential dependency can we sacrifice during training and recover later," which is a productive conceptual shift.

## Suggestions

- The strongest path to strengthening the paper in rebuttal is adding parameter counts for each configuration in Table 2/3 and showing that the multi-resolution benefit persists after capacity normalization. Even a simple estimate would address the most significant methodological concern.
- If the authors can show (or argue convincingly) that fine-tuning a vanilla Titans model with a smaller chunk does *not* recover performance as well as TNT does, the Stage 2 contribution becomes much stronger. Even a small-scale experiment on this would help.
- Consider replacing the training-loss target in Table 1 with a validation-perplexity target for the overlapping configurations, or at minimum explicitly noting which Table 1 configurations correspond to which Table 2 rows.

## Score and Decision

### Anchor comparison

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| DEER (E34AlVLN0v) — parallelizing non-linear sequential models | 6.00 | R1 | TNT has far more comprehensive experiments (LM benchmarks, downstream tasks, ablation) and concrete architectural contributions. TNT > DEER. |
| minLSTM/minGRU (GrmFFxGnOR) — "Were RNNs All We Needed?" | 5.00 | R1 | TNT has much stronger evaluation, clearer novelty, and better empirical results. TNT >> minLSTM. |
| RetNet (UU9Icwbhin) | 4.75 | R1 | TNT's contributions are better motivated and more clearly validated. TNT > RetNet. |
| MELODI (TvGPP8i18S) — hierarchical memory compression | 6.25 | R2 | Similar hierarchical memory concept; TNT has better runtime analysis, downstream tasks, and clearer problem formulation. TNT > MELODI. |
| Zoology (LY3ukUANko) — recall in efficient LMs | 6.33 | R2 | Zoology has stronger theoretical analysis; TNT has more concrete architectural contribution and better speed results. Comparable quality. TNT ≈ Zoology. |
| Patch-Level Training (dDpB23VbVa) — two-stage training for LLMs | 7.50 | R2 | PT has larger-scale experiments (up to 2.7B), simpler idea, comprehensive ablations. TNT has more novel architecture but smaller scale (150M) and several methodological gaps. TNT < PT. |
| ReLU Strikes Back (osoWxY8q2E) — activation sparsity in LLMs | 7.33 | R2 | Has kernel-level optimizations and deployment analysis that TNT lacks. TNT < ReLU. |

**Round 1 bracket**: 5.0–8.0 (TNT clearly above the 5.0–6.0 band based on experimental comprehensiveness, clearly below the 7.5+ band based on scale and methodological gaps).

**Round 2 narrowing**: TNT is stronger than MELODI (6.25) and comparable to Zoology (6.33), but clearly weaker than Patch-Level Training (7.50) which has larger-scale experiments and tighter methodology. The paper lands at **6.5**: a solid contribution with real empirical gains and novel architecture, held back by parameter-count confounding in the multi-resolution experiments, missing fine-tuning baseline for vanilla Titans, and speedup claims tied to training loss rather than validation quality.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>