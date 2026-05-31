Now let me perform calibration searches to score this paper.Initial bracket: **4.0 – 6.0**. The most relevant anchors are ANN-to-SNN conversion papers scoring 5.75, but the paper under review has notable weaknesses around energy measurement, T-degradation, and incomplete baseline comparison. Let me narrow.Now I have enough data. Let me read the QAC paper briefly for comparison.Now I have enough to write the final review. Let me compile it.

---

## Summary

This paper proposes a "dual ANN-to-SNN conversion" pipeline that starts from a statically quantized LLM (PrefixQuant W6A6) rather than a specially trained, conversion-friendly ANN. The key innovation is an Integer Spiking (IS) neuron with multi-hierarchical thresholds designed to emulate the integer quantization function, formally related to it via Theorems 1–2. A layer-wise calibration step then optimizes only neuron thresholds and initial membrane potentials (0.107K parameters per layer) to minimize conversion errors, particularly the unevenness error that arises from temporal spike timing dynamics. Experiments on LLaMA-2-7B and LLaMA-3-8B demonstrate that the calibrated SNN at T=2 recovers near-quantization-baseline accuracy (67.65 vs. 68.70 avg. accuracy for LLaMA-2-7B) while using far fewer learnable parameters than weight fine-tuning.

---

## Strengths

- **Parameter-efficient calibration with striking result (Table 4):** The calibration method tunes only thresholds and initial membrane potentials (0.107K parameters per layer) and outperforms full layer-wise weight fine-tuning (202.375M parameters) on LLaMA-2-7B: 67.65 avg. accuracy vs. 66.39. This is a concrete, quantified finding that directly validates the paper's core claim about parameter efficiency.

- **Theoretically grounded IS neuron design (Theorems 1–2, Eqs. 8–10):** Theorems 1 and 2 formally specify the exact conditions under which the IS neuron's cumulative spike output reproduces the symmetric quantization function of PrefixQuant. Remark 1 honestly acknowledges that integer constraints mean LT = 2ⁿ − 1 rarely holds exactly for T > 1, providing a principled approximation rationale.

- **First large-scale ANN-to-SNN conversion applied to LLMs at LLaMA-2-7B/LLaMA-3-8B scale**, eliminating the prohibitive cost of training a conversion-specific ANN (Table 1 comparison with conventional pipeline). The use of an off-the-shelf quantized model as the starting point is a pragmatic and scalable design choice.

- **Calibration error analysis grounded in figure evidence (Figure 3):** Theorem 3 decomposes the total conversion error into clipping, quantization, and unevenness components with a layer-wise bound; Figure 3 confirms empirically that unevenness error (measured as the gap between ANN vs. QANN and ANN vs. SNN MSE) is the dominant source of degradation, directly motivating the calibration design.

---

## Weaknesses

### Fatal
None.

### Major

- **The paper's central motivation—energy efficiency—is entirely undemonstrated.** The abstract states SNNs offer "brain-inspired efficiency and low power consumption, making them ideal for edge deployment," and Contribution 3 states the framework "potentially reduces the energy consumption of LLMs." Yet no energy measurement, synaptic operation (SOP) count, theoretical MAC estimate, or comparison against the W6A6 quantized baseline on computational cost appears anywhere in the paper. This is not a peripheral gap—it is the only reason a practitioner would deploy a spiking model rather than using PrefixQuant directly. Without any efficiency measurement, the SNN framing is technically interesting but pragmatically unjustified. A reasonable theoretical estimate of SOPs vs. MACs, even for a single inference, would suffice.

- **Performance degrades monotonically with T, yet the temporal dynamics of SNNs are the paper's entire raison d'être.** From Table 2 for LLaMA-2-7B: PPL is 5.76 (PrefixQuant), 5.61 (Ours, T=1), 7.39 (Ours, T=2), 9.71 (Ours, T=4), 12.03 (Ours, T=8). The paper attributes this to "growing unevenness error introduced by the larger time-step" (Section 4.2), which is an observation, not a mechanism or explanation. This matters because in standard ANN-to-SNN theory, more time steps should produce a finer-grained approximation; here, the opposite holds. The paper does not diagnose why, nor does it provide an ablation separating calibration quality at different T values, input encoding schemes, or layer-level error accumulation rate.

