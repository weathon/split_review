Now I have a thorough understanding of the paper. Let me synthesize the consolidated review.

## Summary

This paper proposes Split-Time Temporal Coding (STT), which limits each neuron to at most one spike per time window (TW) and encodes rate via spike timing, and Integration Through Time (ITT), which maps multiple TWs across columns of a systolic array for parallel temporal processing. Together, STT+ITT aim to reduce the unstructured data movement and repeated weight accesses that plague conventional time-serial SNN acceleration. The approach is demonstrated on three neuromorphic benchmarks (NMNIST, DVS-Gesture, NTIDIGITS) using an architectural simulator.

## Strengths

1. **Novel coding scheme that structurizes irregular spike trains.** STT converts unstructured, multi-spike-per-TW activity into a regular pattern (at most one spike per neuron per TW, with timing encoding rate). Section 2.1 clearly describes the three coding rules and Figure 2 illustrates how this eliminates repeated weight accesses across time points — a genuine architectural insight.

2. **ITT enables parallel processing of multiple time windows on a systolic array, improving data reuse in both space and time.** Section 3.1 defines the mapping: each column processes a different TW, weights are reused across rows, and the prefix-sum mechanism (Figure 4) recovers the equivalent of left-aligned rate-code integration. The architectural mapping is clearly reasoned.

3. **Demonstrates applicability across FC, convolutional, and recurrent layers.** Sections 3.3 and 4.3 show the same PE design handles all three layer types (with one additional step for recurrent layers, adopting the self-recurrent structure from Zhang & Li 2021). Table 1 reports results on three fundamentally different network architectures, supporting the "application-independent" claim.

4. **Provides a tunable accuracy-efficiency trade-off via a single parameter (TW size).** Section 4.4 and Figure 6(d) explicitly frame the ML-HW trade-off, and the paper acknowledges that aggressive TW sizes cause accuracy loss. This honest presentation of the trade-off is a strength.

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistent performance numbers across abstract, introduction, and body undermine quantitative claims.** The abstract (line 13) reports "77X and 60X latency and energy efficiency improvements," while the introduction (line 35) and Section 4.3 (lines 175, 179) report "97X latency and 78X energy efficiency improvements." The conclusion (line 206) separately reports "15,000X EDP improvement." The paper never explains these discrepancies. Even if the numbers come from different averaging methods or TW configurations, the inconsistency erodes confidence in all quantitative claims and must be resolved.

2. **The hardware baseline is underspecified, making it difficult to assess the significance of the claimed improvements.** The paper (line 138) describes the baseline as one that "optimizes data reuse and storage efficiency for each time-point (time-serial approach)" without STT/ITT, citing Khodamoradi et al. (2021); Neil & Liu (2014); Shen et al. (2016). However, concrete details are missing: memory hierarchy parameters (cache sizes, global buffer size, off-chip bandwidth), systolic array dimensions, clock frequency, technology node, and what "optimizes data reuse" means in terms of dataflow policy. Without these, the 97×/78× improvements cannot be independently assessed. The baseline may be reasonable for isolating STT+ITT's benefit (as the paper claims it follows prior published approaches), but the lack of specification is a significant gap.

### Minor

3. **No error bars or statistical significance reported for accuracy numbers.** Table 1 reports single accuracy values per configuration without indicating variance across runs. While single-run inference is common in some architecture papers, stating whether accuracy is averaged over multiple trials would strengthen the claims, especially given that STT is applied post-hoc without retraining.

4. **The paper does not quantify the hardware overhead of STT encoding/decoding and prefix-sum computation.** The encoder and decoder are shown in Figure 3(b) but their area, energy, and latency costs are not reported. The paper (line 124) states prefix-sum operations "(TW size - 1)" are "negligible compared to input integration steps" but provides no supporting measurements. Similarly, the overhead of converting original spike trains to STT at the input layer and decoding at the output layer is unaccounted for.

5. **The simulation environment and its parameters are not described in the main text.** Section 4 references "setups described in Section D" (appendix, stripped by the parser), but the main body should include at least the key parameters of the simulator: memory hierarchy configuration, systolic array dimensions, assumed clock frequency, and energy modeling methodology (e.g., whether it uses empirically calibrated energy per access numbers from CACTI or similar). Without these, the energy and latency numbers are difficult to evaluate.

6. **The claim "application-independent" (title and Section 2.1) is overreaching for a three-benchmark evaluation on shallow networks.** The deepest network has only three layers (from Table 1 description). Testing on deeper architectures (e.g., VGG-style SNNs) would be needed to substantiate this claim. The paper's own data shows STT's benefits depend on temporal sparsity patterns, which vary across layers and tasks.

### Trivial
None.

## Nice-to-Haves

