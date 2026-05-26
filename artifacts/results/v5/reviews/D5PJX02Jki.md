Now I have enough information. Let me compile the final review.

## Summary

The paper identifies that standard RoPE discards the imaginary component of the complex-valued attention score, and proposes RoPE++ which re-incorporates this imaginary component as a separate set of attention heads. Two configurations are introduced: RoPE++_EH (equal total head count, half KV cache) and RoPE++_EC (equal cache, doubled head count). Theoretical analysis via sine-integral characteristic curves suggests imaginary attention captures longer-range dependencies. Experiments at 376M and 776M scales show EC substantially outperforms vanilla RoPE on long-context benchmarks (RULER, BABILong), while EH achieves comparable performance with half the cache. A noise-injection experiment provides causal evidence that imaginary heads are more important than real heads for long-context performance.

## Strengths

1. **Novel identification of discarded imaginary information** – The paper is the first to point out that standard RoPE's complex-valued attention score discards the imaginary component, and derives a clean mathematical formulation (Section 3.1, Eqs. 2–4) for re-incorporating it. The derivation showing that imaginary attention requires only a −π/2 rotation of the query is elegant.

2. **Substantial long-context gains for RoPE++_EC** – On RULER and BABILong up to 64k (Table 2), EC consistently outperforms vanilla RoPE by large margins (e.g., 376M: RULER avg 25.0 vs 18.8, +6.2 pts; BABILong avg 16.1 vs 11.0, +5.1 pts). These gains hold at both 376M and 776M and across all evaluated context lengths.

3. **Causal evidence from noise injection** – The controlled experiment in Section 5.2 (Figure 5) independently corrupts real or imaginary attention scores with Gaussian noise. At σ=1.0, imaginary-noised accuracy drops ~5 points (376M) and ~8 points (776M) more than real-noised accuracy. This provides direct causal evidence that imaginary heads carry more long-context information, independent of any head-count confound.

4. **Parameter/cache efficiency without major degradation** – RoPE++_EH maintains comparable average performance to vanilla RoPE while halving KV cache and QKV parameters (Table 1, Table 2). Figure 4 confirms consistent memory reduction and faster decoding, with the margin widening as context grows. This is a practical benefit.

5. **Compatibility with existing techniques** – RoPE++ combines with YaRN and Linear PI (Table 3), still yielding the highest average scores. This demonstrates generalizability beyond the base RoPE.

6. **Clear theoretical analysis** – The characteristic-curve analysis (sine integral, Section 3.2) provides a principled explanation for why imaginary attention captures longer-range dependencies, and the attention-pattern visualization (Figure 5) validates this empirically.

## Weaknesses

### Fatal
None.

### Major

1. **Confounded comparison for the core claim** – RoPE++_EC doubles the total attention heads relative to vanilla RoPE. The paper does not include the obvious control: vanilla RoPE with 2H heads (all real, same head count as EC). Without this control, EC's substantial gains on long-context tasks (Table 2) cannot be cleanly attributed to the imaginary component rather than simply increased model capacity from extra heads. This is the most significant weakness because it directly affects the paper's central thesis. The EH variant controls for head count but its results are mixed (see below), and its architectural changes (halved KV cache) introduce other confounds. A controlled experiment comparing (a) vanilla RoPE with 2H heads, (b) RoPE++_EC with H real + H imaginary heads, and (c) vanilla RoPE with H heads would resolve this.

### Minor

2. **Mixed results for the head-count-controlled variant (EH)** – RoPE++_EH, which holds total head count constant, shows small and inconsistent improvements over vanilla RoPE. On several long-context metrics EH is *worse* than vanilla RoPE: e.g., 376M Long RULER avg 18.2 vs 18.8, 776M Long BABILong avg 19.4 vs 22.8. While EH's efficiency advantage (half cache) is clear, the performance benefit from the imaginary component alone is not consistently demonstrated in this variant, weakening the overall case for the method's core claim.

