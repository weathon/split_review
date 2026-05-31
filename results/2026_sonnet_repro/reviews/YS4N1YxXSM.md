Now let me run the calibration search to anchor the score.Round 1 bracket: **6.0 to 8.0**. QUOKA is stronger than the 6.0 cascading KV cache paper (more rigorous baselines, RULER + LongBench evaluation) but needs to be compared against FlexPrefill-type papers (8.0). Let me narrow further.Now I have enough calibration to write the final review. Let me synthesize.

**Round 1 bracket: 6.0–8.0**
**Round 2 anchors: Selective Attention (6.75), HeadKV (6.5), Cascading KV (6.0), FlexPrefill (8.0)**

QUOKA is better validated than the 6.0–6.75 papers (more hardware platforms, more baselines, more benchmarks, larger empirical margins). FlexPrefill (8.0) requires custom CUDA kernels; QUOKA's hardware-agnostic design is a genuine advantage, but QUOKA's theoretical support (Theorem 1) overclaims and the motivating empirical observation rests on a single layer/head example. **Final bracket: 6.5–7.5; score → 7.0.**

---

## Summary

QUOKA is a training-free, hardware-agnostic sparse attention method targeting chunked prefill. Its core insight is that queries with low cosine similarity to the mean query disproportionately drive attention over most keys, so retaining only those outlier queries (and then selecting the keys most aligned with them via cosine similarity) yields an accurate, highly compressed KV set. Evaluated across NIAH, RULER, LongBench, and Math500 on six model families and three hardware platforms, QUOKA substantially outperforms existing sparse attention baselines while achieving meaningful end-to-end latency reductions.

---

## Strengths

1. **Large, consistent empirical margins on RULER**: At $B_\text{SA} = 1024$, QUOKA scores 57.01 on Llama 3.2-3B at 32k vs. 31.73 for the best competing method (SampleAttention, Table 1). Across all five models and all context lengths (4k–32k), QUOKA leads by 10–20 absolute points, a margin too large to attribute to hyperparameter tuning.

2. **Near-dense accuracy at 25% budget**: Table 2 shows that under a constant 25% KV budget, QUOKA degrades by ≤2 absolute RULER points across all six models and all context lengths up to 32k, validating the core claim that the method closely approximates full attention.

3. **Multi-hardware latency validation**: Figure 5 reports up to 5× standalone attention speedup on an A100, 5–6× on an RTX 2080, and up to 7× on an Intel Xeon CPU—demonstrating that the hardware-agnostic design delivers real-world benefits on platforms where custom CUDA kernels cannot be used.

4. **Ablation-backed design choices**: Cosine similarity scoring outperforms dot-product by ≥10% on RULER (Table 9), and max-aggregation over queries outperforms mean-aggregation (Table 10), providing targeted justification for each algorithmic component.

5. **Pre-aggregation efficiency trick**: The paper correctly identifies that normalizing queries before GQA-head averaging makes mean-over-heads equal to the outer product of the pre-averaged query with keys (Section 3.3 / Algorithm 1 lines 6–8), reducing computation by a factor proportional to the number of KV groups—a clean optimization.

---

## Weaknesses

### Fatal

None.

### Major

1. **Theorem 1 proves the wrong direction for the method's purpose (Section 3.1).** The paper presents Theorem 1 as formally justifying query subselection: "this can be formalized through the following theorem." However, the theorem proves: *if* $q_0$ strongly attends to $k$ (large $\beta_q$) *and* the mean query is anti-correlated with $k$ (i.e., $\alpha_q < 0$), *then* $q_0$ has high $S_q$. The method actually requires the *converse*—that selecting high-$S_q$ queries suffices to capture all strongly-attending queries. No such guarantee is given. Furthermore, the precondition $\alpha_q < 0$ excludes keys that are moderately or positively aligned with the mean query direction, which is a non-trivial restriction. The paper should (a) correctly state the theorem's scope (it covers a class of cases rather than the general case), (b) not present it as a formal justification of the full method, and (c) acknowledge that the general-case support is empirical.

