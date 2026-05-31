I've read the paper. Let me verify the critic's key claims and run calibration searches.Based on round 1, the paper is in the 5-7 range (similar to MELODI). Let me narrow further.Now I have enough information to synthesize the final review. Let me verify a few more specific claims before writing.

**Verifications against the paper:**
- Eq. 7: Confirmed — the "projection" formula is ∑ k_τ k_τᵀ/‖k_τ‖² · q_t. For non-orthogonal keys this is not a projector (not idempotent, norm grows). Critic's math claim is correct.
- §5: Confirmed says "we instantiate it with a strong deep memory model, Titans" — TTT appears in Table 2 only as a baseline, not as TNT-applied.
- Table 1: Confirmed Titans C=8 = 19.48 hrs (slowest = most accurate baseline). Titans C=128 = 3.71 hrs. 17.37× holds only against C=8.
- §5.3: Confirmed dismissal of Gated Transformer's better PPL (22.39 vs 23.09).
- Table 2: All TNT configs labeled "150M parameters" with no per-config parameter accounting visible.
- Eq. 6 "otherwise" branch: Confirmed uses W_{t-1} as base but ∇L computed against W_{ξ(t,Cₗ)} — non-standard.

## Summary
The paper introduces TNT, a two-stage training paradigm for deep memory modules (Titans-style architectures): a Stage-1 hierarchical memory (one global module on large chunks + N local modules with periodic state resets) that enables context parallelism for non-linear recurrences, and a Stage-2 short fine-tuning to recover small-chunk inference accuracy. On a 150M Titans instantiation, TNT reaches a target loss up to 17.37× faster than the slowest/most-accurate Titans baseline and improves average perplexity from 25.07 to 23.09–23.13 with ~5% fine-tuning overhead.

