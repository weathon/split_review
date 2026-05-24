Now let me do the calibration search.## Summary

The paper proposes **RoPE++**, which re-incorporates the imaginary component of the complex-valued attention score that standard RoPE discards. The key algebraic observation is that the imaginary attention can be written as a real attention computation in which the query has been pre-rotated by `-π/2`, allowing it to be implemented as an additional, parameter-shared group of attention heads. Two configurations are evaluated: RoPE++_EC (same KV cache, doubled heads, doubled W_o) and RoPE++_EH (half KV cache, same head count), trained at 376M and 776M scales and evaluated on short-context benchmarks and long-context benchmarks (RULER, BABILong) up to 64k.

## Strengths

- **Clean algebraic reinterpretation of RoPE.** Equations 1–4 show that the negative imaginary part of the complex attention can be re-expressed as a real-valued attention computation with a `-π/2` query rotation, preserving the relative/absolute decomposition that makes RoPE attractive in the first place. This is a genuine analytical contribution, not just an engineering tweak.
- **Theoretical justification of a long-range bias.** Equation 5 and Figure 1 derive that the characteristic curve of the imaginary attention is a sine-integral (`Si(Δt) − Si(Δt/10⁴)`), versus a fast-decaying cosine integral for the real attention. This provides a principled (if not airtight) reason to expect imaginary heads to attend more globally.
- **Causal probe distinguishing real vs. imaginary heads.** Section 5.2 / Figure 5(e,j) add equal-variance Gaussian noise to real vs. imaginary attention and show a 5-point (376M) / 8-point (776M) larger drop on RULER-4k when imaginary heads are corrupted. This is concrete evidence that the new head group is doing functional work, not merely soaking up parameters.
- **Long-context gains for the EC variant on RULER.** Table 2 shows RoPE++_EC beating vanilla RoPE on RULER average by +6.2 (25.0 vs. 18.8) at 376M and +2.0 (29.4 vs. 27.4) at 776M, with gains persisting at 32k and 64k.
- **Cache-efficient EH variant.** Figure 4 documents lower memory and faster TPOT for RoPE++_EH from 32k to 128k, supporting the practical efficiency claim with half the KV cache.
- **Compatibility with existing context-extension methods.** Table 3 shows RoPE++_EC remains the strongest method when combined with Linear PI and YaRN at both scales, indicating the method composes with the standard long-context-extension toolkit rather than competing with it.

## Weaknesses

### Fatal
None — the core algebraic observation is sound and at least one variant (EC) has consistent empirical wins.

### Major

- **Missing rotation-angle ablation isolates the central thesis.** The paper's framing — that the discarded *imaginary* information is what matters — is operationally a `-π/2` rotation applied to one of two parameter-shared heads (Eq. 4, Section 3.3). Without comparing against (a) a learned per-pair rotation `φ` and/or (b) other fixed angles (e.g. `π/4`), one cannot tell whether `-π/2` is the principled choice the theory predicts or whether *any* extra rotated head would yield similar gains. This is the experiment that would convert the contribution from "a way to add heads" into "the complex-analysis structure selects the right inductive bias."
- **Parameter capacity is not equalized for RoPE++_EC.** The paper acknowledges (Section 3.3) that RoPE++_EC has a `W_o` that is "double-sized" relative to vanilla RoPE. RoPE++_EC therefore has strictly more learnable parameters than the RoPE baseline, and Tables 1–3 do not report a parameter-matched RoPE control (e.g., wider FFN or 2× heads with unshared projections under the same budget). Given that several short-context wins in Table 1 are within ~1 average point, a non-trivial share of the gain could plausibly be attributable to capacity rather than to the imaginary-component design specifically.
- **The "comparable performance" framing for RoPE++_EH is inconsistent with Table 2 and Table 3.** At 776M long-context, RoPE++_EH gets BABILong avg 19.4 vs. RoPE's 22.8 (Table 2) — a 3.4-point loss — yet the narrative repeatedly describes EH as achieving "comparable" or "even superior" results. With YaRN at 376M (Table 3), RoPE++_EH gets BABILong avg 10.5 vs. RoPE's 14.4, again losing. The paper should acknowledge that the "half the cache with comparable performance" claim does not hold uniformly on BABILong and discuss when EH does/does not hold up.

### Minor

