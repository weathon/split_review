Now I have a clear picture of where this paper sits. Let me compose the final review.

---

## Summary

RoPE++ re-incorporates the imaginary component of the complex-valued RoPE attention dot product — normally discarded — as a parallel set of "imaginary" attention heads. The method requires only a −π/2 rotation of query vectors, introduces no new KV cache, and yields two configurations: RoPE++_EH (equal heads, halved KV cache) and RoPE++_EC (equal cache, doubled heads). Pre-training experiments at 376M and 776M scales show consistent gains over standard RoPE on both short-context and long-context benchmarks, with the advantage growing at longer context lengths. Noise-injection experiments confirm that the imaginary heads are the primary driver of long-context performance.

## Strengths

- **Mathematically clean derivation with strong theoretical motivation**: The paper shows that the imaginary attention can be expressed identically to real attention with a simple −π/2 query rotation (Eq. 3–4), and derives its characteristic curve as a sine integral function (Eq. 5) that decays far more slowly than the cosine-based real attention curve — providing a principled explanation for why imaginary heads should favor long-range dependencies.

- **Comprehensive and consistent long-context improvements**: On RULER and BABILong up to 64k, RoPE++_EC substantially outperforms standard RoPE at both 376M and 776M scales (e.g., 776M: RULER avg 29.4 vs. 27.4, BABILong 24.1 vs. 22.8 in Table 2). RoPE++_EH matches or exceeds RoPE while using half the KV cache. The gap widens with context length, directly supporting the core claim.

- **Convincing mechanistic evidence**: Attention-pattern visualizations (Figure 5) show imaginary heads attending globally while real heads focus locally. The noise-injection experiment demonstrates that corrupting imaginary attention degrades long-context accuracy by 5–8 points more than corrupting real attention (Section 5.2), establishing a causal link between imaginary heads and long-range performance.

- **Practical efficiency**: RoPE++_EH halves KV cache and consistently reduces memory cost and increases tokens-per-second, with the margin widening as context grows (Figure 4). The method is compatible with FlashAttention and plugs directly into MHA/GQA.

- **Broad compatibility**: When combined with NTK, Linear PI, or YaRN for context extension, RoPE++ variants continue to outperform RoPE (Table 3), demonstrating orthogonality to existing scaling techniques.

## Weaknesses

### Fatal

None.

### Major

- **Model scale limits confidence in practical relevance**: All pre-training experiments are conducted at 376M and 776M parameters. While this is common for position-embedding studies, the paper repeatedly invokes million-token contexts and production LLMs. The efficiency argument (halving KV cache) would matter most at large scale, yet there is no evidence the benefits transfer to the 7B+ regime where long-context efficiency is practically important. This does not invalidate the contribution but significantly limits the strength of the practical claims.

- **Long-context baselines restricted to RoPE only**: FoPE, Pythia (partial RoPE), and ALiBi — all compared at short context in Table 1 — are never evaluated on long-context benchmarks (Table 2). The paper states "We highlight the comparison with RoPE in long-context training because RoPE is the position embedding currently most widely used by long-context LLMs" (line 140), which is a reasonable choice, but ALiBi is explicitly designed for length extrapolation and could be evaluated at 64k without additional training. Since the paper's main advance is long-context capability, the absence of these baselines weakens the claim that RoPE++ is the best available choice for long-context modeling among position embeddings.

### Minor

- **Characteristic curve analysis lacks explicit isotropy assumptions**: The derivation of the imaginary characteristic curve (Eq. 5) and the claim that it supports "semantic aggregation" (Section 3.2) implicitly assumes isotropy of query-key dot products. Citing prior formalization (e.g., Barbero et al., 2024) and stating the assumption explicitly would strengthen the theoretical argument. This does not affect the empirical results.

- **Short-context gains are modest**: RoPE++_EC achieves the best average score on short-context tasks (Table 1), but margins over RoPE are small (+0.8 points at 776M short, +2.2 points at 776M long). While the long-context gains are more substantial, the short-context advantage alone would not justify adoption.

### Trivial

- The configuration description in Figure 2's auto-parsed caption may contain an inconsistency with the textual description of RoPE++_EC and RoPE++_EH (Section 3.3), but the text itself is unambiguous; authors should verify the figure rendering is correct.

## Nice-to-Haves

- Evaluating ALiBi at long context without additional training (since it is designed for zero-shot length extrapolation) would provide a useful baseline and strengthen the long-context claims.
- Including at least one larger-scale result (e.g., 1.5B or 7B) in the main paper, or a summary table of appendix results, would substantially increase community confidence.
- Explicitly stating the isotropy/independence assumptions in the characteristic curve derivation, with a reference to Barbero et al. (2024), would improve theoretical rigor.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "The other position embeddings that were pre-trained at the short-context stage — FoPE, Pythia, and ALiBi — are never evaluated on long-context benchmarks"** → Partially retained as a Major weakness above, but the framing that this is a fatal omission is softened. The paper explicitly justifies focusing on RoPE for long context, and RoPE-based long-context adaptation (rotary base scaling) does not directly apply to ALiBi or FoPE.

