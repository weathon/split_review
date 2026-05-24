Now I have enough information to produce the consolidated review. Let me synthesize everything.

---

## Summary

This paper identifies that standard RoPE discards the imaginary component of the complex-valued attention dot product, and proposes RoPE++ to re-incorporate it as a parallel group of "imaginary" attention heads via a simple –π/2 query rotation. Two configurations are introduced: RoPE++_EC (doubled heads, equal KV-cache) and RoPE++_EH (equal heads, halved KV-cache). Pretraining experiments at 376M and 776M scales show gains over standard RoPE and other position embeddings on both short- and long-context benchmarks, with the imaginary heads demonstrably contributing to long-range dependency modeling.

## Strengths

- **Novel and well-motivated observation**: The paper is the first to identify that standard RoPE's real-only attention discards valuable phase information from the complex product. The mathematical derivation in Section 3.1 is clean, showing the imaginary attention can be expressed as a simple –π/2 rotation of the query, preserving the absolute-relative position embedding format (Equations 2–4). This is elegant and practically simple to implement.

- **Compelling causal evidence for the imaginary component's role**: The noise-injection experiment (Section 5.2, Figure 5) is the paper's strongest piece of evidence. Within the *same* RoPE++_EC model, injecting Gaussian noise into imaginary attention degrades RULER-4k by ~8 points more than the same perturbation to real attention (at σ=1.0, 776M model). This directly isolates the imaginary heads' contribution to long-context capability without any confound from model capacity — a within-model ablation that partially addresses concerns about head-count effects.

- **Comprehensive empirical evaluation**: The paper evaluates both short-context (11 tasks) and long-context (RULER and BABILong across 4k–64k) benchmarks, compares against four baselines (RoPE, FoPE, Pythia, ALiBi), uses two model sizes (376M, 776M), and tests compatibility with NTK, Linear PI, and YaRN (Table 3). RoPE++_EC shows substantial gains on long-context tasks (e.g., RULER average from 18.8→25.0 at 376M; BABILong from 11.0→16.1). This breadth exceeds many comparable position-embedding papers.

- **Practical efficiency configuration**: RoPE++_EH halves KV-cache size and QKV parameters while maintaining competitive performance (Tables 1–2). Memory and throughput measurements (Figure 4) confirm widening efficiency advantages as context grows, making a concrete practical contribution beyond accuracy alone.

- **Attention pattern analysis validates mechanism**: Visualization (Figure 5) shows imaginary heads attend more strongly to global/initial positions while real heads focus locally, directly corroborating the theoretical claim that the imaginary component captures longer-range dependencies.

## Weaknesses

### Fatal

None.

### Major

- **EC parameter comparison is unclear and risks overclaiming**: The paper states that Wo in RoPE++_EC is "double-sized" (line 110) while also claiming the method operates "under the fixed QKV parameter budget" (line 108). These statements are in tension. In GQA with doubled query heads and same d_head, both Wq and Wo would double, increasing total parameters non-trivially. The paper does not report parameter counts or FLOPs for EC versus standard RoPE, making it difficult for readers to assess whether the gains come from the imaginary rotation specifically or from increased capacity. This does not invalidate the contribution — the EH variant and noise-injection experiment provide independent evidence — but it weakens the headline EC results and should be clarified.

- **EH long-context performance is genuinely mixed**: While RoPE++_EH generally matches RoPE on average, specific results are uneven. At 776M on BABILong, EH drops from 22.8 (RoPE) to 19.4 — a substantial decline. On RULER at 376M, EH (18.2) is slightly worse than RoPE (18.8). The paper's claim that RoPE++_EH "achieves comparable results with vanilla RoPE with half the cache" is fair overall, but the inconsistency across tasks and model sizes should be acknowledged more frankly rather than smoothed over by averaging.

### Minor

- **Theoretical analysis is heuristic, not rigorous**: Section 3.2 derives characteristic curves that assume query-key similarity (semantic aggregation). While the sine-integral argument is plausible and intuitive, the paper's abstract claim of having "theoretically demonstrated" the enhancement overstates what is actually a heuristic motivation. The empirical evidence carries the paper; the theory should be presented as motivation rather than demonstration.

- **Limited model scale**: All experiments use 376M and 776M parameter models. While this is reasonable for an academic study with pretraining from scratch, the claims about long-context LLMs would be strengthened by evidence that the benefits persist at larger scales (1B+, 7B+), even through continued training rather than full pretraining.

- **No dedicated extrapolation experiments beyond 64k**: Section 3.4 makes claims about improved length extrapolation, but evaluation stops at 64k (the long-context training length). A perplexity-vs-length curve beyond the training context would directly test the extrapolation argument.

### Trivial

- Figure 2 caption for RoPE++_EC says "key heads are halved" which appears inconsistent with the diagram (same number of key heads as standard RoPE). This is likely a caption error.
- The paper claims "no extra KV cache is introduced" for EC (line 107–108), which is correct, but the additional compute from doubled attention heads should be explicitly noted alongside this claim.

## Nice-to-Haves

