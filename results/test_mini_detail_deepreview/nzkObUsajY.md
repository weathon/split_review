Now I have a solid grounding from the calibration. Let me synthesize the final review.

## Summary

This paper proposes a "dual" ANN-to-SNN conversion framework for LLMs. Instead of the conventional route — training a conversion-friendly ANN and converting it to an SNN — the authors start from an off-the-shelf quantized LLM (PrefixQuant) and introduce an Integer Spiking (IS) neuron with multi-hierarchical thresholds that approximates the symmetric quantization function. A parameter-efficient layer-wise calibration (adjusting only thresholds and initial membrane potentials, ~0.107K parameters per layer) is then applied to reduce conversion errors, particularly the "unevenness error" caused by temporal spike dynamics. Experiments on LLaMA-2-7B and LLaMA-3-8B at W6A6 show that calibration significantly improves over the uncalibrated SNN, approaching the quantized ANN baseline at low time steps (T=1,2).

## Strengths

1. **Eliminates the need for a conversion-specialized ANN.** The pipeline starts from a training-free quantized LLM (PrefixQuant), avoiding the prohibitive cost of retraining LLMs with conversion-friendly activation functions like QCFS. This is a practical contribution for scaling ANN-to-SNN conversion to billion-parameter models. (Section 3.2, Table 1)

2. **Theoretical guarantee of equivalence between the IS neuron and the symmetric quantization function.** Theorem 2 establishes explicit conditions (on thresholds L, time steps T, bias α) under which the summed IS output exactly equals the quantization output. Remark 1 honestly acknowledges when exact equivalence fails due to the integer constraint, a level of theoretical rigor that goes beyond heuristic ReLU-to-IF approximations. (Section 3.2.2)

3. **Parameter-efficient calibration yields large gains.** Adjusting only 0.107K parameters per layer improves average accuracy from 59.99 to 67.65 on LLaMA-2-7B at T=2, outperforming full weight fine-tuning (202.375M parameters, 66.39). This confirms the core claim that the unevenness error is dominant and can be corrected with minimal overhead. (Table 4)

4. **Quantitative isolation of unevenness error as the dominant degradation source.** Figure 3 plots layer-wise MSE for ANN-vs-QANN (clipping+quantization error) and ANN-vs-SNN (all errors). The large gap validates the paper's error analysis and motivates the calibration design. (Section 3.3, Figure 3)

## Weaknesses

### Major

1. **No energy consumption analysis or synaptic operation estimates, despite claiming energy benefits.** The abstract and conclusion state that the SNN "potentially reduces the energy consumption of LLMs," and energy efficiency for edge deployment is the paper's primary motivation. Yet the paper provides zero energy estimates, no synaptic operation counts, and no theoretical or simulated energy comparison to the QANN baseline. Every comparable spiking LLM paper (e.g., SpikeLLM, Spatio-Temporal Approximation for Transformers) includes such analysis. For an SNN paper whose core value proposition is energy efficiency, this is a fundamental omission. The reader has no basis to judge whether the accuracy degradation at T>1 is an acceptable trade-off.

2. **Missing comparison to SpikeZIP, a directly competing ANN-to-SNN conversion method for transformers.** The paper cites SpikeZIP (You et al., 2024) in the related work and notes that it uses a quantization-based approach. Since SpikeZIP also targets conversion without training a tailored ANN and addresses similar nonlinear operations in transformers, it is a direct competitor. Without this comparison, the claimed advantage of the proposed framework is unverifiable.

3. **The structural T-accuracy paradox is discussed but not resolved.** As the paper acknowledges in Section 4.2, performance degrades monotonically as T increases from 2 to 8 (e.g., LLaMA-2-7B: avg acc 67.65 at T=2 → 66.03 at T=8). The best accuracy is at T=1, which is effectively the quantized ANN. The paper attributes this to growing unevenness error (Remark 1), and this is a genuine structural limitation of the approach. The IS neuron's approximation error increases with T because LT must be an integer and L = ceil((2^n−1)/T) creates a larger mismatch. This means the SNN cannot benefit from longer temporal integration — the opposite of conventional conversion, where more timesteps improve approximation. The paper should explicitly discuss whether T>1 provides any practical advantage over the QANN at T=1.

### Minor

