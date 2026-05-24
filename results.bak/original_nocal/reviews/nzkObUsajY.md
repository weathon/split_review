## Summary

The paper proposes a dual ANN-to-SNN conversion framework for LLMs. Instead of the conventional approach — which requires training a conversion-friendly ANN before converting to SNN — it starts from a statically quantized LLM (training-free) and replaces the quantization function with a multi-hierarchical-threshold Integer Spiking (IS) neuron. A parameter-efficient layer-wise calibration (tuning only thresholds and initial membrane potentials) then reduces conversion error, particularly the "unevenness error" arising from temporal spike dynamics. Experiments on LLaMA-2-7B and LLaMA-3-8B under W6A6 quantization show the converted SNN achieves average zero-shot accuracy competitive with the quantized baseline (e.g., 67.65 vs. 68.70 on LLaMA-2-7B, T=2) using orders of magnitude fewer learnable parameters than weight fine-tuning.

## Strengths

1. **Novel and practical conversion pipeline.** The idea of repurposing existing quantized LLMs (rather than training a conversion-specific ANN) is both novel and cost-effective. Table 1 clearly distinguishes the proposed approach from conventional methods that require tailored ANN training and high latency. This directly addresses a real bottleneck for scaling SNN conversion to LLMs.

2. **Rigorous theoretical analysis of the IS neuron.** Theorems 1 and 2 (Section 3.2.2) formally characterize the conditions under which the multi-hierarchical-threshold IS neuron can emulate the symmetric quantization function. Theorem 3 provides a Lipschitz-style bound on the end-to-end conversion error, explicitly decomposing it into clipping, quantization, and unevenness errors. Definition 1 formalizes unevenness error — a contribution that is more precise than the heuristic treatments common in prior conversion work.

3. **Extreme parameter efficiency of the calibration method.** Table 4 shows that tuning only 0.107K parameters per layer (thresholds and initial membrane potentials) achieves higher average accuracy (67.65) on LLaMA-2-7B than full weight fine-tuning with 202.375M parameters (66.39). This dramatic efficiency is the paper's strongest experimental result and directly validates the claim that the QANN weights are already near-optimal.

4. **Empirical identification of unevenness error as the dominant degradation source.** Figure 3 decomposes the conversion error and shows that the gap between ANN-vs-QANN and ANN-vs-SNN errors is large and grows with depth, supporting the paper's focus on unevenness error as the primary target for calibration.

5. **Robustness to group size / parameter budget.** Table 3 demonstrates stable performance across a range of activation group sizes (Avg. Acc. 65.46–67.65), indicating the framework adapts well to different deployment constraints.

## Weaknesses

### Fatal
None.

### Major

1. **Missing energy or latency analysis to support the edge-deployment motivation.** The abstract and introduction repeatedly motivate the work through SNNs' potential for energy-efficient edge deployment. However, the experiments contain no energy estimation (synaptic operations, dynamic energy, or hardware measurements) and no latency comparison against the quantized ANN baseline. The paper compares only accuracy and perplexity against quantization methods (PrefixQuant, DuQuant). Since the quantized ANN already reduces model size and compute, the paper does not demonstrate that the spiking version provides any *additional* practical advantage on the metrics that matter for edge deployment. While the paper hedges with "potentially reduces energy consumption" in the contribution list, the motivational framing creates an expectation the evaluation does not meet. Adding an energy model (e.g., synaptic operation counts or a standard SNN energy estimation framework) would substantiate the motivation and is standard practice in SNN conversion papers.

2. **No experimental comparison to other ANN-to-SNN conversion methods for LLMs.** The paper cites SpikeZIP (You et al., 2024) as a prior conversion method but provides no comparison to it or any other SNN conversion baseline. While the proposed approach is architecturally different (starting from quantized models rather than from a conversion-friendly ANN), a comparison would help situate the contribution within the SNN literature and clarify trade-offs. The current evaluation only compares against quantization baselines, which are not SNN methods.

### Minor

