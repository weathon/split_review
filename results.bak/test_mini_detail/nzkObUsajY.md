Now I have enough calibration data. Let me write the comprehensive final review.

**Round 1 bracket:** I identified the paper sits between the weak anchor cluster (~3.0) and the strong anchor cluster (~7.0). The narrowest plausible score range is between 4.5 and 6.5.

**Round 2 narrowing:** I compared against mtmqwhQiaG (5.25, Rejected), MiPyle6Jef (6.75, Accepted), G3vceNrP4o (4.0, Withdrawn/Reject), and the previously read XrunSYwoLr (7.0, Accepted). The paper is clearly stronger than G3vceNrP4o (4.0) and slightly stronger than mtmqwhQiaG (5.25) because it tackles a harder problem (LLMs vs. image classification) with a more original framework. But it is weaker than MiPyle6Jef (6.75) and XrunSYwoLr (7.0) primarily due to the DuQuant data integrity issue and missing efficiency metrics that are core to the paper's motivation. This places the paper at approximately 5.0.

---

## Summary

This paper proposes a "dual" ANN-to-SNN conversion framework for spiking LLMs. Instead of training a conversion-friendly ANN (the conventional approach), the method starts from a statically quantized LLM (obtained via training-free quantization like PrefixQuant) and replaces quantization functions with an Integer Spiking (IS) neuron equipped with multi-hierarchical thresholds. A layer-wise calibration technique adjusts only thresholds and initial membrane potentials (0.107K parameters per layer) to reduce conversion errors, particularly unevenness error from temporal spike dynamics. Experiments on LLaMA-2-7B and LLaMA-3-8B under W6A6 quantization show that calibration substantially recovers accuracy lost during uncalibrated conversion.

## Strengths

- **Novel dual conversion framework eliminates the need to train a conversion-friendly ANN.** The paper demonstrates that a spiking LLM can be obtained by building on an existing quantized LLM (PrefixQuant) and using IS neurons to replicate the quantization function, without the costly fine-tuning step required by conventional ANN-to-SNN conversion. Table 2 provides direct evidence: on LLaMA-2-7B at T=1, the calibrated SNN achieves 68.79% avg. accuracy, essentially matching the PrefixQuant baseline (68.70%).

- **Parameter-efficient layer-wise calibration with theoretical grounding.** The calibration updates only thresholds and initial membrane potentials (0.107K parameters per layer) yet recovers most of the performance lost during conversion. Table 4 shows this approach yields higher average accuracy than full weight fine-tuning (67.65% vs. 66.39% on LLaMA-2-7B at T=2) despite using ~6 orders of magnitude fewer parameters. Theorem 3 derives an upper bound on conversion error that justifies the layer-wise calibration strategy, and Remark 3 connects the bound to the experimental results.

- **Consistent performance recovery across time steps and model families.** The calibration method maintains competitive accuracy even at higher latencies (T=4, T=8) where the uncalibrated SNN collapses (e.g., LLaMA-3-8B T=8: 37.91% uncalibrated → 63.76% calibrated). This robustness is demonstrated on both LLaMA-2-7B and LLaMA-3-8B across five zero-shot tasks.

## Weaknesses

### Fatal
None.

### Major

- **DuQuant baseline numbers are clearly erroneous.** In Table 2, the reported DuQuant results for LLaMA-3-8B are **identical** to those for LLaMA-2-7B across all five tasks (WinoGrande 67.88, HellaSwag 72.64, ArcC 40.53, ArcE 53.07, PIQA 77.15), with only the PPL differing (5.53 vs. 6.27). This is numerically impossible for two different model families and strongly suggests a copy-paste error. While this does not invalidate the paper's core results (which rely on the Conversion vs. Ours internal comparison), it seriously undermines trust in the paper's data handling. The authors must correct or explain these numbers.

- **No evaluation of the paper's primary motivation — energy efficiency.** The entire motivation for building spiking LLMs is energy efficiency via event-driven, sparse computation. Yet the paper reports no efficiency metrics whatsoever: no spike counts, no FLOPs comparison, no energy estimation, no latency. For a method paper whose experiments explicitly compare against quantization baselines (which already provide efficiency gains), the absence of any demonstration that the spiking version adds energy value is a severe omission. The paper's Contribution 3 states it "potentially reduces the energy consumption of LLMs" but provides no evidence for this claim.

