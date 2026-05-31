I've read the paper. Now let me verify a few more details and then run calibration.Round 1 bracket: between ~5 (ChunkKV) and ~8 (FlexPrefill). FlexPrefill is the most topically relevant. Let me read both to narrow.Round 1 bracket: between ~5 (ChunkKV) and ~8 (FlexPrefill). Now let me narrow.Let me read a couple of anchors that look closest to the paper's profile.I have enough calibration data. Let me now write the final review.

## Summary
QUOKA is a training-free, hardware-agnostic sparse-attention method for chunked prefill. The key idea is a two-step KV selection: (1) query subselection that retains queries with low cosine similarity to the mean query (claimed to attend broadly to keys), and (2) cosine-similarity scoring with pre-aggregation across GQA groups. The paper reports near-dense accuracy on RULER, LongBench, NIAH, and Math500 at ~12% KV budget, plus 3–7× speedups across A100, RTX 2080, and Xeon CPUs against a chunked-prefill dense baseline.

## Strengths
- **Large, consistent empirical gains over the prefill-aware baseline (SampleAttention).** Table 1 shows 86.71 vs. 78.25 at 4k Llama and 57.01 vs. 31.73 at 32k Llama, with similar gaps across five model families including MoE (Qwen3-30B-A3B) and NoPE (SmollM3, GPT-OSS-20B). The cross-family consistency is substantive evidence the method generalizes.
- **Near-dense accuracy at high sparsity on real long-context tasks.** Table 2 shows ≤3% accuracy drop at 25% KV budget across five models; Table 3 shows QUOKA at 0.945 normalized score on LongBench/Llama3.2-3B even at B_SA=512, where other methods drop to 0.70 or below.
- **Hardware portability with real measurements on three platforms.** Figure 5 reports speedups not just on A100 but on Intel Xeon W-2125 and RTX 2080. This portability is a direct, demonstrated consequence of using only `gather/topk/mean/CosSim` instead of custom kernels (Algorithm 1), and is unusually well-supported relative to competing sparse-attention papers that test only on a single GPU.
- **A small but real engineering insight in pre-aggregation.** Section 3.3 notes that under cosine normalization, averaging normalized queries across KV groups before forming the score matrix gives an identical result to per-group scoring followed by averaging, but saves a factor proportional to the number of GQA groups. This is correct and useful for practitioners.

## Weaknesses

### Fatal
None.

### Major
- **Theorem 1 does not actually justify the selection rule, and its symbol `q*` is undefined.** The statement uses `q*` in the conclusion but the premises are only about `q_0`, k, and M_Q. More importantly, the theorem proves that *if* a query attends strongly to k (β_q > 0) *and* M_Q is anti-aligned with k (α_q < 0), *then* CosSim(M_Q, q_0) is small — but the algorithm needs the converse: that small CosSim(M_Q, q) implies strong attention to some key. The α_q < 0 premise also bakes in much of the conclusion. The downstream design is supported only by Figure 2(c)'s correlation of 0.737 on a *single* (layer 0, head 11) of Llama3.2-3B. The fix is to either sharpen the theorem into a real statement justifying the rule or recast Section 3.1 as a clearly empirical/geometric heuristic; as written, it dresses an empirical observation as a derivation.
- **The "geometric observation" is shown on one head only.** Figure 2 is from Llama3.2-3B layer 0, head 11. Given that NoPE, MoE, and varied attention-head topologies are explicitly listed as a generalization contribution, an aggregate or per-head distribution of the (S_q, max_k A) correlation across the model families later evaluated is the version of this figure that supports the claim. Without that, the headline geometric story leans on one example while the algorithm runs on many.
- **Headline RULER comparison is partly against off-design baselines.** Section 2.4 and Section 5 acknowledge that SnapKV/Loki/SparQ/KeyDiff/LessIsMore are generation-time methods whose proxies degrade when averaged across queries in a chunk; reporting that SnapKV scores 29.15 on 4k Llama therefore confirms a thesis the paper already assumed. The single substantive prefill-aware comparison is against SampleAttention, where the gain is real (86.71 vs. 78.25 at 4k) but smaller than the apparent margins. The contribution would be more honestly framed if this asymmetry were stated rather than presented as a sweep.
- **No variance / multi-seed reporting on any benchmark.** This matters specifically because QUOKA on SmollM3 at B_SA ∈ {1024, 2048} scores 1.03 and 1.028 on LongBench (Table 3) — i.e., the sparse method beats dense attention at two adjacent budgets. Math500 (Section 4.4) also reports cases where QUOKA "surpasses dense attention." Either there is real variance in the normalization reference or the orderings are noise; without error bars the reader cannot tell. The pattern is plausibly explainable as regularization, but the paper does not address it.

