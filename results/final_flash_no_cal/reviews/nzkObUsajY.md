## Summary

This paper proposes a dual ANN-to-SNN conversion framework for LLMs that eliminates the need for training a conversion-friendly ANN. The method starts from a statically quantized LLM (PrefixQuant), replaces the quantization functions with a multi-level Integer Spiking (IS) neuron, and applies a parameter-efficient layer-wise calibration that optimizes only thresholds and initial membrane potentials (0.107 K parameters per layer) to recover performance. The IS neuron is theoretically shown to approximate the symmetric quantization function under certain conditions, and an error decomposition analysis motivates the calibration. On LLaMA-2-7B and LLaMA-3-8B at T=2, the calibrated SNN recovers from severe degradation (59.99 % → 67.65 % and 48.83 % → 69.03 %, respectively) to within ∼1–2 points of the quantized baseline.

---

## Strengths

- **Removes the need for conversion-specific ANN training.** Unlike conventional ANN-to-SNN conversion pipelines that require retraining the source ANN with a conversion-friendly activation function (e.g., QCFS), this framework starts from an off-the-shelf quantized LLM. Table 1 and Figure 1 clearly contrast the two pipelines, and the method achieves strong results without any LLM-scale retraining.

- **Parameter-efficient calibration yields large error reduction.** Calibrating only 0.107 K thresholds and initial membrane potentials per layer recovers massive performance drops (e.g., LLaMA-2-7B T=2: uncalibrated 59.99 % → calibrated 67.65 % vs. quantized baseline 68.70 %). Table 4 shows that this outperforms full weight fine‑tuning (66.39 %) despite using 2 000 000× fewer learnable parameters. This is a concrete and practically significant result.

- **Rigorous theoretical grounding for the conversion.** Theorem 2 establishes conditions under which the IS neuron exactly reproduces the symmetric quantization function; Theorem 3 decomposes the total conversion error into clipping, quantization, and unevenness components and shows that layer-wise calibration reduces the overall bound. The analysis directly motivates the design of the neuron and the calibration objective.

- **Targeted diagnosis and mitigation of unevenness error.** Figure 3 empirically isolates unevenness error as the dominant source of conversion error in the SNN (the gap between ANN–SNN MSE and ANN–QANN MSE). The calibration explicitly targets this component, and the large performance gains confirm the diagnosis.

---

## Weaknesses

### Major

- **DuQuant baseline results are clearly erroneous.** In Table 2, the DuQuant accuracy numbers are **identical** across LLaMA-2-7B and LLaMA-3-8B (WinoGrande 67.88, HellaSwag 72.64, ArcC 40.53, ArcE 53.07, PIQA 77.15, Avg. 62.25 for both models). Different models cannot produce the same accuracy on five separate tasks; this is either a copy‑paste error or a flawed reproduction. The only difference is in perplexity (5.53 vs. 6.27). This error undermines the claim that the method *“achieves performance comparable to state-of-the-art quantization techniques”* and must be corrected. The main claims do not depend on the DuQuant comparison (the PrefixQuant baseline and the Conversion vs. Ours comparison are the critical ones), but this mistake still damages confidence in the evaluation.

- **No energy efficiency analysis despite it being a central motivation.** The abstract, introduction, and contributions repeatedly frame the work as a step toward low‑power edge deployment (“brain‑inspired efficiency and low power consumption,” “potentially reduces the energy consumption”). Yet the experiments contain only accuracy and perplexity — no estimated energy from spike counts, no MAC vs. AC operation analysis, no comparison of the SNN’s energy footprint against the quantized ANN it is built on. The IS neuron can emit up to L spikes per time step (Eq. 9), which could increase energy relative to a single-spike IF neuron; this too is unexamined. Without even a theoretical energy estimate, the paper’s central promise is unsubstantiated. This is not a fatal flaw (the conversion method itself stands on its own), but it is a significant gap between what the paper claims and what it demonstrates.

- **Performance degrades as time steps increase, limiting the spiking regime.** Table 2 shows that accuracy consistently drops with larger T (e.g., LLaMA-2-7B: 68.79 at T=1 → 67.65 at T=2 → 67.04 at T=4 → 66.03 at T=8). The paper acknowledges this and attributes it to growing unevenness error, but the calibration only partially mitigates the trend. In standard ANN-to-SNN conversion, larger T improves fidelity to the ANN; here the opposite occurs. This means the method’s best results are at T=1 (a one‑step spiking model that lacks temporal spike dynamics), and at T>1 performance is strictly worse. The paper discusses this honestly, but the practical value of a “spiking” LLM that degrades with more time steps needs a deeper explanation and ideally a mitigation strategy beyond calibration alone.

### Minor

- **The IS neuron’s multi-spike behavior and its energy implications are unaddressed.** The neuron can fire up to L spikes per time step (Eq. 9). Most neuromorphic hardware is optimized for single-spike-per-neuron-per-timestep operation. The paper provides no spike‑count statistics or discussion of whether multi-spike firing is hardware-friendly or energy-efficient. This matters because the low-power argument for SNNs depends on sparse spike activity.