4. **Limited experimental scope: only W6A6 precision, only 7B/8B models.** All experiments use 6-bit weights and 6-bit activations. Lower bit-widths (e.g., W4A4) common in edge deployment are not tested. Only the two smallest LLaMA models are shown; results on LLaMA-13B or 70B would significantly strengthen the scalability claims. The calibration is lightweight, so larger model results should be feasible.

5. **Calibration setup details are insufficient for reproducibility.** The paper (Section 3.4) defines the calibration objective as minimizing ||∑_t ŷ^k(t) – y^k|| per layer, but does not specify how many calibration samples are used, what optimizer is used (SGD? gradient-free?), the learning rate, or the number of optimization steps. This is critical for independent verification.

6. **The error decomposition in Figure 3 is imprecise.** The claim that unevenness error is "the dominant source of degradation" is based on comparing ANN-vs-QANN MSE (which includes clipping + quantization errors) with ANN-vs-SNN MSE (all errors). The difference is attributed to unevenness error. However, this decomposition assumes that clipping and quantization errors are the same in both cases, which they are not — the QANN uses the symmetric quantization function (Eq. 7) while the IS neuron approximates it (Eq. 8-10). The gap in Figure 3 thus conflates unevenness error with the IS neuron's approximation error from the integer constraint (Remark 1).

### Trivial