3. **Theoretical idealization vs. practical approximation gap for the IS neuron.** Theorems 1 and 2 require conditions (input currents falling into specific intervals, exact equality \(LT = 2^n - 1\)) that Remark 1 itself acknowledges are "rarely satisfied" in practice. The approximation error introduced by these relaxations is not quantified empirically. While the calibration step mitigates the practical gap, the paper would benefit from measuring how much deviation from the ideal conditions affects conversion quality (e.g., discrepancy between IS neuron output and the quantization target across layers).

4. **Figure 3 presentation issues.** The dual-axis plot is described as showing MSE, but the right y-axis (ANN vs. SNN series) ranges from -8 to 2, which is impossible if the plotted quantity is MSE (always non-negative). Whether this is a plotting artifact or the right axis reflects a different scale/metric, the figure needs clarification. The claim that "unevenness error plays a main character" would be better supported with a clearer visualization.

5. **Perplexity gap vs. weight fine-tuning.** In Table 4, the calibration method achieves better average accuracy than weight fine-tuning (67.65 vs. 66.39) but worse perplexity (7.39 vs. 6.37). The paper notes this comparison in passing but does not discuss the divergence between accuracy and perplexity as evaluation metrics — perplexity is often more sensitive for language modeling quality, and this gap warrants discussion.

### Trivial
None.

## Nice-to-Haves

- An ablation study separating the effect of tuning thresholds vs. tuning initial membrane potentials, to confirm both are needed.
- Visualization of actual spike trains from a few layers to verify the IS neuron produces meaningful multi-level spikes and to show how calibration changes firing behavior.
- Analysis of the energy-accuracy trade-off as a function of time steps T, since accuracy degrades at larger T while energy typically increases.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The abstract framing is misleading"** — The paper states the spiking model is derived from a quantized model and achieves "comparable performance." This is technically accurate and not misleading.
- **"Substantial components may remain analog"** — The paper explicitly adopts spiking-compatible operations from prior work (You et al., 2024) for nonlinear operations and references the appendix for details. The concern is speculative rather than verifiable from the paper as written.
- **"Calibration optimization details missing"** — The appendix (stripped by the parser) likely contains these details. The main text states the objective; implementation specifics are standard in the appendix.
- **"Lipschitz constants never computed"** — This is common for qualitative theoretical bounds that motivate a design direction; Theorem 3 is used to motivate layer-wise calibration, not to provide quantitative predictions.
- **"Catastrophic degradation without calibration"** — The paper itself discusses this and uses it to motivate the calibration method. This is an observation, not a weakness.
- **Generic framing concerns** about the paper's scope or the importance of the problem — these are not specific to the paper's content.

## Novel Insights

None beyond the paper's own contributions. The three-reviewer synthesis does not surface an observation about the paper that the paper itself does not already articulate or imply.

## Suggestions

1. **Add energy estimation.** Estimate energy consumption using a standard SNN energy model (e.g., synaptic operation counts × per-operation energy, or follow the methodology common in ANN-to-SNN conversion papers). Compare against the quantized ANN baseline to demonstrate the practical advantage of the spiking model.
2. **Add a comparison to at least one SNN conversion baseline** (e.g., SpikeZIP or a direct IF-neuron conversion from the quantized model) to position the work within the SNN literature.
3. **Fix Figure 3.** Clarify what the right axis actually plots — if it is not MSE (since negative values appear), rename it or rescale appropriately.
4. **Quantify the IS neuron approximation error** empirically by measuring the discrepancy between the IS neuron output and the quantization function across layers for a representative model.

## Score and Decision

The paper presents a novel, well-motivated conversion framework with rigorous theoretical grounding and compelling experimental evidence of parameter-efficient calibration. The primary weakness is the absence of energy analysis to substantiate the edge-deployment motivation, and the lack of comparison to other SNN conversion methods. These are significant gaps but not fatal — the core technical contribution (conversion from quantized LLMs + calibration) is validated and practically useful. With the suggested additions, the paper would be substantially stronger.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>