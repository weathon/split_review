Now I have enough information to write the consolidated review. Let me compile my findings.

**Verification of key critic claims against the paper:**

1. **"Contradictory description"** — The critic claims Figure 2(b) says "key heads are halved" contradicts "equal cache." Looking at Figure 2(a) (RoPE): 2 query heads, 2 key heads. Figure 2(b) (EC): 4 query heads, 2 key heads. The key heads are *the same* as RoPE (2), so KV cache *is* equal. The caption's "halved" refers to halved relative to what MHA would expect for 4 query heads — it's an artifact of using a GQA schematic. No actual contradiction. The "QKV parameter budget" / W_o point: QKV = W_q, W_k, W_v (these are fixed). W_o is a separate output projection. The critic conflates them. **Remove as a major weakness; demote to minor presentation issue.**

2. **"Failure to control for parameter count"** — Valid concern: EC's W_o is double-sized. This is a real confound. However, the paper provides mitigating evidence: (a) the EH configuration (same W_o as RoPE, halved QKV) performs comparably or better than RoPE, and (b) the noise perturbation experiment (Figure 5) directly attributes the gain to imaginary attention. **Keep as minor-moderate weakness, not fatal.**

3. **"Long-context evaluation limited to synthetic benchmarks"** — Valid but standard. Many top papers use RULER/BABILong. **Keep as minor weakness.**

4. **"EC efficiency not evaluated"** — Valid. Only EH's efficiency is measured. **Keep as minor weakness.**

Now let me also assess the strength finder's claims more carefully:

- Strength 1 (identifying discarded imaginary component): Valid, backed by equations 1-2 in the paper.
- Strength 2 (noise perturbation experiment): Valid, Figure 5 and Section 5.2 provide direct evidence.
- Strength 3 (strong long-context gains): Valid. Table 2 shows substantial gains at 376M (18.8→25.0 RULER avg).
- Strength 4 (cache-efficient EH): Valid. Figure 4 shows clear memory and throughput benefits.
- Strength 5 (theoretical justification): Valid. Section 3.2 derives the sine integral characteristic.
- Others: All valid and specific to the paper.

Let me also check what the critic said about "Figure 1 decomposition equation is misleading." The paper's Figure 1 shows an equation. Let me check the text... The paper says the equation is in the figure caption. The figure shows a decomposition of q_t k_s^T. The critic says it writes it as a complex sum but RoPE computes a real-valued dot product. But this is actually the mathematical derivation - the paper is showing the complex form that leads to both real and imaginary parts. This is correct. Remove this criticism.

Now let me write the final review.

---

Summary of score reasoning:

The paper identifies a genuine gap in RoPE (discarded imaginary component), provides clean theoretical analysis, proposes two practical configurations, and validates with extensive experiments (two model sizes, ~10 benchmarks, noise perturbation experiment). The core weaknesses are: (1) the EC configuration adds W_o parameters creating a confound, (2) long-context evaluation uses only synthetic benchmarks, (3) EC efficiency not measured, (4) figure caption ambiguity. None are fatal.

Compared to calibration anchors:
- "Scaling Laws of RoPE-based Extrapolation" (5.0): weaker empirical work
- "Wavelet-based Positional Representation" (5.25): weaker novelty and results
- "Round and Round We Go!" (6.2): comparable novelty, less experimentation
- "STRING" (6.5): comparable contribution, different approach
- "CLEX" (6.5): comparable method paper

The paper sits at 6.5 — a solid accept.## Summary

This paper identifies that standard implementations of Rotary Position Embeddings (RoPE) for LLMs discard the imaginary component of the complex-valued attention score, and proposes **RoPE++**, which re-incorporates this component as a parallel group of "imaginary attention" heads. The authors provide theoretical analysis showing that imaginary attention has a slower-decaying characteristic curve (sine integral vs. cosine integral), making it better suited for long-context dependencies. Two configurations are introduced: **RoPE++_EH** (keeps total head count, halves KV cache and QKV parameters) and **RoPE++_EC** (keeps KV cache size, doubles attention heads with a larger output projection). Experiments at 376M and 776M scales across short-context (11 tasks) and long-context (RULER, BABILong, up to 64k) benchmarks show consistent improvements, with a particularly compelling noise-perturbation experiment (Figure 5) directly attributing long-context gains to the imaginary heads.

## Strengths

- **Identifies a genuine and overlooked information loss in RoPE**: The paper mathematically pinpoints that standard RoPE discards the imaginary component of the complex-valued dot product (Equation 1 vs. Equation 2), and derives a clean recovery mechanism. This is a novel contribution — prior work on RoPE improvements has focused on interpolation, base scaling, and data-awareness, but not on recovering this discarded signal. (Section 3, Equations 1–2)

