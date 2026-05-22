Now I have a complete picture. Let me write the final consolidated review.

## Summary

This paper proposes RoPE++, an extension of Rotary Position Embeddings (RoPE) that computes an additional set of attention heads by rotating queries by $-\pi/2$ before applying the standard RoPE transformation. The authors show that this "imaginary attention" has different characteristics from standard "real attention" — it exhibits a slower-decaying attention pattern over distance — and that adding it alongside standard RoPE attention improves performance on both short- and long-context benchmarks at 376M and 776M scales. Two configurations are explored: RoPE++$_{EC}$ (equal KV cache, doubled effective heads) and RoPE++$_{EH}$ (equal head count, half the KV cache and QKV parameters).

## Strengths

1. **Novel and computationally clean architectural modification.** The core idea — computing an additional attention head by rotating the query by $-\pi/2$ (equivalent to re-introducing what would be the imaginary part of the complex RoPE product) — is simple, well-motivated mathematically (Equations 2–4), and requires only a fixed rotation operation, making it straightforward to implement in existing RoPE-based systems including FlashAttention. The paper correctly shows that the new term preserves the unified absolute–relative position embedding format of RoPE (Equation 4).

2. **Consistent empirical gains for RoPE++$_{EC}$.** Across 11 short-context tasks at two model sizes, RoPE++$_{EC}$ achieves the highest average score in every condition (Table 1). On long-context benchmarks RULER and BABILong up to 64k, RoPE++$_{EC}$ consistently outperforms vanilla RoPE by substantial margins (e.g., 376M RULER Avg 25.0 vs 18.8; 776M BABILong Avg 24.1 vs 22.8 in Table 2). The gains grow with context length, supporting the claim that the imaginary attention is especially beneficial for long-range dependencies.

3. **Noise-based ablation provides mechanistic evidence.** The experiment in Section 5.2 (Figure 5e,j) shows that corrupting the imaginary attention heads degrades RULER-4k performance more severely (by 5–8 points at $\sigma=1.0$) than corrupting the real attention heads. This directly supports the claim that the imaginary heads are disproportionately important for long-context modeling, and it is a creative analysis that goes beyond reporting aggregate scores.

4. **Practical efficiency variant with reasonable trade-offs.** RoPE++$_{EH}$ achieves comparable or slightly better results than vanilla RoPE on short tasks with half the KV cache and QKV parameters, and the efficiency gains widen with context length (Figure 4). On the 376M model, the long-context average is competitive (RULER Avg 18.2 vs 18.8, BABILong Avg 11.6 vs 11.0), demonstrating a useful compute–performance trade-off.

5. **Thorough comparison against multiple position embeddings.** The paper compares against FoPE, Pythia (partial RoPE), and ALiBi in addition to vanilla RoPE, and tests both short-context (4k) and long-context (32k training, up to 64k evaluation) regimes with separate pre-training runs. The method is also shown to combine with existing extension techniques (YaRN and Linear PI, Table 3).

## Weaknesses

### Fatal
None.

### Major

1. **Missing control baseline: RoPE with doubled heads for RoPE++$_{EC}$.** The RoPE++$_{EC}$ variant doubles the effective number of attention heads while keeping the KV cache the same size. The paper does not compare against standard RoPE with the same doubled head count (proportional QKV parameters). Without this baseline, we cannot attribute the performance gains to the specific $-\pi/2$ rotation rather than simply having more heads. The noise experiment (Section 5.2) only shows that within the RoPE++ model, imaginary heads are more important than real heads — it does not show they are better than additional *randomly initialized* or *standard* heads would be. This is the most significant experimental gap in the paper. The RoPE++$_{EH}$ variant (same heads, half parameters) partially mitigates the concern by showing that a parameter-reduced version is competitive, but the core attribution question for $_{EC}$ remains open.

### Minor

2. **Framing overreach: "discarded imaginary information."** The paper repeatedly states that standard RoPE "discards the imaginary component" of the complex product. In practice, standard RoPE is implemented as a vector rotation in real space; the real-valued attention score already contains both cosine and sine cross-dimensional terms (Equation 1). The proposed "imaginary" term is a *different* bilinear form (obtained by a $-\pi/2$ rotation of the query), not a "recovered" signal. The mathematics of the method is correct, but the framing is overstated and could mislead readers. Better described as "adding a parallel attention head with a fixed rotation of Q."