- **The approximation error from the inexact condition** *LT = 2^n − 1* **is not quantified.** Remark 1 correctly notes that exact equivalence between the IS neuron and the quantization function rarely holds for T ≠ 1, and describes an approximation using ⌈·⌉. However, the magnitude of this approximation error and its impact on conversion accuracy are not isolated or measured, weakening the theoretical guarantee.

- **Assumption 1 (Lipschitz-like layer-wise error propagation) has technical limitations for quantized functions.** Piecewise-constant quantization functions are not Lipschitz at discontinuities. The paper calls this a “Lipschitz-like condition” and cites prior work with the same assumption, which is acceptable practice, but the limitation is worth noting — the error bound in Theorem 3 is therefore a plausible heuristic rather than a strict mathematical guarantee.

### Trivial

None.

---

## Nice-to-Haves

- Provide even a coarse theoretical energy estimate (e.g., average spike count per layer × dynamic energy per spike, or ratio of AC-like operations to MACs) to substantiate the low-power motivation.
- Compare with a standard IF-neuron-based conversion on a smaller LLM (e.g., 1B scale) to isolate the benefit of the IS neuron design.
- Ablate the calibration data budget (how few samples suffice?) — this is practically important for edge deployment.
- Test on additional commonsense reasoning benchmarks beyond the five used.
- Investigate whether the T-degradation can be reduced by more sophisticated calibration strategies (e.g., per-neuron rather than per-layer thresholds, or input-adaptive initial potentials).

---

## Removed Points

*These points were flagged by reviewers but removed or demoted after verification against the paper.*

- **Calibration procedure not described (iterations, data, optimizer).** The paper states that *“Additional implementation details are provided in the Appendix.”* Per the parsing rule that appendices are stripped by the OCR pipeline but exist in the original submission, this criticism is removed. The main paper appropriately outlines the calibration objective (Sec. 3.4) and defers full implementation specifics to the appendix.
- **Duplicate strengths from Strength Finder.** The claim of *“comprehensive experimental validation”* was removed as generic/superficial. The remaining strengths were verified against specific evidence in the paper.
- **The Lipschitz assumption criticism** was demoted to Minor because the paper already frames it as a *“Lipschitz-like condition”* and cites prior work using the same assumption — it is a known limitation in the field, not an oversight.

---

## Novel Insights

The key insight that emerges from the reviews is that the paper inverts the standard ANN-to-SNN conversion pipeline: instead of training a conversion-friendly ANN and then converting, it starts from a *quantized* ANN and designs a spiking neuron (IS) whose multi-level threshold structure is algebraically matched to the quantization function. This reframes the conversion problem as a quantization‑to‑spiking mapping rather than a ReLU‑to‑firing‑rate mapping, which is why it can avoid retraining. The corollary — that this mapping becomes approximate when the product *LT* does not exactly equal *2ⁿ−1*, causing degradation at larger time steps — is a genuine trade-off that other conversion works have not had to face, because conventional methods use T=N and exact equality by construction. This trade-off and the paper’s partial mitigation via calibration constitute the most novel scientific content of the work.

---

## Suggestions

1. **Fix the DuQuant baseline.** The identical accuracy numbers across LLaMA-2-7B and LLaMA-3-8B must be corrected. Either reproduce DuQuant properly on both models or cite published numbers from the original DuQuant paper using the same evaluation harness.
2. **Add a theoretical energy analysis.** Estimate the number of synaptic operations (spike counts × fan-out) per inference for the SNN and compare against the quantized ANN. This does not require hardware measurements and can be done from existing simulation statistics.
3. **Investigate the T-degradation mechanism more deeply.** Provide spike‑distribution visualizations across layers at different T values, and analyze whether the unevenness error can be further reduced by per-neuron threshold tuning or a more expressive initial membrane potential parameterization.
4. **Soft‑pedal the energy claim** in the current version. Change *“reduces energy consumption”* to *“may enable energy benefits under sparse spike activity, which is left for future work.”*

---

## Score and Decision

**Originality** — Above average. The dual conversion framing (quantization → spiking rather than ReLU → spiking) is novel and well-motivated.  
**Importance** — Above average. Spiking LLMs are a timely problem and avoiding retraining is practically relevant.  
**Support for claims** — Moderate. The core conversion-and-calibration claim is well-supported; the energy claim is unsupported; the SOTA comparison is partially undermined by the DuQuant error.  
**Soundness** — Moderate. The theoretical analysis is sound, but the experimental evaluation has a clear error (DuQuant baseline) and a significant gap (no energy evidence).  
**Clarity** — Good. The paper is clearly written and well-structured.  
**Value to community** — Moderate to good. The IS neuron design and the calibration approach are reusable components.

The paper makes a genuine contribution (a training-free ANN-to-SNN conversion for LLMs with a theory-grounded calibration that recovers most of the performance), but the evaluation has two verifiable problems: the DuQuant baseline is clearly wrong (identical numbers across two different models), and the core energy-efficiency motivation is entirely unvalidated.  The T-degradation, while honestly discussed, further limits the practical regime of the method.  These issues are fixable, but in the current form they prevent acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>