2. **The core motivating empirical observation is documented for a single layer and head (Figure 2c).** The Spearman correlation $r = 0.737$ between $S_q$ and $\max_k(A)$ is reported for Llama 3.2-3B-Instruct, layer 0, head 11 only. Layer 0 is atypical in most transformers (dominated by positional encoding effects), and a single head at one model is not representative evidence for "queries with lower cosine similarity to the mean query attend to the majority of keys" as a general claim. Whether this correlation holds across middle/late layers, across the six tested models, and at different sequence lengths is essential for validating the design principle and is unaddressed. This is the weakest point in an otherwise evidence-heavy paper—the theoretical story rests on two exhibits (Figure 2b and 2c) that would need to be substantially broadened to support the generality claimed.

### Minor

3. **Scores above 1.0 in Table 3 and Math500 are unexplained.** QUOKA reports normalized LongBench scores of 1.030 and 1.028 on Smollm3 at $B_\text{SA} \in \{1024, 2048\}$, and the abstract/conclusion cite "surpassing dense attention" as a strength. A method that retains a strict subset of KV pairs cannot systematically exceed full attention. The paper offers no variance analysis (e.g., confidence intervals across LongBench tasks) to determine whether these above-1.0 scores are statistically significant or simply noise from the normalization-and-average procedure. Either a noise analysis or a mechanistic explanation is needed; without one, presenting these scores as evidence of QUOKA's strength is misleading.

