## Summary

This paper proposes Align With Purpose (AWP), a plug-and-play framework that augments CTC training with an additional hinge-loss term that steers the model toward alignments with a desired property. The method samples N alignments per step, applies a property-specific function f_prop to construct "improved" alignments, and trains the model to prefer them over the originals. The paper demonstrates AWP on two properties — low latency (via a left-shift at repetition points) and minimum WER (via word-level error correction) — across three architectures (Stacked ResNet, Wav2Vec2, Conformer) and data scales up to 280K hours.

## Strengths

- **Clean, well-motivated idea backed by a clear observation.** The paper articulates a real gap: CTC treats all perfect alignments equally, creating a controllability problem. The hinge-loss over sampled alignment pairs is an elegant solution that avoids modifying the CTC forward-backward algorithm (Section 2.2, Eq. 4–5).

- **Meaningful latency improvements at large data scales.** On LV-35K, AWP achieves a 592ms reduction in drift latency (341ms → -251ms, Table 1). Critically, these gains are demonstrated at 35K and 280K hour scales where no prior latency method in this paper is evaluated. The negative DL on LV-35K (-251ms) and LS-960 (-79ms) demonstrates optimization beyond the architectural lower bound set by DCL (line 183).

- **Architecture breadth across three model families.** AWP reduces DL on Stacked ResNet (CNN, 66M params), Conformer (hybrid, 30.7M), and improves WER on Wav2Vec2 (transformer, 90M) (Tables 1 and 2). This breadth is stronger evidence of generality than single-architecture demonstrations in prior work.

- **Unified treatment of both perfect and imperfect alignments.** The low-latency application operates on perfect alignments (preserving collapsed text via Eq. 6 at repetition points), while the mWER application targets imperfect alignments. Prior CTC modification methods are typically restricted to one or the other.

- **Controlled ablation of the latency–WER trade-off.** Figure 2 systematically decomposes how the AWP weight α and start epoch independently affect DL and WER, providing practitioners with a practical control knob.

## Weaknesses

### Fatal

None.

### Major

- **Value of N (number of sampled alignments per step) is never specified.** The paper samples "N random alignments" (line 88) and uses N in the hinge loss (Eq. 4), but never states what N is in any experiment. N directly controls both the gradient signal quality and the computational cost; without it, the method cannot be reproduced or its practical feasibility assessed.

- **f_mWER construction is critically underspecified for frame-level CTC alignments.** The paper states: "fix the alignment of this word according to the GT" (line 144) but never explains how to modify a *frame-level* CTC alignment to "fix" a given word. Which frames correspond to the word? Are all frames in the word's time span replaced with correct characters? How are word boundaries determined — by forced alignment, character time spans, or a heuristic? The simplified character-substitution example in Figure 5 does not disambiguate this. For frame-level CTC alignments, this level of detail is essential for both reproducibility and assessing whether the constructed $\bar{v}_a$ is even plausible under the model's distribution.

- **Training dataset for the Stacked ResNet mWER experiment is not specified.** Table 2 reports a Stacked ResNet baseline WER of 2.63 on test-clean. This does not match any dataset scale shown in Table 1 (LS-960: 3.72, LV-35K: 2.42, Internal-280K: 2.34). The Wav2Vec2 setting is clear (finetuned on LS-960, line 169), but the Stacked ResNet training data for the mWER table is absent, making these results impossible to interpret or reproduce.

- **mWER WER improvements are small and lack statistical support.** The headline "4.5% relative improvement" corresponds to 0.26 absolute WER points on Wav2Vec2 test-other (5.82→5.56) and 0.30 points on Stacked ResNet test-other (7.46→7.16). On test-clean, improvements are 0.05 and 0.06 absolute points. No multiple seeds, confidence intervals, or significance tests are reported. For improvements of this magnitude — well within typical ASR training variance — the conclusion that AWP improves WER is plausible but unsupported by the evidence provided.

- **Latency comparison with prior methods is limited to LS-960 (1K hours).** On LS-960, AWP (-79ms DL, 4.38 WER) is essentially tied with TrimTail (-76ms DL, 4.46 WER) — a 3ms and 0.08 WER difference. The paper's claim that "AWP outperforms the other methods, both in terms of WER and latency" (line 185) overstates what is, on the only comparable dataset, a marginal gap with the strongest prior method. No comparisons exist at 35K or 280K, so it is unknown whether prior methods would scale similarly.

### Minor

- **Selective characterization of the latency–WER trade-off.** The abstract claims "up to 590ms in latency optimization with a minor reduction in WER." The 590ms figure comes from LV-35K where WER degrades from 2.72% to 3.28% (+0.56 absolute, +20.6% relative). Describing a 20.6% relative WER increase as "minor" is a framing choice that understates the cost. While the trade-off is acknowledged (line 189), the abstract's wording is selective.

- **No ablation of several hyperparameters (N, λ).** The paper ablate α and start epoch (Figure 2), but N (number of sampled alignments) and λ (hinge margin in Eq. 4) are never ablated or even reported. For a method whose selling point is simplicity, this is a gap.

- **No runtime analysis of the sampling overhead.** Sampling N alignments per step, computing their probabilities, and applying the hinge loss adds non-trivial computational cost. The paper provides no measurement of training time per step with versus without AWP.

### Trivial

None of note beyond the missing experimental details listed above.

## Nice-to-Haves

- Provide a Pareto frontier analysis of the latency–WER trade-off rather than discrete operating points.
- Report the fraction of sampled alignments that contain repetition points (for latency f_prop to be applicable) or imperfect words (for mWER) to demonstrate that useful structural properties are plentiful in practice.
- Extend latency comparisons with prior methods to LV-35K and Internal-280K scales.
- Demonstrate a third, more non-trivial property to strengthen the "general framework" claim.

## Removed Points

These points from the inputs are flagged for removal; treat with caution:

- **Criticism about code not being available at review time** — Removed per policy: criticisms questioning the availability of promised artifacts are not included.
- **Criticism about raw probability vs. log-probability in Eq. 4 being numerically problematic** — Removed as speculative; the paper describes a standard probability computation with no evidence of numerical issues.
- **Criticism that mWER f_prop using GT makes it less general** — Removed as an observation, not a weakness; the paper does not claim equal generality across applications.
- **Generic "could be" concerns** (e.g., "the appendix may specify X") — Removed as speculative; a fatal flaw must be unambiguous given what is on the page.
- **Strength Finder's inflated "outperforms" claim** — Re-calibrated in the strengths above: AWP is competitive with, not clearly superior to, TrimTail on LS-960.
- **Generic/superficial strengths** (e.g., "addresses an important problem") — Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify N and λ for every experiment** — this is non-negotiable for reproducibility.
2. **Provide a precise, algorithmic description of f_mWER** — e.g., via forced alignment to locate word boundaries, then replacing the frame-level token sequence within that span with the correct characters.
3. **Add multiple-seed experiments with confidence intervals** for the mWER results, or scale back the "4.5% improvement" claim to acknowledge the uncertainty.
4. **Include latency comparisons with prior methods at 35K and 280K scales**, or explicitly note their absence and adjust the claim of superiority.
5. **Add a table of training time per step** with and without AWP to help practitioners assess the computational cost.
6. **Slightly temper the abstract's "minor reduction in WER" language** to accurately reflect settings where the WER degradation is substantial (e.g., LV-35K: 2.72→3.28).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>