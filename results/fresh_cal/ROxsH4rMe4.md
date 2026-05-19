Now I have thoroughly verified the paper against all reviewer claims. Let me produce the consolidated review.

## Summary

The paper proposes a systolic-array SNN accelerator combining two techniques: Split-Time Temporal Coding (STT), which compresses irregular spike trains so each neuron fires at most once per time window; and Integration Through Time (ITT), which processes multiple time windows in parallel across array columns. The core ideas address a real bottleneck in SNN acceleration: unstructured temporal sparsity causing repeated, inefficient data movement. The architecture is evaluated on three benchmarks (NMNIST, DVS-Gesture, NTIDIGITS) covering FC, CONV, and recurrent layers.

## Strengths

- **Novel STT technique with clear mechanism.** Section 2.1 defines three rules for compressing a TW's spike activity into at most one spike whose timing encodes rate information. The paper shows that competitive accuracy is maintained at moderate TW sizes (e.g., NMNIST: 99.17% → 99.09% at TW=10; DVS-Gesture: 96.70% → 95.87% at TW=10) while drastically reducing per-TW computations.

- **ITT enables time-parallel processing on a systolic array.** Section 3.1 and Figure 3(c) demonstrate that mapping different TWs to different columns of a systolic array allows concurrent processing of multiple time windows with weight reuse across rows, directly addressing the key bottleneck of sequential time-point processing.

- **Tunable accuracy–performance trade-off via a single parameter (TW size).** Figure 6(d) systematically plots EDP vs. accuracy across TW sizes, showing that the method enables application-specific optimization without requiring complex hyperparameter tuning.

- **Architecture supports FC, CONV, and recurrent layers with minimal extension.** Section 3.3 shows that recurrent layers require only one additional integration step beyond feedforward processing, and the evaluation covers all three layer types.

## Weaknesses

### Fatal
None.

### Major

- **Abstract contains a different set of headline numbers than the introduction and results.** The abstract (line 13) claims "77X and 60X latency and energy efficiency improvements," while the introduction (line 35) and results section (lines 175, 179) consistently report "97X latency and 78X energy efficiency improvements." The 15,000X EDP figure in the conclusion (line 206) is a different metric and not contradictory, but the 77X/60X vs. 97X/78X discrepancy is a concrete error that undermines reader trust. A reader cannot tell which numbers are correct without guessing that the abstract has a typo.

- **The baseline is insufficiently specified to assess the magnitude of the claimed improvements.** The hardware baseline is described only as a "time-serial approach" that "optimizes data reuse and storage efficiency for each time-point" (line 138), referencing Khodamoradi et al. (2021); Neil & Liu (2014); Shen et al. (2016). No architectural parameters are given: systolic array dimensions, memory hierarchy sizes, clock frequency, technology node, or power model. All results are normalized, so there is no way to assess whether the 78X–97X improvements come from STT/ITT or from a weak baseline. The paper runs a controlled comparison (same arch with/without STT/ITT), which mitigates this concern partially but does not eliminate it — the magnitude depends on how aggressive the baseline's data-reuse optimizations are, and that is not specified.

### Minor

- **STT's encoding function from original spikes to the single-spike timing is ambiguously described.** Rule 2 (line 59) says "the spike count within a TW is represented by the timing of a single spike," while the example (line 63) uses time-to-first-spike (TTFS), not spike count, to compute TFFS. If the input neuron fires 4 spikes in a TW of size 5, the timing is set to TTFS=1, giving TFFS=4 — but this equals the spike count only because the spikes start at time step 1. The precise mapping (spike count vs. TTFS) and whether it generalizes to arbitrary firing patterns is not spelled out, which hurts reproducibility.

- **Accuracy trade-off is downplayed in the abstract.** The abstract (line 10) claims "competitive classification accuracy without a huge drop." Yet for NTIDIGITS at TW=20, accuracy drops from 93.29% to 88.49% (4.8% absolute), which is substantial for a ~93% task. The paper does acknowledge this in Section 4.4 ("non-negligible classification accuracy drop"), but the front matter should qualify the trade-off more carefully.