### Minor

- **Figure 3 error analysis is confusing and potentially misleading.** The right y-axis in Figure 3 ranges from -8 to 2 but is labeled "MSE loss," which is a non-negative quantity. This makes the figure difficult to interpret. The claim that "the difference between the two can measure the magnitude of the unevenness error" is not cleanly supported by the visualization due to the dual-axis scaling. The authors should use a consistent scale or provide a cleaner decomposition of errors.

- **Calibration target inconsistency.** The optimization objective in Section 3.4 is $\min_{\theta^k, v^k(0)} \|\sum_t \hat{y}^k(t) - y^k\|$, where $y^k$ is the FP16 ANN output, not the QANN output. Since the conversion pipeline starts from the QANN, the natural target should be the QANN output $\bar{y}^k$. Using the FP16 target means calibration is implicitly compensating for quantization error as well as conversion error, which is theoretically imprecise (even if it works in practice).

- **T=1 calibration changes are unexplained.** At T=1, the IS neuron with $\alpha^k(t) = 2^{n-j-1}$ and $L = \lceil (2^{n-1})/T \rceil$ should exactly replicate the quantization function per Theorem 2. Yet Table 2 shows calibration changes the output at T=1 (e.g., LLaMA-2-7B: Conversion 68.70% vs. Ours 68.79%). This suggests the initial conversion is already imperfect at T=1 or the calibration is addressing issues beyond temporal unevenness. A brief explanation is needed.

- **Missing details on input encoding and calibration optimization.** The paper states the condition $\sum_{t=1}^T \mathbf{I}^k(t) = \mathbf{X}^k$ but does not specify how the static quantized activations are distributed over time steps to produce $\mathbf{I}^k(t)$, particularly for the first layer. Additionally, the calibration optimization procedure is not described (e.g., gradient descent, grid search, number of calibration samples, sequential or joint optimization). These details are necessary for reproducibility.

### Trivial
None.

## Nice-to-Haves

- Report spike rates and estimated energy consumption using standard SNN energy models (e.g., synaptic operations count) to substantiate the efficiency motivation.
- Provide uncertainty estimates (standard deviations) for accuracy numbers, as several comparisons hinge on small differences (<1%).
- Compare against existing spiking LLM works (SpikeGPT, SpikeBERT, SpikeZIP) in the experiments section, even if only at a high level.

## Removed Points

These points were considered but removed for the reasons stated:

- **"Missing input encoding is a structural flaw"** — While the encoding method is underspecified, it is not a structural flaw. The IS neuron dynamics naturally handle temporal distribution (e.g., by feeding the same input each timestep and relying on the cumulative property in Theorem 2, or by dividing by T). The paper provides the mathematical conditions; an implementer would have sufficient guidance. This is a missing detail rather than a fatal gap, and it is better addressed as a minor weakness.

- **"Performance at higher T degrades significantly; calling it comparable is misleading"** — The paper acknowledges this degradation ("as time-step T increases, the performance degrades correspondingly") and the "comparable" language is applied to T=1 and T=2 settings, not T=8. The Table 2 numbers speak for themselves. This criticism overstates the paper's claims.

- **"Figure 3 is contradictory" (larger claim)** — The harsh critic claimed the ANN-vs-SNN error being smaller than ANN-vs-QANN error is "nonsensical." However, these are on different axes (log vs. linear) and the caption explains the ANN-vs-SNN curve measures a different quantity (not directly comparable by bar height). The figure is confusing but not contradictory. The issue is better described as a presentation problem.

- **"No comparison to existing spiking LLMs" (Scope creep)** — The paper cites SpikeGPT, SpikeBERT, and SpikeZIP in related work but does not experimentally compare. These methods use different training paradigms (direct training or different conversion), making direct comparison non-trivial. This is a nice-to-have, not a weakness.

- **"Missing related works"** — Removed per instructions.

- **"Scaling beyond 8B"** — Not a core requirement for the paper's scope.

## Novel Insights

