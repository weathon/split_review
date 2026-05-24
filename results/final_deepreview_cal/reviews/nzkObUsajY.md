Now I have enough information to write the consolidated review. Let me finalize my assessment.

**Round 1 bracket:** 4.5–7.0 (between SpikeZIP at 3.60 and SpikeLLM at 7.00)

**Round 2 narrowing:** The paper is clearly stronger than the 5.75 anchor (Error-Free Conversion — CNN-only, requires training, rejected) and comparable to the 6.33 anchor (SpikeBERT — different approach, rejected). It's somewhat below the 7.00 anchors (SpikeLLM and Spatio-Temporal) due to the DuQuant copy-paste error and missing energy analysis.

**Final score: 6.0**, Decision: Reject (but borderline — strong rebuttal could flip).

---

## Summary

This paper proposes a training-free ANN-to-SNN conversion framework for LLMs that starts from a statically quantized LLM (PrefixQuant) and replaces the quantization function with a custom Integer Spiking (IS) neuron. A lightweight, parameter-efficient layer-wise calibration (tuning only thresholds and initial membrane potentials — 0.107K parameters per layer) corrects the dominant unevenness error. The method is evaluated on LLaMA-2-7B and LLaMA-3-8B across five zero-shot reasoning tasks and WikiText2 perplexity, demonstrating that calibration recovers most of the accuracy gap between the uncalibrated SNN and the quantized ANN at time steps T=2,4,8.

## Strengths

- **Truly training-free conversion pipeline**: By starting from a pre-quantized LLM (PrefixQuant W6A6) and designing an IS neuron that approximates the symmetric quantization function, the method eliminates the need to train a conversion-friendly ANN from scratch. At T=1, the converted SNN achieves identical accuracy to the quantized model (Table 2), confirming the neuron replacement is functionally sound.

- **Parameter-efficient calibration with strong empirical results**: The layer-wise calibration adjusts only thresholds and initial membrane potentials (0.107K parameters per layer) yet dramatically closes the accuracy gap. On LLaMA-2-7B at T=2, calibration raises average zero-shot accuracy from 59.99% to 67.65% (vs. 68.70% for the quantized baseline). Table 4 shows this tiny parameter budget performs on par with full weight-level calibration (202M parameters), demonstrating remarkable parameter efficiency.

- **Theoretical error decomposition that motivates and guides calibration**: Theorem 3 provides a layer-wise bound on total conversion error and the decomposition into clipping, quantization, and unevenness errors. Figure 3 empirically validates that unevenness error dominates, directly motivating the calibration design. The analysis is coherent and well-aligned with the experiments.

- **Robustness to calibration granularity**: Table 3 shows that varying the activation group size (and thus learnable parameter count from 0.107K to 23.399K per layer) maintains average accuracy within a narrow ~2% range, indicating the method does not require careful hyperparameter tuning.

## Weaknesses

### Fatal

None.

### Major

- **DuQuant baseline contains a copy-paste error that undermines experimental rigor**: Table 2 reports identical per-task scores (WinoGrande 67.88, HellaSwag 72.64, ArcC 40.53, ArcE 53.07, PIQA 77.15, Avg. 62.25) for DuQuant on both LLaMA-2-7B and LLaMA-3-8B. Two different models cannot realistically achieve identical scores across five diverse tasks. This is almost certainly a copy-paste mistake. While DuQuant is a secondary baseline (the primary baseline is PrefixQuant, whose numbers correctly differ between models), this error casts doubt on the care taken in experimental reporting and makes the DuQuant comparison unreliable.

- **No energy or efficiency metrics reported despite energy efficiency being a central motivation**: The paper repeatedly motivates the work by the need for energy-efficient edge deployment and asserts that SNNs offer "brain-inspired efficiency and low power consumption," yet the experiments report only accuracy and perplexity. No spike counts, synaptic operation counts, or energy estimates are provided. For a paper whose third listed contribution is that the method "potentially reduces the energy consumption of LLMs," the absence of any energy analysis makes it impossible to evaluate whether the spiking conversion actually delivers efficiency gains, or to weigh the accuracy drop against energy savings at different time steps.

### Minor

- **Theoretical presentation of the IS neuron equivalence could be tightened**: Theorem 1 states the IS neuron's total output as a clip function without an explicit floor operation, while the quantization function in Eq. (7) uses ⌊·⌋. The IS neuron's threshold-based firing (Eq. 9) inherently produces integer outputs, so the effective behavior does incorporate discretization, but the theorem statement as written conflates clipping with the discrete firing mechanism. Remark 1 helpfully acknowledges that exact equivalence rarely holds in practice, but a cleaner derivation distinguishing the discrete spike accumulation from the continuous clip would strengthen the theoretical foundation.