## Strengths
- **Novel parallelization mechanism for non-linear recurrences.** Eq. 6's periodic reset of local memory to a learned W_init breaks inter-shard sequential dependence — a long-standing obstacle for non-linear RNNs that previously required either linear state transitions or attention-mixing (Zhang et al. 2025; Guo et al. 2025). Combined with a global module (Eq. 5) for cross-shard context, this is a genuinely new architectural lever.
- **Substantial empirical speedup with concurrent quality gain.** Table 1 shows multiple TNT configurations beat all Titans chunk sizes (e.g., TNT C_L=64 → 1.12 hr vs Titans C=128 → 3.71 hr ≈ 3.3×; vs Titans C=8 → 19.48 hr ≈ 17.4×). Figure 4 shows TNT runtime stays ~400–550 ms from 2K to 32K while Titans C=16 grows to ~4000 ms.
- **Stage-2 fine-tuning is cheap and effective.** §5.3/Table 4 reports ~5% additional compute moving Avg PPL from 23.13 → 23.09 while enabling small-chunk inference (C'_L = 1), partially addressing the Challenge 3 train/test chunksize mismatch shown in Fig. 2.
- **Useful ablations.** Table 3 isolates the contribution of the global memory (removing it: 21.04 → 25.60 PPL) and the Q-K Projection (21.04 → 22.01), showing both components carry empirical weight.

## Weaknesses

### Fatal
None.

### Major
- **The "Q-K Projection" operator is not a projection, undermining the stated motivation for Challenge 2's named fix.** Eq. 7 computes (∑_τ k_τk_τᵀ/‖k_τ‖²) q_t. This operator is not idempotent for arbitrary (non-orthogonal) keys and does not project onto span{k_τ}; the true projector onto that subspace is K(KᵀK)⁻¹Kᵀ, which the paper sidesteps to keep a running sum. The mechanism does help empirically (PPL 22.01 → 21.04), but the narrative that it "ensures the input to the memory function is in the space memory was trained on" (§4.1.2) is not what the equation actually implements. The contribution should be reframed as an accumulated key-direction correction rather than a subspace projection — currently a named contribution rests on a justification the math doesn't support.
- **Long-context evaluation is absent despite long-context being the entire motivation.** §1 and §5.2 (32K runtime) position TNT as enabling "truly long sequences," yet Table 2 evaluates only C4/FineWeb/PG19 perplexity and short-context commonsense (PIQA, HellaSwag, ARC-e, CSQA). The crux of the architecture — whether the global memory (C_G=2048) actually preserves information across the periodic resets of local memory at S_L tokens — is precisely the claim a needle-in-a-haystack, RULER, or long-context QA evaluation would answer. Average perplexity can be dominated by local statistics and is the wrong instrument for this question.
- **The "17×" headline relies on the worst-case baseline; the apples-to-apples speedup is much smaller.** Table 1's 17.37× uses Titans C=8 (19.48 hrs), the slowest configuration. Against Titans C=128 (3.71 hrs), TNT's best is ~3.3×. The abstract reconciles this by calling C=8 "the most accurate baseline configuration" — true per Table 2 (Titans C=8 = 25.07 PPL is the best Titans row) — but the framing throughout selects the most favorable comparison. A wall-clock-vs-final-quality Pareto plot would be defensible; the single 17× number is selectively framed.
- **The "evaluated on Titans and TTT" abstract claim is not supported by experiments.** §5 says "we instantiate it with a strong deep memory model, Titans … to demonstrate its effectiveness." Table 2 includes TTT only as a baseline comparator, not as a TNT-applied architecture. The "general training paradigm" claim is asserted but not demonstrated empirically.

### Minor
- **Parameter accounting across TNT variants is unclear.** Table 2 reports configurations from N=1 to N=4 local modules all labeled "150M parameters," but each local module brings its own fast-weight sub-network and a d×d Q-K projection state. Without explicit per-config parameter/FLOP counts, it is unclear whether the 23.13 ↓ 25.07 improvement is partially purchased with extra parameters not reflected in the size label.
- **Eq. 6 "otherwise" branch reads as non-standard or as a typo.** The update uses W_{t-1} as base but computes the gradient with respect to W_{ξ(t,C_L)} — mixing a per-step base with a chunk-base gradient, which differs from the standard Eq. 3. If intentional, it should be derived; if not, it should be corrected, since this is the central local-memory rule.
- **Metric chosen for headline switches between PPL and accuracy depending on which is favorable.** §5.3 frames TNT's headline against Titans on PPL (25.07 → 23.13), but dismisses Gated Transformer's better PPL (22.39 vs 23.09) as "less stable than accuracy" and switches to commonsense accuracy. Pick one or report both consistently.
- **Missing S_L (segment reset window) ablation.** §5.4 sweeps N (number of local modules) but never sweeps S_L, which directly controls how much long-range information is lost across resets — the single most architecturally diagnostic ablation.
- **Stage 2 alignment to "prefill-and-decode" is asserted but not directly tested.** §4.2 motivates C'_L=1 by analogy to autoregressive decoding, but evaluation uses chunked teacher-forced PPL, not actual generation.

### Trivial
None retained (parser artifacts excluded per rules).

## Nice-to-Haves
- A 2D Pareto plot of training wall-clock time vs. final perplexity across all Titans chunk sizes and TNT configurations, replacing the single 17× headline.
- Apply TNT to a second deep-memory backbone (e.g., TTT or Atlas) to substantiate the "general paradigm" claim.
- Either swap Eq. 7 for a true projector (maintain running KᵀK and solve at chunk boundaries) or rewrite the motivation as a key-direction-weighted correction.
- At least one long-context retrieval task (NIAH or single-doc recall) at the 16K–32K context lengths the runtime plots reach.
- Report variance / multiple seeds — at 150M and 10B tokens, differences like 23.13 vs 23.09 PPL or 40.6% vs 40.9% accuracy are within plausible seed noise.

## Removed Points
These points are flagged to be removed, treat them with caution.

- Strength Finder's claim that "TNT is model-agnostic, validated on Titans and TTT" — removed because TTT is only a baseline in Table 2 (the paper itself says "we instantiate it with … Titans"). This contradicts a kept weakness.
- Generic strength about "tackling an important problem" / "removing a scalability barrier" — removed as superficial; the contribution is real but the strength as worded is sloganeering.
- Reproducibility concerns about un-tabulated FLOP breakdowns and lack of training-log disclosure — removed per hard rules against trivial reproducibility nitpicks.

## Novel Insights
None beyond the paper's own contributions. The genuine insight here — that periodic state resets paired with a coarse-chunk global module enable context parallelism for non-linear RNN memories — is the paper's own central claim, not something the reviews surface on top of it.

## Suggestions
- Reframe §4.1.2 honestly: drop "projection onto subspace spanned by past keys"; either motivate the operator as an accumulated rank-1 key-direction correction (since the ablation evidence supports it as a useful heuristic), or implement an actual projector with maintained KᵀK and compare.
- Add at least one long-context retrieval evaluation (NIAH, RULER, or single-doc QA) at 16K–32K. Without it, the architectural claim that the hierarchical memory carries information across resets is unsupported by the metric you report.
- Replace the standalone "17×" headline with a wall-clock vs final-perplexity Pareto curve; the data in Table 1 already supports this and the result will likely still favor TNT honestly.
- Add explicit parameter/FLOP columns to Table 2 for each TNT configuration so that the role of added local modules is unambiguous.
- Add an S_L sweep to §5.4; this is the architecturally most diagnostic ablation and is currently missing.
- Either tone down the abstract's "evaluated on Titans and TTT" / "general paradigm" wording, or actually run a TNT-on-TTT experiment to back it.

## Axis Evaluation
- **Originality:** Genuine. The periodic-reset mechanism for non-linear recurrences is a real architectural contribution not subsumed by Zhang et al. (2025) or Guo et al. (2025).
- **Importance:** High — training efficiency is the binding constraint preventing deep memory modules from being a serious Transformer alternative.
- **Claim support:** Mixed. The speedup claim is real but framed favorably; the quality claim is real and supported. The "long-context training" claim is motivated but not evaluated. The "Q-K Projection" claim is mathematically miscast.
- **Soundness of experiments:** Reasonable baselines (Titans/TTT/Transformers, gated and ungated) and meaningful ablations, but no long-context retrieval tests and no per-config parameter accounting.
- **Clarity:** Generally clear; Eq. 6's update form and §4.1.2's projection rationale are the main confusions.
- **Value:** Real value to the deep-memory community as a training-time recipe. Provides a usable foundation for future work, even if framing and one mechanism need revision.

## Comparative Calibration

Anchors retrieved:

**Round 1 (bracketing):**
- `JOBokGDcX0.md` (avg 2.50, weak band) — overlapping-chunk audio paper; weaker scope, much weaker than TNT.
- `I1484gDBr4.md` (avg 2.50, weak band) — feature-sequence LRNN; thin contribution.
- `4ymHtDAlBv.md` (avg 2.33, weak band) — FSFC RNN; clearly below TNT.
- `1MHgMGoqsH.md` (avg 3.00, weak band) — MPC/BP unification; weaker.
- `s1kyHkdTmi.md` (avg 7.00, middle band) — Evolved Universal Transformer Memory; comparable in topic, somewhat broader empirical story.
- `TvGPP8i18S.md` (avg 6.25, middle band, **read in full**) — MELODI, most directly comparable: hierarchical short/long-term memory, perplexity-focused, accepted with similar limitations (limited downstream tasks, limited context length exploration).
- `FhbZ1PQCaG.md` (avg 5.75, middle band) — Decision Transformers with memory; less relevant.
- `zjeHLSiNv1.md` (avg 6.00, middle band) — UltraMem; comparable scope, accepted.
- `GRMfXcAAFh.md` (avg 8.00, strong band) — Oscillatory SSMs with universality proofs; stronger theoretical grounding than TNT.
- `PdaPky8MUn.md` (avg 8.00, strong band) — Never Train From Scratch; broader methodological insight.
- `Tzh6xAJSll.md` (avg 7.60, strong band) — Scaling Laws for Associative Memories; theoretical depth TNT does not match.
- `OfjIlbelrT.md` (avg 8.00, strong band) — FlexPrefill; stronger empirical breadth.

Round-1 bracket: **5–7**. TNT is clearly above the weak (2-3) anchors and clearly below the strong (8) anchors that have theoretical proofs or broader empirical evaluation.

**Round 2 (narrowing within 5-7):**
- `SXvb8PS4Ud.md` (avg 5.80) — ParallelSpec; efficiency-focused, framing concerns, rejected.
- `QOXrVMiHGK.md` (avg 5.75) — PEARL parallel speculative decoding; accepted with mixed scores.
- `kC5i5X9xrn.md` (avg 5.00) — LightSeq sequence-parallel training; weaker.
- `0JjsZC0w8x.md` (avg 5.75) — COrAL; parallel multi-token, rejected.
- `eENHKMTOfW.md` (avg 6.00) — small-LLM training guide; different topic.
- `7iuFxx9Ccx.md` (avg 6.00) — Slimmable TTT; different test-time training.
- `JCiF03qnmi.md` (avg 6.80) — Critical Batch Size scaling; stronger empirical study, accepted.
- `ulaUJFd96G.md` (avg 6.25, **read in full**) — HOMER hierarchical context merging; comparable scope, accepted despite limited downstream-task breadth.
- `fL4qWkSmtM.md` (avg 6.80) — perplexity-for-long-context critique; methodologically incisive.

**Comparison:** TNT sits closest to MELODI (6.25) and HOMER (6.25) — all three are hierarchical memory papers with real architectural contributions, perplexity-dominated evaluation, and similar reviewer pushback on limited downstream coverage. TNT's training-efficiency speedup is more concrete and substantial than MELODI's footprint claims, but TNT carries an additional pointed issue (the Q-K projection mathematical mismatch) and a more conspicuous gap (no long-context retrieval evaluation despite the motivation).

Net: slightly below MELODI/HOMER (6.25) given the Q-K math issue and missing long-context eval; clearly above the rejected efficiency papers around 5.0–5.75. Final score lands at **6.0** — a borderline accept reflecting a real, useful contribution with revisions that are addressable but currently weaken the framing.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>