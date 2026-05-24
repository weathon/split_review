## Summary

This paper identifies that standard RoPE discards the imaginary component of the complex-valued dot product in attention computation, and proposes RoPE++ to re-incorporate it as a separate group of attention heads. The imaginary-attention heads are computed by rotating queries by -π/2 before the standard RoPE rotation, which produces attention scores whose characteristic curve (a sine integral) decays more slowly than the real part's cosine curve, favoring long-range dependencies. Two configurations are introduced: RoPE++EH (equal heads, halved KV cache) and RoPE++EC (equal cache, doubled heads). Experiments at 376M and 776M scales show consistent gains, especially for RoPE++EC on long-context benchmarks (RULER, BABILong), with ablations confirming the causal role of imaginary attention.

## Strengths

- **Novel and well-motivated idea.** The observation that RoPE's standard implementation discards the imaginary component of the complex-valued dot product is clean and overlooked. Re-incorporating it via a simple -π/2 rotation of queries is elegant and preserves the absolute–relative position embedding duality.

- **Theoretical analysis provides a clear rationale.** Section 3.2 derives that the imaginary attention's characteristic curve approximates a sine integral Si(Δt), which decays far more slowly than the real part's cosine curve. This provides a principled, mathematical explanation for why imaginary heads preferentially attend to distant positions. The analysis of length extrapolation (Section 3.4) further shows that RoPE++ exposes model dimensions to a wider positional-value range during training.

- **Strong empirical gains on long-context benchmarks.** At 376M, RoPE++EC raises the RULER average from 18.8→25.0 and BABILong average from 11.0→16.1 over vanilla RoPE (Table 2). At 776M, the gains are similarly substantial (RULER 27.4→29.4, BABILong 22.8→24.1). These are the paper's most direct evidence for its core claim.

- **Causal ablation (noise injection) convincingly ties imaginary heads to long-context performance.** Adding Gaussian noise to the imaginary component degrades RULER-4k scores by up to 8 points more than the same noise on the real component at 776M (Section 5.2, Figure 5). This goes beyond correlation and demonstrates that imaginary heads are the causal driver of the long-context gains.

