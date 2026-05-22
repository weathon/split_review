Now I have sufficient material to write the final consolidated review.

---

## Summary

This paper proposes RoPE++, an extension of Rotary Position Embeddings that reincorporates the imaginary component of the complex-valued attention dot product (which standard RoPE discards by only taking the real part) as an additional set of attention heads. The method is elegantly simple: computing the imaginary attention is equivalent to rotating the query by −π/2 before applying standard RoPE, so the same keys and KV cache can be reused. Two configurations are offered — RoPE++\_EC (equal cache, doubled attention heads) and RoPE++\_EH (equal heads, halved KV cache). Experiments at 376M and 776M scales show improvements over vanilla RoPE, especially on long-context synthetic benchmarks like RULER and BABILong.

## Strengths

1. **Clean mathematical derivation and intuitive geometric interpretation.** The paper correctly identifies that the imaginary part of the complex RoPE dot product can be computed by a simple −π/2 rotation of the query (Equations 2–4, Section 3.1). This connects directly to a sine‑integral characteristic curve (Equation 5, Figure 1) that the paper shows decays more slowly than the cosine decay of the real component, providing a mechanistic explanation for why imaginary heads may favor long-range dependencies.

2. **Practical dual‑configuration design with concrete efficiency benefits.** RoPE++\_EC doubles the number of attention heads at the same cache cost as vanilla RoPE. RoPE++\_EH halves the KV cache and QKV parameters while retaining the same number of heads. Efficiency measurements in Figure 4 show memory reduction and throughput gains for RoPE++\_EH, with the margin widening as context length grows. This is a practical, deployable contribution — not just a comparable result.

3. **Controlled noise‑ablation experiment supporting the central claim.** In Section 5.2 (Figure 5), the paper adds Gaussian noise separately to real and imaginary attention components. At σ=1.0, corrupting imaginary heads degrades RULER-4k performance by 5–8 points more than corrupting real heads, providing direct evidence that the imaginary component carries information most critical for long-context tasks.

4. **Compatibility with existing long‑context extension methods.** Table 3 shows RoPE++ improves over vanilla RoPE when combined with both Linear PI and YaRN across two model sizes, demonstrating the benefit is orthogonal to and additive on top of prior interpolation techniques.

## Weaknesses

### Major

- **No multiple‑seed runs or statistical significance reporting.** All experiments are reported from a single run without confidence intervals or standard deviations. Many individual comparisons at 776M are small (e.g., RULER 16k: 33.4 vs. 33.0; RULER 64k: 10.9 vs. 10.4). Without any measure of variance, it is impossible to assess whether even the headline improvements are statistically significant. This is the single biggest weakness in the experimental evidence.

- **Long‑context evaluation lacks baselines for other position‑embedding methods.** Table 2 (long‑context RULER and BABILong) compares only RoPE vs. RoPE++. FoPE, Pythia, and ALiBi are included in the short‑context Table 1 but omitted from the long‑context evaluation. The paper justifies this by saying "RoPE is the position embedding currently most widely used by long‑context LLMs" (Section 4.3), but the abstract and conclusion claim superiority "over other position embeddings" in general, not just over RoPE. Without evaluating FoPE/ALiBi after comparable long‑context training, the claim about superiority over other position embeddings in long‑context settings is not fully supported.

- **Length‑extrapolation argument is not directly tested.** Section 3.4 argues that RoPE++ improves length extrapolation because imaginary attention exposes more dimensions to the full ±1 range of trigonometric values during training. However, all long‑context results in Tables 2 and 3 come from models that were further trained on 32k context (via base scaling, Linear PI, or YaRN). There is no "train on 4k, test on 32k" extrapolation experiment without additional fine‑tuning, so any claimed extrapolation benefit is confounded with the long‑context fine‑tuning itself.

### Minor

- **Gains are inconsistent across model scales and modest at 776M.** At 376M, RoPE++\_EC achieves a 6.2‑point gain on RULER average (25.0 vs. 18.8). At 776M, the same comparison yields a 2.0‑point gain (29.4 vs. 27.4). On BABILong at 776M, the gain is 1.3 points (24.1 vs. 22.8). The improvements are directionally consistent but shrink substantially at the larger scale, raising the question of whether the benefit diminishes as model capacity increases. The paper does not discuss this pattern.

- **No efficiency measurements for RoPE++\_EC.** Figure 4 measures memory and speed only for RoPE++\_EH, not EC. The paper notes that RoPE++\_EC doubles the output projection W\_o, but does not quantify the FLOP or memory overhead of this doubled projection in practice.