3. **RoPE++$_{EH}$ shows inconsistent long-context performance at 776M.** At 776M scale on BABILong, RoPE++$_{EH}$ underperforms vanilla RoPE by a notable margin (Avg 19.4 vs 22.8, Table 2). The paper describes this as "comparable results with half the cache," which is misleading when the gap is ~15% relative. While $_{EH}$ performs well at 376M and on RULER, this inconsistency weakens the claim that imaginary attention universally helps across scales and task types.

4. **Limited scale of validation.** Experiments are conducted only at 376M and 776M parameters. Long-context behaviors can differ at larger scales (7B+), and the method's overhead (doubled effective query heads for EC) becomes more practically significant at scale. The paper mentions "analysis on larger model scale" in Appendix C (which the parser strips), but the main text provides no evidence beyond sub-1B models. Given that related work on position embeddings often validates at 7B+, this is a meaningful limitation.

5. **Theoretical justification is heuristic.** The claim that imaginary attention better captures long dependencies is based on the characteristic curve of $\mathbb{E}[\sin(\theta\Delta t)]$, which decays more slowly than $\mathbb{E}[\cos(\theta\Delta t)]$ (Equation 5, Figure 1). However, raw sine oscillates and can be negative, and the actual attention depends on learned query/key content. The argument that slow decay implies better long-context capture is intuitive but not rigorous, and the paper does not causally link the sine integral to the observed performance gains beyond correlation.

6. **RoPE++$_{EH}$ shows degradation when combined with YaRN at 376M.** In Table 3, RoPE++$_{EH}$ with YaRN at 376M achieves an average RULER score of 24.7 vs RoPE's 28.2, a considerable drop. The paper focuses on $_{EC}$'s success in this section but does not adequately discuss why $_{EH}$ sometimes hurts performance when combined with interpolation methods.

### Trivial
None.

## Nice-to-Haves

- **Add the doubled-head RoPE baseline** for RoPE++$_{EC}$ to isolate the effect of the rotation from increased head count.
- **Validate on at least one model at 2.8B–7B scale** to demonstrate scalability.
- **Include real long-context tasks** (e.g., LongChat, L-Eval, NarrativeQA, or passkey retrieval) alongside the synthetic RULER/BABILong benchmarks to strengthen practical relevance.
- **Ablate on the rotation angle:** Compare $-\pi/2$ against other fixed rotations (e.g., $-\pi/4$, $\pi/2$, random rotation) to test whether the specific imaginary component is necessary or if any fixed rotation yields similar gains.

## Removed Points

*These points are flagged to be removed. Treat them with caution.*

