Now I have all the information I need. Let me write the consolidated review.

**Round 1 bracket:** The paper sits between the weak anchors (<3.5, rejected/withdrawn papers with unclear contributions) and the strong anchors (>7.5, highly-rated papers like Scaling Laws of RoPE at 8.0 and Diff Transformer at 8.0). Initial bracket: 5.0–7.0.

**Round 2 narrowing:** Comparing against PoSE (avg 6.0, accepted poster), YaRN (avg 6.5, accepted poster), and the rejected papers at ~4.75–5.0, the paper lands closest to PoSE in quality — a clean, useful idea with sufficient but not comprehensive evaluation. It is more novel than the rejected papers but has smaller-scale experiments than YaRN.

**Final score: 6.0** — marginally above the acceptance threshold. The idea is genuinely novel and the evidence, while limited in scale and scope, supports the core claims.

---

## Summary

This paper identifies that standard RoPE implementations discard the imaginary component of the complex-valued dot product when computing attention scores. The authors propose RoPE++, which re-incorporates this imaginary component as a separate attention head computed alongside the real attention. Two configurations are introduced: RoPE++EH (equal number of attention heads but halves KV cache and QKV parameters) and RoPE++EC (equal cache size but doubles the number of attention heads). The paper provides theoretical analysis showing that imaginary attention has a slower-decaying characteristic curve (sine integral vs. cosine integral), which preferentially captures long-range dependencies. Experiments at 376M and 776M scales show consistent improvements over vanilla RoPE, particularly on synthetic long-context benchmarks (RULER, BABILong), and the method is compatible with standard context extension techniques (PI, YaRN).

## Strengths

1. **Genuinely novel identification and recovery of RoPE's discarded imaginary component.** Section 3.1 shows that imaginary attention can be computed by simply rotating query vectors by -π/2 before applying standard RoPE (Equation 4), requiring no extra KV cache and preserving the unified absolute–relative position embedding format. This is a fundamental insight about RoPE's computation that prior work missed.

2. **Theoretical and empirical evidence that imaginary attention preferentially captures long-range dependencies.** Section 3.2 derives the characteristic curve as a sine integral (Equation 5), which decays more slowly than the cosine integral of real attention (Figure 1). The noise-perturbation experiment (Section 5.2, Figure 5e,j) provides mechanistic evidence: corrupting imaginary attention degrades RULER-4k scores by up to 8 points more than corrupting real attention, directly supporting the claim about imaginary attention's role in long-context modeling.

3. **Substantial gains on synthetic long-context benchmarks with equal cache cost (RoPE++EC).** Table 2 shows RoPE++EC consistently outperforms vanilla RoPE across all tested lengths at both 376M and 776M. At 376M, RoPE++EC achieves RULER average 25.0 vs. RoPE's 18.8 (+33%), and BABILong average 16.1 vs. 11.0 (+46%), with gains persisting at the longest (64k) context.

4. **Cache and parameter efficiency without catastrophic quality loss (RoPE++EH).** RoPE++EH halves KV-cache size and QKV parameters while keeping the same head count. Figure 4 shows reduced memory cost and improved decoding throughput at both scales, with the margin widening as context grows. Short-context performance (Table 1) is comparable to vanilla RoPE (e.g., 376M avg 40.3 vs. 40.1).

5. **Compatibility with standard long-context extension techniques.** Table 3 demonstrates that RoPE++ combined with PI or YaRN consistently outperforms vanilla RoPE with the same extension, confirming generalizability beyond the default NTK-based extension.

## Weaknesses

### Fatal
None.

### Major

1. **Long-context evaluation is limited to synthetic benchmarks.** All long-context evidence comes from RULER and BABILong — synthetic retrieval/reasoning tasks. Real-world long-context tasks (e.g., long-document QA, summarization over long passages, LongBench subsets) are not evaluated. While synthetic benchmarks are useful for controlled analysis, the paper's central claim about "capturing longer dependencies" for practical LLM use cases remains unverified at the task level where it would matter most.

2. **Limited experimental scale.** Experiments are conducted only at 376M and 776M parameters. No results at 1B+ scale are provided. Given that RoPE is primarily used in models ranging from 7B to 405B parameters, it is unclear whether the benefits of imaginary attention persist, diminish, or interact with other properties (e.g., more heads, deeper layers) at larger scales. The paper's claim of "supporting future long-context LLMs" is weakened by the absence of larger-model validation.