- **Theoretical analysis shows why imaginary attention captures longer dependencies**: Section 3.2 derives the characteristic curve of imaginary attention as a sine integral (Equation 5), and Figure 1 illustrates that it decays more slowly than real attention's cosine integral. This provides a principled explanation for why the imaginary component is valuable for long-context modeling, beyond just empirical observation.

- **Noise perturbation experiment provides direct causal evidence**: In Section 5.2, adding Gaussian noise to imaginary attention degrades RULER-4k scores by ~5 points (376M) and ~8 points (776M) more than identical noise applied to real attention (Figure 5e, 5j). This is the strongest piece of evidence in the paper — it directly attributes the functional role in long-context modeling to the imaginary heads, not to confounding factors.

- **Strong and consistent empirical gains on long-context benchmarks**: At 376M, RoPE++_EC achieves 25.0 average RULER vs. 18.8 for RoPE (+6.2), and 16.1 BABILong vs. 11.0 (+5.1) (Table 2). At 776M, gains are smaller but still positive (29.4 vs. 27.4 RULER, 24.1 vs. 22.8 BABILong). The advantages are sustained across context lengths from 4k to 64k.

- **Two practically useful configurations with clear tradeoffs**: RoPE++_EH halves KV cache and QKV parameters while matching or exceeding RoPE's performance (Figure 4 shows lower memory and higher throughput), and RoPE++_EC delivers stronger performance at equal KV cache cost. The method also combines cleanly with existing techniques (Linear PI, YaRN) — Table 3 shows consistent advantages.

- **Attention pattern analysis confirms the specialization hypothesis**: Figure 5(a–d) shows that imaginary heads (odd indices) attend more globally, while real heads attend locally. This interpretable pattern aligns with and visually confirms the theoretical analysis.

## Weaknesses

### Fatal
None.

### Major

- **RoPE++_EC's parameter imbalance is not fully controlled**: RoPE++_EC has a doubled *W_o* (output projection) compared to vanilla RoPE (Section 3.3). While the paper claims improvements come from imaginary attention, the added parameters in *W_o* provide extra model capacity that could partially explain the gains — especially the large jumps at 376M. The paper does not include an ablation where a vanilla RoPE model with the same total parameter budget (e.g., increased hidden dimension or more heads) is compared. The mitigation evidence (EH configuration performs comparably with fewer parameters; the noise perturbation experiment) is suggestive but does not fully isolate the effect. This is the paper's most significant methodological gap.

### Minor

- **Long-context evaluation uses only synthetic benchmarks**: RULER and BABILong, while standard stress tests, are synthetic needle-in-a-haystack tasks. The paper claims imaginary attention "captures longer dependency" for real-world LLM use, but no natural-language long-context benchmarks (e.g., LongBench subsets, QMSum, NarrativeQA) are included to validate this transfer. This limits the generality of the demonstrated practical value.

- **RoPE++_EC efficiency characteristics are unmeasured**: Only RoPE++_EH is evaluated for memory cost and throughput (Figure 4). RoPE++_EC doubles the number of attention score computations, and even with KV cache unchanged, this may incur nontrivial FLOP overhead and latency. The paper mentions fusion with FlashAttention but provides no measurements to verify that EC is indeed "equal cost" in practice beyond cache size.

- **Short-context improvements are modest and lack statistical uncertainty**: In Table 1, average gains over RoPE are 0.2–1.0 points, and the best method varies by task. No confidence intervals, multiple seeds, or significance tests are reported, making it unclear whether these small advantages are reliable.

- **Discrepancy in gains between model scales unaddressed**: At 376M, RoPE++_EC gains +6.2 on RULER average; at 776M, only +2.0. The paper does not discuss this diminishing returns pattern, which could be an important limitation for scaling the method.

### Trivial

- **Figure 2 caption is ambiguously worded**: The caption for Figure 2(b) says "key heads are halved" — but compared to the RoPE baseline in Figure 2(a), the key head count is the same (2 in both cases). The halving is relative to the full MHA standard (4 query heads → 4 key heads expected), not to the baseline. This caused reviewer confusion. Fixing this wording would prevent misinterpretation.

## Nice-to-Haves
- A head-count-controlled ablation: compare RoPE++_EC against a vanilla RoPE model with the same total number of attention heads (doubled heads using only real attention) to formally isolate the imaginary mechanism from added capacity.
- A perplexity-vs-context-length extrapolation curve would directly support the theoretical claims in Section 3.4.
- Inference throughput/latency measurements for RoPE++_EC to verify its "equal cache, equal cost" claim.