- **Long-context comparison is restricted to vanilla RoPE.** Section 4.1 states that continued long-context training is performed only for RoPE and RoPE++; ALiBi/FoPE/Pythia are not extended. The strong long-context claim therefore reads as "better than vanilla RoPE under the same long-context-training recipe," which is narrower than "better than other position embeddings at long context."
- **Theoretical claim about Si(Δt) supporting long-range bias is asserted rather than tightly derived.** Section 3.2 argues that the imaginary characteristic curve "declines very slowly beyond a certain distance," but Si actually oscillates around π/2 with decreasing amplitude. The empirical evidence (Figure 5) and noise probe carry the load; the theoretical claim is suggestive rather than conclusive.
- **No variance / seed reporting.** Many short-context margins in Table 1 are within 1 point on individual benchmarks (e.g., averages 40.0–41.0 at 376M). For some headline claims (especially RoPE++_EH being "comparable" to RoPE), seed variance would help distinguish a small real effect from noise.
- **Scale-trend signal is in the wrong direction.** Comparing Table 2 at 376M vs 776M, the RoPE++_EC advantage on RULER avg shrinks from +6.2 to +2.0 as scale grows. Given the contribution is positioned for "long-context LLMs," the paper would benefit from at least a directional check at a larger scale, since the empirical pattern suggests the gap narrows rather than widens.
- **64k RULER scores are in a low-signal regime.** At 376M / 64k, all methods score 5–10 on RULER; comparisons at this length tell us less than the body of the text implies.

### Trivial

- The phrase "irreversible information loss" overstates what is happening. The attention score must collapse to a real scalar; what was discarded is one of two possible real-valued summaries, not physical information.

## Nice-to-Haves

- A rotation-angle sweep (`-π/2` vs learned vs `π/4` vs `0`) to isolate the role of the principled angle.
- A parameter-equalized RoPE baseline that absorbs the extra `W_o` capacity elsewhere (wider FFN or matched-parameter unshared-head variant).
- At least one experiment at 3B+ scale to support the "long-context LLM" framing.
- Explicit discussion of the BABILong cases where RoPE++_EH underperforms RoPE.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- *Harsh critic's "noise probe could be explained by allocation rather than uniqueness of imaginary info" (Section 5.2 critique).* This is speculative — both interpretations would still establish that imaginary heads carry functionally important information, which is the paper's actual claim. The distinction matters intellectually but does not undermine the empirical conclusion. Demoted/removed.
- *"Empirical case below 7B is not where long-context is usually adjudicated."* Reasonable concern, but the paper's setup is honest about its scale. We retain this as a Minor weakness under "scale-trend signal" rather than as a Major flaw — the paper does not actually claim 7B-scale results.
- *Strength Finder's "important problem" framing.* Generic; removed.

## Novel Insights

None beyond the paper's own contributions. The cleanest novel observation in the paper is itself: that the discarded imaginary part of the complex RoPE inner product is *not* a fundamentally new computation but equivalent to a `-π/2`-rotated query, which means re-incorporating it is exact, cheap, and structure-preserving. The reviewer pool surfaces no insight that goes beyond what the paper already states.

## Suggestions

- Run the rotation-angle ablation (fixed `-π/2` vs learnable scalar vs other fixed angles) and report results in Table 1 / Table 2. This is the single most decision-changing experiment.
- Add a parameter-matched RoPE baseline (wider FFN or 2× heads with unshared QKV at matched parameter budget) so readers can rule out "RoPE++_EC just has more parameters."
- Acknowledge in-text the BABILong cases where RoPE++_EH loses to RoPE (Table 2 at 776M; Table 3 with YaRN at 376M) and adjust the "comparable performance" framing.
- Report at least seed variance, or state that single-seed evaluation is the operating regime, so 1-point differences in Table 1 can be interpreted appropriately.
- If feasible, even one mid-scale (≥3B) data point would substantially strengthen the long-context framing, particularly given the +6.2 → +2.0 trend in RULER gains from 376M to 776M.

## Evaluation on Axes

