## Summary

The paper proposes RoPE++, which re-introduces the imaginary component of the complex-valued RoPE dot product into attention computation. By rotating query vectors by -π/2 before applying standard RoPE, the method computes additional "imaginary" attention heads in parallel. Two configurations are presented: RoPE++_EC (equal KV cache, doubled heads) which improves performance, and RoPE++_EH (equal heads, halved KV cache) which saves memory. Experiments at 376M and 776M scales with 50B pre-training tokens show improvements over vanilla RoPE on short- and long-context benchmarks, with theoretical analysis suggesting imaginary attention preferentially captures long-range dependencies.

## Strengths

- **Mathematically clean derivation (Equations 3–4, Section 3.1):** The paper shows that imaginary attention can be computed by a simple -π/2 rotation of the query vector before applying the standard RoPE embedding, with no change to key embeddings. This preserves the dual absolute-relative position encoding property of RoPE and can be implemented as a trivial linear transformation on queries.

- **Characteristic-curve analysis (Section 3.2, Equation 5):** The paper derives that the imaginary attention's expected value follows a sine-integral function Si(Δt) that decays more slowly at large distances than the cosine-based decay of real attention. This provides a concrete theoretical mechanism — grounded in RoPE's frequency distribution — explaining why imaginary heads should preferentially capture long-range dependencies.

- **Two practical configurations with explicit trade-offs:** RoPE++_EH (equal heads, halved cache) is validated with memory and latency measurements (Figure 4) showing consistent reductions that widen with context length, while RoPE++_EC (equal cache, doubled heads) achieves higher performance. Both are evaluated at non-trivial scale (376M–776M, 50B pre-training tokens + 10B long-context tokens), which is a genuine pretraining effort rather than analysis on a single pretrained model.

- **Compatibility with existing long-context techniques (Table 3):** RoPE++ combined with both Linear PI and YaRN consistently outperforms vanilla RoPE under both interpolation schemes, showing the method generalizes beyond the NTK-based extension used in the main experiments.

## Weaknesses

### Major

- **No ablation controlling for the doubled head count in RoPE++_EC.** RoPE++_EC doubles the number of attention heads while keeping the KV cache equal to vanilla RoPE. Its gains on long-context tasks (e.g., RULER 376M: 25.0 vs 18.8; BABILong 376M: 16.1 vs 11.0) could partly come from having more attention heads — a well-known way to improve Transformer performance — rather than from the imaginary computation specifically. A controlled baseline comparing vanilla RoPE with the same number of heads (e.g., halving head dimension while keeping model dimension constant) is necessary to disentangle these effects. RoPE++_EH partially addresses this concern by keeping head count equal, but the largest gains are in the EC variant, so the core claim that "imaginary attention plays a more dominant role in long context modeling" rests primarily on confounded evidence.

### Minor

- **The noise perturbation experiment (Section 5.2) assigns even-index heads to real attention and odd-index heads to imaginary attention.** Since head importance can vary systematically by index, the experiment does not fully rule out the possibility that odd-index heads are inherently more important for long-context regardless of real/imaginary assignment. A control condition that swaps the assignment (making even-index heads imaginary and odd-index heads real) would strengthen the causal claim.

- **RoPE++_EH sometimes underperforms vanilla RoPE on long-context tasks without discussion.** At 776M, RoPE++_EH scores 19.4 on BABILong average vs 22.8 for vanilla RoPE — a meaningful regression. At 376M on RULER, it scores 18.2 vs 18.8. The paper notes that "RoPE occasionally edges ahead at a few shorter context lengths" (a statement that also describes the *long*-context results), but does not analyze what these patterns mean or when the imaginary component helps vs hurts.

- **The theoretical argument in Section 3.4 (length extrapolation) is compressed.** The claim that RoPE++ exposes dimensions to a wider positional value range relies on claims about when cos/sin values are "always non-negative" that depend on specific θ_n values. The reasoning would benefit from a more quantitative treatment.

### Trivial

- Single-run results without variance estimates are reported throughout. Given the small margins on short-context tasks (e.g., 376M short-context: RoPE++_EC 41.0 vs RoPE 40.1, a 0.9-point gain over 11 tasks), it is unclear whether these differences are stable across random initializations. However, this is standard practice for LLM pretraining at this scale due to cost.

## Nice-to-Haves

- A comparison of RoPE++_EH against other cache-reduction techniques (e.g., MQA or grouped-query attention with fewer groups) at the same cache budget would better contextualize its efficiency advantages.
- An analysis of the BABILong 776M regression for RoPE++_EH (19.4 vs 22.8) could help characterize when imaginary attention is beneficial vs detrimental.

## Removed Points

*These points were flagged for removal from the Harsh Critic and Strength Finder inputs. They are included here for completeness but should not be weighed in the final evaluation.*

1. **Criticism that the "discarded imaginary information" framing is misleading.** REMOVED (factually incorrect — the complex-multiplication formulation of RoPE is the standard mathematical representation from the original RoPE paper; taking the real part of this complex product is a valid description of what standard implementations compute, and the remaining imaginary part is indeed not used. This is not a misrepresentation.)

