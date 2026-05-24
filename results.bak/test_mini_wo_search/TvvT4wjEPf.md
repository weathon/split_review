Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes Overflow-Aware activity Regularization (OAR), a novel regularization technique that mitigates numerical overflow in single-ciphertext CGGI-based FHE RNN inference. By training pre-activations to land in "correct" overflow regions (where the sign under modulus matches the sign in ℤ), OAR enables the use of compact encryption parameters while recovering accuracy lost to overflow. The method is validated on a 1.9M-parameter MNIST RNN (28 timesteps), achieving 90.82% top-1 accuracy at 2.1s per sample — within 0.17% of its quantized plaintext baseline — and also on an enlarged 8.48M-parameter, 128-timestep variant.

## Strengths

1. **Novel, well-motivated regularization that directly addresses an identified obstacle.** Section 3 clearly articulates Observations 1 and 2 (correct vs. incorrect overflow regions), then defines OAR mathematically (eq. 2–4) to penalize pre-activations in incorrect regions. Table 1 demonstrates that OAR recovers +71% (5-bit) and +43% (6-bit) relative accuracy improvements over the same model without OAR. This is the paper's core contribution and is well supported.

2. **Systematic evaluation with ablation on regularization rate and visual confirmation.** Table 2 sweeps OAR rates across 5-bit and 6-bit, identifying $10^{-4}$ as optimal. Figure 4 shows pre-activation histograms that visually confirm OAR shifts values from incorrect to correct overflow regions. These ablations build a causal narrative that OAR works through the intended mechanism, not a side effect.

3. **Demonstrated scalability to larger and deeper RNNs.** Section 4.1.4 extends evaluation to an 8.48M-parameter RNN with 128 timesteps, achieving 92.69% test accuracy with OAR — confirming the technique's efficacy beyond the primary setup. The encrypted evaluation (Table 3) shows minimal accuracy degradation ($\leq$0.17%) and low error metrics (near-zero PD, small MAE), demonstrating faithful FHE execution.

4. **Method is clearly described and easy to reproduce in principle.** Algorithm 1 cleanly extends the prior 4-step quantization procedure with OAR and ModSign. The use of a public library (Concrete-Core) and GPU acceleration is clearly documented.

## Weaknesses

### Fatal
None.

### Major

1. **The 274× latency reduction over SHE is an uncontrolled, apples-to-oranges comparison and should not appear as a headline numerical claim.** The paper compares its 2.1s latency on a 1.9M-parameter MNIST RNN (28 timesteps, GPU-accelerated) against SHE's 576s on a 180K-parameter Penn Treebank RNN (25 timesteps, older CPU, fixed-point serialization). These differ in dataset, task, model architecture, model size, quantization scheme, hardware platform, and encryption parameter choices. The paper acknowledges the parameter/layer differences (line 18, line 189) but still presents "274×" as a headline achievement in both the abstract and introduction. This conflates algorithmic improvement with orthogonal differences and misleads readers. The comparison would need to be on the same task and model, or at minimum be accompanied by a per-operation cost breakdown with clear caveats.

2. **"State-of-the-art in scale" claim is inconsistent with the paper's own cited prior work.** The abstract claims a "new state of the art in latency, model performance, and scale." However, Anonymous [2025] — the paper's own foundation — evaluates a 12.6M-parameter RNN with attention over 188 timesteps, which is substantially larger in both parameter count and sequence length. While the current paper achieves far better latency and accuracy, the claim of SOTA *in scale* (which typically connotes model size or sequence length) is inaccurate as written. The authors should either define the specific criteria on which they are genuinely ahead (e.g., largest single-ciphertext CGGI RNN with accurate evaluation) or rephrase.

### Minor

3. **Full-precision float accuracy of the RNN architecture is not reported.** The paper reports its quantized plaintext baseline at 90.99% and states an 8% drop from "99% accuracy of full-precision plaintext MNIST evaluation" (line 189), but that 99% figure appears to refer to a standard CNN result, not the paper's own RNN architecture. Without reporting the full-precision float accuracy of the same RNN, the reader cannot decompose the total accuracy loss into (a) quantization loss vs. (b) encryption noise vs. (c) overflow effects. Adding this single number would significantly strengthen the paper's evidential chain.

