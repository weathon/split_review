Now I have sufficient calibration data. Let me write the final review.

## Summary

This paper identifies that standard RoPE discards the imaginary component of the complex-valued attention score, and proposes RoPE++ to re-incorporate it as a separate group of attention heads. The authors derive that imaginary attention's characteristic curve (a sine integral) decays more slowly than real attention's cosine integral, theoretically favoring longer dependencies. Two configurations are introduced: RoPE++_EC (equal cache, doubled attention heads) and RoPE++_EH (equal heads, halved KV cache). Pre-training experiments at 376M and 776M scales show gains on short- and long-context benchmarks.

## Strengths

1. **Clean theoretical derivation of the imaginary attention mechanism.** Section 3.2 derives the characteristic curve of imaginary attention (Eq. 5, sine integral) and shows it decays more slowly than real attention's cosine integral (Figure 1), providing a principled mathematical reason why the imaginary component could capture longer dependencies.

2. **Practical efficiency contribution via RoPE++_EH.** RoPE++_EH achieves comparable long-context performance to vanilla RoPE while halving the KV cache and QKV parameters. Figure 4 shows memory cost and TPOT advantages that widen with context length — a practically useful result independent of any long-context quality claim.

3. **Noise ablation experiment directly links imaginary heads to long-context performance.** Section 5.2 adds Gaussian noise to real vs. imaginary heads separately: at σ=1.0, the imaginary-corrupted variant underperforms the real-corrupted variant by 5 points (376M) and 8 points (776M) on RULER-4k (Figure 5e, 5j). This causal intervention provides evidence that the imaginary component is functional, not just decorative.

4. **Compatibility with existing long-context adaptation methods is validated.** Table 3 shows that RoPE++_EC improves over vanilla RoPE under both Linear PI and YaRN consistently (e.g., 376M YaRN RULER avg: 29.8 vs. 28.2), demonstrating that the method generalizes beyond a single training recipe.

## Weaknesses

### Fatal
None.

### Major

1. **RoPE++_EC's gains are confounded with increased attention head count — the central claim is not cleanly supported.** RoPE++_EC doubles the number of attention heads (and doubles W_o) while keeping KV cache equal. The paper does not include a controlled baseline where vanilla RoPE also uses the doubled head architecture (all heads real-valued, same total head count). Without this, the strong RULER and BABILong gains of RoPE++_EC (25.0 vs. 18.8 at 376M, Table 2) cannot be cleanly attributed to the imaginary component rather than to the increased representational capacity from more attention heads. The RoPE++_EH variant, which does control for total head count, shows only mixed results — comparable or slightly better on some metrics, worse on others (e.g., 776M BABILong: 19.4 vs. 22.8, Table 2). This inconsistency further weakens the claim that the imaginary component itself drives long-context improvement. The noise ablation (Section 5.2) provides partial supporting evidence, but operates within the confounded architecture and does not substitute for a clean between-model comparison.

2. **The length extrapolation claim (Section 3.4) lacks direct empirical validation.** The paper argues that RoPE++ improves length extrapolation because imaginary attention exposes dimensions to a wider range of sinusoidal values during training. However, all long-context results in Tables 2 and 3 are obtained after further training at 32k context length with base scaling — measuring adaptation, not zero-shot extrapolation. No experiment evaluates a model trained only at 4k on contexts longer than 4k, which is the standard way to test extrapolation. The theoretical analysis is interesting but remains unvalidated without this experiment.

### Minor

3. **No variance or statistical significance reporting.** Results are reported from single runs without confidence intervals, standard errors, or multiple seeds. Many short-context improvements are small (0.2–2.0 average points, Table 1), making it impossible to assess whether they are meaningful given the natural variance at 50B-token training budgets. While multi-seed training at this scale is expensive, some discussion of expected variance or a smaller-scale multi-seed experiment would strengthen the claims.