2. **Request for random seeds, multiple runs, and variance estimates.** DEMOTED to trivial (single-run evaluation is standard for LLM pretraining at this scale due to computational cost; this is a nice-to-have, not a structural weakness.)

3. **Claims about missing appendix content (architecture details, parameter counts).** REMOVED (the appendix was stripped by the parser; it exists in the original submission.)

4. **Nitpicks about undisclosed hyperparameters or trivial implementation details.** REMOVED (standard practice for this type of work.)

5. **Strength Finder items claiming generic importance of the problem.** REMOVED (generic — the specific, grounded strengths are retained above.)

## Novel Insights

The harsh critic's observation about RoPE++_EH's regression on BABILong 776M (19.4 vs 22.8) is particularly noteworthy because it suggests that the imaginary component may sometimes crowd out useful local attention patterns needed for precise reasoning tasks. This tension between the imaginary component's long-range bias and the real component's local precision is a direction the paper does not explore but that could yield interesting insights about when and why RoPE++ helps or hurts.

## Suggestions

1. **Run RoPE++_EC against a vanilla RoPE baseline with the same number of attention heads** (same model dimension with halved head dimension) to disentangle head-count effects from imaginary-component effects. This is the most important missing experiment.

2. **In the noise experiment, run a control condition that swaps real/imaginary assignment** across head indices (make even-index heads imaginary and odd-index heads real).

3. **Analyze the BABILong 776M regression** for RoPE++_EH — characterize whether this is a systematic pattern for certain task types or a statistical fluctuation.

4. **Provide a more quantitative treatment of the length extrapolation argument** (Section 3.4) with explicit discussion of which dimensions benefit and under what conditions.

## Score and Decision

**Round 1 (Bracketing):** The paper was compared against three score bands on the topic of "RoPE rotary position embedding modification for long context language models":
- Low band (score < 3.5): avg scores 2.50–3.00 — clearly weaker papers with minimal or no pretraining experiments
- Middle band (3.5–7.5): avg scores 5.00–6.50 — including "Round and Round We Go!" (6.20), "Scaling Laws of RoPE-based Extrapolation" (5.00), "Why Does Effective Context Length Fall Short?" (6.50), "PoSE" (6.00)
- High band (> 7.5): avg score 8.00 — strong papers on other topics

The paper clearly belongs in the middle band, with an initial bracket of 5.0–6.5.

**Round 2 (Narrowing):** The search was refined within the 5.0–6.5 range for RoPE modification and long-context position embedding papers. Additional anchors included "Contextual Position Encoding" (5.25, rejected), "Wavelet-based Positional Representation" (5.25, accepted), "DAPE V2" (5.33, rejected), and "Rethinking Addressing/TAPE" (6.00, rejected).

**Final calibration:** The paper is stronger than "Scaling Laws of RoPE-based Extrapolation" (5.00, accepted with controversy) due to more thorough evaluation including downstream benchmarks. It is comparable to "Wavelet-based Positional Representation" (5.25, accepted) and PoSE (6.00, accepted). However, it is weaker than "Round and Round We Go!" (6.20, accepted) because that paper's methodological gap (limited model diversity) is less severe than this paper's head-count confound. Compared to "Why Does Effective Context Length Fall Short?" (6.50, accepted), this paper validates at smaller scale. The head count confound for the paper's strongest variant prevents the evidence from cleanly supporting the core claim about the imaginary component's special role.

| Anchor Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Long-context Extrapolation via Periodic Extension | jp4pxKqCRW.md | 2.50 | 1 | Much weaker — minimal experiments |
| Efficient transformer reinforced PE | 5dDYhvt6dY.md | 3.00 | 1 | Much weaker — different domain |
| Writing in the Margins | 56mg1JFd3n.md | 6.00 | 1 | Stronger — larger-scale validation |
| Round and Round We Go! | GtvuNrk58a.md | 6.20 | 1,2 | Stronger — cleaner evaluation despite less extensive experiments |
| Scaling Laws of RoPE-based Extrapolation | JO7k0SJ5V6.md | 5.00 | 1,2 | Slightly weaker — evaluation limited mostly to perplexity |
| Why Does Effective Context Length Fall Short? (STRING) | eoln5WgrPx.md | 6.50 | 1,2 | Stronger — validated on 70B models, training-free |
| Rethinking Addressing (TAPE) | Us1RXG1Ji2.md | 6.00 | 1,2 | Comparable but rejected due to other issues |
| Contextual Position Encoding | sIGWTd1DcW.md | 5.25 | 3 | Slightly weaker — less thorough experiments |
| Wavelet-based Positional Representation | OhauMUNW8T.md | 5.25 | 3 | Comparable — both have genuine contributions with gaps |
| PoSE | 3Z1gxuAQrA.md | 6.00 | 2,3 | Stronger — clear practical contribution, cleaner experiments |
| What is Wrong with Perplexity | fL4qWkSmtM.md | 6.80 | 2 | Stronger — different contribution type |

The final score of 5.5 reflects a paper that makes a mathematically sound and practically motivated contribution, evaluated at non-trivial scale, but whose central claim is undercut by an unaddressed confound (doubled head count in the best-performing variant).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>