- **No comparison with prior spiking LLM or ANN-to-SNN conversion methods for LLMs**: The paper cites SpikeZIP, SpikeGPT, and related works but does not include any direct comparison, even using published numbers, on the same zero-shot tasks. While the authors may argue that prior methods use fundamentally different approaches (direct training or conversion-trained ANNs), situating the results against prior spiking LLMs would significantly strengthen the contribution.

### Trivial

- Figure 3 uses a dual-axis plot with log scale on one side and linear on the other, which obscures the relative magnitudes of the two error curves. A side-by-side bar chart or table would be clearer.

## Nice-to-Haves

- The calibration procedure details (learning rate, optimizer, number of iterations, exact loss function) are not specified in the main text. These may be in the appendix, but including key hyperparameters in the main paper would improve reproducibility.
- Discussion of limitations — e.g., performance degradation at higher T, reliance on PrefixQuant, applicability beyond LLaMA architectures — would strengthen the paper.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim that Theorem 1/2 "confuses rounding with clipping" and the equivalence is "not valid as presented"**: The IS neuron produces discrete (integer) outputs through its threshold-based firing mechanism in Eq. (9). The clip expression in Theorem 1 captures the bounded nature of the output, and the discretization is inherent in the spiking mechanism. Remark 1 appropriately acknowledges that exact equivalence is not perfectly achieved. This is a presentation issue, not a theoretical fatal flaw. DEMOTED to Minor.

- **Harsh Critic claim about suspicious PrefixQuant or conversion results**: The PrefixQuant numbers differ appropriately between models (e.g., LLaMA-2-7B: 68.70 vs. LLaMA-3-8B: 70.24), and the conversion/Ours numbers are all model-specific. Only DuQuant shows the copy-paste error. KEPT only the DuQuant issue as Major.

- **Harsh Critic claim about "no dynamic or static nature of DuQuant's activation quantization" being unspecified**: The paper states all experiments use W6A6 and that PrefixQuant is the static quantizer. DuQuant is described as using dynamic quantization in the related work section. This is sufficient context.

- **Strength Finder claim about "robustness to learnable parameter sizes"**: This is valid but the accuracy range is ~2%, not "narrow 1% range" as claimed. The actual range is 65.46–67.65 = 2.19%. Still robust, but corrected.

- **Strength Finder generic strengths about "important problem" and "interesting question"**: These are generic and not grounded in specific paper content. Dropped.

## Novel Insights

None beyond the paper's own contributions. The paper's core insight — that a pre-quantized LLM can be converted to a spiking version by replacing the quantization function with a multi-threshold spiking neuron and then calibrating only thresholds and initial membrane potentials — is genuinely novel and well-motivated. The finding that unevenness error dominates conversion error (Figure 3) and can be effectively addressed with extremely parameter-efficient calibration (0.107K parameters per layer matching 202M-parameter weight tuning) is a valuable empirical contribution.

## Suggestions

- Fix the DuQuant baseline numbers immediately. Re-run or use published DuQuant results for both models. This is the most urgent fix.
- Add spike count and energy estimates (e.g., using standard CMOS energy per synaptic operation figures) at different T values. Even a rough analysis would substantially strengthen the paper's motivation.
- Include a comparison table with prior spiking LLM approaches (SpikeZIP-TF, SpikeLLM) using published numbers where possible, or explain clearly why such comparisons are infeasible.
- Clarify in Section 3.4 whether the calibration target y^k refers to the QANN output or the original ANN output. From Definition 1 and the context of unevenness error, the QANN output is the natural target.

## Score and Decision

**Anchor comparison:**
- SpikeZIP (3.60): ANN-QANN-SNN conversion for CNNs. Rejected for novelty and clarity issues. Our paper is substantially stronger — LLM domain, cleaner method, better empirical results.
- Error-Free ANN-to-SNN Conversion (5.75): QCFS-based conversion for CNNs, requires training the source ANN. Rejected. Our paper is stronger — training-free, tackles harder LLM domain.
- SpikeBERT (6.33): Knowledge distillation for spiking language transformers. Rejected. Our paper is comparable in quality with a different, cleaner approach.
- SpikeLLM (7.00): Spiking LLM via saliency-based spiking and GIF neurons, accepted. Our paper is somewhat below due to the DuQuant error and missing energy analysis, despite having the advantage of being truly training-free.
- Spatio-Temporal Approximation (7.00): Training-free SNN conversion for ViT, accepted. Our paper tackles the harder LLM domain with better time-step efficiency (T=2 vs. T≥32), but has less polished experimental reporting.

**Round 1 bracket:** 4.5–7.0 → **Round 2 narrowed to:** 6.0

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>