## Summary

The paper proposes **RoPE++**, an extension of Rotary Position Embeddings that re-incorporates the imaginary component of the complex-valued attention score, which is discarded in standard RoPE. The key insight is that the imaginary attention score has a sine-integral characteristic curve (rather than cosine), which decays more slowly with distance, enabling better long-range dependency modeling. Two configurations are introduced: RoPE++_EH (equal heads, halved KV cache/QKV parameters) and RoPE++_EC (equal cache, doubled attention heads). Both outperform vanilla RoPE on short- and long-context benchmarks at 376M and 776M parameter scales.

---

## Strengths

- **Clean mathematical observation with an elegant implementation.** Standard RoPE discards the imaginary part of the complex product entirely. RoPE++ reintroduces it by noting that imaginary attention reduces to standard RoPE with a fixed −π/2 rotation of the query, so it runs in a single FlashAttention pass with **zero additional KV cache** for RoPE++_EC. This is an unusually clean add-on to an existing architecture.

- **Theoretically grounded characteristic-curve analysis.** The paper analytically derives the expected attention bias curves for both real and imaginary heads (cosine-integral vs. sine-integral form, Equation 5). The argument that the sine-integral decays much more slowly and thereby facilitates long-range information retrieval is well-posed and distinguishes this work from purely empirical methods.

- **Empirical validation across diverse settings.** The improvement holds consistently across two model sizes (376M, 776M), multiple long-context benchmarks (RULER, BABILong up to 64k), and two interpolation strategies (PI, YaRN in Table 3). The ablation using Gaussian noise injection (Section 5.2) provides causal evidence that imaginary heads disproportionately contribute to long-context performance (~8-point gap at σ=1.0, 776M scale).

- **Length-extrapolation analysis is novel.** Section 3.4 identifies that, under RoPE, low-frequency dimensions see only non-negative cosine values during pre-training and encounter OOD negative values at extrapolation time. RoPE++ exposes those dimensions to the full [−1, +1] range during training, a concrete and previously unrecognized mechanism for improved extrapolation.

- **Practical efficiency demonstrated.** Figure 4 confirms that RoPE++_EH reduces memory cost and improves TPOT across context lengths 2k–32k, with the gap widening at longer contexts, validating the efficiency motivation for RoPE++_EH.

---

## Weaknesses

### Fatal
None.

### Major

1. **Scale limited to 376M–776M parameters.** All experiments are conducted at sub-1B scale. Modern production LLMs that would benefit most from improved long-context handling operate at 7B–70B+. The interaction between RoPE++ and scaling behavior — particularly whether the sine-based bias in imaginary heads survives the gradient dynamics of large models — remains unvalidated. Given that prior work (e.g., ablations on head specialization) sometimes shows qualitatively different behavior at scale, this is a meaningful gap in the empirical story.

2. **Long-context baselines incomplete.** Table 2 omits FoPE, Pythia, and ALiBi from the long-context comparison. Since these methods were trained with the same 4k pre-training setup and are compared on short-context tasks, the absence of an equivalent long-context fine-tuning comparison leaves the reader unable to judge whether the gain over these alternatives persists. The claim that "RoPE++ acquires the highest scores" in the long-context setting is only relative to vanilla RoPE.

3. **Absolute long-context performance is low.** RULER averages of 18–29 (out of 100) and BABILong averages of 11–24 reflect highly limited long-context capability for these model sizes. It is difficult to judge whether the reported gains (e.g., +6.2 on RULER avg at 376M) would remain meaningful or even directionally correct when these tasks are well within a larger model's capability. The practical significance of observed deltas is unclear.

### Minor

1. **RoPE++_EH trades capacity for efficiency in an understudied way.** Halving K/V dimensions means each key–value pair has half the expressive capacity. The paper argues the imaginary-head pair compensates, but no ablation isolates whether the KV compression itself harms performance at longer contexts or specialized task types. The comparison in Table 2 is promising but too coarse to be conclusive here.

2. **The noise-injection experiment does not account for scale sensitivity.** The experiment uses fixed σ values (0.2–1.5) without normalizing for the scale of the attention logits, which may differ between real and imaginary heads due to architectural differences. This slightly weakens the causal interpretation.

### Trivial
None worth noting.

---

## Nice-to-Haves

- A proof-of-concept or scaling law experiment at 3B–7B to show that the gain trend holds beyond 776M.
- Measurement of training FLOPs for each configuration to clarify the efficiency trade-offs during the forward pass (not just inference throughput).
- Ablation comparing imaginary attention alone (all heads imaginary) vs. mixed configurations, even if 100% imaginary is theoretically limited, a sweep from 25% to 75% would clarify the optimal balance.

---

## Novel Insights

The deepest insight in this paper is not the performance improvement per se, but the **complementarity of cosine- and sine-modulated attention biases as positional signals**. Standard RoPE commits entirely to cosine-integral decay (localist attention), while imaginary attention provides a sine-integral bias that saturates slowly and spreads attention across long contexts. Combining them is essentially a spectral decomposition of positional information: each frequency contributes both in-phase and quadrature components to the attention logit, exposing the model to the full Fourier spectrum of relative positions. This perspective, together with the observation that RoPE's training-time position-embedding range is actually *doubled* by combining real and imaginary phases, is a genuinely novel framing of why long-context extrapolation struggles with RoPE and how it can be systematically alleviated.

---

## Suggestions

- Include at least one 3B–7B scaling point — even a 1B-token "sanity-check" pre-training — to validate that the long-context advantage does not diminish at realistic deployment scales.
- Report FLOPs (training and inference) per token in a dedicated table to make the cost–benefit analysis precise for practitioners choosing between RoPE++_EC and RoPE++_EH.
- Add FoPE and ALiBi to the long-context fine-tuning comparison in Table 2 so the claimed advantage is unambiguous across all baselines.
- Provide a heatmap analysis of which specific RULER sub-tasks (multi-key retrieval, multi-value retrieval, etc.) imaginary heads improve most, as this would shed light on the mechanistic story.

---

## Score and Decision

The paper makes a clear, mathematically clean observation about an information-theoretic gap in standard RoPE that has been universally overlooked, derives a near-zero-cost fix, provides a well-structured theoretical analysis, and supports it with consistent empirical gains across multiple benchmarks. The missing dimension is scale: the entire empirical case rests on sub-1B models, which limits confidence in practical relevance for today's LLMs. The incomplete long-context baseline comparison is a secondary but real gap. These weaknesses are significant enough to prevent a clear accept, but the originality and internal rigor of the paper make it a genuine contribution to the positional-embedding literature.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>