- Retraining networks with STT constraints (i.e., training under the "at most one spike per TW" rule) would likely recover accuracy lost at larger TW sizes and make the trade-off curve significantly more favorable. A single case study would strengthen the paper considerably.
- A roofline model or comparison against a published SNN accelerator (e.g., Loihi, TrueNorth) using normalized metrics (e.g., throughput per watt) would help contextualize the absolute gains, though this is not strictly required given the different architectural paradigms.
- A limitations section acknowledging that STT assumes rate-based coding and may not be suitable for temporal-code SNNs, and that the architecture has not been implemented in RTL or silicon, would improve scientific rigor.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Unfair and unrealistic baseline" (Harsh Critic's Claim 1, in full).** The reviewer claims the baseline is "naive" and "does not exploit any sparsity or data reuse optimisations." However, the paper (line 138) explicitly states the baseline "optimizes data reuse and storage efficiency for each time-point (time-serial approach)" and cites three prior works (Khodamoradi et al. 2021; Neil & Liu 2014; Shen et al. 2016) that use such approaches. The baseline is a conventional time-serial accelerator, not a strawman — it represents the standard practice for SNN acceleration before STT/ITT. The reviewer's demand for comparison with Loihi/TrueNorth is scope creep, as those are fundamentally different architectural paradigms (multi-core asynchronous designs) that cannot be meaningfully compared via the same simulator without extensive re-implementation.

2. **"Lack of comparison with prior SNN accelerators" (Claim 4).** The paper discusses Loihi and TrueNorth qualitatively (line 23) and positions its contribution as a different approach (systolic array with temporal compression). Comparing against them would require porting workloads to hardware one does not have access to, or building detailed simulators of those chips — an unreasonable expectation for an architecture proposal paper. The chosen baseline (time-serial, optimized for data reuse) is the correct control for isolating STT+ITT's benefits.

3. **Harsh Critic's claim that "accuracy degradation is downplayed" (Claim 3) in its strongest form.** The paper acknowledges "local temporal information loss" and "non-negligible classification accuracy drop" (lines 181, 190). The trade-off is presented transparently as tunable. Without being able to read Table 1's image data directly, the specific numbers claimed by the reviewer (98.86% → 89.80% on NMNIST) cannot be verified, but the paper's own description frames the drop as manageable at reasonable TW sizes.

4. **Demand for "competitive baseline" (e.g., Loihi or blocked-GEMM sparse accelerator) from Strengthening section.** As noted above, this is scope creep beyond what an architecture proposal should be expected to provide.

5. **All pure formatting/style nitpicks, parser artifacts, and missing appendix content complaints.** These are parser-stripped sections, not author omissions.

## Novel Insights

The reviews reveal that the paper's main contribution is genuinely architectural rather than algorithmic: the key insight is that by imposing a structural constraint (≤1 spike per TW) on already-trained networks, one can convert the irregular temporal pattern of SNN computation into something amenable to systolic-array acceleration — namely, a structured sparse matrix whose nonzero entries are uniformly spaced across columns. The ITT mapping then exploits this regularity for parallelism. This is a different direction from the event-driven, core-to-core communication paradigm of Loihi/TrueNorth, and offers potential for higher utilization of dense compute fabrics. The unresolved tension is that the claimed benefit (97×/78×) is hard to verify without a more detailed baseline specification, but the underlying architectural idea is sound.

## Suggestions

1. **Resolve the numerical inconsistency.** Unify the abstract and introduction numbers (77×/60× vs. 97×/78×). Clearly state which TW configuration and which averaging method (arithmetic/geometric mean across which benchmarks) produces each number. Provide absolute latency and energy values (cycles and nJ) in addition to normalized ratios.

2. **Specify the baseline in detail.** Describe the memory hierarchy (cache sizes, global buffer, off-chip bandwidth), array dimensions, clock frequency, technology node, and dataflow policy assumed for both baseline and proposed architecture. If the baseline follows prior published works, state which specific optimizations from those works are included.

3. **Report the overhead of STT encoder/decoder hardware** (area, energy, latency) to substantiate the claim that these costs are "negligible."

4. **Add error bars** for accuracy results (e.g., mean and standard deviation over 3–5 runs) and clarify whether accuracy numbers are for a single run or averaged.

5. **Include a limitations paragraph** in the conclusion acknowledging that: (a) STT is designed for rate-coded networks, (b) the architecture has not been implemented in RTL or fabricated, and (c) the evaluation is limited to three (shallow) benchmarks.

## Score and Decision

The paper proposes genuinely novel ideas (STT and ITT) for SNN acceleration with a clear architectural rationale. The core contribution — using temporal-window-based coding to enable systolic-array parallelism across time — is interesting and well-motivated. However, the evaluation has significant weaknesses: (1) inconsistent performance numbers (77×/60× vs. 97×/78×) that are never reconciled, and (2) an underspecified hardware baseline that makes the claimed improvements difficult to assess. Additionally, the lack of quantified encoder/decoder overhead and error bars weakens the evidential support.

These issues are addressable in a revision, but in their current form they undermine confidence in the paper's central quantitative claims. The paper would benefit from a major revision that resolves the numerical inconsistencies, specifies the baseline explicitly, and reports hardware overhead.

**MY FINAL SCORE:** <pineapple>5.0</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>