3. **No variance or significance measures** – All results are reported without confidence intervals, standard deviations, or significance tests. Many comparisons involve differences of 1–3 percentage points (Table 1, Table 2). Without uncertainty estimates, it is difficult to assess which differences are meaningful vs. noise. This is especially relevant given the moderate training budgets (50B pre-training tokens + 10B long-context tokens).

4. **No direct length-extrapolation perplexity analysis** – Section 3.4 argues that RoPE++ improves length extrapolation by exposing more dimensions to the full ±1 value range of sinusoidal functions. However, no direct empirical evidence (e.g., a perplexity-vs-length plot beyond the training window, as in the original RoPE paper) is provided. The task-based evaluation in Table 2 goes up to 64k but aggregates over tasks; a simple perplexity curve on held-out texts would more directly validate the extrapolation claim.

5. **Limited model scales** – Experiments are conducted only at 376M and 776M parameters. For a method that claims to improve position encoding for LLMs, validation at scales of 1B+ (where RoPE-based long-context models are most impactful) would substantially strengthen the paper. The paper mentions "analysis on larger model scale" in Appendix C, but the appendix is not available for verification.

### Trivial

6. **Figure 2 caption inconsistency** – The Figure 2 caption describes RoPE++_EC as having "key heads halved" and RoPE++_EH as having "key heads doubled," which contradicts the body text (Section 3.3) where EC maintains equal cache (same key-value heads) and EH halves cache. While the body text is the authoritative description, this inconsistency creates confusion about the architectural design.

7. **Brief justification of the negative imaginary part** – The paper states that the negative imaginary part is used to preserve semantic aggregation (Section 3.2) but provides only a brief justification. A more detailed interpretive discussion would help readers understand this design choice.

## Nice-to-Haves

- A controlled experiment comparing RoPE++_EC against vanilla RoPE with the same number of total heads (2H, all real).
- FLOPs and training-time overhead analysis alongside the cache-efficiency results.
- Perplexity-vs-length curves for direct extrapolation validation.
- Evaluation at larger model scales (≥1B) to confirm the method's generalizability.

## Removed Points

These points were raised in the inputs but are excluded from the main review for the following reasons:

- **"Missing NTK-aware scaling, YaRN, corrected base scaling as primary baselines"** – Removed as scope creep. YaRN/NTK-aware scaling are orthogonal context-extension techniques, not alternative position embeddings. The paper compares against appropriate PE baselines (FoPE, Pythia, ALiBi, vanilla RoPE) and tests compatibility with YaRN/PI in §5.3.
- **"Pre-training budgets may not be enough for full convergence"** – Removed as speculative. No specific evidence is provided that 50B tokens is insufficient for convergence at these model sizes.
- **"Noise ablation criticism (corrupting one set of heads could affect the other)"** – Removed. The noise is applied independently to attention scores of real vs. imaginary heads under identical conditions; the asymmetry in downstream effect is a valid causal signal.
- **"Performance at 64k is very low for all models"** – Removed. Low absolute performance at 64k is expected for 376M/776M models; this is not a specific weakness of the proposed method.
- **"Missing FLOPs analysis"** – Moved to Nice-to-Haves. It would strengthen the paper but is not a core weakness.
- **"Missing related works"** – Removed per policy (cannot verify existence of missing citations without external sources).

## Novel Insights

