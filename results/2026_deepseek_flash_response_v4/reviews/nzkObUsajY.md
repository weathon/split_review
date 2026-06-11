## Summary
This paper proposes a dual ANN-to-SNN conversion framework for building spiking LLMs without training a conversion-friendly ANN. The approach starts from an off-the-shelf quantized LLM (via training-free PTQ), replaces quantizers with an Integer Spiking (IS) neuron with multi-hierarchical thresholds, and applies a layer-wise calibration that adjusts only per-layer thresholds and initial membrane potentials (0.107K params/layer). Experiments on LLaMA-2-7B and LLaMA-3-8B at W6A6 show the calibration recovers much of the accuracy lost during conversion.

## Strengths
1. **Eliminates the need for training a conversion-specific ANN** — Conventional ANN-to-SNN conversion requires training a tailored ANN with conversion-friendly activations (e.g., QCFS), which is prohibitive at LLM scale. The dual conversion framework (Section 3.2) instead starts from an already-quantized LLM obtained via training-free PTQ, removing this bottleneck. Table 1 contrasts this with conventional methods, and Table 2 validates the approach on LLaMA-2-7B and LLaMA-3-8B.

2. **Extreme parameter efficiency of calibration** — Section 4.4 (Table 4) shows that adjusting only thresholds and initial membrane potentials (0.107K parameters per layer) recovers average accuracy from 59.99 to 67.65 on LLaMA-2-7B at T=2, while full weight fine-tuning (202M parameters) achieves only 66.39 accuracy. This concretely demonstrates that the dominant conversion errors can be corrected with minimal parameter overhead.

3. **Empirical diagnosis of unevenness error as the dominant degradation** — Figure 3 disentangles clipping/quantization error from unevenness error by comparing ANN-vs-QANN MSE with ANN-vs-SNN MSE. The gap directly identifies unevenness error as the primary degradation source, cleanly motivating the calibration design.

4. **Consistent recovery across timesteps and model families** — Table 2 shows calibration bridges large gaps across T ∈ {2,4,8} and across both LLaMA-2-7B and LLaMA-3-8B (e.g., LLaMA-3-8B at T=4: 41.09 → 67.21 avg acc), indicating the method targets structural error rather than overfitting a single configuration.

## Weaknesses

### Fatal
None.

### Major
1. **Performance degrades with more timesteps, contradicting the core SNN value proposition** — In standard ANN-to-SNN conversion, more timesteps improve approximation accuracy. Here, T=1 gives the best results and T=8 the worst (LLaMA-2-7B Avg Acc: 68.79 at T=1 vs 66.03 at T=8; PPL: 5.61 vs 12.03). The paper acknowledges this (Section 4.2: "as time-step T increases, the performance degrades correspondingly") and attributes it to "growing unevenness error," but does not resolve the paradox. At T=1 the network is effectively a quantized ANN with different activations — no meaningful spiking dynamics occur. The paper provides no energy measurements or analysis to justify why anyone would run T>1, given that doing so incurs multiplicative computational cost for strictly worse performance. This undermines the central motivation for using SNNs (energy-efficient temporal processing) and the claim that the framework produces SNNs with "neural dynamics" (Contribution 3).

2. **No comparison against any SNN baseline for the claimed domain** — The paper claims to advance spiking LLMs (title: "How to Get Spiking LLMs?") and cites SpikeZIP as a related advance, yet compares only against quantization methods (PrefixQuant, DuQuant) and a weight fine-tuning baseline. No existing ANN-to-SNN conversion method applied to LLMs is used as a baseline. While the stated claim of "comparable to quantization techniques" is accurate on its face, the absence of any SNN baseline makes it impossible to assess whether the method advances the state of the art in *spiking* LLMs specifically.

### Minor
3. **"Comparable" claim is overstated for perplexity** — For LLaMA-2-7B at T=2, Avg Acc is 67.65 vs PrefixQuant's 68.70 (close), but PPL is 7.39 vs 5.76 (28% relative increase). At T=8, PPL reaches 12.03 vs 5.76 (109% increase). While accuracy recovery is strong, the perplexity degradation at T>1 is substantial, and the "comparable" framing is misleading for language modeling quality.

4. **Uncalibrated conversion is near-random at higher T; calibration does nearly all the work** — At T=8 on LLaMA-3-8B, uncalibrated "Conversion" achieves 37.91 Avg Acc and PPL 190.63 (essentially collapsed output); calibration recovers to 63.76 and 18.93. While the paper presents a unified pipeline, the framing emphasizes the IS neuron design as accurately emulating the quantization function (Section 3.2.2), when the exact equivalence conditions (Theorem 2) require LT = 2^n - 1 which "rarely holds" (Remark 1). The calibration is what makes the method work, and the paper should be more transparent about this.

5. **No energy or efficiency analysis** — The entire motivation is energy-efficient edge deployment of LLMs via SNNs, yet no energy measurements, FLOP comparisons, or even analytical estimates are provided. This gap is especially salient given that the method runs T forward passes with degraded performance at higher T.

6. **Theoretical bound (Theorem 3) is purely qualitative** — The bound decomposes error into layer-wise terms scaled by products of Lipschitz constants (∏ ρ^τ). For a 32-layer model, even modest ρ>1 yields exponential growth, but the constants are never estimated, bounded, or measured for any model tested. The theorem motivates layer-wise calibration (Remark 3) but provides no practical guarantee about error magnitudes.