- **Originality:** Moderate-to-high. The complex-analytic reinterpretation of RoPE is genuinely fresh; mechanically, the modification is small but principled.
- **Importance of question:** Position encoding for long context is a well-motivated and actively studied area.
- **Whether claims are well supported:** Partially. The "long-context advantage" is well supported for EC on RULER and via the noise probe, but the "EH is comparable" claim is overstated in light of BABILong losses, and "the imaginary part is uniquely valuable" cannot be distinguished from "an extra rotated head is valuable" without the angle ablation.
- **Soundness of experiments:** Adequate but not airtight. Parameter capacity is not equalized; no variance is reported; long-context comparison is restricted to vanilla RoPE.
- **Clarity of writing:** Generally clear; the derivations are easy to follow.
- **Value to the community:** Real but modest. The algebraic identity is useful pedagogically; the efficiency angle of EH is potentially practical even if its long-context numbers are mixed.

## Score and Decision

**Anchors retrieved:**

Round 1 (bracketing):
- `jp4pxKqCRW.md` — avg 2.50 (Round 1, weak band, Reject) — periodic-extension RoPE paper with weak experiments; this paper is clearly stronger.
- `5dDYhvt6dY.md` — avg 3.00 (Round 1, weak band, Reject) — far less ambitious and on toy MT setup; not comparable.
- `I1484gDBr4.md` — avg 2.50 (Round 1, weak band, Reject) — different topic (LRNNs); not used for comparison.
- `N581Nje6fH.md` — avg 1.50 (Round 1, weak band, Reject) — different topic; not used.
- `JO7k0SJ5V6.md` — avg 5.00 (Round 1, mid band, Accept) — "Scaling Laws of RoPE-based Extrapolation"; comparable scope but with 7B/13B experiments. This paper is similar in spirit but at much smaller scale.
- `GtvuNrk58a.md` — avg 6.20 (Round 1, mid band, Accept) — "Round and Round We Go"; deeper analytical contribution at 7B scale. Stronger than the paper under review.
- `eoln5WgrPx.md` — avg 6.50 (Round 1, mid band, Accept) — "STRING"; more thorough empirical case at larger scale.
- `wXpSidPpc5.md` — avg 6.50 (Round 1, mid band, Accept) — "CLEX"; broader long-context method.
- `EytBpUGB1Z.md`, `OvoCm1gGhN.md`, `E4Fk3YuG56.md`, `OfjIlbelrT.md` — avg 8.00–8.50 (Round 1, strong band) — substantially stronger than the paper under review.

Round 2 (narrowing):
- `fn0mjkZopf.md` — avg 5.25 (Round 2, Reject) — learning-PE paper, less ambitious experimentally; this paper is at least comparable.
- `xHMMt7r3GW.md` — avg 5.33 (Round 2, Reject) — "LieRE"; RoPE generalization with mixed but interesting empirics; the paper under review is similarly positioned.
- `OhauMUNW8T.md` — avg 5.25 (Round 2, Accept) — "Wavelet-based PE for Long Context"; reinterprets RoPE through wavelets, marginal empirical gains. Closest analog: this paper has a tighter algebraic identity and a more direct causal probe but similar criticisms about scale and ablations.
- `t717joHHSc.md` — avg 4.75 (Round 2, Reject) — position-bias paper; tangential.
- `VkqqZcofEu.md` — avg 5.75 (Round 2, Reject) — controlled-study paper; broader empirical scope, comparable score range.
- `Us1RXG1Ji2.md` — avg 6.00 (Round 2, Reject) — "TAPE"; principled new PE with broader experiments; somewhat stronger empirically than this paper.
- `sIGWTd1DcW.md` — avg 5.25 (Round 2, Reject) — "Contextual PE"; comparable scope.

**Round-1 bracket:** This paper plausibly sits between 4.5 and 6.0 — weaker than the 6.2–6.5 anchors (which have larger-scale or more comprehensive empirics) and stronger than the sub-3.5 rejects.

**Round-2 narrowing:** The closest analogs are Wavelet-based (5.25, Accept) and LieRE (5.33, Reject). This paper has a slightly cleaner theoretical identity than Wavelet and adds a causal noise probe that strengthens the empirical case, but it also has a clearer missing ablation (rotation angle) and acknowledged-but-unhandled mixed results for EH. It sits in roughly the same band — modest gains, principled insight, real but limited experiments. TAPE (6.00, Reject) is somewhat stronger empirically.

The paper lands close to the Wavelet/LieRE band, slightly below TAPE, well below Round-and-Round/STRING/CLEX. A score of 5.0 reflects a borderline paper with a genuinely elegant idea, modest empirical gains, and addressable but real gaps in ablations and honesty about EH's mixed long-context numbers.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>