Now I have all the information I need. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None

### Major
- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me produce the final review.

---

Here is my consolidated review.

## Summary

This paper proposes a systolic array architecture for accelerating spiking neural networks (SNNs) using two techniques: Split-Time Temporal Coding (STT), which limits each neuron to at most one spike per time window (TW), thereby structurizing and sparsifying spike trains; and Integration Through Time (ITT), which processes multiple TWs in parallel across the systolic array's columns. The architecture is claimed to be application-independent, supporting fully-connected, convolutional, and recurrent layers within the same PE design.

## Strengths

1. **STT cleanly converts unstructured, bursty spiking into structured, single-spike-per-window patterns, directly reducing computation and data movement.** The paper demonstrates this via Fig. 1(b) (spike raster before/after STT) and Fig. 5(a) (normalized number of spikes drops inversely with TW size). Section 4.1 explains that weight access per neuron per TW is reduced from multiple time points to a single access, directly cutting the dominant synaptic integration cost.

2. **ITT enables parallel processing of multiple TWs on a systolic array, yielding meaningful weight reuse and latency reduction.** Section 3.1 formalizes the matrix-matrix view of spike inputs across TWs, and Fig. 3(c) shows how PEs in the same row share weights across columns. The evaluation in Section 4.2 (Fig. 5(b)) confirms that L1 cache and global buffer accesses are sharply reduced with ITT+STT relative to a time-serial baseline.

3. **The prefix-sum method recovers equivalent rate-code information from a single spike per TW with minimal overhead.** Section 3.1 and Fig. 4(b) show that using a prefix sum on the integrated synaptic inputs (ISI) yields the same partial sums as a left-aligned rate code. The paper notes that the prefix sum cost is only (TW size − 1) operations per TW, negligible relative to the input integration savings. This is an efficient implementation trick.

4. **The unified PE design handles FC, convolutional, and recurrent layers.** Section 3.3 shows that recurrent layers require only one additional integration step (Step 1-R) compared to feedforward layers, and Fig. 4(a) illustrates the unified PE datapath. The evaluation covers all three layer types, demonstrating architectural generality.

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistent and unexplained performance numbers undermine the quantitative claims.** The abstract (line 13) claims "77X and 60X latency and energy efficiency improvements," while the introduction (line 35) and results section (lines 175-179) consistently state "97X latency and 78X energy efficiency improvements." These are materially different numbers for the same claimed metric, and the paper does not acknowledge or explain the discrepancy. Furthermore, the conclusion (line 192, 206) claims "15,000X EDP improvement," but if latency improves ~97× and energy ~78×, the product is ~7,500× — roughly half the stated value. The paper does not explain whether 15,000× is derived from per-benchmark multiplication followed by averaging, or from a different subset of the data. These inconsistencies erode confidence in the quantitative evidence and must be resolved for the paper to be credible.

2. **Architecture description is too shallow to assess feasibility or enable reproduction.** The paper describes the systolic array at a conceptual level (PEs, row/column mapping, prefix-sum) but omits critical details needed for an architecture paper: (a) no array dimensions or PE count are specified; (b) memory hierarchy sizes (scratchpad, L1 cache, global buffer) are not given; (c) the energy and latency models used in the simulator are not presented — no energy-per-operation values, no cycle counts, no absolute numbers in Joules or seconds are reported; (d) the mapping of convolutional layers to matrix multiplication (e.g., im2col) is not discussed, nor is the handling of varying spatial dimensions across layers. The paper relies on an "architecture simulator" that is not described. Without these details, the claimed 97×/78× improvements cannot be independently verified or reproduced, and the contribution — which is an architecture — remains only partially specified.

3. **Evaluation is limited to three small benchmarks despite claiming "application-independent" and "universal" applicability.** The benchmarks (NMNIST, DVS-Gesture, NTIDIGITS) are all small-scale. No results on larger or more complex tasks (e.g., CIFAR-10, CIFAR-100, ImageNet, or larger temporal datasets like Google Speech Commands) are provided to support the claim of universal applicability. Accuracy drops are non-negligible (e.g., DVS-Gesture drops from ~91.8% to ~87.5% at TW10, per Table 1), and on larger tasks the accuracy loss could be more severe. The "application-independent" claim is not commensurate with the evidence provided.

### Minor