- **Overhead of the prefix-sum computation per neuron per TW is not quantified.** The paper claims (line 124) that the prefix sum costs (TW size − 1) additions per neuron per TW, which "is negligible compared to input integration steps." For TW=20, this is 19 additions per neuron per TW. The paper does not provide a breakdown showing how this compares to the total operations, nor does it account for this overhead in the reported energy/latency results.

- **"Application-independent" and "universally applicable" claims are overstated relative to the evidence base.** The paper tests three relatively small benchmarks (10–11 classes each). While FC, CONV, and recurrent layers are covered, strong claims of universality would require demonstration on larger-scale tasks (e.g., ImageNet-scale SNNs) or deeper networks.

### Trivial

- The abstract uses "for different benchmarks on average," which is grammatically awkward and contributes to the number-confusion problem.

## Nice-to-Haves

- **Applying STT during training rather than only at inference.** The paper uses pre-trained networks (Zhang & Li 2020) and applies STT only at inference. Training with STT-aware regularization could recover some of the accuracy lost at larger TW sizes and would be a stronger evaluation of STT's viability.
- **Absolute performance numbers** (cycles, pJ, microseconds) for a representative configuration would improve interpretability and reproducibility, even if the paper's main comparisons are relative.

## Removed Points

- **"No comparison to Loihi 2 / modern commercial chips"** — REMOVED as scope creep. The paper targets a systolic array architecture, which is a fundamentally different design point from Loihi's mesh-of-cores. The paper's baseline is a conventional time-serial SNN accelerator, which is a reasonable comparison for demonstrating the benefits of STT/ITT.
- **"STT encoding mapping not specified for all cases"** — The reviewer's specific concern about "if a neuron fires 3 spikes in a TW of size 5, does it always fire at time step 3?" is rooted in a misunderstanding; the paper uses TTFS (time to first spike), not spike count directly, to determine the single-spike timing. However, the general ambiguity between spike-count encoding and TTFS encoding is kept as a Minor weakness above.
- **"Reproducibility concern about missing appendix/proofs"** — REMOVED per hard rules (appendix is stripped by parser; proofs may exist in the original submission).
- **"Not enough baselines"** — REMOVED as vague and not clearly specified which baselines are missing. The paper provides a controlled comparison against a conventional time-serial approach.
- **"Missing area/power analysis of the systolic array"** — REMOVED. This is not standard for a paper that focuses on data-movement improvements. The paper provides energy and latency results; area estimation would be nice-to-have but not required.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine number inconsistency in the abstract but do not provide new analytical insights beyond what the paper already claims.

## Suggestions

1. **Fix the abstract numbers** to match the introduction and results (97X latency, 78X energy), or clearly explain why the abstract reports different figures (e.g., if they are per-benchmark best numbers vs. averages).
2. **Provide a concrete baseline specification** in the main text or a supplementary table: array dimensions, memory sizes, clock frequency, and the optimizations included in the "data-reuse-efficient time-serial" baseline. This would allow readers to gauge how aggressive the baseline is and whether the 78X–97X claims are calibrated appropriately.
3. **Clarify the STT encoding function**: explicitly state whether the single-spike timing per TW is determined by time-to-first-spike, spike-count, or a different rule, and provide the general formula for the mapping.
4. **Quantify the prefix-sum overhead** and include it in the reported energy/latency numbers, or provide a breakdown showing why it is negligible.
5. **Qualify the accuracy claim in the abstract** (e.g., "competitive accuracy with typical drops of 0.1–1% at moderate compression levels, and up to 5% at aggressive compression").

## Score and Decision

The paper makes a genuine contribution: STT and ITT are well-motivated techniques that address a real bottleneck in SNN acceleration. The core results (97X/78X improvements) are directionally plausible given the compression factor. The number inconsistency in the abstract is the most serious issue but is fixable. The baseline description, while sparse, represents a reasonable controlled comparison. No fatal methodological flaws were identified.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>