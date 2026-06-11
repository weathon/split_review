Now I have strong calibration anchors. Let me write the final review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes a "dual" ANN-to-SNN conversion framework for LLMs. Instead of training a conversion-friendly ANN (as conventional methods do), it starts from an off-the-shelf quantized LLM (W6A6), replaces the quantization function with multi-level Integer Spiking (IS) neurons, and applies a parameter-efficient layer-wise calibration that optimizes only neuronal thresholds and initial membrane potentials (0.107K parameters/layer vs. ~200M for weight fine-tuning). Experiments on LLaMA-2-7B and LLaMA-3-8B show the calibrated SNN achieves performance close to the quantized baseline at T=1–2, with calibration recovering much of the gap versus uncalibrated conversion.

## Strengths

1. **Eliminates the need to train a conversion-specific ANN** — Conventional ANN-to-SNN conversion (Bu et al., 2022) requires training a tailored ANN with QCFS activations, which is prohibitive for LLMs. The paper's pipeline starts from a training-free quantized LLM (Table 1, Section 3.2). This is a genuine architectural innovation for scaling SNN conversion to LLMs.

2. **Three-orders-of-magnitude parameter efficiency** — Table 4 shows calibration using only 0.107K learnable parameters per layer achieves competitive or better average accuracy than full weight fine-tuning (~200M parameters): 67.65 vs. 66.39 Avg. Acc. on LLaMA-2-7B and 69.03 vs. 68.65 on LLaMA-3-8B while using ~2,000× fewer parameters.

3. **Robustness to calibration group size** — Table 3 demonstrates average accuracy varies by <2% across group sizes from 1 to 256 (0.107K–23.399K params/layer), indicating the method does not require careful hyperparameter tuning.

## Weaknesses

### Major

1. **Energy efficiency — the paper's entire motivation — is asserted but never measured.** The paper's raison d'être is that SNNs offer "brain-inspired efficiency and low power consumption" (abstract), yet contains zero measurements of energy consumption, spike counts, synaptic operations, or any proxy for energy cost. At T=2/4/8 the model runs multiple forward passes — at T=8 the SNN uses ~8× the compute of the quantized ANN baseline while achieving worse perplexity (12.03 vs. 5.76 on LLaMA-2-7B). Without even a simple energy proxy, the paper's central claim is unsubstantiated. Compare with SpikeLLM (ICLR 2025, score 7.00), which was accepted partly because it did provide energy-efficiency comparisons; the absence here is a gap of the same nature but more severe.

2. **Performance degrades as timesteps increase — opposite of standard SNN conversion behavior, with no mechanistic explanation.** In standard IF-based conversion, more timesteps improve approximation. Here, performance monotonically degrades with T (LLaMA-2-7B Avg. Acc.: 68.79 at T=1 → 67.65 at T=2 → 67.04 at T=4 → 66.03 at T=8; Table 2). The paper attributes this to "growing unevenness error" (line 212), which is a restatement rather than an explanation. Why does unevenness error grow with T in this architecture? Is it the IS neuron's multi-level threshold structure, the way input currents are distributed across timesteps, or the nonlinear operations adopted from You et al. (2024)? The best performance is at T=1, where the IS neuron has no temporal dynamics and essentially acts as a quantization function — this undermines the SNN motivation and severely limits the method's practical value for neuromorphic deployment where temporal coding matters.

3. **No comparison against any other spiking LLM approach.** The paper mentions SpikeZIP (You et al., 2024) and SpikeGPT (Zhu et al., 2023) as exemplars, yet evaluates only against quantization methods (PrefixQuant, DuQuant) and its own uncalibrated baseline. "Conversion" in Table 2 is the authors' own uncalibrated SNN, not a competing method. Without any comparison to other SNN-based approaches (e.g., SpikeZIP-TF, SpikeLLM), a reader cannot judge whether this approach advances the state of spiking LLMs. The paper claims comparability to quantization techniques, but this is a different claim than advancing SNN-based LLM deployment.

### Minor

1. **Theoretical disconnect between what is bounded and what is optimized.** Theorem 3 bounds the SNN-to-ANN error (∥∑ŷ(t) − y∥), but the calibration objective (Section 3.4) minimizes ∥∑ŷ^k(t) − y^k∥ where y^k is the QANN output — the SNN-to-QANN gap. The bound's second term (QANN-to-ANN quantization error, Σ(∏ρ^τ)∥g^k(x^k) − y^k∥) is not addressed by calibration, and the paper does not acknowledge this disconnect. Additionally, Theorem 3's bound involves products of Lipschitz constants (∏ρ^τ) that can grow or shrink exponentially with depth; the paper does not estimate ρ^k or discuss tightness.

2. **Only one quantization setting (W6A6) and two model sizes (7B/8B) tested.** The method's behavior at different bit-widths (W4A4, W8A8) is a natural question since Theorem 2 ties IS neuron parameters L, T to the quantization bit n. Only LLaMA-family models are tested. For comparison, SpikeLLM was tested up to 70B parameters and across multiple bit-widths. The limited scope makes it unclear how well the method generalizes.

3. **Only one PTQ method (PrefixQuant) is used as the starting point.** Testing at least one alternative PTQ method (e.g., QuaRot, SpinQuant) would show the approach is not tied to a specific quantization scheme.