4. **Inconsistent baseline sets across tables (Tables 1 and 3).** Table 1 (RULER) includes SnapKV, KeyDif, and LoLi alongside the four baselines stated in Section 4; Table 3 (LongBench) includes only those four. No explanation is given for the omission. LoLi is competitive in some Table 1 settings (e.g., 74.84 vs. QUOKA's 86.71 on Llama3.2 at 4k), and its absence from LongBench prevents a complete picture.

### Trivial

5. **Notation gap in Theorem 1**: $q^*$ appears in Equation (5) and the subsequent discussion without explicit definition in the main text. From context it refers to the query that strongly attends to $k$, but this should be stated outright.

6. **Abstract anchors "88% fewer KV pairs" to a specific sequence length without stating it.** This figure corresponds to $B_\text{SA} = 1024$ at 8192 tokens (12.5% retention); at 32k tokens (the main evaluation length), retention is ~3%. The claim is not wrong, but it should specify the corresponding context length to be fully informative.

---

## Nice-to-Haves

- A small targeted analysis of how the $S_q$–$\max_k(A)$ correlation varies across layers (early, middle, late) and across the tested model families would meaningfully strengthen the theoretical story and would be directly actionable.
- Characterizing the break-even sequence length at which QUOKA's pre-selection overhead is offset by attention savings would help practitioners decide when to deploy it, especially on edge devices.
- Table 2 uses a 25% budget (B_SA ≈ 8192 at 32k) while Table 1 uses B_SA = 1024. A note linking these operating points would help readers interpret the two tables together.
- Latency is reported for Qwen3-4B only; showing a second model would improve generalizability of the efficiency claim.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"NIAH caption shows Full performing worse than QUOKA (Figure 4)"** — The paper text confirms this is a parser artifact. The figure description is machine-generated from an image caption; the underlying figure is consistent with QUOKA approximating dense attention. Not a real paper flaw.

- **Abstract "88% fewer KV pairs" omits sequence length** — Retained as a trivial weakness above, but the harsh critic's framing of this as substantively misleading is overstated. The abstract is describing a summary statistic; this is a precision suggestion, not a real flaw.

- **"Table 2 and Table 1 are incomparable without statement"** — The paper does explicitly state the two settings separately ("We also simulated $B_\text{SA}$ growing with the KV cache to maintain a constant compression ratio"), so the difference is disclosed. Retained as a nice-to-have presentation suggestion.

- **Pre-aggregation trick correctness questioned** — The harsh critic verified this is mathematically correct and raised no substantive concern. The paper's derivation is sound.

- **$B_\text{CP} = 128$ amplifies relative benefit** — The paper explicitly frames this as a "resource-constrained scenario" and provides ablations over $B_\text{CP}$ (Table 11). The experimental context is clearly stated; this is not a hidden inflation.

- **Strength Finder claim about QUOKA "surpassing dense attention" as a strength** — Removed per hard rule: conflicts with verified weakness (W3) showing these scores are unexplained and likely noise.

---

## Novel Insights

The observation that query geometry—specifically, angular distance from the mean query—predicts which queries dominate attention over most keys is the paper's most distinctive contribution. Prior sparse attention for prefill either treats all queries homogeneously (SampleAttention) or is designed for single-query decode. QUOKA's two-stage funnel (identify outlier queries → select keys aligned with those queries) is a principled departure from both families. The pre-aggregation trick that equates mean-over-normalized-queries with mean-over-cosine-similarities is a clean efficiency gain. What remains under-explored—and would be genuinely novel to establish—is whether the outlier-query geometry is a consistent architectural feature across layers and model families, or a phenomenon that happens to hold in the layers where long-context retrieval is most active.

---

## Suggestions

1. **Correct the framing of Theorem 1**: Replace "this can be formalized through the following theorem" with language that accurately conveys the theorem's scope (sufficient condition under $\alpha_q < 0$). Add one sentence noting that the general effectiveness relies on the empirical correlation in Figure 2c, which motivates a broader analysis across layers.

2. **Broaden Figure 2c**: Show the $S_q$–$\max_k(A)$ correlation for a grid of (layer, head) pairs—at minimum early, middle, and late layers for Llama 3.2-3B and one Qwen model. If the correlation is robust, this strengthens every claim in the paper. If it degrades in later layers, the paper should acknowledge where the method relies on empirical observation rather than the geometric principle.

3. **Address the above-1.0 LongBench scores**: Either (a) report per-task standard deviations to show the gap is within noise, or (b) acknowledge that the LongBench normalization-and-average procedure has variance that can produce scores slightly above 1.0, and remove the "surpassing dense attention" framing.

4. **Reconcile Table 1 and Table 3 baselines**: Explain in the caption or text why SnapKV, KeyDif, and LoLi appear in Table 1 but not Table 3. If they were excluded due to inapplicability at LongBench lengths, state this explicitly.

---

## Score Calibration

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| IntelLLM (KV cache compression) | 3.0 | R1 | Much weaker: limited contribution, no latency evaluation |
| EfficientSkip | 2.5 | R1 | Much weaker: rejected, sparse LLM training, not inference |
| Cascading KV Cache | 6.0 | R1/R2 | Weaker: single hardware, fewer baselines, weaker theory |
| OmniKV | 6.0 | R2 | Weaker: no multi-hardware, narrower evaluation |
| HeadKV | 6.5 | R2 | Comparable depth; QUOKA has more hardware breadth and larger margins |
| Selective Attention | 6.75 | R2 | Weaker empirical breadth (no RULER/NIAH), requires training data |
| FlexPrefill | 8.0 | R1 | Comparable but requires custom CUDA kernels; QUOKA more portable; QUOKA's theoretical weaknesses offset portability advantage |

**Round 1 bracket**: 6.0–8.0.
**Round 2 narrowing**: QUOKA is clearly above the 6.0–6.75 cluster (better baselines, more hardware, larger margins, hardware-agnostic). Compared to FlexPrefill (8.0), QUOKA's portability advantage is offset by the theory overclaiming (Theorem 1 direction) and the single-data-point motivating observation. The net sits in the upper-middle of the bracket.

**Final score: 7.0**. Decision: **Accept**.

The method is original within its scope (chunked prefill KV selection), the research question (efficient prefill under hardware constraints) is practically important, the claims are largely well-supported by strong empirical results, the experiments are sound and multi-hardware, the writing is clear, and the contribution to the community (a training-free hardware-agnostic alternative to custom-kernel sparse attention) is real. The theoretical framing should be corrected and the motivating observation should be broadened, but neither issue invalidates the core contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>