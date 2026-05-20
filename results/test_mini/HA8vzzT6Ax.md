Now let me write the consolidated review.

## Summary

This paper revisits the claimed "inevitable trade-off" between watermark strength and speculative sampling efficiency. It introduces a quantitative (KL divergence-based) measure of watermark strength, formalizes the trade-off as a Pareto frontier characterized via constrained optimization, and derives explicit curves for several watermarking schemes. Its core algorithmic contribution is **pseudorandom acceptance** (Algorithm 1): by making the draft-token acceptance decision a deterministic function of pseudorandom numbers instead of a true random coin flip, the output becomes a deterministic function of the full pseudorandom state. Theorem 4.1 proves that for any unbiased degenerate decoder, this scheme simultaneously attains maximal sampling efficiency (1−TV(Q,P)) and maximal watermark strength (Ent(P)). Experiments on Llama-68M/7B and Gemma-2B/7B with Gumbel-max and SynthID watermarks show that the method preserves AATPS while improving TPR@1%FPR.

## Strengths

1. **Quantitative watermark-strength measure that moves beyond binary definitions.** Definition 3.1 defines watermark strength as expected KL divergence, and Theorem 3.1 shows this governs the exponential p-value decay rate of the likelihood-ratio test. Theorem 3.2 upper-bounds it by Ent(P) with equality iff the watermarked distribution is degenerate. This enables a continuous, nuanced trade-off analysis that prior binary-strength frameworks (Hu & Huang, 2024) could not capture.

2. **Explicit Pareto characterization of the trade-off.** The trade-off is formalized as the function L(r) in Definition 3.2, and closed-form solutions are derived for linearly-watermarked classes (Eq. 10). Figure 1 displays concrete curves for Gumbel-max, SynthID, Hu's class, and Google's class, enabling direct comparison of which scheme dominates at a given efficiency.

3. **Pseudorandom-acceptance algorithm with theoretical guarantees.** Algorithm 1 is clean and principled: it replaces the random acceptance coin flip with a pseudorandom draw from ζ^R. Theorem 4.1 proves unbiasedness (part a), maximal sampling efficiency (part b), and maximal watermark strength (part c) under the stated assumptions. This is the paper's central constructive claim.

4. **Empirical validation of efficiency preservation and detectability improvement.** Figure 2 (left panel) shows that AATPS for both watermarks closely matches standard speculative sampling. The middle and right panels demonstrate improved TPR@1%FPR for the proposed detectors (Ars-τ and Bayes-MLP) over prior methods (Ars-Prior, Bayes-Prior) for both watermarks, approaching the oracle at 200 tokens. PTT and LOGPPL results in the appendix confirm runtime acceleration and unbiasedness.

## Weaknesses

### Fatal
None.

### Major

1. **SynthID detection comparison confounds two factors (use of *u* vs. use of MLP capacity).** For SynthID, the proposed detector (Bayes-MLP) uses a three-layer MLP with access to the acceptance variable *u* and the two candidate statistics (y^D, y^T), while the baseline (Bayes-Prior) combines the two statistics via a simple weighted average. This comparison conflates two separate differences: (i) the additional information from the pseudorandom acceptance variable and (ii) the greater model capacity of the MLP. The paper does not provide an ablation that isolates the contribution of *u*—e.g., an MLP trained on (y^D, y^T) *without* *u*. Without this, the reader cannot determine whether the improvement in Figure 2 (right panel) stems from the pseudorandom acceptance mechanism or simply from replacing a weak classifier (weighted average) with a stronger one (MLP). This weakness affects the *SynthID* results specifically; the Gumbel-max results (middle panel) are not subject to this concern because the comparison there is between two scoring rules (Ars-τ vs. Ars-Prior) that differ only in how they use *u*.

### Minor

2. **Bonus-step tokens are excluded from detection without empirical justification.** The paper acknowledges (footnote, line 253) that tokens generated during bonus steps (Algorithm 1, lines 15–16) are not covered by the acceptance variable *u*, and asserts that "as long as the lookahead *K* is not very small…the sampling process rarely enters a bonus step, so its impact on detection is negligible in practice." However, experiments use *K* = 2, 3, 4, and bonus steps will occur nontrivially—especially for *K* = 2. The paper does not report bonus-step frequencies or show that excluding these tokens does not alter the ROC curves. This should be quantified.