- **Harsh Critic Issue 1 labeled as "fatal" / "invalidates core claim."** The "discarded imaginary information" framing is overstated (retained as Minor Weakness #2 above), but the method itself is mathematically sound and well-defined. Calling this fatal is disproportionate — the paper's core technical contribution does not depend on this framing. The critic's claim that "the real attention already contains both cosine and sine terms" is correct, but the imaginary attention is a *different* bilinear form, which is a genuine addition. Downgraded from "invalidates core claim" to Minor (framing issue).

- **Critic's claim that "the negative sign is arbitrary" (Section 3.1).** The paper explicitly justifies the negative sign in Section 3.2: "For $\Delta t > 0$, when $q_t, k_s$ are similar, their attention is on average larger regardless of relative distance, which is the reason why we take the negative imaginary part as imaginary attention." This justification is present in the paper. REMOVED — reviewer missed the explanation.

- **Critic's claim that the noise experiment "only [shows] one level of noise ($\sigma=1.0$)."** The paper discusses the full range: "When $\sigma$ is small ($\sigma < 0.2$)... when it is large enough ($\sigma = 1.5$), both drop sharply. Importantly, in the intermediate range..." The specific claim of "5–8 point gap" is at $\sigma=1.0$ and is presented alongside the full-curve discussion. The paper does not hide the broader curve. REMOVED.

- **Critic's claim that the paper uses "only synthetic RULER/BABILong" with "no real long-context tasks."** Table 1 evaluates 9 real downstream tasks (TruthfulQA, PIQA, HellaSwag, Winogrande, ARC-e, GPQA, SocialIQA, OpenBookQA, SuperGLUE) plus WikiText and LAMBADA perplexity — these are real, not synthetic. Only the long-context benchmarks (RULER, BABILong) are synthetic, which is standard practice in this subfield. REMOVED.

- **Strength Finder's generic strengths about the problem being "important" or "addressing a relevant problem."** Dropped per instructions about removing generic/superficial strengths. The remaining strengths are specific and evidence-backed.

## Novel Insights

The reviewers' analyses surface an insight not fully articulated in the paper: the $-\pi/2$ rotation can be understood as generating a *quadrature* pair of attention heads, analogous to the sine/cosine pair in a Fourier decomposition. Just as a complex number's real and imaginary parts encode complementary phase information, the real and imaginary attention heads encode complementary positional patterns (local vs. global). This perspective could unify RoPE++ with other dual-attention designs and suggests that the benefit may come from having two orthogonal positional projections rather than from "recovering lost information" per se. The paper would be strengthened by making this Fourier/quadrature perspective explicit in the motivation.

## Suggestions

1. **Reframe the contribution** as "adding a parallel attention head via $-\pi/2$ query rotation that produces a complementary long-range attention pattern" rather than "recovering discarded imaginary information." The latter framing is contentious and distracts from the valid technical contribution.

2. **Add the critical missing baseline**: standard RoPE with doubled heads and proportional parameters. This single experiment would resolve the main attribution concern and substantially strengthen the paper.

3. **Test at a larger scale.** Even a shorter pre-training run (e.g., 10B tokens) at 2.8B or 7B would significantly increase confidence in the method's generality.

4. **Be more precise about the parameter budget.** Clarify for RoPE++$_{EC}$ how $W_q$ size changes (or doesn't change) relative to the baseline — a simple table showing head count, head dimension, QKV parameter counts, and FLOPs for each variant would eliminate ambiguity.

5. **Address the $_{EH}$ inconsistency** at 776M on BABILong and with YaRN. If $_{EH}$ does not universally help, the paper should clearly characterize the conditions under which it works vs. doesn't, rather than describing all results as "comparable."

## Score and Decision

**Calibration anchors** (all retrieved in a single batch):

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jp4pxKqCRW.md` (Long-context Extrapolation via Periodic Extension) | 2.50 (Reject) | Weaker on all axes: poorer writing, less rigorous experiments, weaker theory. Current paper clearly stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KJLqgaixgn.md` (Sparse Training) | 3.50 (Reject) | Lower-quality submission on a different problem. Current paper has clearer contribution and more thorough experiments. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/t717joHHSc.md` (Mitigate Position Bias) | 4.75 (Reject) | Similar tier — both have an interesting idea with limited validation. Current paper has more rigorous training and evaluation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JO7k0SJ5V6.md` (Scaling Laws of RoPE-based Extrapolation) | 5.00 (Accept) | Similar tier: a solid contribution with notable weaknesses. The scaling laws paper had mixed reviews (scores 1,6,8) and was accepted. Current paper is similarly positioned — real contribution, incomplete experimental design. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3Z1gxuAQrA.md` (PoSE) | 6.00 (Accept) | Stronger paper: larger-scale validation (LLaMA 7B, up to 128k), cleaner framing. Current paper's core idea is more novel, but PoSE has stronger empirical support. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GtvuNrk58a.md` (Round and Round We Go!) | 6.20 (Accept) | Stronger paper: insightful mechanistic analysis on 7B models, rigorous theoretical framing. Current paper has more comprehensive downstream evaluation but at much smaller scale. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eoln5WgrPx.md` (STRING) | 6.50 (Accept) | Stronger paper: demonstrates training-free gains on 70B models, clean motivation. Current paper's contribution is more novel architecturally but falls short on scale and experimental rigor. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6PmJoRfdaK.md` (LongLoRA) | 7.00 (Accept) | Substantially stronger: efficient fine-tuning at 7B–70B scale, clear practical impact. Current paper is not in the same tier. |

Positioned relative to these anchors, this paper has a genuinely novel core idea, clean math, and decent small-scale validation, but the experimental design has a notable gap (missing doubled-head baseline) and the framing is overstated. It is stronger than the 2.50–3.50 papers, comparable to the 5.00 paper, but clearly weaker than the 6.00+ papers primarily due to limited scale and the missing control experiment.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>