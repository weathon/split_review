## Summary

This paper proposes a "dual ANN-to-SNN conversion" framework for deploying Large Language Models as Spiking Neural Networks (SNNs) on edge devices. Instead of training a dedicated conversion-friendly ANN (the conventional pipeline), the authors start from a pre-trained, statically quantized LLM (via PrefixQuant) and introduce an Integer Spiking (IS) neuron with multi-hierarchical thresholds that directly emulates the quantization function. A parameter-efficient layer-wise calibration — optimizing only neuronal thresholds and initial membrane potentials — is then applied to suppress unevenness error, the dominant degradation source. Theoretical bounds on conversion error are derived and validated empirically on LLaMA-2-7B and LLaMA-3-8B across several zero-shot reasoning benchmarks.

---

## Strengths

- **Genuinely novel pipeline.** The insight of treating a quantized LLM as the intermediate ANN for SNN conversion (rather than training a custom ANN from scratch) is elegant and practical. It eliminates the most expensive step of conventional ANN-to-SNN methods while leveraging the best available quantization tooling (PrefixQuant).

- **Theoretically grounded.** Theorems 1–3 connect IS neuron behavior to the quantization function and establish a layer-wise Lipschitz-propagated upper bound on conversion error. The analysis motivates the calibration target directly and is consistent with the empirical finding (Figure 3) that unevenness error dominates.

- **Dramatic parameter efficiency of calibration.** Table 4 shows that tuning only 0.107K parameters per layer (thresholds + initial membrane potentials) matches or exceeds weight calibration using 202M parameters per layer on average accuracy. This is a striking result that makes the approach practically attractive.

- **Calibration delivers substantial gains.** At T=2 for LLaMA-2-7B, calibration raises average zero-shot accuracy from 59.99 to 67.65 (versus 68.70 for PrefixQuant) — nearly recovering quantized-ANN performance. Without calibration the SNN is unusable; with it, the gap is small.

---

## Weaknesses

### Fatal
None. The core method is technically sound and the experiments support the main claims.

### Major

1. **Energy efficiency is never measured.** The entire motivation rests on SNNs being energy-efficient for edge deployment, but no energy, latency, or throughput numbers appear anywhere. For T=1 the model is operationally equivalent to a quantized ANN; for T>1, every forward pass involves T serial spike-propagation steps. Without an energy estimate (even theoretical, e.g., synaptic operation counts), the central premise — that this approach reduces LLM energy consumption — is completely unsubstantiated. A reader cannot tell whether T=2 on neuromorphic hardware is cheaper than T=1 dense inference.

2. **The T>1 regime degrades monotonically and the motivation is circular.** Performance at T=4 (67.04 avg acc) and T=8 (66.03) for LLaMA-2-7B is strictly worse than T=1 (68.79) and also worse than T=2 (67.65). If increasing T increases both energy cost (more timesteps) and task degradation (more unevenness error), there is no case where T>1 is beneficial under the paper's own metrics. The paper attributes degradation to growing unevenness error with larger T but does not explain when one would ever prefer T>1. A deployment scenario where T>1 is advantageous (e.g., sparse spike regime on neuromorphic hardware) must be justified.

3. **No comparison with spiking LLM baselines.** SpikeGPT, SpikeBERT, and SpikeZIP are cited in the introduction as prior spiking LLM work, yet none appear in the experimental tables. Comparing only against ANN quantization methods (PrefixQuant, DuQuant) characterizes the accuracy gap but does not establish where the proposed method sits relative to prior spiking approaches.

### Minor

1. **DuQuant results are anomalous and unexplained.** DuQuant shows 62.25 avg acc and 5.53 PPL on LLaMA-2-7B — a large accuracy gap from PrefixQuant (68.70) despite its PPL being nearly as good as baseline (5.53 vs 5.47). The same DuQuant numbers (67.88, 72.64, 40.53, 53.07, 77.15) appear identically for both LLaMA-2-7B and LLaMA-3-8B, which is suspicious and should be explained.

2. **Conditions of Theorem 2 are non-trivial.** The theorem requires that every per-timestep input current falls into a specific set of intervals — a condition that can fail in practice (as Remark 1 acknowledges). The paper does not quantify how often this condition is violated or what error it introduces when it fails, making it unclear what the theorems actually guarantee for real inputs.

3. **Group-size ablation (Table 3) is counterintuitive.** The recommended setting (group\_size = -1, 0.107K params) outperforms all finer-grained groupings despite having fewer parameters. The pattern does not follow a monotone trend (e.g., group\_size=16 gives 67.03 acc / PPL 6.89, which is worse than group\_size=256 on accuracy but better on PPL). This warrants explanation.

### Trivial

- Table 2 is missing the "Ours, W6A6, T=8" row for LLaMA-2-7B (only the LLaMA-3-8B Baseline row appears in that position). The table layout suggests a row may have been accidentally merged.

---

## Nice-to-Haves

- A comparison of synaptic operation (SOP) counts for SNN vs. MAC counts for QANN would give readers a concrete efficiency picture even without neuromorphic hardware.
- Experiments at W4A4 would test whether the IS neuron design generalizes to lower bitwidths, which are more practically relevant for extreme edge deployment.

---

## Novel Insights

The observation that a quantized LLM already encodes discrete, integer-valued activations that can be *re-interpreted* as multi-timestep spike accumulations — rather than treating the quantization function as an approximation target to be learned — is a genuinely fresh angle. It inverts the conventional SNN pipeline: instead of training the ANN toward the neuron's behavior, the neuron is designed to match the already-quantized ANN's behavior. The finding that calibrating only two scalar parameters per neuron group (threshold and initial potential) suffices to nearly close the quantization-to-SNN gap is surprising and suggests that the principal source of unevenness error is a global bias rather than weight mismatch. This has potential implications for calibration design in other ANN-to-SNN settings beyond LLMs.

---

## Suggestions

- Add even a rough theoretical estimate of energy savings (SOP count) relative to quantized dense-matrix inference for T=2,4 to substantiate the edge-deployment motivation.
- Clearly delineate a scenario where T>1 is the preferred operating point (e.g., on neuromorphic hardware where binary spikes give multiplicative energy savings), or reframe the contribution to focus on T=1 as the primary practical setting.
- Include SpikeZIP or another spiking-LLM baseline in the comparison table to situate the work within the SNN community.
- Investigate and explain the DuQuant anomaly (identical numbers across two different model families).

---

## Score and Decision

The paper introduces a genuine methodological innovation (training-free LLM-to-SNN conversion via a quantized ANN intermediate) supported by sound theory and strong calibration efficiency. The calibration results (0.107K params matching 202M-param weight tuning) are compelling. However, the motivation for multiple timesteps is undermined by monotonically degrading performance, and no energy measurements are provided despite energy efficiency being the stated raison d'être of the entire framework. The comparison baseline is incomplete (no spiking LLM competitors). These are meaningful gaps for a paper whose central claim is efficient SNN deployment of LLMs.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>