## Removed Points
- **"Contradictory description of EC architecture"** (harsh critic #1): The critic claimed the caption "key heads are halved" contradicts "equal cache." In Figure 2(a) (RoPE): 2 key heads. Figure 2(b) (EC): 2 key heads. KV cache is identical. The caption's phrasing is ambiguous but not contradictory. The critic also conflated "QKV parameter budget" (addressing *W_q, W_k, W_v*) with *W_o* (the output projection), which are separate. Removed as factually inaccurate.
- **"Figure 1 decomposition equation is misleading"**: The critic claimed the paper writes attention as a complex sum but RoPE computes real-valued dot products. The equation is the correct decomposition of the complex product that naturally yields real and imaginary parts — this is the paper's core mathematical contribution, not a presentation error. Removed as misunderstanding.
- **"Missing limitations section"**: The paper states that "More discussion on the extrapolation performance and limitation of RoPE++ can be found in Appendix D" (end of Section 5.3). The appendix was stripped by the parser; the limitations exist in the original submission. Removed.
- Various generic formatting nitpicks and speculation-based criticisms. Removed per filtering rules.

## Novel Insights

The calibration process surfaced a useful comparative observation: while prior RoPE analysis work (e.g., "Round and Round We Go!") focused on mechanistic analysis of how existing models *use* RoPE frequencies, and prior RoPE improvement work focused on interpolation/extrapolation of the *existing* computation, this paper takes a genuinely different approach by asking what information is *lost* before computation even begins. The imaginary component was mathematically present in the full complex product but pragmatically discarded — and this paper shows that its recovery creates a new functional dimension (global-vs-local specialization across heads) that standard RoPE cannot achieve regardless of hyperparameter tuning. This reframes the position-embedding design space: rather than asking "how should we scale/rotate the existing signal," one can ask "which parts of the full complex representation are we throwing away?" This perspective may apply beyond RoPE to other position embedding schemes that use complex representations.

## Suggestions
1. **Add a parameter-controlled ablation**: Compare RoPE++_EC against a vanilla RoPE model with total parameters matched (e.g., same head count but all real, or slightly increased hidden dimension) to disentangle the imaginary mechanism from added capacity.
2. **Include at least one natural-language long-context benchmark** (e.g., a LongBench subset) to demonstrate practical value beyond synthetic retrieval tasks.
3. **Add error bars or multi-seed results** for the main long-context results, especially given the modest-magnitude gains at 776M.
4. **Fix the Figure 2 caption** to avoid the ambiguous "halved" phrasing, and clarify the relationship between the RoPE, EC, and EH configurations in terms of exact head counts, cache cost, and parameter counts.

## Score and Decision

**Calibration report:**

**Round 1 bracket** (5.5–7.0): Three queries across score bands for RoPE/long-context position embedding papers.

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| jp4pxKqCRW — Periodic Extension | 2.50 | R1 | Weaker paper; limited experiments, low scores |
| 5dDYhvt6dY — Reinforced PE | 3.00 | R1 | Unrelated low-scoring paper |
| I1484gDBr4 — LRNN | 2.50 | R1 | Unrelated |
| GtvuNrk58a — Round and Round We Go! | 6.20 | R1 | Comparable novelty; less empirical breadth |
| JO7k0SJ5V6 — Scaling Laws of RoPE | 5.00 | R1 | Stronger theory, weaker empirics than current paper |
| eoln5WgrPx — STRING | 6.50 | R1 | Comparable; larger-model eval, different approach |
| Us1RXG1Ji2 — TAPE | 6.00 | R1 | Similar-strength method paper |
| EytBpUGB1Z — Retrieval Head | 8.00 | R1 | Stronger overall; broader impact, cleaner evaluation |
| OvoCm1gGhN — Differential Transformer | 8.00 | R1 | Stronger; architectural change, more extensive eval |

**Round 2 narrowing** (adjusted to 5.5–7.0):

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| OhauMUNW8T — Wavelet-based PE | 5.25 | R2 | Weaker; marginal improvements, less novelty |
| sIGWTd1DcW — Contextual PE | 5.25 | R2 | Similar weakness profile |
| fL4qWkSmtM — LongPPL | 6.80 | R2 | Different contribution (metric paper); not directly comparable |
| wXpSidPpc5 — CLEX | 6.50 | R2 | Comparable contribution; more complex method, similar empirical scope |

**Final score:** The paper sits above the wavelet (5.25) and scaling laws (5.00) anchors, is comparable to "Round and Round" (6.2), STRING (6.5), and CLEX (6.5), and is below the 8.0 anchor papers. The core idea is novel, well-motivated, and supported by theoretical analysis plus a clever causal experiment (noise perturbation). The main limitations — the EC parameter confound, synthetic-only long-context eval, and unmeasured EC efficiency — are real but not fatal. A strong accept at a good venue.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>