4. **The "dual" terminology is never formally defined.** The paper contrasts Figure 1(a) and 1(b), calling the latter "dual," but this is simply a different pipeline architecture — there is no formal duality. This is a presentational issue.

5. **Theorem 2's exact equivalence rarely holds in practice**, as the paper acknowledges (Remark 1: LT = 2^n − 1 "rarely holds for arbitrary integer choices of L and T if T ≠ 1"). The IS neuron only approximately mimics the quantization function, which is fine, but the theoretical framing is weaker than it initially appears.

### Trivial

1. Figure 3's right y-axis is described as ranging from −8 to 2 for MSE loss, which is nonsensical (MSE cannot be negative). Likely a labeling/parser artifact, but it makes the figure uninterpretable from the text.

## Nice-to-Haves

- Add even a simple energy proxy (spike count, synaptic operations per forward pass) to substantiate the efficiency motivation.
- Investigate the mechanism behind T-degradation — e.g., measuring per-timestep violations of Theorem 1's interval conditions.
- Test at least one additional bit-width and one alternative PTQ method.
- Include at least one spiking LLM baseline (e.g., SpikeZIP-TF, if feasible) to contextualize the contribution within the SNN literature.

## Removed Points

These points are flagged to be removed, treat them with caution:

- Criticism about missing related works (cannot confirm without external sources). 
- Speculative claims about "not yet released" code or that reproducibility is impossible (the paper states code will be released upon publication).
- Formatting/style nitpicks about the paper's presentation (parser artifacts from PDF extraction).
- The claim that T=1 "is not an SNN" — IS neurons at T=1 still produce discrete-valued outputs via threshold-based firing; single-timestep SNNs are a standard setting in the SNN literature.
- The claim that the evaluation is fundamentally wrong because baselines are quantization methods — the paper explicitly states it is comparing "with state-of-the-art quantization techniques" (abstract, Section 4.1), so the evaluation is aligned with the stated claim. The issue is the absence of SNN baselines, not that quantization baselines are inappropriate.
- The claim that Table 4's framing is deceptive — the paper reports both Avg. Acc. and PPL, showing the trade-off clearly.
- Strength Finder's claim about "Provably bounded conversion error" overstates the theory — it's a bound, not a proof of practical convergence — but it's still a genuine strength as a formal analysis.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation that meaningfully extends or reinterprets the paper's findings.

## Suggestions

1. **Measure energy consumption** or at minimum report spike counts and synaptic operations per forward pass. Without this, the central motivation is an article of faith.
2. **Provide a mechanistic analysis of T-degradation.** This is the paper's most unusual and concerning behavior — standard SNN conversion improves with more timesteps. Understanding why this method reverses that trend is critical.
3. **Add at least one spiking LLM baseline.** The paper positions itself as an SNN method; it needs evaluation against other SNN methods to be properly assessed.
4. **Acknowledge the SNN-to-QANN vs. SNN-to-ANN gap** in Theorem 3. If possible, measure the QANN-to-ANN quantization error term separately.
5. **Test at additional bit-widths and model sizes** to demonstrate the method's generality.

## Score and Decision

**Round 1 bracketing:** I anchored the paper against SNN conversion papers. Weak anchors (score < 3.5) were mostly unrelated (CAN, brain-inspired regularizers, etc.). Middle anchors (3.5–7.5) included SpikeZIP (3.60, Reject), Spatio-Temporal Approximation (7.00, Accept), and When SNN meets ANN (5.75, Reject). Strong anchors (>7.5) were neuroscience papers (grid cells, brain organization) with scores of 8.00 but low topical relevance. The plausible bracket was [3.5, 7.0].

**Round 2 narrowing:** I retrieved additional anchors in the (4.0, 6.5) and (6.0, 8.5) ranges. The most directly comparable anchor is **SpikeLLM** (ZadnlOHsHv, 7.00, Accept), which also introduces spiking to LLMs but provides energy measurements, tests up to 70B parameters, and is accepted. The reviewed paper is clearly weaker than this anchor. Two other relevant anchors: **When SNN meets ANN** (GTzP2GC7NR, 5.75, Reject) — the reviewed paper is comparable in quality but has a more novel pipeline; **SpikeZIP** (u438df0Uce, 3.60, Reject) — the reviewed paper is stronger. **SpikeBERT** (6c4gv0E9sF, 6.33, Reject — mixed 8,8,3) is about SNN for language but uses a different approach (knowledge distillation). The paper sits between the 3.60 and 5.75 anchors, somewhat closer to 5.75 given the genuine novelty of the pipeline, but the major gaps (no energy measurements, unexplained T-degradation, no SNN baselines, limited scope) prevent it from reaching 6+ quality.

**Final score: 5.0.** The paper has a genuinely novel and sensible core idea (starting from an off-the-shelf quantized LLM), and the parameter-efficient calibration is a clear engineering contribution. However, the evaluation does not carry the paper's weight: the central motivation (energy efficiency) is entirely unmeasured, the T-degradation behavior is both unexplained and runs counter to the SNN value proposition, and the absence of any spiking LLM baseline means the contribution cannot be properly situated in the literature it claims to advance. These gaps are structural rather than minor and would require substantial additional work to address.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>