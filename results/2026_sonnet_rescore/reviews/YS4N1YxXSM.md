## Summary

QUOKA is a training-free, hardware-agnostic sparse attention algorithm for chunked prefill that selects representative queries based on cosine dissimilarity to the mean query, then subselects the KV pairs most aligned with those queries. By leveraging the geometric observation that low-cosine-similarity queries attend to the broadest set of keys, QUOKA reduces the active KV budget dramatically while preserving accuracy. Evaluation across six model families on NIAH, RULER, LongBench, and Math500 demonstrates clear accuracy advantages over competing sparse methods (10–20 pp on RULER at 32k) alongside multi-hardware latency gains of 3–7×.

---

## Strengths

- **Dramatic accuracy advantage on long-context benchmarks (verified in Tables 1–3):** On RULER at 32k with B_SA = 1024, QUOKA scores 57.01 on Llama 3.2-3B while the best competitor (SampleAttention) reaches 31.73 — a 25-point gap that is too large to attribute to tuning or cherry-picking. The margin holds across all five model families in Table 1 (10–20 pp in every column), and Table 2 shows QUOKA at 25% budget stays within ~2 pp of full attention at 32k.

- **Substantial, multi-hardware end-to-end speedups (verified in Fig. 5 and Section 4.6):** 5× standalone attention speedup and 3× TTFT on A100, 5–6× on RTX 2080, and up to 7× on Intel Xeon CPU. The gains are measured end-to-end (TTFT) and at the module level, and QUOKA outperforms or matches all sparse competitors on each platform.

- **Ablation-backed algorithmic design (referenced in Sections 3.2–3.3 and Section 4.5):** The use of cosine similarity over dot product is justified by >10% RULER improvement (Table 9); max aggregation over queries is justified by both the heavy-tailed query deviation distribution (Figure 3) and a direct ablation (Table 10). The pre-aggregation trick for GQA is both mathematically justified and efficiency-critical. These are not post-hoc choices.

- **Generalization across architectures and constraints:** Results span dense, MoE (Qwen3-30B-A3B), and NoPE (GPT-OSS) architectures. The ablation (Table 11, referenced in Section 4.5) shows stable performance across varying B_CP, demonstrating robustness in resource-constrained environments.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Theorem 1 is one-directional and overclaimed (Section 3.1).** The paper writes "This can be formalized through the following theorem" before presenting Theorem 1, implying the theorem justifies the query-selection mechanism. But the theorem proves the *forward* direction: if a query strongly attends to a key *and* the mean query has negative cosine similarity with that key (α_q < 0), then the query will have high S_q. What the method actually requires is the *reverse*: that selecting queries with high S_q is sufficient to capture queries that dominate attention. This reverse direction is not shown. Moreover, the condition α_q < 0 is restrictive; keys that are moderately aligned with the mean query direction (α_q ≥ 0) — plausibly common in later layers — fall outside the theorem's coverage. The empirical evidence (Figures 2b, 2c) is the actual support for the design choice, and the paper would be more credible by presenting the theorem as illustrating a consistent case rather than formalizing correctness.

- **Core motivating correlation shown for a single head and layer (Figure 2):** The scatter plot in Figure 2c (r = 0.737) is from Llama 3.2-3B-Instruct, layer 0, head 11 only. Layer 0 is often atypical (strong positional/syntactic structure), and a correlation of 0.737 for one case does not establish that the principle holds broadly. Whether this correlation is consistent across middle and late layers, across all six tested models, and at different sequence lengths is never shown. Given that this observation is the paper's stated motivating premise ("we observe that queries with lower cosine similarity to the mean query interact more strongly with more keys"), grounding it in a single example weakens the foundation.

- **Scores above dense baseline unreported for noise (Table 3, Section 4.4):** SmolLM3 entries in Table 3 show normalized scores of 1.030 and 1.028 at B_SA ∈ {1024, 2048}. The paper and conclusion highlight "in some cases surpasses dense attention" as a contribution. However, these normalized values are task-averages, and with enough tasks, sampling noise can push averages above 1.0 without a real effect. The paper provides no variance estimate, confidence interval, or task-level breakdown to distinguish a real improvement from noise. Reporting scores above 1.0 as supporting evidence without such analysis is at minimum misleading.

- **Inconsistent baseline sets across tables (Tables 1 vs. 3):** Table 1 (RULER) includes SnapKV, KeyDif, and LoLi — three methods absent from Table 3 (LongBench) and from the stated baseline list in Section 4. No explanation is provided for the asymmetry. LoLi is competitive with QUOKA on Qwen2.5 at 32k in Table 1 (34.12 vs. 59.37) — a meaningful gap but readers cannot assess the full competitive landscape from Table 3 alone.

### Trivial