3. **The gap between Theorem 4.1(c) (which requires degenerate decoders) and the SynthID experiments (m=30, non-degenerate) could be more clearly articulated.** Theorem 4.1 is correctly conditioned on the decoder being degenerate (point‑mass), and the paper does note (line 183) that SynthID with m=30 does not achieve maximum watermark strength. However, the experimental section presents Gumbel-max and SynthID results side‑by‑side without emphasizing that only the Gumbel‑max results directly verify Theorem 4.1(c), while the SynthID results represent a heuristic benefit. Clarifying this distinction would prevent readers from over-interpreting the SynthID improvements as a direct empirical proof of the theorem.

4. **The computational cost of generating ζ^R is not discussed.** The algorithm introduces a third pseudorandom stream (ζ^R) alongside the watermarking streams ζ^D and ζ^T. While the overhead is likely negligible, the paper does not mention it.

5. **"Repeated context masking" is mentioned but not explained.** The paper states it "skips watermarking for repeated contexts" (line 224) but does not describe how this interacts with the pseudorandom acceptance mechanism—specifically, whether it reverts to true randomness for those steps and whether it affects the degeneracy guarantee of Theorem 4.1.

6. **The phrase "complete characterization" (Section 3 title) slightly overstates what is provided.** The trade-off curves are derived for specific decoder families (linear, Hu's, Google's) and for simulated (Q,P) pairs; the approach is general in principle, but the paper does not provide an analytic characterization of the Pareto frontier for arbitrary decoders.

### Trivial
None.

## Nice-to-Haves
- The connection between the trade-off analysis (Section 3.2) and the algorithm (Section 4.1) could be made more explicit by noting that Theorem 4.1(b,c) shows the pseudorandom acceptance scheme attains the upper-right corner (r = 1−TV(Q,P), WS = Ent(P)) of the Pareto frontier, thereby *constructively* proving the trade-off can be broken. (This is implicit in the current text but worth stating directly.)
- An empirical trade-off curve for a real model pair (e.g., Llama-68M/7B) on a specific prompt distribution would strengthen the claim that the trade-off exists in practice and the proposed algorithm moves the operating point toward the optimum.

## Removed Points

These points were considered but removed as they do not survive verification against the paper or the review guidelines:

- **"Trade-off analysis is decoupled from the algorithm; no proof that the algorithm solves the optimization problem."** — Removed because Theorem 4.1(b,c) *does* prove that the algorithm attains the maximum on both axes (r = 1−TV, WS = Ent(P)), which is exactly the upper-right corner of the trade-off frontier. The critic appears to have missed this.
- **"Theorem 4.1(c) claim is deceptively broad"** (as a fatal issue) — Removed because the theorem's assumption explicitly requires a degenerate decoder ("Assume the decoder S is unbiased and achieves the largest watermark strength (hence it is degenerate by Thm. 3.2)"). The paper also acknowledges the gap for SynthID with finite m. The weakness is real but minor (see Weakness 3), not fatal.
- **"Missing related works"** — Not included, as the reviewer does not have external sources to verify missing references.
- **"No significance tests or confidence intervals"** — Removed because the paper reports 95% confidence intervals (shaded regions in Figure 2, error bars in left panel).
- **"Full derivation from (8) to (10) is missing"** — Removed; the derivation is sketched in the text, which is standard for a page-limited venue.
- **Generic/superficial strengths from Strength Finder** ("the paper addresses an important problem," "the paper targets an interesting question") — Removed; only concrete, evidence-backed strengths are kept.
- **"Unfair comparison" criticisms where asymmetry favors the baseline** — Not applicable; the concern about SynthID is kept as a major weakness because it asymmetrically *hurts* the baseline (comparing MLP+u vs. weighted average), which is a valid concern.

## Novel Insights

The reviews surface two observations that go beyond the paper's own framing. First, the harsh critic's confusion about whether Theorem 4.1 connects to the optimization framework (point removed above) revealingly suggests that the paper's narrative structure—Section 3's Pareto analysis followed by Section 4's algorithm—could benefit from a short bridging statement that explicitly maps the theorem's results back to the trade-off curve. Second, the SynthID detection comparison issue points to a broader methodological point: when introducing a new source of information (the acceptance variable *u*), the paper should demonstrate the *marginal* benefit of that information, not just the joint benefit of adding both information and model capacity. This is a recurring issue in machine learning papers and worth noting.

## Suggestions

