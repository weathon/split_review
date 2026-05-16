Now I have a thorough understanding of the paper. Let me synthesize the review.

## Summary

The paper proposes TIGER, a time-frequency domain speech separation model that achieves dramatic parameter (94.3%) and MAC (95.3%) reductions relative to TF-GridNet while remaining competitive or superior on complex acoustic scenarios. It also introduces EchoSet, a reverberation/noise dataset built on SoundSpaces 2.0 and Matterport3D that models room geometry, materials, and occlusions. On EchoSet (the most challenging benchmark), TIGER large (0.82M params) surpasses TF-GridNet (14.43M params) by 0.49 dB SDRi; on cleaner benchmarks it trails by small margins (6% on Libri2Mix, 2% on LRS2-2Mix). Extensive ablations validate the contributions of the MSA and F³A modules.

## Strengths

1. **Extreme efficiency with competitive performance on complex data.** TIGER large has only 0.82M parameters and 15.27 G/s MACs — a 94.3% parameter reduction and 95.3% MAC reduction versus TF-GridNet — yet achieves the best SDRi on EchoSet (14.22 vs. 13.73) and is within 2–6% on standard benchmarks (Table 2). This is genuinely the first sub-1M-parameter speech separation model competitive with SOTA.

2. **EchoSet dataset addresses a genuine gap in simulation fidelity.** Unlike prior datasets (WHAMR!, Libri2Mix, LRS2-2Mix), EchoSet accounts for room shape, material properties, object occlusions within the same acoustic scene, and random overlap ratios (Table 1). The dataset construction using SoundSpaces 2.0 and Matterport3D is clearly described and methodologically sound.

3. **Convincing ablation studies validate architectural contributions.** Tables 4–7 systematically isolate the value of band-split (LowFreqNarrowSplit beats EvenSplit and NonSplit), MSA (removing it drops SDRi from 13.15 to 7.58), and F³A (removing it drops to 12.34). Replacement experiments with LSTM, Mamba, and SRU show that MSA and F³A achieve the best efficiency-performance trade-off — alternatives use 2–3× more parameters and MACs.

4. **Generalization beyond speaker separation is demonstrated.** The paper reports that TIGER applied to cinematic sound separation achieves a 39.4% SDR improvement over BSRNN with 97.3% fewer parameters and 77.6% fewer MACs (Section 6.2), showing the architecture's versatility.

## Weaknesses

### Fatal

None.

### Major

1. **Real-world validation of EchoSet (Figure 1) lacks essential numerical support.** The paper's claim that "the gap between EchoSet and real-world audio is relatively small" and that TIGER "achieved the best separation performance" on real-world data rests entirely on a bar chart with no reported numerical values, no error bars, no specification of evaluation metrics (SDRi? SI-SDRi?), and no statistical significance assessment. The description of the real-world data collection ("10 real-world environments and 40 speakers...followed the same mixing method as LRS2-2Mix") is too vague to be reproducible. This is the central experiment validating the dataset contribution, yet it is presented at a level of rigor well below the rest of the paper. *(Verified: lines 170–172 describe the data; Figure 1 is a bare bar chart with no numbers.)*

2. **Missing architectural hyperparameters impair reproducibility.** Several critical dimensions are not specified numerically: the feature channel dimension \(N\), the hidden dimension \(H\) in the MSA module, the number of downsampling scales \(D\), the number of attention heads \(A\), and the exact sub-band width boundaries \(G_k\) for the LowFreqNarrowSplit scheme. STFT parameters (window size, hop length, FFT size) are also omitted. Without these, the method cannot be faithfully re-implemented from the paper alone. *(Verified: the paper defines these symbols but never assigns concrete values.)*

### Minor

1. **The "~5% improvement" claim in the introduction is imprecise.** Line 31 states TIGER "improved the performance by about 5% compared with TF-GridNet" on EchoSet. The actual improvement is 3.6% for SDRi and 6.8% for SI-SDRi. While "about 5%" could be an approximate average, it is slightly misleading on the primary metric. *(Verified: (14.22−13.73)/13.73 ≈ 3.57%.)*

2. **Cinematic sound separation results are reported but under-developed.** Section 6.2 gives percentage improvements (39.4% SDR gain, 97.3% parameter reduction) but provides no comparison table, no description of the evaluation dataset, no baseline protocol, and no experimental details. The reader is directed to a project page. This is a potentially strong result that deserves proper experimental exposition in the main paper. *(Verified: lines 253–254 contain the numbers but no table or evaluation details.)*

3. **The abstract's phrasing could inadvertently mislead about the breadth of superiority.** The abstract states TIGER achieves "performance surpassing SOTA model TF-GridNet" — but this is qualified by "On EchoSet and real-world data." However, a casual reader could miss the qualifier and assume TIGER uniformly surpasses TF-GridNet. The paper's own discussion (Section 6.2) honestly acknowledges the pattern (TIGER shines on complex data, trails slightly on clean benchmarks), and the abstract should more visibly reflect this nuance.