- **At T=1, the "SNN" has no temporal spike dynamics and is definitionally a recalibrated quantized model.** Table 2 shows "Conversion W6A6, T=1" matches PrefixQuant exactly (LLaMA-2-7B avg. acc 68.70 vs. 68.70), as expected because a single time step with IS dynamics collapses to the quantization function. "Ours T=1" shows minor improvement (68.79) from calibration, but this is threshold adjustment on the quantized model—not a spiking neural network in any meaningful sense. The paper never acknowledges this explicitly. Since T=1 is the method's best operating point and T>1 degrades performance monotonically, the paper's strongest result is not actually an SNN with temporal dynamics.

### Minor

- **Missing direct comparison with SpikeZIP (You et al., 2024)**, which is cited in the introduction as "the dominant approach" in spiking LLM conversion and is used for its spiking-compatible operations (Section 3.2.3). Including SpikeZIP as an experimental baseline would allow readers to quantify the contribution relative to the closest prior work. This is not a fatal flaw—the two methods differ in scope and architecture—but the absence makes it harder to assess progress in the specific sub-field of spiking language models.

- **Theorem 3's Lipschitz product $\prod_{\tau=k+1}^{K} \rho^\tau$ is potentially vacuous for 32-layer LLaMA models.** For linear layers without spectral normalization, individual $\rho^k$ values can exceed 1, making the K-term product astronomically large. The paper does not report whether these constants are bounded in practice, nor does it empirically validate the bound. As written, Theorem 3 motivates layer-wise calibration conceptually but does not provide a quantitatively useful bound.

### Trivial

- Table 1's claim that the proposed IS neuron achieves "Low" latency vs. "High" for conventional IF is framed as a property of the neuron type rather than the number of time steps, which drives actual inference latency. This framing is slightly misleading.

---

## Nice-to-Haves

- A theoretical or empirical SOP-vs-MAC analysis, even using published conversion factors from neuromorphic hardware literature, would directly support the energy efficiency claim without requiring actual hardware deployment.
- An ablation diagnosing the T-degradation mechanism (e.g., comparing calibration at T=4 and evaluating at T=4 vs. calibrating at T=2 and evaluating at T=4) would clarify whether the degradation is intrinsic to the IS neuron design at higher T or an artifact of calibrating at a mismatched T.
- An explicit acknowledgment that T=1 is effectively a reparametrized quantized model (not a temporally dynamic SNN), focusing the performance comparison claims on T≥2 settings.
- The calibration procedure's data source and number of calibration samples are not specified in the main text. Table 3 shows robustness to group size, but calibration data details affect reproducibility and the validity of comparisons.

---

## Removed Points

*These points are flagged for removal; treat with caution.*

- **Figure 3 confusion about negative MSE values (harsh critic):** The y-axis of the right axis (ranging from −8 to 2) in the figure description appears confusing, but this is a PDF-parsing artifact. The text itself correctly says the difference between the two curves measures unevenness error, and this is consistent with the paper's definition (Definition 1). Not a genuine weakness.

- **Abstract claims "comparable to SOTA" are misleading (harsh critic):** The paper says "comparable to state-of-the-art quantization techniques" — while at T=2, LLaMA-2-7B is 1 point below PrefixQuant (67.65 vs. 68.70), which is in range for "comparable" by standard NLP convention (and better than DuQuant at 62.25). This is not a misrepresentation.

- **Remark 1 hiding the approximation**: The harsh critic implies Remark 1 is problematic, but the paper explicitly and honestly states "the exact equivalence between the IS neuron outputs and the quantization function may not be perfectly achieved in practice" — this is the authors being forthright, not hiding a flaw. Removed.

- **Comparison unfairness with PrefixQuant / DuQuant**: The harsh critic notes that DuQuant W6A6 achieves lower PPL (5.53) than the SNN's T=2 (7.39). However, DuQuant uses dynamic quantization (per-token runtime scaling), so its W6A6 setup has more computational overhead than the static W6A6 used in this paper. This is not an unfair comparison in either direction.

- **SNN latency vs. QANN latency per T steps**: Strength Finder claimed the method "achieves low latency." This is generic and depends on hardware. Removed from strengths — the paper does not measure inference latency.

- **Strength about "brain-inspired efficiency"**: This is a motivation/aspiration, not a demonstrated strength. Removed from strengths.

---

## Novel Insights