- Add an ablation: compare Bayes-MLP (on y^D, y^T, u) against an MLP of the same architecture trained on (y^D, y^T) *without* u. If the improvement of Bayes-MLP over this MLP-no-u baseline mirrors the gap between Ars-τ and Ars-Prior, the role of u is cleanly established.
- Report the empirical frequency of bonus steps for each K ∈ {2,3,4} and verify that removing these tokens from the detection pipeline does not change the ROC curves, or extend the detection rule to handle bonus-step tokens.
- Add a sentence in Section 5 explicitly noting that only the Gumbel-max experiments directly satisfy Theorem 4.1's degeneracy assumption, while the SynthID results represent a practical benefit from the pseudorandom acceptance mechanism even when the decoder is not perfectly degenerate.
- Clarify how repeated context masking interacts with the pseudorandom acceptance mechanism.

## Score and Decision

**Bracketing (Round 1):** Using calibration search on broadly similar watermarking papers, three bands emerged:
- **Weak anchors** (score < 3.5): score 2.0–3.0 — papers with significant flaws or withdrawn. This paper is clearly stronger.
- **Middle anchors** (3.5 < score < 7.5): score 4.5–5.5 — incremental watermarking papers with partial evaluations (CATMark, DynamicBias, OpenStamp, BenchmarkContamination). This paper has a stronger theoretical contribution than these.
- **Strong anchors** (score > 7.5): score 8.0 — papers on different topics (transduction, in-context binding, multi-turn conversation). Not directly comparable on content.

**Round 1 bracket: [5.0, 7.0]** — above typical watermarking methods papers but below the strongest theoretical/empirical packages.

**Narrowing (Round 2):** Searching within (6.0, 7.5) found:
- PMark (7.00, Accept Poster): Strong distortion-free semantic watermark with clean theory and experiments. The paper under review has a similarly strong theoretical contribution but the SynthID ablation weakness makes it less clean.
- LLM Fingerprinting via Semantically Conditioned Watermarks (6.50, Accept Oral): Solid conceptual contribution with comprehensive experiments. The paper under review has stronger theory but the SynthID comparison issue is a comparable concern to the utility-drop issues in that paper.

**Final calibration:** The paper under review is stronger than the 5.0–5.5 anchors (which have weaker theory or more incremental contributions) but has one clear methodological weakness (SynthID ablation) that papers at the 6.5–7.0 level typically resolve. The Gumbel-max results are clean and well-supported; the overall theoretical contribution is substantial. Placing the paper at **6.0** reflects this: it is a solid paper with a genuine theoretical contribution and promising empirical results, held back from a higher score by the need to clean up the SynthID detection comparison.

**Anchor papers retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/.../0hnnPy6vt2.md | 2.00 | 1 | Much weaker — withdrawn paper |
| /home/.../pAeEzS4LwS.md | 2.67 | 1 | Weaker — Reject |
| /home/.../US1UwMHHtS.md | 3.00 | 1 | Weaker — withdrawn |
| /home/.../ROcFqn6Pxi.md | 3.00 | 1 | Weaker — withdrawn |
| /home/.../WFGxFzFDmQ.md | 5.00 | 1 | Comparable novelty but weaker theory |
| /home/.../yr06ivlnaG.md | 4.50 | 1 | Weaker — multi-bit watermark |
| /home/.../DU5eTaQSHT.md | 5.00 | 1 | Weaker — engineering contribution |
| /home/.../Q2DrdrPcYm.md | 5.33 | 1/2 | Weaker — more incremental |
| /home/.../qOyF214xmg.md | 8.00 | 1 | Different topic (transduction) |
| /home/.../UJ2UUjT2ko.md | 8.00 | 1 | Different topic |
| /home/.../VKGTGGcwl6.md | 8.00 | 1 | Different topic |
| /home/.../DM0Y0oL33T.md | 8.00 | 1 | Different topic |
| /home/.../Vvks41GeL9.md | 5.50 | 2 | Slightly weaker — DynamicBias |
| /home/.../EhDgP69DJG.md | 7.00 | 2 | Stronger — PMark (cleaner experiments) |
| /home/.../4AfWqR3quK.md | 5.50 | 2 | Weaker — SynthID analysis paper |
| /home/.../5GVfneFvhq.md | 5.33 | 2 | Different topic (unlearning) |
| /home/.../t38nZqqi3Z.md | 6.50 | 2 | Comparable — stronger experiments, weaker theory |
| /home/.../wyucYNGPiW.md | 6.50 | 2 | Different domain (images) |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>