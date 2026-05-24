Now I have all the information needed to produce the final consolidated review.

---

## Summary
QUOKA is a training-free, hardware-agnostic sparse attention method designed for chunked prefill during LLM inference. It accelerates attention by (1) retaining a small subset of "informative" queries (those with low cosine similarity to the mean query) and (2) subselecting keys based on their cosine similarity to those retained queries, using max-aggregation across queries and mean-aggregation across GQA heads. Evaluated across six model families on long-context retrieval and reasoning benchmarks (NIAH, RULER, LongBench, Math500), QUOKA achieves near-baseline accuracy while using 88% fewer KV pairs per attention evaluation, and delivers up to 5× attention speedup and 3× TTFT reduction on enterprise GPUs, with speedups extending to CPUs and consumer GPUs.

## Strengths
- **Comprehensive and compelling empirical results:** On RULER (Table 1), QUOKA outperforms all competing sparse attention methods by 10–20% absolute across five model families and sequence lengths up to 32k at a budget of 1024. On LongBench (Table 3), it maintains relative scores ≥0.945 even at a budget of only 512 tokens, far exceeding competitors. On NIAH (Figure 4), QUOKA preserves retrieval accuracy across document lengths and needle depths where other sparse methods degrade sharply. This breadth and consistency across benchmarks is a genuine strength.

- **Hardware-agnostic design with demonstrated latency gains across platforms:** The algorithm uses only standard linear-algebra primitives (cosine similarity, top-k, gather), requiring no custom kernels or training. Figure 5 demonstrates that this portability translates to real speedups: up to 5× attention-module speedup and 3× TTFT reduction on Nvidia A100, up to 7× speedup on Intel Xeon CPU, and 5–6× speedup on Nvidia RTX 2080 consumer GPU. This is rare among sparse attention papers, most of which show speedups on only one platform.

- **Broad architectural generalization:** The evaluation spans Llama3.2, Qwen2.5, Qwen3-4B, Qwen3-30B-A3B (MoE), SmolLM3, and GPT-OSS-20B — covering RoPE, NoPE, MoE, and GQA variants. QUOKA achieves the highest scores among sparse baselines in every setting (Tables 1–3), providing strong evidence of general applicability.

- **Graceful degradation under sparsity:** Accuracy decreases smoothly as the selective budget shrinks (Tables 3, 5, 6), with less than 3% performance drop when using under 12% of original tokens. This robustness allows practitioners to tune the method for diverse hardware constraints.

- **Clear algorithm and integration with existing kernels:** Algorithm 1 is concisely described, and the method feeds reduced KV sets into standard dense attention kernels (e.g., FlashAttention), making it straightforward to deploy.

## Weaknesses

### Fatal
None.

### Major
None. While there are real issues (below), none undermine the paper's core empirical contribution.

### Minor
- **Theorem 1 has undefined notation and a weak link to the method's central claim.** The theorem introduces variable \(q^*\) in the conclusion (Eq. 5) that is never defined in the premises (which only mention \(q_0\)). The paper claims the theorem formalizes the observation that "queries with lower cosine similarity to the mean query attend to the majority of keys," but the theorem relates only to the existence of a *single* key \(k\) with certain cosine values, not to breadth of attention across keys. The empirical evidence in Figure 2 is from a single head (layer 0, head 11) of one model (Llama3.2-3B), showing correlation between \(S_q\) and \(\max_k(A)\) — maximum attention to a single key, not the number of keys attended to. The method still works well empirically (the ablation in Table 12 validates the design), but the theoretical framing is overstated relative to the evidence presented. This weakens the conceptual narrative and makes the approach appear less well-motivated than its empirical results suggest.

- **Latency evaluation is restricted to a single small model.** All speedup measurements (Figure 5, Section 4.6) use Qwen3-4B, a 4B-parameter model. The paper showcases accuracy on much larger models (Qwen3-30B-A3B, GPT-OSS-20B) but does not report latency scaling behavior for them. The claim of universal hardware-agnostic speedup would be strengthened by including at least one larger model in the latency experiments, particularly since memory-bandwidth interactions differ at larger scales.

- **Baselines could be more fairly adapted to the chunked prefill setting.** The compared methods (SparQ, Loki, LessIsMore) were originally designed for single-query decode. The paper uses them with naive query-averaging for multi-query chunked prefill, which the paper itself notes degrades their performance. While the paper's claim that QUOKA better suits prefill is well motivated, some of QUOKA's margin may partly reflect the comparison setup. A brief experiment adapting one strong baseline (e.g., SampleAttention) to use the same max-aggregation strategy that QUOKA employs would strengthen the comparison.