7. **Figure 3 axis issue** — The ANN-vs-SNN curve is plotted with a right-axis ranging from -8 to 2 for what the caption describes as MSE loss, which cannot be negative. This appears to be a labeling or metric error in the visualization.

8. **Table 3 inverse correlation unexplained** — Varying the learnable parameter budget shows the smallest budget (0.107K params, group size -1) gives the best accuracy (67.65), while the largest (23.399K params, group size 1) gives the worst (65.46). This inverse trend is noted but not discussed or explained.

9. **No limitations discussion** — The conclusion restates claims without caveats. No limitations of the method are discussed anywhere, despite the acknowledged T>1 degradation and boundary conditions on the theoretical equivalence.

### Trivial
None beyond those listed above.

## Nice-to-Haves
- Comparison against at least one existing SNN/ANN-to-SNN conversion method for LLMs (e.g., SpikeZIP or SpikeLLM).
- Energy or efficiency estimates (even analytical) to substantiate the core motivation.
- Results at other quantization levels (e.g., W4A4, W8A8) to test generality.
- Ablation of calibration data requirements (how many samples, sensitivity to calibration set).
- Analysis of why the weight fine-tuning baseline (Table 4) achieves worse accuracy despite using 1.9M× more parameters — this comparison currently looks like the baseline may be undertuned.

## Removed Points
- **Truncated sentence at line 194** — PDF extraction artifact, not a paper flaw. Removed per formatting-artifact rule.
- **Accusation that the evaluation is "against the wrong baselines" as a fatal flaw** — The paper's stated claim is "comparable to state-of-the-art quantization techniques" and the comparison set aligns with this claim. The lack of SNN baselines is a real weakness (kept as Major #2) but not a fatal omission.
- **Strength: "Formal error-bound analysis grounded in layer-wise Lipschitz constants"** — Removed because it conflicts with Weakness #6 (the bound is purely qualitative with unmeasured constants).
- **Generic praise about addressing an important problem** — Removed as generic/superficial.
- **Missing related works** — Cannot confirm without external sources. Removed per rule.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add a comparison against at least one SNN conversion baseline (e.g., SpikeZIP or SpikeLLM) or clearly reframe the paper's scope to emphasize the calibration contribution rather than claiming advances in spiking LLMs.
2. Include energy or efficiency estimates to support the edge-deployment motivation, and discuss the T>1 degradation transparently — explain if any regime where T>1 could be beneficial, or acknowledge that the method is best used at T=1 (effectively a quantized ANN with spiking-compatible operations).
3. Provide estimates of the Lipschitz constants in Theorem 3 to ground the theoretical bound, or reframe it as purely qualitative motivation.
4. Fix Figure 3's axis labeling to clarify what metric is plotted for the ANN-vs-SNN curve.
5. Add a limitations section discussing the T>1 degradation, reliance on calibration, and the energy-accuracy trade-off.
6. Explain the inverse correlation in Table 3 between parameter budget and performance.

## Score and Decision

**Calibration procedure:**

**Round 1 (Bracketing):** Three calibration_search calls querying bands (<3.5, 3.5-7.5, >7.5) for ANN-to-SNN conversion / spiking LLM topics. Low band yielded tangential papers (sparsity, brain-regularizers). Middle band yielded directly relevant anchors: SpikeLLM (7.0, Accept), QAC (5.75, Reject), Spatio-Temporal Approximation (7.0, Accept), SpikeZIP (3.6, Reject). High band yielded neuroscience papers. Initial bracket: 5.0–6.5.

**Round 2 (Narrowing):** Two calibration_search calls targeting (4.5-6.5) and (6.0-7.5) for quantization-aware conversion and training-free spiking LLM conversion. Read QAC (5.75, Reject), SpikeLLM (7.0, Accept), Spatio-Temporal Approximation (7.0, Accept), SpikeBERT (6.33, Reject), Canonic Signed Spike (5.25, Reject) in full.

**Anchor comparisons:**
- **SpikeLLM (7.0, Accept)** — Stronger in scope (up to 70B models), novelty (first spiking LLM), and evaluation (energy analysis included). Our paper is clearly weaker.
- **Spatio-Temporal Approximation (7.0, Accept)** — First training-free SNN conversion for Transformers. Stronger theoretical contributions. Our paper has less novelty.
- **QAC (5.75, Reject)** — Very similar approach (QANN→SNN conversion + calibration of thresholds/membrane potentials). Tested on CIFAR/ImageNet, not LLMs. Shared weaknesses: "why not use quantized ANNs?" question. Our paper extends to LLMs but adds issues (T>1 degradation, no SNN baselines, no energy analysis). Comparable quality.
- **SpikeBERT (6.33, Reject)** — Highly polarized (8,8,3). Spiking BERT via distillation. Our paper is more consistent but less ambitious.
- **Canonic Signed Spike (5.25, Reject)** — SNN coding scheme. Tested on CIFAR/ImageNet. Our paper is slightly stronger due to LLM-scale evaluation.
- **SpikeZIP (3.6, Reject)** — ANN-QANN-SNN conversion, not at LLM scale. Our paper is clearly stronger.

**Final score positioning:** Between QAC (5.75, Reject) and the mid-6-range anchors. Our paper shares QAC's structural limitations (limited framing of why SNN over quantized ANN, calibration doing most of the work) plus additional issues specific to the LLM setting (T>1 degradation absent resolution, missing energy analysis). Score: 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>