7. The term "training-free" in the abstract and contributions is used for the conversion itself, but the calibration step involves optimization over calibration data. The paper should clarify this distinction upfront (it currently does so only implicitly in Figure 1's caption).

## Nice-to-Haves

- Including a comparison with the quantized ANN baseline (PrefixQuant) as a "T=0" baseline in Table 2, to clarify whether the SNN at any T > 0 provides an advantage over direct use of the QANN.
- Ablation that isolates the approximation error from the integer constraint (Remark 1) by simulating the IS neuron with exact LT = 2^n−1 on synthetic data.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The IS neuron and calibration are not novel"** — The paper explicitly cites prior work (Sun et al., 2022; Wang & Zhang, 2023; Li & Zeng, 2022; Hao et al., 2024) for the M-HT/IS neuron. The novelty is in applying it to LLM-scale quantized conversion and identifying unevenness error as dominant. The harsh critic's claim that the calibration is "a straightforward application of existing calibration ideas" is an opinion, not a verified weakness. Every method builds on prior work, and the paper is transparent about its antecedents.

- **"Accuracy paradoxically decreases with more time steps … The paper does not discuss this trade-off"** — The paper explicitly discusses this in Section 4.2: "Moreover, as time-step T increases, the performance degrades correspondingly. We attribute this phenomenon to the growing unevenness error introduced by the larger time-step." The reviewer missed this discussion. However, the underlying structural limitation is real, so I have retained it as Major weakness #3 (recast as a technical limitation that is acknowledged but not resolved).

- **"The Lipschitz constants ρ^k are never computed or estimated, so the bound is not actionable"** — This is standard in ANN-to-SNN analysis; Bu et al. (2022) and others use similar non-constructive bounds. The bound's purpose is to show that layer-wise error propagation is controlled (Remark 3), not to compute exact values. This is a standard theoretical framing, not a weakness.

- **"The paper does not prove that the condition in Theorem 1 is satisfied in practice"** — The condition is that input currents fall into specific intervals. Calibration is designed to make this hold approximately, which is standard for conversion methods that assume input distributions.

- **Strawman criticisms about missing appendix content, formatting, or reproducibility details that the parser likely stripped** (e.g., "spiking-compatible operations not explained in main text," "no details about spike generation for LayerNorm/Softmax"). The appendix exists in the original submission; the parser strips it.

- **"Direct-training spiking LLM (e.g., SpikeGPT) should be compared"** — The paper's scope is ANN-to-SNN conversion, not direct training. Comparing to direct-training methods would be a different paradigm, and the paper is not claiming to outperform them.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add synaptic operation counts and energy estimates** for all T values tested, compared to the QANN baseline and FP16 baseline. Without this, the paper's central motivation remains unsubstantiated. Use the standard SNN energy estimation methodology (synaptic operations × per-synapse energy) and compare with the equivalent MAC-based energy for the quantized ANN.

2. **Include a comparison to SpikeZIP** as a directly competing ANN-to-SNN method for transformers. If there are differences in assumptions (e.g., SpikeZIP may require different bit-widths or neuron design), explain them and argue why your approach is preferable.

3. **Add results on at least one lower bit-width (W4A4) and one larger model (LLaMA-13B).** The calibration is lightweight and these experiments should be feasible.

4. **Provide the calibration setup details** (number of samples, optimizer, learning rate, steps) in the main text for reproducibility.

5. **Address the T-accuracy paradox more directly.** Show explicitly that the approximation error from Eq. (7) to Eq. (8) grows with T, and discuss whether T > 1 offers any practical benefit over the QANN. If the SNN's advantage over the QANN only emerges on neuromorphic hardware, state this clearly and provide the evidence needed to support it.

## Score and Decision

**Calibration anchor details (all rounds):**

*Round 1 — Bracketing:*
- Weak (<3.5): `j0sq9r3HFv.md` (2.50), `7DY2DFDT0T.md` (2.50), `f7aWmxgSN4.md` (3.00), `BBldjKEBlJ.md` (3.00). Irrelevant topics (neural parameter extraction, LLM sparsity, graph learning, neural activity forecasting). This paper is clearly far above these.
- Middle (3.5–7.5): `ZadnlOHsHv.md` — SpikeLLM (7.00, Accept). Closest competitor: spiking LLM with 7B–70B models, energy analysis, requires training. Our paper is weaker: no energy analysis, smaller scale, but has the advantage of being training-free.
`XrunSYwoLr.md` — Spatio-Temporal Approximation (7.00, Accept). Training-free SNN conversion for ViTs, includes energy analysis. Our paper tackles harder domain (LLMs) but lacks energy analysis.
`GTzP2GC7NR.md` — Error-Free Conversion (5.75, Reject). Requires training tailored ANNs with QCFS. Our paper's training-free approach is more practical, and the LLM domain is more challenging.
`6c4gv0E9sF.md` — SpikeBERT (6.33, Reject). Small-scale BERT spiking via KD, not LLM-scale. Our paper tackles larger models but lacks energy analysis that SpikeBERT includes.
- Strong (>7.5): `aWXnKanInf.md` (8.00), `I4e82CIDxv.md` (8.00), `tcsZt9ZNKD.md` (8.20), `TJo6aQb7mK.md` (7.60). These are on different topics (brain-like models, sparse autoencoders, scaling, ternary LMs). Not directly comparable.

*Round 2 — Narrowing:*
- (4.5–6.0): `D4sQzdMvcG.md` — QAC (5.75, Reject). Quantization-aware conversion for CNNs with membrane calibration. Our paper has a similar theoretical angle (quantization-to-SNN equivalence) but targets LLMs, which is harder. However, QAC has more complete experiments. Our paper is slightly stronger.
`GTzP2GC7NR.md` — Error-Free (5.75, Reject). Already discussed above.
`mJ4mgYjDru.md` — Discretized QIF (4.60, Reject). Not relevant (neuron model paper for CV).
`vlQ56aWJhl.md` — S-TLLR (5.00, Reject). Not relevant (STDP learning rule).
- (6.0–7.5): `ZadnlOHsHv.md`, `XrunSYwoLr.md`, `MiPyle6Jef.md` — QP-SNN (6.75, Accept, CV SNN quantization/pruning, not directly comparable), `6c4gv0E9sF.md`.

**Bracket after Round 1:** This paper sits between the rejected conversion methods at ~5.75 and the accepted spiking LLM work at ~7.00.

**Narrowing:** Compared to the accepted papers (SpikeLLM at 7.00, Spatio-Temporal Approx at 7.00), this paper has a novel and promising direction (dual conversion from quantized LLMs) but falls short in execution: no energy analysis, limited scale, and a structural T-accuracy paradox that undermines the SNN value proposition. Compared to the rejected papers at ~5.75 (QAC, Error-Free), it tackles a harder problem (LLMs) with a more practical approach (training-free), but its experimental support is thinner. The paper is meaningfully above the 4.5–5.0 range but clearly below the 7.0 accepted papers.

**Final score: 5.5.** The core idea has merit and the theoretical analysis is clean, but the missing energy analysis — which is essential for any SNN paper claiming energy benefits — combined with the unresolved T-accuracy structural limitation and narrow experimental scope, make the paper insufficient for acceptance in its current form. Major revision with the additions listed in Suggestions could raise it to the 6.5–7.0 range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>