3. **RoPE++EH sacrifices quality on some long-context benchmarks without adequate discussion.** On BABILong at 776M (Table 2), RoPE++EH achieves only 19.4 average vs. vanilla RoPE's 22.8 — a 3.4-point deficit. The paper describes RoPE++EH as delivering "comparable" performance but does not squarely discuss this degradation. Users choosing RoPE++EH for efficiency should be aware that the quality-efficiency trade-off is real and non-negligible on some long-context tasks.

### Minor

4. **Short-context gains are modest and reported without statistical significance.** At 376M, RoPE++EC's average short-context gain over RoPE is ~0.9 points; at 776M it is ~0.8 points. Individual task differences are often within 1–2 points, and no confidence intervals, significance tests, or multiple-run statistics are reported. While this is typical for pre-training papers at this scale, it makes it difficult to distinguish genuine improvement from random variation.

5. **The claim that benefits become "more significant as context length increases" is not monotonic in the data.** At 376M RULER (Table 2), RoPE++EC's absolute gain over RoPE at 32k is 8.2 points (17.7 vs. 9.5), but at 64k it is 3.5 points (9.0 vs. 5.5). While relative gains remain substantial at 64k, the language over-promises relative to the actual trend.

### Trivial
None.

## Nice-to-Haves

- **Real long-context tasks:** Adding even one or two real-world benchmarks (e.g., LongBench subsets, NarrativeQA, QMSum) would substantially strengthen the claim that imaginary attention helps in practical settings.
- **Perplexity curves on long sequences:** Showing perplexity as a function of context length beyond 4k (up to 32k or 64k) for both RoPE and RoPE++ would provide a cleaner diagnostic of length extrapolation improvement, as is standard in the long-context literature.
- **A clearer break-even analysis for RoPE++EH:** An explicit statement of which benchmarks see degradation and by how much, rather than describing results as "comparable," would improve scientific honesty.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **"Fairness of baseline configuration — RoPE++EC doubles heads; compare against RoPE with doubled heads"** — Removed. The paper's design is intentional: RoPE++EC trades doubled heads for equal cache. Comparing against RoPE with doubled heads would change cache cost, defeating the purpose of the EC configuration. The paper clearly explains this design choice in Section 3.3 and Figure 2.

2. **"Missing related work"** — Removed per instructions (no external sources to verify existence of cited works).

3. **"Missing appendix content / proofs in appendix"** — Removed. The parser strips appendix content from all papers; these exist in the original submission.

4. **"Ablation with only imaginary heads / 75% imaginary vs. 25% real"** — Removed. The paper explicitly explains (Section 3.3) that imaginary attention is defined relative to real attention and cannot exist independently: "configurations such as 75% imaginary vs. 25% real or 100% imaginary... are impossible under RoPE++." The reviewer's suggestion misunderstands the method's constraints.

5. **Generic strengths from Strength Finder (e.g., "the paper is well-written," "the problem is important," "addressed an important problem")** — Removed as generic/superficial. Only strengths with concrete, article-specific evidence are retained.

6. **"Pure formatting/style nitpicks" and "typos/grammar issues"** — Removed per instructions (parser artifacts).

## Novel Insights

The most interesting observation from synthesizing the reviews is that the noise-perturbation experiment (Figure 5) is arguably the strongest evidence in the paper, yet it is placed in the Discussion section rather than being positioned as a central result. This experiment does more than any single benchmark score to validate the core mechanistic claim — that imaginary heads are functionally specialized for long-range information. The pattern of results (imaginary corruption hurting long-context performance more than real corruption) provides causal evidence rather than merely correlational. Future work building on RoPE++ could productively use similar perturbation paradigms to probe the functional specialization of attention heads across different position embedding schemes.

## Suggestions

1. Add at least one real long-context benchmark (e.g., a LongBench subset) to demonstrate that the synthetic gains translate to practical tasks.
2. Explicitly discuss the RoPE++EH quality-efficiency trade-off in the main text, noting where performance degrades (BABILong at 776M) and by how much.
3. Consider adding perplexity curves as a function of context length for both RoPE and RoPE++, which is a standard diagnostic in the long-context literature (used in YaRN, Scaling Laws of RoPE).
4. Tone down the claim about "benefits becoming more significant as context length increases" to better match the empirical trend (gains are significant but not strictly monotonic).

## Score and Decision

