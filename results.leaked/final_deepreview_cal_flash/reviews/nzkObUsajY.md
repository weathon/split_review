Now I have all the information I need. Let me compose the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

---

Let me compute the final review now.

For the score, let me think about this carefully based on the calibration:

**Round 1 bracketing**: The paper sits between the weak anchors (score < 3.5, mostly unrelated) and the strong anchors (score > 7.5, which are top-tier papers). The most relevant band is the middle band (3.5-7.5).

**Round 2 narrowing**: The most comparable anchors are:
- GTzP2GC7NR (5.75, Reject) — ANN-to-SNN conversion for CNNs, requires training a conversion-friendly ANN. The reviewed paper is more novel (LLM-targeting, training-free) and has stronger results.
- D4sQzdMvcG (5.75, Reject) — ANN-to-SNN conversion with calibration for CV. Similar calibration approach but applied to CNNs. Reviewed paper targets harder domain (LLMs).
- XrunSYwoLr (7.00, Accept) — Training-free SNN conversion for vision Transformers. Similar goal but for ViT not LLM. More thorough evaluation. Reviewed paper has comparable ambition but less polished evaluation.
- 6c4gv0E9sF (6.33, Reject) — SpikeBERT, spiking BERT via knowledge distillation. Different approach (training-based). Comparable language domain.

The reviewed paper is better than the 5.75 anchors (more novel, harder domain, better results) but has some weaknesses that the 7.00 anchor doesn't have (missing comparison with spiking LLM methods, underspecified calibration). I'd place it between these, around 6.0-6.5.

I'll go with **6.5** — the paper has genuine novelty (the dual conversion idea is clean and well-motivated), solid empirical results, and the parameter-efficient calibration is clearly beneficial. The main weaknesses (missing spiking LLM comparison, calibration details) are real but addressable in revision and don't undermine the core claim.

Decision: **Accept** — this is a solid contribution to the SNN + LLM intersection. The paper opens a new direction (training-free conversion via quantized bridge) and the results validate the approach.

Actually, wait — looking at the scores more carefully. The 5.75 anchors were rejected, the 6.33 was rejected, the 7.00 was accepted. So there's a not-sharp boundary around 6.5-7.0 where papers go from reject to accept. With a score of 6.5, this would be borderline. Let me think...

The paper's core contribution is solid. The missing comparison is a significant weakness but the paper frames its approach as fundamentally different from SpikeZIP (training-free vs. requiring training). The calibration details are missing but this is a minor issue. The theoretical caveats are acknowledged by the authors.

Given that I see the paper as having a genuinely novel contribution with solid experimental support and addressable weaknesses, I'll lean toward Accept and score 6.5.