- **Efficiency variant with practical value.** RoPE++EH halves the KV cache and QKV parameters while maintaining comparable short-context performance (e.g., 776M average 42.5 vs. RoPE's 42.0, Table 1) and competitive long-context results, with concrete memory and speed measurements across context lengths (Figure 4).

- **Compatibility with existing length-extension techniques is demonstrated.** Table 3 shows that RoPE++ maintains its advantage when combined with Linear PI and YaRN, confirming that the method is orthogonal to and additive with other extrapolation approaches.

- **Code and checkpoints are publicly released**, supporting reproducibility.

## Weaknesses

### Major

1. **RoPE++EC comparison with vanilla RoPE is confounded by increased capacity.** The EC variant doubles the number of attention heads and doubles the output projection W_o compared to vanilla RoPE. While the paper frames this as "equal cache size," the total parameter count increases. The gains in Tables 1–3 could partly stem from having more heads available for semantic computation rather than specifically from the imaginary mechanism. A control experiment — vanilla RoPE with doubled heads and doubled W_o — would cleanly isolate the imaginary-attention contribution. The EH variant partially addresses this (same heads, halved cache), but EH's long-context results are mixed (see below).

2. **RoPE++EH shows inconsistent long-context gains.** At 776M on BABILong, RoPE++EH scores 19.4 vs. vanilla RoPE's 22.8 — a notable degradation. This is not discussed as a limitation. If imaginary attention is universally beneficial for long-context modeling, halving the cache (which still includes both real and imaginary heads) should not cause such a drop. The EH variant is presented as "comparable" but this specific result weakens the claim that imaginary attention is broadly helpful.

3. **Experimental scale is limited.** Validation is restricted to 376M and 776M parameters. Modern RoPE-based LLMs operate at 7B+ scales, and the paper provides no evidence that the benefits transfer. The claim that the method improves "LLMs" broadly would be stronger with at least one larger-scale demonstration or continued-pretraining experiments on an existing 7B checkpoint.

### Minor

1. **The shared-parameter constraint limits architectural flexibility.** Section 3.3 notes that "configurations such as 75% imaginary vs. 25% real or 100% imaginary are impossible under RoPE++" because real and imaginary heads must share W_q. This is a genuine limitation — the ratio of real to imaginary heads is always fixed at 1:1, which may not be optimal for all tasks or model depths.

2. **The theoretical derivation of the characteristic curve (Section 3.2) relies on approximations whose tightness is not characterized.** The transition from the discrete average over d/2 frequencies to the continuous integral form (Equation 5) uses an approximation whose error is not bounded. The integral form is qualitatively informative but the paper would benefit from quantifying how well it matches the discrete version for realistic d values.

### Trivial

- Figure 3's axis labels are small and hard to read; the "yellow" and "gray" shading distinction is not visible in black-and-white printing.

## Nice-to-Haves

- A "doubled-head vanilla RoPE" baseline to disentangle capacity from mechanism (as noted in Major weakness 1).
- Error bars or confidence intervals on the main benchmark results would strengthen the reliability assessment, though the authors note they pre-train from scratch which makes multiple runs expensive.

## Removed Points

The Harsh Critic provided no usable content (output was a non-English non-response). The Strength Finder's strengths were mostly verified and retained; a few generic phrasings ("the paper addressed an important problem") were dropped.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a controlled baseline: vanilla RoPE with doubled heads (matching RoPE++EC's head count) to isolate the imaginary-attention effect from increased model capacity.
2. Discuss the BABILong-776M EH degradation explicitly and explore why halving the cache hurts BABILong more than RULER.
3. If feasible, include a continued-pretraining experiment on an existing 7B-scale model (e.g., Llama-2-7B or Llama-3-8B) to demonstrate transferability to practical scales.
4. Quantify the approximation error in Equation 5 (discrete sum vs. continuous integral) for typical d values.

## Score and Decision

**Bracketing (Round 1):** Queries for weak anchors (avg ≤ 3.5) returned papers scoring 2.5–3.0 — clearly below this paper's quality. Queries for strong anchors (avg ≥ 7.5) returned papers scoring 8.0 with substantially broader scope or deeper theoretical novelty. The plausible bracket is (5.0, 7.0).

**Narrowing (Round 2):** Anchors within the bracket:

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| "Round and Round We Go! What makes Rotary Positional Encodings useful?" (GtvuNrk58a) | 6.20 | Similar mechanism-level analysis of RoPE. That paper had greater theoretical depth but weaker empirical evaluation (single model, perplexity only for proposed method). RoPE++ has stronger empirical evaluation but a more straightforward contribution. Comparable quality. |
| "Scaling Laws of RoPE-based Extrapolation" (JO7k0SJ5V6) | 5.00 | Theoretical framework for RoPE extrapolation. Weaker evaluation (mostly perplexity). RoPE++ is clearly stronger empirically. |
| "Wavelet-based Positional Representation for Long Context" (OhauMUNW8T) | 5.25 | Novel positional encoding method. Limited to perplexity evaluation, marginal empirical gains. RoPE++ has superior empirical validation. |
| "Stick-breaking Attention" (r8J3DSD5kF) | 6.50 | Fundamentally novel attention mechanism, broader contribution. Slightly more novel than RoPE++. |
| "Eliminating Position Bias" (fvkElsJOsN) | 6.60 | Different type of contribution (analysis + training-free fix), similar evaluation quality. |

The paper is stronger than the 5.0–5.25 anchors (Scaling Laws, Wavelet-based) due to its thorough evaluation and causal ablation. It is comparable to the "Round and Round" paper (6.20) — both have a clean idea, theoretical analysis, and empirical validation, though "Round and Round" has more mechanistic depth while RoPE++ has broader evaluation. The confounded EC comparison and mixed EH results prevent it from reaching the 6.5+ range. The final score of **6.0** reflects a solid, well-executed contribution with real but not fatal limitations.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>