- The abstract states "88% fewer key-value pairs" without specifying the context length at which this figure applies (it corresponds to B_SA = 1024 at ~8192 tokens; at 32k the retention rate is ~3%). This is not wrong but is underspecified.

---

## Nice-to-Haves

- **Extend motivating analysis across layers and models.** A targeted supplement showing how the correlation between S_q and max_k(A) varies across early, middle, and late layers, and across at least two model families, would either validate or qualify the generality of the core claim. Either result would be scientifically useful.

- **Characterize the break-even sequence length.** The paper does not identify the minimum sequence length at which QUOKA's pre-selection overhead is offset by KV selection savings. A simple measured curve or theoretical estimate would help practitioners decide when to deploy QUOKA.

- **State the operating-point difference between Tables 1 and 2 explicitly.** Table 1 uses B_SA = 1024 (fixed), while Table 2 uses 25% of cache length. At 32k, 25% gives B_SA ≈ 8192 vs. 1024 — these are radically different regimes. A sentence noting this would avoid confusion.

- **Latency for one model only.** Section 4.6 measures latency only on Qwen3-4B. Reporting speedup for one additional model (e.g., Llama 3.2-3B) would strengthen generalizability of the efficiency claims.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"QUOKA exceeds full attention" is described as a parser artifact.** The harsh critic notes Figure 4 as-parsed shows "Full (c) showing lower accuracy than QUOKA" — this is a PDF parsing artifact, not a paper error. Removed.

- **Comparison tables missing extra methods favors QUOKA.** The presence of SnapKV, KeyDif, and LoLi in Table 1 but not Table 3 is flagged above as a Minor weakness. However, the harsh critic's framing that LoLi is "competitive" at 4k (74.84 vs. 86.71) misweights the comparison — QUOKA is still clearly better at 4k, and LoLi degrades severely at longer contexts (8.05 at 32k vs. 57.01). The competitive framing is overstated; the weakness retained above is only about presentation transparency.

- **Claims about reproducibility (hyperparameters, source code).** The paper explicitly documents all hyperparameters and notes simplicity of implementation. Removed per hard rules.

- **Strength Finder generic claims.** "The paper addresses an important problem" and "training-free is a contribution" dropped as insufficiently specific to this paper. The specific retained strengths above are anchored to concrete data points.

---

## Novel Insights

The most genuinely novel insight in this work is the *direction* of query-geometry utilization for multi-query KV selection: rather than aggregating all query information symmetrically (as prior methods do), QUOKA identifies that queries *far from the mean* are informationally decisive — they interact with the broadest set of keys — while near-mean queries are redundant. This transforms the multi-query aggregation problem from "how to average fairly across queries" to "which queries carry the most signal," an asymmetric reformulation that has not been applied in the chunked prefill setting. The pre-aggregation trick (averaging normalized queries across GQA groups before scoring keys, rather than after) is a clean implementation insight that reduces the scoring cost by a factor equal to the number of KV groups, making the approach practical for modern GQA architectures without additional overheads.

---

## Suggestions

1. Revise the framing of Theorem 1: state explicitly that it establishes a sufficient condition (high β_q and negative α_q imply high S_q) but that the design relies on empirical evidence for the converse. This is a one-sentence fix that makes the theoretical section more credible.
2. Add a cross-layer / cross-model analysis of the S_q–max_k(A) correlation, even if brief (a small table with Spearman r values at layers 0, 12, last-1 for two models would suffice).
3. For the scores-above-1.0 in Table 3 and Math500: add task-level standard deviation or flag them as within-noise explicitly rather than claiming they demonstrate superiority to full attention.
4. Unify the baseline set across Tables 1 and 3, or add a footnote explaining why SnapKV/KeyDif/LoLi were excluded from LongBench.

---

## Score and Decision

**Originality:** The core idea — exploiting query-mean cosine dissimilarity to identify informationally dominant queries in chunked prefill — is novel and not a direct application of prior work. **4/5**

**Importance:** Prefill latency in resource-constrained settings is a real and pressing bottleneck. The multi-hardware scope amplifies practical relevance. **4/5**

**Claims supported:** Main accuracy and latency claims are well-supported by extensive experiments across 6 models and 3 hardware platforms. Minor issues with the theoretical claim (Theorem 1 direction) and one unexplained result (scores > 1.0). **4/5**

**Soundness:** Method design is algorithmically clean and ablation-justified. Theorem 1 has a real gap in scope/direction but does not affect experimental validity. **4/5**

**Clarity:** Generally clear, with some presentation inconsistencies (baseline asymmetry, operating-point ambiguity between tables). **3/5**

**Community value:** Directly applicable to practical LLM deployment across diverse hardware with large performance margins. High utility for the inference optimization community. **4/5**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>