Actually, let me reconsider. The harsh critic's point about missing SpikeZIP comparison is valid and significant. If I were a reviewer, I'd want to see at least a discussion of why SpikeZIP cannot be compared (e.g., requires training a conversion-friendly ANN that doesn't exist at 7B scale). The paper mentions this general limitation but doesn't make the specific argument.

Let me go with **6.0** and **Accept** — the paper has clear value but the missing comparison is a real concern. Score 6.0 is consistent with a paper that has genuine strengths and addressable weaknesses.

Hmm, actually I'm torn. Let me look at what score 6 means in the NeurIPS/ICLR context... Generally 6 is "accept, good paper" and 5 is "weak accept/borderline." Given that the missing comparison is significant but the paper's core novelty is real, I'll go with 6.0.

Wait, I need to think about this differently. The instructions say:
- Score distribution: extreme scores are rare but valid
- Do NOT cluster scores around 5
- The score should be relative to retrieval samples

Given the anchors:
- 5.75 anchors were rejected
- 6.33 was rejected (SpikeBERT)
- 7.00 was accepted (STA)

The reviewed paper is comparable to SpikeBERT (6.33, Reject) in ambition but has a different approach and better results. SpikeBERT was rejected partly because it only matched TextCNN performance and had overclaimed. The reviewed paper has clearer demonstrated value (recovering QANN performance with <0.1K params per layer).

The STA paper at 7.00 (Accept) is cleaner in its evaluation but only tested on ViT-B/32. The reviewed paper tests on LLMs (7B/8B scale) which is harder.

I think 6.0-6.5 is the right range. Let me go with **6.0** and **Accept**. The missing spiking LLM baseline comparison is a genuine weakness, and the calibration details need to be provided. But the core idea is novel and the results are clear.

Actually, you know what, I'll go with **6.5**. Let me explain: The paper's contribution is novel (first training-free conversion for LLMs via quantization bridge), the results clearly show the method works (recovering QANN accuracy at T=1, and with calibration at T>1), and the parameter efficiency is impressive (0.107K vs 202M params). The weaknesses are real but addressable. 6.5 better reflects that this is a good, solid paper with room for improvement.

Let me finalize at 6.5, Accept.Now I'll write the final consolidated review.

## Summary

This paper proposes a "dual ANN-to-SNN conversion" framework for obtaining spiking LLMs. Instead of training a conversion-friendly ANN (the conventional approach, which is expensive for large models), the method starts from a statically quantized LLM (via PrefixQuant) and introduces a multi-level threshold Integer Spiking (IS) neuron that approximates the quantization function. A parameter-efficient layer-wise calibration of neuronal thresholds and initial membrane potentials is introduced to reduce conversion errors, particularly the unevenness error caused by temporal spike dynamics. Experiments on LLaMA-2-7B and LLaMA-3-8B show that the calibrated SNN recovers quantized-ANN accuracy at T=1 and substantially outperforms uncalibrated conversion at larger timesteps, using only ~0.1K learnable parameters per layer versus ~200M for weight fine-tuning.

## Strengths

1. **Novel and well-motivated dual conversion paradigm.** The core idea—using a statically quantized LLM as a bridge to SNN conversion, thereby sidestepping the need to train a conversion-friendly ANN—is clean, original, and directly addresses a real bottleneck (conventional ANN-to-SNN conversion requires training a tailored ANN, which is prohibitively expensive at LLM scale). This framing is clearly contrasted with conventional conversion in Figure 1 and Table 1, and the approach is validated without any ANN fine-tuning in Section 4.

2. **Parameter-efficient calibration with strong empirical gains.** The layer-wise calibration adjusts only neuronal thresholds and initial membrane potentials (0.107K parameters per layer) while freezing all other weights. Table 2 shows that calibration lifts average accuracy from 59.99% to 67.65% for LLaMA-2-7B at T=2, and from 48.83% to 69.03% for LLaMA-3-8B at T=2. Table 4 further demonstrates that this uses 2,000,000× fewer learnable parameters than weight calibration while achieving comparable or better accuracy (67.65% vs. 66.39% for LLaMA-2-7B). This combination of strong recovery and minimal overhead is the paper's most compelling practical result.

3. **Performance recovery at T=1.** The calibrated SNN at T=1 matches or slightly exceeds the quantized ANN baseline (LLaMA-3-8B: 71.67% vs. 70.24% average zero-shot accuracy; LLaMA-2-7B: 68.79% vs. 68.70%), as shown in Table 2. This demonstrates that the conversion does not sacrifice model quality while introducing spiking dynamics, directly fulfilling the paper's main performance claim.

4. **Ablation across learnable parameter budgets.** Table 3 varies the activation group size across several orders of magnitude (0.107K to 23.399K parameters per layer). Average accuracy stays within a narrow range (65.46%–67.65%), showing the calibration is robust and broadly effective.

5. **Theoretical error decomposition and bounding.** The paper formally defines clipping, quantization, and unevenness errors (Section 3.3) and provides Theorem 3 bounding overall conversion error in terms of per-layer errors. This provides a principled motivation for the layer-wise calibration approach.

## Weaknesses

### Fatal
None.

### Major

1. **Missing experimental comparison with existing spiking LLM methods.** The paper cites SpikeZIP (You et al., 2024) as an ANN-to-SNN conversion method for language models and even adopts its spiking-compatible operations (Section 3.2.3), yet the evaluation (Section 4) compares only against quantization baselines (PrefixQuant, DuQuant) and the authors' own uncalibrated version. No comparison—neither accuracy/latency numbers nor a substantive argument for incomparability—is provided against SpikeZIP or any other method that produces a spiking LLM. Since the paper is positioned as advancing spiking LLMs (the title asks "How to Get Spiking LLMs?"), the reader needs to understand how this approach fares relative to prior work in the same domain. The paper argues that conventional conversion methods require training a conversion-friendly ANN, which is expensive at LLM scale—this is a valid justification for a different approach, but it does not relieve the authors of the responsibility to either (a) provide an empirical comparison under a feasible setup, or (b) give a concrete technical argument (with evidence) for why such a comparison is not meaningful. Without this, the contribution relative to prior spiking LLM work is not clearly established.

### Minor

1. **Calibration procedure is underspecified.** The calibration objective is stated as `min_{θ^k, v^k(0)} || Σ_t ŷ^k(t) – y^k ||` (Section 3.4), but no details are given about: what data is used for calibration (how many samples, from which dataset), what optimizer and learning rate are used, how many optimization steps, whether calibration is performed sequentially layer-by-layer or jointly, or what stopping criterion is applied. The paper states that code will be released upon publication, but the current lack of even basic procedural details prevents reproducibility assessment and raises questions about potential overfitting. This is a few sentences that should be added.

2. **Theoretical equivalence conditions are acknowledged as impractical, but the resulting approximation error is not characterized.** Theorem 2 requires `LT = 2^n – 1` and specific input current intervals. Remark 1 openly states that this equality "rarely holds for arbitrary integer choices of L and T if T ≠ 1" and that the method resorts to `L = ceil((2^n-1)/T)`. The paper does not analyze how large the resulting mismatch is—neither theoretically nor empirically across layers. The error bound in Theorem 3 is generic (it applies to any conversion) and does not leverage properties of the IS neuron design. The theoretical framing is weakened by this gap between the exact-equivalence promise and the acknowledged approximation.

3. **Energy efficiency claims are unsupported.** The introduction and related work repeatedly assert that SNNs offer "low power consumption" and "energy efficiency" (e.g., Section 1, Section 2.1), and contribution 3 claims the work "potentially reduces the energy consumption of LLMs." However, no energy measurements, spike rate analyses, or even theoretical FLOPs comparisons are provided anywhere in the paper. While actual hardware measurements may be out of scope, an analysis of spike counts or estimated synaptic operations would substantiate the qualitative energy argument.

4. **Figure 3 axis concern.** The auto-generated figure description indicates the right y-axis (ANN vs. SNN MSE, linear scale) ranges from -8 to 2. Since MSE cannot be negative, either the axis is mislabeled or the auto-generated description is inaccurate. This figure is central to the claim that unevenness error dominates, and the visual evidence as presented is unreliable. The authors should clarify or correct the axis ranges.

5. **Perplexity-accuracy trade-off in Table 4 not discussed.** For LLaMA-2-7B, the proposed calibration achieves better average accuracy (67.65 vs. 66.39) but worse perplexity (7.39 vs. 6.37) compared to weight calibration. This discrepancy is not addressed.

### Trivial
None.

## Nice-to-Haves

- A comparison with other quantization schemes (e.g., QuaRot, SpinQuant) beyond PrefixQuant would broaden the contribution.
- An analysis of spike rates (spike counts per layer) to give a qualitative energy argument.
- Confidence intervals or significance tests for the accuracy results, especially where differences are small (~0.1–0.5%).
- A brief latency comparison (simulated spiking operations vs. QANN inference) to contextualize the practical trade-offs.

## Removed Points

- **"T=1 improvement suggests approximation error present even at T=1" (Harsh Critic, Section-by-Section)**: This point is removed because the calibration modifies thresholds and initial potentials relative to the QANN, so the SNN is not constrained to be identical to the QANN even at T=1. The small improvement (68.79 vs. 68.70 on LLaMA-2-7B) is well within expected noise and does not indicate approximation error. For LLaMA-3-8B, the larger gap (71.67 vs. 70.24) may reflect that the calibration is genuinely improving the QANN baseline at T=1 (since it optimizes neuron parameters post-conversion).
- **"Performance degradation as T increases should be discussed as acceptable" (Harsh Critic)**: The paper already addresses this explicitly: "as time-step T increases, the performance degrades correspondingly. We attribute this phenomenon to the growing unevenness error introduced by the larger time-step." This is adequate discussion for a known phenomenon in SNN conversion.
- **"Missing comparison with SpikeZIP" characterization as "structural / fatal" (Harsh Critic)**: Downgraded from potentially fatal to Major. The paper's core claim—that the dual conversion + calibration approach recovers QANN performance—is well-supported by the existing experiments. The missing comparison is a significant scope gap but does not invalidate the demonstrated results. The paper also provides a justification (conventional methods require training that is expensive at LLM scale), even if this justification could be more explicit.
- **Strength Finder generic strengths about "important problem" and "potential value"**: Removed per filtering rules (too generic, no concrete anchor in the paper).
- **Various minor reproducibility nitpicks about individual hyperparameters**: Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The primary insight—that a quantized LLM's activation function can be approximated by an Integer Spiking neuron, with layer-wise calibration correcting the temporal unevenness error—is well articulated in the paper and constitutes its main novelty.

## Suggestions

1. Add an experimental comparison or a concrete technical argument for why SpikeZIP and similar methods cannot be directly compared at this scale. If a full comparison is infeasible, a focused experiment (e.g., on a smaller proxy model where SpikeZIP's ANN training is feasible) or a quantitative analysis of the training cost difference would substantially strengthen the paper.
2. Specify calibration details: number of samples, dataset used, optimizer, learning rate, number of steps, and whether calibration is sequential or joint. This is essential for reproducibility.
3. Either correct Figure 3's axes or clarify that the auto-generated description is inaccurate. Add numerical quantification of the three error components (clipping, quantization, unevenness) to support the claim that unevenness dominates.
4. Provide spike rate statistics (average spikes per neuron per timestep across layers) to give a qualitative energy argument, or explicitly state that energy benefits are not measured but expected from the spiking paradigm.
5. Discuss the perplexity-accuracy trade-off observed in Table 4.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing)**: Three queries targeting weak (score < 3.5), middle (3.5–7.5), and strong (>7.5) bands on ANN-to-SNN conversion and spiking LLM topics.

- Weak band anchors (avg 2.33–3.00): Largely unrelated to the paper's topic (LLM biology, knowledge graphs, neural forecasting). Not useful for direct comparison.
- Middle band anchors (avg 3.60–5.75): **GTzP2GC7NR** (5.75, Reject) — ANN-to-SNN conversion for CNNs; **D4sQzdMvcG** (5.75, Reject) — quantization-aware ANN-to-SNN conversion with calibration for vision; **6c4gv0E9sF** (6.33, Reject) — SpikeBERT, spiking BERT via knowledge distillation; **u438df0Uce** (3.60, Reject) — different SpikeZIP paper for CNNs.
- Strong band anchors (avg 7.60–8.00): Top-tier LLM quantization/accept papers — these are clearly more polished and comprehensive.
- **Initial bracket**: 4.5–7.5.

**Round 2 (Narrowing)**: Two queries targeting the plausible bracket, including one on training-free SNN conversion for Transformers.

- **XrunSYwoLr** (7.00, Accept) — "Spatio-Temporal Approximation: A Training-Free SNN Conversion for Transformers." Training-free SNN conversion for ViT-B/32. The reviewed paper is comparable in ambition (both are training-free conversion approaches for non-conv architectures) but the STA paper has a more thorough evaluation and clearer baseline comparisons. The reviewed paper targets harder models (7B+ LLMs vs. ViT-B/32) and has more parameter-efficient calibration. I judge the reviewed paper as slightly weaker due to the missing SpikeZIP comparison and underspecified calibration details.
- **MiPyle6Jef** (6.75, Accept) — QP-SNN on quantization/pruning for SNNs. Less directly comparable.
- **GTzP2GC7NR** (5.75, Reject) — The reviewed paper is clearly stronger: more novel paradigm, harder domain (LLMs vs. CNNs), and better-validated calibration.

**Anchors summary**:
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| GTzP2GC7NR | 5.75 | 1,2 | Weaker: CV-domain conversion requiring ANN training |
| D4sQzdMvcG | 5.75 | 1,2 | Weaker: CV-domain, similar calibration concept but simpler domain |
| 6c4gv0E9sF | 6.33 | 2 | Comparable: SpikeBERT also targets language, but uses training (distillation) |
| u438df0Uce | 3.60 | 1 | Weaker: different SpikeZIP paper (CNNs), low score |
| XrunSYwoLr | 7.00 | 2 | Slightly stronger: cleaner evaluation, but only on ViT-B/32 |
| MiPyle6Jef | 6.75 | 2 | Less directly comparable (pruning/quantization for SNNs) |

**Final score determination**: The paper is stronger than the 5.75 anchors (more novel, harder domain) and comparable to but slightly weaker than the 7.00 anchor (missing comparison, calibration details). The SpikeBERT anchor at 6.33 (Reject) is a relevant comparison — both target language, but SpikeBERT uses training while this paper uses training-free conversion. I place this paper at 6.5, reflecting a solid contribution with genuine novelty and clear empirical validation, weighted against addressable weaknesses in the evaluation scope.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>