- A controlled baseline with doubled real-only heads (same parameter count as EC) would cleanly isolate the imaginary component's contribution beyond mere head-count increase. The noise-injection experiment partially fills this gap but addresses a slightly different question.
- A variant using a different fixed rotation (e.g., random orthogonal) instead of –π/2 would test whether the specific phase relationship matters or any query diversification helps.
- Reporting training FLOPs or wall-clock time for EC vs. standard RoPE would give readers a complete cost picture.
- Testing on a larger model (1B+) through continued training would strengthen generalizability claims.

## Removed Points

These points were raised by reviewers but are removed or demoted after verification against the paper:

- **"EC increases model parameters substantially, confounding results"** — REMOVED as a fatal criticism. The paper's own statements about Wo being "double-sized" create legitimate confusion, but (a) the noise-injection experiment holds the model architecture constant, providing within-model evidence that imaginary heads specifically matter for long-context; (b) the EH variant uses *fewer* parameters yet still often matches or exceeds RoPE; (c) in MHA with halved d_head, EC would have identical parameter counts. The concern is retained above as a Major weakness about clarity, not a fatal methodological flaw.

- **"No baseline controls for head-count increase"** — PARTIALLY RETAINED as a Nice-to-Have. The noise-injection experiment already controls for this by comparing within the same model. An additional architectural baseline would strengthen but is not required for the paper's claims to hold.

- **"The theoretical part does not constitute a rigorous demonstration"** — RETAINED but downgraded to Minor. The paper's abstract wording overstates the theoretical contribution, but the heuristic analysis is still informative and well-motivated. This is a framing issue, not a scientific error.

- **"Missing discussion of training cost / FLOPs for EC"** — Moved to Nice-to-Haves. Reasonable request but not a weakness per se given the paper already discusses memory and throughput for EH.

- **"EH performance differences are small and not uniformly positive"** — RETAINED as Major. This is a genuine limitation of the experimental results, not a reviewer misunderstanding.

- **"Demands confidence intervals / user studies / theoretical proofs"** — REMOVED. These are not standard requirements for empirical position-embedding papers at this scale.

- **"Extrapolation argument presented without dedicated extrapolation experiments"** — RETAINED as Minor.

- **Various formatting/style nitpicks and missing-reference complaints** — REMOVED per instructions.

## Novel Insights

The most interesting novel insight emerging from this work is the functional asymmetry between real and imaginary attention heads revealed by the noise-injection experiment: imaginary heads are substantially more critical for long-context performance than real heads, despite both being computed from the same QKV parameters with only a –π/2 rotation difference. This suggests that the phase relationship between query and key vectors carries information that is not redundant with the real-valued dot product, and that LLMs learn to rely on this phase information for long-range retrieval. This finding goes beyond the paper's initial motivation of "recovering discarded information" and points toward a more nuanced understanding of how RoPE-based attention organizes positional and semantic information.

## Suggestions

- Clarify the parameter comparison for EC explicitly: report total parameter counts for standard RoPE, RoPE++_EC, and RoPE++_EH at both model sizes. If d_head is halved in EC (making parameter counts equal in MHA), state this explicitly. If Wo does indeed double, acknowledge the capacity increase and discuss its magnitude relative to total model size.
- Add a dedicated extrapolation figure (perplexity vs. sequence length beyond 64k) to support Section 3.4's claims, or soften the extrapolation language if such experiments are not feasible.
- Qualify the EH results more carefully in the text, noting where it underperforms (e.g., BABILong at 776M) rather than relying solely on averages.

## Score and Decision

**Round 1 bracket**: Based on comparison with anchors — PoSE (6.00), "Round and Round We Go" (6.20), CLEX (6.50), STRING (6.50), Scaling Laws of RoPE (5.00) — RoPE++ plausibly sits in the **6.0–7.0** range.

**Round 2 narrowing**: Compared against CLEX (6.50) and STRING (6.50), RoPE++ offers a comparably novel RoPE modification with strong empirical validation. RoPE++ has the advantage of a clean, simple method with compelling mechanistic experiments (noise injection, attention patterns), but is limited to smaller model scales and has some clarity issues around EC parameter accounting. It is comparable to these 6.5 anchors — stronger in mechanistic analysis, somewhat weaker in scale of models tested. The paper is clearly above the 5.0–6.0 tier (where evaluation is perplexity-only or limited in scope) and below the 7.5+ tier (which would require large-model validation, airtight ablation designs, or breakthrough results).

**Anchors referenced**:
- `JO7k0SJ5V6` (Scaling Laws of RoPE, 5.00): RoPE++ is stronger — evaluates on real long-context benchmarks, not just perplexity.
- `GtvuNrk58a` (Round and Round We Go, 6.20): RoPE++ is comparable — both offer novel RoPE insights; RoPE++ has broader empirical scope but less theoretical depth.
- `3Z1gxuAQrA` (PoSE, 6.00): RoPE++ is stronger — more comprehensive evaluation including non-perplexity long-context benchmarks.
- `wXpSidPpc5` (CLEX, 6.50): RoPE++ is comparable — both have strong empirical results; CLEX has larger-model validation, RoPE++ has better mechanistic analysis.
- `eoln5WgrPx` (STRING, 6.50): RoPE++ is comparable — different approach (pretraining vs. inference), similar level of contribution quality.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>