4. **No ablation comparing OAR₁ vs. OAR₂.** Both regularizers are defined (eq. 2–3), and the paper notes OAR₂ imposes a higher penalty on values near the center of incorrect regions (line 88). However, all experiments use only OAR₂. A brief comparison (even on one bit-width) would clarify whether OAR₂ is strictly better or whether OAR₁ is a viable alternative, and would remove a loose end.

5. **The statement about ModSign being insufficient alone is vague.** Line 113 states: "Experimenting with the function itself, the model did not quantize and perform well." No quantitative results are given. Reporting the accuracy without OAR (but with ModSign) would substantiate this claim and strengthen the justification for why both components are necessary.

6. **No runtime breakdown.** The paper reports 2.1s total latency but does not break it down (e.g., PBS operations vs. additions vs. GPU overhead). Such a breakdown would help the community target optimization efforts.

### Trivial
None of consequence — the paper is clearly written and well formatted.

## Nice-to-Haves

- A direct latency/accuracy comparison on a shared task with Anonymous [2025]'s approach (without OAR) on the same MNIST RNN would cleanly isolate OAR's contribution. This is not a core flaw since Table 1 already provides a with/without-OAR comparison internally, but it would strengthen the comparative positioning.
- Discussion of the OAR regularization rate's sensitivity across more bit-widths (the paper focuses on 5- and 6-bit in Table 2).
- Convergence analysis: does OAR require more/fewer epochs to reach peak accuracy compared to training without OAR?

## Removed Points

These points have been verified against the paper and removed with justification:

1. **"Below 5-bit, the paper calls 37.10% random — but 5-bit is not random."** Removed. The paper (line 131) clearly states "Below 5-bit, both settings fail to surpass random accuracy levels." 5-bit (37.10%) is not described as random; the text refers to bit-widths <5. Reviewer misread.

2. **"MNIST is not a natural sequence task."** Removed. Processing MNIST rows as 28-timestep sequences is a standard and widely accepted RNN benchmark in the privacy-preserving ML literature (used by the paper's own antecedent Anonymous [2025] and others). This is a standard practice, not a weakness.

3. **"Anonymous [2025] is anonymized and cannot be fully verified."** Removed per Hard Rules: the paper is under double-blind review, and references cited in the paper are assumed to exist. Reproducibility concerns rooted in doubting cited entities are not valid criticisms.

4. **"No comparison to standard unencrypted RNNs on MNIST achieving ~98%."** Removed as scope creep. The paper's goal is to evaluate encrypted vs. plaintext of *its own architecture*; achieving SOTA plaintext accuracy is not a stated contribution. The 99% reference is used as loose context, not as a controlled baseline.

5. **"The paper could mention recent advances in CGGI-based CNNs."** Removed. Missing related works is excluded per instructions, and this is not central to the RNN focus.

6. **Formatting and grammar nitpicks.** Removed per Hard Rules (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated narrative: OAR is a novel and empirically effective technique for a well-characterized problem. The most useful signal from the reviews is the identification of overclaimed comparative positioning (274×, SOTA in scale), which is a presentation issue rather than a technical flaw. The observation that the paper could strengthen its claim decomposition by reporting the full-precision float accuracy of its own architecture is a concrete, actionable suggestion not present in the paper itself.

## Suggestions

1. **Re-cast or heavily qualify the 274× comparison.** Either run a controlled experiment on a shared task (e.g., implement SHE's approach on the MNIST RNN, or your approach on the Penn Treebank task), or replace the raw latency ratio with a per-operation cost comparison accompanied by explicit caveats about differences in dataset, model size, hardware, and encryption parameters.

2. **Correct the "state-of-the-art in scale" wording.** Acknowledge that Anonymous [2025] has larger parameter counts and sequence lengths, and clarify that the current SOTA claim pertains specifically to *accurate single-ciphertext CGGI RNN inference at practical latencies*.

3. **Add the full-precision float accuracy** of the exact RNN architecture (same layers, same units, no quantization) as a single row in Table 1 or a footnote.

4. **Include an OAR₁ vs. OAR₂ ablation** on one representative bit-width (e.g., 6-bit) to close the loose end.

5. **Add quantitative support** for the claim that ModSign alone is insufficient (line 113).

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>