4. **The paper describes LRS2-2Mix as having "Full" overlap (Table 1)** but does not reconcile this with the original LRS2-2Mix mixing procedure. This is a factual claim about a prior dataset that should be verified against the original source.

### Trivial

- Line 171 says the real-world data "followed the same mixing method as LRS2-2Mix" — LRS2-2Mix is a dataset, not a mixing procedure. This phrasing is ambiguous; the intended meaning (the procedure described in the LRS2-2Mix paper) should be clarified.
- Line 31: "EchoSet is more close to the real-world data" (grammar).

## Nice-to-Haves

- **Confidence intervals or standard deviations** on main results (Tables 2–3) are not standard in the speech separation literature for large-scale benchmark evaluations, but would strengthen the 0.49 dB EchoSet advantage over TF-GridNet.
- **Explicit comparison of computational cost methodology** between MACs reported here and those in the TF-GridNet paper would help readers reconcile the numbers.
- **Ablation controlling for parameter count** in the MSA/F³A replacement experiments (Tables 6–7) would rule out the confound that the comparison conflates architectural efficiency with capacity differences. The current comparison is still informative but not perfectly controlled.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Overclaiming of surpassing SOTA" — removed as partially a misreading.** The harsh critic states the abstract claims surpassing TF-GridNet without qualification. This is inaccurate: the abstract explicitly says "On EchoSet and real-world data." The claim is accurate for EchoSet and could be accurate for real-world data if Figure 1 supported it (it does not — see Major weakness #1). The critic's framing that TIGER is "clearly worse" on standard benchmarks ignores the paper's own nuanced discussion showing competitive (not "clearly worse") performance with 95% fewer resources. The core of this concern is better captured by Minor weakness #3 (phrasing clarity).

- **"MACs for TF-GridNet seem excessively high" — removed.** The paper specifies MACs are "calculated for one second of audio at 16 kHz" (line 173). Different paper-to-paper MAC computations may not use identical counting methods. This is a methodological disagreement, not an error in the paper, and the paper transparently states its computation basis.

- **"LRS2-2Mix mixing method confusion" — down from minor to removed/trivial.** The paper likely means "the mixing procedure described in the LRS2-2Mix work." This is a clarity issue, not a substantive error.

- **"Baseline reproducibility — not stated whether baselines were tuned" — removed.** For standard benchmarks (Libri2Mix, LRS2-2Mix), published numbers are the norm. For EchoSet, the paper states "All the models were trained and tested on EchoSet" (line 257) with the same configuration. This concern is about a convention the paper follows.

- **Strength Finder's generic strengths dropped.** Several claimed strengths are generic ("Ablation on band-split schemes confirms the value of prior-knowledge-driven frequency division" — this is just describing Table 4, not a standalone strength). These are subsumed under the core strengths.

## Novel Insights

The reviews surface an interesting tension: the paper's strongest selling points (efficiency on complex data, realistic dataset) are also its weakest-supported claims (real-world validation is bare, the EchoSet advantage is a 0.49 dB single-dataset result without variance). This suggests the paper would benefit much more from investing in rigorous real-world evaluation than from further architectural refinement. The reviewers agree that the architectural and dataset contributions are sound; the disagreement is about whether the current level of evidence for the generalization claims meets the bar. An insightful observation is that the paper's own ablation methodology (Tables 5–7) is stronger than its evaluation methodology (Figure 1), creating an asymmetry where internal validity is high but external validity is asserted rather than demonstrated.

None beyond the paper's own contributions.

## Suggestions

1. **Add a table with numerical SDRi/SI-SDRi values for the real-world test (Figure 1),** including sample sizes, error bars, and a clear description of the recording setup (microphones, distances, room types). This single addition would address the most serious weakness.

2. **Report the missing architectural hyperparameters** (\(N, H, D, A\)) and the exact sub-band boundaries for LowFreqNarrowSplit, along with STFT parameters (window size, hop, FFT size). This is essential for reproducibility.

3. **Add a proper experimental section for the cinematic sound separation results** — at minimum a table comparing TIGER with BSRNN on a well-defined benchmark, with dataset and protocol described.

4. **Rephrase the abstract** to more prominently reflect that TIGER's advantage over TF-GridNet is conditional on acoustic complexity, and that on clean benchmarks it is competitive (not superior) while using dramatically fewer resources.

5. **Clarify the LRS2-2Mix overlap characterization** by verifying against the original source, or adding a citation-specific justification.

## Score and Decision

This paper makes two solid contributions — an efficient architecture with a well-motivated design and a carefully constructed dataset that addresses real limitations of prior benchmarks. The ablation studies are thorough and convincing. The weaknesses are primarily in presentation and evaluation rigor: the key real-world generalization experiment lacks numerical reporting, architectural details needed for reproduction are omitted, and some claims could be more precisely scoped. These are all fixable in revision. The core methodology and results are sound.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>