- **No per‑task breakdown for RULER.** RULER comprises multiple sub‑tasks (SQA, NIAH, VT, etc.). Reporting only the average hides where RoPE++ helps or hurts.

### Trivial

- None (the paper is clearly written and free of significant presentation issues).

## Nice-to-Haves

1. A direct extrapolation experiment (train on 4k, test at 32k without further fine‑tuning) to support the length‑extrapolation claims in Section 3.4.
2. Long‑context evaluations of FoPE and ALiBi after comparable 32k training, to substantiate claims of superiority over other position embeddings in long‑context settings.
3. An ablation that zeroes out imaginary heads (rather than adding noise) as a cleaner test of their importance.

## Removed Points

- **"Mischaracterization of the contribution as 'recovering discarded information'"** — The harsh critic claimed the framing is misleading. However, the paper is technically accurate: standard RoPE computes a complex‑valued dot product and takes only the real part. The imaginary part of that complex product is mathematically present but unused in the attention computation. Describing this as "discarded" information is a standard and unproblematic framing; the paper never claims RoPE "used to have" imaginary attention that was "actively removed."
- **"The derivation is mathematically correct but the observation is trivial in hindsight"** — This is a subjective opinion, not a technical weakness. Many good ideas are simple in retrospect.
- **"RoPE++ sometimes underperforms RoPE in Table 3"** — The cited case (376M YaRN RULER 4k: 36.4 vs. 36.0, a 0.4‑point difference) is well within the noise floor for a single‑run experiment and does not constitute a meaningful underperformance.
- **"Missing related works"** — The paper has a dedicated related work section. The reviewer's request for further citations cannot be verified without external sources.
- Various formatting and document‑structure nitpicks, which are artifacts of the PDF extraction process.

## Novel Insights

None beyond the paper's own contributions. The core insight — that the imaginary component of the RoPE dot product captures a different attention bias that can be recovered by a −π/2 query rotation — is the paper's main contribution, and the reviews do not surface additional novel angles beyond what the paper already states.

## Suggestions

1. **Run all main experiments with at least 3 random seeds** and report means ± standard deviations. This is essential to establish that the reported gains are not within noise, especially at 776M where differences are smaller.
2. **Add FoPE and ALiBi to Table 2** after training them on 32k context under the same protocol. This directly supports the claim of superiority over other position embeddings in long‑context settings.
3. **Include a direct extrapolation experiment** (train on 4k, evaluate at 16k/32k without any additional training) to validate the Section 3.4 argument.
4. **Provide a per‑task breakdown for RULER** to show where the method helps or hurts, and discuss why gains are larger at 376M than at 776M.
5. **Quantify the W\_o overhead for RoPE++\_EC** in terms of FLOPs and parameter count, and ideally provide memory/speed measurements for EC as well.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison to This Paper |
|---|---|---|
| `GtvuNrk58a` — "Round and Round We Go" (RoPE analysis) | 6.20 | Analytical paper with similarly thorough math but limited empirical scope. RoPE++ has stronger practical validation. |
| `wXpSidPpc5` — "CLEX" (continuous length extrapolation) | 6.50 | Stronger experiments (multi‑seed, more baselines) than RoPE++. RoPE++ has a simpler, more practical method. |
| `Us1RXG1Ji2` — "TAPE" (contextualized PE) | 6.00 | Comparable contribution level. TAPE has more severe experiment omissions (missing baselines). |
| `JO7k0SJ5V6` — "Scaling Laws of RoPE" | 5.00 | RoPE++ has more comprehensive experiments, including downstream tasks beyond perplexity. |
| `N5qFgohx9u` — "MöbiusAttention" (complex‑valued attention) | 3.50 | RoPE++ is substantially stronger in experimental rigor and practical contribution. |
| `jp4pxKqCRW` — "Periodic Extension" (RoPE extrapolation) | 2.50 | RoPE++ is clearly superior in both execution and evidence quality. |

The paper proposes a clean, well‑motivated extension to RoPE with clear practical advantages (cache efficiency, compatibility with existing interpolation methods) and positive empirical results across multiple benchmarks and model sizes. However, the experimental evidence has notable gaps: the lack of multiple‑seed runs and statistical significance testing makes it hard to assess the reliability of the modest gains at 776M, the missing long‑context baselines for other position embeddings weakens comparative claims, and the length‑extrapolation argument remains untested. These gaps are real but addressable, and they do not invalidate the core contribution.

**Score**: 5.5 — a solid, incremental contribution with a practical design and decent empirical support, held back by missing statistical rigor and incomplete baselines. Comparable to mid‑range accepted papers in this area.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>