### Minor
- **The query-selection rule is not isolated from the rest of the pipeline.** All comparisons are full-system (QUOKA vs. SampleAttention vs. SparQ). A controlled ablation that varies only the query-selection rule (random sampling, K-means medoids over Q, dot-product-to-M_Q, top-norm Q) with cosine-similarity scoring and aggregation held fixed would tell readers whether the gains come from the query-geometry observation or from the scoring/aggregation choices. The Section 4.5 ablations sweep budgets and chunk sizes but not the selection rule itself.
- **Latency story is fixed at `B_CP=128`.** Section 4.6 / Figure 5 are entirely at B_CP=128, which is precisely the small-chunk regime where the dense baseline pays the most per-chunk launch and KV-bandwidth overhead. A sweep over B_CP would let readers locate the regime where QUOKA's intrinsic sparsity speedup persists versus where the gap is amortizing chunked-prefill overhead the dense baseline incurs disproportionately.
- **Main-text content on Math500 is one paragraph deferring to Table 8.** Given that generation-time use is listed as a contribution and the abstract claims applicability beyond prefill, this is thinner than the contributions list implies.
- **NoPE/MoE generalization is asserted but not analyzed separately.** Including Qwen3-30B-A3B and GPT-OSS-20B in Table 1 demonstrates *that* QUOKA works on these architectures, but the geometric assumption underlying Section 3.1 is not specifically validated for NoPE (where positional information is absent and query distributions may behave differently).
- **Section 4 setup mixes two different cost knobs.** "QUOKA and SampleAttention subselect 16 queries; SparQ and LOKI down-project to 64 dimensions" controls different things; without iso-overhead accounting for the scoring function, the comparison is iso-B_SA but not iso-scoring-cost.

### Trivial
None retained.

## Nice-to-Haves
- A per-head/per-layer distribution of the (S_q, max_k A) correlation across Llama, Qwen, SmollM, and GPT-OSS, to upgrade Figure 2 from one example to a characterization.
- An ablation that swaps the query-selection rule alone, holding scoring and aggregation fixed.
- B_CP sweep on the latency figures.
- Bootstrap or multi-seed error bars on at least the cases where QUOKA exceeds the dense baseline.
- A negative-case analysis: heads or settings where the query-geometry assumption fails.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"NIAH Figure 4 dense baseline degrades at long context, which should be impossible under chunked prefill."** This claim relies on the auto-generated parser caption for the figure; the paper text in Section 4.1 makes no such claim about Full attention exceeding chunked-prefill Full. More importantly, model-level NIAH failure at long context (independent of chunked vs. non-chunked) is well documented for Llama3.2-3B, so the harsh critic's "this must be a bug" framing is too strong.
- **Generic "more datasets / more models" pushes.** The paper already evaluates on five model families and four benchmarks.
- **"Theorem 1 is structurally fatal."** Demoted to Major (not Fatal) because the algorithm and empirical results stand independently; the theorem is misleading rather than load-bearing.
- **Strength: "Theorem 1 provides a theoretical bound tying low CosSim(M_Q, q) to high attention weight, a property prior work did not exploit."** Dropped because the Major weakness above shows the bound does not actually establish that direction; the strength conflicts with a verified weakness.
- **Strength: "Max aggregation preserves rare but important interactions … Table 10 referenced in text."** Kept as supporting strength but the magnitude claim ("> 10%") comes from an appendix table not in the parsed text; treat as a soft strength.

## Novel Insights
The genuinely novel observation, which both reviewers agree on, is that *low-cosine-similarity-to-mean queries are the broadly-attending ones*, and that this geometric property can be used as a cheap, training-free signal for query subselection in multi-query prefill. The pre-aggregation equivalence under cosine-normalized inputs is a small but real efficiency observation. Neither reviewer surfaces an insight beyond what the paper itself claims.

## Suggestions
- Rewrite Section 3.1 honestly: either prove a converse statement that genuinely supports the selection rule (e.g., a probabilistic bound on expected attention mass under a generative model of Q and K conditional on CosSim with M_Q), or drop Theorem 1 and present the rule as an empirical/geometric heuristic.
- Replace the single-head Figure 2 with an aggregate distribution of the (S_q, max_k A) correlation across heads, layers, and the model families used in Table 1.
- Add a query-selection-only ablation that fixes the scoring/aggregation pipeline and varies only how the N_Q queries are picked.
- Reframe Table 1 to acknowledge that most baselines are off-design for prefill, and make the SampleAttention comparison the headline.
- Add error bars on benchmarks where QUOKA crosses the dense baseline; the SmollM3 0.945→1.03→1.028 trajectory deserves either an explanation or noise quantification.
- Sweep B_CP in the latency study to disentangle intrinsic sparsity gain from chunked-prefill amortization.