Beyond the paper's own contributions, the key observation emerging from the reviews is that the dual conversion approach (quantize-then-convert) exposes a fundamental tension in spiking LLM design: the IS neuron's ability to replicate quantization functions at T=1 makes the framework practical, but the unevenness error at higher T severely degrades performance, and the calibration only partially recovers it. This suggests that the sweet spot for the framework is T=1–2, which limits the potential energy-efficiency advantage of spiking computation (since efficiency gains typically require higher time steps to exploit event-driven sparsity). The paper neither acknowledges this limitation nor provides efficiency numbers that would allow readers to assess the trade-off. This tension between the framework's theoretical elegance and its practical operating regime is worth highlighting as a direction for future work.

## Suggestions

1. **Fix the DuQuant numbers.** Verify the source and correct the table — this is the single most important fix.
2. **Report energy efficiency metrics** (spike rates, estimated energy/synaptic operations) to substantiate the core motivation.
3. **Clarify the input encoding mechanism** for the first layer: specify how static inputs are distributed over T time steps.
4. **Describe the calibration optimization procedure** in detail (optimizer, number of samples, sequential vs. joint).
5. **Fix Figure 3** to use a unified or clearly labeled scale so the error comparison is interpretable.
6. **Explain the T=1 calibration discrepancy** — why does calibration change performance when Theorem 2 predicts exact equivalence?

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews/j0sq9r3HFv.md | 2.50 | R1 | Irrelevant topic (LLMs for neuroscience parameter extraction). Much weaker paper. |
| /home/wg25r/review_agent/human_reviews/uOnElFfuey.md | 3.00 | R1 | Not about SNN conversion. Not comparable. |
| /home/wg25r/review_agent/human_reviews/gcEhF4nuYI.md | 3.00 | R1 | Token pruning for LLMs, unrelated topic. |
| /home/wg25r/review_agent/human_reviews/wPK65O4pqS.md | 3.00 | R1 | Spiking Transformer, not about conversion. Weaker methodology. |
| /home/wg25r/review_agent/human_reviews/uXytIlC1iQ.md | 3.75 | R1 | BrainGPT — SNN-based LLM. Rejected due to unclear methodology, small scale. Current paper is stronger in method and evaluation. |
| /home/wg25r/review_agent/human_reviews/4ILqqOJFkS.md | 3.67 | R1 | Spiking SSM, rejected for incremental contribution. Current paper addresses a harder problem with more novelty. |
| /home/wg25r/review_agent/human_reviews/G3vceNrP4o.md | 4.00 | R2 | ANN-SNN distillation for image restoration, rejected. Limited novelty. Current paper is stronger. |
| /home/wg25r/review_agent/human_reviews/mtmqwhQiaG.md | 5.25 | R2 | CSS coding for SNN conversion, rejected (scores 3,6,6,6). Novel coding scheme but missing efficiency metrics and incremental novelty concerns. Current paper is comparable but addresses a harder problem (LLMs). |
| /home/wg25r/review_agent/human_reviews/Sf4ep9Udjf.md | 6.75 | R1 | P-SpikeSSM, accepted (Poster). Probabilistic spiking SSM with strong theory. Current paper is weaker due to data integrity issues. |
| /home/wg25r/review_agent/human_reviews/MiPyle6Jef.md | 6.75 | R2 | QP-SNN, accepted (Poster). Quantized and pruned SNN. Well-executed but limited to CV tasks. Current paper addresses LLMs but has data integrity problems that this paper does not. |
| /home/wg25r/review_agent/human_reviews/XrunSYwoLr.md | 7.00 | R1/R2 | Spatio-Temporal Approximation, accepted (Poster). Training-free SNN conversion for Transformers (ViT). Solid theory and clean experiments. Current paper is clearly weaker due to the DuQuant error and missing efficiency metrics. |

**Round 1 bracket:** 4.5–6.5, narrowed from the weak cluster (~3) and strong cluster (~7).

**Final score determination:** The paper is above the rejected SNN papers at ~3.75–4.0 (clearer methodology, harder problem) and comparable to the rejected CSS paper at 5.25 (similar profile of interesting idea + missing key evidence). It falls below the accepted papers at 6.75–7.0, primarily because the DuQuant data error undermines confidence in results and the missing efficiency metrics leave a central claim unsupported.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>