The reviews converge on the key tension in the paper: the idea of re-incorporating the discarded imaginary component of RoPE is genuinely novel and the mathematical derivation is clean, but the experimental validation is undermined by a confounded comparison (EC's extra heads vs. imaginary contribution). The noise-injection experiment is the reviews' most interesting finding — it provides a way to disentangle the imaginary component's contribution that is independent of the head-count confound, and the clear gap (5–8 points) between corrupting real vs. imaginary heads is stronger causal evidence than typical ablation studies in this space. This suggests the method could be better served by foregrounding the noise experiment as the primary evidence rather than the raw performance comparison.

## Suggestions

1. **Run the controlled experiment**: Compare vanilla RoPE with 2H heads (all real) against RoPE++_EC (H real + H imaginary heads) and vanilla RoPE with H heads. If RoPE++_EC outperforms 2H vanilla RoPE by a clear margin, the core claim is fully supported.

2. **Add uncertainty quantification**: Report results over multiple training seeds or at minimum provide standard deviations. This is especially important for the 1–2 point differences in Table 1.

3. **Add perplexity-vs-length curves**: Plot validation perplexity at context lengths up to 128k to directly demonstrate the extrapolation benefit claimed in Section 3.4.

4. **Scale up**: Validate at 1B+ scale to confirm the method's practicality.

5. **Fix Figure 2**: Correct the caption descriptions to align with the body text.

6. **Foreground the noise experiment**: The noise-injection study is the cleanest evidence for the imaginary component's role. Consider making it a main result.

## Score and Decision

### Calibration Anchors

| Anchor ID | Score | Round/Query | Comparison |
|-----------|-------|-------------|------------|
| jp4pxKqCRW | 2.50 | R1-topic-low | "Periodic Extension" — poor writing, limited experiments, all results in appendix. Current paper is substantially better. |
| 5dDYhvt6dY | 3.00 | R1-topic-low | "Efficient transformer with reinforced PE" — limited scope. Current paper has stronger theory and eval. |
| JO7k0SJ5V6 | 5.00 | R1-topic-mid, R2 | "Scaling Laws of RoPE-based Extrapolation" — strong theory but weak evaluation (mostly perplexity). Comparable quality overall. |
| OhauMUNW8T | 5.25 | R2 | "Wavelet-based Positional Representation" — similar scope, marginal improvements, limited evaluation. Comparable quality. |
| sIGWTd1DcW | 5.25 | R2 | "Contextual Position Encoding" — similar topic. Comparable quality. |
| 3Z1gxuAQrA | 6.00 | R1-topic-mid | "PoSE" — stronger experimental validation, clearer contribution. Current paper is weaker. |
| wXpSidPpc5 | 6.50 | R1-topic-mid | "CLEX" — stronger evaluation, clearer contribution. Current paper is weaker. |
| eoln5WgrPx | 6.50 | R1-topic-mid | "STRING" — SOTA results on 70B models, clear improvements. Current paper is substantially weaker. |
| GtvuNrk58a | 6.20 | R3 | "Round and Round We Go" — deeper mechanistic understanding. Current paper is weaker on analysis depth. |
| N581Nje6fH | 1.50 | R1-topic-low | Unrelated paper, irrelevant for comparison. |
| VkqqZcofEu | 5.75 | R1-weakness | "Controlled Study on Long Context" — comprehensive comparison study. Different contribution type. |

**Round-1 bracket**: 3.5–6.5. The paper is clearly above the 1.5–3.0 band (poorly written papers with minimal experiments) but below the 6.0–6.5 band (well-executed methods with thorough evaluation at scale).

**What the low-band anchors failed at**: Poor writing/organization, limited evaluation (perplexity-only), lack of theoretical rigor, missing baselines, inaccessible results (appendix-only). The current paper shares **none** of these failures — it is well-organized, includes multiple task evaluations, has solid theoretical derivation, and presents results clearly in the main text. This places it well above the 2.5–3.0 band.

**Round-2 narrowing**: Within the 3.5–6.5 bracket, the paper sits at 5.0, comparable to the "Scaling Laws of RoPE" (5.00) and "Wavelet-based" (5.25) papers — both of which have a similar pattern of a decent idea with solid but incomplete evaluation. The paper cannot reach 6.0+ because: (a) the confounded comparison undermines the core claim more significantly than any single weakness in the 6.0+ anchors, and (b) limited model scales (376M/776M vs. the 7B+ models in 6.0+ papers).

**Score rationale**: The paper has a genuinely novel idea with solid theoretical foundations and reasonable experimental evidence. However, the confounded comparison for the EC configuration is a Major weakness that prevents full confidence in the core claim. The mixed EH results and lack of variance reporting further limit the empirical strength. A score of 5.0 reflects a paper with clear merit but significant unresolved issues that prevent a stronger recommendation. The paper is near the accept/reject boundary for a standard conference.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>