1. **The hardware baseline is underspecified.** The paper compares against a "conventional SNN baseline" described as a time-serial approach that "optimizes data reuse and storage efficiency for each time-point" (line 138). While the comparison is reasonable in principle (the paper's contribution IS enabling parallelism across time), the baseline is not described with enough specificity to understand what optimizations it actually includes. No description is given of its systolic array configuration, memory hierarchy, or dataflow, making it difficult to assess whether the comparison is fair or whether the impressive improvement ratios partly reflect an unoptimized baseline.

2. **Only inference-time application of STT is evaluated; training with STT is not explored.** The paper applies STT only to pre-trained models at inference time (line 183). Training with the one-spike-per-TW constraint (e.g., via surrogate gradients) could potentially reduce accuracy loss or yield different accuracy-efficiency tradeoffs. This is acknowledged as future work (or not at all), but it limits the paper's current scope.

3. **The energy analysis shows only normalized/relative numbers.** Fig. 5(b) and Fig. 6 show energy dissipation improvements as relative comparisons (normalized), without providing absolute energy values (in Joules or pJ per inference). Combined with the missing energy model parameters, this makes it difficult to evaluate the absolute efficiency of the proposed architecture.

4. **The ML-HW tradeoff analysis (Fig. 6d) is presented at a high level without per-benchmark breakdowns.** Table 1 reports accuracy but not the corresponding hardware metrics per benchmark. A table showing per-benchmark latency, energy, and EDP alongside accuracy for each TW size would be far more informative than relative curves alone.

### Trivial
None.

## Nice-to-Haves

- Comparing against additional baselines such as a systolic array processing one time point at a time (spatially parallel but time-sequential) would strengthen the evaluation and isolate the specific benefits of STT+ITT.
- Incorporating STT into training (e.g., via surrogate gradient methods) could potentially reduce accuracy loss and is a natural next step.
- An ablation study separating the contributions of STT alone, ITT alone, and the combined approach would help readers understand where the gains come from.

## Removed Points

- **"Strawman baseline" criticism (Harsh Critic's point 1):** The paper clearly describes its baseline as a time-serial approach without STT/ITT, citing prior work (Khodamoradi et al., Neil & Liu, Shen et al.). This is a reasonable comparison for a paper whose contribution is enabling time-parallel processing. The criticism that the baseline should be compared against neuromorphic chips (Loihi, TrueNorth) or other systolic-array SNN proposals demands scope outside the paper's stated contribution. The baseline comparison is conventional and appropriate; labeling it a "strawman" is an overstatement.

- **Criticism about missing appendix content (Section D) and non-specified hyperparameters:** These sections exist in the original submission but were stripped by the PDF parser. Per the hard rules, such criticisms should be removed.

- **Strength Finder's claim that the "single most important piece of evidence" is 15,000× EDP improvement:** This conflicts with the verified weakness about the EDP number being unexplained and inconsistent with the individual latency/energy claims. Removed as a central evidence point due to the inconsistency.

- **Criticism about novelty of STT (being a form of time-to-first-spike encoding):** While STT does share conceptual similarity with TTFS coding, the paper's contribution is the specific application to TW-level structuring for systolic array parallelism, not the encoding scheme in isolation. This criticism confuses the encoding concept with the combined STT+ITT+systolic-array contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any insight that the paper itself does not already articulate.

## Suggestions

1. **Harmonize all quantitative claims.** The abstract (77×/60×) must be reconciled with the body (97×/78×). The EDP improvement of 15,000× must be clearly derived from per-benchmark data — show the per-benchmark latency, energy, and EDP improvements in a table so readers can verify the calculation.
2. **Provide architectural specifications.** Include systolic array dimensions, memory hierarchy sizes (scratchpad, L1, global buffer), and the energy model parameters (energy per MAC, per memory access at each level) to enable reproducibility.
3. **Add absolute numbers.** Supplement normalized/relative plots with absolute latency (cycle counts or seconds) and absolute energy (Joules or pJ) for at least one representative configuration.
4. **Expand the benchmark set.** Results on at least one larger-scale task (e.g., CIFAR-10 SNN conversion or a larger temporal dataset) would significantly strengthen the "application-independent" claim.
5. **Better specify the baseline.** Describe the baseline architecture with enough detail that readers understand what optimizations it includes (array configuration, dataflow, memory sizes).

## Score and Decision

This paper presents conceptually interesting ideas (STT and ITT for systolic-array SNN acceleration) with a clean algorithmic formulation and a clever prefix-sum trick. However, the paper has significant presentation and evidential weaknesses that prevent acceptance in its current form: (1) the quantitative claims are internally inconsistent (77× vs 97×, unexplained 15,000× EDP), (2) the architecture is described at a level too shallow to be reproducible, and (3) the evaluation is limited to three small benchmarks. These issues are addressable with substantial revisions, but as presented, the paper does not provide a credible and verifiable demonstration of its claimed efficiency.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>