- **Harsh critic: "the authors mention larger-scale verification in the stripped appendix"** → REMOVED per rules: the appendix is stripped by the parser; criticizing missing appendix content is not valid.

- **Harsh critic: "The text would benefit from a concise note about the scale of experiments so that expectations are properly calibrated"** → REMOVED: pure style preference, not a substantive weakness.

- **Harsh critic: "The survey is adequate but could better position the paper's novelty relative to prior work that also manipulates the complex-valued nature of attention"** → REMOVED: generic criticism without specific citation or concrete gap identified.

- **Harsh critic: "the paper's framing repeatedly invokes million-token contexts and production LLMs"** → Partially retained in the Major weakness about model scale, but stripped of speculative language.

- **Strength Finder: "This paper addressed an important problem"** → REMOVED: generic, not specific to this paper.

## Novel Insights

The paper's most original insight is the re-characterization of the discarded imaginary component of RoPE attention not as noise but as a structurally distinct signal — one whose characteristic curve (sine integral) decays far more slowly than the real component's (cosine integral), making it naturally suited for long-range dependency modeling. The noise-injection experiment that causally isolates the imaginary heads' contribution to long-context performance is a particularly clean demonstration. The observation that imaginary attention exposes query/key dimensions to the full [−1, +1] range of positional embeddings during pre-training (Section 3.4), thereby implicitly improving length extrapolation by eliminating OOD position values, is also a subtle but valuable insight.

## Suggestions

- Prioritize showing at least summary results at a larger model scale (e.g., 1.5B) in the main paper; this is the single change that would most increase the paper's impact.
- Add a zero-shot long-context evaluation of ALiBi (no fine-tuning needed, since it is designed for length extrapolation) to complement the RoPE-only long-context comparison.
- Add one sentence in Section 3.2 explicitly stating the isotropy assumption for the characteristic curve and citing Barbero et al. (2024).

## Score and Decision

**Originality**: The core idea — re-incorporating the discarded imaginary part as parallel heads — is genuinely novel and well-motivated. No prior work has identified or exploited this specific property of RoPE's complex-valued computation.

**Importance**: Position embeddings are a foundational component of modern LLMs, and RoPE is the dominant choice. Any improvement here has broad potential impact, especially given the trend toward longer contexts.

**Claim support**: The core claims (imaginary heads capture long-range dependencies, RoPE++ improves long-context performance over RoPE) are well supported by both theoretical analysis and consistent empirical results across multiple benchmarks and two model sizes. The mechanistic evidence (attention patterns, noise experiments) is particularly strong.

**Soundness**: The methodology is sound — pre-training from scratch with controlled comparisons, standard benchmarks, fair hyperparameters. The main limitation is scale.

**Clarity**: Well-written with clear mathematical derivations and helpful visualizations.

**Value to community**: The method is simple to implement, compatible with existing infrastructure, and offers practical efficiency benefits. The open-source release of code and checkpoints adds value.

### Anchor comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `OhauMUNW8T` (Wavelet PE) | 5.25 | R2 | RoPE++ is stronger: more comprehensive benchmarks, deeper mechanistic analysis, practical efficiency benefits |
| `VkqqZcofEu` (Controlled Study) | 5.75 | R2 | RoPE++ proposes a novel method rather than just a study; more original contribution |
| `GtvuNrk58a` (Round and Round) | 6.20 | R1/R2 | Comparable: both RoPE innovations with theoretical + empirical contributions; RoPE++ has broader benchmarks but smaller model scale |
| `Us1RXG1Ji2` (TAPE) | 6.00 | R1/R2 | Different approach (contextualized PE); RoPE++ has cleaner integration with existing RoPE models |
| `eoln5WgrPx` (STRING) | 6.50 | R1/R2 | STRING is stronger due to 70B-scale results; RoPE++ works at smaller scale but does pre-training from scratch |
| `EytBpUGB1Z` (Retrieval Head) | 8.00 | R1 | Much stronger: 7B+ scale, broader impact |

**Round 1 bracket**: 5.0–7.0  
**Round 2 narrowing**: RoPE++ is clearly above the 5.25–5.75 cluster but does not reach the 6.50 level of STRING (which has 70B results). It is comparable to "Round and Round" (6.20) in contribution quality, trading off model scale for evaluation breadth. I place it at 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>