4. **Potential concern about the sine integral's non-decaying behavior is not discussed.** As the paper notes, the imaginary attention's characteristic curve (Figure 1) does not decay to zero but approaches a constant, producing an oscillatory long-range baseline. The paper does not discuss how the model might learn to use this oscillatory signal or whether the constant baseline could drown out content-based attention. This is not a fatal flaw but deserves analysis.

### Trivial
None.

## Nice-to-Haves
- Evaluate on a natural long-context benchmark (e.g., LongBench, Needle-in-a-Haystack) alongside the synthetic RULER and BABILong.
- Test zero-shot length extrapolation from 4k-trained models to 8k–32k contexts to directly validate Section 3.4.
- Provide a small-scale multi-seed experiment or variance estimate for the key comparisons.

## Removed Points
- **Criticism about missing YaRN/PI baselines (Harsh Critic).** The reviewer claimed "YaRN and PI alone are not compared as baselines." This is factually wrong — Table 3 includes RoPE (without RoPE++) under both PI and YaRN as baselines. **Removed** (factual error).
- **Criticism about no natural long-context benchmarks.** This is scope creep — the paper uses standard synthetic benchmarks (RULER, BABILong) that are widely accepted for measuring long-context ability. **Removed** (scope creep; moved to Nice-to-Haves).
- **Criticism about testing only up to 64k.** The paper's claims are about the proposed mechanism, not about achieving specific context lengths. Testing at 64k is reasonable for the model sizes used. **Removed** (scope creep).
- **Criticism about FLOPs analysis for RoPE++_EC.** The paper describes that W_o is double-sized and head groups are doubled, which clearly implies the compute trade-off. **Removed** (already addressed by the paper's own description).
- **Strength Finder's generic strengths** about "addressing an important problem" or "well-motivated." **Removed** (generic/superficial).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add the controlling experiment that is most needed:** Train a vanilla RoPE model with the same total attention head count as RoPE++_EC (all heads real-valued), matching the doubled W_o size. If RoPE++_EC still outperforms this baseline on long-context benchmarks, the imaginary component's contribution would be cleanly isolated. This single experiment would substantially strengthen the paper's central claim.
2. **Add a zero-shot extrapolation experiment:** Evaluate models trained only at 4k context on sequences of 8k, 16k, and 32k (perplexity or RULER) to directly test the extrapolation claim in Section 3.4.
3. **Consider reframing the paper around the efficiency contribution of RoPE++_EH,** which is better supported by the current evidence, and positioning the RoPE++_EC long-context advantage as suggestive rather than definitive.

## Score and Decision

**Round 1 bracket:** After comparing to low-score anchors (1.5–3.0, withdrawn/reject RoPE papers), middle-score anchors (4.0–6.5, RoPE modification papers), and high-score anchors (8.0+, unrelated), I placed the paper between 3.5 and 5.5.

**Round 2 narrowing:** Compared the paper against specific anchors:
- *MrRoPE* (6.50, Oral): Clearly stronger — deep theoretical framework, training-free, no confound. Paper under review is weaker.
- *Frayed RoPE* (6.00, Poster): Stronger — deep geometric analysis, training-free. Paper under review is weaker.
- *Frequency Bands in RoPE* (5.20, Poster): Careful empirical analysis with some theoretical backing. The paper under review has a more architectural contribution but a more serious experimental confound. Comparable or slightly weaker.
- *PoPE* (4.00, Reject): Similar profile (RoPE modification, confound issue) but less comprehensive evaluation. Paper under review is slightly stronger.
- *AlphaRoPE* (4.00, Reject): Incremental RoPE scaling method. Paper under review has comparable quality and slightly broader evaluation.

**Final position:** The paper has a genuinely interesting core idea and some supporting evidence (theoretical derivation, noise ablation, efficiency variant), but the most headline claim about RoPE++_EC's long-context superiority is undermined by the confound with doubled attention heads. The missing controlled baseline prevents clean attribution. Compared to the anchors, the paper sits between the 4.0 (Reject) and 5.2 (Poster) level — above clearly flawed papers but below the well-controlled RoPE+ papers. I assign **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>