## Evaluation on Required Axes
- **Originality:** Moderate. The query-geometry observation and pre-aggregation trick are novel, but situated in a crowded sparse-attention literature.
- **Importance of the research question:** High. Chunked-prefill efficiency on heterogeneous hardware is a deployment bottleneck.
- **Claims well supported:** Mostly yes empirically; theoretically the central justification (Theorem 1) is shaky.
- **Soundness of experiments:** Reasonable scale and breadth, but lacking variance, baseline-design parity, and single-component ablation for the query-selection rule.
- **Clarity:** Adequate. Algorithm 1 is precise; Section 3.1 conflates empirical evidence with theory in a way that should be cleaned up.
- **Value to the research community:** Practitioner-relevant; the portability story and pre-aggregation observation are likely to be reused.

## Calibration

**Round 1 anchors (all retrieved):**
- `4QWPCTLq20.md` IntelLLM (3.0, weak): much weaker — narrow KV-compression, far less evaluation than QUOKA.
- `2DD4AXOAZ8.md` MixAttention (2.0, weak): minor architecture tweak, weaker empirics than QUOKA.
- `7DY2DFDT0T.md` EfficientSkip (2.5, weak): clearly weaker.
- `vw0NurJ7UX.md` PrefixQuant (3.0, weak): different topic; weaker.
- `uHkfU4TaPh.md` DynamicKV (4.4, mid): comparable problem, weaker empirics.
- `8sglLco8Ti.md` ChunkKV (5.25, mid, read): incremental novelty, missing latency stats — QUOKA clearly stronger on novelty and hardware breadth.
- `p7vJ3wsm34.md` KV-Distill (4.0, mid): requires training, weaker generality.
- `Q5VlpYRxGF.md` KVMerger (4.33, mid): similar tier as ChunkKV.
- `OfjIlbelrT.md` FlexPrefill (8.0, strong, read): closest prefill-sparse-attention analog; cleaner algorithmic derivation, fewer methodological gaps than QUOKA.
- `E4Fk3YuG56.md` Cut Cross-Entropy (8.5, strong): different topic.
- `OvoCm1gGhN.md` Differential Transformer (8.0, strong): different topic.
- `t7P5BUKcYv.md` MoE++ (8.0, strong): different topic.

**Round-1 bracket:** between ChunkKV (5.25) and FlexPrefill (8.0).

**Round 2 anchors:**
- `gkUyYcY1W9.md` SharedContextBench (6.5, accept): comparable evaluation breadth, different focus.
- `TrKRpaOk8y.md` LongGen / "A Little Goes a Long Way" (6.4, accept, read): comparable empirical strength, but requires training. QUOKA is similar in measured speedup magnitude and stronger in being training-free / cross-hardware.
- `VkqqZcofEu.md` Controlled Study (5.75, reject): study paper, different style.
- `6PmJoRfdaK.md` LongLoRA (7.0, accept): training-based, more polished — QUOKA below this.
- `lRTDMGYCpy.md` Critical KV (5.75, reject, read): incremental, missing baselines — QUOKA broader.
- `NcKUcd4EkA.md` Harnessing Query (5.25, reject): tangential.
- `UjSmUlUU6y.md` SimLayerKV (5.25, reject): less ambitious.
- `RtDok9eS3s.md` Simplifying Transformer (7.33, accept): different topic.
- `oDdzXQzP2F.md` Transformer-VQ (7.33, accept): more ambitious algorithmic novelty.
- `s3003xWtfd.md` CoreInfer (6.25, reject): similar tier.

**Narrowed bracket:** QUOKA is clearly above the 5.25–5.75 rejects (Critical KV, ChunkKV, SimLayerKV) due to broader hardware portability, stronger empirical gaps, and a more distinctive geometric observation. It is below FlexPrefill (8.0) and LongLoRA (7.0) due to Theorem 1's misleading framing, single-head motivation figure, and lack of variance reporting. It sits closest to LongGen (6.4) and SharedContextBench (6.5) — comparable empirical strength, similar polish, similar level of unresolved methodological concerns.

**Final placement:** Slightly below LongGen because LongGen's argumentation is more careful and the paper has fewer presentation issues; clearly above CoreInfer (6.25) on empirical strength and hardware portability.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>