**Anchors consulted (all rounds):**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| `/home/wg25r/review_agent/human_reviews/jp4pxKqCRW.md` (Periodic Extension) | 2.50 | R1 | Much weaker — unclear contribution, withdrawn |
| `/home/wg25r/review_agent/human_reviews/5dDYhvt6dY.md` (Reinforced PE) | 3.00 | R1 | Much weaker — narrow task, small experiment |
| `/home/wg25r/review_agent/human_reviews/4QWPCTLq20.md` (IntelLLM) | 3.00 | R1 | Much weaker — different topic, withdrawn |
| `/home/wg25r/review_agent/human_reviews/I1484gDBr4.md` (Linear RNN) | 2.50 | R1 | Much weaker — different topic, withdrawn |
| `/home/wg25r/review_agent/human_reviews/wHBfxhZu1u.md` (YaRN) | 6.50 | R1 | Similar quality but YaRN tested on 7B models and had real-world adoption; RoPE++ has more novel core insight but smaller scale |
| `/home/wg25r/review_agent/human_reviews/3Z1gxuAQrA.md` (PoSE) | 6.00 | R1, R2 | Comparable — both have clean ideas, similar scale limitations, similar evaluation gaps |
| `/home/wg25r/review_agent/human_reviews/r9oqHOdoHf.md` (TULIP) | 6.67 | R1 | Slightly stronger — tested on practical vision-language task, better evaluation |
| `/home/wg25r/review_agent/human_reviews/t717joHHSc.md` (Mitigate Position Bias) | 4.75 | R1, R2 | Weaker — less novel, inconsistent experimental results, rejected |
| `/home/wg25r/review_agent/human_reviews/JO7k0SJ5V6.md` (Scaling Laws of RoPE) | 8.00 | R1 | Stronger — deeper theoretical analysis, 7B/13B models, 1M context length |
| `/home/wg25r/review_agent/human_reviews/EytBpUGB1Z.md` (Retrieval Head) | 8.00 | R1 | Stronger — thorough mechanistic analysis across many models, oral |
| `/home/wg25r/review_agent/human_reviews/OvoCm1gGhN.md` (Diff Transformer) | 8.00 | R1 | Stronger — comprehensive evaluation across scales and tasks, oral |
| `/home/wg25r/review_agent/human_reviews/PdaPky8MUn.md` (Never Train from Scratch) | 8.00 | R1 | Stronger — thorough empirical study across architectures, oral |
| `/home/wg25r/review_agent/human_reviews/lnffMykYSj.md` (Long Range Abilities) | 4.50 | R2 | Weaker — unclear motivation, missing experimental details, rejected |
| `/home/wg25r/review_agent/human_reviews/AozPzKE0oc.md` (Fast RoPE Attention) | 4.80 | R2 | Weaker — flawed proofs, no experiments, rejected |
| `/home/wg25r/review_agent/human_reviews/s3IBHTTDYl.md` (Inductive Biases to Count) | 6.75 | R2 | Slightly stronger — thorough empirical study, accepted poster |
| `/home/wg25r/review_agent/human_reviews/ONPECq0Rk7.md` (Headless Language Models) | 6.50 | R2 | Slightly stronger — tested at more scales, accepted poster |
| `/home/wg25r/review_agent/human_reviews/bRLed9prWC.md` (Future Language Modeling) | 7.33 | R2 | Stronger — novel task formulation, accepted poster |
| `/home/wg25r/review_agent/human_reviews/i7oU4nfKEA.md` (When Is Multilinguality a Curse) | 6.25 | R2 | Comparable — thorough but rejected; RoPE++ is similar quality but not directly comparable topic |

**Round 1 bracket:** 5.0–7.0. The paper is clearly above the withdrawn/rejected papers scoring 2.5–3.0 and clearly below the 8.0-level papers with more comprehensive evaluation and theory.

**Round 2 narrowing:** Within the bracket, the paper is most comparable to PoSE (6.0, accepted) and slightly below YaRN (6.5, accepted). It shares PoSE's scale limitation (small models) but has more evaluation breadth. It is clearly above the rejected papers at 4.5–5.0. The novelty of the core idea is a genuine strength; the limited experimental scope is the main weakness holding it back.

**Final calibration:** The paper is comparable to or slightly better than PoSE (6.0) but not as strong as YaRN (6.5). Given the genuine novelty of the contribution but the significant limitations in experimental scope (small models, synthetic long-context only), 6.0 is the appropriate score — marginally above the acceptance threshold.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>