### Trivial
- The asymptotic complexity of QUOKA is stated as "sub-quadratic" in the main text but the precise bound is deferred to Appendix C. A concise statement (e.g., \(O(B_{SA} \cdot d)\) vs. \(O(T^2 d)\)) in the main text would improve motivation.

## Nice-to-Haves
- A discussion of failure modes or conditions where QUOKA might underperform (e.g., extremely structured prompts, tasks requiring uniform attention across all tokens) would help practitioners.
- Extending latency measurements to at least one larger model (e.g., the 30B-active MoE model) would solidify the generality claim.
- Investigating whether QUOKA's occasional LongBench scores above 1.0 (Table 3, SmolLM3 at budgets 1024 and 2048) reflect noise, regularization effects, or chunked prefill artifacts would be informative.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **From Harsh Critic — "Missing discussion of failure modes"**: Moved to Nice-to-Haves. The paper evaluates on diverse benchmarks and the method's limitations are not critical to evaluating the contribution.
- **From Harsh Critic — "Math500 table not shown in main body"**: The table is referenced as Table 8; the absence from the extracted text is an artifact of appendix stripping by the parser. The original submission includes it.
- **From Harsh Critic — "Asymptotic complexity analysis deferred to appendix"**: Retained as Trivial since the paper does state sub-quadratic complexity in the main text, but a more precise statement would help.
- **From Strength Finder — Generic strengths about problem importance**: Removed as generic/superficial (e.g., "the problem is important" — not a concrete contribution of this paper).
- **From Harsh Critic — Demands for fairness analysis that are speculative**: The claim that baselines could be adapted is kept as a minor weakness, but the speculative suggestion that QUOKA's margins are "partly an artifact" without evidence is toned down.

## Novel Insights
The paper's observation that queries with low cosine similarity to the mean query carry the most influential attention signal is conceptually interesting and leads to an elegant two-stage selection mechanism (query subselection → key subselection). While the theoretical formalization is underdeveloped, the geometric intuition — that outlier queries, rather than average queries, should drive KV selection — represents a genuine insight for the sparse attention literature. The pre-aggregation trick for GQA (averaging normalized queries across KV groups before scoring, exploiting linearity of the mean and outer product) is a clean efficiency contribution that costs almost nothing but yields a factor-of-KV-groups reduction in scoring cost.

## Suggestions
- Clean up Theorem 1: either define \(q^*\) explicitly (likely \(q^* = q_0\)) or replace the theorem with a more modest statement about what is actually shown. The method's empirical strength does not require a theorem to justify it.
- Add a latency measurement for at least one larger model (Qwen3-30B-A3B or similar) to support the claim of scaling efficiency.
- Consider a short experiment where one baseline (e.g., SampleAttention) is given QUOKA's max-aggregation or query subselection module to isolate which components drive the gains.

## Score and Decision

**Anchor comparison summary:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| EfficientSkip | 2.50 | 1 | Far weaker — trains sparse variants from dense, limited evaluation |
| IntelLLM | 3.00 | 1 | Far weaker — KV cache compression with narrow scope |
| LazyLLM | 5.00 | 1 | Weaker — dynamic token pruning, less comprehensive evaluation |
| SwiftKV | 5.50 | 1 | Weaker — requires training, single model family, missing end-to-end results |
| HiP | 6.25 | 2 | Weaker — hierarchical pruning, limited model variety, less comprehensive benchmarks |
| HShare | 6.80 | 2 | Weaker — KV sharing for decoding, narrower evaluation, presentation issues |
| StreamingLLM | 7.50 | 2 | Comparable — influential insight (attention sink), but narrower benchmarks and weaker baselines; QUOKA has more comprehensive evaluation and clearer latency results |
| FlexPrefill | 8.00 | 1/2 | Comparable — both training-free sparse attention for prefill; FlexPrefill has a more novel mechanism, but QUOKA has more comprehensive evaluation (6 model families vs. 4, 4 benchmarks vs. 2, 3 hardware platforms vs. 1), better latency characterization |

**Round 1 bracket:** Based on comparison with FlexPrefill (8.0) and SwiftKV/HiP (~5.5-6.25), QUOKA plausibly falls in the **6.5–8.0** range.

**Round 2 narrowing:** Comparison with StreamingLLM (7.50) and FlexPrefill (8.00) places QUOKA at approximately **7.5**. QUOKA is empirically stronger than StreamingLLM (broader model families, more benchmarks, multi-hardware latency) but has a less cleanly articulated core insight. It is roughly comparable to FlexPrefill in contribution level — simpler method, stronger empirical validation — but the confusing Theorem 1 and single-model latency evaluation pull it slightly below the clean 8.0 of FlexPrefill.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>