The calibration result in Table 4 reveals an unexpected inversion: tuning 0.107K neuron parameters (thresholds and membrane potentials) outperforms fine-tuning 202M weight parameters for SNN conversion quality. This suggests that the source of conversion error in this regime is not weight misspecification but neuron-level temporal dynamics that weight fine-tuning cannot address, while threshold/potential adjustment can. This is a substantive empirical insight beyond what the paper's theory explicitly predicts, and it supports the paper's framing that calibrating the "right" parameters matters more than the total parameter count.

---

## Suggestions

1. **Add an SOP/MAC comparison** for at least one inference setting (e.g., T=2 on LLaMA-2-7B). Published SOP-to-energy ratios from neuromorphic hardware are available; even a theoretical estimate would anchor the energy efficiency claim.

2. **Run an ablation diagnosing T-degradation**: Calibrate at T=2 and evaluate at T=2; calibrate at T=4 and evaluate at T=4; also calibrate at T=2 and evaluate at T=4. This 2×2 table would reveal whether calibration is T-specific or generalizes.

3. **Explicitly discuss T=1**: State clearly that T=1 replicates quantized inference (no temporal SNN dynamics) and frame the T=2 calibrated result as the method's minimal meaningful SNN configuration.

4. **Add SpikeZIP or similar spiking LLM methods** to Table 2 to enable direct comparison in the spiking-language-model sub-field.

---

## Calibration Anchors

| Paper | Path | Avg Human Score | Round | Comparison |
|---|---|---|---|---|
| Automated Parameter Extraction (LLM+SNN) | j0sq9r3HFv.md | 2.50 | 1 | Off-topic; not comparable |
| EfficientQAT (QAT for LLMs) | 6Mdvq0bPyG.md | 3.00 | 1 | Similar quantization-efficiency setting but much less methodological depth |
| LLM Compression with Convex Opt | 0T8vCKa7yu.md | 3.00 | 1 | Different method, similar domain |
| SpikeZIP (ANN-to-SNN for LLMs) | u438df0Uce.md | 3.60 | 1+2 | Most topically similar; paper under review is stronger in novelty, scale, and theoretical rigor |
| When SNN meets ANN (Error-Free Conversion) | GTzP2GC7NR.md | 5.75 | 1 | Similar SNN conversion method; paper under review shares energy-measurement gap but is stronger in scale (LLM vs. CNN) |
| QAC (Mixed-Timestep SNN) | D4sQzdMvcG.md | 5.75 | 1+2 | Same calibration approach for threshold/membrane; paper under review is weaker on the T-degradation issue |
| Temporal Misinformation (ANN-to-SNN conversion) | sgke1JuVlc.md | 5.00 | 2 | ANN-to-SNN large models; paper under review has cleaner theory but shared energy measurement gap |
| Bridge the Gap SNN-ANN (Image Restoration) | G3vceNrP4o.md | 4.00 | 2 | ANN-SNN distillation, weaker scope |
| OmniQuant (Calibrated LLM Quantization) | 8Wuvhh0LYW.md | 6.40 | 2 | Calibrated LLM quantization with stronger experimental completeness; paper under review is weaker on multiple axes |

**Round 1 bracket:** 4.0–6.0  
**Round 2 narrowing:** The closest anchors to the paper under review are the 5.75 SNN conversion papers (QAC, Error-Free SNN) and SpikeZIP (3.6). The paper is stronger than SpikeZIP on novelty and scale but has a more fundamental problem than the 5.75 papers: the method's best operating point (T=1) is not an SNN with temporal dynamics, and T>1 degrades performance without explanation. The energy measurement gap is shared across all SNN anchors. Against OmniQuant (6.4), which demonstrates a calibrated quantization approach with proper efficiency analysis, the paper under review is clearly weaker. I place the paper below the 5.75 SNN conversion papers—it sits around **4.5**, closer to the lower end of the bracket.

**Final Score: 4.5 | Reject**

---

## Score and Decision

The paper introduces a technically reasonable conversion framework and a genuinely elegant calibration result. However, it fails to substantiate its primary motivation (energy efficiency), its best operating point is not an SNN in any dynamic sense, and performance degrades monotonically with the number of time steps without a mechanistic explanation. These are not presentation issues — they are gaps between the paper's stated contribution and its actual evidence. Compared to peer-level ANN-to-SNN conversion papers (scored 5.75 at this venue) that at least demonstrate performance advantages on their stated domain, this paper's strongest result (T=1) is definitionally a recalibrated quantized model. Calibration with 0.107K parameters beating 202M-parameter weight fine-tuning is a genuinely interesting finding, but it is insufficient to carry the paper's larger claims.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>